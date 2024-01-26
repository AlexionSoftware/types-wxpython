# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class TimeCtrl(BaseMaskedTextCtrl):
    """ Masked control providing several time formats and manipulation of time values.

        Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
    """
    def __init__(self, parent, id=-1, value = '00:00:00', pos = wx.DefaultPosition, size = wx.DefaultSize, fmt24hr=False, spinButton = None, style = wx.TE_PROCESS_TAB, validator = wx.DefaultValidator, name = "time", **kwargs) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def BindSpinButton(self, sb: SpinButton) -> None:
        """ This function binds an externally created spin button to the control,
so that up/down events from the button automatically change the control.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def ChangeValue(self, value: Any) -> None:
        """ Validating ChangeValue function for time values:
This function will do dynamic type checking on the value argument,
and convert DateTime, mxDateTime, or 12/24 format time string
into the appropriate format string for the control.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetBounds(self, as_string = False) -> None:
        """ This function returns a two-tuple (min,max), indicating the
current bounds of the control.  Each value can be None if
that bound is not set.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetFormat(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetMax(self, as_string = False) -> None:
        """ Gets the minimum value of the control.
If None, it will return None.  Otherwise it will return
the current minimum bound on the control, as a DateTime
by default, or as a string if as_string argument is True.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetMin(self, as_string = False) -> None:
        """ Gets the minimum value of the control.
If None, it will return None.  Otherwise it will return
the current minimum bound on the control, as a DateTime
by default, or as a string if as_string argument is True.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetMxDateTime(self, value=None) -> None:
        """ Returns the value of the control as an mx.DateTime, with the date
portion set to January 1, 1970.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetValue(self, as_wxDateTime = False, as_mxDateTime = False, as_wxTimeSpan = False, as_mxDateTimeDelta = False) -> None:
        """ This function returns the value of the display as a string by default,
but supports return as a DateTime, mx.DateTime, TimeSpan,
or mx.DateTimeDelta, if requested.
(Evaluated in the order aboveâ first one wins!)

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetWxDateTime(self, value=None) -> None:
        """ This function is the conversion engine for TimeCtrl; it takes
one of the following types:

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def IsInBounds(self, value=None) -> None:
        """ Returns True if no value is specified and the current value
of the control falls within the current bounds.  As the clock
is a âcircleâ, both minimum and maximum bounds must be set for
a value to ever be considered âout of boundsâ.  This function can
also be called with a value to see if that value would fall within
the current bounds of the given control.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def IsLimited(self) -> None:
        """ Returns True if the control is currently limiting the
value to fall within any current bounds.  Note: can
be set even if there are no current bounds.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def IsValid(self, value: Any) -> None:
        """ Can be used to determine if a given value would be a legal and
in-bounds value for the control.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetBounds(self, min=None, max=None) -> None:
        """ This function is a convenience function for setting the min and max
values at the same time.  The function only applies the maximum bound
if setting the minimum bound is successful, and returns True only if both operations succeed.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetFormat(self, format) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetInsertionPoint(self, pos) -> None:
        """ This override records the specified position and associated cell before
calling base classâ function.  This is necessary to handle the optional
spin button, because the insertion point is lost when the focus shifts
to the spin button.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetLimited(self, limited: boolean) -> None:
        """ If called with a value of True, this function will cause the control
to limit the value to fall within the bounds currently specified.
If the controlâs value currently exceeds the bounds, it will then
be limited accordingly.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetMax(self, max: Optional[int]=None) -> None:
        """ Sets the maximum value of the control. If a value of None
is provided, then the control will have no explicit maximum value.
If the value specified is less than the current minimum value, then
the function returns False and the maximum will not change from its
current setting. On success, the function returns True.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetMin(self, min: Optional[int]=None) -> None:
        """ Sets the minimum value of the control.  If a value of None
is provided, then the control will have no explicit minimum value.
If the value specified is greater than the current maximum value,
then the function returns 0 and the minimum will not change from
its current setting.  On success, the function returns 1.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetMxDateTime(self, mxdt) -> None:
        """ Because SetValue can take an mx.DateTime, (if DateTime is importable),
this is now just an alias.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetParameters(self, **kwargs) -> None:
        """ Function providing access to the parameters governing TimeCtrl display
and bounds.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetSelection(self, sel_start, sel_to) -> None:
        """ SetSelection(from_, to_)

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetValue(self, value: Any) -> None:
        """ Validating SetValue function for time values:
This function will do dynamic type checking on the value argument,
and convert DateTime, mxDateTime, or 12/24 format time string
into the appropriate format string for the control.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetWxDateTime(self, wxdt) -> None:
        """ Because SetValue can take a DateTime, this is now just an alias.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """



class TimeCtrlAccessorsMixin:
    """ Defines TimeCtrlâs list of attributes having their own Get/Set functions,
ignoring those in the base class that make no sense for a time control.

        Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrlAccessorsMixin.html
    """


class TimeUpdatedEvent(PyCommandEvent):
    """ Used to fire an EVT_TIMEUPDATE event whenever the value in a TimeCtrl changes.

        Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeUpdatedEvent.html
    """
    def __init__(self, id, value ='12:00:00 AM') -> None:
        """ Initialize self.  See help(type(self)) for accurate signature.

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeUpdatedEvent.html
        """

    def GetValue(self) -> None:
        """ Retrieve the value of the time control at the time this event was generated

            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeUpdatedEvent.html
        """



