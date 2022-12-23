from typing import Any, Callable, ContextManager, Optional, Union


BOTH: int
EXPAND: int
ALL: int
ID_YES: int
ID_NO: int
ID_OK: int
ID_CANCEL: int
ID_CLOSE: int
ID_IGNORE: int
DEFAULT_DIALOG_STYLE: int
RESIZE_BORDER: int
BORDER_NONE: int
VERTICAL: int
HORIZONTAL: int
NOT_FOUND: int
OPEN: int
ACCEL_CTRL: int
LIST_FORMAT_LEFT: int
LC_SINGLE_SEL: int
LC_VRULES: int
LC_HRULES: int
LC_REPORT: int
MINIMIZE_BOX: int
IMAGE_LIST_SMALL: int
LIST_AUTOSIZE: int
CAPTION: int
SYSTEM_MENU: int
CLIP_CHILDREN: int
TAB_TRAVERSAL: int
CLOSE_BOX: int
LIST_NEXT_ALL: int
LIST_STATE_SELECTED: int
LIST_STATE_DONTCARE: int
EAST: int
CB_DROPDOWN: int
CB_READONLY: int
LIST_FORMAT_RIGHT: int
BITMAP_TYPE_PNG: int
APP_ASSERT_SUPPRESS: int
RA_HORIZONTAL: int
RA_VERTICAL: int
GROW: int
NO_BORDER: int
FONTFAMILY_DEFAULT: int
NORMAL: int
FONTWEIGHT_BOLD: int
DEFAULT: int
LB_EXTENDED: int
LI_HORIZONTAL: int
LI_VERTICAL: int

ICON_NONE: int
ICON_ERROR: int
ICON_WARNING: int
ICON_QUESTION: int
ICON_INFORMATION: int
ICON_EXCLAMATION: int
ICON_HAND: int
ICON_AUTH_NEEDED: int

EVT_TREE_ITEM_MENU: int
EVT_TREE_SEL_CHANGED: int
EVT_TREE_ITEM_MIDDLE_CLICK: int
EVT_TREE_ITEM_ACTIVATED: int
EVT_TREE_ITEM_RIGHT_CLICK: int
EVT_CHOICE: int
EVT_TEXT: int
EVT_CHECKBOX: int
EVT_BUTTON: int
EVT_LEFT_UP: int
EVT_RIGHT_UP: int
EVT_LEFT_DOWN: int
EVT_MENU: int
EVT_TIMER: int
EVT_TEXT_ENTER: int
EVT_END_SESSION: int
EVT_QUERY_END_SESSION: int
EVT_LIST_ITEM_SELECTED: int
EVT_LIST_ITEM_ACTIVATED: int
EVT_LIST_ITEM_DESELECTED: int
EVT_CHAR: int
EVT_LIST_COL_CLICK: int
EVT_CLOSE: int
EVT_COMBOBOX: int
EVT_KEY_DOWN: int
EVT_LISTBOX: int
EVT_LISTBOX_DCLICK: int

TR_HIDE_ROOT: int
TR_NO_BUTTONS: int
TR_DEFAULT_STYLE: int
TE_PASSWORD: int
TE_PROCESS_ENTER: int
TE_MULTILINE: int
ST_ELLIPSIZE_END: int

WHITE: int
BLACK: int
RED: int
SYS_COLOUR_MENU: int
CURSOR_HAND: int

NewId: Callable
NewIdRef: Callable
DefaultSize: 'Size' = (-1, -1)

wxEVT_COMMAND_BUTTON_CLICKED: int


class EvtHandler:
	""" Interface voor wx.EvtHandler
	"""

	def Bind(self, event: int, handler: Callable, id: int = None) -> None:
		""" Bind an event to an event handler.
		"""

	def Unbind(self, event: int, source: Optional['EvtHandler'] = None, id: int = None, id2: int = None, handler: Optional[Callable] = None) -> bool:
		""" Disconnects the event handler binding for event from self. Returns True if successful.
		"""

	def ProcessEvent(self, event: 'Event') -> bool:
		""" Processes an event, searching event tables and calling zero or more suitable event handler function(s).
		"""


class Window(EvtHandler):
	""" Interface voor wx.Window
	"""

	def __init__(self, parent: Any, id: int = None, pos: tuple[int, int] = None, size: tuple[int, int] = None, style: int = 0, name: str = "", title: str = ""):
		""" Constructs a window, which can be a child of a frame, dialog or any other non-control window.
		"""

	def GetParent(self) -> 'Window':
		""" Returns the parent of the window, or None if there is no parent.
		"""
		pass

	def SetSizer(self, sizer: 'Sizer') -> None:
		""" Sets the window to have the given layout sizer.
		"""
		pass

	def Layout(self) -> bool:
		""" Lays out the children of this window using the associated sizer.
		"""

	def Fit(self) -> None:
		""" Sizes the window to fit its best size.
		"""

	def Center(self, direction: int = 'BOTH') -> None:
		""" Centres the window.
		"""

	def Destroy(self) -> bool:
		""" Destroys the window safely.
		"""

	def Hide(self) -> bool:
		""" Equivalent to calling wx.Window.Show (False).
		"""

	def Show(self, show: bool = True) -> bool:
		""" Shows or hides the window.
		"""

	def SetFocus(self) -> None:
		""" This sets the window to receive keyboard input.
		"""

	def SetFont(self, font: 'Font') -> bool:
		""" Sets the font for this window.
		"""

	def SetForegroundColour(self, colour: Any) -> bool:
		""" Sets the foreground colour of the window.
		"""

	def SetBackgroundColour(self, colour: Any) -> bool:
		""" Sets the background colour of the window.
		"""

	def GetLabel(self) -> str:
		""" Gets the window's label.
		"""

	def SetLabel(self, label: str) -> None:
		""" Sets the window's label.
		"""

	def GetFont(self) -> 'Font':
		""" Returns the font for this window.
		"""

	def Raise(self) -> None:
		""" Raises the window to the top of the window hierarchy (Z-order).
		"""

	def Enable(self, enable: bool = True) -> bool:
		""" Enable or disable the window for user input.
		"""

	def SetAcceleratorTable(self, accel: 'AcceleratorTable') -> None:
		""" Sets the accelerator table for this window.
		"""

	def SetCursor(self, cursor: 'Cursor') -> bool:
		""" Sets the window's cursor.
		"""

	def SetMinSize(self, size: tuple[int, int]) -> None:
		""" Sets the minimum size of the window, to indicate to the sizer layout mechanism that this is the minimum required size.
		"""

	def SetMaxSize(self, size: tuple[int, int]) -> None:
		""" Sets the maximum size of the window, to indicate to the sizer layout mechanism that this is the maximum required size.
		"""

	def Refresh(self, eraseBackground: bool = True, rect: Any = None) -> None:
		""" Causes this window, and all of its children recursively (except under GTK1 where this is not implemented), to be repainted.
		"""

	def GetId(self) -> int:
		""" Retrieve the ID of the Window
		"""
		...

	def GetChildren(self) -> list['Window']:
		""" Retrieve all chhildren
		"""
		...

	def PopupMenu(self, menu: 'Menu') -> bool:
		""" Pops up the given menu at the specified coordinates, relative to this window, and returns control when the user has dismissed the menu.
		"""
		...

	def SetToolTip(self, label: str) -> None:
		""" Instellen van de ToolTip
		"""
		...

	def SetSizeHints(self, minSize: Union[tuple[int, int], 'Size'], maxSize: Union[tuple[int, int], 'Size'] = 'DefaultSize', incSize='DefaultSize') -> None:
		""" Use of this function for windows which are not toplevel windows (such as wx.Dialog or wx.Frame) is discouraged.
		"""
		...

	def IsShown(self) -> bool:
		""" Returns True if the window is shown, False if it has been hidden.
		"""

	def GetSize(self) -> 'Size':
		""" Returns the size of the Window
		"""
		...

	def IsEnabled(self) -> bool:
		""" Returns True if the window is enabled, i.e. if it accepts user input, False otherwise.

			Notice that this method can return False even if this window itself hadn’t been explicitly disabled when one of its parent windows is disabled. To get the intrinsic status of this window, use IsThisEnabled
		"""

	def SetWindowStyle(self, flags: int) -> None:
		""" Sets the style of the window.

		Please note that some styles cannot be changed after the window creation and that Refresh might need to be called after changing the others for the change to take place immediately.
		"""

	def GetForegroundColour(self) -> 'Colour':
		""" Returns the foreground colour of the window.
		"""

	def GetEventHandler(self) -> EvtHandler:
		""" Returns the event handler for this window.

			By default, the window is its own event handler.
		"""


NullCursor: 'Cursor'
CURSOR_WAIT: int


class Cursor:
	""" Interface voor wx.Cursor
	"""

	def __init__(self, cursor: int):
		""" Constructor
		"""


class Timer:
	""" Interface voor wx.Timer
	"""

	def __init__(self, owner: Window, id: int = -1):
		""" Constructor
		"""

	def Start(self, milliseconds: int = -1, oneShot: int = 0) -> bool:
		""" (Re)starts the timer.
		"""

	def StartOnce(self, milliseconds: int = -1) -> bool:
		""" Starts the timer for a once-only notification.
		"""

	def Stop(self) -> None:
		""" Stops the timer.
		"""


class Font:
	""" Interface voor wx.Font
	"""

	def __init__(self, pointSize: int, family: int, style: int, weight: int, underline: bool = False, faceName: str = "", encoding: int = -1):
		""" Creates a font object with the specified attributes and size in pixels.
		"""

	def Bold(self) -> 'Font':
		""" Returns a bold version of this font.
		"""

	def Scaled(self, factor: float) -> 'Font':
		""" Change size of font
		"""


class Event:
	""" Interface voor wx.Event
	"""

	def __init__(self, id: int = 0, eventType: int = -1):
		""" Constructor.
		"""

	def GetId(self) -> int:
		""" Retrieve the ID of the Event
		"""
		...

	def Skip(self, skip: bool = True) -> None:
		""" This method can be used inside an event handler to control whether further event handlers bound to this event will be called after the current one returns.
		"""

	def GetItem(self) -> Any:
		""" Get an item
		"""

	def IsOk(self) -> bool:
		""" Check if an item is correct
		"""

	def GetEventObject(self) -> Any:
		""" Retrieve object
		"""

	def PopupMenu(self, menu: 'Menu') -> bool:
		""" Pops up the given menu at the specified coordinates, relative to this window, and returns control when the user has dismissed the menu.
		"""
		...

	def SetEventObject(self, object: Window) -> None:
		""" Sets the originating object.
		"""


class ListEvent(Event):
	""" Interface voor wx.ListEvent
	"""

	def GetIndex(self) -> int:
		""" The item index.
		"""


class PyEvent(Event):
	""" Interface voor wx.PyEvent
	"""
	...


class Icon:
	""" Interface voor wx.Icon
	"""


class TopLevelWindow(Window):
	""" Interface voor wx.TopLevelWindow
	"""

	def SetTitle(self, title: str) -> None:
		""" Sets the window title.
		"""

	def SetIcon(self, icon: Icon) -> None:
		""" Sets the icon for this window.
		"""


class Dialog(TopLevelWindow):
	""" Interface voor wx.Dialog
	"""

	def ShowModal(self):
		""" Shows an application-modal dialog.
		"""
		...

	def EndModal(self, endId: int) -> None:
		""" Stop the Modal
		"""
		...


class TreeCtrl(Window):
	""" Interface voor wx.TreeItemId
	"""

	def AddRoot(self, text: str, image: int = -1, selImage: int = -1, data: Any = None) -> 'TreeItemId':
		""" Adds the root node to the tree, returning the new item.
		"""

	def AppendItem(self, parent: 'TreeItemId', text: str, image: int = -1, selImage: int = -1, data: Any = None) -> 'TreeItemId':
		""" Appends an item to the end of the branch identified by parent, return a new item id.
		"""

	def GetRootItem(self) -> 'TreeItemId':
		""" Returns the root item for the tree control.
		"""

	def DeleteChildren(self, item: 'TreeItemId') -> None:
		""" Deletes all children of the given item (but not the item itself).
		"""

	def GetItemData(self, item: 'TreeItemId') -> Any:
		""" Gets the item client data.
		"""

	def SetItemData(self, item: 'TreeItemId', data: Any) -> None:
		""" Sets the item client data.
		"""

	def SetItemBold(self, item: 'TreeItemId', bold: bool = True) -> None:
		""" Makes item appear in bold font if bold parameter is True or resets it to the normal state.
		"""

	def SetItemBackgroundColour(self, item: 'TreeItemId', col: 'Colour') -> None:
		""" Sets the colour of the item’s background.
		"""

	def ExpandAll(self) -> None:
		""" Expands all items in the tree.
		"""

	def GetFirstChild(self, item: 'TreeItemId') -> tuple[Any, 'TreeItemId']:
		""" Returns the first child; call GetNextChild for the next child.
		"""

	def GetChildrenCount(self, item: 'TreeItemId', recursively: bool = True) -> int:
		""" Returns the number of items in the branch.
		"""

	def GetNextChild(self, item: 'TreeItemId', cookie: Any) -> tuple[Any, 'TreeItemId']:
		""" Returns the next child; call GetFirstChild for the first child.
		"""

	def SelectItem(self, item: 'TreeItemId', select: bool = True) -> None:
		""" Selects the given item.
		"""


class TreeItemId:
	""" Interface voor wx.TreeItemId
	"""


class Control(Window):
	""" Interface voor wx.Control
	"""

	def SetValue(self, state: Any) -> None:
		""" Set the value of the control
		"""

	def GetValue(self) -> Any:
		""" Get the value of the control
		"""


class ItemContainer:

	def Append(self, item: str) -> None:
		""" Appends item into the control.
		"""

	def AppendItems(self, choices: list[str]) -> None:
		""" Vullen van de Choice
		"""

	def GetItems(self) -> list[str]:
		""" Alias for GetStrings
		"""

	def GetStrings(self) -> list[str]:
		""" Returns the array of the labels of all items in the control.
		"""


class Choice(ItemContainer, Control):
	""" Interface voor wx.Choice
	"""

	def __init__(self, parent: Any, id: int = 0, pos: tuple[int, int] = None, size: tuple[int, int] = None, choices: list[Any] = None, style: int = None, validator: int = None, name: str = None):
		pass

	def Clear(self) -> None:
		""" Leeghalen van de Choice
		"""

	def SetSelection(self, index: int) -> None:
		""" Sets the selection to the given item n or removes the selection entirely if n == NOT_FOUND .
		"""

	def FindString(self, search: str) -> int:
		""" Finds an item whose label matches the given string.
		"""

	def GetCount(self) -> int:
		""" Returns the number of items in the control.
		"""

	def GetString(self, index: int) -> str:
		""" Returns the label of the item with the given index.
		"""

	def GetSelection(self) -> int:
		""" Returns the index of the selected item or NOT_FOUND if no item is selected.
		"""


class CheckBox(Control):
	""" Interface voor wx.CheckBox
	"""

	def __init__(self, parent: Any, id: int = 0, label: str = "", pos: tuple[int, int] = None, size: tuple[int, int] = None, style: int = 0, validator: int = None, name: str = ""):
		pass

	def IsChecked(self) -> bool:
		""" This is just a maybe more readable synonym for GetValue : just as the latter, it returns True if the checkbox is checked and False otherwise.
		"""


class Panel(Window):
	""" Interface voor wx.Panel
	"""


class TextEntry:

	def GetValue(self) -> str:
		""" Gets the contents of the control.

			Notice that for a multiline text control, the lines will be separated by (Unix-style) \n characters, even under Windows where they are separated by a \r\n sequence in the native control.
		"""

	def SetEditable(self, editable: bool) -> None:
		""" Makes the text item editable or read-only, overriding the wx.TE_READONLY flag.
		"""

	def SetInsertionPoint(self, pos: int) -> None:
		""" Sets the insertion point at the given position.
		"""

	def SetInsertionPointEnd(self) -> None:
		""" Sets the insertion point at the end of the text control.
		"""

	def Clear(self) -> None:
		""" Leeghalen van de Choice
		"""

	def SetSelection(self, from_: int, to_: int) -> None:
		""" Selects the text starting at the first position up to (but not including) the character at the last position.

			If both parameters are equal to -1 all text in the control is selected.

			Notice that the insertion point will be moved to from by this function.
		"""


class TextCtrl(TextEntry, Control):
	""" Interface voor wx.TextCtrl
	"""

	def __init__(self, parent: Any, id: int = None, pos: tuple[int, int] = None, size: tuple[int, int] = None, style: int = 0, name: str = "", title: str = "", value: str = ""):
		""" Constructs a window, which can be a child of a frame, dialog or any other non-control window.
		"""


class SearchCtrl(TextCtrl):
	""" Interface voor wx.SearchCtrl
	"""

	def ShowCancelButton(self, show: bool) -> None:
		""" Shows or hides the cancel button.
		"""

	def SetDescriptiveText(self, text: str) -> None:
		""" Set the text to be displayed in the search control when the user has not yet typed anything in it.
		"""


class Colour:
	""" Interface voor wx.Colour
	"""

	def __init__(self, *args, **kwargs):
		pass


class Sizer(Window):

	def Add(self, window: Any, proportion: int = 0, flag: int = 0, border: int = 0) -> 'SizerItem':
		""" Appends a child to the sizer.
		"""

	def Insert(self, index: int, window: Any, proportion: int = 0, flag: int = 0, border: int = 0) -> 'SizerItem':
		""" Insert a child into the sizer before any existing item at index.)
		"""

	def AddSpacer(self, size: int) -> 'SizerItem':
		""" This base function adds non-stretchable space to both the horizontal and vertical orientation of the sizer.
		"""

	def InsertSpacer(self, index: int, size: int) -> 'SizerItem':
		""" Inserts non-stretchable space to the sizer.
		"""

	def AddStretchSpacer(self, prop: int = 1) -> 'SizerItem':
		""" Adds stretchable space to the sizer.
		"""

	def InsertStretchSpacer(self, index: int, prop: int = 1) -> 'SizerItem':
		""" Inserts stretchable space to the sizer.
		"""

	def Clear(self, delete_windows: bool = False) -> None:
		""" Detaches all children from the sizer.
		"""

	def Detach(self, window: Window) -> bool:
		""" Detach the child window from the sizer without destroying it.
		"""

	def GetChildren(self) -> list['SizerItem']:
		""" Returns the list of the items in this sizer.
		"""

	def GetItem(self, win: Union[int, Window]) -> Optional['SizerItem']:
		""" Finds the wx.SizerItem which holds the given window.
		"""

	def Remove(self, index: int) -> bool:
		""" Removes a child from the sizer and destroys it if it is a sizer or a spacer, but not if it is a window (because windows are owned by their parent window, not the sizer).
		"""

	def Fit(self, window: Window) -> 'Size':
		""" Tell the sizer to resize the window so that its client area matches the sizer’s minimal size ( ComputeFittingClientSize is called to determine it).

			This is commonly done in the constructor of the window itself, see sample in the description of wx.BoxSizer.
		"""


class SizerItem:
	""" Interface voor wx.SizerItem
	"""

	def IsSizer(self) -> bool:
		""" Is this item a sizer?
		"""

	def IsSpacer(self) -> bool:
		""" Is this item a spacer?
		"""

	def IsWindow(self) -> bool:
		""" Is this item a window?
		"""


class BoxSizer(Sizer):
	""" Interface voor wx.BoxSizer
	"""

	def __init__(self, orient: int = 'HORIZONTAL'):
		""" Constructor for a wx.BoxSizer
		"""
		pass

	def SetOrientation(self, orient: int) -> None:
		""" Sets the orientation of the box sizer, either wx.VERTICAL or wx.HORIZONTAL.
		"""


class WrapSizer(Sizer):
	""" Interface voor wx.WrapSizer
	"""

	def __init__(self):
		""" Constructor for a wx.WrapSizer
		"""
		pass


class GridSizer(Sizer):
	""" Interface voor wx.GridSizer
	"""

	def __init__(self, rows: int = 0, cols: int = 0, vgap: int = 0, hgap: int = 0):
		""" Constructor voor wx.GridSizer
		"""


class FlexGridSizer(GridSizer):
	""" Interface voor wx.FlexGridSizer
	"""

	def AddGrowableCol(self, idx: int, proportion: int = 0) -> None:
		""" Specifies that column idx (starting from zero) should be grown if there is extra space available to the sizer.
		"""

	def CalcMin(self) -> 'Size':
		""" This method is abstract and has to be overwritten by any derived class.
		"""

	def GetColWidths(self) -> list[int]:
		""" Returns a read-only array containing the widths of the columns in the sizer.
		"""

	def GetFlexibleDirection(self) -> int:
		""" Returns a wx.Orientation value that specifies whether the sizer flexibly resizes its columns, rows, or both (default).
		"""

	def GetNonFlexibleGrowMode(self) -> int:
		""" Returns the value that specifies how the sizer grows in the “non-flexible” direction if there is one.
		"""

	def GetRowHeights(self) -> list[int]:
		""" Returns a read-only array containing the heights of the rows in the sizer.
		"""

	def IsColGrowable(self, idx: int) -> bool:
		""" Returns True if column idx is growable.
		"""

	def IsRowGrowable(self, idx: int) -> bool:
		""" Returns True if row idx is growable.
		"""

	def RemoveGrowableCol(self, idx: int) -> None:
		""" Specifies that the idx column index is no longer growable.
		"""

	def RepositionChildren(self, minSize: 'Size') -> None:
		""" Method which must be overridden in the derived sizer classes.
		"""

	def SetFlexibleDirection(self, direction: int) -> None:
		""" Specifies whether the sizer should flexibly resize its columns, rows, or both.
	"""

	def SetNonFlexibleGrowMode(self, mode: int) -> None:
		""" Specifies how the sizer should grow in the non-flexible direction if there is one (so SetFlexibleDirection must have been called previously).
		"""


class GBPosition:
	""" This class represents the position of an item in a virtual grid of rows and columns managed by a GridBagSizer.
	"""

	def __init__(self, row: int = 0, col: int = 0):
		""" Construct a new wx.GBPosition, setting the row and column.
		"""


class GBSpan:
	""" This class is used to hold the row and column spanning attributes of items in a GridBagSizer.
	"""

	def __init__(self, rowspan: int = 0, colspan: int = 0):
		""" Construct a new wx.GBSpan, setting the rowspan and colspan.
		"""


class GridBagSizer(FlexGridSizer):
	""" A wx.Sizer that can lay out items in a virtual grid like a wx.FlexGridSizer but in this case explicit positioning of the items is allowed using wx.GBPosition, and items can optionally span more than one row and/or column using wx.GBSpan.
	"""

	def __init__(self, vgap: int = 0, hgap: int = 0):
		""" Construct
		"""

	def Add(self, window: Window, pos: GBPosition, span: GBSpan = None, flag: int = 0, border: int = 0, userData: Any = None) -> SizerItem:
		""" Adds the given item to the given position.
		"""


class Size:
	""" Interface voor wx.Size
	"""

	def GetHeight(self) -> int:
		""" Gets the height member.
		"""

	def GetWidth(self) -> int:
		""" Gets the width member.
		"""


class FrozenWindow(ContextManager):
	""" Interface voor wx.FrozenWindow
	"""

	def __init__(self, window: Window):
		pass

	def __enter__(self) -> None:
		pass

	def __exit__(self, *args, **kwargs) -> None:
		pass


class SystemSettings:
	""" Interface voor wx.SystemSettings
	"""

	@staticmethod
	def GetAppearance() -> int:
		""" Returns the object describing the current system appearance.
		"""

	@staticmethod
	def GetColour(index: int) -> Colour:
		""" Returns a system colour.
		"""

	@staticmethod
	def GetFont(index: int) -> Font:
		""" Returns a system font.
		"""

	@staticmethod
	def GetMetric(index: int, win: Window = None) -> int:
		""" Returns the value of a system metric, or -1 if the metric is not supported on the current system.
		"""

	@staticmethod
	def GetScreenType() -> int:
		""" Returns the screen type.
		"""

	@staticmethod
	def HasFeature(index: int) -> bool:
		""" Returns True if the port has certain feature.
		"""


class Button(Window):
	""" Interface voor wx.Button
	"""

	def __init__(self, parent: Any, id: int = None, pos: tuple[int, int] = None, size: tuple[int, int] = None, style: int = 0, name: str = "", label: str = ""):
		""" Constructs a window, which can be a child of a frame, dialog or any other non-control window.
		"""


class BitmapButton(Button):
	""" Interface voor wx.Button
	"""


class StaticText(Window):
	""" Interface voor wx.StaticText
	"""

	def __init__(self, parent: Window, label: str = None, style: int = None, size: tuple[int, int] = None, pos: tuple[int, int] = None):
		""" Constructor
		"""
		...

	def Wrap(self, width: int) -> None:
		""" This functions wraps the controls label so that each of its lines becomes at most width pixels wide if possible (the lines are broken at words boundaries so it might not be the case if words are too long).
		"""
		...


class StaticBox(Window):
	""" Interface voor wx.StaticBox
	"""

	def __init__(self, parent: Window, id: int = -1, label: str = "", pos: tuple[int, int] = None, size: tuple[int, int] = None, style: int = 0, name: str = ""):
		""" Constructor
		"""


class StaticBoxSizer(BoxSizer):
	""" Interface voor wx.StaticBoxSizer
	"""

	def __init__(self, box: StaticBox, orient: int = 0):
		""" Constructor
		"""


class AcceleratorTable:
	""" Interface voor wx.AcceleratorTable
	"""

	def __init__(self, entries: list[tuple[int, int, int]]):
		""" Constructor
		"""


class StaticLine(Window):
	""" Interface voor wx.StaticLine
	"""

	def __init__(self, parent: Any, orien: int = -1, pos: tuple[int, int] = None, size: tuple[int, int] = None, style: int = None):
		""" Constructor
		"""


class ListCtrl(Window):
	""" Interface voor wx.ListCtrl
	"""

	def AppendColumn(self, heading: str, format: int = -1, width: int = -1) -> int:
		""" Adds a new column to the list control in report view mode.
		"""
		...

	def InsertColumn(self, col: int, heading: str, format: int = -1, width: int = -1) -> int:
		""" Insert a new column in the list control in report view mode at the given position specifying its most common attributes.
		"""
		...

	def SetColumnWidth(self, col: int, width: int) -> bool:
		""" Sets the column width.
		"""
		...

	def SetItem(self, index: int, column: int, label: str, imageId: int = -1) -> bool:
		""" Sets an item string field at a particular column.
		"""
		...

	def InsertItem(self, index: int, label: str, imageIndex: int = -1) -> int:
		""" Insert an image/string item.
		"""
		...

	def Select(self, idx: int, on: int = 1) -> None:
		""" Selects/deselects an item.
		"""
		...

	def IsSelected(self, index: int) -> bool:
		""" Returns True if the item with the given index is selected, False otherwise.
		"""

	def Focus(self, idx: int) -> None:
		""" Focus and show the given item.
		"""
		...

	def GetFirstSelected(self) -> int:
		""" Returns the first selected item, or -1 when none is selected.
		"""
		...

	def GetSelectedItemCount(self) -> int:
		""" Returns the number of selected items in the list control.
		"""
		...

	def GetColumnCount(self) -> int:
		""" Returns the number of columns in the list control.
		"""
		...

	def ClearAll(self) -> None:
		""" Deletes all items and all columns.
		"""
		...

	def DeleteAllItems(self) -> None:
		""" Deletes all items.
		"""
		...

	def SetColumnImage(self, index: int, imageIndex: int) -> None:
		""" Set the column image for a row
		"""
		...

	def GetNextItem(self, item: int, geometry: int = 'LIST_NEXT_ALL', state: int = 'LIST_STATE_DONTCARE') -> int:
		""" Searches for an item with the given geometry or state, starting from item but excluding the item itself.
		"""
		...

	def AssignImageList(self, imageList: 'ImageList', style: int = None) -> None:
		""" Set the ImageList
		"""
		...


class Frame(TopLevelWindow):
	""" Interface voor wx.Frame
	"""
	...


class Bitmap:
	""" Interface voor wx.Bitmap
	"""

	def __init__(self, name: str, type: int = 1):
		""" Loads a bitmap from a file or resource.
		"""
		...

	def GetSize(self) -> Size:
		""" Returns the size of the bitmap in pixels.
		"""
		...


class StaticBitmap(Window):
	""" Interface voor wx.StaticBitMap
	"""

	def __init__(self, parent: Window, id: int = 'ID_ANY', bitmap: Bitmap = None, pos: Size = None, size: Size = None, style: int = 0, name: str = ""):
		""" Constructor, creating and showing a static bitmap control.
		"""
		...


class ImageList:
	""" Interface voor wx.ImageList
	"""

	def __init__(self, width: int, height: int):
		""" Constructor
		"""
		...

	def Add(self, icon: Bitmap) -> None:
		""" Adds a new image or images using a bitmap and optional mask bitmap.
		"""
		...


class CallLater:
	""" A convenience class for wx.Timer, that calls the given callable object once after the given amount of milliseconds, passing any positional or keyword args. The return value of the callable is available after it has been run with the GetResult method.
	"""

	def __init__(self, millis: int, callableObj: Callable):
		""" Constructor
		"""
		raise NotImplementedError


class CallAfter:
	""" Calling this function on an object schedules an asynchronous call to the functor specified as CallAfter() argument at a (slightly) later time. This is useful when processing some events as certain actions typically can't be performed inside their handlers, e.g. you shouldn't show a modal dialog from a mouse click event handler as this would break the mouse capture state – but you can call a function showing this message dialog after the current event handler completes.
	"""

	def __init__(self, callableObj: Callable, *args, **kw):
		""" Constructor
		"""
		raise NotImplementedError


class AppConsole:

	def SetAppDisplayName(self, name: str) -> None:
		""" Set the application name to be used in the user-visible places such as window titles.
			See GetAppDisplayName for more about the differences between the display name and name.
			Notice that if this function is called, the name is used as is, without any capitalization as done by default by GetAppDisplayName .
		"""

	def SetAppName(self, name: str) -> None:
		""" Sets the name of the application.
			This name should be used for file names, configuration file entries and other internal strings. For the user-visible strings, such as the window titles, the application display name set by SetAppDisplayName is used instead.
			By default the application name is set to the name of its executable file.
		"""

	def SetVendorDisplayName(self, name: str) -> None:
		""" Set the vendor name to be used in the user-visible places.
		"""

	def SetVendorName(self, name: str) -> None:
		""" Sets the name of application's vendor.
			The name will be used in registry access. A default name is set by wxWidgets.
		"""


class App(EvtHandler, AppConsole):
	""" Inteface voor wx.App
	"""

	def MainLoop(self) -> None:
		""" Execute the main GUI event loop
		"""
		...

	def ExitMainLoop(self) -> None:
		""" Stop the MainLoop
		"""
		...

	def SetTopWindow(self, frame: TopLevelWindow) -> None:
		""" Set the main” top level window, which will be used for the parent of the on-demand output window as well as for dialogs that do not have an explicit parent set.
		"""
		...

	def GetTopWindow(self) -> TopLevelWindow:
		""" Get the “main” top level window, which will be used for the parent of the on-demand output window as well as for dialogs that do not have an explicit parent set.
		"""
		...

	def SetAssertMode(self, wxAppAssertMode: int) -> None:
		"""Set the mode indicating how the application responds to assertion statements. Valid settings are a combination of these flags:
		"""
		...


class Notebook(Control):
	""" Interface voor wx.Notebook
	"""


class KeyboardState:

	def ControlDown(self) -> bool:
		""" Returns True if the Control key or Apple/Command key under macOS is pressed.

			This function doesn't distinguish between right and left control keys.

			Notice that GetModifiers should usually be used instead of this one.
		"""


class KeyEvent(KeyboardState, Event):
	""" Interface voor wx.KeyEvent
	"""

	def GetKeyCode(self) -> int:
		""" Returns the key code of the key that generated this event.

			ASCII symbols return normal ASCII values, while events from special keys such as “left cursor arrow” ( WXK_LEFT ) return values outside of the ASCII range. See wx.KeyCode for a full list of the virtual key codes.

			Note that this method returns a meaningful value only for special non-alphanumeric keys or if the user entered a Latin-1 character (this includes ASCII and the accented letters found in Western European languages but not letters of other alphabets such as e.g. Cyrillic). Otherwise it simply method returns WXK_NONE and GetUnicodeKey should be used to obtain the corresponding Unicode character.

			Using GetUnicodeKey is in general the right thing to do if you are interested in the characters typed by the user, GetKeyCode should be only used for special keys (for which GetUnicodeKey returns WXK_NONE ). To handle both kinds of keys you might write:
		"""


class CommandEvent(Event):
	""" Interface voor wx.Event
	"""

	def SetString(self, string: str) -> None:
		""" Sets the m_commandString member.
		"""


class PyCommandEvent(Event):
	""" Interface voor wx.Event
	"""

	def __init__(self, eventType: int, windowId: int):
		""" Constructor
		"""
		...


class ComboBox(ItemContainer, TextEntry, Control):
	""" Interface voor wx.ComboBox
	"""

	def __init__(self, parent: Window, choices: list, style: int = None, size: tuple[int, int] = -1, pos: tuple[int, int] = -1):
		""" Constructor
		"""
		...

	def SetTextSelection(self, from_: int, to_: int) -> None:
		""" Same as wx.TextEntry.SetSelection
		"""


class ItemKind:
	""" Interface voor wx.ItemKind
	"""
	ITEM_SEPARATOR = 0
	ITEM_NORMAL = 1
	ITEM_CHECK = 2
	ITEM_RADIO = 3
	ITEM_DROPDOWN = 4
	ITEM_MAX = 5


class Menu(EvtHandler):
	""" Interface voor wx.Menu
	"""

	def __init__(self, parent: Optional[Window] = None, style: int = None):
		""" Constructor
		"""
		...

	def Append(self, id: int, item: str = "", helpString: str = "", kind: int = ItemKind.ITEM_NORMAL) -> None:
		""" Adds a menu item.
		"""
		...

	def AppendRadioItem(self, id: int, item: str, help: str = "") -> None:
		""" Adds a radio item to the end of the menu.
		"""
		...

	def AppendSeparator(self) -> None:
		""" Adds a separator to the end of the menu.
		"""
		...

	def Check(self, id: int, check: bool) -> None:
		""" Checks or unchecks the menu item.
		"""
		...

	def Enable(self, id: int, enable: bool) -> None:
		""" Enables or disables (greys out) a menu item.
		"""
		...

	def GetLabel(self, id: int) -> str:
		""" Returns a menu item label.
		"""
		...


class ListBox(ItemContainer, Control):
	""" Interface voor wx.ListBox
	"""

	def __init__(self, parent: Window, choices: list, style: int = None, size: tuple[int, int] = -1, pos: tuple[int, int] = -1):
		""" Constructor
		"""

	def SetSelection(self, n: int) -> None:
		""" Sets the selection to the given item n or removes the selection entirely if n == NOT_FOUND .
		"""

	def GetSelection(self) -> int:
		""" Returns the index of the selected item or NOT_FOUND if no item is selected.
		"""

	def GetSelections(self) -> list[int]:
		""" Fill an array of ints with the positions of the currently selected items.
		"""


class RadioBox(Control):
	""" Interface voor wx.RadioBox
	"""

	def __init__(self, parent: Window, id: int = -1, label: str = "", pos: tuple[int, int] = None, size: tuple[int, int] = None, choices: list[str] = [], majorDimension: int = 0, style: int = -1, validator: Any = None, name: str = ""):
		""" Constructor
		"""

	def EnableItem(self, n: int, enable: bool = True) -> bool:
		""" Enables or disables an individual button in the radiobox.
		"""

	def SetSelection(self, n: int) -> None:
		""" Sets the selection to the given item.

			Notice that a radio box always has selection, so n must be valid here and passing NOT_FOUND is not allowed.
		"""

	def GetSelection(self) -> int:
		""" Returns the index of the selected item.

			As radio boxes always have a selected item, the return value is never NOT_FOUND for this class.
		"""


class Log:
	""" Interface voor wx.Log
	"""

	@classmethod
	def SetActiveTarget(cls, target: 'Log') -> None:
		""" Sets the specified log target as the active one.
		"""
		...


def GetApp() -> App:
	""" Retrieve the WX App
	"""
	...


def PostEvent(window: EvtHandler, event: Event) -> None:
	""" Send an Event
	"""
	...
