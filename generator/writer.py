# -*- coding: utf-8 -*-
from logging import Logger
import os
from queue import Queue

from .interfaces import ITyping, ITypingClass, ITypingFunction, ITypingLiteral, TypingType
from .extras import EXTRA_KNOWN_ITEMS

SPACER = "    "


class TypingWriter:
	""" Write typing to PYI
	"""
	def __init__(self, logger: Logger) -> None:
		""" Constructor
		"""
		self.logger = logger

	def write(self, typings: Queue[ITyping], moduleImports: dict[str, dict[str, list[str]]]) -> bool:
		""" Write the typing to a pyi
		"""
		# Make a dict per file
		contentPerFileType: dict[str, list[ITyping]] = {}
		self._convertToPerFile(typings, contentPerFileType)

		# Write the files
		for moduleName, typingList in contentPerFileType.items():
			# Find the module imports
			tModuleImport: dict[str, list[str]] = {}
			if moduleName in moduleImports:
				tModuleImport = moduleImports[moduleName]

			# Write the file
			self._writeToFile(moduleName, typingList, tModuleImport)
		return True

	def _convertToPerFile(self, typings: Queue[ITyping], contentPerFileType: dict[str, list[ITyping]]) -> None:
		""" Conver the list to a dict
		"""
		# Walk through all the files
		while not typings.empty():
			# Make the modulename right
			item = typings.get()
			fileName = item["moduleName"]
			if fileName.startswith("wx."):
				fileName = fileName.replace("wx.", "").replace(".", os.sep)
			else:
				fileName = ""

			# Check if the module is in the content
			if fileName not in contentPerFileType:
				contentPerFileType[fileName] = []

			# Check if this is a valid item, the name is not a digit
			if item["name"].isdigit():
				continue

			# Put in the module
			contentPerFileType[fileName].append(item)

	def _writeToFile(self, fileName: str, typings: list[ITyping], moduleImports: dict[str, list[str]]) -> None:
		""" Write to a file
		"""
		# Build the filePath
		if fileName != "":
			filePath = os.path.join("wx-stubs", fileName, "__init__.pyi")
		else:
			filePath = os.path.join("wx-stubs", "__init__.pyi")

		# Create the filedir
		if os.path.exists(os.path.dirname(filePath)) is False:
			# Walk through the paths and create them
			mkPath = ""
			for path in os.path.dirname(filePath).split(os.sep):
				mkPath = os.path.join(mkPath, path)
				if os.path.exists(mkPath) is False:
					# Create the directory
					os.makedirs(mkPath)

					# Create an empty file
					with open(os.path.join(mkPath, "__init__.py"), "w", encoding="utf-8") as fileHandler:
						fileHandler.write("")

		# Combine the data
		data = "# -*- coding: utf-8 -*-\nfrom typing import Any, ContextManager, Optional, Union, TypeAlias\n\n"

		# Add the imports
		for moduleName, importList in moduleImports.items():
			if fileName == "":
				# wx hoofd module
				pass
			elif moduleName.startswith("." + fileName):
				# wx sub module
				moduleName = moduleName[len(fileName) + 1:]
			else:
				moduleName = ("." * (fileName.count(".") + 2)) + moduleName
			data += "from " + moduleName + " import " + ", ".join(importList) + "\n"
		data += "\n"

		# Write the typing
		for item in typings:
			typingStr = self._convertTypingToStr(item, moduleName=fileName)
			data += typingStr + "\n\n"

		# Write the file
		self.logger.info("Writing file: " + filePath)
		with open(filePath, "w", encoding="utf-8") as fileHandler:
			fileHandler.write(data)

	def _convertTypingToStr(self, typing: ITyping, moduleName: str, depth: int = 0) -> str:
		""" Convert the typing dict to a str
		"""
		# Check the type: Literal
		if typing["type"] == TypingType.LITERAL:
			# Build the output
			lTypingObj: ITypingLiteral = typing  # type: ignore
			output = (SPACER * depth) + lTypingObj["name"]
			output += ": " + lTypingObj["returnType"]
			if "docstring" in lTypingObj and lTypingObj["docstring"]:
				output += "  # " + lTypingObj["docstring"].replace("\n", "").replace("\r", "")
			return output

		# Check the type: Alias
		elif typing["type"] == TypingType.ALIAS:
			# Build the output
			lTypingObj: ITypingLiteral = typing  # type: ignore
			output = (SPACER * depth) + lTypingObj["name"]
			output += ": TypeAlias = " + lTypingObj["returnType"]
			if "docstring" in lTypingObj and lTypingObj["docstring"]:
				output += "  # " + lTypingObj["docstring"]
			return output

		# Check the type: Function
		elif typing["type"] == TypingType.FUNCTION:
			# Build the output
			fTypingObj: ITypingFunction = typing  # type: ignore
			output = ""

			# Check if we have a static method
			if "methodType" in fTypingObj and fTypingObj["methodType"]:
				if fTypingObj["methodType"] == "static":
					output += (SPACER * depth) + "@staticmethod\n"

			# Build the signuature
			output += (SPACER * depth) + "def " + fTypingObj["name"] + "(" + fTypingObj["paramStr"] + ") -> " + fTypingObj["returnType"] + ":\n"

			# Add the docstring
			output += (SPACER * (depth + 1)) + '""" ' + fTypingObj["docstring"] + "\n"
			if "source" in fTypingObj and fTypingObj["source"]:
				output += "\n" + (SPACER * (depth + 2)) + "Source: " + fTypingObj["source"] + "\n"

			# Finish
			output += (SPACER * (depth + 1)) + '"""\n'
			return output

		# Check the type: Class
		elif typing["type"] == TypingType.CLASS:
			# Build the output
			cTypingObj: ITypingClass = typing  # type: ignore

			# Add the class name
			output = (SPACER * depth) + "class " + cTypingObj["name"]

			# Set the parent class
			if cTypingObj["superClass"]:
				superClasses = ",".join([sc.split(".")[-1] for sc in cTypingObj["superClass"]])
				output += "(" + superClasses + ")"
			output += ":\n"

			# Add the docstring
			output += (SPACER * (depth + 1)) + '""" ' + cTypingObj["docstring"] + "\n"
			if "source" in cTypingObj and cTypingObj["source"]:
				output += "\n" + (SPACER * (depth + 2)) + "Source: " + cTypingObj["source"] + "\n"
			output += (SPACER * (depth + 1)) + '"""\n'

			# Check all the functions
			for functionTyping in cTypingObj["functions"]:
				output += self._convertTypingToStr(functionTyping, moduleName, depth+1) + "\n"

			# Check if the extras have any functions
			fullClassName = cTypingObj["moduleName"] + "." + cTypingObj["name"]
			for extraItem in EXTRA_KNOWN_ITEMS:
				if extraItem["type"] == TypingType.FUNCTION:
					functionItem: ITypingFunction = extraItem  # type: ignore
					if "className" in functionItem and functionItem["className"] == fullClassName:
						output += self._convertTypingToStr(extraItem, moduleName, depth+1) + "\n"

			# Check all the properties
			# Properties are added after functions to avoid conflicts between
			# propeties names and class names.
			for propertyTyping in cTypingObj["properties"]:
				output += self._convertTypingToStr(propertyTyping, moduleName, depth+1) + "\n"
			if len(cTypingObj["properties"]) > 0:
				output += "\n"

			return output
		return ""
