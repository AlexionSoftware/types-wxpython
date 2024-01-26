# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class UltimateListTextCtrl(ExpandoTextCtrl):
    """ Control used for in-place edit.

        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
    """
    def __init__(self, owner, itemEdit) -> None:
        """ Default class constructor.
For internal use: do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """

    def AcceptChanges(self) -> None:
        """ Accepts/refuses the changes made by the user.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """

    def Finish(self) -> None:
        """ Finish editing.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """

    def OnChar(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_CHAR event for UltimateListTextCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """

    def OnKeyUp(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_KEY_UP event for UltimateListTextCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """

    def OnKillFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_KILL_FOCUS event for UltimateListTextCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """

    def StopEditing(self) -> None:
        """ Suddenly stops the editing.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """



EVT_CHAR: int

EVT_KEY_UP: int

EVT_KILL_FOCUS: int

class UltimateListCtrl(Control):
    """ UltimateListCtrl is a class that mimics the behaviour of ListCtrl, with almost
the same base functionalities plus some more enhancements. This class does
not rely on the native control, as it is a full owner-drawn list control.

        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=0, validator=wx.DefaultValidator, name="UltimateListCtrl") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def Append(self, entry: Any) -> None:
        """ Append an item to the UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def Arrange(self, flag: ULC_ALIGN_DEFAULT) -> None:
        """ Arranges the items in icon or small icon view.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def AssignImageList(self, imageList, which) -> None:
        """ Assigns the image list associated with the control.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ClearAll(self) -> None:
        """ Deletes everything in UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ClearColumnImage(self, col: Any) -> None:
        """ Clears all the images in the specified column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ClientToScreen(self, x: int, y: int) -> None:
        """ Converts to screen coordinates from coordinates relative to this window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ClientToScreenXY(self, x, y) -> None:
        """ Converts to screen coordinates from coordinates relative to this window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def CreateOrDestroyFooterWindowAsNeeded(self) -> None:
        """ Creates or destroys the footer window depending on the window style flags.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def CreateOrDestroyHeaderWindowAsNeeded(self) -> None:
        """ Creates or destroys the header window depending on the window style flags.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DeleteAllColumns(self) -> None:
        """ Deletes all the column in UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DeleteAllItems(self) -> None:
        """ Deletes all items in the UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DeleteColumn(self, col: Any) -> None:
        """ Deletes the specified column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DeleteItem(self, item: Any) -> None:
        """ Deletes the specified item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DeleteItemWindow(self, itemOrId, col=0) -> None:
        """ Deletes the window associated to an item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DoGetBestSize(self) -> None:
        """ Gets the size which best suits the window: for a control, it would be the
minimal size which doesnât truncate the control, for a panel - the same size
as it would have after a call to Fit().

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DoLayout(self) -> None:
        """ Layouts the header, main and footer windows. This is an auxiliary method to avoid code
duplication.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def EditLabel(self, item: Any) -> None:
        """ Starts editing an item label.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def EnableItem(self, itemOrId, col=0, enable=True) -> None:
        """ Enables/disables an item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def EnableSelectionGradient(self, enable: bool=True) -> None:
        """ Globally enables/disables drawing of gradient selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def EnableSelectionVista(self, enable: bool=True) -> None:
        """ Globally enables/disables drawing of Windows Vista selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def EnsureVisible(self, item) -> None:
        """ Ensures this item is visible.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def FindItem(self, start, str, partial=False) -> None:
        """ Find an item whose label matches this string.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def FindItemAtPos(self, start, pt: Union[tuple[int, int], 'Point']) -> None:
        """ Find an item nearest this position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def FindItemData(self, start, data) -> None:
        """ Find an item whose data matches this data.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def Focus(self, idx: Any) -> None:
        """ Focus and show the given item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetAGWWindowStyleFlag(self) -> None:
        """ Returns the UltimateListCtrl AGW-specific style flag.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetBackgroundColour(self) -> None:
        """ Returns the background colour of the window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetBackgroundImage(self) -> None:
        """ Returns the UltimateListCtrl background image (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetCheckedItemCount(self, col=0) -> int:
        """ Returns the number of checked items in the given column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetClassDefaultAttributes(self, variant) -> None:
        """ Returns the default font and colours which are used by the control. This is
useful if you want to use the same font or colour in your own control as in
a standard control â which is a much better idea than hard coding specific
colours or fonts which might look completely out of place on the users system,
especially if it uses themes.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetColumn(self, col: Any) -> None:
        """ Returns information about this column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetColumnCount(self) -> None:
        """ Returns the total number of columns in the UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetColumnWidth(self, col: Any) -> None:
        """ Returns the column width for the input column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetCountPerPage(self) -> None:
        """ Returns the number of items that can fit vertically in the visible area
of the UltimateListCtrl (list or report view) or the total number of
items in the list control (icon or small icon view).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetDefaultBorder(self) -> None:
        """ Returns the default window border.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetDisabledTextColour(self) -> None:
        """ Returns the items disabled colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetDropTarget(self) -> None:
        """ Returns the associated drop target, which may be None.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetEditControl(self) -> None:
        """ Returns a pointer to the edit UltimateListTextCtrl if the item is being edited or
None otherwise (it is assumed that no more than one item may be edited
simultaneously).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetFirstGradientColour(self) -> None:
        """ Returns the first gradient colour for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetFirstSelected(self) -> None:
        """ Return first selected item, or -1 when none is selected.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetFocusedItem(self) -> None:
        """ Returns the currently focused item or -1 if none is focused.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetFooterHeight(self) -> None:
        """ Returns the UltimateListHeaderWindow height, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetForegroundColour(self) -> None:
        """ Returns the foreground colour of the window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetGradientStyle(self) -> None:
        """ Returns the gradient style for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetHeaderHeight(self) -> None:
        """ Returns the UltimateListHeaderWindow height, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetHyperTextFont(self) -> None:
        """ Returns the font used to render an hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetHyperTextNewColour(self) -> None:
        """ Returns the colour used to render a non-visited hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetHyperTextVisitedColour(self) -> None:
        """ Returns the colour used to render a visited hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetImageList(self, which: 'IMAGE_LIST_NORMAL') -> None:
        """ Returns the image list associated with the control.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItem(self, itemOrId, col=0) -> None:
        """ Returns the information about the input item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemBackgroundColour(self, item: Any) -> None:
        """ Returns the item background colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemCount(self) -> None:
        """ Returns the number of items in the UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemCustomRenderer(self, itemOrId, col=0) -> None:
        """ Returns the custom renderer used to draw the input item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemData(self, item: Any) -> None:
        """ Gets the application-defined data associated with this item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemFont(self, item: Any) -> None:
        """ Returns the item font.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemKind(self, itemOrId, col=0) -> None:
        """ Returns the item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemOverFlow(self, itemOrId, col=0) -> None:
        """ Returns if the item is in the overflow state.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemPosition(self, item: Any) -> None:
        """ Returns the position of the item, in icon or small icon view.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemPyData(self, item: Any) -> None:
        """ Returns the data for the item, which can be any Python object.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemRect(self, item, code=ULC_RECT_BOUNDS) -> None:
        """ Returns the rectangle representing the itemâs size and position, in physical
coordinates.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemSpacing(self, isSmall: bool=False) -> None:
        """ Returns the spacing between item texts and icons, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemState(self, item, stateMask) -> None:
        """ Returns the item state flags for the input item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemText(self, item: UltimateListItem) -> None:
        """ Returns the item text.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemTextColour(self, item: Any) -> None:
        """ Returns the item text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemVisited(self, itemOrId, col=0) -> None:
        """ Returns whether an hypertext item was visited.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemWindow(self, itemOrId, col=0) -> None:
        """ Returns the window associated to the item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemWindowEnabled(self, itemOrId, col=0) -> None:
        """ Returns whether the window associated to the item is enabled.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetNextItem(self, item, geometry=ULC_NEXT_ALL, state=ULC_STATE_DONTCARE) -> None:
        """ Searches for an item with the given geometry or state, starting from item
but excluding the item itself.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetNextSelected(self, item: Any) -> None:
        """ Returns subsequent selected items, or -1 when no more are selected.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetScrolledWin(self) -> None:
        """ Returns the header window owner.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetScrollPos(self, orientation: Any) -> None:
        """ Returns the scrollbar position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetScrollRange(self) -> None:
        """ Returns the scrollbar range in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetScrollThumb(self) -> None:
        """ Returns the scrollbar size in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetSecondGradientColour(self) -> None:
        """ Returns the second gradient colour for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetSelectedItemCount(self) -> None:
        """ Returns the number of selected items in UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetSubItemRect(self, item, subItem, code) -> None:
        """ Returns the rectangle representing the size and position, in physical coordinates,
of the given subitem, i.e. the part of the row item in the column subItem.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetTextColour(self) -> None:
        """ Returns the UltimateListCtrl foreground colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetTopItem(self) -> None:
        """ Gets the index of the topmost visible item when in list or report view.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetUserLineHeight(self) -> None:
        """ Returns the custom value for the UltimateListCtrl item height, if previously set with
SetUserLineHeight.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetViewRect(self) -> None:
        """ Returns the rectangle taken by all items in the control. In other words,
if the controls client size were equal to the size of this rectangle, no
scrollbars would be needed and no free space would be left.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetWaterMark(self) -> None:
        """ Returns the UltimateListCtrl watermark image (if any), displayed in the
bottom right part of the window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def HasAGWFlag(self, flag: Any) -> None:
        """ Returns True if the window has the given flag bit set.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def HasFooter(self) -> None:
        """ Returns True if UltimateListCtrl has a footer window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def HasHeader(self) -> None:
        """ Returns True if UltimateListCtrl has a header window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def HitTest(self, pointOrTuple: Any) -> None:
        """ HitTest method for a UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def InsertColumn(self, col, heading, format=ULC_FORMAT_LEFT, width=-1) -> None:
        """ Inserts a column into UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def InsertColumnInfo(self, col, item) -> None:
        """ Inserts a column into UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def InsertImageItem(self, index, imageIds, it_kind=0) -> None:
        """ Inserts an image item at the given location.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def InsertImageStringItem(self, index, label, imageIds, it_kind=0) -> None:
        """ Inserts an image+string item at the given location.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def InsertItem(self, info: UltimateListItem) -> None:
        """ Inserts an item into UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def InsertStringItem(self, index, label, it_kind=0) -> None:
        """ Inserts a string item at the given location.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def IsColumnShown(self, column: Any) -> None:
        """ Returns True if the input column is shown, False if it is hidden.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def IsItemChecked(self, itemOrId, col=0) -> None:
        """ Returns whether an item is checked or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def IsItemEnabled(self, itemOrId, col=0) -> None:
        """ Returns whether an item is enabled or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def IsItemHyperText(self, itemOrId, col=0) -> None:
        """ Returns whether an item is hypertext or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def IsSelected(self, idx: Any) -> None:
        """ Returns True if the item is selected.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def IsVirtual(self) -> None:
        """ Returns True if the UltimateListCtrl has the ULC_VIRTUAL style set.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemAttr(self, item: Any) -> None:
        """ This function may be overloaded in the derived class for a control with
ULC_VIRTUAL style. It should return the attribute for the specified
item or None to use the default appearance parameters.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemCheck(self, item: Any) -> None:
        """ This function may be overloaded in the derived class for a control with
ULC_VIRTUAL style. It should return whether a checkbox-like item or
a radiobutton-like item is checked or unchecked.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemColumnCheck(self, item: Any, column=0) -> None:
        """ This function must be overloaded in the derived class for a control with
ULC_VIRTUAL and ULC_REPORT style. It should return whether a
checkbox-like item or a radiobutton-like item in the column header is checked
or unchecked.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemColumnImage(self, item: Any, column=0) -> None:
        """ This function must be overloaded in the derived class for a control with
ULC_VIRTUAL and ULC_REPORT style. It should return a Python list of
indexes representing the images associated to the input item or an empty list
for no images.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemColumnKind(self, item, column=0) -> None:
        """ This function must be overloaded in the derived class for a control with
ULC_VIRTUAL style. It should return the item kind for the input item in
the header window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemImage(self, item: Any) -> None:
        """ This function must be overloaded in the derived class for a control with
ULC_VIRTUAL style having an image list (if the control doesnât have an
image list, it is not necessary to overload it). It should return a Python
list of indexes representing the images associated to the input item or an
empty list for no images.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemKind(self, item: Any) -> None:
        """ This function must be overloaded in the derived class for a control with
ULC_VIRTUAL style. It should return the item kind for the input item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemText(self, item, col) -> None:
        """ This function must be overloaded in the derived class for a control with
ULC_VIRTUAL style. It should return the string containing the text of
the given column for the specified item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemTextColour(self, item, col) -> None:
        """ This function must be overloaded in the derived class for a control with
ULC_VIRTUAL style. It should return a wx.Colour object or None for
the default color.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemToolTip(self, item, col) -> None:
        """ This function must be overloaded in the derived class for a control with
ULC_VIRTUAL style. It should return the string containing the text of
the tooltip for the specified item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnInternalIdle(self) -> None:
        """ This method is normally only used internally, but sometimes an application
may need it to implement functionality that should not be disabled by an
application defining an OnIdle handler in a derived class.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_SET_FOCUS event for UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ Handles the wx.EVT_SIZE event for UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def PopupMenu(self, menu, pos=wx.DefaultPosition) -> None:
        """ Pops up the given menu at the specified coordinates, relative to this window,
and returns control when the user has dismissed the menu. If a menu item is
selected, the corresponding menu event is generated and will be processed as
usual. If the coordinates are not specified, the current mouse cursor position
is used.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def Refresh(self, eraseBackground=True, rect=None) -> None:
        """ Causes this window, and all of its children recursively (except under wxGTK1
where this is not implemented), to be repainted.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def RefreshItem(self, item: Any) -> None:
        """ Redraws the given item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def RefreshItems(self, itemFrom, itemTo) -> None:
        """ Redraws the items between itemFrom and itemTo.
The starting item must be less than or equal to the ending one.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ScreenToClient(self, x: int, y: int) -> None:
        """ Converts from screen to client window coordinates.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ScreenToClientXY(self, x, y) -> None:
        """ Converts from screen to client window coordinates.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ScrollList(self, dx, dy) -> None:
        """ Scrolls the UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def Select(self, idx, on=True) -> None:
        """ Selects/deselects an item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetAGWWindowStyleFlag(self, style: int) -> None:
        """ Sets the UltimateListCtrl AGW-specific style flag.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetBackgroundColour(self, colour: NullColour) -> None:
        """ Changes the background colour of UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetBackgroundImage(self, image: Optional[None]=None) -> None:
        """ Sets the UltimateListCtrl background image.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetColumn(self, col, item) -> None:
        """ Sets information about this column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetColumnCustomRenderer(self, col=0, renderer=None) -> None:
        """ Associate a custom renderer to this columnâs header.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetColumnImage(self, col, image) -> None:
        """ Sets one or more images to the specified column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetColumnShown(self, column, shown=True) -> None:
        """ Sets the specified column as shown or hidden.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetColumnToolTip(self, col, tip) -> None:
        """ Sets the tooltip for the column header

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetColumnWidth(self, col, width: 'LIST_AUTOSIZE') -> None:
        """ Sets the column width.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetCursor(self, cursor: Any) -> None:
        """ Sets the windowâs cursor.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetDisabledTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the items disabled colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetDropTarget(self, dropTarget: DropTarget) -> None:
        """ Associates a drop target with this window.
If the window already has a drop target, it is deleted.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetFirstGradientColour(self, colour: Optional[None]=None) -> None:
        """ Sets the first gradient colour for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetFocus(self) -> None:
        """ This sets the window to receive keyboard input.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the UltimateListCtrl font.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetFooterCustomRenderer(self, renderer: Optional[Any]=None) -> None:
        """ Associate a custom renderer with the footer - all columns will use it.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetFooterHeight(self, height: None) -> None:
        """ Sets the UltimateListHeaderWindow height, in pixels. This overrides the default
footer window size derived from RendererNative. If height is None, the
default behaviour is restored.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetForegroundColour(self, colour: NullColour) -> None:
        """ Changes the foreground colour of UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetGradientStyle(self, vertical: Any=0) -> None:
        """ Sets the gradient style for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetHeaderCustomRenderer(self, renderer: Optional[Any]=None) -> None:
        """ Associate a custom renderer with the header - all columns will use it.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetHeaderHeight(self, height: None) -> None:
        """ Sets the UltimateListHeaderWindow height, in pixels. This overrides the default
header window size derived from RendererNative. If height is None, the
default behaviour is restored.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetHyperTextFont(self, font: 'Font') -> None:
        """ Sets the font used to render hypertext items.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetHyperTextNewColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used to render a non-visited hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetHyperTextVisitedColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used to render a visited hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetImageList(self, imageList, which) -> None:
        """ Sets the image list associated with the control.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItem(self, info: UltimateListItem) -> None:
        """ Sets the information about the input item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemBackgroundColour(self, item, col) -> None:
        """ Sets the item background colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemColumnImage(self, item, column, image) -> None:
        """ Sets a Python list of image indexes associated with the item in the input
column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemCount(self, count: Any) -> None:
        """ Sets the total number of items we handle.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemCustomRenderer(self, itemOrId, col=0, renderer=None) -> None:
        """ Associate a custom renderer to this item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemData(self, item, data) -> None:
        """ Sets the application-defined data associated with this item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemFont(self, item, f) -> None:
        """ Sets the item font.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemHyperText(self, itemOrId, col=0, hyper=True) -> None:
        """ Sets whether the item is hypertext or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemImage(self, item, image, selImage=-1) -> None:
        """ Sets a Python list of image indexes associated with the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemKind(self, itemOrId, col=0, kind=0) -> None:
        """ Sets the item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemOverFlow(self, itemOrId, col=0, over=True) -> None:
        """ Sets the item in the overflow/non overflow state.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemPosition(self, item, pos) -> None:
        """ Sets the position of the item, in icon or small icon view.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemPyData(self, item, pyData) -> None:
        """ Sets the data for the item, which can be any Python object.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemSpacing(self, spacing, isSmall=False) -> None:
        """ Sets the spacing between item texts and icons.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemState(self, item, state, stateMask) -> None:
        """ Sets the item state flags for the input item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemText(self, item, text) -> None:
        """ Sets the item text.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemTextColour(self, item, col) -> None:
        """ Sets the item text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemVisited(self, itemOrId, col=0, visited=True) -> None:
        """ Sets whether an hypertext item was visited or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemWindow(self, itemOrId, col=0, wnd=None, expand=False) -> None:
        """ Sets the window for the given item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemWindowEnabled(self, itemOrId, col=0, enable=True) -> None:
        """ Enables/disables the window associated to the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetScrollPos(self, orientation, pos, refresh=True) -> None:
        """ Sets the scrollbar position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetSecondGradientColour(self, colour: Optional[None]=None) -> None:
        """ Sets the second gradient colour for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetSingleStyle(self, style, add=True) -> None:
        """ Adds or removes a single window style.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetStringItem(self, index, col, label, imageIds=[], it_kind=0) -> None:
        """ Sets a string or image at the given location.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetTextColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets the UltimateListCtrl foreground colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetUserLineHeight(self, height: Any) -> None:
        """ Sets a custom value for the UltimateListCtrl item height.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetWaterMark(self, watermark: Optional[None]=None) -> None:
        """ Sets the UltimateListCtrl watermark image to be displayed in the bottom
right part of the window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SortItems(self, func: Any = None) -> None:
        """ Call this function to sort the items in the UltimateListCtrl. Sorting is done
using the specified function func. This function must have the
following prototype:

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def Update(self) -> None:
        """ Calling this method immediately repaints the invalidated area of the window
and all of its children recursively while this would usually only happen when
the flow of control returns to the event loop.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """



EVT_SET_FOCUS: int

EVT_SIZE: int

IMAGE_LIST_NORMAL: int

IMAGE_LIST_SMALL: int

IMAGE_LIST_STATE: int

LIST_AUTOSIZE: int

LIST_AUTOSIZE_USEHEADER: int

SYS_COLOUR_HIGHLIGHT: int

HORIZONTAL: int

VERTICAL: int

class UltimateListItem(Object):
    """ This class stores information about a UltimateListCtrl item or column.

        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
    """
    def __init__(self, item: Optional[None]=None) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def Attributes(self) -> None:
        """ Returns the associated attributes if they exist, or create a new UltimateListItemAttr
structure and associate it with this item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def Check(self, checked: bool=True) -> None:
        """ Checks/unchecks an item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def CheckFooter(self, checked: bool=True) -> None:
        """ Checks/unchecks a footer item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def Clear(self) -> None:
        """ Resets the item state to the default.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def ClearAttributes(self) -> None:
        """ Deletes the item attributes if they have been stored.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def DeleteWindow(self) -> None:
        """ Deletes the window associated to the item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ Enables or disables the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetAlign(self) -> None:
        """ Returns the alignment for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetAttributes(self) -> None:
        """ Returns the associated UltimateListItemAttr attributes.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetBackgroundColour(self) -> None:
        """ Returns the background colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetColumn(self) -> None:
        """ Returns the zero-based column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetCustomRenderer(self) -> None:
        """ Returns the custom renderer associated with this item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetData(self) -> None:
        """ Returns client data associated with the control.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFont(self) -> None:
        """ Returns the item font.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterAlign(self) -> None:
        """ Returns the alignment for the footer item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterBackgroundColour(self) -> None:
        """ Returns the footer item background colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterFont(self) -> None:
        """ Returns the footer item font.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterFormat(self) -> None:
        """ Returns the footer item format.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterImage(self) -> None:
        """ Returns the zero-based index of the image associated with the footer item into
the image list.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterKind(self) -> None:
        """ Returns the footer item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterText(self) -> None:
        """ Returns the footer text.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterTextColour(self) -> None:
        """ Returns the footer item text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFormat(self) -> None:
        """ Returns the header item format.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetId(self) -> None:
        """ Returns the zero-based item position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetImage(self) -> None:
        """ Returns a Python list with the zero-based indexes of the images associated
with the item into the image list.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetKind(self) -> None:
        """ Returns the item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetMask(self) -> None:
        """ Returns a bit mask indicating which fields of the structure are valid.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetOverFlow(self) -> None:
        """ Returns if the item is in the overflow state.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetPyData(self) -> None:
        """ Returns data for the item, which can be any Python object.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetState(self) -> None:
        """ Returns a bit field representing the state of the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetText(self) -> None:
        """ Returns the label/header text.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetTextColour(self) -> None:
        """ Returns the text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetToolTip(self) -> None:
        """ Returns the label/header tooltip.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetVisited(self) -> None:
        """ Returns whether an hypertext item was visited or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetWidth(self) -> None:
        """ Returns the column width.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetWindow(self) -> None:
        """ Returns the window associated to the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetWindowEnabled(self) -> None:
        """ Returns whether the associated window is enabled or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetWindowSize(self) -> None:
        """ Returns the associated window size.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def HasAttributes(self) -> None:
        """ Returns True if the item has attributes associated with it.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def Init(self) -> None:
        """ Initializes an empty UltimateListItem.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def IsChecked(self) -> None:
        """ Returns whether the item is checked or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def IsEnabled(self) -> None:
        """ Returns True if the item is enabled.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def IsFooterChecked(self) -> None:
        """ Returns whether the footer item is checked or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def IsHyperText(self) -> None:
        """ Returns whether the item is hypetext or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def IsShown(self) -> None:
        """ Returns True if the item is shown, or False if it is hidden.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_SET_FOCUS event for the window associated to an item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetAlign(self, align: ULC_FORMAT_LEFT) -> None:
        """ Sets the alignment for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ Sets the background colour for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetColumn(self, col: Any) -> None:
        """ Sets the zero-based column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetCustomRenderer(self, renderer: Any) -> None:
        """ Associate a custom renderer to this item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetData(self, data: Any) -> None:
        """ Sets client data for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the font for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterAlign(self, align) -> None:
        """ Sets the alignment for the footer item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ Sets the background colour for the footer item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterFont(self, font: 'Font') -> None:
        """ Sets the font for the footer item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterFormat(self, format: Any) -> None:
        """ Sets the footer item format.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterImage(self, image: Any) -> None:
        """ Sets the zero-based index of the image associated with the footer item into the
image list.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterKind(self, kind) -> None:
        """ Sets the footer item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterText(self, text: Any) -> None:
        """ Sets the text label for the footer item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ Sets the text colour for the footer item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetHyperText(self, hyper: bool=True) -> None:
        """ Sets whether the item is hypertext or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetId(self, id: Any) -> None:
        """ Sets the zero-based item position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetImage(self, image: Any) -> None:
        """ Sets the zero-based indexes of the images associated with the item into the
image list.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetKind(self, kind: Any) -> None:
        """ Sets the item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetMask(self, mask: ULC_MASK_STATE) -> None:
        """ Sets the mask of valid fields.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetOverFlow(self, over: bool=True) -> None:
        """ Sets the item in the overflow/non overflow state.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetPyData(self, pyData) -> None:
        """ Sets data for the item, which can be any Python object.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetShown(self, shown: bool=True) -> None:
        """ Sets an item as shown/hidden.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetState(self, state: ULC_STATE_DONTCARE) -> None:
        """ Sets the item state flags.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetStateMask(self, stateMask: Any) -> None:
        """ Sets the bitmask that is used to determine which of the state flags are
to be set.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetText(self, text: Any) -> None:
        """ Sets the text label for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ Sets the text colour for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetToolTip(self, text: Any) -> None:
        """ Sets the tooltip text for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetVisited(self, visited: bool=True) -> None:
        """ Sets whether an hypertext item was visited or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetWidth(self, width: Any) -> None:
        """ Sets the column width.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetWindow(self, wnd, expand=False) -> None:
        """ Sets the window associated to the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetWindowEnabled(self, enable: bool=True) -> None:
        """ Sets whether the associated window is enabled or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """



class UltimateListHeaderWindow(Control):
    """ This class holds the header window for UltimateListCtrl.

        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
    """
    def __init__(self, win, id, owner, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, validator=wx.DefaultValidator, name="UltimateListCtrlcolumntitles", isFooter=False) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def AdjustDC(self, dc: 'DC') -> None:
        """ Shifts the wx.DC origin to match the position of the main window horizontal
scrollbar: this allows us to always use logical coordinates.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def DoGetBestSize(self) -> None:
        """ Gets the size which best suits the window: for a control, it would be the
minimal size which doesnât truncate the control, for a panel - the same size
as it would have after a call to Fit().

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def DrawCurrent(self) -> None:
        """ Force the redrawing of the column window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def DrawTextFormatted(self, dc, text, rect) -> None:
        """ Draws the item text, correctly formatted.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def GetOwner(self) -> None:
        """ Returns the header window owner, an instance of UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def GetTextHeight(self) -> None:
        """ Returns the column text height, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def GetWindowHeight(self) -> None:
        """ Returns the UltimateListHeaderWindow height, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def HandleColumnCheck(self, column, pos) -> None:
        """ Handles the case in which a column contains a checkbox-like item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def HitTestColumn(self, x, y) -> None:
        """ HitTest method for column headers.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def IsColumnShown(self, column: Any) -> None:
        """ Returns True if the input column is shown, False if it is hidden.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def OnEnterWindow(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_ENTER_WINDOW event for UltimateListHeaderWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def OnInternalIdle(self) -> None:
        """ This method is normally only used internally, but sometimes an application
may need it to implement functionality that should not be disabled by an
application defining an OnIdle handler in a derived class.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def OnLeaveWindow(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEAVE_WINDOW event for UltimateListHeaderWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def OnMouse(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_MOUSE_EVENTS event for UltimateListHeaderWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ Handles the wx.EVT_PAINT event for UltimateListHeaderWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_SET_FOCUS event for UltimateListHeaderWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def SendListEvent(self, eventType, pos) -> None:
        """ Sends a UltimateListEvent for the parent window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def SetCustomRenderer(self, renderer: Optional[Any]=None) -> None:
        """ Associate a custom renderer with the header - all columns will use it

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """



EVT_ENTER_WINDOW: int

EVT_LEAVE_WINDOW: int

EVT_MOUSE_EVENTS: int

EVT_PAINT: int

NOT_FOUND: int

class PyImageList:
    """ A PyImageList contains a list of images. Images can have masks for
transparent drawing, and can be made from a variety of sources including
bitmaps and icons.

        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
    """
    def __init__(self, width, height, mask=True, initialCount=1, style=IL_VARIABLE_SIZE) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def Add(self, bitmap: 'Bitmap') -> None:
        """ Adds a new image or images using a bitmap.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def AddIcon(self, icon: Icon) -> None:
        """ Adds a new image using an icon.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def AddWithColourMask(self, bitmap, maskColour) -> None:
        """ Adds a new image or images using a bitmap and a colour mask.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def Draw(self, index, dc, x, y, flags, solidBackground=True) -> None:
        """ Draws a specified image onto a device context.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def GetBitmap(self, index: Any) -> None:
        """ Returns the bitmap corresponding to the given index, or NullBitmap
if the index is invalid.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def GetIcon(self, index: Any) -> None:
        """ Returns the icon corresponding to the given index, or NullIcon
if the index is invalid.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def GetImageCount(self) -> None:
        """ Returns the number of images in the list.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def GetSize(self, index: Any) -> None:
        """ Retrieves the size of an image in the list.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def Remove(self, index: Any) -> None:
        """ Removes the image at the given position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def RemoveAll(self) -> None:
        """ Removes all the images in the list.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def Replace(self, index, bitmap) -> None:
        """ Replaces the existing image with the new bitmap.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def ReplaceIcon(self, index, icon) -> None:
        """ Replaces the existing image with the new icon.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """



IMAGELIST_DRAW_NORMAL: int

IMAGELIST_DRAW_TRANSPARENT: int

IMAGELIST_DRAW_SELECTED: int

IMAGELIST_DRAW_FOCUSED: int

class UltimateListMainWindow(ScrolledWindow):
    """ This is the main widget implementation of UltimateListCtrl.

        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
    """
    def __init__(self, parent, id, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=0, name="listctrlmainwindow") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def AutoCheckChild(self, isChecked, column) -> None:
        """ Checks/unchecks all the items.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def AutoToggleChild(self, column: Any) -> None:
        """ Toggles all the items.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def CacheLineData(self, line: UltimateListLineData) -> None:
        """ Saves the current line attributes.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ChangeCurrent(self, current: Any) -> None:
        """ Changes the current line to the specified one.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def CheckItem(self, item, checked=True, sendEvent=True) -> None:
        """ Actually checks/uncheks an item, sending (eventually) the two
events EVT_LIST_ITEM_CHECKING / EVT_LIST_ITEM_CHECKED.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DeleteAllItems(self) -> None:
        """ Deletes all items in the UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DeleteColumn(self, col: Any) -> None:
        """ Deletes the specified column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DeleteEverything(self) -> None:
        """ Deletes all items in the UltimateListCtrl, resetting column widths to zero.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DeleteItem(self, lindex: Any) -> None:
        """ Deletes the specified item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DeleteItemWindow(self, item: UltimateListItem) -> None:
        """ Deletes the window associated to an item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DoDeleteAllItems(self) -> None:
        """ Actually performs the deletion of all the items.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DoGetBestSize(self) -> None:
        """ Gets the size which best suits the window: for a control, it would be the
minimal size which doesnât truncate the control, for a panel - the same size
as it would have after a call to Fit().

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DragFinish(self, event: MouseEvent) -> None:
        """ A drag and drop operation has just finished.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DrawCheckbox(self, dc, x, y, kind, checked, enabled) -> None:
        """ Draws the item checkbox/radiobutton image.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DrawDnDArrow(self) -> None:
        """ Draws a drag and drop visual representation of an arrow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DrawImage(self, index, dc, x, y, enabled) -> None:
        """ Draws one of the item images.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def EditLabel(self, item: UltimateListItem) -> None:
        """ Starts editing an item label.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def EnableItem(self, item, enable=True) -> None:
        """ Enables/disables an item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def EnableSelectionGradient(self, enable: bool=True) -> None:
        """ Globally enables/disables drawing of gradient selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def EnableSelectionVista(self, enable: bool=True) -> None:
        """ Globally enables/disables drawing of Windows Vista selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def EnsureVisible(self, index: Any) -> None:
        """ Ensures this item is visible.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def FindItem(self, start, string, partial=False) -> None:
        """ Find an item whose label matches this string.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def FindItemAtPos(self, pt: Union[tuple[int, int], 'Point']) -> None:
        """ Find an item nearest this position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def FindItemData(self, start, data) -> None:
        """ Find an item whose data matches this data.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetBackgroundImage(self) -> None:
        """ Returns the UltimateListCtrl background image (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetCheckboxImageSize(self) -> None:
        """ Returns the checkbox/radiobutton image size.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetCheckedItemCount(self, col: Any=0) -> int:
        """ Returns the number of checked items in the given column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetColumn(self, col: Any) -> None:
        """ Returns information about this column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetColumnCount(self) -> None:
        """ Returns the total number of columns in the UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetColumnCustomRenderer(self, col: Any) -> None:
        """ Returns the custom renderer used to draw the column header

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetColumnWidth(self, col: Any) -> None:
        """ Returns the column width for the input column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetControlBmp(self, checkbox=True, checked=False, enabled=True, x=16, y=16) -> None:
        """ Returns a native looking checkbox or radio button bitmap.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetCountPerPage(self) -> None:
        """ Returns the number of items that can fit vertically in the visible area
of the UltimateListCtrl (list or report view) or the total number of
items in the list control (icon or small icon view).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetDisabledTextColour(self) -> None:
        """ Returns the items disabled colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetDummyLine(self) -> None:
        """ Returns a dummy line.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetFirstGradientColour(self) -> None:
        """ Returns the first gradient colour for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetGradientStyle(self) -> None:
        """ Returns the gradient style for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetHeaderWidth(self) -> None:
        """ Returns the header window width, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetHighlightBrush(self) -> None:
        """ Returns the brush to use for the item highlighting.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetHyperTextFont(self) -> None:
        """ Returns the font used to render an hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetHyperTextNewColour(self) -> None:
        """ Returns the colour used to render a non-visited hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetHyperTextVisitedColour(self) -> None:
        """ Returns the colour used to render a visited hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetImageSize(self, index: Any) -> None:
        """ Returns the image size for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItem(self, item, col=0) -> None:
        """ Returns the information about the input item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemCount(self) -> None:
        """ Returns the number of items in the UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemCustomRenderer(self, item: UltimateListItem) -> None:
        """ Returns the custom renderer used to draw the input item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemKind(self, item: UltimateListItem) -> None:
        """ Returns the item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemOverFlow(self, item: UltimateListItem) -> None:
        """ Returns if the item is in the overflow state.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemPosition(self, item: Any) -> None:
        """ Returns the position of the item, in icon or small icon view.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemRect(self, item: Any) -> None:
        """ Returns the rectangle representing the itemâs size and position, in physical
coordinates.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemSpacing(self, isSmall: bool=False) -> None:
        """ Returns the spacing between item texts and icons, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemState(self, item, stateMask) -> None:
        """ Returns the item state flags for the input item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemText(self, item: UltimateListItem) -> None:
        """ Returns the item text.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemTextSize(self, item: UltimateListItem) -> None:
        """ Returns the item width, in pixels, considering only the item text.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemVisited(self, item: UltimateListItem) -> None:
        """ Returns whether an hypertext item was visited.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemWidthWithImage(self, item: UltimateListItem) -> None:
        """ Returns the item width, in pixels, considering the item text and its images.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemWindow(self, item: UltimateListItem) -> None:
        """ Returns the window associated to the item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemWindowEnabled(self, item: UltimateListItem) -> None:
        """ Returns whether the window associated to the item is enabled.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLine(self, n: Any) -> None:
        """ Returns the line data for the given index.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineCheckboxRect(self, line: UltimateListLineData) -> None:
        """ Returns the line client rectangle for the item checkbox image only.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineHeight(self, item: Optional[None]=None) -> None:
        """ Returns the line height for a specific item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineHighlightRect(self, line: UltimateListLineData) -> None:
        """ Returns the line client rectangle when the line is highlighted.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineIconRect(self, line: UltimateListLineData) -> None:
        """ Returns the line client rectangle for the item image only.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineLabelRect(self, line: UltimateListLineData, col=0) -> None:
        """ Returns the line client rectangle for the item text only.
Note this is the full column width unless an image or
checkbox exists. It is not the width of the text itself

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineRect(self, line: UltimateListLineData) -> None:
        """ Returns the line client rectangle.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineSize(self, line: UltimateListLineData) -> None:
        """ Returns the size of the total line client rectangle.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineY(self, line: UltimateListLineData) -> None:
        """ Returns the line y position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetListCtrl(self) -> None:
        """ Returns the parent widget, an instance of UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetMainWindowOfCompositeControl(self) -> None:
        """ Returns the UltimateListMainWindow parent.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetNextActiveItem(self, item, down=True) -> None:
        """ Returns the next active item. Used Internally at present.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetNextItem(self, item, geometry=ULC_NEXT_ALL, state=ULC_STATE_DONTCARE) -> None:
        """ Searches for an item with the given geometry or state, starting from item
but excluding the item itself.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetRuleColour(self) -> None:
        """ Returns the colour to be used for drawing the horizontal and vertical rules.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetSecondGradientColour(self) -> None:
        """ Returns the second gradient colour for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetSelectedItemCount(self) -> None:
        """ Returns the number of selected items in UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetSubItemRect(self, item, subItem) -> None:
        """ Returns the rectangle representing the size and position, in physical coordinates,
of the given subitem, i.e. the part of the row item in the column subItem.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetTextLength(self, s: Any) -> None:
        """ Returns the text width for the input string.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetTotalWidth(self) -> None:
        """ Returns the total width of the columns in UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetUserLineHeight(self) -> None:
        """ Returns the custom value for the UltimateListMainWindow item height, if previously set with
SetUserLineHeight.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetViewRect(self) -> None:
        """ Returns the rectangle taken by all items in the control. In other words,
if the controls client size were equal to the size of this rectangle, no
scrollbars would be needed and no free space would be left.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetVisibleLinesRange(self) -> None:
        """ Returns the range of visible items on screen.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetWaterMark(self) -> None:
        """ Returns the UltimateListCtrl watermark image (if any), displayed in the
bottom right part of the window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HandleHyperLink(self, item: UltimateListItem) -> None:
        """ Handles the hyperlink items, sending the EVT_LIST_ITEM_HYPERLINK event.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HasAGWFlag(self, flag: Any) -> None:
        """ Returns True if the window has the given flag bit set.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HasCurrent(self) -> None:
        """ Returns True if the current item has been set, either programmatically
or by user intervention.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HasFocus(self) -> None:
        """ Returns True if the window has focus.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HasFooter(self) -> None:
        """ Returns True if the footer window is shown.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HasHeader(self) -> None:
        """ Returns True if the header window is shown.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HideWindows(self) -> None:
        """ Hides the windows associated to the items. Used internally.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HighlightAll(self, on: bool=True) -> None:
        """ Highlights/unhighlights all the lines in UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HighlightLine(self, line, highlight=True) -> None:
        """ Highlights a line in UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HighlightLines(self, lineFrom, lineTo, highlight=True) -> None:
        """ Highlights a range of lines in UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HitTest(self, x, y) -> None:
        """ HitTest method for a UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HitTestLine(self, line, x, y) -> None:
        """ HitTest method for a UltimateListCtrl line.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def Init(self) -> None:
        """ Initializes the UltimateListMainWindow widget.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def InReportView(self) -> None:
        """ Returns True if the window is in report mode.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def InsertColumn(self, col, item) -> None:
        """ Inserts a column into UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def InsertItem(self, item: UltimateListItem) -> None:
        """ Inserts an item into UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def InTileView(self) -> None:
        """ Returns True if the window is in tile mode (partially implemented).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsColumnShown(self, column: Any) -> None:
        """ Returns True if the input column is shown, False if it is hidden.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsEmpty(self) -> None:
        """ Returns True if the window has no items in it.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsHighlighted(self, line: UltimateListLineData) -> None:
        """ Returns True if the input line is highlighted.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsItemChecked(self, item: UltimateListItem) -> None:
        """ Returns whether an item is checked or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsItemEnabled(self, item: UltimateListItem) -> None:
        """ Returns whether an item is enabled or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsItemHyperText(self, item: UltimateListItem) -> None:
        """ Returns whether an item is hypertext or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsSingleSel(self) -> None:
        """ Returns True if we are in single selection mode, False if multi selection.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsVirtual(self) -> None:
        """ Returns True if the window has the ULC_VIRTUAL style set.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def MoveToFocus(self) -> None:
        """ Brings the current item into view.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def MoveToItem(self, item: UltimateListItem) -> None:
        """ Scrolls the input item into view.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnArrowChar(self, newCurrent, event) -> None:
        """ Handles the keyboard arrows key events.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnChar(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_CHAR event for UltimateListMainWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnChildFocus(self, event: ChildFocusEvent) -> None:
        """ Handles the wx.EVT_CHILD_FOCUS event for UltimateListMainWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnCompareItems(self, line1, line2) -> None:
        """ Returns whether 2 lines have the same index.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ Handles the wx.EVT_ERASE_BACKGROUND event for UltimateListMainWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnHoverTimer(self, event: TimerEvent) -> None:
        """ Handles the wx.EVT_TIMER event for UltimateListMainWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnKeyDown(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_KEY_DOWN event for UltimateListMainWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnKeyUp(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_KEY_UP event for UltimateListMainWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnKillFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_KILL_FOCUS event for UltimateListMainWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnMouse(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_MOUSE_EVENTS event for UltimateListMainWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ Handles the wx.EVT_PAINT event for UltimateListMainWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnRenameAccept(self, itemEdit, value) -> None:
        """ Called by UltimateListTextCtrl, to accept the changes and to send the
EVT_LIST_END_LABEL_EDIT event.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnRenameCancelled(self, itemEdit) -> None:
        """ Called by UltimateListTextCtrl, to cancel the changes and to send the
EVT_LIST_END_LABEL_EDIT event.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnRenameTimer(self) -> None:
        """ The timer for renaming has expired. Start editing.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnScroll(self, event: ScrollEvent) -> None:
        """ Handles the wx.EVT_SCROLLWIN event for UltimateListMainWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_SET_FOCUS event for UltimateListMainWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def PaintWaterMark(self, dc: 'DC') -> None:
        """ Draws a watermark at the bottom right of UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def RecalculatePositions(self, noRefresh: bool=False) -> None:
        """ Recalculates all the items positions, and sets the scrollbars positions
too.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def RefreshAfter(self, lineFrom: Any) -> None:
        """ Redraws all the lines after the input one.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def RefreshAll(self) -> None:
        """ Refreshes the entire UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def RefreshLine(self, line: UltimateListLineData) -> None:
        """ Redraws the input line.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def RefreshLines(self, lineFrom, lineTo) -> None:
        """ Redraws a range of lines in UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def RefreshSelected(self) -> None:
        """ Redraws the selected lines.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ResetCurrent(self) -> None:
        """ Resets the current item to None.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ResetLineDimensions(self, force: bool=False) -> None:
        """ Resets the line dimensions, so that client rectangles and positions are
recalculated.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ResetTextControl(self) -> None:
        """ Called by UltimateListTextCtrl when it marks itself for deletion.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ResetVisibleLinesRange(self, reset: bool=False) -> None:
        """ Forces us to recalculate the range of visible lines.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ResizeColumns(self) -> None:
        """ If ULC_AUTOSIZE_FILL was passed to UltimateListCtrl.SetColumnWidth() then
that columnâs width will be expanded to fill the window on a resize event.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ReverseHighlight(self, line: UltimateListLineData) -> None:
        """ Toggles the line state and refreshes it.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ScrollList(self, dx, dy) -> None:
        """ Scrolls the UltimateListCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SendNotify(self, line, command, point=wx.DefaultPosition, col=0) -> None:
        """ Actually sends a UltimateListEvent.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetBackgroundImage(self, image: None) -> None:
        """ Sets the UltimateListCtrl background image.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetColumn(self, col, item) -> None:
        """ Sets information about this column.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetColumnCustomRenderer(self, col=0, renderer=None) -> None:
        """ Associate a custom renderer to this columnâs header

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetColumnWidth(self, col, width: 'LIST_AUTOSIZE') -> None:
        """ Sets the column width.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetDisabledTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the items disabled colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetFirstGradientColour(self, colour: Optional[None]=None) -> None:
        """ Sets the first gradient colour for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Overridden base class virtual to reset the line height when the font changes.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetGradientStyle(self, vertical: Any=0) -> None:
        """ Sets the gradient style for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetHyperTextFont(self, font: 'Font') -> None:
        """ Sets the font used to render hypertext items.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetHyperTextNewColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used to render a non-visited hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetHyperTextVisitedColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used to render a visited hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetImageList(self, imageList, which) -> None:
        """ Sets the image list associated with the control.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetImageListCheck(self, sizex, sizey, imglist=None) -> None:
        """ Sets the checkbox/radiobutton image list.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItem(self, item: UltimateListItemData) -> None:
        """ Sets information about the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemCount(self, count: UltimateListCtrl) -> None:
        """ This method can only be used with virtual UltimateListCtrl. It is used to
indicate to the control the number of items it contains. After calling it,
the main program should be ready to handle calls to various item callbacks
(such as UltimateListCtrl.OnGetItemText()) for all items in the range from 0 to count.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemCustomRenderer(self, item, renderer=None) -> None:
        """ Associate a custom renderer to this item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemHyperText(self, item, hyper=True) -> None:
        """ Sets whether the item is hypertext or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemKind(self, item, kind) -> None:
        """ Sets the item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemOverFlow(self, item, over=True) -> None:
        """ Sets the item in the overflow/non overflow state.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemSpacing(self, spacing, isSmall=False) -> None:
        """ Sets the spacing between item texts and icons.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemState(self, litem, state, stateMask) -> None:
        """ Sets the item state flags for the input item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemStateAll(self, state, stateMask) -> None:
        """ Sets the item state flags for all the items.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemText(self, item, value) -> None:
        """ Sets the item text.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemVisited(self, item, visited=True) -> None:
        """ Sets whether an hypertext item was visited.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemWindow(self, item, wnd, expand=False) -> None:
        """ Sets the window for the given item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemWindowEnabled(self, item, enable=True) -> None:
        """ Enables/disables the window associated to the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetReportView(self, inReportView: bool) -> None:
        """ Sets whether UltimateListCtrl is in report view or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetSecondGradientColour(self, colour: Optional[None]=None) -> None:
        """ Sets the second gradient colour for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetUserLineHeight(self, height: Any) -> None:
        """ Sets a custom value for the UltimateListMainWindow item height.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetWaterMark(self, watermark: None) -> None:
        """ Sets the UltimateListCtrl watermark image to be displayed in the bottom
right part of the window.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SortItems(self, func: Any = None) -> None:
        """ Call this function to sort the items in the UltimateListCtrl. Sorting is done
using the specified function func. This function must have the
following prototype:

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def TileBackground(self, dc: 'DC') -> None:
        """ Tiles the background image to fill all the available area.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def UpdateCurrent(self) -> None:
        """ Updates the current line selection.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """



EVT_CHILD_FOCUS: int

EVT_ERASE_BACKGROUND: int

EVT_TIMER: int

EVT_KEY_DOWN: int

EVT_SCROLLWIN: int

class UltimateListItemAttr:
    """ Represents the attributes (colour, font, â¦) of a UltimateListCtrl
UltimateListItem.

        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
    """
    def __init__(self, colText=wx.NullColour, colBack=wx.NullColour, font=wx.NullFont, enabled=True, footerColText=wx.NullColour, footerColBack=wx.NullColour, footerFont=wx.NullFont) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ Enables or disables the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def GetBackgroundColour(self) -> None:
        """ Returns the currently set background colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def GetFont(self) -> None:
        """ Returns the currently set item font.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def GetFooterBackgroundColour(self) -> None:
        """ Returns the currently set background colour for a footer item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def GetFooterFont(self) -> None:
        """ Returns the currently set font for a footer item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def GetFooterTextColour(self) -> None:
        """ Returns the currently set text colour for a footer item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def GetTextColour(self) -> None:
        """ Returns the currently set text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def HasBackgroundColour(self) -> None:
        """ Returns True if the currently set background colour is valid.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def HasFont(self) -> None:
        """ Returns True if the currently set font is valid.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def HasFooterBackgroundColour(self) -> None:
        """ Returns True if the currently set background colour for the footer item
is valid.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def HasFooterFont(self) -> None:
        """ Returns True if the currently set font for the footer item
is valid.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def HasFooterTextColour(self) -> None:
        """ Returns True if the currently set text colour for the footer item
is valid.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def HasTextColour(self) -> None:
        """ Returns True if the currently set text colour is valid.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def IsEnabled(self) -> None:
        """ Returns True if the item is enabled.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def SetBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ Sets a new background colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets a new font for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def SetFooterBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ Sets a new footer item background colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def SetFooterFont(self, font: 'Font') -> None:
        """ Sets a new font for the footer item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def SetFooterTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ Sets a new footer item text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def SetTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ Sets a new text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """



class UltimateListEvent(CommandListEvent):
    """ A list event holds information about events associated with UltimateListCtrl
objects.

        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListEvent.html
    """
    def __init__(self, commandTypeOrEvent=None, winid=0) -> None:
        """ Default class constructor.
For internal use: do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListEvent.html
        """

    def Allow(self) -> None:
        """ This is the opposite of Veto: it explicitly allows the event to be processed.
For most events it is not necessary to call this method as the events are
allowed anyhow but some are forbidden by default (this will be mentioned
in the corresponding event description).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListEvent.html
        """

    def GetNotifyEvent(self) -> None:
        """ Returns the actual NotifyEvent.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListEvent.html
        """

    def IsAllowed(self) -> None:
        """ Returns True if the change is allowed ( Veto hasnât been called) or
False otherwise (if it was).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListEvent.html
        """

    def Veto(self) -> None:
        """ Prevents the change announced by this event from happening.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListEvent.html
        """



class UltimateListLineData:
    """ A simple class which holds line geometries for UltimateListCtrl.

        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
    """
    def __init__(self, owner: UltimateListCtrl) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def CalculateSize(self, dc, spacing) -> None:
        """ Calculates the line size and item positions.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def Check(self, index, checked=True) -> None:
        """ Checks/unchecks an item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def Draw(self, line, dc) -> None:
        """ Draws the line on the specified device context.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def DrawHorizontalGradient(self, dc, rect, hasfocus) -> None:
        """ Gradient fill from colour 1 to colour 2 from left to right.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def DrawInReportMode(self, dc, line, rect, rectHL, highlighted, current, enabled, oldPN, oldBR) -> None:
        """ Draws the line on the specified device context when the parent UltimateListCtrl
is in report mode.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def DrawTextFormatted(self, dc, text, row, col, itemRect, overflow) -> None:
        """ Draws the item text, correctly formatted.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def DrawVerticalGradient(self, dc, rect, hasfocus) -> None:
        """ Gradient fill from colour 1 to colour 2 from top to bottom.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def DrawVistaRectangle(self, dc, rect, hasfocus) -> None:
        """ Draws the selected item(s) with the Windows Vista style.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetAttr(self) -> None:
        """ Returns an instance of UltimateListItemAttr associated with the first item
in the line.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetHeight(self) -> None:
        """ Returns the line height, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetImage(self, index: Any=0) -> None:
        """ Returns a Python list with the zero-based indexes of the images associated
with the item into the image list.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetItem(self, index, info) -> None:
        """ Returns information about the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetKind(self, index: Any=0) -> None:
        """ Returns the item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetMode(self) -> None:
        """ Returns the current highlighting mode.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetText(self, index: Any) -> None:
        """ Returns the item text at the position index.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetToolTip(self, index: Any) -> None:
        """ Returns the item tooltip at the position index.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetWidth(self) -> None:
        """ Returns the line width.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetX(self) -> None:
        """ Returns the line x position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetY(self) -> None:
        """ Returns the line y position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def HasImage(self, col=0) -> None:
        """ Returns True if the first item in the line has at least one image
associated with it.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def HasMode(self, mode: Any) -> None:
        """ Returns True if the parent UltimateListCtrl has the window
style specified by mode.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def HasText(self) -> None:
        """ Returns True if the text of first item in the line is not the empty
string.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def HideItemWindow(self, item: UltimateListItem) -> None:
        """ If the input item has a window associated with it, hide it.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def Highlight(self, on: bool) -> None:
        """ Sets the current line as highlighted or not highlighted.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def InitItems(self, num: Any) -> None:
        """ Initializes the list of items.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def InReportView(self) -> None:
        """ Returns True if the parent UltimateListCtrl is in report view.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def IsChecked(self, index: Any) -> None:
        """ Returns whether the item is checked or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def IsHighlighted(self) -> None:
        """ Returns True if the line is highlighted.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def IsVirtual(self) -> None:
        """ Returns True if the parent UltimateListCtrl has the ULC_VIRTUAL style set.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def ResetDimensions(self) -> None:
        """ Resets the line dimensions (client rectangle).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def ReverseHighlight(self) -> None:
        """ Reverses the line highlighting, switching it off if it was on and vice-versa.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetAttr(self, attr: UltimateListItemAttr) -> None:
        """ Sets an instance of UltimateListItemAttr to the first item in the line.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetAttributes(self, dc, attr, highlighted) -> None:
        """ Sets various attributes to the input device context.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetColour(self, index, c) -> None:
        """ Sets the text colour for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetHeight(self, height: Any) -> None:
        """ Sets the line height.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetImage(self, index, image) -> None:
        """ Sets the zero-based indexes of the images associated with the item into the
image list.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetItem(self, index, info) -> None:
        """ Sets information about the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetKind(self, index, kind=0) -> None:
        """ Sets the item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetPosition(self, x, y, spacing) -> None:
        """ Sets the line position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetReportView(self, inReportView: bool) -> None:
        """ Sets whether UltimateListLineData is in report view or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetText(self, index, s) -> None:
        """ Sets the item text at the position index.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetToolTip(self, index, s) -> None:
        """ Sets the item tooltip at the position index.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetWidth(self, width: Any) -> None:
        """ Sets the line width.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetX(self, x: int) -> None:
        """ Sets the line x position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetY(self, y: int) -> None:
        """ Sets the line y position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """



class UltimateListItemData:
    """ A simple class which holds information about UltimateListItem visual
attributes (client rectangles, positions, etcâ¦).

        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
    """
    def __init__(self, owner: UltimateListCtrl) -> None:
        """ Default class constructor

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def Check(self, checked: bool=True) -> None:
        """ Checks/unchecks an item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def DeleteWindow(self) -> None:
        """ Deletes the window associated to the item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ Enables or disables the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetAttr(self) -> None:
        """ Returns the item attributes.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetBackgroundColour(self) -> None:
        """ Returns the currently set background colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetColour(self) -> None:
        """ Returns the currently set text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetCustomRenderer(self) -> None:
        """ Returns the custom renderer associated with this item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetFont(self) -> None:
        """ Returns the currently set font.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetHeight(self) -> None:
        """ Returns the item height, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetImage(self) -> None:
        """ Returns a Python list with the zero-based indexes of the images associated
with the item into the image list.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetItem(self, info: UltimateListItemData) -> None:
        """ Returns information about the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetKind(self) -> None:
        """ Returns the item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetOverFlow(self) -> None:
        """ Returns if the item is in the overflow state.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetText(self) -> None:
        """ Returns the item text.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetTextForMeasuring(self) -> None:
        """ Returns the item text or a simple string if the item text is the
empty string.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetToolTip(self) -> None:
        """ Returns the item tooltip.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetVisited(self) -> None:
        """ Returns whether an hypertext item was visited or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetWidth(self) -> None:
        """ Returns the item width, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetWindow(self) -> None:
        """ Returns the window associated to the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetWindowEnabled(self) -> None:
        """ Returns whether the associated window is enabled or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetWindowSize(self) -> None:
        """ Returns the associated window size.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetX(self) -> None:
        """ Returns the item x position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetY(self) -> None:
        """ Returns the item y position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def HasBackgroundColour(self) -> None:
        """ Returns True if the currently set background colour is valid.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def HasColour(self) -> None:
        """ Returns True if the currently set text colour is valid.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def HasFont(self) -> None:
        """ Returns True if the currently set font is valid.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def HasImage(self) -> None:
        """ Returns True if the item has at least one image associated with it.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def HasText(self) -> None:
        """ Returns True if the item text is not the empty string.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def Init(self) -> None:
        """ Initializes the item data structure.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def IsChecked(self) -> None:
        """ Returns whether the item is checked or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def IsEnabled(self) -> None:
        """ Returns True if the item is enabled, False if it is disabled.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def IsHit(self, x, y) -> None:
        """ Returns True if the input position is inside the item client rectangle.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def IsHyperText(self) -> None:
        """ Returns whether the item is hypetext or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetAttr(self, attr: UltimateListItemAttr) -> None:
        """ Sets the item attributes.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the background colour for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the text colour for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetCustomRenderer(self, renderer: Any) -> None:
        """ Associate a custom renderer to this item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetData(self, data: Any) -> None:
        """ Sets client data for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the text font for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetHyperText(self, hyper: bool=True) -> None:
        """ Sets whether the item is hypertext or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetImage(self, image: Any) -> None:
        """ Sets the zero-based indexes of the images associated with the item into the
image list.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetItem(self, info: UltimateListItemData) -> None:
        """ Sets information about the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetKind(self, kind: Any) -> None:
        """ Sets the item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetOverFlow(self, over: bool=True) -> None:
        """ Sets the item in the overflow/non overflow state.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetPosition(self, x, y) -> None:
        """ Sets the item position.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetSize(self, width, height) -> None:
        """ Sets the item size.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetText(self, text: Any) -> None:
        """ Sets the text label for the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetToolTip(self, tooltip: Any) -> None:
        """ Sets the tooltip for the item

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetVisited(self, visited: bool=True) -> None:
        """ Sets whether an hypertext item was visited or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetWindow(self, wnd, expand=False) -> None:
        """ Sets the window associated to the item.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetWindowEnabled(self, enable: bool=True) -> None:
        """ Sets whether the associated window is enabled or not.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """



class CommandListEvent(PyCommandEvent):
    """ A list event holds information about events associated with UltimateListCtrl
objects.

        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
    """
    def __init__(self, commandTypeOrEvent=None, winid=0) -> None:
        """ Default class constructor.
For internal use: do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetCacheFrom(self) -> None:
        """ Returns the first item which the list control advises us to cache.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetCacheTo(self) -> None:
        """ Returns the last item (inclusive) which the list control advises us to cache.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetColumn(self) -> None:
        """ Returns the column position: it is only used with COL events.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetData(self) -> None:
        """ Returns the item data.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetImage(self) -> None:
        """ Returns the item image.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetIndex(self) -> None:
        """ Returns the item index.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetItem(self) -> None:
        """ Returns the item itself.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetKeyCode(self) -> None:
        """ Returns the key code if the event is a keypress event.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetLabel(self) -> None:
        """ Returns the (new) item label for EVT_LIST_END_LABEL_EDIT event.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetMask(self) -> None:
        """ Returns the item mask.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetPoint(self) -> None:
        """ Returns the position of the mouse pointer if the event is a drag event.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetText(self) -> None:
        """ Returns the item text.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def IsEditCancelled(self) -> None:
        """ Returns True if it the label editing has been cancelled by the user
( GetLabel returns an empty string in this case but it doesnât allow
the application to distinguish between really cancelling the edit and
the admittedly rare case when the user wants to rename it to an empty
string).

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def SetEditCanceled(self, editCancelled: bool) -> None:
        """ Sets the item editing as cancelled/not cancelled.

            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    Index: None  # See GetIndex



ULC_ALIGN_DEFAULT: int

ULC_ALIGN_SNAP_TO_GRID: int

ULC_VRULES: int

ULC_HRULES: int

ULC_ICON: int

ULC_SMALL_ICON: int

ULC_LIST: int

ULC_REPORT: int

ULC_ALIGN_TOP: int

ULC_ALIGN_LEFT: int

ULC_AUTOARRANGE: int

ULC_VIRTUAL: int

ULC_EDIT_LABELS: int

ULC_NO_HEADER: int

ULC_NO_SORT_HEADER: int

ULC_SINGLE_SEL: int

ULC_SORT_ASCENDING: int

ULC_SORT_DESCENDING: int

ULC_TILE: int

ULC_NO_HIGHLIGHT: int

ULC_STICKY_HIGHLIGHT: int

ULC_STICKY_NOSELEVENT: int

ULC_SEND_LEFTCLICK: int

ULC_HAS_VARIABLE_ROW_HEIGHT: int

ULC_AUTO_CHECK_CHILD: int

ULC_AUTO_TOGGLE_CHILD: int

ULC_AUTO_CHECK_PARENT: int

ULC_SHOW_TOOLTIPS: int

ULC_HOT_TRACKING: int

ULC_BORDER_SELECT: int

ULC_TRACK_SELECT: int

ULC_HEADER_IN_ALL_VIEWS: int

ULC_NO_FULL_ROW_SELECT: int

ULC_FOOTER: int

ULC_USER_ROW_HEIGHT: int

ULC_FORMAT_LEFT: int

ULC_FORMAT_RIGHT: int

ULC_FORMAT_CENTRE: int

ULC_FORMAT_CENTER: int

ULC_MASK_STATE: int

ULC_MASK_TEXT: int

ULC_MASK_IMAGE: int

ULC_MASK_DATA: int

ULC_MASK_WIDTH: int

ULC_MASK_FORMAT: int

ULC_MASK_FONTCOLOUR: int

ULC_MASK_FONT: int

ULC_MASK_BACKCOLOUR: int

ULC_MASK_KIND: int

ULC_MASK_ENABLE: int

ULC_MASK_CHECK: int

ULC_MASK_HYPERTEXT: int

ULC_MASK_WINDOW: int

ULC_MASK_PYDATA: int

ULC_MASK_SHOWN: int

ULC_MASK_RENDERER: int

ULC_MASK_OVERFLOW: int

ULC_MASK_FOOTER_TEXT: int

ULC_MASK_FOOTER_IMAGE: int

ULC_MASK_FOOTER_FORMAT: int

ULC_MASK_FOOTER_FONT: int

ULC_MASK_FOOTER_CHECK: int

ULC_MASK_FOOTER_KIND: int

ULC_STATE_DONTCARE: int

ULC_STATE_DROPHILITED: int

ULC_STATE_FOCUSED: int

ULC_STATE_SELECTED: int

ULC_STATE_CUT: int

ULC_STATE_DISABLED: int

ULC_STATE_FILTERED: int

ULC_STATE_INUSE: int

ULC_STATE_PICKED: int

ULC_STATE_SOURCE: int

