# -*- coding: utf-8 -*-
from logging import Logger
import os
from queue import Queue

from .interfaces import ITyping, ITypingClass, ITypingFunction, ITypingLiteral, TypingType

SPACER = "    "


class TypingWriter:
	""" Write typing to PYI
	"""
	def __init__(self, logger: Logger) -> None:
		""" Constructor
		"""
		self.logger = logger

	def write(self, typings: Queue[ITyping]) -> bool:
		""" Write the typing to a pyi
		"""
		# Make a dict per file
		contentPerFileType: dict[str, list[ITyping]] = {}
		self._convertToPerFile(typings, contentPerFileType)

		# Write the files
		for moduleName, typingList in contentPerFileType.items():
			# Write the file
			self._writeToFile(moduleName, typingList)
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

			# Check if we should override something in the item
			self._overrideItemData(item)

			# Put in the module
			contentPerFileType[fileName].append(item)

	def _writeToFile(self, fileName: str, typings: list[ITyping]) -> None:
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
		data = "# -*- coding: utf-8 -*-\nfrom typing import Any, ContextManager, Optional, Union, TypeAlias\n\n\n"
		for item in typings:
			typingStr = self._convertTypingToStr(item)
			data += typingStr + "\n\n"

		# Write the file
		self.logger.info("Writing file: " + filePath)
		with open(filePath, "w", encoding="utf-8") as fileHandler:
			fileHandler.write(data)

	def _convertTypingToStr(self, typing: ITyping, depth: int = 0) -> str:
		""" Convert the typing dict to a str
		"""
		# Check the type: Literal
		if typing["type"] == TypingType.LITERAL:
			lTypingObj: ITypingLiteral = typing  # type: ignore
			output = (SPACER * depth) + lTypingObj["name"]
			output += ": " + lTypingObj["returnType"]
			if "docstring" in lTypingObj and lTypingObj["docstring"]:
				output += "  # " + lTypingObj["docstring"]
			return output

		# Check the type: Alias
		elif typing["type"] == TypingType.ALIAS:
			lTypingObj: ITypingLiteral = typing  # type: ignore
			output = (SPACER * depth) + lTypingObj["name"]
			output += ": TypeAlias = " + lTypingObj["returnType"]
			if "docstring" in lTypingObj and lTypingObj["docstring"]:
				output += "  # " + lTypingObj["docstring"]
			return output

		# Check the type: Function
		elif typing["type"] == TypingType.FUNCTION:
			fTypingObj: ITypingFunction = typing  # type: ignore
			output = ""
			if "methodType" in fTypingObj and fTypingObj["methodType"]:
				if fTypingObj["methodType"] == "static":
					output += (SPACER * depth) + "@staticmethod\n"
			output += (SPACER * depth) + "def " + fTypingObj["name"] + "(" + fTypingObj["paramStr"] + ") -> " + fTypingObj["returnType"] + ":\n"
			output += (SPACER * (depth + 1)) + '""" ' + fTypingObj["docstring"] + "\n"
			if "source" in fTypingObj and fTypingObj["source"]:
				output += "\n" + (SPACER * (depth + 2)) + "Source: " + fTypingObj["source"] + "\n"
			output += (SPACER * (depth + 1)) + '"""\n'
			return output

		# Check the type: Class
		elif typing["type"] == TypingType.CLASS:
			cTypingObj: ITypingClass = typing  # type: ignore
			output = (SPACER * depth) + "class " + cTypingObj["name"]
			if cTypingObj["superClass"]:
				output += "(" + ",".join(cTypingObj["superClass"]) + ")"
			output += ":\n"
			output += (SPACER * (depth + 1)) + '""" ' + cTypingObj["docstring"] + "\n"
			if "source" in cTypingObj and cTypingObj["source"]:
				output += "\n" + (SPACER * (depth + 2)) + "Source: " + cTypingObj["source"] + "\n"
			output += (SPACER * (depth + 1)) + '"""\n'

			# Check all the properties
			for propertyTyping in cTypingObj["properties"]:
				output += self._convertTypingToStr(propertyTyping, depth+1) + "\n"
			if len(cTypingObj["properties"]) > 0:
				output += "\n"

			# Check all the functions
			for functionTyping in cTypingObj["functions"]:
				output += self._convertTypingToStr(functionTyping, depth+1) + "\n"

			return output
		return ""

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
