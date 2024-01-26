# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class BaseMaskedTextCtrl(TextCtrl,MaskedEditMixin):
    """ This is the primary derivation from MaskedEditMixin.  It provides
a general masked text control that can be configured with different
masks.

        Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
    """
    def __init__(self, parent, id=-1, value = '', pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TE_PROCESS_TAB, validator=wx.DefaultValidator, name = 'maskedTextCtrl', setupEventHandling = True, **kwargs) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def ChangeValue(self, value: str) -> None:
        """ Provided to accommodate similar functionality added to base
control in wxPython 2.7.1.1.

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def Clear(self) -> None:
        """ Blanks the current control value by replacing it with the default value.

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def Cut(self) -> None:
        """ This function redefines the externally accessible TextCtrl.Cut
to be a smart âeraseâ of the text in question, so as not to corrupt the
masked control.

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def IsEmpty(*args, **kw) -> None:
        """ IsEmpty() -> bool

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def IsModified(self) -> None:
        """ This function overrides the raw TextCtrl.IsModified method,
because the  masked edit mixin uses SetValue to change the value, which
doesnât modify the state of this attribute.  So, the derived control
keeps track on each keystroke to see if the value changes, and if so,
itâs been modified.

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def ModifyValue(self, value, use_change_value=False) -> None:
        """ This factored function of common code does the bulk of the work for
SetValue and ChangeValue.

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def Paste(self) -> None:
        """ This function redefines the externally accessible TextCtrl.Paste
to be a smart âpasteâ of the text in question, so as not to corrupt the
masked control.

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def Refresh(self) -> None:
        """ This function redefines the externally accessible TextCtrl.Refresh
to validate the contents of the masked control as it refreshes.

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def SetFont(self, *args, **kwargs) -> None:
        """ Set the font, then recalculate control size, if appropriate.

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def SetValue(self, value) -> None:
        """ This function redefines the externally accessible TextCtrl.SetValue
to be a smart âpasteâ of the text in question, so as not to corrupt the
masked control.

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def Undo(self) -> None:
        """ This function defines the undo operation for the control.
(The default undo is 1-deep.)

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """



class PreMaskedTextCtrl(BaseMaskedTextCtrl,MaskedEditAccessorsMixin):
    """ This class exists to support the use of XRC subclassing.

        Source: https://docs.wxpython.org/wx.lib.masked.textctrl.PreMaskedTextCtrl.html
    """
    def __init__(self) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.PreMaskedTextCtrl.html
        """

    def OnCreate(self, evt) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.PreMaskedTextCtrl.html
        """



class TextCtrl(BaseMaskedTextCtrl,MaskedEditAccessorsMixin):
    """ The âuser-visibleâ masked text control; it is identical to the
BaseMaskedTextCtrl class itâs derived from.
(This extra level of inheritance allows us to add the generic
set of masked edit parameters only to this class while allowing
other classes to derive from the âbaseâ masked text control,
and provide a smaller set of valid accessor functions.)
See BaseMaskedTextCtrl for available methods.

        Source: https://docs.wxpython.org/wx.lib.masked.textctrl.TextCtrl.html
    """


