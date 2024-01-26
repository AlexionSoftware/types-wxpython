# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class MaskedEditMixin:
    """ This class allows us to abstract the masked edit functionality that could
be associated with any text entry control. (eg. wx.TextCtrl, wx.ComboBox, etc.)
It forms the basis for all of the lib.masked controls.

        Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
    """
    def __init__(self, name = 'MaskedEdit', **kwargs) -> None:
        """ This is the âconstructorâ for setting up the mixin variable parameters for the composite class.

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def ClearValue(self) -> None:
        """ Blanks the current control value by replacing it with the default value.

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def ClearValueAlt(self) -> None:
        """ Blanks the current control value by replacing it with the default value.
Using ChangeValue, so not to fire a change event

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def GetCtrlParameter(self, paramname) -> None:
        """ Routine for retrieving the value of any given parameter

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def GetFieldParameter(self, field_index, paramname) -> None:
        """ Routine provided for getting a parameter of an individual field.

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def GetMaskParameter(self, paramname) -> None:
        """ old name for the GetCtrlParameters function  (DEPRECATED)

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def GetPlainValue(self, candidate=None) -> None:
        """ Returns controlâs value stripped of the template text.
plainvalue = MaskedEditMixin.GetPlainValue()

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def IsDefault(self, value=None) -> None:
        """ Returns True if the value specified (or the value of the control if not specified)
is equal to the default value.

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def IsEmpty(self, value=None) -> None:
        """ Returns True if control is equal to an empty value.
(Empty means all editable positions in the template == fillChar.)

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def IsValid(self, value=None) -> None:
        """ Indicates whether the value specified (or the current value of the control
if not specified) is considered valid.

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def SetBackgroundColour(self, colour) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def SetCtrlParameters(self, **kwargs) -> None:
        """ This public function can be used to set individual or multiple masked edit
parameters after construction.  (See maskededit module overview for the list
of valid parameters.)

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def SetFieldParameters(self, field_index, **kwargs) -> None:
        """ Routine provided to modify the parameters of a given field.
Because changes to fields can affect the overall control,
direct access to the fields is prevented, and the control
is always âreconfiguredâ after setting a field parameter.
(See maskededit module overview for the list of valid field-level
parameters.)

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def SetForegroundColour(self, colour) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def SetMaskParameters(self, **kwargs) -> None:
        """ old name for the SetCtrlParameters function  (DEPRECATED)

            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """



class MaskedEditAccessorsMixin:
    """ To avoid a ton of boiler-plate, and to automate the getter/setter generation
for each valid control parameter so we never forget to add the functions when
adding parameters, this class programmatically adds the masked edit mixin
parameters to itself.
(This makes it easier for Designers like Boa to deal with masked controls.)

        Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditAccessorsMixin.html
    """


