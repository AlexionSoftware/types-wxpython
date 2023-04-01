# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class TimeZone:
    """ Class representing a time zone.

        Source: https://docs.wxpython.org/wx.DateTime.TimeZone.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.DateTime.TimeZone.html
        """

    def GetOffset(self) -> int:
        """ Return the offset of this time zone from UTC, in seconds.

            Source: https://docs.wxpython.org/wx.DateTime.TimeZone.html
        """

    def IsLocal(self) -> bool:
        """ Return True if this is the local time zone.

            Source: https://docs.wxpython.org/wx.DateTime.TimeZone.html
        """

    @staticmethod
    def Make(offset: int) -> 'DateTime.TimeZone':
        """ Create a time zone with the given offset in seconds.

            Source: https://docs.wxpython.org/wx.DateTime.TimeZone.html
        """

    Offset: int  # See GetOffset



class Tm:
    """ Contains broken down date-time representation.

        Source: https://docs.wxpython.org/wx.DateTime.Tm.html
    """
    def GetWeekDay(self) -> 'WeekDay':
        """ Return the week day corresponding to this date.

            Source: https://docs.wxpython.org/wx.DateTime.Tm.html
        """

    def IsValid(self) -> bool:
        """ Check if the given date/time is valid (in Gregorian calendar).

            Source: https://docs.wxpython.org/wx.DateTime.Tm.html
        """

    WeekDay: 'WeekDay'  # See GetWeekDay
    hour: Any  # A public C++ attribute of type int. Hours since midnight in 0..23 range.
    mday: Any  # A public C++ attribute of type int. Day of the month in 1..31 range.
    min: Any  # A public C++ attribute of type int. Minutes in 0..59 range.
    mon: Any  # A public C++ attribute of type DateTime.Month. Month, as an enumerated constant.
    msec: Any  # A public C++ attribute of type int. Number of milliseconds.
    sec: Any  # A public C++ attribute of type int. Seconds in 0..59 (60 with leap seconds) range.
    yday: Any  # A public C++ attribute of type int. Day of the year in 0..365 range.
    year: Any  # A public C++ attribute of type int. Year.



Country: TypeAlias = int  # Enumeration

WeekFlags: TypeAlias = int  # Enumeration

Month: TypeAlias = Any  # Enumeration

TZ: TypeAlias = Any

