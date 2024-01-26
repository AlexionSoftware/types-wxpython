# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class AuiDefaultTabArt:
    """ Tab art provider code - a tab provider provides all drawing functionality to the AuiNotebook.
This allows the AuiNotebook to have a pluggable look-and-feel.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
    """
    def __init__(self) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def Clone(self) -> None:
        """ Clones the art object.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def DrawBackground(self, dc, wnd, rect) -> None:
        """ Draws the tab area background.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def DrawButton(self, dc, wnd, in_rect, button, orientation) -> None:
        """ Draws a button on the tab or on the tab area, depending on the button identifier.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def DrawFocusRectangle(self, dc, page, wnd, draw_text, text_offset, bitmap_offset, drawn_tab_yoff, drawn_tab_height, textx, texty) -> None:
        """ Draws the focus rectangle on a tab.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def DrawTab(self, dc, wnd, page, in_rect, close_button_state, paint_control=False) -> None:
        """ Draws a single tab.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetAGWFlags(self) -> None:
        """ Returns the tab art flags.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetBestTabCtrlSize(self, wnd, pages, required_bmp_size) -> None:
        """ Returns the best tab control size.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetIndentSize(self) -> None:
        """ Returns the tabs indent size.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetMeasuringFont(self) -> None:
        """ Returns the font for calculating text measurements.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetNormalFont(self) -> None:
        """ Returns the normal font for drawing tab labels.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetSelectedFont(self) -> None:
        """ Returns the selected tab font for drawing tab labels.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, close_button_state, control=None) -> None:
        """ Returns the tab size for the given caption, bitmap and button state.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetAGWFlags(self, agwFlags: int) -> None:
        """ Sets the tab art flags.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetBaseColour(self, base_colour: Union[int, str, 'Colour']) -> None:
        """ Sets a new base colour.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetCustomButton(self, bitmap_id, button_state, bmp) -> None:
        """ Sets a custom bitmap for the close, left, right and window list buttons.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetDefaultColours(self, base_colour: Optional[Union[int, str, 'Colour']]=None) -> None:
        """ Sets the default colours, which are calculated from the given base colour.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetMeasuringFont(self, font: 'Font') -> None:
        """ Sets the font for calculating text measurements.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetNormalFont(self, font: 'Font') -> None:
        """ Sets the normal font for drawing tab labels.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetSelectedFont(self, font: 'Font') -> None:
        """ Sets the selected tab font for drawing tab labels.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetSizingInfo(self, tab_ctrl_size, tab_count, minMaxTabWidth) -> None:
        """ Sets the tab sizing information.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def ShowDropDown(self, wnd, pages, active_idx) -> None:
        """ Shows the drop-down window menu on the tab area.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """



class ChromeTabArt(AuiDefaultTabArt):
    """ A class to draw tabs using the Google Chrome browser style.
It uses custom bitmap to render the tabs, so that the look and feel is as close
as possible to the Chrome style.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
    """
    def __init__(self) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """

    def Clone(self) -> None:
        """ Clones the art object.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """

    def DrawTab(self, dc, wnd, page, in_rect, close_button_state, paint_control=False) -> None:
        """ Draws a single tab.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, close_button_state, control=None) -> None:
        """ Returns the tab size for the given caption, bitmap and button state.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """

    def SetAGWFlags(self, agwFlags: int) -> None:
        """ Sets the tab art flags.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """

    def SetBitmaps(self, mirror: bool) -> None:
        """ Assigns the tab custom bitmaps

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """

    def SetSizingInfo(self, tab_ctrl_size, tab_count, minMaxTabWidth) -> None:
        """ Sets the tab sizing information.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """



class FF2TabArt(AuiDefaultTabArt):
    """ A class to draw tabs using the Firefox 2 (FF2) style.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.FF2TabArt.html
    """
    def __init__(self) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.FF2TabArt.html
        """

    def Clone(self) -> None:
        """ Clones the art object.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.FF2TabArt.html
        """

    def DrawTab(self, dc, wnd, page, in_rect, close_button_state, paint_control=False) -> None:
        """ Draws a single tab.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.FF2TabArt.html
        """

    def DrawTabBackground(self, dc, rect, focus, upperTabs) -> None:
        """ Draws the tab background for the Firefox 2 style.
This is more consistent with FlatNotebook than before.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.FF2TabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, close_button_state, control) -> None:
        """ Returns the tab size for the given caption, bitmap and button state.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.FF2TabArt.html
        """



class VC71TabArt(AuiDefaultTabArt):
    """ A class to draw tabs using the Visual Studio 2003 (VC71) style.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC71TabArt.html
    """
    def __init__(self) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC71TabArt.html
        """

    def Clone(self) -> None:
        """ Clones the art object.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC71TabArt.html
        """

    def DrawTab(self, dc, wnd, page, in_rect, close_button_state, paint_control=False) -> None:
        """ Draws a single tab.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC71TabArt.html
        """



class VC8TabArt(AuiDefaultTabArt):
    """ A class to draw tabs using the Visual Studio 2005 (VC8) style.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
    """
    def __init__(self) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
        """

    def Clone(self) -> None:
        """ Clones the art object.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
        """

    def DrawTab(self, dc, wnd, page, in_rect, close_button_state, paint_control=False) -> None:
        """ Draws a single tab.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
        """

    def FillVC8GradientColour(self, dc, tabPoints, active) -> None:
        """ Fills the tab with the Visual Studio 2005 gradient background.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, close_button_state, control=None) -> None:
        """ Returns the tab size for the given caption, bitmap and button state.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
        """

    def SetSizingInfo(self, tab_ctrl_size, tab_count, minMaxTabWidth) -> None:
        """ Sets the tab sizing information.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
        """



