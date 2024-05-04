# -*- coding: utf-8 -*-
import sys
from enum import Enum
from typing import Optional, TypedDict

if sys.version_info >= (3,11,0):
	from typing import NotRequired
else:
	from typing import Optional as NotRequired


class TypingType(Enum):
	""" Type of typings
	"""
	LITERAL = "literal"
	FUNCTION = "function"
	CLASS = "class"
	ALIAS = "alias"


class ITyping(TypedDict):
	""" Base voor all items
	"""
	type: TypingType
	name: str
	moduleName: str
	docstring: str
	source: str


class ITypingFunction(ITyping):
	""" Interface for classes
	"""
	className: NotRequired[str]
	methodType: str
	params: dict[str, str]
	paramStr: str
	returnType: str


class ITypingClass(ITyping):
	""" Interface for Classes
	"""
	superClass: Optional[list[str]]
	functions: list[ITypingFunction]
	properties: list['ITypingLiteral']


class ITypingLiteral(ITyping):
	""" Interface for literals
	"""
	returnType: str
