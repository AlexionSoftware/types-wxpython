# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class HyperLinkCtrl(GenStaticText):
    """ HyperLinkCtrl is a control for wxPython that acts like a hyper
link in a typical browser. Latest features include the ability to
capture your own left, middle, and right click events to perform
your own custom event handling and ability to open link in a new
or current browser window.

        Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
    """
    def __init__(self, parent, id=-1, label="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name="staticText", URL="") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def AutoBrowse(self, AutoBrowse: bool=True) -> None:
        """ Automatically browse to URL when clicked.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def DisplayError(self, ErrorMessage, ReportErrors=True) -> None:
        """ Displays an error message (according to the ReportErrors parameter) in a
MessageBox.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def DoPopup(self, DoPopup: bool=True) -> None:
        """ Sets whether to show popup menu on right click or not.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def EnableRollover(self, EnableRollover: bool=False) -> None:
        """ Enable/disable rollover.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GetBold(self) -> None:
        """ Returns whether the HyperLinkCtrl has text in bold or not.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GetColours(self) -> None:
        """ Gets the colours for the link, the visited link and the mouse
rollover.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GetLinkCursor(self) -> None:
        """ Gets the link cursor.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GetUnderlines(self) -> None:
        """ Returns if link is underlined, if the mouse rollover is
underlined and if the visited link is underlined.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GetURL(self) -> None:
        """ Retrieve the URL associated to the HyperLinkCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GetVisited(self) -> None:
        """ Returns whether a link has been visited or not.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GotoURL(self, URL, ReportErrors=True, NotSameWinIfPossible=False) -> None:
        """ Goto the specified URL.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def OnMouseEvent(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_MOUSE_EVENTS events for HyperLinkCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def OnPopUpCopy(self, event: 'MenuEvent') -> None:
        """ Handles the wx.EVT_MENU event for HyperLinkCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def OpenInSameWindow(self, NotSameWinIfPossible: bool=False) -> None:
        """ Open multiple URL in the same window (if possible).

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def ReportErrors(self, ReportErrors: bool=True) -> None:
        """ Set whether to report browser errors or not.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def SetBold(self, Bold: bool=False) -> None:
        """ Sets the HyperLinkCtrl label in bold text.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def SetColours(*args, **kwargs) -> None:
        """ Sets the colours for the link, the visited link and the mouse rollover.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def SetLinkCursor(self, cur: Cursor=wx.CURSOR_HAND) -> None:
        """ Sets link cursor properties.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def SetUnderlines(self, link=True, visited=True, rollover=True) -> None:
        """ Sets whether the text should be underlined or not for new links, visited
links and rollovers.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def SetURL(self, URL: HyperLinkCtrl) -> None:
        """ Sets the HyperLinkCtrl text to the specified URL.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def SetVisited(self, Visited: bool=False) -> None:
        """ Sets a link as visited.

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def UpdateLink(self, OnRefresh: bool=True) -> None:
        """ Updates the link, changing text properties if:

            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """



EVT_MOUSE_EVENTS: int

EVT_MENU: int

