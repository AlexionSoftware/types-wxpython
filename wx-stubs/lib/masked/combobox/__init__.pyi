# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class BaseMaskedComboBox(ComboBox,MaskedEditMixin):
    """ Base class for generic masked edit comboboxes; allows auto-complete of values.
It is not meant to be instantiated directly, but rather serves as a base class
for any subsequent refinements.

        Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
    """
    def __init__(self, parent, id=-1, value = '', pos = wx.DefaultPosition, size = wx.DefaultSize, choices = [], style = wx.CB_DROPDOWN, validator = wx.DefaultValidator, name = "maskedComboBox", setupEventHandling = True, **kwargs) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def Append(self, choice, clientData=None) -> None:
        """ This base control function override is necessary so the control can keep
track of any additions to the list of choices, because ComboBox
doesnât have an accessor for the choice list.  The code here is the same
as in the SetParameters() mixin function, but is done for the individual
value as appended, so the list can be built incrementally without speed
penalty.

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def AppendItems(self, choices) -> None:
        """ AppendItems is handled in terms
of lib.masked.combobox.ComboBox.Append, to avoid code replication.

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def Clear(self) -> None:
        """ This base control function override is necessary so the derived control
can keep track of any additions to the list of choices, because
ComboBox  doesnât have an accessor for the choice list.

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def Cut(self) -> None:
        """ This function redefines the externally accessible ComboBox.Cut
to be a smart âeraseâ of the text in question, so as not to corrupt the
masked control.

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def GetMark(self) -> None:
        """ GetTextSelection() -> (from, to)

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def IsEmpty(*args, **kw) -> None:
        """ IsEmpty() -> bool

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def OnWindowDestroy(self, event) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def Paste(self) -> None:
        """ This function redefines the externally accessible ComboBox.Paste
to be a smart âpasteâ of the text in question, so as not to corrupt the
masked control.

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def Refresh(self) -> None:
        """ This function redefines the externally accessible ComboBox.Refresh
to validate the contents of the masked control as it refreshes.

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def SetFont(self, *args, **kwargs) -> None:
        """ Set the font, then recalculate control size, if appropriate.

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def SetSelection(self, index: int) -> None:
        """ Necessary override for bookkeeping on choice selection, to keep current
value current.

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def SetValue(self, value) -> None:
        """ This function redefines the externally accessible ComboBox.SetValue
to be a smart âpasteâ of the text in question, so as not to corrupt the
masked control.

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def Undo(self) -> None:
        """ This function defines the undo operation for the control.
(The default undo is 1-deep.)

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """



class ComboBox(BaseMaskedComboBox,MaskedEditAccessorsMixin):
    """ The âuser-visibleâ masked combobox control, this class is
identical to the BaseMaskedComboBox class itâs derived from.
(This extra level of inheritance allows us to add the generic
set of masked edit parameters only to this class while allowing
other classes to derive from the âbaseâ masked combobox control,
and provide a smaller set of valid accessor functions.)
See BaseMaskedComboBox for available methods.

        Source: https://docs.wxpython.org/wx.lib.masked.combobox.ComboBox.html
    """


class PreMaskedComboBox(BaseMaskedComboBox,MaskedEditAccessorsMixin):
    """ This class exists to support the use of XRC subclassing.

        Source: https://docs.wxpython.org/wx.lib.masked.combobox.PreMaskedComboBox.html
    """
    def __init__(self) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.PreMaskedComboBox.html
        """

    def OnCreate(self, evt) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.combobox.PreMaskedComboBox.html
        """



