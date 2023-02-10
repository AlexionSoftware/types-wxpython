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
BK_DEFAULT: int
NO_IMAGE: int
TE_READONLY: int
MODERN: int
FIXED_MINSIZE: int
ALIGN_CENTER_VERTICAL: int

ACCEL_NORMAL: int
ACCEL_CTRL: int
ACCEL_SHIFT: int
WXK_F1: int
WXK_F2: int
WXK_F3: int
WXK_F4: int
WXK_F5: int
WXK_F6: int
WXK_F7: int
WXK_F8: int
WXK_F9: int
WXK_F10: int
WXK_F11: int
WXK_F12: int
WXK_DELETE: int

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
EVT_SIZE: int
EVT_ICONIZE: int

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
DefaultSize: tuple[int, int] = (-1, -1)
DefaultPosition: tuple[int, int] = (-1, -1)

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

	def __init__(self, parent: Any, id: int = None, pos: Optional[Union['Position', tuple[int, int]]] = None, size: Optional[Union['Size', tuple[int, int]]] = None, style: int = 0, name: str = "", title: str = "") -> None:
		""" Constructs a window, which can be a child of a frame, dialog or any other non-control window.
		"""

	def GetScreenRect(self) -> 'Size':
		""" Returns the position and size of the window on the screen as a wxRect object.
		"""

	def GetHandle(self) -> Any:
		""" Returns the platform-specific handle of the physical window.

			Cast it to an appropriate handle, such as HWND for Windows, Widget for Motif or GtkWidget for GTK.
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

	def SetMinSize(self, size: Union['Size', tuple[int, int]]) -> None:
		""" Sets the minimum size of the window, to indicate to the sizer layout mechanism that this is the minimum required size.
		"""

	def SetMaxSize(self, size: Union['Size', tuple[int, int]]) -> None:
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

	def SetPosition(self, pt: Union[tuple[int, int], 'Position']) -> None:
		""" Moves the window to the specified position.

			This is exactly the same as calling Move with the default arguments.
		"""

	def SetSize(self, size: Union[tuple[int, int], 'Size']) -> None:
		""" Sets the size of the window in pixels.
		"""

	def CenterOnScreen(self, direction: int = -1) -> None:
		""" A synonym for CentreOnScreen .
		"""

	def CentreOnScreen(self, direction: int = -1) -> None:
		""" Centres the window on screen.
			Specifies the direction for the centering. May be HORIZONTAL , VERTICAL or BOTH .
		"""


NullCursor: 'Cursor'
CURSOR_WAIT: int


class Cursor:
	""" Interface voor wx.Cursor
	"""

	def __init__(self, cursor: int) -> None:
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

	def IsMaximized(self) -> bool:
		""" Returns true if the window is maximized.
		"""

	def SetTitle(self, title: str) -> None:
		""" Sets the window title.
		"""

	def SetIcon(self, icon: Icon) -> None:
		""" Sets the icon for this window.
		"""

	def SetIcons(self, icons: 'IconBundle') -> None:
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

	def IsModal(self) -> bool:
		""" Returns True if the dialog box is modal, False otherwise.
		"""


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

	def __init__(self, parent: Any, id: int = 0, pos: Optional[Union['Position', tuple[int, int]]] = None, size: Optional[Union['Size', tuple[int, int]]] = None, choices: list[Any] = None, style: int = None, validator: int = None, name: str = None) -> None:
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

	def __init__(self, parent: Any, id: int = 0, label: str = "", pos: Optional[Union['Position', tuple[int, int]]] = None, size: Optional[Union['Size', tuple[int, int]]] = None, style: int = 0, validator: int = None, name: str = "") -> None:
		pass

	def IsChecked(self) -> bool:
		""" This is just a maybe more readable synonym for GetValue : just as the latter, it returns True if the checkbox is checked and False otherwise.
		"""


class Panel(Window):
	""" Interface voor wx.Panel
	"""


class TextEntry:
	""" Common base class for single line text entry fields.
	"""

	def AppendText(self, text: str) -> None:
		""" Appends the text to the end of the text control.

			Note After the text is appended, the insertion point will be at the end of the text control. If this behaviour is not desired, the programmer should use GetInsertionPoint and SetInsertionPoint .
		"""

	def AutoComplete(self, choices: list[str]) -> bool:
		""" Call this function to enable auto-completion of the text typed in a single-line text control using the given choices.

			Returns: True if the auto-completion was enabled or False if the operation failed, typically because auto-completion is not supported by the current platform.
		"""

	def AutoCompleteDirectories(self) -> bool:
		""" Call this function to enable auto-completion of the text using the file system directories.

			Unlike AutoCompleteFileNames which completes both file names and directories, this function only completes the directory names.

			Notice that currently this function is only implemented in wxMSW port and does nothing under the other platforms.

			Returns: True if the auto-completion was enabled or False if the operation failed, typically because auto-completion is not supported by the current platform.
		"""

	def AutoCompleteFileNames(self) -> bool:
		""" Call this function to enable auto-completion of the text typed in a single-line text control using all valid file system paths.

			Notice that currently this function is only implemented in wxMSW port and does nothing under the other platforms.

			Returns: True if the auto-completion was enabled or False if the operation failed, typically because auto-completion is not supported by the current platform.
		"""

	def CanCopy(self) -> bool:
		""" Returns True if the selection can be copied to the clipboard.
		"""

	def CanCut(self) -> bool:
		""" Returns True if the selection can be cut to the clipboard.
		"""

	def CanPaste(self) -> bool:
		""" Returns True if the contents of the clipboard can be pasted into the text control.

			On some platforms (Motif, GTK) this is an approximation and returns True if the control is editable, False otherwise.
		"""

	def CanRedo(self) -> bool:
		""" Returns True if there is a redo facility available and the last operation can be redone.
		"""

	def CanUndo(self) -> bool:
		""" Returns True if there is an undo facility available and the last operation can be undone.
		"""

	def ChangeValue(self, value: str) -> None:
		""" Sets the new text control value.

			It also marks the control as not-modified which means that IsModified() would return False immediately after the call to ChangeValue .

			The insertion point is set to the start of the control (i.e. position 0) by this function.

			This functions does not generate the wxEVT_TEXT event but otherwise is identical to SetValue .

			See User Generated Events vs Programmatically Generated Events for more information.
		"""

	def Clear(self) -> None:
		""" Clears the text in the control.

			Note that this function will generate a wxEVT_TEXT event, i.e. its effect is identical to calling SetValue (“”).
		"""

	def Copy(self) -> None:
		""" Copies the selected text to the clipboard.
		"""

	def Cut(self) -> None:
		""" Copies the selected text to the clipboard and removes it from the control.
		"""

	def ForceUpper(self) -> None:
		""" Convert all text entered into the control to upper case.

			Call this method to ensure that all text entered into the control is converted on the fly to upper case. If the control is not empty, its existing contents is also converted to upper case.
		"""

	def GetHint(self) -> str:
		""" Returns the current hint string.
		"""

	def GetInsertionPoint(self) -> int:
		""" Returns the insertion point, or cursor, position.

			This is defined as the zero based index of the character position to the right of the insertion point. For example, if the insertion point is at the end of the single-line text control, it is equal to GetLastPosition .

			Notice that insertion position is, in general, different from the index of the character the cursor position at in the string returned by GetValue . While this is always the case for the single line controls, multi-line controls can use two characters "\\r\\n" as line separator (this is notably the case under MSW) meaning that indices in the control and its string value are offset by 1 for every line.
		"""

	def GetLastPosition(self) -> int:
		""" Returns the zero based index of the last position in the text control, which is equal to the number of characters in the control.
		"""

	def GetMargins(self) -> 'Size':
		""" Returns the margins used by the control.

			The x field of the returned point is the horizontal margin and the y field is the vertical one.
		"""

	def GetRange(self, from_: int, to_: int) -> str:
		""" Returns the string containing the text starting in the positions from and up to to in the control.

			The positions must have been returned by another wx.TextCtrl method. Please note that the positions in a multiline wx.TextCtrl do not correspond to the indices in the string returned by GetValue because of the different new line representations ( CR or CR LF) and so this method should be used to obtain the correct results instead of extracting parts of the entire value. It may also be more efficient, especially if the control contains a lot of data.
		"""

	def GetSelection(self) -> tuple[int, int]:
		""" Gets the current selection span.

			If the returned values are equal, there was no selection. Please note that the indices returned may be used with the other wx.TextCtrl methods but don’t necessarily represent the correct indices into the string returned by GetValue for multiline controls under Windows (at least,) you should use GetStringSelection to get the selected text.
		"""

	def GetStringSelection(self) -> str:
		""" Gets the text currently selected in the control.

			If there is no selection, the returned string is empty.
		"""

	def GetValue(self) -> str:
		""" Gets the contents of the control.

			Notice that for a multiline text control, the lines will be separated by (Unix-style) \n characters, even under Windows where they are separated by a \r\n sequence in the native control.
		"""

	def IsEditable(self) -> bool:
		""" Returns True if the controls contents may be edited by user (note that it always can be changed by the program).

			In other words, this functions returns True if the control hasn’t been put in read-only mode by a previous call to SetEditable .
		"""

	def IsEmpty(self) -> bool:
		""" Returns True if the control is currently empty.

			This is the same as GetValue .empty() but can be much more efficient for the multiline controls containing big amounts of text.
		"""

	def Paste(self) -> None:
		""" Pastes text from the clipboard to the text item.
		"""

	def Redo(self) -> None:
		""" If there is a redo facility and the last operation can be redone, redoes the last operation.

			Does nothing if there is no redo facility.
		"""

	def Remove(self, from_: int, to_: int) -> None:
		""" Removes the text starting at the first given position up to (but not including) the character at the last position.

			This function puts the current insertion point position at to as a side effect.
		"""

	def Replace(self, from_: int, to_: int, value: str) -> None:
		""" Replaces the text starting at the first position up to (but not including) the character at the last position with the given text.

			This function puts the current insertion point position at to as a side effect.
		"""

	def SelectAll(self) -> None:
		""" Selects all text in the control.
		"""

	def SelectNone(self) -> None:
		""" Deselects selected text in the control.
		"""

	def SetEditable(self, editable: bool) -> None:
		""" Makes the text item editable or read-only, overriding the wx.TE_READONLY flag.
		"""

	def SetHint(self, hint: str) -> bool:
		""" Sets a hint shown in an empty unfocused text control.

			The hints are usually used to indicate to the user what is supposed to be entered into the given entry field, e.g. a common use of them is to show an explanation of what can be entered in a wx.SearchCtrl.

			The hint is shown (usually greyed out) for an empty control until it gets focus and is shown again if the control loses it and remains empty. It won’t be shown once the control has a non-empty value, although it will be shown again if the control contents is cleared. Because of this, it generally only makes sense to use hints with the controls which are initially empty.

			Notice that hints are known as cue banners under MSW or placeholder strings under macOS.

			For the platforms without native hints support, the implementation has several known limitations. Notably, the hint display will not be properly updated if you change wx.TextEntry contents programmatically when the hint is displayed using methods other than SetValue or ChangeValue or others which use them internally (e.g. Clear ). In other words, currently you should avoid calling methods such as WriteText or Replace when using hints and the text control is empty. If you bind to the control's focus and wxEVT_TEXT events, you must call wx.Event.Skip on them so that the generic implementation works correctly.

			Another limitation is that hints are ignored for the controls with TE_PASSWORD style.
		"""

	def SetInsertionPoint(self, pos: int) -> None:
		""" Sets the insertion point at the given position.
		"""

	def SetInsertionPointEnd(self) -> None:
		""" Sets the insertion point at the end of the text control.

			This is equivalent to calling wx.TextCtrl.SetInsertionPoint with wx.TextCtrl.GetLastPosition argument.
		"""

	def SetMargins(self, pt: 'Size') -> bool:
		""" Attempts to set the control margins.

			When margins are given as wx.Point, x indicates the left and y the top margin. Use -1 to indicate that an existing value should be used.
		"""

	def SetMaxLength(self, len: int) -> None:
		""" This function sets the maximum number of characters the user can enter into the control.

			In other words, it allows limiting the text value length to len not counting the terminating NUL character.

			If len is 0, the previously set max length limit, if any, is discarded and the user may enter as much text as the underlying native text control widget supports (typically at least 32Kb). If the user tries to enter more characters into the text control when it already is filled up to the maximal length, a wxEVT_TEXT_MAXLEN event is sent to notify the program about it (giving it the possibility to show an explanatory message, for example) and the extra input is discarded.

			Note that in wxGTK this function may only be used with single line text controls.
		"""

	def SetSelection(self, from_: int, to_: int) -> None:
		""" Selects the text starting at the first position up to (but not including) the character at the last position.

			If both parameters are equal to -1 all text in the control is selected.

			Notice that the insertion point will be moved to from by this function.
		"""

	def SetValue(self, value: str) -> None:
		""" Sets the new text control value.

			It also marks the control as not-modified which means that IsModified() would return False immediately after the call to SetValue .

			The insertion point is set to the start of the control (i.e. position 0) by this function unless the control value doesn’t change at all, in which case the insertion point is left at its original position.

			Note that, unlike most other functions changing the controls values, this function generates a wxEVT_TEXT event. To avoid this you can use ChangeValue instead.
		"""

	def Undo(self) -> None:
		""" If there is an undo facility and the last operation can be undone, undoes the last operation.

			Does nothing if there is no undo facility.
		"""

	def WriteText(self, text: str) -> None:
		""" Writes the text into the text control at the current insertion position.
		"""


class TextCtrl(TextEntry, Control):
	""" Interface voor wx.TextCtrl
	"""

	def __init__(self, parent: Any, id: int = None, pos: Optional[Union['Position', tuple[int, int]]] = None, size: Optional[Union['Size', tuple[int, int]]] = None, style: int = 0, name: str = "", title: str = "", value: str = "") -> None:
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

	def __init__(self, *args, **kwargs) -> None:
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

	def __init__(self, orient: int = 'HORIZONTAL') -> None:
		""" Constructor for a wx.BoxSizer
		"""
		pass

	def SetOrientation(self, orient: int) -> None:
		""" Sets the orientation of the box sizer, either wx.VERTICAL or wx.HORIZONTAL.
		"""


class WrapSizer(Sizer):
	""" Interface voor wx.WrapSizer
	"""

	def __init__(self) -> None:
		""" Constructor for a wx.WrapSizer
		"""
		pass


class GridSizer(Sizer):
	""" Interface voor wx.GridSizer
	"""

	def __init__(self, rows: int = 0, cols: int = 0, vgap: int = 0, hgap: int = 0) -> None:
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

	def __init__(self, row: int = 0, col: int = 0) -> None:
		""" Construct a new wx.GBPosition, setting the row and column.
		"""


class GBSpan:
	""" This class is used to hold the row and column spanning attributes of items in a GridBagSizer.
	"""

	def __init__(self, rowspan: int = 0, colspan: int = 0) -> None:
		""" Construct a new wx.GBSpan, setting the rowspan and colspan.
		"""


class GridBagSizer(FlexGridSizer):
	""" A wx.Sizer that can lay out items in a virtual grid like a wx.FlexGridSizer but in this case explicit positioning of the items is allowed using wx.GBPosition, and items can optionally span more than one row and/or column using wx.GBSpan.
	"""

	def __init__(self, vgap: int = 0, hgap: int = 0) -> None:
		""" Construct
		"""

	def Add(self, window: Window, pos: GBPosition, span: GBSpan = None, flag: int = 0, border: int = 0, userData: Any = None) -> SizerItem:
		""" Adds the given item to the given position.
		"""


class Size:
	""" Interface voor wx.Size
	"""

	def __init__(self, width: Optional[int] = None, height: Optional[int] = None) -> None:
		""" Initializes this size object with the given width and height.
		"""

	def GetHeight(self) -> int:
		""" Gets the height member.
		"""

	def GetWidth(self) -> int:
		""" Gets the width member.
		"""


class Position:
	""" Interface voor wx.Position
	"""


class FrozenWindow(ContextManager):
	""" Interface voor wx.FrozenWindow
	"""

	def __init__(self, window: Window) -> None:
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


class AnyButton(Control):
	""" Interface voor wx.AnyButton
	"""

	def GetBitmap(self) -> 'Bitmap':
		""" Return the bitmap shown by the button.

			The returned bitmap may be invalid only if the button doesn’t show any images.
		"""

	def GetBitmapCurrent(self) -> 'Bitmap':
		""" Returns the bitmap used when the mouse is over the button.

			The returned bitmap is only valid if SetBitmapCurrent had been previously called.
		"""

	def GetBitmapDisabled(self) -> 'Bitmap':
		""" Returns the bitmap used for the disabled state.

			The returned bitmap is only valid if SetBitmapDisabled had been previously called.
		"""

	def GetBitmapFocus(self) -> 'Bitmap':
		""" Returns the bitmap used for the focused state.

			The returned bitmap is only valid if SetBitmapFocus had been previously called.
		"""

	def GetBitmapLabel(self) -> 'Bitmap':
		""" Returns the bitmap for the normal state.

			This is exactly the same as GetBitmap but uses a name backwards-compatible with wx.BitmapButton.
		"""

	def GetBitmapMargins(self) -> Size:
		""" Get the margins between the bitmap and the text of the button.
		"""

	def GetBitmapPressed(self) -> 'Bitmap':
		""" Returns the bitmap used when the button is pressed.

			The returned bitmap is only valid if SetBitmapPressed had been previously called.
		"""

	def SetBitmap(self, bitmap: 'Bitmap', dir: int = -1) -> None:
		""" Sets the bitmap to display in the button.

			The bitmap is displayed together with the button label. This method sets up a single bitmap which is used in all button states, use SetBitmapDisabled , SetBitmapPressed , SetBitmapCurrent or SetBitmapFocus to change the individual images used in different states.
		"""

	def SetBitmapCurrent(self, bitmap: 'Bitmap') -> None:
		""" Sets the bitmap to be shown when the mouse is over the button.

			If bitmap is invalid, the normal bitmap will be used in the current state.
		"""

	def SetBitmapDisabled(self, bitmap: 'Bitmap') -> None:
		""" Sets the bitmap for the disabled button appearance.

			If bitmap is invalid, the disabled bitmap is set to the automatically generated greyed out version of the normal bitmap, i.e. the same bitmap as is used by default if this method is not called at all. Use SetBitmap with an invalid bitmap to remove the bitmap completely (for all states).
		"""

	def SetBitmapFocus(self, bitmap: 'Bitmap') -> None:
		""" Sets the bitmap for the button appearance when it has the keyboard focus.

			If bitmap is invalid, the normal bitmap will be used in the focused state.
		"""

	def SetBitmapLabel(self, bitmap: 'Bitmap') -> None:
		""" Sets the bitmap label for the button.
		"""

	def SetBitmapMargins(self, *args, **kw) -> None:
		""" Set the margins between the bitmap and the text of the button.

			This method is currently only implemented under MSW. If it is not called, default margin is used around the bitmap.
		"""

	def SetBitmapPosition(self, dir: int) -> None:
		""" Set the position at which the bitmap is displayed.

			This method should only be called if the button does have an associated bitmap.
		"""

	def SetBitmapPressed(self, bitmap: 'Bitmap') -> None:
		""" Sets the bitmap for the selected (depressed) button appearance.
		"""


class Button(AnyButton):
	""" Interface voor wx.Button
	"""

	def __init__(self, parent: Any, id: int = None, pos: Optional[Union['Position', tuple[int, int]]] = None, size: Optional[Union['Size', tuple[int, int]]] = None, style: int = 0, name: str = "", label: str = "") -> None:
		""" Constructs a window, which can be a child of a frame, dialog or any other non-control window.
		"""


class BitmapButton(Button):
	""" Interface voor wx.Button
	"""

	def __init__(self, parent: Window, id: int = -1, bitmap: Optional['Bitmap'] = None, pos: Optional[Union[tuple[int, int], 'Position']] = None, size: Optional[Union[tuple[int, int], 'Size']] = None, style: int = 0, validator: Any = None, name: str = "") -> None:
		""" Constructor, creating and showing a button.
		"""


class StaticText(Window):
	""" Interface voor wx.StaticText
	"""

	def __init__(self, parent: Window, label: str = None, style: int = None, size: Optional[Union['Size', tuple[int, int]]] = None, pos: Optional[Union['Position', tuple[int, int]]] = None) -> None:
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

	def __init__(self, parent: Window, id: int = -1, label: str = "", pos: Optional[Union['Position', tuple[int, int]]] = None, size: Optional[Union['Size', tuple[int, int]]] = None, style: int = 0, name: str = ""):
		""" Constructor
		"""


class StaticBoxSizer(BoxSizer):
	""" Interface voor wx.StaticBoxSizer
	"""

	def __init__(self, box: StaticBox, orient: int = 0) -> None:
		""" Constructor
		"""


class AcceleratorTable:
	""" Interface voor wx.AcceleratorTable
	"""

	def __init__(self, entries: list[tuple[int, int, int]]) -> None:
		""" Constructor
		"""


class StaticLine(Window):
	""" Interface voor wx.StaticLine
	"""

	def __init__(self, parent: Any, orien: int = -1, pos: Optional[Union['Position', tuple[int, int]]] = None, size: Optional[Union['Size', tuple[int, int]]] = None, style: int = None):
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

	def __init__(self, name: str, type: int = 1) -> None:
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

	def __init__(self, parent: Window, id: int = 'ID_ANY', bitmap: Bitmap = None, pos: Optional[Union['Position', tuple[int, int]]] = None, size: Optional[Union['Size', tuple[int, int]]] = None, style: int = 0, name: str = "") -> None:
		""" Constructor, creating and showing a static bitmap control.
		"""
		...


class ImageList:
	""" Interface voor wx.ImageList
	"""

	def __init__(self, width: int, height: int) -> None:
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

	def __init__(self, millis: int, callableObj: Callable) -> None:
		""" Constructor
		"""
		raise NotImplementedError


class CallAfter:
	""" Calling this function on an object schedules an asynchronous call to the functor specified as CallAfter() argument at a (slightly) later time. This is useful when processing some events as certain actions typically can't be performed inside their handlers, e.g. you shouldn't show a modal dialog from a mouse click event handler as this would break the mouse capture state – but you can call a function showing this message dialog after the current event handler completes.
	"""

	def __init__(self, callableObj: Callable, *args, **kw) -> None:
		""" Constructor
		"""
		raise NotImplementedError


class EventLoopBase:
	""" Interface voor wx.EventLoopBase
	"""

	def Dispatch(self) -> bool:
		""" Dispatches the next event in the windowing system event queue.

			Blocks until an event appears if there are none currently (use Pending if this is not wanted).

			Returns False if the event loop should stop and True otherwise.
		"""

	def DispatchTimeout(self, timeout: int) -> int:
		""" Dispatch an event but not wait longer than the specified timeout for it.

			If an event is received before the specified timeout expires, it is processed and the function returns 1 normally or 0 if the event loop should quite. Otherwise, i.e. if the timeout expires, the functions returns -1 without processing any events.

			Returns 1 if an event was processed, 0 if the event loop should quit or -1 if the timeout expired.
		"""

	def Exit(self, rc: int = 0) -> None:
		""" Exit the currently running loop with the given exit code.

			The loop will exit, i.e. its Run method will return, during the next event loop iteration.

			Notice that this method can only be used if this event loop is the currently running one, i.e. its IsRunning returns True. If this is not the case, an assert failure is triggered and nothing is done as outer event loops can’t be exited from immediately. Use ScheduleExit if you’d like to exit this loop even if it doesn’t run currently.
		"""

	@staticmethod
	def GetActive() -> Optional['EventLoopBase']:
		""" Return the currently active (running) event loop.

			May return None if there is no active event loop (e.g. during application startup or shutdown).
		"""

	def IsEventAllowedInsideYield(self, cat: int) -> bool:
		""" Returns True if the given event category is allowed inside a YieldFor call (i.e.

			compares the given category against the last mask passed to YieldFor ).
		"""

	def IsMain(self) -> bool:
		""" Returns True if this is the main loop executed by wx.App.OnRun .
		"""

	def IsOk(self) -> bool:
		""" Use this to check whether the event loop was successfully created before using it.
		"""

	def IsRunning(self) -> bool:
		""" Return True if this event loop is currently running.

			Notice that even if this event loop hasn't terminated yet but has just spawned a nested (e.g. modal) event loop, this method would return False.
		"""

	def IsYielding(self) -> bool:
		""" Returns True if called from inside wx.Yield or from inside YieldFor .
		"""

	def OnExit(self) -> None:
		""" This function is called before the event loop terminates, whether this happens normally (because of wx.Exit call) or abnormally (because of an exception thrown from inside the loop).

		The default implementation calls wx.AppConsole.OnEventLoopExit .
	"""

	def Pending(self) -> bool:
		""" Return True if any events are available.

			If this method returns True, calling Dispatch will not block.
		"""

	def ProcessIdle(self) -> bool:
		""" This virtual function is called when the application becomes idle and normally just sends wx.IdleEvent to all interested parties.

		It should return True if more idle events are needed, False if not.
	"""

	def Run(self) -> int:
		""" Start the event loop, return the exit code when it is finished.

			Logically, this method calls Dispatch in a loop until it returns False and also takes care of generating idle events during each loop iteration. However not all implementations of this class really implement it like this (e.g. wxGTK does not) so you shouldn’t rely on Dispatch being called from inside this function.
		"""

	def ScheduleExit(self, rc: int = 0) -> None:
		""" Schedule an exit from the loop with the given exit code.

			This method is similar to wx.Exit but can be called even if this event loop is not the currently running one – and if it is the active loop, then it works in exactly the same way as wx.Exit .

			The loop will exit as soon as the control flow returns to it, i.e. after any nested loops terminate.
		"""

	@staticmethod
	def SetActive(loop: 'EventLoopBase') -> None:
		"""	Set currently active (running) event loop.

			Called by wx.EventLoopActivator, use an instance of this class instead of calling this method directly to ensure that the previously active event loop is restored.

			Results in a call to wx.AppConsole.OnEventLoopEnter .
		"""

	def WakeUp(self) -> None:
		""" Called by wxWidgets to wake up the event loop even if it is currently blocked inside Dispatch .
		"""

	def WakeUpIdle(self) -> None:
		""" Makes sure that idle events are sent again.
		"""

	def Yield(self, onlyIfNeeded: bool = False) -> bool:
		""" Yields control to pending messages in the windowing system.

			This can be useful, for example, when a time-consuming process writes to a text window. Without an occasional yield, the text window will not be updated properly, and on systems with cooperative multitasking, other processes will not respond.

			Caution should be exercised, however, since yielding may allow the user to perform actions which are not compatible with the current task. Disabling menu items or whole menus during processing can avoid unwanted reentrance of code: see wx.SafeYield for a better function.

			Note that wx.Yield will not flush the message logs. This is intentional as calling wx.Yield is usually done to quickly update the screen and popping up a message box dialog may be undesirable. If you do wish to flush the log messages immediately (otherwise it will be done during the next idle loop iteration), call wx.Log.FlushActive .

			If onlyIfNeeded parameter is True and the flow control is already inside wx.Yield , i.e. IsYielding returns True, the method just silently returns False and doesn’t do anything.
		"""

	def YieldFor(self, eventsToProcess: int) -> bool:
		""" Works like wx.Yield with onlyIfNeeded == True, except that it allows the caller to specify a mask of the wx.EventCategory values which indicates which events should be processed and which should instead be “delayed” (i.e. processed by the main loop later).

			Note that this is a safer alternative to wx.Yield since it ensures that only the events you’re interested to will be processed; i.e. this method helps to avoid unwanted reentrancies.

			Note that currently only wxMSW and wxGTK do support selective yield of native events coming from the underlying GUI toolkit. wxWidgets events posted using wx.EvtHandler.AddPendingEvent or wx.EvtHandler.QueueEvent are instead selectively processed by all ports.
		"""


class AppConsole:
	""" Interface voor wx.AppConsole
	"""

	def GetMainLoop(self) -> EventLoopBase:
		""" Returns the main event loop instance, i.e. the event loop which is started by OnRun and which dispatches all events sent from the native toolkit to the application (except when new event loops are temporarily set-up).

		The returned value maybe None. Put initialization code which needs a not None main event loop into OnEventLoopEnter .
		"""

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

	def AddPage(self, page: Window, text: str, select: bool = False, imageId: int = -1) -> bool:
		""" Adds a new page.

			The page must have the book control itself as the parent and must not have been added to this control previously.

			The call to this function will generate the page changing and page changed events if select is True, but not when inserting the very first page (as there is no previous page selection to switch from in this case and so it wouldn’t make sense to e.g. veto such event).
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

	def __init__(self, eventType: int, windowId: int) -> None:
		""" Constructor
		"""
		...


class ComboBox(ItemContainer, TextEntry, Control):
	""" Interface voor wx.ComboBox
	"""

	def __init__(self, parent: Window, choices: list, style: int = None, size: Optional[Union['Size', tuple[int, int]]] = None, pos: Optional[Union['Position', tuple[int, int]]] = None):
		""" Constructor
		"""
		...

	def SetTextSelection(self, from_: int, to_: int) -> None:
		""" Same as wx.TextEntry.SetSelection
		"""

	def FindString(self, search: str) -> int:
		""" Finds an item whose label matches the given string.
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

	def __init__(self, parent: Optional[Window] = None, style: int = None) -> None:
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

	def __init__(self, parent: Window, choices: list, style: int = None, size: Optional[Union['Size', tuple[int, int]]] = None, pos: Optional[Union['Position', tuple[int, int]]] = None):
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


class CheckListBox(ListBox):
	""" Interface voor wx.CheckListBox
	"""


class RadioBox(Control):
	""" Interface voor wx.RadioBox
	"""

	def __init__(self, parent: Window, id: int = -1, label: str = "", pos: Optional[Union['Position', tuple[int, int]]] = None, size: Optional[Union['Size', tuple[int, int]]] = None, choices: list[str] = [], majorDimension: int = 0, style: int = -1, validator: Any = None, name: str = ""):
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


class DataFormat:
	""" Interface voor wx.DataFormat
	"""

	def __init__(self, format: Any) -> None:
		""" Constructs a data format object for a custom format identified by its name format.
		"""

	def GetId(self) -> str:
		""" Returns the name of a custom format (this function will fail for a standard format).
		"""

	def GetType(self) -> int:
		""" Returns the platform-specific number identifying the format.
		"""

	def SetId(self, format: str) -> None:
		""" Sets the format to be the custom format identified by the given name.
		"""

	def SetType(self, type: int) -> None:
		""" Sets the format to the given value, which should be one of DF_XXX constants.
		"""


class DataObject:
	""" Interface voor wx.DataObject
	"""

	def GetAllFormats(self, dir: int = -1) -> list[DataFormat]:
		""" Returns a list of wx.DataFormat objects which this data object supports transferring in the given direction.
		"""

	def GetDataHere(self, format: DataFormat, buf: Any) -> bool:
		""" Copies this data object’s data in the requested format to the buffer provided.
		"""

	def GetDataSize(self, format: DataFormat) -> int:
		""" Returns the data size of the given format format.
		"""

	def GetFormatCount(self, dir: int = -1) -> int:
		""" Returns the number of available formats for rendering or setting the data.
		"""

	def GetPreferredFormat(self, dir: int = -1) -> DataFormat:
		""" Returns the preferred format for either rendering the data (if dir is Get , its default value) or for setting it.

			Usually this will be the native format of the wx.DataObject.
		"""

	def IsSupported(self, format: DataFormat, dir: int = -1) -> bool:
		""" Returns True if this format is supported.
		"""

	def SetData(self, format: DataFormat, buf: Any) -> bool:
		""" Copies data from the provided buffer to this data object for the specified format.
		"""


class TextDataObject(DataObject):
	""" Interface voor wx.TextDataObject
	"""

	def __init__(self, text: str = "") -> None:
		""" Constructor, may be used to initialise the text (otherwise SetText should be used later).
		"""

	def GetText(self) -> str:
		""" Returns the text associated with the data object.

			You may wish to override this method when offering data on-demand, but this is not required by wxWidgets’ internals. Use this method to get data in text form from the wx.Clipboard.
		"""

	def GetTextLength(self) -> int:
		""" Returns the data size.

			By default, returns the size of the text data set in the constructor or using SetText . This can be overridden to provide text size data on-demand. It is recommended to return the text length plus 1 for a trailing zero, but this is not strictly required.
		"""

	def SetText(self, strText: str) -> None:
		""" Sets the text associated with the data object.

			This method is called when the data object receives the data and, by default, copies the text into the member variable. If you want to process the text on the fly you may wish to override this function.
		"""


class Clipboard:
	""" Interface voor wx.Clipboard
	"""

	def AddData(self, data: DataObject) -> bool:
		""" Call this function to add the data object to the clipboard.

			This is an obsolete synonym for SetData .
		"""

	def Clear(self) -> None:
		""" Clears the global clipboard object and the system’s clipboard if possible.
		"""

	def Close(self) -> None:
		""" Call this function to close the clipboard, having opened it with Open .
		"""

	def Flush(self) -> bool:
		""" Flushes the clipboard: this means that the data which is currently on clipboard will stay available even after the application exits (possibly eating memory), otherwise the clipboard will be emptied on exit.

			Currently this method is implemented in MSW and GTK and always returns False otherwise.

			Returns False if the operation is unsuccessful for any reason.

			Note On GTK, only the non-primary selection can be flushed. Calling this function when the clipboard is using the primary selection will return False and not make any data available after the program exits.
		"""

	@staticmethod
	def Get() -> 'Clipboard':
		""" Returns the global instance (wxTheClipboard) of the clipboard object.
		"""

	def GetData(self, data: str) -> bool:
		""" Call this function to fill data with data on the clipboard, if available in the required format.

			Returns True on success.
		"""

	def IsOpened(self) -> bool:
		""" Returns True if the clipboard has been opened.
		"""

	def IsSupported(self, format: DataFormat) -> bool:
		""" Returns True if there is data which matches the data format of the given data object currently available on the clipboard.

			Todo The name of this function is misleading. This should be renamed to something that more accurately indicates what it does.
		"""

	def IsUsingPrimarySelection(self) -> bool:
		""" Returns True if we are using the primary selection, False if clipboard one.

			See also UsePrimarySelection
		"""

	def Open(self) -> bool:
		""" Call this function to open the clipboard before calling SetData and GetData .

			Call Close when you have finished with the clipboard. You should keep the clipboard open for only a very short time.

			Returns True on success. This should be tested (as in the sample shown above).
		"""

	def SetData(self, data: DataObject) -> bool:
		""" Call this function to set the data object to the clipboard.

			The new data object replaces any previously set one, so if the application wants to provide clipboard data in several different formats, it must use a composite data object supporting all of the formats instead of calling this function several times with different data objects as this would only leave data from the last one in the clipboard.

			After this function has been called, the clipboard owns the data, so do not delete the data explicitly.
		"""

	def UsePrimarySelection(self, primary: bool = False) -> None:
		""" On platforms supporting it (all X11-based ports), wx.Clipboard uses the CLIPBOARD X11 selection by default.

			When this function is called with True, all subsequent clipboard operations will use PRIMARY selection until this function is called again with False.

			On the other platforms, there is no PRIMARY selection and so all clipboard operations will fail. This allows implementing the standard X11 handling of the clipboard which consists in copying data to the CLIPBOARD selection only when the user explicitly requests it (i.e. by selecting the “Copy” menu command) but putting the currently selected text into the PRIMARY selection automatically, without overwriting the normal clipboard contents with the currently selected text on the other platforms.
		"""


TheClipboard: Clipboard


class IconBundle:
	""" Interface voor wx.IconBundle
	"""

	def AddIcon(self, icon: Union[Icon, str], type: int = -1) -> None:
		""" Adds all the icons contained in the file to the bundle; if the collection already contains icons with the same width and height, they are replaced by the new ones.
		"""

	def GetIcon(self, size: Union[tuple[int, int], Size], flags: int = -1) -> Icon:
		""" Returns the icon with the given size.

			If size is wx.DefaultSize , it is interpreted as the standard system icon size, i.e. the size returned by wx.SystemSettings.GetMetric for SYS_ICON_X and SYS_ICON_Y .

			If the bundle contains an icon with exactly the requested size, it’s always returned. Otherwise, the behaviour depends on the flags. If only wx.IconBundle.FALLBACK_NONE is given, the function returns an invalid icon. If wx.IconBundle.FALLBACK_SYSTEM is given, it tries to find the icon of standard system size, regardless of the size passed as parameter. Otherwise, or if the icon system size is not found neither, but wx.IconBundle.FALLBACK_NEAREST_LARGER flag is specified, the function returns the smallest icon of the size larger than the requested one or, if this fails too, just the icon closest to the specified size.
		"""

	def GetIconByIndex(self, n: int) -> Icon:
		""" return the icon at index (must be < GetIconCount )
		"""

	def GetIconCount(self) -> int:
		""" return the number of available icons
		"""

	def GetIconOfExactSize(self, size: Union[tuple[int, int], Size]) -> Icon:
		""" Returns the icon with exactly the given size or wx.NullIcon if this size is not available.
		"""

	def IsEmpty(self) -> bool:
		""" Returns True if the bundle doesn’t contain any icons, False otherwise (in which case a call to GetIcon with default parameter should return a valid icon).
		"""


class SplitterWindow(Window):
	""" Interface voor wx.SplitterWindow
	"""

	def GetDefaultSashSize(self) -> int:
		""" Returns the default sash size in pixels.

			The size of the sash is its width for a vertically split window and its height for a horizontally split one. Its other direction is the same as the client size of the window in the corresponding direction.

			The default sash size is platform-dependent because it conforms to the current platform look-and-feel and cannot be changed.
		"""

	def GetMinimumPaneSize(self) -> int:
		""" Returns the current minimum pane size (defaults to zero).
		"""

	def GetSashGravity(self) -> float:
		""" Returns the current sash gravity.
		"""

	def GetSashPosition(self) -> int:
		""" Returns the current sash position.
		"""

	def GetSashSize(self) -> int:
		""" Returns the default sash size in pixels or 0 if it is invisible.
		"""

	def GetSplitMode(self) -> int:
		""" Gets the split mode.
		"""

	def GetWindow1(self) -> Window:
		""" Returns the left/top or only pane.
		"""

	def GetWindow2(self) -> Window:
		""" Returns the right/bottom pane.
		"""

	def Initialize(self, window: Window) -> None:
		""" Initializes the splitter window to have one pane.

			The child window is shown if it is currently hidden.

			Note This should be called if you wish to initially view only a single pane in the splitter window.
		"""

	def IsSashInvisible(self) -> bool:
		""" Returns True if the sash is invisible even when the window is split, False otherwise.

			Note This is a shortcut for HasFlag(wxSP_NOSASH)
		"""

	def IsSplit(self) -> bool:
		""" Returns True if the window is split, False otherwise.
		"""

	def ReplaceWindow(self, winOld: Window, winNew: Window) -> bool:
		""" This function replaces one of the windows managed by the wx.SplitterWindow with another one.

			It is in general better to use it instead of calling Unsplit and then resplitting the window back because it will provoke much less flicker (if any). It is valid to call this function whether the splitter has two windows or only one.

			Both parameters should be not None and winOld must specify one of the windows managed by the splitter. If the parameters are incorrect or the window couldn’t be replaced, False is returned. Otherwise the function will return True, but please notice that it will not delete the replaced window and you may wish to do it yourself.
		"""

	def SetMinimumPaneSize(self, paneSize: int) -> None:
		""" Sets the minimum pane size.

			Note The default minimum pane size is zero, which means that either pane can be reduced to zero by dragging the sash, thus removing one of the panes. To prevent this behaviour (and veto out-of-range sash dragging), set a minimum size, for example 20 pixels. If the wx.SP_PERMIT_UNSPLIT style is used when a splitter window is created, the window may be unsplit even if minimum size is non-zero.
		"""

	def SetSashGravity(self, gravity: float) -> None:
		""" Sets the sash gravity.

			Notice that when sash gravity for a newly created splitter window, it is often necessary to explicitly set the splitter size using SetSize to ensure that is big enough for its initial sash position. Otherwise, i.e. if the window is created with the default tiny size and only resized to its correct size later, the initial sash position will be affected by the gravity and typically result in sash being at the rightmost position for the gravity of 1. See the example code creating wx.SplitterWindow in the splitter sample for more details.

			Note Gravity is real factor which controls position of sash while resizing wx.SplitterWindow. Gravity tells wx.SplitterWindow how much will left/top window grow while resizing. Example values:
				0.0: only the bottom/right window is automatically resized
				0.5: both windows grow by equal size
				1.0: only left/top window grows Gravity should be a real value between 0.0 and 1.0. Default value of sash gravity is 0.0. That value is compatible with previous (before gravity was introduced) behaviour of wx.SplitterWindow.
		"""

	def SetSashInvisible(self, invisible: bool = True) -> None:
		""" Sets whether the sash should be invisible, even when the window is split.

			When the sash is invisible, it doesn’t appear on the screen at all and, in particular, doesn’t allow the user to resize the windows.

			Note Only sets the internal variable; does not update the display.
		"""

	def SetSashPosition(self, position: int, redraw: bool = True) -> None:
		""" Sets the sash position.

			Note Does not currently check for an out-of-range value.
		"""

	def SetSplitMode(self, mode: int) -> None:
		""" Sets the split mode.
			Can be wx.SPLIT_VERTICAL or wx.SPLIT_HORIZONTAL.
		"""

	def SplitHorizontally(self, window1: Window, window2: Window, sashPosition: int = 0) -> bool:
		""" Initializes the top and bottom panes of the splitter window.

			The child windows are shown if they are currently hidden.

			Returns True if successful, False otherwise (the window was already split).

			Note This should be called if you wish to initially view two panes. It can also be called at any subsequent time, but the application should check that the window is not currently split using IsSplit .
		"""

	def SplitVertically(self, window1: Window, window2: Window, sashPosition: int = 0) -> bool:
		""" Initializes the left and right panes of the splitter window.

			The child windows are shown if they are currently hidden.

			Returns: True if successful, False otherwise (the window was already split).

			Note This should be called if you wish to initially view two panes. It can also be called at any subsequent time, but the application should check that the window is not currently split using IsSplit .
		"""

	def Unsplit(self, toRemove: Optional[Window] = None) -> bool:
		""" Unsplits the window.

			Returns: True if successful, False otherwise (the window was not split).
		"""


class SizeEvent(Event):
	""" Interface voor wx.SizeEvent
	"""

	def GetSize(self) -> Size:
		""" Returns the entire size of the window generating the size change event.

			This is the new total size of the window, i.e. the same size as would be returned by wx.Window.GetSize if it were called now. Use wx.Window.GetClientSize if you catch this event in a top level window such as wx.Frame to find the size available for the window contents.
		"""


class PyUserData:
	""" Interface voor wx.PyUserData
	"""


class BitmapBundle:
	""" Interface voor wx.BitmapBundle
	"""


class VisualAttributes:
	""" Interface voor wx.VisualAttributes
	"""


class ToolBarToolBase:
	""" Interface voor wx.ToolBarToolBase
	"""

	def __init__(self, tbar: Optional['ToolBar'] = None, toolid: int = -1, label: str = "", bmpNormal: Optional[Bitmap] = None, bmpDisabled: Optional[Bitmap] = None, kind: int = -1, clientData: Optional['PyUserData'] = None, shortHelpString: str = "", longHelpString: str = "") -> None:
		""" Constructor
		"""

	def Attach(self, tbar: 'ToolBar') -> None:
		""" """

	def CanBeToggled(self) -> bool:
		""" """

	def Detach(self) -> None:
		""" """

	def Enable(self, enable: bool) -> bool:
		""" """

	def GetBitmap(self) -> Bitmap:
		""" """

	def GetClientData(self) -> 'PyUserData':
		""" """

	def GetControl(self) -> Control:
		""" """

	def GetDisabledBitmap(self) -> Bitmap:
		""" """

	def GetDisabledBitmapBundle(self) -> 'BitmapBundle':
		""" Return the bundle containing disabled tool bitmaps.

			This bundle may be invalid if the tool doesn't show a bitmap or doesn't have a specific disabled bitmap creates one automatically from the normal bitmap.
		"""

	def GetDropdownMenu(self) -> Menu:
		""" """

	def GetId(self) -> int:
		""" """

	def GetKind(self) -> int:
		""" """

	def GetLabel(self) -> str:
		""" """

	def GetLongHelp(self) -> str:
		""" """

	def GetNormalBitmap(self) -> Bitmap:
		""" """

	def GetNormalBitmapBundle(self) -> 'BitmapBundle':
		""" Return the bundle containing normal tool bitmaps.

			This bundle may be invalid if the tool doesn't show a bitmap.
		"""

	def GetShortHelp(self) -> str:
		""" """

	def GetStyle(self) -> int:
		""" """

	def GetToolBar(self) -> 'ToolBar':
		""" Return the toolbar this tool is a member of.
		"""

	def IsButton(self) -> bool:
		""" """

	def IsControl(self) -> bool:
		""" """

	def IsEnabled(self) -> bool:
		""" """

	def IsSeparator(self) -> bool:
		""" """

	def IsStretchable(self) -> bool:
		""" """

	def IsStretchableSpace(self) -> bool:
		""" """

	def IsToggled(self) -> bool:
		""" """

	def MakeStretchable(self) -> None:
		""" """

	def SetClientData(self, clientData: 'PyUserData') -> None:
		""" """

	def SetDisabledBitmap(self, bmp: Bitmap) -> None:
		""" """

	def SetDropdownMenu(self, menu: Menu) -> None:
		""" """

	def SetLabel(self, label: str) -> None:
		""" """

	def SetLongHelp(self, help: str) -> bool:
		""" """

	def SetNormalBitmap(self, bmp: Bitmap) -> None:
		""" """

	def SetShortHelp(self, help: str) -> bool:
		""" """

	def SetToggle(self, toggle: bool) -> bool:
		""" """

	def Toggle(self, toggle: bool = False) -> bool:
		""" """


class ToolBar(Control):
	""" Interface voor wx.ToolBar
	"""

	def __init__(self, parent: Window, id: int = -1, pos: Optional[Union[tuple[int, int], Position]] = None, size: Optional[Union[tuple[int, int], Size]] = None, style: int = -1, name: str = "") -> None:
		""" Constructs a toolbar.

			Note After a toolbar is created, you use AddTool and perhaps AddSeparator , and then you must call Realize to construct and display the toolbar tools.
		"""

	def AddCheckTool(self, toolId: int, label: str, bitmap1: Bitmap, bmpDisabled: Optional[Bitmap] = None, shortHelp: str = "", longHelp: str = "", clientData: Optional[Any] = None) -> ToolBarToolBase:
		""" Adds a new check (or toggle) tool to the toolbar.
		"""

	def AddControl(self, control: Control, label: str = "") -> ToolBarToolBase:
		""" Adds any control to the toolbar, typically e.g. a wx.ComboBox.

			Note Mac: labels are only displayed if wxWidgets is built with MAC_USE_NATIVE_TOOLBAR set to 1
		"""

	def AddLabelTool(self, id: int, label: str, bitmap: Bitmap, bmpDisabled: Optional[Bitmap] = None, kind: int = -1, shortHelp: str = "", longHelp: str = "", clientData: Optional['PyUserData'] = None) -> ToolBarToolBase:
		""" Old style method to add a tool in the toolbar.
		"""

	def AddRadioTool(self, toolId: int, label: str, bitmap1: Bitmap, bmpDisabled: Optional[Bitmap] = None, shortHelp: str = "", longHelp: str = "", clientData: Optional['PyUserData'] = None) -> ToolBarToolBase:
		""" Adds a new radio tool to the toolbar.

			Consecutive radio tools form a radio group such that exactly one button in the group is pressed at any moment, in other words whenever a button in the group is pressed the previously pressed button is automatically released. You should avoid having the radio groups of only one element as it would be impossible for the user to use such button.

			By default, the first button in the radio group is initially pressed, the others are not.
		"""

	def AddSeparator(self) -> ToolBarToolBase:
		""" Adds a separator for spacing groups of tools.

			Notice that the separator uses the look appropriate for the current platform so it can be a vertical line (MSW, some versions of GTK) or just an empty space or something else.
		"""

	def AddSimpleTool(self, toolId: int, bitmap: Bitmap, shortHelpString: str = "", longHelpString: str = "", isToggle: int = 0) -> ToolBarToolBase:
		""" Old style method to add a tool to the toolbar.
		"""

	def AddStretchableSpace(self) -> ToolBarToolBase:
		""" Adds a stretchable space to the toolbar.

			Any space not taken up by the fixed items (all items except for stretchable spaces) is distributed in equal measure between the stretchable spaces in the toolbar. The most common use for this method is to add a single stretchable space before the items which should be right-aligned in the toolbar, but more exotic possibilities are possible, e.g. a stretchable space may be added in the beginning and the end of the toolbar to centre all toolbar items.
		"""

	def AddTool(self, tool: Optional[ToolBarToolBase] = None, toolId: Optional[int] = -1, label: Optional[str] = "", bitmap: Optional[Bitmap] = None, bmpDisabled: Optional[Bitmap] = None, kind: int = -1, shortHelp: str = "", longHelp: str = "", clientData: Optional['PyUserData'] = None) -> ToolBarToolBase:
		""" Adds a tool to the toolbar.

			Note After you have added tools to a toolbar, you must call Realize in order to have the tools appear.
		"""

	def ClearTools(self) -> None:
		""" Deletes all the tools in the toolbar.
		"""

	def CreateSeparator(self) -> ToolBarToolBase:
		""" Factory function to create a new separator toolbar tool.
		"""

	def CreateTool(self, control: Optional[Control] = None, toolId: Optional[int] = None, label: str = "", bmpNormal: Optional[Bitmap] = None, bmpDisabled: Optional[Bitmap] = None, kind: int = -1, clientData: Optional['PyUserData'] = None, shortHelp: str = "", longHelp: str = "") -> ToolBarToolBase:
		""" Factory function to create a new toolbar tool.
		"""

	def DeleteTool(self, toolId: int) -> bool:
		""" Removes the specified tool from the toolbar and deletes it.

			If you don't want to delete the tool, but just to remove it from the toolbar (to possibly add it back later), you may use RemoveTool instead.

			Note It is unnecessary to call Realize for the change to take place, it will happen immediately.
		"""

	def DeleteToolByPos(self, pos: int) -> bool:
		""" This function behaves like DeleteTool but it deletes the tool at the specified position and not the one with the given id.
		"""

	def EnableTool(self, toolId: int, enable: bool) -> bool:
		""" Enables or disables the tool.

			Note Some implementations will change the visible state of the tool to indicate that it is disabled.
		"""

	def FindById(self, id: int) -> Optional[ToolBarToolBase]:
		""" Returns a pointer to the tool identified by id or None if no corresponding tool is found.
		"""

	def FindControl(self, id: int) -> Optional[ToolBarToolBase]:
		""" Returns a pointer to the control identified by id or None if no corresponding control is found.
		"""

	def FindToolForPosition(self, x: int, y: int) -> Optional[ToolBarToolBase]:
		""" Finds a tool for the given mouse position.

			Note Currently not implemented in wxGTK (always returns None there).
		"""

	@staticmethod
	def GetClassDefaultAttributes(variant: int = -1) -> 'VisualAttributes':
		""" """

	def GetMargins(self) -> Size:
		""" Returns the left/right and top/bottom margins, which are also used for inter-toolspacing.
		"""

	def GetToolBitmapSize(self) -> Size:
		""" Returns the size of bitmap that the toolbar expects to have.

			The default bitmap size is platform-dependent: for example, it is 16x15 for MSW and 24x24 for GTK. This size does not necessarily indicate the best size to use for the toolbars on the given platform, for this you should use ArtProvider::GetNativeSizeHint(wxART_TOOLBAR) but in any case, as the bitmap size is deduced automatically from the size of the bitmaps associated with the tools added to the toolbar, it is usually unnecessary to call neither this function nor SetToolBitmapSize at all.

			Note Note that this is the size of the bitmap you pass to AddTool , and not the eventual size of the tool button.
		"""

	def GetToolByPos(self, pos: Union[Position, tuple[int, int]]) -> Optional[ToolBarToolBase]:
		""" Returns a pointer to the tool at ordinal position pos.

			Dont confuse this with FindToolForPosition .
		"""

	def GetToolClientData(self, toolId: int) -> Optional['PyUserData']:
		""" Get any client data associated with the tool.
		"""

	def GetToolEnabled(self, toolId: int) -> bool:
		""" Called to determine whether a tool is enabled (responds to user input).
		"""

	def GetToolLongHelp(self, toolId: int) -> str:
		""" Returns the long help for the given tool.
		"""

	def GetToolPacking(self) -> int:
		""" Returns the value used for packing tools.
		"""

	def GetToolPos(self, toolId: int) -> int:
		""" Returns the tool position in the toolbar, or NOT_FOUND if the tool is not found.
		"""

	def GetToolSeparation(self) -> int:
		""" Returns the default separator size.
		"""

	def GetToolShortHelp(self, toolId: int) -> str:
		""" Returns the short help for the given tool.
		"""

	def GetToolSize(self) -> Size:
		""" Returns the size of a whole button, which is usually larger than a tool bitmap because of added 3D effects.
		"""

	def GetToolState(self, toolId: int) -> bool:
		""" Gets the on/off state of a toggle tool.
		"""

	def GetToolsCount(self) -> int:
		""" Returns the number of tools in the toolbar.
		"""

	def InsertControl(self, pos: int, control: Control, label: str = "") -> ToolBarToolBase:
		""" Inserts the control into the toolbar at the given position.

			You must call Realize for the change to take place.
		"""

	def InsertLabelTool(self, pos: int, id: int, label: str, bitmap: Bitmap, bmpDisabled: Optional[Bitmap] = None, kind: int = -1, shortHelp: str = "", longHelp: str = "", clientData: Optional['PyUserData'] = None) -> ToolBarToolBase:
		""" Old style method to insert a tool in the toolbar.
		"""

	def InsertSeparator(self, pos: int) -> ToolBarToolBase:
		""" Inserts the separator into the toolbar at the given position.

			You must call Realize for the change to take place.
		"""

	def InsertSimpleTool(self, pos: int, toolId: int, bitmap: Bitmap, shortHelpString: str = "", longHelpString: str = "", isToggle: int = 0) -> ToolBarToolBase:
		""" Old style method to insert a tool in the toolbar.
		"""

	def InsertStretchableSpace(self, pos: int) -> ToolBarToolBase:
		""" Inserts a stretchable space at the given position.
		"""

	def InsertTool(self, pos: int, tool: Optional[ToolBarToolBase] = None, toolId: Optional[int] = None, label: Optional[str] = "", bitmap: Optional[Bitmap] = None, bmpDisabled: Optional[Bitmap] = None, kind: int = -1, shortHelp: str = "", longHelp: str = "", clientData: Optional['PyUserData'] = None) -> Optional[ToolBarToolBase]:
		""" Inserts the tool with the specified attributes into the toolbar at the given position.

			You must call Realize for the change to take place.
		"""

	def Realize(self) -> bool:
		""" This function should be called after you have added tools.
		"""

	def RemoveTool(self, id: int) -> ToolBarToolBase:
		""" Removes the given tool from the toolbar but doesn't delete it.

			This allows inserting/adding this tool back to this (or another) toolbar later.

			Note It is unnecessary to call Realize for the change to take place, it will happen immediately.
		"""

	def SetDropdownMenu(self, id: int, menu: Menu) -> bool:
		""" Sets the dropdown menu for the tool given by its id.

			The tool itself will delete the menu when it's no longer needed. Only supported under GTK+ und MSW.

			If you define a EVT_TOOL_DROPDOWN() handler in your program, you must call wx.Event.Skip from it or the menu won't be displayed.
		"""

	def SetMargins(self, x: int = 0, y: int = 0, size: Optional[Union[tuple[int, int], Size]] = None) -> bool:
		""" Set the values to be used as margins for the toolbar.

			Note This must be called before the tools are added if absolute positioning is to be used, and the default (zero-size) margins are to be overridden.
		"""

	def SetToolBitmapSize(self, size: Union[tuple[int, int], Size]) -> None:
		""" Sets the default size of each tool bitmap.

			It is usually unnecessary to call this function, as the tools will always be made big enough to fit the size of the bitmaps used in them. Moreover, calling it forces wx.ToolBar to scale its images in high DPI using the provided size, instead of letting wx.BitmapBundle used for the tool bitmaps determine the best suitable bitmap size, which may result in suboptimal appearance.

			If you do call it, it must be done before toolbar is Realized.
		"""

	def SetToolClientData(self, id: int, clientData: 'PyUserData') -> None:
		""" Sets the client data associated with the tool.
		"""

	def SetToolDisabledBitmap(self, id: int, bitmap: Bitmap) -> None:
		""" Sets the bitmap to be used by the tool with the given ID when the tool is in a disabled state.

			This can only be used on Button tools, not controls.

			Note The native toolbar classes on the main platforms all synthesize the disabled bitmap from the normal bitmap, so this function will have no effect on those platforms.
		"""

	def SetToolLongHelp(self, toolId: int, helpString: str) -> None:
		""" Sets the long help for the given tool.

			Note You might use the long help for displaying the tool purpose on the status line.
		"""

	def SetToolNormalBitmap(self, id: int, bitmap: Bitmap) -> None:
		""" Sets the bitmap to be used by the tool with the given ID.

			This can only be used on Button tools, not controls.
		"""

	def SetToolPacking(self, packing: int = 1) -> None:
		""" Sets the value used for spacing tools.

			Note The packing is used for spacing in the vertical direction if the toolbar is horizontal, and for spacing in the horizontal direction if the toolbar is vertical.
		"""

	def SetToolSeparation(self, separation: int = 5) -> None:
		""" Sets the default separator size.
		"""

	def SetToolShortHelp(self, toolId: int, helpString: str) -> None:
		""" Sets the short help for the given tool.

			Note An application might use short help for identifying the tool purpose in a tooltip.
		"""

	def ToggleTool(self, toolId: int, toggle: bool) -> None:
		""" Toggles a tool on or off.

			This does not cause any event to get emitted.
		"""


def GetApp() -> App:
	""" Retrieve the WX App
	"""
	...


def PostEvent(window: EvtHandler, event: Event) -> None:
	""" Send an Event
	"""
	...


def Yield() -> None:
	""" Process pending events
	"""


def SafeYield() -> None:
	""" Process pending events
	"""
