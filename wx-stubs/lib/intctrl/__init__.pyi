# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class IntCtrl(TextCtrl):
    """ This class provides a control that takes and returns integers as
value, and provides bounds support and optional value limiting.

        Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
    """
    def __init__(self, parent, id=-1, value = 0, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, validator = wx.DefaultValidator, name = "integer", min=None, max=None, limited = 0, allow_none = 0, allow_long = 0, default_color = wx.NullColour, oob_color = wx.RED) -> None:
        """ Default constructor

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def ChangeValue(self, value: int) -> None:
        """ Change the value without sending an EVT_TEXT event.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def Cut(self) -> None:
        """ Override the TextCtrl.Cut function, with our own
that does validation.  Will result in a value of 0
if entire contents of control are removed.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def GetBounds(self) -> None:
        """ This function returns a two-tuple (min,max), indicating the
current bounds of the control.  Each value can be None if
that bound is not set.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def GetColors(self) -> None:
        """ Returns a tuple of (default_color, oob_color), indicating
the current color settings for the control.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def GetMax(self) -> None:
        """ Gets the maximum value of the control.  It will return the current
maximum integer, or None if not specified.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def GetMin(self) -> None:
        """ Gets the minimum value of the control.  It will return the current
minimum integer, or None if not specified.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def GetValue(self) -> Optional[int]:
        """ Returns the current integer (long) value of the control.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def IsInBounds(self, value: Optional[int]=None) -> None:
        """ Returns True if no value is specified and the current value
of the control falls within the current bounds.  This function can
also be called with a value to see if that value would fall within
the current bounds of the given control.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def IsLimited(self) -> None:
        """ Returns True if the control is currently limiting the
value to fall within the current bounds.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def IsLongAllowed(self) -> None:
        """ Is a long value allowed.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def IsNoneAllowed(self) -> None:
        """ Is a None value allowed.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def OnText(self, event) -> None:
        """ Handles an event indicating that the text controlâs value
has changed, and issue EVT_INT event.
NOTE: using wx.TextCtrl.SetValue() to change the controlâs
contents from within a wx.EVT_CHAR handler can cause double
text events.  So we check for actual changes to the text
before passing the events on.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def Paste(self) -> None:
        """ Override the TextCtrl.Paste function, with our own
that does validation.  Will raise ValueError if not a
valid integerizable value.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetBounds(self, min=None, max=None) -> None:
        """ This function is a convenience function for setting the min and max
values at the same time.  The function only applies the maximum bound
if setting the minimum bound is successful, and returns True only if both operations succeed.
..note:

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetColors(self, default_color=wx.BLACK, oob_color=wx.RED) -> None:
        """ Tells the control what colors to use for normal and out-of-bounds
values.  If the value currently exceeds the bounds, it will be
recolored accordingly.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetLimited(self, limited: bool) -> None:
        """ If called with a value of True, this function will cause the control
to limit the value to fall within the bounds currently specified.
If the controlâs value currently exceeds the bounds, it will then
be limited accordingly.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetLongAllowed(self, allow_long: bool) -> None:
        """ Change the behavior of the validation code, allowing control
to have a long value or not, as appropriate.  If the value
of the control is currently long, and allow_long is 0, the
value of the control will be adjusted to fall within the
size of an integer type, at either the sys.maxsize or -sys.maxsize-1,
for positive and negative values, respectively.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetMax(self, max: Optional[int]=None) -> None:
        """ Sets the maximum value of the control. If a value of None
is provided, then the control will have no explicit maximum value.
If the value specified is less than the current minimum value, then
the function returns 0 and the maximum will not change from its
current setting. On success, the function returns 1.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetMin(self, min: Optional[int]=None) -> None:
        """ Sets the minimum value of the control.  If a value of None
is provided, then the control will have no explicit minimum value.
If the value specified is greater than the current maximum value,
then the function returns 0 and the minimum will not change from
its current setting.  On success, the function returns 1.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetNoneAllowed(self, allow_none: bool) -> None:
        """ Change the behavior of the validation code, allowing control
to have a value of None or not, as appropriate.  If the value
of the control is currently None, and allow_none is 0, the
value of the control will be set to the minimum value of the
control, or 0 if no lower bound is set.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetValue(self, value: int) -> None:
        """ Sets the value of the control to the integer value specified.
The resulting actual value of the control may be altered to
conform with the bounds set on the control if limited,
or colored if not limited but the value is out-of-bounds.
A ValueError exception will be raised if an invalid value
is specified.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    Limited: Any  # Returns True if the control is currently limiting thevalue to fall within the current bounds.
    LongAllowed: Any  # Is a long value allowed.
    Max: Any  # Gets the maximum value of the control.  It will return the currentmaximum integer, or None if not specified.
    Min: Any  # Gets the minimum value of the control.  It will return the currentminimum integer, or None if not specified.
    NoneAllowed: Any  # Is a None value allowed.
    Value: Any  # Returns the current integer (long) value of the control.



class IntUpdatedEvent(PyCommandEvent):
    """ Event sent from the IntCtrl when control is updated.

        Source: https://docs.wxpython.org/wx.lib.intctrl.IntUpdatedEvent.html
    """
    def __init__(self, id, value = 0, object=None) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntUpdatedEvent.html
        """

    def GetValue(self) -> None:
        """ Retrieve the value of the control at the time
this event was generated.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntUpdatedEvent.html
        """



class IntValidator(Validator):
    """ Validator class used with IntCtrl handles all validation of
input prior to changing the value of the underlying TextCtrl.

        Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
    """
    def __init__(self) -> None:
        """ Standard constructor

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
        """

    def Clone(self) -> None:
        """ Standard cloner

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
        """

    def OnChar(self, event) -> None:
        """ Validates keystrokes to make sure the resulting value will a legal
value.  Erasing the value causes it to be set to 0, with the value
selected, so it can be replaced.  Similarly, replacing the value
with a â-â sign causes the value to become -1, with the value
selected.  Leading zeros are removed if introduced by selection,
and are prevented from being inserted.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
        """

    def TransferFromWindow(self) -> None:
        """ Transfer data from window to validator.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
        """

    def TransferToWindow(self) -> None:
        """ Transfer data from validator to window.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
        """

    def Validate(self, window) -> None:
        """ Because each operation on the control is vetted as itâs made,
the value of the control is always valid.

            Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
        """



EVT_INT: int

WXK_CTRL_V: int

WXK_CTRL_X: int

