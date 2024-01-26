# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class TabTextCtrl(ExpandoTextCtrl):
    """ Control used for in-place edit.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
    """
    def __init__(self, owner, tab, page_index) -> None:
        """ Default class constructor.
For internal use: do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def AcceptChanges(self) -> None:
        """ Accepts/refuses the changes made by the user.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def Finish(self) -> None:
        """ Finish editing.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def item(self) -> None:
        """ Returns the item currently edited.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def OnChar(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_CHAR event for TabTextCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def OnKeyUp(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_KEY_UP event for TabTextCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def OnKillFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_KILL_FOCUS event for TabTextCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def StopEditing(self) -> None:
        """ Suddenly stops the editing.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """



EVT_CHAR: int

EVT_KEY_UP: int

EVT_KILL_FOCUS: int

class AuiNotebook(Panel):
    """ AuiNotebook is a notebook control which implements many features common in applications with dockable panes.
Specifically, AuiNotebook implements functionality which allows the user to rearrange tab
order via drag-and-drop, split the tab window into many different splitter configurations, and toggle
through different themes to customize the controlâs look and feel.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=AUI_NB_DEFAULT_STYLE, name="AuiNotebook") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def AddControlToPage(self, page_idx, control) -> None:
        """ Adds a control inside a tab (not in the tab area).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def AddPage(self, page, caption, select=False, bitmap=wx.NullBitmap, disabled_bitmap=wx.NullBitmap, control=None, tooltip="") -> None:
        """ Adds a page. If the select parameter is True, calling this will generate a
page change event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def AddTabAreaButton(self, id, location, normal_bitmap=wx.NullBitmap, disabled_bitmap=wx.NullBitmap, name="") -> None:
        """ Adds a button in the tab area.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def AdvanceSelection(self, forward=True, wrap=True) -> None:
        """ Cycles through the tabs.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def AssignImageList(self, imageList: 'ImageList') -> None:
        """ Sets the image list for the AuiNotebook control.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def CalculateNewSplitSize(self) -> None:
        """ Calculates the size of the new split.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def CalculateTabCtrlHeight(self) -> None:
        """ Calculates the tab control area height.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def CloneTabAreaButtons(self) -> None:
        """ Clones the tab area buttons when the AuiNotebook is being split.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def DeletePage(self, page_idx: int) -> None:
        """ Deletes a page at the given index. Calling this method will generate a page
change event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def Destroy(self) -> None:
        """ Destroys the window safely.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def DoSizing(self) -> None:
        """ Performs all sizing operations in each tab control.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def EditTab(self, page_index: int) -> None:
        """ Starts the editing of an item label, sending a EVT_AUINOTEBOOK_BEGIN_LABEL_EDIT event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def EnableTab(self, page_idx, enable=True) -> None:
        """ Enables/disables a page in the notebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def EnsureVisible(self, indx: int) -> None:
        """ Ensures the input page index indx is visible.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def FindNextActiveTab(self, idx: int) -> None:
        """ Finds the next active tab (used mainly when AuiNotebook has inactive/disabled
tabs in it).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def FindTab(self, page: AuiNotebookPage) -> None:
        """ Finds the tab control that currently contains the window as well
as the index of the window in the tab control. It returns True if the
window was found, otherwise False.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def FloatPage(self, page_index: int) -> None:
        """ Float the page in page_index by reparenting it to a floating frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetActiveTabCtrl(self) -> None:
        """ Returns the active tab control. It is called to determine which control
gets new windows being added.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetAGWWindowStyleFlag(self) -> None:
        """ Returns the AGW-specific style of the window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetArtProvider(self) -> None:
        """ Returns the associated art provider.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetAuiManager(self) -> None:
        """ Returns the associated AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetCurrentPage(self) -> None:
        """ Returns the currently active page (not the index), or None if none was selected.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetDefaultBorder(self) -> None:
        """ Returns the default border style for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetEnabled(self, page_idx: int) -> None:
        """ Returns whether the page specified by the index page_idx is enabled.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetHeightForPageHeight(self, pageHeight: int) -> None:
        """ Gets the height of the notebook for a given page height.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetHidden(self, page_idx: int) -> None:
        """ Returns whether the page specified by the index page_idx is hidden.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetImageList(self) -> None:
        """ Returns the associated image list (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetMinMaxTabWidth(self) -> None:
        """ Returns the minimum and the maximum tab widths for AuiNotebook when the
AUI_NB_TAB_FIXED_WIDTH style is defined.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPage(self, page_idx: int) -> None:
        """ Returns the page specified by the given index.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageBitmap(self, page_idx: int) -> None:
        """ Returns the tab bitmap for the page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageCount(self) -> None:
        """ Returns the number of pages in the notebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageImage(self, page: int) -> None:
        """ Returns the image index for the given page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageIndex(self, page_wnd: 'Window') -> None:
        """ Returns the page index for the specified window. If the window is not
found in the notebook, wx.NOT_FOUND is returned.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageInfo(self, page_idx: int) -> None:
        """ Returns the AuiNotebookPage info structure specified by the given index.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageText(self, page_idx: int) -> None:
        """ Returns the tab label for the page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageTextColour(self, page_idx: int) -> None:
        """ Returns the tab text colour for the page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageTooltip(self, page_idx: int) -> None:
        """ Returns the tab tooltip for the page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetSashDClickUnsplit(self) -> None:
        """ Returns whether a splitted AuiNotebook can be unsplitted by double-clicking
on the splitter sash.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetSelection(self) -> None:
        """ Returns the index of the currently active page, or -1 if none was selected.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetShownPageCount(self) -> None:
        """ Returns the number of pages shown in the notebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetTabContainer(self) -> None:
        """ Returns the instance of AuiTabContainer.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetTabCtrlFromPoint(self, pt: Union[tuple[int, int], 'Point']) -> None:
        """ Returns the tab control at the specified point.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetTabCtrlHeight(self) -> None:
        """ Returns the tab control height.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetTabFrameFromTabCtrl(self, tab_ctrl: AuiTabCtrl) -> None:
        """ Returns the tab frame associated with a tab control.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetTabFrameFromWindow(self, wnd: 'Window') -> None:
        """ Returns the tab frame associated with a window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def HasCloseButton(self, page_idx: int) -> None:
        """ Returns whether a tab displays a close button or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def HasMultiplePages(self) -> None:
        """ This method should be overridden to return True if this window has multiple pages. All
standard class with multiple pages such as Notebook, Listbook and Treebook
already override it to return True and user-defined classes with similar behaviour
should do it as well to allow the library to handle such windows appropriately.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def HideAllTabs(self, hidden: bool=True) -> None:
        """ Hides all tabs on the AuiNotebook control.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def HidePage(self, page_idx, hidden=True) -> None:
        """ Sets whether a page is hidden.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def InitNotebook(self, agwStyle: int) -> None:
        """ Contains common initialization code called by all constructors.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def InsertPage(self, page_idx, page, caption, select=False, bitmap=wx.NullBitmap, disabled_bitmap=wx.NullBitmap, control=None, tooltip="") -> None:
        """ This is similar to AddPage, but allows the ability to specify the insert location.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def IsMouseWellOutsideWindow(self) -> None:
        """ Returns whether the mouse is well outside the AuiNotebook screen rectangle.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def IsRenamable(self, page_idx: int) -> None:
        """ Returns whether a tab can be renamed or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def LoadPerspective(self, layout: str) -> None:
        """ Loads a layout which was saved with SavePerspective.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def NotebookPreview(self, thumbnail_size: int=200) -> None:
        """ Generates a preview of all the pages in the notebook (MSW and GTK only).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnChildFocusNotebook(self, event: ChildFocusEvent) -> None:
        """ Handles the wx.EVT_CHILD_FOCUS event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnCloseFloatingPage(self, event: CloseEvent) -> None:
        """ Handles the wx.EVT_CLOSE event for a floating page in AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnNavigationKeyNotebook(self, event: NavigationKeyEvent) -> None:
        """ Handles the wx.EVT_NAVIGATION_KEY event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnRenameAccept(self, page_index, value) -> None:
        """ Called by TabTextCtrl, to accept the changes and to send the
EVT_AUINOTEBOOK_END_LABEL_EDIT event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnRenameCancelled(self, page_index: int) -> None:
        """ Called by TabTextCtrl, to cancel the changes and to send the
EVT_AUINOTEBOOK_END_LABEL_EDIT event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ Handles the wx.EVT_SIZE event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabBeginDrag(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_BEGIN_DRAG event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabBgDClick(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_BG_DCLICK event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabButton(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_BUTTON event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabCancelDrag(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_CANCEL_DRAG event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabClicked(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_PAGE_CHANGING event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabDClick(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_TAB_DCLICK event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabDragMotion(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_DRAG_MOTION event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabEndDrag(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_END_DRAG event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabMiddleDown(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_TAB_MIDDLE_DOWN event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabMiddleUp(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_TAB_MIDDLE_UP event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabRightDown(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_TAB_RIGHT_DOWN event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabRightUp(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_TAB_RIGHT_UP event for AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def ReDockPage(self, pane: Any) -> None:
        """ Re-docks a floating AuiNotebook tab in the original position, when possible.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def RemoveControlFromPage(self, page_idx: int) -> None:
        """ Removes a control from a tab (not from the tab area).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def RemoveEmptyTabFrames(self) -> None:
        """ Removes all the empty tab frames.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def RemovePage(self, page_idx: int) -> None:
        """ Removes a page, without deleting the window pointer.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def RemoveTabAreaButton(self, id: int) -> None:
        """ Removes a button from the tab area.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def ReparentControl(self, control, dest_tabs) -> None:
        """ Reparents a control added inside a tab.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def ResetTextControl(self) -> None:
        """ Called by TabTextCtrl when it marks itself for deletion.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SavePerspective(self) -> None:
        """ Saves the entire user interface layout into an encoded string, which can then
be stored by the application (probably using Config). When a perspective
is restored using LoadPerspective, the entire user interface will return
to the state it was when the perspective was saved.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetAGWWindowStyleFlag(self, agwStyle: int) -> None:
        """ Sets the AGW-specific style of the window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetArtProvider(self, art: Any) -> None:
        """ Sets the art provider to be used by the notebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetCloseButton(self, page_idx, hasCloseButton) -> None:
        """ Sets whether a tab should display a close button or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the tab font.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetImageList(self, imageList: 'ImageList') -> None:
        """ Sets the image list for the AuiNotebook control.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetMeasuringFont(self, font: 'Font') -> None:
        """ Sets the font for calculating text measurements.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetMinMaxTabWidth(self, minTabWidth, maxTabWidth) -> None:
        """ Sets the minimum and/or the maximum tab widths for AuiNotebook when the
AUI_NB_TAB_FIXED_WIDTH style is defined.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetNavigatorIcon(self, bmp: 'Bitmap') -> None:
        """ Sets the icon used by the TabNavigatorWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetNormalFont(self, font: 'Font') -> None:
        """ Sets the normal font for drawing tab labels.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetPageBitmap(self, page_idx, bitmap) -> None:
        """ Sets the tab bitmap for the page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetPageImage(self, page, image) -> None:
        """ Sets the image index for the given page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetPageText(self, page_idx, text) -> None:
        """ Sets the tab label for the page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetPageTextColour(self, page_idx, colour) -> None:
        """ Sets the tab text colour for the page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetPageTooltip(self, page_idx, tooltip) -> None:
        """ Sets the tab tooltip for the page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetRenamable(self, page_idx, renamable) -> None:
        """ Sets whether a tab can be renamed via a left double-click or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetSashDClickUnsplit(self, unsplit: bool=True) -> None:
        """ Sets whether to unsplit a splitted AuiNotebook when double-clicking on a sash.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetSelectedFont(self, font: 'Font') -> None:
        """ Sets the selected tab font for drawing tab labels.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetSelection(self, new_page, force=False) -> None:
        """ Sets the page selection. Calling this method will generate a page change event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetSelectionToPage(self, page: AuiNotebookPage) -> None:
        """ Sets the selection based on the input page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetSelectionToWindow(self, win: 'Window') -> None:
        """ Sets the selection based on the input window win.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetTabCtrlHeight(self, height: int) -> None:
        """ Sets the tab height.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetUniformBitmapSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Ensures that all tabs will have the same height, even if some tabs donât have bitmaps.
Passing wx.DefaultSize to this method will instruct the control to use dynamic tab
height, which is the default behaviour. Under the default behaviour, when a tab with a
large bitmap is added, the tab controlâs height will automatically increase to accommodate
the larger bitmap.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def ShowWindowMenu(self) -> None:
        """ Shows the window menu for the active tab control associated with this
notebook, and returns True if a selection was made.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def Split(self, page, direction) -> None:
        """ Performs a split operation programmatically.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def UnSplit(self) -> None:
        """ Restores original view after a tab split.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def UnsplitDClick(self, part, sash_size, pos) -> None:
        """ Unsplit the AuiNotebook on sash double-click.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def UpdateHintWindowSize(self) -> None:
        """ Updates the AuiManager hint window size.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def UpdateTabCtrlHeight(self, force: bool=False) -> None:
        """ UpdateTabCtrlHeight does the actual tab resizing. Itâs meant
to be used internally.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """



EVT_CHILD_FOCUS: int

EVT_CLOSE: int

EVT_NAVIGATION_KEY: int

EVT_SIZE: int

LEFT: int

RIGHT: int

NOT_FOUND: int

DefaultSize: int

TOP: int

BOTTOM: int

class AuiTabCtrl(Control,AuiTabContainer):
    """ This is an actual wx.Window - derived window which can be used as a tab control in the normal sense.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.NO_BORDER|wx.WANTS_CHARS|wx.TAB_TRAVERSAL) -> None:
        """ Default class constructor.
Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def DoGetBestSize(self) -> None:
        """ Gets the size which best suits the window: for a control, it would be the
minimal size which doesnât truncate the control, for a panel - the same
size as it would have after a call to Fit().

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def GetDefaultBorder(self) -> None:
        """ Returns the default border style for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def GetPointedToTab(self) -> Any:
        """ Returns the page at which the mouse is pointing (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def IsDragging(self) -> None:
        """ Returns whether the user is dragging a tab with the mouse or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnButton(self, event: AuiNotebookEvent) -> None:
        """ Handles the EVT_AUINOTEBOOK_BUTTON event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnCaptureLost(self, event: MouseCaptureLostEvent) -> None:
        """ Handles the wx.EVT_MOUSE_CAPTURE_LOST event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnEnterWindow(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_ENTER_WINDOW event fof AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ Handles the wx.EVT_ERASE_BACKGROUND event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnKeyDown(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_KEY_DOWN event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnKeyDown2(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_KEY_DOWN event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnKillFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_KILL_FOCUS event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnLeaveWindow(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEAVE_WINDOW event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnLeftDClick(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEFT_DCLICK event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnLeftDown(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEFT_DOWN event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnLeftUp(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEFT_UP event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnMiddleDown(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_MIDDLE_DOWN event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnMiddleUp(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_MIDDLE_UP event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnMotion(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_MOTION event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ Handles the wx.EVT_PAINT event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnRightDown(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_RIGHT_DOWN event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnRightUp(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_RIGHT_UP event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_SET_FOCUS event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ Handles the wx.EVT_SIZE event for AuiTabCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def RestartTooltipTimer(self, wnd: 'Window') -> None:
        """ Starts a timer: when it fires, a tooltip will be shown on the notebook tab
the mouse is pointing at.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def ShowTooltip(self) -> None:
        """ Shows the tooltip on the tab.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def StopTooltipTimer(self) -> None:
        """ Stops the timer keeping track of tooltips and mouse movements on the tab area.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """



EVT_MOUSE_CAPTURE_LOST: int

EVT_ENTER_WINDOW: int

EVT_ERASE_BACKGROUND: int

EVT_KEY_DOWN: int

EVT_LEAVE_WINDOW: int

EVT_LEFT_DCLICK: int

EVT_LEFT_DOWN: int

EVT_LEFT_UP: int

EVT_MIDDLE_DOWN: int

EVT_MIDDLE_UP: int

EVT_MOTION: int

EVT_PAINT: int

EVT_RIGHT_DOWN: int

EVT_RIGHT_UP: int

EVT_SET_FOCUS: int

class AuiTabContainer:
    """ AuiTabContainer is a class which contains information about each tab.
It also can render an entire tab control to a specified DC.
Itâs not a window class itself, because this code will be used by
the AuiNotebook, where it is disadvantageous to have separate
windows for each tab control in the case of âdocked tabsâ.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
    """
    def __init__(self, auiNotebook: AuiNotebook) -> None:
        """ Default class constructor.
Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def AddButton(self, id, location, normal_bitmap=wx.NullBitmap, disabled_bitmap=wx.NullBitmap, name="") -> None:
        """ Adds a button in the tab area.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def AddPage(self, page, info) -> None:
        """ Adds a page to the tab control.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def ButtonHitTest(self, x, y, state_flags=AUI_BUTTON_STATE_HIDDEN|AUI_BUTTON_STATE_DISABLED) -> None:
        """ Tests if a button was hit.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def CloneButtons(self) -> None:
        """ Clones the tab area buttons when the AuiNotebook is being split.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def DoShowHide(self) -> None:
        """ This function shows the active window, then hides all of the other windows
(in that order).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def EnableTab(self, idx, enable=True) -> None:
        """ Enables/disables a tab in the AuiTabContainer.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def FindNextActiveTab(self, idx: int) -> None:
        """ Finds the next active tab in the AuiTabContainer.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetActivePage(self) -> None:
        """ Returns the current selected tab or wx.NOT_FOUND if none is selected.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetAGWFlags(self) -> None:
        """ Returns the tab art flags.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetArtProvider(self) -> None:
        """ Returns the current art provider being used.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetEnabled(self, idx: int) -> None:
        """ Returns whether a tab is enabled or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetHidden(self, idx: int) -> None:
        """ Returns whether a tab is hidden or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetIdxFromWindow(self, wnd: 'Window') -> None:
        """ Returns the tab index based on the window wnd associated with it.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetPage(self, idx: int) -> None:
        """ Returns the page specified by the given index.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetPageCount(self) -> None:
        """ Returns the number of pages in the AuiTabContainer.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetPages(self) -> None:
        """ Returns a list of all the pages in this AuiTabContainer.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetShownPageCount(self) -> None:
        """ Returns the number of pages shown in the AuiTabContainer.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetTabOffset(self) -> None:
        """ Returns the tab offset.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetWindowFromIdx(self, idx: int) -> None:
        """ Returns the window associated with the tab with index idx.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def HideTab(self, idx, hidden=True) -> None:
        """ hides/shows a tab in the AuiTabContainer.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def InsertPage(self, page, info, idx) -> None:
        """ Inserts a page in the tab control in the position specified by idx.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def IsTabVisible(self, tabPage, tabOffset, dc, wnd) -> None:
        """ Returns whether a tab is visible or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def MakeTabVisible(self, tabPage, win) -> None:
        """ Make the tab visible if it wasnât already.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def MovePage(self, page, new_idx) -> None:
        """ Moves a page in a new position specified by new_idx.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def RemoveButton(self, id: int) -> None:
        """ Removes a button from the tab area.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def RemovePage(self, wnd: 'Window') -> None:
        """ Removes a page from the tab control.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def Render(self, raw_dc, wnd) -> None:
        """ Renders the tab catalog to the specified wx.DC.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetActivePage(self, wndOrInt: 'Window') -> None:
        """ Sets the AuiNotebook active page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetAGWFlags(self, agwFlags: int) -> None:
        """ Sets the tab art flags.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetArtProvider(self, art: Any) -> None:
        """ Instructs AuiTabContainer to use art provider specified by parameter art
for all drawing calls. This allows pluggable look-and-feel features.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetMeasuringFont(self, font: 'Font') -> None:
        """ Sets the font for calculating text measurements.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetNoneActive(self) -> None:
        """ Sets all the tabs as inactive (non-selected).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetNormalFont(self, font: 'Font') -> None:
        """ Sets the normal font for drawing tab labels.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetSelectedFont(self, font: 'Font') -> None:
        """ Sets the selected tab font for drawing tab labels.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetTabOffset(self, offset: int) -> None:
        """ Sets the tab offset.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetTabRect(self, rect: 'Rect') -> None:
        """ Sets the tab area rectangle.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def TabHitTest(self, x, y) -> None:
        """ TabHitTest() tests if a tab was hit, passing the window pointer
back if that condition was fulfilled.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """



class AuiNotebookPage:
    """ A simple class which holds information about tab captions, bitmaps and
colours.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookPage.html
    """
    def __init__(self) -> None:
        """ Default class constructor.
Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookPage.html
        """

    def IsMultiline(self) -> None:
        """ Returns whether the tab contains multiline text.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookPage.html
        """



class TabNavigatorWindow(Dialog):
    """ This class is used to create a modal dialog that enables âSmart Tabbingâ,
similar to what you would get by hitting Alt + Tab on Windows.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
    """
    def __init__(self, parent, props, centreOnMouse=False) -> None:
        """ Default class constructor. Used internally.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def CloseDialog(self, returnId=wx.ID_OK) -> None:
        """ Closes the TabNavigatorWindow dialog, setting selection in AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def GetSelectedPage(self) -> None:
        """ Gets the page index that was selected when the dialog was closed.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnItemSelected(self, event: ListEvent) -> None:
        """ Handles the wx.EVT_LISTBOX_DCLICK event for the ListBox inside TabNavigatorWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnKeyUp(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_KEY_UP for the TabNavigatorWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnLeftDown(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEFT_DOWN event for self._panel.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnLeftUp(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEFT_UP event for self._panel.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnMotion(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_MOTION event for self._panel.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnNavigationKey(self, event: NavigationKeyEvent) -> None:
        """ Handles the wx.EVT_NAVIGATION_KEY for the TabNavigatorWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnPanelEraseBg(self, event: EraseEvent) -> None:
        """ Handles the wx.EVT_ERASE_BACKGROUND event for TabNavigatorWindow top panel.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnPanelPaint(self, event: PaintEvent) -> None:
        """ Handles the wx.EVT_PAINT event for TabNavigatorWindow top panel.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def PopulateListControl(self, book: AuiNotebook) -> None:
        """ Populates the TabNavigatorWindow listbox with a list of tabs.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """



EVT_LISTBOX_DCLICK: int

class TabFrame(Window):
    """ TabFrame is an interesting case. Itâs important that all child pages
of the multi-notebook control are all actually children of that control
(and not grandchildren). TabFrame facilitates this. There is one
instance of TabFrame for each tab control inside the multi-notebook.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
    """
    def __init__(self, parent) -> None:
        """ Default class constructor.
Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def DoGetClientSize(self) -> None:
        """ Returns the window client size.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def DoGetSize(self) -> None:
        """ Returns the window size.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def DoSetSize(self, x, y, width, height, flags=wx.SIZE_AUTO) -> None:
        """ Sets the position and size of the window in pixels. The flags
parameter indicates the interpretation of the other params if they are
equal to -1.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def DoSizing(self) -> None:
        """ Does the actual sizing of the tab control.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def SetTabCtrlHeight(self, h: int) -> None:
        """ Sets the tab control height.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def Show(self, show: bool=True) -> None:
        """ Shows/hides the window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def Update(self) -> None:
        """ Calling this method immediately repaints the invalidated area of the window
and all of its children recursively while this would usually only happen when
the flow of control returns to the event loop.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """



SIZE_AUTO: int

SIZE_AUTO_WIDTH: int

SIZE_AUTO_HEIGHT: int

SIZE_USE_EXISTING: int

SIZE_ALLOW_MINUS_ONE: int

SIZE_FORCE: int

class AuiNotebookEvent(CommandNotebookEvent):
    """ A specialized command event class for events sent by AuiNotebook.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookEvent.html
    """
    def __init__(self, command_type=None, win_id=0) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookEvent.html
        """

    def Allow(self) -> None:
        """ This is the opposite of Veto: it explicitly allows the event to be
processed. For most events it is not necessary to call this method as the
events are allowed anyhow but some are forbidden by default (this will
be mentioned in the corresponding event description).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookEvent.html
        """

    def GetNotifyEvent(self) -> None:
        """ Returns the actual NotifyEvent.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookEvent.html
        """

    def IsAllowed(self) -> None:
        """ Returns whether the event is allowed or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookEvent.html
        """

    def Veto(self) -> None:
        """ Prevents the change announced by this event from happening.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookEvent.html
        """



class AuiTabContainerButton:
    """ A simple class which holds information about tab buttons and their state.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainerButton.html
    """
    def __init__(self) -> None:
        """ Default class constructor.
Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainerButton.html
        """



class TabNavigatorProps:
    """ Data storage class for managing and providing access to TabNavigatorWindow properties.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorProps.html
    """
    def __init__(self) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorProps.html
        """

    Font: Any  # Sets/Gets the font for the L{TabNavigatorWindow}, an instance of wx.Font.
    Icon: Any  # Sets/Gets the icon for the L{TabNavigatorWindow}, an instance of wx.Bitmap.
    MinSize: Any  # Sets/Gets the minimum size for the L{TabNavigatorWindow}, an instance of wx.Size.



class CommandNotebookEvent(PyCommandEvent):
    """ A specialized command event class for events sent by AuiNotebook .

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
    """
    def __init__(self, command_type=None, win_id=0) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def GetDispatched(self) -> None:
        """ Returns whether the event was dispatched (used for automatic AuiNotebook ).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def GetDragSource(self) -> None:
        """ Returns the drag and drop source.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def GetLabel(self) -> None:
        """ Returns the label-itemtext (for EVT_AUINOTEBOOK_BEGIN | END_LABEL_EDIT only).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def GetOldSelection(self) -> None:
        """ Returns the page that was selected before the change, or -1 if none was
selected.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def GetSelection(self) -> None:
        """ Returns the currently selected page, or -1 if none was selected.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def IsEditCancelled(self) -> None:
        """ Returns the edit cancel flag (for EVT_AUINOTEBOOK_BEGIN | END_LABEL_EDIT only).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def SetDispatched(self, b: Any) -> None:
        """ Sets the event as dispatched (used for automatic AuiNotebook ).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def SetDragSource(self, s: Any) -> None:
        """ Sets the drag and drop source.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def SetEditCanceled(self, editCancelled: bool) -> None:
        """ Sets the edit cancel flag (for EVT_AUINOTEBOOK_BEGIN | END_LABEL_EDIT only).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def SetLabel(self, label: str) -> None:
        """ Sets the label. Useful only for EVT_AUINOTEBOOK_END_LABEL_EDIT.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def SetOldSelection(self, s: int) -> None:
        """ Sets the id of the page selected before the change.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def SetSelection(self, s: int) -> None:
        """ Sets the selection member variable.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """



