# -*- coding: utf-8 -*-
from enum import Enum
from typing import Optional, TypedDict


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
