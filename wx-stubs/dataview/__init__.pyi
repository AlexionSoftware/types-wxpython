# -*- coding: utf-8 -*-
from typing import Optional, Any


class DataViewCtrl('Control'):
	""" DataViewCtrl is a control to display data either in a tree like
fashion or in a tabular form or both.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def AllowMultiColumnSort(self, allow: bool) -> bool:
		""" Call to allow using multiple columns for sorting.
		"""

	def AppendBitmapColumn(self, *args, **kw) -> 'dataview.DataViewColumn':
		""" Appends a column for rendering a bitmap.
		"""

	def AppendColumn(self, col: 'dataview.DataViewColumn') -> bool:
		""" Appends a   wx.dataview.DataViewColumn  to the control.
		"""

	def AppendDateColumn(self, *args, **kw) -> 'dataview.DataViewColumn':
		""" Appends a column for rendering a date.
		"""

	def AppendIconTextColumn(self, *args, **kw) -> 'dataview.DataViewColumn':
		""" Appends a column for rendering text with an icon.
		"""

	def AppendProgressColumn(self, *args, **kw) -> 'dataview.DataViewColumn':
		""" Appends a column for rendering a progress indicator.
		"""

	def AppendTextColumn(self, *args, **kw) -> 'dataview.DataViewColumn':
		""" Appends a column for rendering text.
		"""

	def AppendToggleColumn(self, *args, **kw) -> 'dataview.DataViewColumn':
		""" Appends a column for rendering a toggle.
		"""

	def _AssociateModel(self, model: 'dataview.DataViewModel') -> bool:
		""" Associates a   wx.dataview.DataViewModel  with the control.
		"""

	def AssociateModel(self, model) -> None:
		""" Associates a DataViewModel with the control.
Ownership of the model object is passed to C++, however it
is reference counted so it can be shared with other views.
		"""

	def ClearColumns(self) -> bool:
		""" Removes all columns.
		"""

	def Collapse(self, item: 'dataview.DataViewItem') -> None:
		""" Collapses the item.
		"""

	def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=DataViewCtrlNameStr) -> bool:
		""" Create the control.
		"""

	def DeleteColumn(self, column: 'dataview.DataViewColumn') -> bool:
		""" Deletes given column.
		"""

	def EditItem(self, item, column) -> None:
		""" Programmatically starts editing given cell of item.
		"""

	def EnableDragSource(self, format: 'DataFormat') -> bool:
		""" Enable drag operations using the given format.
		"""

	def EnableDropTarget(self, format: 'DataFormat') -> bool:
		""" Enable drop operations using the given format.
		"""

	def EnableDropTargets(self, formats: Vector) -> bool:
		""" Enable drop operations using any of the specified formats.
		"""

	def EnableSystemTheme(self, enable: bool=True) -> None:
		""" Can be used to disable the system theme of controls using it by default.
		"""

	def EnsureVisible(self, item, column=None) -> None:
		""" Call this to ensure that the given item is visible.
		"""

	def Expand(self, item: 'dataview.DataViewItem') -> None:
		""" Expands the item.
		"""

	def ExpandAncestors(self, item: 'dataview.DataViewItem') -> None:
		""" Expands all ancestors of the item.
		"""

	def ExpandChildren(self, item: 'dataview.DataViewItem') -> None:
		""" Expand all children of the given item recursively.
		"""

	@staticmethod
	def GetClassDefaultAttributes(variant: WindowVariant=WINDOW_VARIANT_NORMAL) -> VisualAttributes:
		""" variant (WindowVariant) â
		"""

	def GetColumn(self, pos: int) -> 'dataview.DataViewColumn':
		""" Returns pointer to the column.
		"""

	def GetColumnCount(self) -> int:
		""" Returns the number of columns.
		"""

	def GetColumnPosition(self, column: 'dataview.DataViewColumn') -> int:
		""" Returns the position of the column or -1 if not found in the control.
		"""

	def GetColumns(self) -> None:
		""" Returns a list of column objects.
		"""

	def GetCountPerPage(self) -> int:
		""" Return the number of items that can fit vertically in the visible area of the control.
		"""

	def GetCurrentColumn(self) -> 'dataview.DataViewColumn':
		""" Returns the column that currently has focus.
		"""

	def GetCurrentItem(self) -> 'dataview.DataViewItem':
		""" Returns the currently focused item.
		"""

	def GetExpanderColumn(self) -> 'dataview.DataViewColumn':
		""" Returns column containing the expanders.
		"""

	def GetIndent(self) -> int:
		""" Returns indentation.
		"""

	def GetItemRect(self, item, col=None) -> Rect:
		""" Returns item rectangle.
		"""

	def GetMainWindow(self) -> Window:
		""" Returns the window corresponding to the main area of the control.
		"""

	def GetModel(self) -> 'dataview.DataViewModel':
		""" Returns pointer to the data model associated with the control (if any).
		"""

	def GetSelectedItemsCount(self) -> int:
		""" Returns the number of currently selected items.
		"""

	def GetSelection(self) -> 'dataview.DataViewItem':
		""" Returns first selected item or an invalid item if none is selected.
		"""

	def GetSelections(self) -> DataViewItemArray:
		""" Returns a list of the currently selected items.
		"""

	def GetSortingColumn(self) -> 'dataview.DataViewColumn':
		""" Returns the   wx.dataview.DataViewColumn  currently responsible for sorting or None if none has been selected.
		"""

	def GetTopItem(self) -> 'dataview.DataViewItem':
		""" Return the topmost visible item.
		"""

	def HasSelection(self) -> bool:
		""" Returns True if any items are currently selected.
		"""

	def HitTest(self, point) -> PyObject:
		""" HitTest(point) . (item, col)
		"""

	def InsertColumn(self, pos, col) -> bool:
		""" Inserts a   wx.dataview.DataViewColumn  to the control.
		"""

	def IsExpanded(self, item: 'dataview.DataViewItem') -> bool:
		""" Return True if the item is expanded.
		"""

	def IsMultiColumnSortAllowed(self) -> bool:
		""" Return True if using more than one column for sorting is allowed.
		"""

	def IsSelected(self, item: 'dataview.DataViewItem') -> bool:
		""" Return True if the item is selected.
		"""

	def PrependBitmapColumn(self, *args, **kw) -> 'dataview.DataViewColumn':
		""" Prepends a column for rendering a bitmap.
		"""

	def PrependColumn(self, col: 'dataview.DataViewColumn') -> bool:
		""" Prepends a   wx.dataview.DataViewColumn  to the control.
		"""

	def PrependDateColumn(self, *args, **kw) -> 'dataview.DataViewColumn':
		""" Prepends a column for rendering a date.
		"""

	def PrependIconTextColumn(self, *args, **kw) -> 'dataview.DataViewColumn':
		""" Prepends a column for rendering text with an icon.
		"""

	def PrependProgressColumn(self, *args, **kw) -> 'dataview.DataViewColumn':
		""" Prepends a column for rendering a progress indicator.
		"""

	def PrependTextColumn(self, *args, **kw) -> 'dataview.DataViewColumn':
		""" Prepends a column for rendering text.
		"""

	def PrependToggleColumn(self, *args, **kw) -> 'dataview.DataViewColumn':
		""" Prepends a column for rendering a toggle.
		"""

	def Select(self, item: 'dataview.DataViewItem') -> None:
		""" Select the given item.
		"""

	def SelectAll(self) -> None:
		""" Select all items.
		"""

	def SetAlternateRowColour(self, colour: 'Colour') -> bool:
		""" Set custom colour for the alternate rows used with wx.dataview.DV_ROW_LINES style.
		"""

	def SetCurrentItem(self, item: 'dataview.DataViewItem') -> None:
		""" Changes the currently focused item.
		"""

	def SetExpanderColumn(self, col: 'dataview.DataViewColumn') -> None:
		""" Set which column shall contain the tree-like expanders.
		"""

	def SetHeaderAttr(self, attr: 'ItemAttr') -> bool:
		""" Set custom colours and/or font to use for the header.
		"""

	def SetIndent(self, indent: int) -> None:
		""" Sets the indentation.
		"""

	def SetRowHeight(self, rowHeight: int) -> bool:
		""" Sets the row height.
		"""

	def SetSelections(self, sel: DataViewItemArray) -> None:
		""" Sets the selection to the array of DataViewItems.
		"""

	def ToggleSortByColumn(self, column: int) -> None:
		""" Toggle sorting by the given column.
		"""

	def Unselect(self, item: 'dataview.DataViewItem') -> None:
		""" Unselect the given item.
		"""

	def UnselectAll(self) -> None:
		""" Unselect all item.
		"""

dataview.DV_SINGLE: int  #  Single selection mode. This is the default.
dataview.DV_MULTIPLE: int  #  Multiple selection mode.
dataview.DV_ROW_LINES: int  #  Use alternating colours for odd and even rows.
dataview.DV_HORIZ_RULES: int  #  Display the separator lines between rows.
dataview.DV_VERT_RULES: int  #  Display the separator lines between columns.
dataview.DV_VARIABLE_LINE_HEIGHT: int  #  Allow variable line heights. This can be inefficient when displaying large number of items.
dataview.DV_NO_HEADER: int  #  Do not show column headers (which are shown by default). ^^
EVT_DATAVIEW_SELECTION_CHANGED: int  #  Process a  wxEVT_DATAVIEW_SELECTION_CHANGED   event.
EVT_DATAVIEW_ITEM_ACTIVATED: int  #  Process a  wxEVT_DATAVIEW_ITEM_ACTIVATED   event. This event is triggered by double clicking an item or pressing some special key (usually âEnterâ) when it is focused.
EVT_DATAVIEW_ITEM_START_EDITING: int  #  Process a  wxEVT_DATAVIEW_ITEM_START_EDITING   event. This event can be vetoed in order to prevent editing on an item by item basis.
EVT_DATAVIEW_ITEM_EDITING_STARTED: int  #  Process a  wxEVT_DATAVIEW_ITEM_EDITING_STARTED   event.
EVT_DATAVIEW_ITEM_EDITING_DONE: int  #  Process a  wxEVT_DATAVIEW_ITEM_EDITING_DONE   event.
EVT_DATAVIEW_ITEM_COLLAPSING: int  #  Process a  wxEVT_DATAVIEW_ITEM_COLLAPSING   event.
EVT_DATAVIEW_ITEM_COLLAPSED: int  #  Process a  wxEVT_DATAVIEW_ITEM_COLLAPSED   event.
EVT_DATAVIEW_ITEM_EXPANDING: int  #  Process a  wxEVT_DATAVIEW_ITEM_EXPANDING   event.
EVT_DATAVIEW_ITEM_EXPANDED: int  #  Process a  wxEVT_DATAVIEW_ITEM_EXPANDED   event.
EVT_DATAVIEW_ITEM_VALUE_CHANGED: int  #  Process a  wxEVT_DATAVIEW_ITEM_VALUE_CHANGED   event.
EVT_DATAVIEW_ITEM_CONTEXT_MENU: int  #  Process a  wxEVT_DATAVIEW_ITEM_CONTEXT_MENU   event generated when the user right clicks inside the control. Notice that this menu is generated even if the click didnât occur on any valid item, in this case  wx.dataview.DataViewEvent.GetItem   simply returns an invalid item.
EVT_DATAVIEW_COLUMN_HEADER_CLICK: int  #  Process a  wxEVT_DATAVIEW_COLUMN_HEADER_CLICK   event.
EVT_DATAVIEW_COLUMN_HEADER_RIGHT_CLICK: int  #  Process a  wxEVT_DATAVIEW_COLUMN_HEADER_RIGHT_CLICK   event. Notice that currently this event is not generated in the native macOS versions of the control.
EVT_DATAVIEW_COLUMN_SORTED: int  #  Process a  wxEVT_DATAVIEW_COLUMN_SORTED   event.
EVT_DATAVIEW_COLUMN_REORDERED: int  #  Process a  wxEVT_DATAVIEW_COLUMN_REORDERED   event.
EVT_DATAVIEW_ITEM_BEGIN_DRAG: int  #  Process a  wxEVT_DATAVIEW_ITEM_BEGIN_DRAG   event which is generated when the user starts dragging a valid item. This event must be processed and  wx.dataview.DataViewEvent.SetDataObject   must be called to actually start dragging the item.
EVT_DATAVIEW_ITEM_DROP_POSSIBLE: int  #  Process a  wxEVT_DATAVIEW_ITEM_DROP_POSSIBLE   event.
EVT_DATAVIEW_ITEM_DROP: int  #  Process a  wxEVT_DATAVIEW_ITEM_DROP   event. ^^


