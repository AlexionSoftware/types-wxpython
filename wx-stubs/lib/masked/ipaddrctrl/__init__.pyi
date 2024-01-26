# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class IpAddrCtrl(BaseMaskedTextCtrl,IpAddrCtrlAccessorsMixin):
    """ This class is a particular type of MaskedTextCtrl that accepts
and understands the semantics of IP addresses, reformats input
as you move from field to field, and accepts â.â as a navigation
character, so that typing an IP address can be done naturally.

        Source: https://docs.wxpython.org/wx.lib.masked.ipaddrctrl.IpAddrCtrl.html
    """
    def __init__(self, parent, id=-1, value = '', pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TE_PROCESS_TAB, validator = wx.DefaultValidator, name = 'IpAddrCtrl', setupEventHandling = True, **kwargs) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.masked.ipaddrctrl.IpAddrCtrl.html
        """

    def GetAddress(self) -> None:
        """ Returns the control value, with any spaces removed.

            Source: https://docs.wxpython.org/wx.lib.masked.ipaddrctrl.IpAddrCtrl.html
        """

    def OnDot(self, event) -> None:
        """ Defines what action to take when the â.â character is typed in the
control.  By default, the current field is right-justified, and the
cursor is placed in the next field.

            Source: https://docs.wxpython.org/wx.lib.masked.ipaddrctrl.IpAddrCtrl.html
        """

    def SetValue(self, value: str) -> None:
        """ Takes a string value, validates it for a valid IP address,
splits it into an array of 4 fields, justifies it
appropriately, and inserts it into the control.
Invalid values will raise a ValueError exception.

            Source: https://docs.wxpython.org/wx.lib.masked.ipaddrctrl.IpAddrCtrl.html
        """



class IpAddrCtrlAccessorsMixin:
    """ Defines IpAddrCtrlâs list of attributes having their own
Get/Set functions, exposing only those that make sense for
an IP address control.

        Source: https://docs.wxpython.org/wx.lib.masked.ipaddrctrl.IpAddrCtrlAccessorsMixin.html
    """


