# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class FlatNotebook(Panel):
    """ The FlatNotebook is a full implementation of the Notebook, and designed to be
a drop-in replacement for Notebook. The API functions are similar so one can
expect the function to behave in the same way.

        Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=0, name="FlatNotebook") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def AddPage(self, page, text, select=False, imageId=-1) -> None:
        """ Adds a page to the FlatNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def AdvanceSelection(self, forward: bool=True) -> None:
        """ Cycles through the tabs.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def AssignImageList(self, imageList: 'ImageList') -> None:
        """ Assigns the image list for the page control.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def DeleteAllPages(self) -> None:
        """ Deletes all the pages in the FlatNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def DeletePage(self, page: Any) -> None:
        """ Deletes the specified page, and the associated window.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def DoGetBestSize(self) -> None:
        """ Gets the size which best suits the window: for a control, it would be the
minimal size which doesnât truncate the control, for a panel - the same
size as it would have after a call to Fit().

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def EnableTab(self, page, enabled=True) -> None:
        """ Enables or disables a tab.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def EnsureVisible(self, page: Any) -> None:
        """ Ensures that a tab is visible.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetActiveTabColour(self) -> None:
        """ Returns the active tab colour.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetActiveTabTextColour(self) -> None:
        """ Get the active tab text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetAGWWindowStyleFlag(self) -> None:
        """ Returns the FlatNotebook window style.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetBorderColour(self) -> None:
        """ Returns the border colour.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetCurrentPage(self) -> None:
        """ Returns the currently selected notebook page or None if none is selected.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetCustomPage(self) -> None:
        """ Returns a custom panel to show when there are no pages left in FlatNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetEnabled(self, page: Any) -> None:
        """ Returns whether a tab is enabled or not.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetGradientColourBorder(self) -> None:
        """ Gets the tab border colour.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetGradientColourFrom(self) -> None:
        """ Gets first gradient colour.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetGradientColourTo(self) -> None:
        """ Gets second gradient colour.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetImageList(self) -> None:
        """ Returns the associated image list.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetNonActiveTabTextColour(self) -> None:
        """ Returns the non active tabs text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPadding(self) -> None:
        """ Returns the amount of space around each pageâs icon and label, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPage(self, page) -> None:
        """ Returns the window at the given page position, or None.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageBestSize(self) -> None:
        """ Return the page best size.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageCount(self) -> None:
        """ Returns the number of pages in the FlatNotebook control.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageImage(self, page: Any) -> None:
        """ Returns the image index for the given page.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageIndex(self, win: 'Window') -> None:
        """ Returns the index at which the window is found.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageShapeAngle(self, page_index: Any) -> None:
        """ Returns the angle associated to a tab.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageText(self, page: Any) -> None:
        """ Returns the string for the given page.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageTextColour(self, page: Any) -> None:
        """ Returns the tab text colour if it has been set previously, or None otherwise.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPreviousSelection(self) -> None:
        """ Returns the previous selection.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetSelection(self) -> None:
        """ Returns the currently selected page, or -1 if none was selected.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetTabArea(self) -> None:
        """ Returns the associated page.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetTabAreaColour(self) -> None:
        """ Returns the area behind the tabs colour.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetTileOrientation(self) -> None:
        """ Returns the orientation when on tiling mode. This method can return
wx.VERTICAL when the panels are vertically stacked, wx.HORIZONTAL
when they are horizontally stacked panels or None when there is no
stacking and FlatNotebook behaves like a normal notebook.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def HasAGWFlag(self, flag: FlatNotebook) -> None:
        """ Returns whether a flag is present in the FlatNotebook style.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def HideTabs(self) -> None:
        """ Hides the tabs.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def Init(self) -> None:
        """ Initializes all the class attributes.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def InsertPage(self, indx, page, text, select=True, imageId=-1) -> None:
        """ Inserts a new page at the specified position.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def OnDropTarget(self, x, y, nTabPage, wnd_oldContainer) -> None:
        """ Handles the drop action from a drag and drop operation.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def OnNavigationKey(self, event: NavigationKeyEvent) -> None:
        """ Handles the wx.EVT_NAVIGATION_KEY event for FlatNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def RemovePage(self, page: Any) -> None:
        """ Deletes the specified page, without deleting the associated window.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetActiveTabColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the active tab colour.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetActiveTabTextColour(self, textColour: Union[int, str, 'Colour']) -> None:
        """ Sets the text colour for the active tab.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetAGWWindowStyleFlag(self, agwStyle: int) -> None:
        """ Sets the FlatNotebook window style flags.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetAllPagesShapeAngle(self, angle: Any) -> None:
        """ Sets the angle associated to all the tab.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetCustomPage(self, panel: 'Window') -> None:
        """ Sets a custom panel to show when there are no pages left in FlatNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetGradientColourBorder(self, border: Union[int, str, 'Colour']) -> None:
        """ Sets the tab border colour.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetGradientColourFrom(self, fr: Union[int, str, 'Colour']) -> None:
        """ Sets the starting colour for the gradient.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetGradientColours(self, fr, to, border) -> None:
        """ Sets the gradient colours for the tab.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetGradientColourTo(self, to: Union[int, str, 'Colour']) -> None:
        """ Sets the ending colour for the gradient.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetImageList(self, imageList: 'ImageList') -> None:
        """ Sets the image list for the page control.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetNavigatorIcon(self, bmp: 'Bitmap') -> None:
        """ Set the icon used by the TabNavigatorWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetNonActiveTabTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the non active tabs text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetPadding(self, padding: Any) -> None:
        """ Sets the amount of space around each pageâs icon and label, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetPageImage(self, page, image) -> None:
        """ Sets the image index for the given page.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetPageShapeAngle(self, page_index, angle) -> None:
        """ Sets the angle associated to a tab.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetPageText(self, page, text) -> None:
        """ Sets the text for the given page.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetPageTextColour(self, page, colour) -> None:
        """ Sets the tab text colour individually.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetRightClickMenu(self, menu: 'Menu') -> None:
        """ Sets the popup menu associated to a right click on a tab.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetSelection(self, page: Any) -> None:
        """ Sets the selection for the given page.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetTabAreaColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the area behind the tabs colour.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def ShowCustomPage(self, show=True) -> None:
        """ Hides the custom panel which is shown when there are no pages left in FlatNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def ShowTabs(self) -> None:
        """ Shows the tabs if hidden previously.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def Tile(self, orient: Optional['VERTICAL']=None) -> None:
        """ Shows pages in column/row mode (one panel after the other in columns/rows).

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """



EVT_NAVIGATION_KEY: int

VERTICAL: int

HORIZONTAL: int

class FlatNotebookCompatible(FlatNotebook):
    """ This class is more compatible with the Notebook API, especially regarding
page changing events. Use the FlatNotebookCompatible.SetSelection() method if you wish to send page
changing events, or FlatNotebookCompatible.ChangeSelection() otherwise.

        Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebookCompatible.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=0, name="FlatNotebook") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebookCompatible.html
        """

    def ChangeSelection(self, page: Any) -> None:
        """ Sets the selection for the given page.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebookCompatible.html
        """

    def SetSelection(self, page: Any) -> None:
        """ Sets the selection for the given page.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebookCompatible.html
        """



class TabNavigatorWindow(Dialog):
    """ This class is used to create a modal dialog that enables Smart Tabbing,
similar to what you would get by hitting Alt + Tab on Windows.

        Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
    """
    def __init__(self, parent=None, icon=None) -> None:
        """ Default class constructor.
Used internally.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def CloseDialog(self) -> None:
        """ Closes the TabNavigatorWindow dialog, setting the new selection in
FlatNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def OnItemSelected(self, event: ListEvent) -> None:
        """ Handles the wx.EVT_LISTBOX_DCLICK for the TabNavigatorWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def OnKeyUp(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_KEY_UP for the TabNavigatorWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def OnNavigationKey(self, event: NavigationKeyEvent) -> None:
        """ Handles the wx.EVT_NAVIGATION_KEY for the TabNavigatorWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def OnPanelEraseBg(self, event: EraseEvent) -> None:
        """ Handles the wx.EVT_ERASE_BACKGROUND for the TabNavigatorWindow top panel.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def OnPanelPaint(self, event: PaintEvent) -> None:
        """ Handles the wx.EVT_PAINT for the TabNavigatorWindow top panel.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def PopulateListControl(self, book: FlatNotebook) -> None:
        """ Populates the TabNavigatorWindow listbox with a list of tabs.

            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """



EVT_LISTBOX_DCLICK: int

EVT_KEY_UP: int

EVT_ERASE_BACKGROUND: int

EVT_PAINT: int

FNB_VC71: int

FNB_FANCY_TABS: int

FNB_TABS_BORDER_SIMPLE: int

FNB_NO_X_BUTTON: int

FNB_NO_NAV_BUTTONS: int

FNB_MOUSE_MIDDLE_CLOSES_TABS: int

FNB_BOTTOM: int

FNB_NODRAG: int

FNB_VC8: int

FNB_X_ON_TAB: int

FNB_BACKGROUND_GRADIENT: int

FNB_COLOURFUL_TABS: int

FNB_DCLICK_CLOSES_TABS: int

FNB_SMART_TABS: int

FNB_DROPDOWN_TABS_LIST: int

FNB_ALLOW_FOREIGN_DND: int

FNB_HIDE_ON_SINGLE_TAB: int

FNB_DEFAULT_STYLE: int

FNB_FF2: int

FNB_NO_TAB_FOCUS: int

FNB_RIBBON_TABS: int

FNB_HIDE_TABS: int

FNB_NAV_BUTTONS_WHEN_NEEDED: int

