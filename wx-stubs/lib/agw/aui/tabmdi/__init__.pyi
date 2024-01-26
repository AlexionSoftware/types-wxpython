# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class AuiMDIClientWindow(AuiNotebook):
    """ AuiNotebook is a notebook control which implements many features common in applications with dockable panes.
Specifically, AuiNotebook implements functionality which allows the user to rearrange tab
order via drag-and-drop, split the tab window into many different splitter configurations, and toggle
through different themes to customize the controlâs look and feel.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
    """
    def __init__(self, parent, agwStyle=0) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
        """

    def OnPageChanged(self, event) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
        """

    def OnPageClose(self, event) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ Handles the wx.EVT_SIZE event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
        """

    def PageChanged(self, old_selection, new_selection) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
        """

    def SetSelection(self, nPage) -> None:
        """ Sets the page selection. Calling this method will generate a page change event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
        """



EVT_SIZE: int

