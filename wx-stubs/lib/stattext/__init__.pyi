# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class GenStaticText(Control):
    """ GenStaticText is a generic implementation of wx.StaticText.

        Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
    """
    def __init__(self, parent, ID=-1, label="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name="genstattext") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def AcceptsFocus(self) -> None:
        """ Can this window be given focus by mouse click?

            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def Disable(self) -> None:
        """ Disables the control.

            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def DoGetBestSize(self) -> None:
        """ Overridden base class virtual.  Determines the best size of
the control based on the label size and the current font.

            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ Enable or disable the widget for user input.

            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def GetDefaultAttributes(self) -> None:
        """ Overridden base class virtual.  By default we should use
the same font/colour attributes as the native wx.StaticText.

            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def OnEraseBackground(self, event: 'EraseEvent') -> None:
        """ Handles the wx.EVT_ERASE_BACKGROUND event for GenStaticText.

            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def OnPaint(self, event: 'PaintEvent') -> None:
        """ Handles the wx.EVT_PAINT for GenStaticText.

            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the static text font and updates the controlâs size to exactly
fit the label unless the control has wx.ST_NO_AUTORESIZE flag.

            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def SetLabel(self, label: str) -> None:
        """ Sets the static text label and updates the controlâs size to exactly
fit the label unless the control has wx.ST_NO_AUTORESIZE flag.

            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def ShouldInheritColours(self) -> None:
        """ Overridden base class virtual.  If the parent has non-default
colours then we want this control to inherit them.

            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """



EVT_ERASE_BACKGROUND: int

EVT_PAINT: int

ST_NO_AUTORESIZE: int

