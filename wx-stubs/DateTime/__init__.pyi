# -*- coding: utf-8 -*-
from typing import Optional, Any


class TimeZone:
	""" Class representing a time zone.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def GetOffset(self) -> long:
		""" Return the offset of this time zone from UTC, in seconds.
		"""

	def IsLocal(self) -> bool:
		""" Return True if this is the local time zone.
		"""

	@staticmethod
	def Make(offset: long) -> 'DateTime.TimeZone':
		""" Create a time zone with the given offset in seconds.
		"""



class Tm:
	""" Contains broken down date-time representation.
	"""
	def GetWeekDay(self) -> 'DateTime.WeekDay':
		""" Return the week day corresponding to this date.
		"""

	def IsValid(self) -> bool:
		""" Check if the given date/time is valid (in Gregorian calendar).
		"""



