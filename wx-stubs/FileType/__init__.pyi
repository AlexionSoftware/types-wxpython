# -*- coding: utf-8 -*-
from typing import Optional, Any


class MessageParameters:
	""" Class representing message parameters.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def GetFileName(self) -> str:
		""" Return the filename.
		"""

	def GetMimeType(self) -> str:
		""" Return the MIME type.
		"""

	def GetParamValue(self, name: str) -> str:
		""" Overridable method for derived classes. Returns empty string by default.
		"""



