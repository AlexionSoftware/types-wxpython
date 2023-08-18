# -*- coding: utf-8 -*-
from logging import Logger
from queue import Queue
from typing import Union

from .interfaces import ITyping, TypingType, ITypingClass, ITypingFunction, ITypingLiteral


class Ensurerer:
	""" Make sure the typing is correct
	"""
	def __init__(self, logger: Logger) -> None:
		""" Constructor
		"""
		# Remember the logger
		self.logger = logger

		# Dicts
		self.typingDict: dict[str, ITyping] = {}
		self.aliasDict: dict[str, ITyping] = {}
		self.literalDict: dict[str, ITyping] = {}
		self.moduleImports: dict[str, dict[str, list[str]]] = {}

	def ensure(self, typings: Queue[ITyping]) -> bool:
		""" Make sure the typing is correct
		"""
		# Load all the typings in a dict
		while not typings.empty():
			typing = typings.get()
			self.typingDict[typing["moduleName"] + "." + typing["name"]] = typing

		# Find all the ALIASes
		for typing in self.typingDict.values():
			if typing["type"] == TypingType.ALIAS:
				self.aliasDict[typing["moduleName"] + "." + typing["name"][1:]] = typing

		# Find all the LITERALs
		for typing in self.typingDict.values():
			if typing["type"] == TypingType.LITERAL:
				self.literalDict[typing["moduleName"] + "." + typing["name"]] = typing

		# Walk through all the typings
		for key, typing in self.typingDict.items():
			# Check the override
			self._overrideItemData(typing)

			# Ensure the typing
			self.typingDict[key] = self._ensureTyping(typing)

		# Load everything back into the queue
		for typing in self.typingDict.values():
			typings.put(typing)

		return True

	def _ensureTyping(self, typing: ITyping) -> ITyping:
		""" Make sure the typing is correct
		"""
		# Check the type: Class
		if typing["type"] == TypingType.CLASS:
			typingObjc: ITypingClass = typing  # type: ignore

			# Ensure superclass import
			if typingObjc["superClass"]:
				self._ensureSuperClass(typingObjc)

			# Put all the literals back into the ensureTyping
			for literal in typingObjc["properties"]:
				self._ensureTyping(literal)

			# Put all the functions back into the ensureTyping
			for function in typingObjc["functions"]:
				self._ensureTyping(function)

		# Check the type: Literal
		elif typing["type"] == TypingType.LITERAL:
			typingObjl: ITypingLiteral = typing  # type: ignore

			# Find the return type
			typingObjl["returnType"] = self._ensureReturnType(typingObjl)

		# Check the type: Function
		elif typing["type"] == TypingType.FUNCTION:
			typingObjf: ITypingFunction = typing  # type: ignore

			# Find the return type
			typingObjf["returnType"] = self._ensureReturnType(typingObjf)

			# Find the param types
			for key, value in typingObjf["params"].items():
				typingObjf["params"][key] = self._ensureParamType(typingObjf, value)

		return typing

	def _ensureReturnType(self, typingObjl: Union[ITypingLiteral, ITypingFunction]) -> str:
		""" Make sure the return type is correct
		"""
		# Opzoeken van de module
		orgItem = typingObjl.copy()
		moduleName = typingObjl["moduleName"]
		if moduleName == "":
			moduleName = "wx"
		moduleParts = moduleName.split(".")
		if len(moduleParts) > 1:
			moduleName = ".".join(moduleParts[:-1])

		# Check if there is a dot in the return type
		if "." in typingObjl["returnType"] and typingObjl["returnType"].startswith("wx."):
			# Only use the last part
			typingObjl["returnType"] = typingObjl["returnType"].split(".")[-1]

		# Check if type is a Union
		if typingObjl["returnType"].startswith("Union[") or typingObjl["returnType"].startswith("Optional[") or typingObjl["returnType"].startswith("list[") or typingObjl["returnType"].startswith("tuple["):
			# Dont need to do anything
			return typingObjl["returnType"]

		# Check of het een build-in is
		if typingObjl["returnType"] in ["'int'", "int", "str", "bool", "float", "tuple", "tuple", "None", "Any", "list"]:
			# Fix the typing
			return typingObjl["returnType"].replace("'", "")

		# Check if the last part of the module name is equal to the first part of the returntype
		if len(typingObjl["returnType"].replace("'", "").split(".")) > 1 and moduleName.split(".")[-1] == typingObjl["returnType"].replace("'", "").split(".")[0]:
			# Remove the first part of the return type
			typingObjl["returnType"] = ".".join(typingObjl["returnType"].replace("'", "").split(".")[1:])

		# Check if the return type is a alias
		returnType = moduleName + "." + typingObjl["returnType"].replace("'", "")
		if returnType in self.aliasDict:
			typingObjl["returnType"] = "'_" + typingObjl["returnType"][1:]

		# Check if the typing is being ended with a '
		if typingObjl["returnType"][0] == "'" and typingObjl["returnType"][-1] != "'":
			typingObjl["returnType"] += "'"
		if typingObjl["returnType"][0] != "'" and typingObjl["returnType"][-1] == "'":
			typingObjl["returnType"] = "'" + typingObjl["returnType"]

		# Check if the return type exists
		if returnType not in self.typingDict:
			# Check how many dots are in the return type
			if len(returnType.split(".")) > 2:
				# Check if the typing existing one dot higher
				for i in range(0, len(returnType.split("."))):
					testReturnType = ".".join(returnType.split(".")[:(i * -1)]) + "." + returnType.split(".")[-1]
					if testReturnType in self.typingDict:
						returnType = testReturnType
						break
		# Check if the return type exists
		if returnType not in self.typingDict:
			# We can't find it
			self.logger.error("ReturnType '%s' does not exist in %s.%s - %s" % (typingObjl["returnType"], typingObjl["moduleName"], typingObjl["name"], orgItem))
			raise KeyError(returnType)

		# Return the type
		if returnType.startswith("wx."):
			# Check if the return type is in a different module
			if moduleName != ".".join(returnType.split(".")[:-1]):
				# Add the import to the module
				fileModuleName = moduleName.replace("wx", "")
				fileModuleName = fileModuleName[1:] if fileModuleName.startswith(".") else fileModuleName
				importModuleName = (".".join(returnType.split(".")[:-1])).replace("wx", "")
				importItemName = returnType.split(".")[-1].replace("wx.", "")
				if fileModuleName not in self.moduleImports:
					self.moduleImports[fileModuleName] = {}
				if importModuleName not in self.moduleImports[fileModuleName]:
					self.moduleImports[fileModuleName][importModuleName] = []
				if importItemName not in self.moduleImports[fileModuleName][importModuleName]:
					self.moduleImports[fileModuleName][importModuleName].append(importItemName)

			# Give the back
			return "'" + returnType.split(".")[-1] + "'"
		return returnType

	def _ensureParamType(self, typingObjl: ITypingFunction, paramType: str) -> str:
		""" Make sure the return type is correct
		"""
		# Opzoeken van de module
		moduleName = typingObjl["moduleName"]
		moduleParts = moduleName.split(".")
		if len(moduleParts) > 1 and moduleParts[0] == "wx":
			moduleName = ".".join(moduleParts[:-1])

		# Check if there is a dot in the return type
		if "." in paramType and paramType.startswith("wx."):
			# Only use the last part
			paramType = paramType.split(".")[-1]

		# Check if type is a Union
		if paramType.startswith("Union[") or paramType.startswith("Optional[") or paramType.startswith("list["):
			# Dont need to do anything
			return paramType

		# Check of het een build-in is
		if paramType in ["'int'", "int", "str", "bool", "float", "tuple", "tuple", "None", "Any", "list"]:
			# Fix the typing
			return paramType.replace("'", "")

		# Check if the last part of the module name is equal to the first part of the returntype
		if len(paramType.replace("'", "").split(".")) > 1 and moduleName.split(".")[-1] == paramType.replace("'", "").split(".")[0]:
			# Remove the first part of the return type
			paramType = ".".join(paramType.replace("'", "").split(".")[1:])

		# Check if the return type is a alias
		returnType = moduleName + "." + paramType.replace("'", "")
		if returnType in self.aliasDict:
			paramType = "'_" + paramType[1:]

		# Check if the typing is being ended with a '
		if paramType[0] == "'" and paramType[-1] != "'":
			paramType += "'"
		if paramType[0] != "'" and paramType[-1] == "'":
			paramType = "'" + paramType

		# Check if the return type exists
		if returnType not in self.typingDict:
			# Check how many dots are in the return type
			if len(returnType.split(".")) > 2:
				# Check if the typing existing one dot higher
				for i in range(0, len(returnType.split("."))):
					testReturnType = ".".join(returnType.split(".")[:(i * -1)]) + "." + returnType.split(".")[-1]
					if testReturnType in self.typingDict:
						returnType = testReturnType
						break

		# Check if the return type exists
		if returnType not in self.typingDict:
			# We can't find it
			self.logger.error("Param type '%s' does not exist in %s.%s" % (paramType, typingObjl["moduleName"], typingObjl["name"]))
			raise KeyError(returnType)

		# Return the type
		if returnType.startswith("wx."):
			return "'" + returnType[3:] + "'"
		return returnType

	def _overrideItemData(self, typing: ITyping) -> None:
		""" Override the item data
		"""
		from .overrides import OVERRIDES

		# Generate the full module name
		fullModuleName = typing["moduleName"] + "." + typing["name"]

		# Check if we have an override
		if fullModuleName in OVERRIDES:
			# Override the info
			typing.update(OVERRIDES[fullModuleName])  # type: ignore

		# Check if the type is a class
		if typing["type"] == TypingType.CLASS:
			# Check the overrides for all the functions
			cTypeObject: ITypingClass = typing  # type: ignore
			for functionTyping in cTypeObject["functions"]:
				self._overrideItemData(functionTyping)
			for literalTyping in cTypeObject["properties"]:
				self._overrideItemData(literalTyping)

	def _ensureSuperClass(self, typingObjc: ITypingClass) -> None:
		""" Ensure the superclass
		"""
		# Check if we have an superclass
		moduleName = typingObjc["moduleName"]
		superClasses = typingObjc["superClass"]
		if superClasses:
			# Walk through all the superclasses
			for superClassName in superClasses:
				if superClassName.startswith("wx."):
					# Check if the return type is in a different module
					if moduleName != ".".join(superClassName.split(".")[:-1]):
						# Add the import to the module
						fileModuleName = moduleName.replace("wx", "")
						fileModuleName = fileModuleName[1:] if fileModuleName.startswith(".") else fileModuleName
						importModuleName = (".".join(superClassName.split(".")[:-1])).replace("wx", "")
						importItemName = superClassName.split(".")[-1].replace("wx.", "")
						if fileModuleName not in self.moduleImports:
							self.moduleImports[fileModuleName] = {}
						if importModuleName not in self.moduleImports[fileModuleName]:
							self.moduleImports[fileModuleName][importModuleName] = []
						if importItemName not in self.moduleImports[fileModuleName][importModuleName]:
							self.moduleImports[fileModuleName][importModuleName].append(importItemName)

	def getModuleImports(self) -> dict[str, dict[str, list[str]]]:
		""" Get the module imports
		"""
		return self.moduleImports
