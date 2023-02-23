# -*- coding: utf-8 -*-
from typing import Optional, Any


class Grid('olled< wxWindow >'):
	""" Grid and its related classes are used for displaying and editing
tabular data.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def AppendCols(self, numCols=1, updateLabels=True) -> bool:
		""" Appends one or more new columns to the right of the grid.
		"""

	def AppendRows(self, numRows=1, updateLabels=True) -> bool:
		""" Appends one or more new rows to the bottom of the grid.
		"""

	def AreHorzGridLinesClipped(self) -> bool:
		""" Return True if the horizontal grid lines stop at the last column boundary or False if they continue to the end of the window.
		"""

	def AreVertGridLinesClipped(self) -> bool:
		""" Return True if the vertical grid lines stop at the last row boundary or False if they continue to the end of the window.
		"""

	def AssignTable(self, table, selmode=GridSelectCells) -> None:
		""" Assigns a pointer to a custom grid table to be used by the grid.
		"""

	def AutoSize(self) -> None:
		""" Automatically sets the height and width of all rows and columns to fit their contents.
		"""

	def AutoSizeColLabelSize(self, col: int) -> None:
		""" Automatically adjusts width of the column to fit its label.
		"""

	def AutoSizeColumn(self, col, setAsMin=True) -> None:
		""" Automatically sizes the column to fit its contents.
		"""

	def AutoSizeColumns(self, setAsMin: bool=True) -> None:
		""" Automatically sizes all columns to fit their contents.
		"""

	def AutoSizeRow(self, row, setAsMin=True) -> None:
		""" Automatically sizes the row to fit its contents.
		"""

	def AutoSizeRowLabelSize(self, col: int) -> None:
		""" Automatically adjusts height of the row to fit its label.
		"""

	def AutoSizeRows(self, setAsMin: bool=True) -> None:
		""" Automatically sizes all rows to fit their contents.
		"""

	def BeginBatch(self) -> None:
		""" Increments the gridâs batch count.
		"""

	def BlockToDeviceRect(self, topLeft, bottomRight, gridWindow=None) -> Rect:
		""" Convert grid cell coordinates to grid window pixel coordinates.
		"""

	def CalcCellsExposed(self, reg, gridWindow=None) -> GridCellCoordsArray:
		""" Appends one or more new columns to the right of the grid.
		"""

	def CalcColLabelsExposed(self, reg, gridWindow=None) -> Any:
		""" Appends one or more new columns to the right of the grid.
		"""

	def CalcGridWindowScrolledPosition(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def CalcGridWindowUnscrolledPosition(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def CalcRowLabelsExposed(self, reg, gridWindow=None) -> Any:
		""" Appends one or more new columns to the right of the grid.
		"""

	def CanDragCell(self) -> bool:
		""" Return True if the dragging of cells is enabled or False otherwise.
		"""

	def CanDragColMove(self) -> bool:
		""" Returns True if columns can be moved by dragging with the mouse.
		"""

	def CanDragColSize(self, col: int) -> bool:
		""" Returns True if the given column can be resized by dragging with the mouse.
		"""

	def CanDragGridColEdges(self) -> bool:
		""" Return True if column edges inside the grid can be dragged to resize the rows.
		"""

	def CanDragGridRowEdges(self) -> bool:
		""" Return True if row edges inside the grid can be dragged to resize the rows.
		"""

	def CanDragGridSize(self) -> bool:
		""" Return True if the dragging of grid lines to resize rows and columns is enabled or False otherwise.
		"""

	def CanDragRowMove(self) -> bool:
		""" Returns True if rows can be moved by dragging with the mouse.
		"""

	def CanDragRowSize(self, row: int) -> bool:
		""" Returns True if the given row can be resized by dragging with the mouse.
		"""

	def CanEnableCellControl(self) -> bool:
		""" Returns True if the in-place edit control for the current grid cell can be used and False otherwise.
		"""

	def CanHaveAttributes(self) -> bool:
		""" Returns True if this grid has support for cell attributes.
		"""

	def CanHideColumns(self) -> bool:
		""" Returns True if columns can be hidden from the popup menu of the native header.
		"""

	def CellToGridWindow(self, *args, **kw) -> 'grid.GridWindow':
		""" Overloaded Implementations:
		"""

	def CellToRect(self, *args, **kw) -> Rect:
		""" Return the rectangle corresponding to the grid cellâs size and position in logical coordinates.
		"""

	def ClearGrid(self) -> None:
		""" Clears all data in the underlying grid table and repaints the grid.
		"""

	def ClearSelection(self) -> None:
		""" Deselects all cells that are currently selected.
		"""

	def ClipHorzGridLines(self, clip: bool) -> None:
		""" Change whether the horizontal grid lines are clipped by the end of the last column.
		"""

	def ClipVertGridLines(self, clip: bool) -> None:
		""" Change whether the vertical grid lines are clipped by the end of the last row.
		"""

	def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=WANTS_CHARS, name=GridNameStr) -> bool:
		""" Creates the grid window for an object initialized using the default constructor.
		"""

	def CreateGrid(self, numRows, numCols, selmode=GridSelectCells) -> bool:
		""" Creates a grid with the specified initial number of rows and columns.
		"""

	def DeleteCols(self, pos=0, numCols=1, updateLabels=True) -> bool:
		""" Deletes one or more columns from a grid starting at the specified position.
		"""

	def DeleteRows(self, pos=0, numRows=1, updateLabels=True) -> bool:
		""" Deletes one or more rows from a grid starting at the specified position.
		"""

	def DeselectCell(self, row, col) -> None:
		""" Deselects a cell.
		"""

	def DeselectCol(self, col: int) -> None:
		""" Deselects a column of cells.
		"""

	def DeselectRow(self, row: int) -> None:
		""" Deselects a row of cells.
		"""

	def DevicePosToGridWindow(self, *args, **kw) -> 'grid.GridWindow':
		""" Overloaded Implementations:
		"""

	def DisableCellEditControl(self) -> None:
		""" Disables in-place editing of grid cells.
		"""

	def DisableColResize(self, col: int) -> None:
		""" Disable interactive resizing of the specified column.
		"""

	def DisableDragColMove(self) -> None:
		""" Disables column moving by dragging with the mouse.
		"""

	def DisableDragColSize(self) -> None:
		""" Disables column sizing by dragging with the mouse.
		"""

	def DisableDragGridSize(self) -> None:
		""" Disable mouse dragging of grid lines to resize rows and columns.
		"""

	def DisableDragRowMove(self) -> None:
		""" Disables row moving by dragging with the mouse.
		"""

	def DisableDragRowSize(self) -> None:
		""" Disables row sizing by dragging with the mouse.
		"""

	def DisableHidingColumns(self) -> None:
		""" Disables column hiding from the header popup menu.
		"""

	def DisableRowResize(self, row: int) -> None:
		""" Disable interactive resizing of the specified row.
		"""

	def DrawCellHighlight(self, dc, attr) -> None:
		""" dc (wx.DC) â
		"""

	def DrawColLabel(self, dc, col) -> None:
		""" dc (wx.DC) â
		"""

	def DrawColLabels(self, dc, cols) -> None:
		""" dc (wx.DC) â
		"""

	def DrawCornerLabel(self, dc: 'DC') -> None:
		""" dc (wx.DC) â
		"""

	def DrawRowLabel(self, dc, row) -> None:
		""" dc (wx.DC) â
		"""

	def DrawRowLabels(self, dc, rows) -> None:
		""" dc (wx.DC) â
		"""

	def DrawTextRectangle(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def EnableCellEditControl(self, enable: bool=True) -> None:
		""" Enables or disables in-place editing of grid cell data.
		"""

	def EnableDragCell(self, enable: bool=True) -> None:
		""" Enables or disables cell dragging with the mouse.
		"""

	def EnableDragColMove(self, enable: bool=True) -> bool:
		""" Enables or disables column moving by dragging with the mouse.
		"""

	def EnableDragColSize(self, enable: bool=True) -> None:
		""" Enables or disables column sizing by dragging with the mouse.
		"""

	def EnableDragGridSize(self, enable: bool=True) -> None:
		""" Enables or disables row and column resizing by dragging gridlines with the mouse.
		"""

	def EnableDragRowMove(self, enable: bool=True) -> bool:
		""" Enables or disables row moving by dragging with the mouse.
		"""

	def EnableDragRowSize(self, enable: bool=True) -> None:
		""" Enables or disables row sizing by dragging with the mouse.
		"""

	def EnableEditing(self, edit: bool) -> None:
		""" Makes the grid globally editable or read-only.
		"""

	def EnableGridLines(self, enable: bool=True) -> None:
		""" Turns the drawing of grid lines on or off.
		"""

	def EnableHidingColumns(self, enable: bool=True) -> bool:
		""" Enables or disables column hiding from the header popup menu.
		"""

	def EndBatch(self) -> None:
		""" Decrements the gridâs batch count.
		"""

	def Fit(self) -> None:
		""" Overridden   wx.Window  method.
		"""

	def ForceRefresh(self) -> None:
		""" Causes immediate repainting of the grid.
		"""

	def FreezeTo(self, *args, **kw) -> bool:
		""" Overloaded Implementations:
		"""

	def GetBatchCount(self) -> int:
		""" Returns the number of times that BeginBatch   has been called without (yet) matching calls to EndBatch .
		"""

	def GetCellAlignment(self, row, col) -> tuple:
		""" Sets the arguments to the horizontal and vertical text alignment values for the grid cell at the specified location.
		"""

	def GetCellBackgroundColour(self, row, col) -> Colour:
		""" Returns the background colour of the cell at the specified location.
		"""

	def GetCellEditor(self, row, col) -> 'grid.GridCellEditor':
		""" Returns a pointer to the editor for the cell at the specified location.
		"""

	def GetCellFitMode(self, row, col) -> 'grid.GridFitMode':
		""" Returns the cell fitting mode.
		"""

	def GetCellFont(self, row, col) -> Font:
		""" Returns the font for text in the grid cell at the specified location.
		"""

	def GetCellHighlightColour(self) -> Colour:
		""" Colour
		"""

	def GetCellHighlightPenWidth(self) -> int:
		""" int
		"""

	def GetCellHighlightROPenWidth(self) -> int:
		""" int
		"""

	def GetCellOverflow(self, row, col) -> bool:
		""" Returns True if the cell value can overflow.
		"""

	def GetCellRenderer(self, row, col) -> 'grid.GridCellRenderer':
		""" Returns a pointer to the renderer for the grid cell at the specified location.
		"""

	def GetCellSize(self, *args, **kw) -> 'grid.Grid.CellSpan':
		""" Overloaded Implementations:
		"""

	def GetCellTextColour(self, row, col) -> Colour:
		""" Returns the text colour for the grid cell at the specified location.
		"""

	def GetCellValue(self, *args, **kw) -> str:
		""" Returns the string contained in the cell at the specified location.
		"""

	@staticmethod
	def GetClassDefaultAttributes(variant: WindowVariant=WINDOW_VARIANT_NORMAL) -> VisualAttributes:
		""" variant (WindowVariant) â
		"""

	def GetColAt(self, colPos: int) -> int:
		""" Returns the column ID of the specified column position.
		"""

	def GetColGridLinePen(self, col: int) -> Pen:
		""" Returns the pen used for vertical grid lines.
		"""

	def GetColLabelAlignment(self) -> tuple:
		""" Sets the arguments to the current column label alignment values.
		"""

	def GetColLabelSize(self) -> int:
		""" Returns the current height of the column labels.
		"""

	def GetColLabelTextOrientation(self) -> int:
		""" Returns the orientation of the column labels (either  HORIZONTAL   or   VERTICAL ).
		"""

	def GetColLabelValue(self, col: int) -> str:
		""" Returns the specified column label.
		"""

	def GetColLeft(self, col: int) -> int:
		""" Returns the coordinate of the left border specified column.
		"""

	def GetColMinimalAcceptableWidth(self) -> int:
		""" Returns the minimal width to which a column may be resized.
		"""

	def GetColMinimalWidth(self, col: int) -> int:
		""" Get the minimal width of the given column/row.
		"""

	def GetColPos(self, colID: int) -> int:
		""" Returns the position of the specified column.
		"""

	def GetColRight(self, col: int) -> int:
		""" Returns the coordinate of the right border specified column.
		"""

	def GetColSize(self, col: int) -> int:
		""" Returns the width of the specified column.
		"""

	def GetColSizes(self) -> 'grid.GridSizesInfo':
		""" Get size information for all columns at once.
		"""

	def GetCornerLabelAlignment(self, horiz, vert) -> None:
		""" Sets the arguments to the current corner label alignment values.
		"""

	def GetCornerLabelTextOrientation(self) -> int:
		""" Returns the orientation of the corner label (either  HORIZONTAL   or   VERTICAL ).
		"""

	def GetCornerLabelValue(self) -> str:
		""" Returns the (top-left) corner label.
		"""

	def GetDefaultCellAlignment(self) -> tuple:
		""" Returns the default cell alignment.
		"""

	def GetDefaultCellBackgroundColour(self) -> Colour:
		""" Returns the current default background colour for grid cells.
		"""

	def GetDefaultCellFitMode(self) -> 'grid.GridFitMode':
		""" Returns the default cell fitting mode.
		"""

	def GetDefaultCellFont(self) -> Font:
		""" Returns the current default font for grid cell text.
		"""

	def GetDefaultCellOverflow(self) -> bool:
		""" Returns True if the cells can overflow by default.
		"""

	def GetDefaultCellTextColour(self) -> Colour:
		""" Returns the current default colour for grid cell text.
		"""

	def GetDefaultColLabelSize(self) -> int:
		""" Returns the default height for column labels.
		"""

	def GetDefaultColSize(self) -> int:
		""" Returns the current default width for grid columns.
		"""

	def GetDefaultEditor(self) -> 'grid.GridCellEditor':
		""" Returns a pointer to the current default grid cell editor.
		"""

	def GetDefaultEditorForCell(self, *args, **kw) -> 'grid.GridCellEditor':
		""" Returns the default editor for the specified cell.
		"""

	def GetDefaultEditorForType(self, typeName: str) -> 'grid.GridCellEditor':
		""" Returns the default editor for the cells containing values of the given type.
		"""

	def GetDefaultGridLinePen(self) -> Pen:
		""" Returns the pen used for grid lines.
		"""

	def GetDefaultRenderer(self) -> 'grid.GridCellRenderer':
		""" Returns a pointer to the current default grid cell renderer.
		"""

	def GetDefaultRendererForCell(self, row, col) -> 'grid.GridCellRenderer':
		""" Returns the default renderer for the given cell.
		"""

	def GetDefaultRendererForType(self, typeName: str) -> 'grid.GridCellRenderer':
		""" Returns the default renderer for the cell containing values of the given type.
		"""

	def GetDefaultRowLabelSize(self) -> int:
		""" Returns the default width for the row labels.
		"""

	def GetDefaultRowSize(self) -> int:
		""" Returns the current default height for grid rows.
		"""

	def GetFirstFullyVisibleColumn(self) -> int:
		""" Returns the leftmost column of the current visible area.
		"""

	def GetFirstFullyVisibleRow(self) -> int:
		""" Returns the topmost row of the current visible area.
		"""

	def GetFrozenColGridWindow(self) -> Window:
		""" Return the columns grid window containing column frozen cells.
		"""

	def GetFrozenCornerGridWindow(self) -> Window:
		""" Return the corner grid window containing frozen cells.
		"""

	def GetFrozenRowGridWindow(self) -> Window:
		""" Return the rows grid window containing row frozen cells.
		"""

	def GetGridColHeader(self) -> HeaderCtrl:
		""" Return the header control used for column labels display.
		"""

	def GetGridColLabelWindow(self) -> Window:
		""" Return the column labels window.
		"""

	def GetGridCornerLabelWindow(self) -> Window:
		""" Return the window in the top left grid corner.
		"""

	def GetGridCursorCol(self) -> int:
		""" Returns the current grid cell column position.
		"""

	def GetGridCursorCoords(self) -> 'grid.GridCellCoords':
		""" Returns the current grid cursor position.
		"""

	def GetGridCursorRow(self) -> int:
		""" Returns the current grid cell row position.
		"""

	def GetGridLineColour(self) -> Colour:
		""" Returns the colour used for grid lines.
		"""

	def GetGridRowLabelWindow(self) -> Window:
		""" Return the row labels window.
		"""

	def GetGridWindow(self) -> Window:
		""" Return the main grid window containing the grid cells.
		"""

	def GetGridWindowOffset(self, gridWindow: 'grid.GridWindow') -> Point:
		""" This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
		"""

	def GetLabelBackgroundColour(self) -> Colour:
		""" Returns the colour used for the background of row and column labels.
		"""

	def GetLabelFont(self) -> Font:
		""" Returns the font used for row and column labels.
		"""

	def GetLabelTextColour(self) -> Colour:
		""" Returns the colour used for row and column label text.
		"""

	def GetNumberCols(self) -> int:
		""" Returns the total number of grid columns.
		"""

	def GetNumberFrozenCols(self) -> int:
		""" Returns the number of frozen grid columns.
		"""

	def GetNumberFrozenRows(self) -> int:
		""" Returns the number of frozen grid rows.
		"""

	def GetNumberRows(self) -> int:
		""" Returns the total number of grid rows.
		"""

	def GetOrCreateCellAttr(self, row, col) -> 'grid.GridCellAttr':
		""" Returns the attribute for the given cell creating one if necessary.
		"""

	def GetOrCreateCellAttrPtr(self, row, col) -> 'grid.GridCellAttrPtr':
		""" Returns the attribute for the given cell creating one if necessary.
		"""

	def GetRowAt(self, rowPos: int) -> int:
		""" Returns the row ID of the specified row position.
		"""

	def GetRowGridLinePen(self, row: int) -> Pen:
		""" Returns the pen used for horizontal grid lines.
		"""

	def GetRowLabelAlignment(self) -> tuple:
		""" Returns the alignment used for row labels.
		"""

	def GetRowLabelSize(self) -> int:
		""" Returns the current width of the row labels.
		"""

	def GetRowLabelValue(self, row: int) -> str:
		""" Returns the specified row label.
		"""

	def GetRowMinimalAcceptableHeight(self) -> int:
		""" Returns the minimal size to which rows can be resized.
		"""

	def GetRowMinimalHeight(self, col: int) -> int:
		""" Returns the minimal size for the given column.
		"""

	def GetRowPos(self, rowID: int) -> int:
		""" Returns the position of the specified row.
		"""

	def GetRowSize(self, row: int) -> int:
		""" Returns the height of the specified row.
		"""

	def GetRowSizes(self) -> 'grid.GridSizesInfo':
		""" Get size information for all row at once.
		"""

	def GetScrollLineX(self) -> int:
		""" Returns the number of pixels per horizontal scroll increment.
		"""

	def GetScrollLineY(self) -> int:
		""" Returns the number of pixels per vertical scroll increment.
		"""

	def GetSelectedBlocks(self) -> 'grid.GridBlocks':
		""" Returns a range of grid selection blocks.
		"""

	def GetSelectedCells(self) -> GridCellCoordsArray:
		""" Returns an array of individually selected cells.
		"""

	def GetSelectedColBlocks(self) -> PyObject:
		""" Returns an ordered range of non-overlapping selected columns.
		"""

	def GetSelectedCols(self) -> Any:
		""" Returns an array of selected columns.
		"""

	def GetSelectedRowBlocks(self) -> PyObject:
		""" Returns an ordered range of non-overlapping selected rows.
		"""

	def GetSelectedRows(self) -> Any:
		""" Returns an array of selected rows.
		"""

	def GetSelectionBackground(self) -> Colour:
		""" Returns the colour used for drawing the selection background.
		"""

	def GetSelectionBlockBottomRight(self) -> GridCellCoordsArray:
		""" Returns an array of the bottom right corners of blocks of selected cells.
		"""

	def GetSelectionBlockTopLeft(self) -> GridCellCoordsArray:
		""" Returns an array of the top left corners of blocks of selected cells.
		"""

	def GetSelectionForeground(self) -> Colour:
		""" Returns the colour used for drawing the selection foreground.
		"""

	def GetSelectionMode(self) -> 'grid.Grid.GridSelectionModes':
		""" Returns the current selection mode.
		"""

	def GetSortingColumn(self) -> int:
		""" Return the column in which the sorting indicator is currently displayed.
		"""

	def GetTable(self) -> 'grid.GridTableBase':
		""" Returns a base pointer to the current table object.
		"""

	def GoToCell(self, *args, **kw) -> None:
		""" Make the given cell current and ensure it is visible.
		"""

	def GridLinesEnabled(self) -> bool:
		""" Returns True if drawing of grid lines is turned on, False otherwise.
		"""

	def HideCellEditControl(self) -> None:
		""" Hides the in-place cell edit control.
		"""

	def HideCol(self, col: int) -> None:
		""" Hides the specified column.
		"""

	def HideColLabels(self) -> None:
		""" Hides the column labels by calling SetColLabelSize   with a size of 0.
		"""

	def HideRow(self, col: int) -> None:
		""" Hides the specified row.
		"""

	def HideRowLabels(self) -> None:
		""" Hides the row labels by calling SetRowLabelSize   with a size of 0.
		"""

	def InsertCols(self, pos=0, numCols=1, updateLabels=True) -> bool:
		""" Inserts one or more new columns into a grid with the first new column at the specified position.
		"""

	def InsertRows(self, pos=0, numRows=1, updateLabels=True) -> bool:
		""" Inserts one or more new rows into a grid with the first new row at the specified position.
		"""

	def IsCellEditControlEnabled(self) -> bool:
		""" Returns True if the in-place edit control is currently enabled.
		"""

	def IsCellEditControlShown(self) -> bool:
		""" Returns True if the in-place edit control is currently shown.
		"""

	def IsColShown(self, col: int) -> bool:
		""" Returns True if the specified column is not currently hidden.
		"""

	def IsCurrentCellReadOnly(self) -> bool:
		""" Returns True if the current cell is read-only.
		"""

	def IsEditable(self) -> bool:
		""" Returns False if the whole grid has been set as read-only or True otherwise.
		"""

	def IsInSelection(self, *args, **kw) -> bool:
		""" Returns True if the given cell is selected.
		"""

	def IsReadOnly(self, row, col) -> bool:
		""" Returns True if the cell at the specified location canât be edited.
		"""

	def IsRowShown(self, row: int) -> bool:
		""" Returns True if the specified row is not currently hidden.
		"""

	def IsSelection(self) -> bool:
		""" Returns True if there are currently any selected cells, rows, columns or blocks.
		"""

	def IsSortOrderAscending(self) -> bool:
		""" Return True if the current sorting order is ascending or False if it is descending.
		"""

	def IsSortingBy(self, col: int) -> bool:
		""" Return True if this column is currently used for sorting.
		"""

	def IsUsingNativeHeader(self) -> bool:
		""" Return True if native header control is currently being used.
		"""

	def IsVisible(self, *args, **kw) -> bool:
		""" Returns True if a cell is either entirely or at least partially visible in the grid window.
		"""

	def MakeCellVisible(self, *args, **kw) -> None:
		""" Brings the specified cell into the visible grid cell area with minimal scrolling.
		"""

	def MoveCursorDown(self, expandSelection: bool) -> bool:
		""" Moves the grid cursor down by one row.
		"""

	def MoveCursorDownBlock(self, expandSelection: bool) -> bool:
		""" Moves the grid cursor down in the current column such that it skips to the beginning or end of a block of non-empty cells.
		"""

	def MoveCursorLeft(self, expandSelection: bool) -> bool:
		""" Moves the grid cursor left by one column.
		"""

	def MoveCursorLeftBlock(self, expandSelection: bool) -> bool:
		""" Moves the grid cursor left in the current row such that it skips to the beginning or end of a block of non-empty cells.
		"""

	def MoveCursorRight(self, expandSelection: bool) -> bool:
		""" Moves the grid cursor right by one column.
		"""

	def MoveCursorRightBlock(self, expandSelection: bool) -> bool:
		""" Moves the grid cursor right in the current row such that it skips to the beginning or end of a block of non-empty cells.
		"""

	def MoveCursorUp(self, expandSelection: bool) -> bool:
		""" Moves the grid cursor up by one row.
		"""

	def MoveCursorUpBlock(self, expandSelection: bool) -> bool:
		""" Moves the grid cursor up in the current column such that it skips to the beginning or end of a block of non-empty cells.
		"""

	def MovePageDown(self) -> bool:
		""" Moves the grid cursor down by some number of rows so that the previous bottom visible row becomes the top visible row.
		"""

	def MovePageUp(self) -> bool:
		""" Moves the grid cursor up by some number of rows so that the previous top visible row becomes the bottom visible row.
		"""

	def ProcessTableMessage(self, msg: 'grid.GridTableMessage') -> bool:
		""" Receive and handle a message from the table.
		"""

	def RefreshAttr(self, row, col) -> None:
		""" Invalidates the cached attribute for the given cell.
		"""

	def RegisterDataType(self, typeName, renderer, editor) -> None:
		""" Register a new data type.
		"""



