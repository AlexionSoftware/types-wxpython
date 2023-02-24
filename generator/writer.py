# -*- coding: utf-8 -*-
from logging import Logger
import os
from queue import Queue

from .interfaces import ITyping, ITypingClass, ITypingFunction, ITypingLiteral

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
		contentPerFileType: dict[str, dict[str, str]] = {}
		self._convertToPerFile(typings, contentPerFileType)

		# Write the files
		for moduleName, typings in contentPerFileType.items():
			# Write the file
			self._writeToFile(moduleName, typings)

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
			os.makedirs(os.path.dirname(filePath))

		# Combine the data
		data = "# -*- coding: utf-8 -*-\nfrom typing import Any, Optional, Union\n\n\n"
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
		if typing["type"] == "literal":
			typingObj: ITypingLiteral = typing
			output = typingObj["name"]
			output += ": " + typingObj["returnType"]
			if "docstring" in typingObj and typingObj["docstring"]:
				output += "  # " + typingObj["docstring"]
			return output

		# Check the type: Function
		elif typing["type"] == "function":
			typingObj: ITypingFunction = typing
			output = ""
			if "methodType" in typingObj and typingObj["methodType"]:
				if typingObj["methodType"] == "static":
					output += (SPACER * depth) + "@staticmethod\n"
			output += (SPACER * depth) + "def " + typingObj["name"] + "(" + typingObj["paramStr"] +  ") -> " + typingObj["returnType"] + ":\n"
			output += (SPACER * (depth + 1)) + '""" ' + typingObj["docstring"] + "\n"
			if "source" in typingObj and typingObj["source"]:
				output += "\n" + (SPACER * (depth + 2)) + "Source: " + typingObj["source"] + "\n"
			output += (SPACER * (depth + 1)) + '"""\n'
			return output

		# Check the type: Class
		elif typing["type"] == "class":
			typingObj: ITypingClass = typing
			output = (SPACER * depth) + "class " + typingObj["name"]
			if typingObj["superClass"]:
				output += "(" + ",".join(typingObj["superClass"]) +  ")"
			output += ":\n"
			output += (SPACER * (depth + 1)) + '""" ' + typingObj["docstring"] + "\n"
			if "source" in typingObj and typingObj["source"]:
				output += "\n" + (SPACER * (depth + 2)) + "Source: " + typingObj["source"] + "\n"
			output += (SPACER * (depth + 1)) + '"""\n'

			# Check all the functions
			for functionTyping in typingObj["functions"]:
				output += self._convertTypingToStr(functionTyping, depth+1) + "\n"
			return output
