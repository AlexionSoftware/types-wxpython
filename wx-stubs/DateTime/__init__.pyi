# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union

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



class Tm:
    """ Contains broken down date-time representation.

        Source: https://docs.wxpython.org/wx.DateTime.Tm.html
    """
    def GetWeekDay(self) -> 'DateTime.WeekDay':
        """ Return the week day corresponding to this date.

            Source: https://docs.wxpython.org/wx.DateTime.Tm.html
        """

    def IsValid(self) -> bool:
        """ Check if the given date/time is valid (in Gregorian calendar).

            Source: https://docs.wxpython.org/wx.DateTime.Tm.html
        """



