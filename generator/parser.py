# -*- coding: utf-8 -*-
from logging import Logger
import re
from queue import Queue
from typing import Optional

import requests
from bs4 import BeautifulSoup, Tag

from .interfaces import ITyping, ITypingClass, ITypingFunction, ITypingLiteral


BASE_URL = "https://docs.wxpython.org/"


class Parser:
	""" Parse the information to ITyping
	"""
	def __init__(self, fetchQueue: Queue, logger: Logger) -> None:
		""" Constructor
		"""
		self.foundTypingUrls: list[str] = []
		self.fetchQueue = fetchQueue
		self.logger = logger

	def processClassApi(self, url: str) -> Optional[list[ITyping]]:
		""" Process a Class API
		"""
		# Check if we already know this
		if url in self.foundTypingUrls:
			self.logger.warn("Already found this url: '%s'" % url)
			return None
		if not url.endswith(".html"):
			self.logger.error("Cannot process this url: This is not HTML '%s'" % url)
			return None

		# Retrieve the page
		fullUrl = BASE_URL + url
		r = requests.get(fullUrl)
		if r.status_code != 200:
			self.logger.error("This page '%s' doesnt work!" % url)
			return None

		# Process the HTML
		soup = BeautifulSoup(r.text, 'html.parser')
		if soup is None:
			self.logger.error("This page '%s' doesnt work!" % url)
			return None

		# Find all the reference to other classes
		self._findInternalReference(soup)

		# Find the name of the class
		titleElem = soup.find("title")
		if titleElem is None:
			self.logger.error("This page '%s' doesnt work!" % url)
			return None
		classFullName = titleElem.get_text()
		classFullName = classFullName[:classFullName.find(" ")]
		className = classFullName.split(".")[-1]
		moduleName = ".".join(classFullName.split(".")[:-1])

		# Check if there is an module name found
		if className == "wx":
			className = ""
			moduleName = "wx"

		# Build the list with items
		result: list[ITyping] = []

		# Find the place with all the classes
		apiTableElem = soup.find(id="api-class-api")
		if apiTableElem is not None:
			# Build the class
			classType: ITypingClass = {
				"type": TypingType.CLASS,
				"name": className,
				"moduleName": moduleName,
				"source": fullUrl,
			}

			# Find the superclass
			classType["superClass"] = self._findParentClass(soup)

			# Find the class doc
			classType["docstring"] = self._processClassDocstring(apiTableElem)

			# Fill the class
			functions = self._processTypingMethod(classFullName, soup, apiTableElem, source=fullUrl)
			classType["functions"] = functions

			# Add to the list
			result.append(classType)

		# Check for functions
		functions = self._processTypingMethod(moduleName, soup, soup, methodIdName="function", source=fullUrl)
		result.extend(functions)

		# Check for events
		styles = self._processClassWindowStyles(moduleName, soup)
		result.extend(styles)

		# Check for styles
		events = self._processClassWindowEvents(moduleName, soup)
		result.extend(events)

		# Check if there are literals
		literals = soup.find_all(class_="literal")
		if len(literals) > 0:
			literals = self._processLiterals(moduleName, soup)
			result.extend(literals)

		# Remember we already processed this one
		self.foundTypingUrls.append(url)

		return result

	def _processLiterals(self, moduleName: str, soup: Tag) -> list[ITypingLiteral]:
		""" Process literals in a table
		"""
		# Make the output
		result: list[ITypingLiteral] = []

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
				literalName = literalName.split(".")[-1]

				# Check if there is a * in the name
				if "*" in literalName:
					continue

				# Make the item
				literalObj: ITypingLiteral = {
					"type": TypingType.LITERAL,
					"name": literalName,
					"moduleName": moduleName,
					"returnType": "int",
				}
				result.append(literalObj)

		return result

	def _processClassDocstring(self, apiTableElem: Tag) -> str:
		""" Find the class docstring
		"""
		# Find the API
		apiTable = apiTableElem.find("dd")

		# The first p is the class def
		ps: list[Tag] = apiTable.find_all("p")
		if len(ps) > 0:
			if "constructors" in ps[0].get_text():
				return ps[1].get_text()
			else:
				return ps[0].get_text()
		return ""

	def _processTypingMethod(self, className: str, soup: Tag, apiTableElem: Tag, methodIdName: str = "method", source: str = "") -> list[ITypingFunction]:
		""" Process a class with methods
		"""
		# Make a list
		result: list[ITypingFunction] = []

		# Find all the methods
		methodTags: list[Tag] = apiTableElem.find_all("dl", class_=methodIdName)
		for methodTag in methodTags:
			# Create the method
			methodType: ITypingFunction = {
				"type": TypingType.FUNCTION,
				"moduleName": className,
				"source": source,
			}

			# Find the name
			methodName: str = methodTag.find_all("dt", limit=1)[0].get_text()[:-2].strip()
			methodType["name"] = methodName

			# Find the docstring
			methodType["docstring"] = ""
			if len(methodTag.find_all("p", limit=1)) > 0:
				methodType["docstring"] = methodTag.find_all("p", limit=1)[0].get_text().strip()

			# Set the params
			methodType["params"] = {}

			# Set the return type
			methodType["returnType"] = "None"

			# Check if this is an alias
			if methodType["docstring"].startswith("Alias"):
				# Change the return type
				# We should find the other method and copy that
				#
				methodType["returnType"] = "Any"

			# Check if this is a real thing
			if methodName.startswith("~"):
				continue

			# Check if this is a __eq__ or __ne__ method
			if methodName.startswith("__eq__") or methodName.startswith("__ne__"):
				# Make sure the compare is there
				methodName = methodName[:6] + "(self, item: Any)"
				methodType["name"] = methodName
				methodType["returnType"] = "bool"

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
									methodType["params"][paramName] = paramType

							# Check if there is a single param
							elif part.find("p"):
								# Retrieve information
								paramName: str = part.find_all("strong", limit=1)[0].get_text().strip()
								paramType = "Any"
								if len(part.find_all("em", limit=1)) > 0:
									paramType: str = self._ensureTyping(part.find_all("em", limit=1)[0].get_text().strip())
								elif len(part.find_all("span", limit=1)) > 0:
									paramType: str = self._ensureTyping(part.find_all("span", limit=1)[0].get_text().strip())

								methodType["params"][paramName] = paramType

						# Check if the last header was return
						elif nextPart == "return":
							# Retrieve the return type
							methodType["returnType"] = self._ensureTyping(part.get_text().strip(), typingType="return")

			# Check if static
			if methodName.startswith("static"):
				methodType["methodType"] = "static"
				methodName = methodType["name"][7:]
				methodType["name"] = methodName

			# Build the param list
			methodType["paramStr"] = methodName[methodName.find("(") + 1: -1]
			methodName = methodName[:methodName.find("(")]
			methodType["name"] = methodName

			# Make sure the name doesnt start with wx
			if methodType["name"].startswith("wx"):
				methodType["name"] = methodType["name"].split(".")[-1]

			# Check if there is an function
			# This is a mistake in the documentation
			if "(" in methodType["paramStr"]:
				# We dont know what to do, so just stop
				methodType["paramStr"] = "*args, **kwargs"

			# Check if there is a star
			if methodType["paramStr"] != "*args, **kwargs" and ":" not in methodType["paramStr"]:
				for paramKey, paramType in methodType["params"].items():
					# Check if the key is optional
					if "%s=None" % paramKey in methodType["paramStr"]:
						paramType = "Optional[%s]" % paramType

					# Find the key
					search = re.search(paramKey + r"\b", methodType["paramStr"])
					if search:
						paramIndex = search.span()[1]
						methodType["paramStr"] = methodType["paramStr"][:paramIndex] + (": %s" % paramType) + methodType["paramStr"][paramIndex:]
					else:
						continue

			# Check if we found typing for the params
			if "*" not in methodType["paramStr"] and methodType["paramStr"] != "self" and ":" not in methodType["paramStr"]:
				# We should be able to find all the params
				self.logger.error("Could not find all the params for %s.%s" % (methodType["moduleName"], methodType["name"]))

			# Add the method to the list
			result.append(methodType)

		# Save the output
		return result

	def _processClassWindowStyles(self, moduleName: str, soup: Tag) -> list[ITypingLiteral]:
		""" Find window classes
		"""
		# Build the typing output
		result = []

		# Find the window styles
		styleElem = soup.find(id="styles-window-styles")
		if styleElem:
			ulElem = styleElem.find("ul")
			if ulElem:
				liElems: list[Tag] = ulElem.find_all("li")
				for liElem in liElems:
					# Find the name of the element
					styleName = liElem.get_text().strip()
					styleDef = ""

					# Check if there is a definition
					if ":" in styleName:
						styleDef = styleName[(styleName.find(":") + 1):]
						styleName = styleName[:styleName.find(":")]

					# Check if there is a wx prefix
					if styleName.startswith("wx."):
						styleName = styleName.split(".")[-1]

					# Check if there is an enter
					if "\n" in styleName:
						styleName = styleName[:styleName.find("\n")]
					if "\n" in styleDef:
						styleDef = styleDef[:styleDef.find("\n")]

					# Add to the output
					literalObj: ITypingLiteral = {
						"type": TypingType.LITERAL,
						"name": styleName,
						"moduleName": moduleName,
						"returnType": "int",
						"docstring": styleDef.strip(),
					}
					result.append(literalObj)

		return result

	def _processClassWindowEvents(self, moduleName: str, soup: Tag) -> list[ITypingLiteral]:
		""" Find window events
		"""
		# Build the typing output
		result: list[ITypingLiteral] = []

		# Find the window styles
		eventElem = soup.find(id="events-events-emitted-by-this-class")
		if eventElem:
			ulElem = eventElem.find("ul")
			if ulElem:
				liElems: list[Tag] = ulElem.find_all("li")
				for liElem in liElems:
					# Find the name of the element
					eventName = liElem.get_text().strip()
					eventDef = ""
					if ":" in eventName:
						eventDef = eventName[(eventName.find(":") + 1):]
						eventName = eventName[:eventName.find(":")]
					if eventName.startswith(moduleName):
						eventName = eventName.split(".")[-1]

					# Check if there is a *
					if "*" in eventName:
						continue

					# Check if there is an enter
					if "\n" in eventName:
						eventName = eventName[:eventName.find("\n")]
					if "\n" in eventDef:
						eventDef = eventDef[:eventDef.find("\n")]

					# Add to the output
					literalObj: ITypingLiteral = {
						"type": TypingType.LITERAL,
						"name": eventName,
						"moduleName": moduleName,
						"returnType": "int",
						"docstring": eventDef.strip(),
					}
					result.append(literalObj)

		return result

	def _findParentClass(self, soup: Tag) -> Optional[list[str]]:
		""" Find the parent class
		"""
		# Make room for the parent class
		parentClass: list[str] = []

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
					parentClassStr: str = firstParentElement["href"].replace(".html", "")

					# Check if the class starts with wx.
					if parentClassStr.startswith("wx."):
						parentClassStr = parentClassStr.split(".")[-1]

					# Check if there is a < in it
					if "<" in parentClassStr:
						# Remove this part
						parentClassStr = parentClassStr[:parentClassStr.find("<")]

					# Add the class to the list
					parentClass.append(parentClassStr)

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
							nextParentName: str = nextParentElement["href"].replace(".html", "")

							# Check if the class starts with wx.
							if nextParentName.startswith("wx."):
								nextParentName = nextParentName.split(".")[-1]

							# Check if there is a < in it
							if "<" in nextParentName:
								# Remove this part
								nextParentName = nextParentName[:nextParentName.find("<")]

							# Add the class to the list
							parentClass.append(nextParentName)

						# Check the next parent
						index += 1

		# Check if we would anything
		if len(parentClass) > 0:
			return parentClass
		return None

	def _ensureTyping(self, typing: str, typingType: str = "param") -> str:
		""" Make sure the typing exists
		"""
		# Make a list of all posible typing problems
		typingMap = {
			"list of strings": "list[str]",
			"list of integers": "list[int]",
			"list of floats": "list[float]",
			"String": "str",
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
			"wx.FontFamily": "int",
			"FontFamily": "int",
			"wx.FontStyle": "int",
			"FontStyle": "int",
			"wx.FontEncoding": "int",
			"FontEncoding": "int",
			"wx.FontWeight": "int",
			"FontWeight": "int",
			"DefaultPosition": "Union[tuple[int, int], wx.Position]",
			"DefaultSize": "Union[tuple[int, int], wx.Size]",
			"WindowID": "int",
			"wx.WindowID": "int",
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
			elif typing == "wx.Point":
				typing = "Union[tuple[int, int], 'Point']"
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

	def _findInternalReference(self, soup: Tag) -> None:
		""" Search for internal references
		"""
		# Find all the a tags
		aTags = soup.find_all("a", class_="internal")

		# Walk through all the a tags and add them to the queue
		for aTag in aTags:
			# Make sure it is a internal link
			href: str = aTag["href"]
			if href.startswith("#"):
				continue
			if href.startswith("http"):
				continue

			# Use the href untill the #
			if "#" in href:
				href = href[:href.find("#")]

			# Add to the queue
			self.fetchQueue.put(href)
