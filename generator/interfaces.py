# -*- coding: utf-8 -*-
from typing import Optional, TypedDict

class ITyping(TypedDict):
	""" Base voor all items
	"""
	type: str
	name: str
	moduleName: str
	docstring: str


class ITypingFunction(ITyping):
	""" Interface for classes
	"""
	type: str
	methodType: str
	params: dict[str, str]
	paramStr: str
	returnType: str


class ITypingClass(ITyping):
	""" Interface for Classes
	"""
	superClass: Optional[list[str]]
	functions: list[ITypingFunction]


class ITypingLiteral(ITyping):
	""" Interface for literals
	"""
