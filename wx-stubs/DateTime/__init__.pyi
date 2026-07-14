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
    def Make(offset: int) -> 'TimeZone':
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
    hour: int  # A public C++ attribute of type int. Hours since midnight in 0..23 range.
    mday: int  # A public C++ attribute of type int. Day of the month in 1..31 range.
    min: int  # A public C++ attribute of type int. Minutes in 0..59 range.
    mon: Month  # A public C++ attribute of type DateTime.Month. Month, as an enumerated constant.
    msec: int  # A public C++ attribute of type int. Number of milliseconds.
    sec: int  # A public C++ attribute of type int. Seconds in 0..59 (60 with leap seconds) range.
    yday: int  # A public C++ attribute of type int. Day of the year in 0..365 range.
    year: int  # A public C++ attribute of type int. Year.


class Country(int):  # Enum
    pass

Country_Unknown: Country
Country_Default: Country
Country_WesternEurope_Start: Country
Country_EEC: Country
France: Country
Germany: Country
UK: Country
Country_WesternEurope_End: Country
Russia: Country
USA: Country

class WeekFlags(int):  # Enum
    pass

Default_First: WeekFlags
Monday_First: WeekFlags
Sunday_First: WeekFlags

class NameFlags(int):  # Enum
    pass

Name_Full: NameFlags
Name_Abbr: NameFlags

class WeekDay(int):  # Enum
    pass

Sun: WeekDay
Mon: WeekDay
Tue: WeekDay
Wed: WeekDay
Thu: WeekDay
Fri: WeekDay
Sat: WeekDay
Inv_WeekDay: WeekDay

class Month(int):  # Enum
    pass

Jan: Month
Feb: Month
Mar: Month
Apr: Month
May: Month
Jun: Month
Jul: Month
Aug: Month
Sep: Month
Oct: Month
Nov: Month
Dec: Month
Inv_Month: Month

class Year(int):  # Enum, partial
    pass

Inv_Year: Year

class Calendar(int):  # Enum
    pass

Gregorian: Calendar
Julian: Calendar

class TZ(int):  # Enum
    pass

Local: TZ
GMT_12: TZ
GMT_11: TZ
GMT_10: TZ
GMT_9: TZ
GMT_8: TZ
GMT_7: TZ
GMT_6: TZ
GMT_5: TZ
GMT_4: TZ
GMT_3: TZ
GMT_2: TZ
GMT_1: TZ
GMT0: TZ
GMT1: TZ
GMT2: TZ
GMT3: TZ
GMT4: TZ
GMT5: TZ
GMT6: TZ
GMT7: TZ
GMT8: TZ
GMT9: TZ
GMT10: TZ
GMT11: TZ
GMT12: TZ
GMT13: TZ
WET: TZ
WEST: TZ
CET: TZ
CEST: TZ
EET: TZ
EEST: TZ
MSK: TZ
MSD: TZ
AST: TZ
ADT: TZ
EST: TZ
EDT: TZ
CST: TZ
CDT: TZ
MST: TZ
MDT: TZ
PST: TZ
PDT: TZ
HST: TZ
AKST: TZ
AKDT: TZ
A_WST: TZ
A_CST: TZ
A_EST: TZ
A_ESST: TZ
NZST: TZ
NZDT: TZ
UTC: TZ
