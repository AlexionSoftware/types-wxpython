# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class ExpandoTextCtrl(TextCtrl):
    """ The ExpandoTextCtrl is a multi-line wx.TextCtrl that will
adjust its height on the fly as needed to accommodate the number of
lines needed to display the current content of the control.  It is
assumed that the width of the control will be a fixed value and
that only the height will be adjusted automatically.  If the
control is used in a sizer then the width should be set as part of
the initial or min size of the control.

        Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
    """
    def __init__(self, parent, id=-1, value="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, validator=wx.DefaultValidator, name="expando") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def AppendText(self, text: str) -> None:
        """ Appends the text to the end of the text control.

            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def GetMaxHeight(self) -> int:
        """ Returns the maximum height that the control will expand to on its own.

            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def OnSize(self, evt) -> None:
        """ Handles the wx.EVT_SIZE event for ExpandoTextCtrl.

            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def OnTextChanged(self, evt) -> None:
        """ Handles the wx.EVT_TEXT event for ExpandoTextCtrl.

            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def SetFont(self, font: 'Font') -> bool:
        """ Sets the font for the ExpandoTextCtrl.

            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def SetMaxHeight(self, h: int) -> None:
        """ Sets the maximum height that the control will expand to on its
own, and adjusts it down if needed.

            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def WriteText(self, text: str) -> None:
        """ Writes the text into the text control at the current insertion position.

            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """



EVT_SIZE: int

EVT_TEXT: int

