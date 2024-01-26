# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class GenStaticBitmap(Control):
    """ GenStaticBitmap is a generic implementation of wx.StaticBitmap.

        Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
    """
    def __init__(self, parent, ID, bitmap, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, name = "genstatbmp") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def AcceptsFocus(self) -> None:
        """ Can this window be given focus by mouse click?

            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def DoGetBestSize(self) -> None:
        """ Overridden base class virtual.  Determines the best size of
the control based on the label size and the current font.

            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def GetBitmap(self) -> 'Bitmap':
        """ Returns the bitmap currently used in the control.

            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def GetDefaultAttributes(self) -> None:
        """ Overridden base class virtual.  By default we should use
the same font/colour attributes as the native StaticBitmap.

            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def OnEraseBackground(self, event: 'EraseEvent') -> None:
        """ Handles the wx.EVT_ERASE_BACKGROUND event for GenStaticBitmap.

            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def OnPaint(self, event: 'PaintEvent') -> None:
        """ Handles the wx.EVT_PAINT for GenStaticBitmap.

            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def SetBitmap(self, bitmap: 'Bitmap') -> None:
        """ Sets the bitmap label.

            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def ShouldInheritColours(self) -> None:
        """ Overridden base class virtual.  If the parent has non-default
colours then we want this control to inherit them.

            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """



EVT_ERASE_BACKGROUND: int

EVT_PAINT: int

