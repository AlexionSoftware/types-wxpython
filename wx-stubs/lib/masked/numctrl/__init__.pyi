# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class NumCtrl(BaseMaskedTextCtrl,NumCtrlAccessorsMixin):
    """ Masked edit control supporting ânativeâ numeric values, ie. .SetValue(3), for
example, and supporting a variety of formatting options, including automatic
rounding specifiable precision, grouping and decimal place characters, etc.

        Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
    """
    def __init__(self, parent, id=-1, value = 0, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TE_PROCESS_TAB, validator = wx.DefaultValidator, name = "masked.num", **kwargs) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def ChangeValue(self, value: int) -> None:
        """ Sets the value of the control to the value specified.
The resulting actual value of the control may be altered to
conform with the bounds set on the control if limited,
or colored if not limited but the value is out-of-bounds.
A ValueError exception will be raised if an invalid value
is specified.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetAllowNegative(self) -> None:
        """ (For regularization of property accessors)

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetAllowNone(self) -> None:
        """ (For regularization of property accessors)

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetAutoSize(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetBounds(self) -> None:
        """ This function returns a two-tuple (min,max), indicating the
current bounds of the control.  Each value can be None if
that bound is not set.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetDecimalChar(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetFraction(self, candidate=None) -> None:
        """ Returns the fractional portion of the value as a float. If there is no
fractional portion, the value returned will be 0.0.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetFractionWidth(self) -> None:
        """ Get the fraction width.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetGroupChar(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetGroupDigits(self) -> None:
        """ (For regularization of property accessors)

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetIntegerWidth(self) -> None:
        """ Get the integer width.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetLimited(self) -> None:
        """ (For regularization of property accessors)

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetLimitOnFieldChange(self) -> None:
        """ (For regularization of property accessors)

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetMax(self) -> None:
        """ Gets the maximum value of the control.  It will return the current
maximum integer, or None if not specified.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetMin(self) -> None:
        """ Gets the lower bound value of the control.  It will return
None if not specified.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetSelectOnEntry(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetValue(self) -> None:
        """ Returns the current numeric value of the control.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def IsGroupingAllowed(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def IsInBounds(self, value: Optional[Any]=None) -> None:
        """ Returns True if no value is specified and the current value
of the control falls within the current bounds.  This function can
also be called with a value to see if that value would fall within
the current bounds of the given control.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def IsLimited(self) -> None:
        """ Returns True if the control is currently limiting the
value to fall within the current bounds.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def IsLimitedOnFieldChange(self) -> None:
        """ Returns True if the control is currently limiting the
value to fall within the current bounds.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def IsNegativeAllowed(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def IsNoneAllowed(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def OnTextChange(self, event) -> None:
        """ Handles an event indicating that the text controlâs value
has changed, and issue EVT_NUM event.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetAllowNegative(self, value) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetAllowNone(self, allow_none: boolean) -> None:
        """ Change the behavior of the validation code, allowing control
to have a value of None or not, as appropriate.  If the value
of the control is currently None, and allow_none is False, the
value of the control will be set to the minimum value of the
control, or 0 if no lower bound is set.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetAutoSize(self, value) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetBounds(self, min=None, max=None) -> None:
        """ This function is a convenience function for setting the min and max
values at the same time.  The function only applies the maximum bound
if setting the minimum bound is successful, and returns True only if both operations succeed.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetDecimalChar(self, value) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetFractionWidth(self, value: int) -> None:
        """ Set the fraction width of the control

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetGroupChar(self, value) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetGroupDigits(self, value) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetIntegerWidth(self, value: int) -> None:
        """ Set the integer width of the control

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetLimited(self, limited: boolean) -> None:
        """ If called with a value of True, this function will cause the control
to limit the value to fall within the bounds currently specified.
If the controlâs value currently exceeds the bounds, it will then
be limited accordingly.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetLimitOnFieldChange(self, limit: boolean) -> None:
        """ If called with a value of True, this function will cause the control
to prevent navigation out of the current field if its value is out-of-bounds,
and limit the value to fall within the bounds currently specified if the
control loses focus.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetMax(self, max: Optional[int]=None) -> None:
        """ Sets the maximum value of the control. If a value of None
is provided, then the control will have no explicit maximum value.
If the value specified is less than the current minimum value, then
the function returns False and the maximum will not change from its
current setting. On success, the function returns True.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetMin(self, min: Optional[int]=None) -> None:
        """ Sets the minimum value of the control.  If a value of None
is provided, then the control will have no explicit minimum value.
If the value specified is greater than the current maximum value,
then the function returns False and the minimum will not change from
its current setting.  On success, the function returns True.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetParameters(self, **kwargs) -> None:
        """ This function is used to initialize and reconfigure the control.
See TimeCtrl module overview for available
parameters.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetSelectOnEntry(self, value) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetValue(self, value: int) -> None:
        """ Sets the value of the control to the value specified.
The resulting actual value of the control may be altered to
conform with the bounds set on the control if limited,
or colored if not limited but the value is out-of-bounds.
A ValueError exception will be raised if an invalid value
is specified.

            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """



class NumCtrlAccessorsMixin:
    """ Defines masked.NumCtrlâs list of attributes having their own
Get/Set functions, ignoring those that make no sense for
a numeric control.

        Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrlAccessorsMixin.html
    """


