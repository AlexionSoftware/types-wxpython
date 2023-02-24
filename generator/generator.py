# -*- coding: utf-8 -*-
import os
import re
from queue import Queue
from typing import Optional

import requests
from bs4 import BeautifulSoup, Tag


# Some starting points to find the data
BASE_URL = "https://docs.wxpython.org/"
BASE_INDEX_URLS: list[str] = [
	"https://docs.wxpython.org/wx.1moduleindex.html",
	"https://docs.wxpython.org/wx.ribbon.1moduleindex.html",
	"https://docs.wxpython.org/wx.lib.buttons.html",
]
EXTRA_CLASS_URLS: list[str] = [
	"https://docs.wxpython.org/wx.FontFamily.enumeration.html",
	"https://docs.wxpython.org/wx.FontWeight.enumeration.html",
	"https://docs.wxpython.org/wx.StockCursor.enumeration.html",
	"https://docs.wxpython.org/wx.StandardID.enumeration.html",
	"https://docs.wxpython.org/wx.functions.html",
]
SPACER = "    "
EXTRA_TYPING = """
GROW: int  # Synonym for wx.EXPAND\n
RA_HORIZONTAL: int  # Synonym of wx.HORIZONTAL\n
RA_VERTICAL: int  # Synonym of wx.VERTICAL\n
NORMAL: int\n
DEFAULT: int\n
"""


class DocumentationGenerator:
	""" Generate the documentation
	"""

	def generate(self) -> None:
		""" Generate
		"""
		# Create a Queue with classes
		self.classQueue: Queue[str] = Queue()

		# Remember the whole file
		self.typings: dict[str, str] = {}
		self.foundTypingUrls: list[str] = []

		# Add the extra classes to the queue
		# This classes are not found by default
		# So we add them manually
		#
		for classUrl in EXTRA_CLASS_URLS:
			self.classQueue.put(classUrl)

		# Check each index
		for url in BASE_INDEX_URLS:
			print(url)
			self._processIndex(url)

			# Process all the classes
			while not self.classQueue.empty():
				# Retrieve the next item
				classUrl = self.classQueue.get()
				print(classUrl)

				# Process the data
				self._processClassApi(classUrl)

		# Make a dict per file
		contentPerFileType: dict[str, dict[str, str]] = {}
		for itemKey in self.typings.keys():
			# Check if this has one .
			if itemKey.count(".") == 0:
				# Use the default file
				fileName = "__init__.pyi"
			else:
				# There are more dots
				pathParts = itemKey.split(".")[:-1]
				fileName = os.path.join("\\".join(pathParts), "__init__.pyi")

			# Connect class to the right file
			if fileName not in contentPerFileType:
				contentPerFileType[fileName] = {}
			contentPerFileType[fileName][itemKey] = self.typings[itemKey]

		# Save all the files
		for fileName in contentPerFileType:
			# Build the filePath
			filePath = os.path.join("wx-stubs", fileName)

			# Create the filedir
			if os.path.exists(os.path.dirname(filePath)) is False:
				os.makedirs(os.path.dirname(filePath))

			# Combine the data
			data = "# -*- coding: utf-8 -*-\nfrom typing import Any, Optional, Union\n\n\n"
			# Check if this is the base class
			if fileName == "__init__.pyi":
				data += EXTRA_TYPING
			for value in contentPerFileType[fileName].values():
				data += value + "\n\n"

			# Write the file
			with open(filePath, "w", encoding="utf-8") as fileHandler:
				fileHandler.write(data)

	def _processIndex(self, url: str) -> None:
		""" Process the index file with all the classes
		"""
		# Retrieve the page
		r = requests.get(url)
		if r.status_code != 200:
			print("This page '%s' doesnt work!" % url)
			return

		# Process the HTML
		soup = BeautifulSoup(r.text, 'html.parser')
		indexTable = soup.find(id="class-summary")
		if indexTable is None:
			indexTable = soup.find(id="class-summary-classes-summary")

		# Check each row
		for aTag in indexTable.find_all("a", class_="reference"):
			self.classQueue.put(aTag["href"])

	def _processClassApi(self, url: str) -> None:
		""" Process a Class API
		"""
		# Check if we already know this
		if url in self.foundTypingUrls:
			return
		if url.endswith(".png"):
			return

		# Retrieve the page
		r = requests.get(BASE_URL + url)
		if r.status_code != 200:
			print("This page '%s' doesnt work!" % url)
			return

		# Process the HTML
		soup = BeautifulSoup(r.text, 'html.parser')

		# Find the name of the class
		className = soup.find("title").get_text()
		className = className[:className.find(" ")][3:]

		# Find the place with all the classes
		apiTableElem = soup.find(id="api-class-api")
		if apiTableElem is not None:
			self._processTypingClassMethod(className, soup, apiTableElem)

		# Check if there are literals
		literals = soup.find_all(class_="literal")
		if len(literals) > 0:
			self._processLiterals(className, soup)

		# Remeber we already processed this one
		self.foundTypingUrls.append(url)

	def _processLiterals(self, className: str, soup: Tag) -> None:
		""" Process literals in a table
		"""
		# Remeber the class
		typingOutput = ""
		if className in self.typings:
			typingOutput = self.typings[className]

		# Check every literal
		literals: list[Tag] = soup.find_all(class_="literal")
		for literalElem in literals:
			# Check if this is a literal
			if "py" in literalElem["class"]:
				continue

			# Get the name of the literal
			literalName = literalElem.get_text().strip()
			if literalName.startswith("wx."):
				# Remove the wx.
				literalName = literalName[3:]

				# Check if there is a * in the name
				if "*" in literalName:
					continue

				# Save the literal
				typingOutput += literalName + ": int\n"

		# Save the output
		self.typings[className] = typingOutput

	def _processTypingClassMethod(self, className: str, soup: Tag, apiTableElem: Tag) -> None:
		""" Process a class with methods
		"""
		# Find the parent class
		parentClass = self._findParentClass(soup)

		# Find the real name for the class
		classSubName = className.split(".")[-1]

		# Build the typing
		typingOutput = "class %s" % classSubName
		if parentClass is not None:
			typingOutput += "(%s):\n" % parentClass
		else:
			typingOutput += ":\n"

		# Find the API
		apiTable = apiTableElem.find("dd")

		# The first p is the class def
		ps: list[Tag] = apiTable.find_all("p")
		if len(ps) > 0:
			if "constructors" in ps[0].get_text():
				typingOutput += SPACER + '""" ' + ps[1].get_text() + "\n" + SPACER + '"""\n'
			else:
				typingOutput += SPACER + '""" ' + ps[0].get_text() + "\n" + SPACER + '"""\n'

		# Find all the methods
		methodTags: list[Tag] = apiTable.find_all("dl", class_="method")
		for methodTag in methodTags:
			# Find the info
			methodName: str = methodTag.find_all("dt", limit=1)[0].get_text()[:-2].strip()
			methodDef = ""
			if len(methodTag.find_all("p", limit=1)) > 0:
				methodDef: str = methodTag.find_all("p", limit=1)[0].get_text().strip()
			params: dict[str, str] = {}
			returnType: str = "None"

			# Check if this is a real thing
			if methodName.startswith("~"):
				continue

			# Find the parts
			fieldListElem = methodTag.find("dl", class_="field-list")
			if fieldListElem:
				parts: list[Tag] = fieldListElem.children
				nextPart = ""
				for part in parts:
					# Check if header
					if part.name == "dt":
						# Check if the next part will be parameters
						if part.get_text() == "Parameters":
							nextPart = "params"

						# Check if the next part will be return type
						elif part.get_text() == "Return type":
							nextPart = "return"

						else:
							# We dont know what this is
							nextPart = ""

					# Check if content
					elif part.name == "dd":
						# Check if the last header was params
						if nextPart == "params":
							# Check if there is a list of params
							if part.find("ul"):
								# Find all the params
								paramElems = part.find_all("li", recursive=False)
								for paramElem in paramElems:
									# Retrieve the information
									paramName = paramElem.find("strong").get_text().strip()
									paramType = "Any"
									if paramElem.find("em"):
										paramType = self._ensureTyping(paramElem.find("em").get_text().strip())
									elif paramElem.find("span"):
										paramType = self._ensureTyping(paramElem.find("span").get_text().strip())
									params[paramName] = paramType

							# Check if there is a single param
							elif part.find("p"):
								# Retrieve information
								paramName: str = part.find_all("strong", limit=1)[0].get_text().strip()
								paramType = "Any"
								if len(part.find_all("em", limit=1)) > 0:
									paramType: str = self._ensureTyping(part.find_all("em", limit=1)[0].get_text().strip())
								elif len(part.find_all("span", limit=1)) > 0:
									paramType: str = self._ensureTyping(part.find_all("span", limit=1)[0].get_text().strip())

								params[paramName] = paramType

						# Check if the last header was return
						elif nextPart == "return":
							# Retrieve the return type
							returnType = self._ensureTyping(part.get_text().strip(), typingType="return")

			# Check if static
			if methodName.startswith("static"):
				typingOutput += SPACER + "@staticmethod\n"
				methodName = methodName[7:]

			# Build the param list
			paramList = methodName[methodName.find("(") + 1: -1]
			methodName = methodName[:methodName.find("(")]

			# Check if there is an function
			# This is a mistake in the documentation
			if "(" in paramList:
				# We dont know what to do, so just stop
				paramList = "*args, **kwargs"
				break

			# Check if there is a star
			if paramList != "*args, **kwargs":
				for paramKey, paramType in params.items():
					# Check if the key is optional
					if "%s=None" % paramKey in paramList:
						paramType = "Optional[%s]" % paramType

					# Find the key
					search = re.search(paramKey + r"\b", paramList)
					if search:
						paramIndex = search.span()[1]
						paramList = paramList[:paramIndex] + (": %s" % paramType) + paramList[paramIndex:]
					else:
						continue

			# Build the method
			typingOutput += SPACER + "def %s(%s) -> %s:\n" % (methodName, paramList, returnType)
			typingOutput += SPACER + SPACER + '""" ' + methodDef + '\n' + SPACER + SPACER + '"""\n\n'

		# Check for events
		typingOutput += self._processClassWindowStyles(soup)

		# Check for styles
		typingOutput += self._processClassWindowEvents(soup)

		# Save the output
		self.typings[className] = typingOutput

	def _processClassWindowStyles(self, soup: Tag) -> str:
		""" Find window classes
		"""
		# Build the typing output
		typingOutput = ""

		# Find the window styles
		styleElem = soup.find(id="styles-window-styles")
		if styleElem:
			ulElem = styleElem.find("ul")
			if ulElem:
				liElems: list[Tag] = ulElem.find_all("li")
				for liElem in liElems:
					# Find the name of the element
					styleName = liElem.get_text().strip()
					styleName = styleName.replace(":", ": int  # ")
					if styleName.startswith("wx."):
						styleName = styleName[3:]

					# Check if there is an enter
					if "\n" in styleName:
						styleName = styleName[:styleName.find("\n")]

					# Add to the output
					typingOutput += styleName + "\n"

		return typingOutput

	def _processClassWindowEvents(self, soup: Tag) -> str:
		""" Find window events
		"""
		# Build the typing output
		typingOutput = ""

		# Find the window styles
		eventElem = soup.find(id="events-events-emitted-by-this-class")
		if eventElem:
			ulElem = eventElem.find("ul")
			if ulElem:
				liElems: list[Tag] = ulElem.find_all("li")
				for liElem in liElems:
					# Find the name of the element
					eventName = liElem.get_text().strip()
					eventName = eventName.replace(":", ": int  # ")
					if eventName.startswith("wx."):
						eventName = eventName[3:]

					# Check if there is a *
					if "*" in eventName:
						continue

					# Check if there is an enter
					if "\n" in eventName:
						eventName = eventName[:eventName.find("\n")]

					# Add to the output
					typingOutput += eventName + "\n"

		return typingOutput

	def _findParentClass(self, soup: Tag) -> Optional[str]:
		""" Find the parent class
		"""
		# Make room for the parent class
		parentClass: Optional[str] = None

		# Find the hierarchy element
		hierarchTable = soup.find(id="class-hierarchy-class-hierarchy")
		if hierarchTable:
			# Find the map element
			hierarchMap = hierarchTable.find("map")
			if hierarchMap:
				# Find all the area, each area is a subclass
				hierarchItems = hierarchMap.find_all("area")

				# Check if there are more than 1, the first one is this class
				if len(hierarchItems) > 1:
					# Find the parent class name
					firstParentElement = hierarchItems[1]
					parentClass = firstParentElement["href"].replace(".html", "")

					# Check if the class starts with wx.
					if parentClass.startswith("wx."):
						parentClass = parentClass[3:]

					# Check if there is a < in it
					if "<" in parentClass:
						# Remove this part
						parentClass = parentClass[:parentClass.find("<")]

					# Now that we found the first one, lets check if there are more
					index = 2
					while index < len(hierarchItems):
						# Retrieve the parent
						nextParentElement = hierarchItems[index]

						# Find the coords
						nextCoords = nextParentElement["coords"].split(",")
						firstCoords = firstParentElement["coords"].split(",")

						# Check if it is at the same height
						if nextCoords[1] == firstCoords[1]:
							# This is a subclass
							nextParentName = nextParentElement["href"].replace(".html", "")

							# Check if the class starts with wx.
							if nextParentName.startswith("wx."):
								nextParentName = nextParentName[3:]

							# Check if there is a < in it
							if "<" in nextParentName:
								# Remove this part
								nextParentName = nextParentName[:nextParentName.find("<")]

							# Add to the parentclass
							parentClass += ", " + nextParentName

						# Check the next parent
						index += 1

		return parentClass

	def _ensureTyping(self, typing: str, typingType: str = "param") -> str:
		""" Make sure the typing exists
		"""
		# Make a list of all posible typing problems
		typingMap = {
			"list of strings": "list[str]",
			"list of integers": "list[int]",
			"list of floats": "list[float]",
			"string": "str",
			"long": "int",
			"True": "bool",
			"False": "bool",
			"a Python object": "Any",
			"wx.EventCategory": "int",
			"EventCategory": "int",
			"wx.EventType": "int",
			"EventType": "int",
			"wx.AccStatus": "int",
			"AccStatus": "int",
			"PyObject": "Any",
			"wx.PyObject": "Any",
			"wx.Direction": "int",
			"Direction": "int",
			"wx.ArtID": "int",
			"ArtID": "int",
			"wx.Alignment": "int",
			"Alignment": "int",
			"wx.WindowVariant": "int",
			"WindowVariant": "int",
			"DefaultPosition": "Union[tuple[int, int], wx.Position]",
			"DefaultSize": "Union[tuple[int, int], wx.Size]",
		}
		for typingKey, typingReplace in typingMap.items():
			if typingKey in typing:
				typing = typingReplace

		# Check if this is a param
		if typingType == "param":
			# Change Size to Union
			if typing == "wx.Size":
				typing = "Union[tuple[int, int], 'Size']"
			elif typing == "wx.Position":
				typing = "Union[tuple[int, int], 'Position']"
			elif typing == "wx.Colour":
				typing = "Union[int, str, 'Colour']"

		# Check if this is a return
		if typingType == "return":
			# Check if Object, this is usally a Window
			if typing == "wx.Object":
				typing = "wx.Window"

		# Check if there is a weird thing
		if "[" in typing and "]" not in typing:
			typing = "Any"

		# Check if WX is in the list
		if typing.startswith("wx"):
			typing = "'" + typing[3:] + "'"
		return typing
