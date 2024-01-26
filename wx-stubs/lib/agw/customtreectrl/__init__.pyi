# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class CommandTreeEvent(CommandEvent):
    """ CommandTreeEvent is a special subclassing of CommandEvent.

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
    """
    def __init__(self, evtType, evtId, item=None, evtKey=None, point=None, label=None, **kwargs) -> None:
        """ Default class constructor.
For internal use: do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetItem(self) -> None:
        """ Gets the item on which the operation was performed or the newly selected
item for EVT_TREE_SEL_CHANGED and EVT_TREE_SEL_CHANGING events.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetKeyCode(self) -> None:
        """ Returns the virtual key code. ASCII events return normal ASCII values, while
non-ASCII events return values such as wx.WXK_LEFT for the left cursor key.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetKeyEvent(self) -> None:
        """ Returns the keyboard data (for EVT_TREE_KEY_DOWN event only).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetLabel(self) -> None:
        """ Returns the item text (for EVT_TREE_BEGIN_LABEL_EDIT and
EVT_TREE_END_LABEL_EDIT events only).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetOldItem(self) -> None:
        """ Returns the previously selected item for EVT_TREE_SEL_CHANGED and
EVT_TREE_SEL_CHANGING events.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetPoint(self) -> None:
        """ Returns the point where the mouse was when the drag operation started
(for EVT_TREE_BEGIN_DRAG and EVT_TREE_BEGIN_RDRAG events only)
or the click position.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetToolTip(self) -> None:
        """ Returns the tooltip for the item (for EVT_TREE_ITEM_GETTOOLTIP events).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def IsEditCancelled(self) -> None:
        """ Returns the edit cancel flag (for EVT_TREE_BEGIN_LABEL_EDIT and
EVT_TREE_END_LABEL_EDIT events only).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetEditCanceled(self, editCancelled: bool) -> None:
        """ Sets the edit cancel flag (for EVT_TREE_BEGIN_LABEL_EDIT and
EVT_TREE_END_LABEL_EDIT events only).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetItem(self, item: GenericTreeItem) -> None:
        """ Sets the item on which the operation was performed or the newly selected
item for EVT_TREE_SEL_CHANGED and EVT_TREE_SEL_CHANGING events.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetKeyEvent(self, event: CommandTreeEvent) -> None:
        """ Sets the keyboard data (for EVT_TREE_KEY_DOWN event only).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetLabel(self, label: str) -> None:
        """ Sets the item text (for EVT_TREE_BEGIN_LABEL_EDIT and
EVT_TREE_END_LABEL_EDIT events only).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetOldItem(self, item: GenericTreeItem) -> None:
        """ Returns the previously selected item for EVT_TREE_SEL_CHANGED and
EVT_TREE_SEL_CHANGING events.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetPoint(self, pt: Union[tuple[int, int], 'Point']) -> None:
        """ Sets the point where the mouse was when the drag operation started
(for EVT_TREE_BEGIN_DRAG and EVT_TREE_BEGIN_RDRAG events only)
or the click position.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetToolTip(self, toolTip) -> None:
        """ Sets the tooltip for the item (for EVT_TREE_ITEM_GETTOOLTIP events).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """



WXK_LEFT: int

class CustomTreeCtrl(ScrolledWindow):
    """ CustomTreeCtrl is a class that mimics the behaviour of TreeCtrl, with almost the
same base functionalities plus some more enhancements. This class does not rely on
the native control, as it is a full owner-drawn tree control.

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=TR_DEFAULT_STYLE, validator=wx.DefaultValidator, name="CustomTreeCtrl") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AcceptsFocus(self) -> None:
        """ Can this window be given focus by mouse click?

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AddRoot(self, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, on_the_right=True) -> 'GenericTreeItem':
        """ Adds a root item to the CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AdjustMyScrollbars(self) -> None:
        """ Internal method used to adjust the ScrolledWindow scrollbars.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AppendItem(self, parentId, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, on_the_right=True) -> 'GenericTreeItem':
        """ Appends an item as a last child of its parent.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AppendSeparator(self, parentId: GenericTreeItem) -> None:
        """ Appends an horizontal line separator as a last child of its parent.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AssignButtonsImageList(self, imageList: 'ImageList') -> None:
        """ Assigns the button image list.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AssignImageList(self, imageList: 'ImageList') -> None:
        """ Assigns the normal image list.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AssignLeftImageList(self, imageList: 'ImageList') -> None:
        """ Assigns the image list for CustomTreeCtrl filled with images to be used on
the leftmost part of the client area. Any item can have a leftmost image associated
with it.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AssignStateImageList(self, imageList: 'ImageList') -> None:
        """ Assigns the state image list.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AutoCheckChild(self, item, checked) -> None:
        """ Transverses the tree and checks/unchecks the items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AutoCheckParent(self, item, checked) -> None:
        """ Traverses up the tree and checks/unchecks parent items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AutoToggleChild(self, item: GenericTreeItem) -> None:
        """ Transverses the tree and toggles the items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CalculateLevel(self, item, dc, level, y, align=0) -> None:
        """ Calculates the level of an item inside the tree hierarchy.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CalculateLineHeight(self) -> None:
        """ Calculates the base height for all lines in the tree.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CalculatePositions(self) -> None:
        """ Calculates all the positions of the visible items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CalculateSize(self, item, dc, level=-1, align=0) -> None:
        """ Calculates overall position and size of an item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CheckChilds(self, item, checked=True) -> None:
        """ Programmatically check/uncheck item children.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CheckItem(self, item, checked=True) -> None:
        """ Actually checks/uncheks an item, sending (eventually) the two
events EVT_TREE_ITEM_CHECKING and EVT_TREE_ITEM_CHECKED.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CheckItem2(self, item, checked=True, torefresh=False) -> None:
        """ Used internally to avoid EVT_TREE_ITEM_CHECKED events.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CheckSameLevel(self, item, checked=False) -> None:
        """ Uncheck radio items which are on the same level of the checked one.
Used internally.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ChildrenClosing(self, item: GenericTreeItem) -> None:
        """ We are about to destroy the item children.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Collapse(self, item: GenericTreeItem) -> None:
        """ Collapse an item, sending a EVT_TREE_ITEM_COLLAPSING and
EVT_TREE_ITEM_COLLAPSED events.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CollapseAndReset(self, item: GenericTreeItem) -> None:
        """ Collapse the given item and deletes its children.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Delete(self, item: GenericTreeItem) -> None:
        """ Deletes an item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DeleteAllItems(self) -> None:
        """ Deletes all items in the CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DeleteChildren(self, item: GenericTreeItem) -> None:
        """ Delete all the itemâs children.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DeleteItemWindow(self, item: GenericTreeItem) -> None:
        """ Deletes the window associated to an item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DoGetBestSize(self) -> None:
        """ Gets the size which best suits the window: for a control, it would be the
minimal size which doesnât truncate the control, for a panel - the same size
as it would have after a call to Fit().

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DoInsertItem(self, parentId, previous, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, separator=False, on_the_right=True) -> None:
        """ Actually inserts an item in the tree.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DoSelectItem(self, item, unselect_others=True, extended_select=False, from_key=False) -> None:
        """ Actually selects/unselects an item, sending EVT_TREE_SEL_CHANGING and
EVT_TREE_SEL_CHANGED events.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DrawHorizontalGradient(self, dc, rect, hasfocus) -> None:
        """ Gradient fill from colour 1 to colour 2 from left to right.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DrawVerticalGradient(self, dc, rect, hasfocus) -> None:
        """ Gradient fill from colour 1 to colour 2 from top to bottom.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DrawVistaRectangle(self, dc, rect, hasfocus) -> None:
        """ Draws the selected item(s) with the Windows Vista style.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Edit(self, item: GenericTreeItem) -> None:
        """ Internal function. Starts the editing of an item label, sending a
EVT_TREE_BEGIN_LABEL_EDIT event.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def EditLabel(self, item: GenericTreeItem) -> None:
        """ Starts editing an item label.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def EnableChildren(self, item, enable=True) -> None:
        """ Enables/disables the item children.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def EnableItem(self, item, enable=True, torefresh=True) -> None:
        """ Enables/disables an item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def EnableSelectionGradient(self, enable: bool=True) -> None:
        """ Globally enables/disables drawing of gradient selections.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def EnableSelectionVista(self, enable: bool=True) -> None:
        """ Globally enables/disables drawing of Windows Vista selections.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def EnsureVisible(self, item: GenericTreeItem) -> None:
        """ Scrolls and/or expands items to ensure that the given item is visible.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Expand(self, item: GenericTreeItem) -> None:
        """ Expands an item, sending a EVT_TREE_ITEM_EXPANDING and
EVT_TREE_ITEM_EXPANDED events.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ExpandAll(self) -> None:
        """ Expands all CustomTreeCtrl items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ExpandAllChildren(self, item: GenericTreeItem) -> None:
        """ Expands all the items children of the input item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def FillArray(self, item, array=[]) -> None:
        """ Internal function. Used to populate an array of selected items when
the style TR_MULTIPLE is used.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def FindItem(self, idParent, prefixOrig) -> None:
        """ Finds the first item starting with the given prefix after the given parent.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Freeze(self) -> None:
        """ Freeze CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetAGWWindowStyleFlag(self) -> None:
        """ Returns the CustomTreeCtrl style.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetBackgroundImage(self) -> None:
        """ Returns the CustomTreeCtrl background image (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetBorderPen(self) -> None:
        """ Returns the pen used to draw the selected item border.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetBoundingRect(self, item, textOnly=False) -> None:
        """ Retrieves the rectangle bounding the item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetButtonsImageList(self) -> None:
        """ Returns the buttons image list associated with CustomTreeCtrl (from
which application-defined button images are taken).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetChildrenCount(self, item, recursively=True) -> int:
        """ Returns the item children count.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetConnectionPen(self) -> None:
        """ Returns the pen used to draw the connecting lines between items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetControlBmp(self, checkbox=True, checked=False, enabled=True, x=16, y=16) -> None:
        """ Returns a native looking checkbox or radio button bitmap.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetCount(self) -> None:
        """ Returns the global number of items in the tree.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetDisabledColour(self) -> None:
        """ Returns the colour for items in a disabled state.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetDragFullScreen(self) -> None:
        """ Returns whether built-in drag/drop will be full screen or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetEditControl(self) -> None:
        """ Returns a reference to the edit TreeTextCtrl if the item is being edited or
None otherwise (it is assumed that no more than one item may be edited
simultaneously).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetFirstChild(self, item: GenericTreeItem) -> None:
        """ Returns the itemâs first child and an integer value âcookieâ.
Call GetNextChild for the next child using this very âcookieâ return
value as an input.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetFirstGradientColour(self) -> None:
        """ Returns the first gradient colour for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetFirstVisibleItem(self) -> None:
        """ Returns the first visible item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetGradientStyle(self) -> None:
        """ Returns the gradient style for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetHilightFocusColour(self) -> None:
        """ Returns the colour used to highlight focused selected items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetHilightNonFocusColour(self) -> None:
        """ Returns the colour used to highlight unfocused selected items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetHyperTextFont(self) -> None:
        """ Returns the font used to render hypertext items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetHyperTextNewColour(self) -> None:
        """ Returns the colour used to render a non-visited hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetHyperTextVisitedColour(self) -> None:
        """ Returns the colour used to render a visited hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetImageList(self) -> None:
        """ Returns the normal image list associated with CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetImageListCheck(self) -> None:
        """ Returns the image list used to build the check/radio buttons in CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetIndent(self) -> None:
        """ Returns the item indentation, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItem3StateValue(self, item: GenericTreeItem) -> None:
        """ Gets the state of a 3-state checkbox item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemBackgroundColour(self, item: GenericTreeItem) -> None:
        """ Returns the item background colour.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemFont(self, item: GenericTreeItem) -> None:
        """ Returns the item font.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemImage(self, item, which=TreeItemIcon_Normal) -> None:
        """ Returns the item image.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemLeftImage(self, item: GenericTreeItem) -> None:
        """ Returns the item leftmost image, i.e. the image associated to the item on the leftmost
part of the CustomTreeCtrl client area.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemParent(self, item: GenericTreeItem) -> Optional['GenericTreeItem']:
        """ Returns the item parent (can be None for root items).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemSize(self, item: GenericTreeItem) -> None:
        """ Returns the horizontal space available in CustomTreeCtrl, in pixels, to draw this item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemText(self, item: GenericTreeItem) -> str:
        """ Returns the item text.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemTextColour(self, item: GenericTreeItem) -> None:
        """ Returns the item text colour or separator horizontal line colour.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemType(self, item: GenericTreeItem) -> None:
        """ Returns the item type.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemVisited(self, item: GenericTreeItem) -> None:
        """ Returns whether an hypertext item was visited.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemWindow(self, item: GenericTreeItem) -> None:
        """ Returns the window associated to the item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemWindowEnabled(self, item: GenericTreeItem) -> None:
        """ Returns whether the window associated to the item is enabled.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetLastChild(self, item: GenericTreeItem) -> None:
        """ Returns the item last child.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetLeftImageList(self) -> None:
        """ Returns the image list for CustomTreeCtrl filled with images to be used on
the leftmost part of the client area. Any item can have a leftmost image associated
with it.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetLineHeight(self, item: GenericTreeItem) -> None:
        """ Returns the line height for the given item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetMaxWidth(self, respect_expansion_state: bool=True) -> None:
        """ Returns the maximum width of the CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNext(self, item: GenericTreeItem) -> None:
        """ Returns the next item. Only for internal use right now.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNextActiveItem(self, item, down=True) -> None:
        """ Returns the next active item. Used Internally at present.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNextChild(self, item, cookie) -> None:
        """ Returns the itemâs next child.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNextExpanded(self, item: 'GenericTreeItem') -> None:
        """ Returns the next expanded item after the input one.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNextShown(self, item: GenericTreeItem) -> None:
        """ Returns the next displayed item in the tree. This is either the first
child of the item (if it is expanded and has children) or its next
sibling. If there is no next sibling the tree is walked backwards
until a next sibling for one of its parents is found.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNextSibling(self, item: GenericTreeItem) -> None:
        """ Returns the next sibling of an item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNextVisible(self, item: GenericTreeItem) -> None:
        """ Returns the next visible item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetPrev(self, item: GenericTreeItem) -> None:
        """ Returns the previous item. Only for internal use right now.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetPrevExpanded(self, item: 'GenericTreeItem') -> None:
        """ Returns the previous expanded item before the input one.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetPrevShown(self, item: GenericTreeItem) -> None:
        """ Returns the previous displayed item in the tree. This is either the
last displayed child of its previous sibling, or its parent item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetPrevSibling(self, item: GenericTreeItem) -> None:
        """ Returns the previous sibling of an item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetPrevVisible(self, item: GenericTreeItem) -> None:
        """ Returns the previous visible item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetPyData(self, item: GenericTreeItem) -> None:
        """ Returns the data associated to an item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetRootItem(self) -> Optional['GenericTreeItem']:
        """ Returns the root item, an instance of GenericTreeItem.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetSecondGradientColour(self) -> None:
        """ Returns the second gradient colour for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetSelection(self) -> Optional['GenericTreeItem']:
        """ Returns the current selected item (i.e. focused item).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetSelections(self) -> list['GenericTreeItem']:
        """ Returns a list of selected items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetSeparatorColour(self, colour) -> None:
        """ Returns the pen colour for separator-type items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetSpacing(self) -> None:
        """ Returns the spacing between the start and the text, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetStateImageList(self) -> None:
        """ Returns the state image list associated with CustomTreeCtrl (from which
application-defined state images are taken).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HandleHyperLink(self, item: GenericTreeItem) -> None:
        """ Handles the hyperlink items, sending the EVT_TREE_ITEM_HYPERLINK event.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HasAGWFlag(self, flag: int) -> bool:
        """ Returns True if CustomTreeCtrl has the flag bit set.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HasButtons(self) -> None:
        """ Returns whether CustomTreeCtrl has the TR_HAS_BUTTONS flag set.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HasChildren(self, item: GenericTreeItem) -> None:
        """ Returns whether an item has children or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HideItem(self, item, hide=True) -> None:
        """ Hides/shows an item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HideItemWindows(self, item) -> None:
        """ Hide all windows belonging to the item and its children.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HideWindows(self) -> None:
        """ Hides the windows associated to the items. Used internally.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HitTest(self, point, flags=0) -> tuple['GenericTreeItem', int]:
        """ Calculates which (if any) item is under the given point, returning the tree item
at this point plus extra information flags.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def InsertItem(self, parentId, input, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, separator=False, on_the_right=True) -> None:
        """ Inserts an item after the given previous.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def InsertItemByIndex(self, parentId, idPrevious, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, separator=False, on_the_right=True) -> None:
        """ Inserts an item after the given previous.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def InsertItemByItem(self, parentId, idPrevious, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, separator=False, on_the_right=True) -> None:
        """ Inserts an item after the given previous.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def InsertSeparator(self, parentId, input) -> None:
        """ Inserts a separator item after the given previous.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsBold(self, item: GenericTreeItem) -> None:
        """ Returns whether the item font is bold or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsDescendantOf(self, parent, item) -> None:
        """ Checks if the given item is under another one in the tree hierarchy.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsExpanded(self, item: GenericTreeItem) -> None:
        """ Returns whether the item is expanded or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsItalic(self, item: GenericTreeItem) -> None:
        """ Returns whether the item font is italic or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsItem3State(self, item: GenericTreeItem) -> None:
        """ Returns whether or not the checkbox item is a 3-state checkbox.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsItemChecked(self, item: GenericTreeItem) -> None:
        """ Returns whether an item is checked or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsItemEnabled(self, item: GenericTreeItem) -> None:
        """ Returns whether an item is enabled or disabled.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsItemHyperText(self, item: GenericTreeItem) -> None:
        """ Returns whether an item is hypertext or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsItemSeparator(self, item: GenericTreeItem) -> None:
        """ Returns whether an item is of separator type or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsSelected(self, item: GenericTreeItem) -> None:
        """ Returns whether the item is selected or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsVisible(self, item: GenericTreeItem) -> None:
        """ Returns whether the item is visible or not (i.e., its hierarchy is expanded
enough to show the item, and it has not been hidden).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ItemHasChildren(self, item: GenericTreeItem) -> None:
        """ Returns whether the item has children or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnAcceptEdit(self, item, value) -> None:
        """ Called by TreeTextCtrl, to accept the changes and to send the
EVT_TREE_END_LABEL_EDIT event.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnCancelEdit(self, item: GenericTreeItem) -> None:
        """ Called by TreeTextCtrl, to cancel the changes and to send the
EVT_TREE_END_LABEL_EDIT event.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnCompareItems(self, item1, item2) -> None:
        """ Returns whether 2 items have the same text.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnDestroy(self, event: 'WindowDestroyEvent') -> None:
        """ Handles the wx.EVT_WINDOW_DESTROY event for CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnEditTimer(self) -> None:
        """ The timer for editing has expired. Start editing.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ Handles the wx.EVT_ERASE_BACKGROUND event for CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnGetToolTip(self, event: CommandTreeEvent) -> None:
        """ Process the tooltip event, to speed up event processing. Does not actually
get a tooltip.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnInternalIdle(self) -> None:
        """ This method is normally only used internally, but sometimes an application
may need it to implement functionality that should not be disabled by an
application defining an OnIdle handler in a derived class.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnKeyDown(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_KEY_DOWN event for CustomTreeCtrl, sending a
EVT_TREE_KEY_DOWN event.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnKillFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_KILL_FOCUS event for CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnMouse(self, event: MouseEvent) -> None:
        """ Handles a bunch of wx.EVT_MOUSE_EVENTS events for CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ Handles the wx.EVT_PAINT event for CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_SET_FOCUS event for CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ Handles the wx.EVT_SIZE event for CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def PaintItem(self, item, dc, level, align) -> None:
        """ Actually draws an item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def PaintLevel(self, item, dc, level, y, align) -> None:
        """ Paint a level in the hierarchy of CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def PrependItem(self, parent, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, separator=False, on_the_right=True) -> None:
        """ Prepends an item as a first child of parent.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def PrependSeparator(self, parent: GenericTreeItem) -> None:
        """ Prepends a separator item as a first child of parent.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def RecurseOnChildren(self, item, maxwidth, respect_expansion_state) -> None:
        """ Recurses over all the children of the spcified items, calculating their
maximum width.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def RefreshItemWithWindows(self, item: 'GenericTreeItem') -> None:
        """ Refreshes the items with which a window is associated.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def RefreshLine(self, item: GenericTreeItem) -> None:
        """ Refreshes a damaged item line.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def RefreshSelected(self) -> None:
        """ Refreshes a damaged selected item line.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def RefreshSelectedUnder(self, item: GenericTreeItem) -> None:
        """ Refreshes the selected items under the given item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def RefreshSubtree(self, item: GenericTreeItem) -> None:
        """ Refreshes a damaged subtree of an item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ResetEditControl(self) -> None:
        """ Called by TreeTextCtrl when it marks itself for deletion.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ScrollTo(self, item: GenericTreeItem) -> None:
        """ Scrolls the specified item into view.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SelectAll(self) -> None:
        """ Selects all the item in the tree.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SelectAllChildren(self, item: GenericTreeItem) -> None:
        """ Selects all the children of the given item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SelectItem(self, item, select=True) -> None:
        """ Selects/deselects an item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SelectItemRange(self, item1, item2) -> None:
        """ Selects all the items between item1 and item2.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SendDeleteEvent(self, item: GenericTreeItem) -> None:
        """ Actually sends the EVT_TREE_DELETE_ITEM event.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetAGWWindowStyleFlag(self, agwStyle: int) -> None:
        """ Sets the CustomTreeCtrl window style.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetBackgroundColour(self, colour: NullColour) -> None:
        """ Changes the background colour of CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetBackgroundImage(self, image: None) -> None:
        """ Sets the CustomTreeCtrl background image.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetBorderPen(self, pen: 'Pen') -> None:
        """ Sets the pen used to draw the selected item border.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetButtonsImageList(self, imageList: 'ImageList') -> None:
        """ Sets the buttons image list for CustomTreeCtrl (from which application-defined
button images are taken).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetConnectionPen(self, pen: 'Pen') -> None:
        """ Sets the pen used to draw the connecting lines between items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetDisabledColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour for items in a disabled state.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetDragFullScreen(self, fullScreen: bool=False) -> None:
        """ Sets whether a drag operation will be performed full screen or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetFirstGradientColour(self, colour: Optional[None]=None) -> None:
        """ Sets the first gradient colour for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the CustomTreeCtrl font.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetForegroundColour(self, colour: NullColour) -> None:
        """ Changes the foreground colour of CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetGradientStyle(self, vertical: int=0) -> None:
        """ Sets the gradient style for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetHilightFocusColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used to highlight focused selected items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetHilightNonFocusColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used to highlight unfocused selected items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetHyperTextFont(self, font: 'Font') -> None:
        """ Sets the font used to render hypertext items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetHyperTextNewColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used to render a non-visited hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetHyperTextVisitedColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used to render a visited hypertext item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetImageList(self, imageList: 'ImageList') -> None:
        """ Sets the normal image list for CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetImageListCheck(self, sizex, sizey, imglist=None) -> None:
        """ Sets the checkbox/radiobutton image list.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetIndent(self, indent: int) -> None:
        """ Sets the indentation for CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItem3State(self, item, allow) -> None:
        """ Sets whether the item has a 3-state value checkbox assigned to it or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItem3StateValue(self, item, state) -> None:
        """ Sets the checkbox item to the given state.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemBackgroundColour(self, item, colour) -> None:
        """ Sets the item background colour.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemBold(self, item, bold=True) -> None:
        """ Sets the item font as bold/unbold.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemDropHighlight(self, item, highlight=True) -> None:
        """ Gives the item the visual feedback for drag and drop operations.
This is useful when something is dragged from outside the CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemFont(self, item, font) -> None:
        """ Sets the item font.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemHasChildren(self, item, has=True) -> None:
        """ Forces the appearance/disappearance of the button next to the item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemHyperText(self, item, hyper=True) -> None:
        """ Sets whether the item is hypertext or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemImage(self, item, image, which=TreeItemIcon_Normal) -> None:
        """ Sets the item image, depending on the item state.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemItalic(self, item, italic=True) -> None:
        """ Sets the item font as italic/non-italic.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemLeftImage(self, item, image) -> None:
        """ Sets the item leftmost image, i.e. the image associated to the item on the leftmost
part of the CustomTreeCtrl client area.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemText(self, item, text) -> None:
        """ Sets the item text.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemTextColour(self, item, colour) -> None:
        """ Sets the item text colour or separator horizontal line colour.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemType(self, item, ct_type) -> None:
        """ Sets the item type.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemVisited(self, item, visited=True) -> None:
        """ Sets whether an hypertext item was visited.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemWindow(self, item, wnd, on_the_right=True) -> None:
        """ Sets the window for the given item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemWindowEnabled(self, item, enable=True) -> None:
        """ Enables/disables the window associated to the item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetLeftImageList(self, imageList: 'ImageList') -> None:
        """ Sets the image list for CustomTreeCtrl filled with images to be used on
the leftmost part of the client area. Any item can have a leftmost image associated
with it.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetPyData(self, item, data) -> None:
        """ Sets the data associated to an item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetSecondGradientColour(self, colour: Optional[None]=None) -> None:
        """ Sets the second gradient colour for gradient-style selections.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetSeparatorColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the pen colour for separator-type items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetSpacing(self, spacing: int) -> None:
        """ Sets the spacing between items in CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetStateImageList(self, imageList: 'ImageList') -> None:
        """ Sets the state image list for CustomTreeCtrl (from which application-defined
state images are taken).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ShouldInheritColours(self) -> None:
        """ Return True from here to allow the colours of this window to be
changed by InheritAttributes, returning False forbids inheriting them
from the parent window.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SortChildren(self, item: GenericTreeItem) -> None:
        """ Sorts the children of the given item using the OnCompareItems method of
CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def TagAllChildrenUntilLast(self, crt_item, last_item, select) -> None:
        """ Used internally.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def TagNextChildren(self, crt_item, last_item, select) -> None:
        """ Used internally.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Thaw(self) -> None:
        """ Thaw CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def TileBackground(self, dc: 'DC') -> None:
        """ Tiles the background image to fill all the available area.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Toggle(self, item: GenericTreeItem) -> None:
        """ Toggles the item state (collapsed/expanded).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ToggleItemSelection(self, item: GenericTreeItem) -> None:
        """ Toggles the item selection.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def UnCheckRadioParent(self, item, checked=False) -> None:
        """ Used internally to handle radio node parent correctly.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Unselect(self) -> None:
        """ Unselects the current selection.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def UnselectAll(self) -> None:
        """ Unselect all the items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def UnselectAllChildren(self, item: GenericTreeItem) -> None:
        """ Unselects all the children of the given item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """



EVT_WINDOW_DESTROY: int

EVT_ERASE_BACKGROUND: int

EVT_KEY_DOWN: int

EVT_KILL_FOCUS: int

EVT_MOUSE_EVENTS: int

EVT_PAINT: int

EVT_SET_FOCUS: int

EVT_SIZE: int

CHK_UNCHECKED: int

CHK_CHECKED: int

CHK_UNDETERMINED: int

SYS_COLOUR_HIGHLIGHT: int

class DragImage(DragImage):
    """ This class handles the creation of a custom image in case of item drag
and drop.

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.DragImage.html
    """
    def __init__(self, treeCtrl, item) -> None:
        """ Default class constructor.
For internal use: do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.DragImage.html
        """

    def CreateBitmap(self) -> None:
        """ Actually creates the drag and drop bitmap for DragImage.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.DragImage.html
        """



class GenericTreeItem:
    """ This class holds all the information and methods for every single item in
CustomTreeCtrl. This is a generic implementation of TreeItem.

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
    """
    def __init__(self, parent, text="", ct_type=0, wnd=None, image=-1, selImage=-1, data=None, separator=False, on_the_right=True) -> None:
        """ Default class constructor.
For internal use: do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def AssignAttributes(self, attr: TreeItemAttr) -> None:
        """ Assigns the item attributes (font, colours, etcâ¦) for this item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Attr(self) -> None:
        """ Creates a new attribute (font, colours, etcâ¦) for this item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Check(self, checked: bool=True) -> None:
        """ Checks/unchecks an item. Internal use only.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Collapse(self) -> None:
        """ Collapses the item. Internal use only.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def DeleteChildren(self, tree: CustomTreeCtrl) -> None:
        """ Deletes the item children. Internal use only.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def DeleteWindow(self) -> None:
        """ Deletes the window associated to the item (if any). Internal use only.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ Enables/disables the item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Expand(self) -> None:
        """ Expands the item. Internal use only.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Get3StateValue(self) -> None:
        """ Gets the state of a 3-state checkbox item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetAttributes(self) -> None:
        """ Returns the item attributes (font, colours, etcâ¦).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetCheckedImage(self, which: int=TreeItemIcon_Checked) -> None:
        """ Returns the item check image.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetChildren(self) -> None:
        """ Returns the itemâs children.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetChildrenCount(self, recursively: bool=True) -> None:
        """ Gets the number of children of this item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetCurrentCheckedImage(self) -> None:
        """ Returns the current item check image.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetCurrentImage(self) -> None:
        """ Returns the current item image.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetData(self) -> Any:
        """ Returns the data associated to this item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetHeight(self) -> None:
        """ Returns the height of the item, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetImage(self, which: int=TreeItemIcon_Normal) -> None:
        """ Returns the item image for a particular item state.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetLeftImage(self) -> None:
        """ Returns the leftmost image associated to this item, i.e. the image on the
leftmost part of the client area of CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetParent(self) -> Optional['GenericTreeItem']:
        """ Gets the item parent (another instance of GenericTreeItem or None for
root items.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetSize(self, x, y, theButton) -> None:
        """ Returns the item size.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetText(self) -> None:
        """ Returns the item text.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetType(self) -> None:
        """ Returns the item type.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetValue(self) -> None:
        """ Returns whether the item is checked or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetVisited(self) -> None:
        """ Returns whether an hypertext item was visited or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetWidth(self) -> None:
        """ Returns the width of the itemâs contents, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetWindow(self) -> None:
        """ Returns the window associated to the item (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetWindowEnabled(self) -> None:
        """ Returns whether the associated window is enabled or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetWindowSize(self) -> None:
        """ Returns the associated window size.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetX(self) -> None:
        """ Returns the x position on an item, in logical coordinates.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetY(self) -> None:
        """ Returns the y position on an item, in logical coordinates.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def HasChildren(self) -> None:
        """ Returns whether the item has children or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def HasPlus(self) -> None:
        """ Returns whether the item has the plus button or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Hide(self, hide: bool) -> None:
        """ Hides/shows the item. Internal use only.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def HitTest(self, point, theCtrl, flags=0, level=0) -> None:
        """ HitTest method for an item. Called from the main window CustomTreeCtrl.HitTest().

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Insert(self, child, index) -> None:
        """ Inserts an item in the item children list for this item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Is3State(self) -> None:
        """ Returns whether or not the checkbox item is a 3-state checkbox.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsBold(self) -> None:
        """ Returns whether the item font is bold or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsChecked(self) -> None:
        """ This is just a maybe more readable synonym for GetValue.
Returns whether the item is checked or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsEnabled(self) -> None:
        """ Returns whether the item is enabled or not. Hidden items always return False.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsExpanded(self) -> None:
        """ Returns whether the item is expanded or not. Hidden items always return False.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsHidden(self) -> None:
        """ Returns whether the item is hidden or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsHyperText(self) -> None:
        """ Returns whether the item is hypetext or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsItalic(self) -> None:
        """ Returns whether the item font is italic or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsOk(self) -> None:
        """ Returns whether the item is ok or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsSelected(self) -> None:
        """ Returns whether the item is selected or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsSeparator(self) -> None:
        """ Returns whether the item is meant to be an horizontal line separator or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_SET_FOCUS event for the window associated with the item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def OnTreeItemCollapsing(self, event: GenericTreeItem) -> None:
        """ Handles the wx.EVT_TREE_ITEM_COLLAPSING event for the window associated with the item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Set3State(self, allow: bool) -> None:
        """ Sets whether the item has a 3-state value checkbox assigned to it or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Set3StateValue(self, state: int) -> None:
        """ Sets the checkbox item to the given state.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetAttributes(self, attr: TreeItemAttr) -> None:
        """ Sets the item attributes (font, colours, etcâ¦).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetBold(self, bold: bool) -> None:
        """ Sets the item font bold.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetData(self, data: Any) -> None:
        """ Sets the data associated to this item.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetHasPlus(self, has: bool=True) -> None:
        """ Sets whether an item has the âplusâ button.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetHeight(self, h: int) -> None:
        """ Sets the itemâs height. Used internally.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetHilight(self, set: bool=True) -> None:
        """ Sets the item focus/unfocus.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetHyperText(self, hyper: bool=True) -> None:
        """ Sets whether the item is hypertext or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetImage(self, image, which) -> None:
        """ Sets the item image.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetItalic(self, italic: bool) -> None:
        """ Sets the item font italic.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetLeftImage(self, image: int) -> None:
        """ Sets the item leftmost image, i.e. the image associated to the item on the leftmost
part of the CustomTreeCtrl client area.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetText(self, text: str) -> None:
        """ Sets the item text.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetType(self, ct_type: int) -> None:
        """ Sets the item type.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetVisited(self, visited: bool=True) -> None:
        """ Sets whether an hypertext item was visited or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetWidth(self, w: int) -> None:
        """ Sets the itemâs width. Used internally.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetWindow(self, wnd, on_the_right=True) -> None:
        """ Sets the window associated to the item. Internal use only.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetWindowEnabled(self, enable: bool=True) -> None:
        """ Sets whether the associated window is enabled or not.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetX(self, x: int) -> None:
        """ Sets the x position on an item, in logical coordinates.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetY(self, y: int) -> None:
        """ Sets the y position on an item, in logical coordinates.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """



EVT_TREE_ITEM_COLLAPSING: int

class TreeEditTimer(Timer):
    """ Timer used for enabling in-place edit.

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEditTimer.html
    """
    def __init__(self, owner: Timer) -> None:
        """ Default class constructor.
For internal use: do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEditTimer.html
        """

    def Notify(self) -> None:
        """ The timer has expired, starts the item editing.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEditTimer.html
        """



class TreeEvent(CommandTreeEvent):
    """ CommandTreeEvent is a special class for all events associated with tree controls.

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEvent.html
    """
    def __init__(self, evtType, evtId, item=None, evtKey=None, point=None, label=None, **kwargs) -> None:
        """ Default class constructor.
For internal use: do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEvent.html
        """

    def Allow(self) -> None:
        """ This is the opposite of Veto: it explicitly allows the event to be processed.
For most events it is not necessary to call this method as the events are
allowed anyhow but some are forbidden by default (this will be mentioned
in the corresponding event description).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEvent.html
        """

    def GetNotifyEvent(self) -> None:
        """ Returns the actual NotifyEvent.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEvent.html
        """

    def IsAllowed(self) -> None:
        """ Returns True if the change is allowed ( Veto hasnât been called) or
False otherwise (if it was).

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEvent.html
        """

    def Veto(self) -> None:
        """ Prevents the change announced by this event from happening.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEvent.html
        """



class TreeFindTimer(Timer):
    """ Timer used to clear the CustomTreeCtrl _findPrefix attribute if no
key was pressed for a sufficiently long time.

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeFindTimer.html
    """
    def __init__(self, owner: Timer) -> None:
        """ Default class constructor.
For internal use: do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeFindTimer.html
        """

    def Notify(self) -> None:
        """ The timer has expired, clear the _findPrefix attribute in CustomTreeCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeFindTimer.html
        """



class TreeItemAttr:
    """ Creates the item attributes (text colour, background colour and font).

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
    """
    def __init__(self, colText=wx.NullColour, colBack=wx.NullColour, colBorder=wx.NullColour, font=wx.NullFont) -> None:
        """ Default class constructor.
For internal use: do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def GetBackgroundColour(self) -> None:
        """ Returns the attribute background colour.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def GetBorderColour(self) -> None:
        """ Returns the attribute border colour.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def GetFont(self) -> None:
        """ Returns the attribute font.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def GetTextColour(self) -> None:
        """ Returns the attribute text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def HasBackgroundColour(self) -> None:
        """ Returns whether the attribute has background colour.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def HasBorderColour(self) -> None:
        """ Returns whether the attribute has border colour.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def HasFont(self) -> None:
        """ Returns whether the attribute has font.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def HasTextColour(self) -> None:
        """ Returns whether the attribute has text colour.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def SetBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ Sets the item background colour attribute.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def SetBorderColour(self, colBorder) -> None:
        """ Sets the item border colour attribute.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the item font attribute.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def SetTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ Sets the text colour attribute.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """



class TreeTextCtrl(ExpandoTextCtrl):
    """ Control used for in-place edit.

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
    """
    def __init__(self, owner, item=None) -> None:
        """ Default class constructor.
For internal use: do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def AcceptChanges(self) -> None:
        """ Accepts/rejects the changes made by the user.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def Finish(self) -> None:
        """ Finish editing.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def item(self) -> None:
        """ Returns the item currently edited.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def OnChar(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_CHAR event for TreeTextCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def OnKeyUp(self, event: KeyEvent) -> None:
        """ Handles the wx.EVT_KEY_UP event for TreeTextCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def OnKillFocus(self, event: FocusEvent) -> None:
        """ Handles the wx.EVT_KILL_FOCUS event for TreeTextCtrl.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def StopEditing(self) -> None:
        """ Suddenly stops the editing.

            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """



EVT_CHAR: int

EVT_KEY_UP: int

TREE_HITTEST_ABOVE: int

TREE_HITTEST_BELOW: int

TREE_HITTEST_NOWHERE: int

TREE_HITTEST_ONITEMBUTTON: int

TREE_HITTEST_ONITEMICON: int

TREE_HITTEST_ONITEMINDENT: int

TREE_HITTEST_ONITEMLABEL: int

TREE_HITTEST_ONITEM: int

TREE_HITTEST_ONITEMRIGHT: int

TREE_HITTEST_TOLEFT: int

TREE_HITTEST_TORIGHT: int

TREE_HITTEST_ONITEMUPPERPART: int

TREE_HITTEST_ONITEMLOWERPART: int

TREE_HITTEST_ONITEMCHECKICON: int

