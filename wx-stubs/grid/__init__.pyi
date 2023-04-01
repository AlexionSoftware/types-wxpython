# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class Grid(Scrolled):
    """ Grid and its related classes are used for displaying and editing
tabular data.

        Source: https://docs.wxpython.org/wx.grid.Grid.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AppendCols(self, numCols=1, updateLabels=True) -> bool:
        """ Appends one or more new columns to the right of the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AppendRows(self, numRows=1, updateLabels=True) -> bool:
        """ Appends one or more new rows to the bottom of the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AreHorzGridLinesClipped(self) -> bool:
        """ Return True if the horizontal grid lines stop at the last column boundary or False if they continue to the end of the window.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AreVertGridLinesClipped(self) -> bool:
        """ Return True if the vertical grid lines stop at the last row boundary or False if they continue to the end of the window.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AssignTable(self, table, selmode=GridSelectCells) -> None:
        """ Assigns a pointer to a custom grid table to be used by the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSize(self) -> None:
        """ Automatically sets the height and width of all rows and columns to fit their contents.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSizeColLabelSize(self, col: int) -> None:
        """ Automatically adjusts width of the column to fit its label.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSizeColumn(self, col, setAsMin=True) -> None:
        """ Automatically sizes the column to fit its contents.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSizeColumns(self, setAsMin: bool=True) -> None:
        """ Automatically sizes all columns to fit their contents.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSizeRow(self, row, setAsMin=True) -> None:
        """ Automatically sizes the row to fit its contents.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSizeRowLabelSize(self, col: int) -> None:
        """ Automatically adjusts height of the row to fit its label.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSizeRows(self, setAsMin: bool=True) -> None:
        """ Automatically sizes all rows to fit their contents.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def BeginBatch(self) -> None:
        """ Increments the gridâs batch count.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def BlockToDeviceRect(self, topLeft, bottomRight, gridWindow=None) -> 'Rect':
        """ Convert grid cell coordinates to grid window pixel coordinates.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CalcCellsExposed(self, reg, gridWindow=None) -> 'grid.GridCellCoordsArray':
        """ Appends one or more new columns to the right of the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CalcColLabelsExposed(self, reg, gridWindow=None) -> list[int]:
        """ Appends one or more new columns to the right of the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CalcGridWindowScrolledPosition(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CalcGridWindowUnscrolledPosition(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CalcRowLabelsExposed(self, reg, gridWindow=None) -> list[int]:
        """ Appends one or more new columns to the right of the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragCell(self) -> bool:
        """ Return True if the dragging of cells is enabled or False otherwise.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragColMove(self) -> bool:
        """ Returns True if columns can be moved by dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragColSize(self, col: int) -> bool:
        """ Returns True if the given column can be resized by dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragGridColEdges(self) -> bool:
        """ Return True if column edges inside the grid can be dragged to resize the rows.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragGridRowEdges(self) -> bool:
        """ Return True if row edges inside the grid can be dragged to resize the rows.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragGridSize(self) -> bool:
        """ Return True if the dragging of grid lines to resize rows and columns is enabled or False otherwise.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragRowMove(self) -> bool:
        """ Returns True if rows can be moved by dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragRowSize(self, row: int) -> bool:
        """ Returns True if the given row can be resized by dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanEnableCellControl(self) -> bool:
        """ Returns True if the in-place edit control for the current grid cell can be used and False otherwise.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanHaveAttributes(self) -> bool:
        """ Returns True if this grid has support for cell attributes.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanHideColumns(self) -> bool:
        """ Returns True if columns can be hidden from the popup menu of the native header.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CellToGridWindow(self, *args, **kw) -> 'grid.GridWindow':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CellToRect(self, *args, **kw) -> 'Rect':
        """ Return the rectangle corresponding to the grid cellâs size and position in logical coordinates.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ClearGrid(self) -> None:
        """ Clears all data in the underlying grid table and repaints the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ClearSelection(self) -> None:
        """ Deselects all cells that are currently selected.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ClipHorzGridLines(self, clip: bool) -> None:
        """ Change whether the horizontal grid lines are clipped by the end of the last column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ClipVertGridLines(self, clip: bool) -> None:
        """ Change whether the vertical grid lines are clipped by the end of the last row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=WANTS_CHARS, name=GridNameStr) -> bool:
        """ Creates the grid window for an object initialized using the default constructor.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CreateGrid(self, numRows, numCols, selmode=GridSelectCells) -> bool:
        """ Creates a grid with the specified initial number of rows and columns.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DeleteCols(self, pos=0, numCols=1, updateLabels=True) -> bool:
        """ Deletes one or more columns from a grid starting at the specified position.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DeleteRows(self, pos=0, numRows=1, updateLabels=True) -> bool:
        """ Deletes one or more rows from a grid starting at the specified position.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DeselectCell(self, row, col) -> None:
        """ Deselects a cell.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DeselectCol(self, col: int) -> None:
        """ Deselects a column of cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DeselectRow(self, row: int) -> None:
        """ Deselects a row of cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DevicePosToGridWindow(self, *args, **kw) -> 'grid.GridWindow':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableCellEditControl(self) -> None:
        """ Disables in-place editing of grid cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableColResize(self, col: int) -> None:
        """ Disable interactive resizing of the specified column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableDragColMove(self) -> None:
        """ Disables column moving by dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableDragColSize(self) -> None:
        """ Disables column sizing by dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableDragGridSize(self) -> None:
        """ Disable mouse dragging of grid lines to resize rows and columns.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableDragRowMove(self) -> None:
        """ Disables row moving by dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableDragRowSize(self) -> None:
        """ Disables row sizing by dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableHidingColumns(self) -> None:
        """ Disables column hiding from the header popup menu.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableRowResize(self, row: int) -> None:
        """ Disable interactive resizing of the specified row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawCellHighlight(self, dc, attr) -> None:
        """ dc (wx.DC) â

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawColLabel(self, dc, col) -> None:
        """ dc (wx.DC) â

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawColLabels(self, dc, cols) -> None:
        """ dc (wx.DC) â

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawCornerLabel(self, dc: 'DC') -> None:
        """ dc (wx.DC) â

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawRowLabel(self, dc, row) -> None:
        """ dc (wx.DC) â

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawRowLabels(self, dc, rows) -> None:
        """ dc (wx.DC) â

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawTextRectangle(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableCellEditControl(self, enable: bool=True) -> None:
        """ Enables or disables in-place editing of grid cell data.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableDragCell(self, enable: bool=True) -> None:
        """ Enables or disables cell dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableDragColMove(self, enable: bool=True) -> bool:
        """ Enables or disables column moving by dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableDragColSize(self, enable: bool=True) -> None:
        """ Enables or disables column sizing by dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableDragGridSize(self, enable: bool=True) -> None:
        """ Enables or disables row and column resizing by dragging gridlines with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableDragRowMove(self, enable: bool=True) -> bool:
        """ Enables or disables row moving by dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableDragRowSize(self, enable: bool=True) -> None:
        """ Enables or disables row sizing by dragging with the mouse.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableEditing(self, edit: bool) -> None:
        """ Makes the grid globally editable or read-only.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableGridLines(self, enable: bool=True) -> None:
        """ Turns the drawing of grid lines on or off.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableHidingColumns(self, enable: bool=True) -> bool:
        """ Enables or disables column hiding from the header popup menu.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EndBatch(self) -> None:
        """ Decrements the gridâs batch count.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def Fit(self) -> None:
        """ Overridden   wx.Window  method.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ForceRefresh(self) -> None:
        """ Causes immediate repainting of the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def FreezeTo(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetBatchCount(self) -> int:
        """ Returns the number of times that BeginBatch   has been called without (yet) matching calls to EndBatch .

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellAlignment(self, row, col) -> tuple:
        """ Sets the arguments to the horizontal and vertical text alignment values for the grid cell at the specified location.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellBackgroundColour(self, row, col) -> 'Colour':
        """ Returns the background colour of the cell at the specified location.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellEditor(self, row, col) -> 'grid.GridCellEditor':
        """ Returns a pointer to the editor for the cell at the specified location.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellFitMode(self, row, col) -> 'grid.GridFitMode':
        """ Returns the cell fitting mode.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellFont(self, row, col) -> 'Font':
        """ Returns the font for text in the grid cell at the specified location.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellHighlightColour(self) -> 'Colour':
        """ Colour

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellHighlightPenWidth(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellHighlightROPenWidth(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellOverflow(self, row, col) -> bool:
        """ Returns True if the cell value can overflow.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellRenderer(self, row, col) -> 'grid.GridCellRenderer':
        """ Returns a pointer to the renderer for the grid cell at the specified location.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellSize(self, *args, **kw) -> 'grid.Grid.CellSpan':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellTextColour(self, row, col) -> 'Colour':
        """ Returns the text colour for the grid cell at the specified location.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellValue(self, *args, **kw) -> str:
        """ Returns the string contained in the cell at the specified location.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColAt(self, colPos: int) -> int:
        """ Returns the column ID of the specified column position.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColGridLinePen(self, col: int) -> 'Pen':
        """ Returns the pen used for vertical grid lines.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColLabelAlignment(self) -> tuple:
        """ Sets the arguments to the current column label alignment values.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColLabelSize(self) -> int:
        """ Returns the current height of the column labels.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColLabelTextOrientation(self) -> int:
        """ Returns the orientation of the column labels (either  HORIZONTAL   or   VERTICAL ).

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColLabelValue(self, col: int) -> str:
        """ Returns the specified column label.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColLeft(self, col: int) -> int:
        """ Returns the coordinate of the left border specified column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColMinimalAcceptableWidth(self) -> int:
        """ Returns the minimal width to which a column may be resized.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColMinimalWidth(self, col: int) -> int:
        """ Get the minimal width of the given column/row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColPos(self, colID: int) -> int:
        """ Returns the position of the specified column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColRight(self, col: int) -> int:
        """ Returns the coordinate of the right border specified column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColSize(self, col: int) -> int:
        """ Returns the width of the specified column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColSizes(self) -> 'grid.GridSizesInfo':
        """ Get size information for all columns at once.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCornerLabelAlignment(self, horiz, vert) -> None:
        """ Sets the arguments to the current corner label alignment values.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCornerLabelTextOrientation(self) -> int:
        """ Returns the orientation of the corner label (either  HORIZONTAL   or   VERTICAL ).

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCornerLabelValue(self) -> str:
        """ Returns the (top-left) corner label.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultCellAlignment(self) -> tuple:
        """ Returns the default cell alignment.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultCellBackgroundColour(self) -> 'Colour':
        """ Returns the current default background colour for grid cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultCellFitMode(self) -> 'grid.GridFitMode':
        """ Returns the default cell fitting mode.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultCellFont(self) -> 'Font':
        """ Returns the current default font for grid cell text.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultCellOverflow(self) -> bool:
        """ Returns True if the cells can overflow by default.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultCellTextColour(self) -> 'Colour':
        """ Returns the current default colour for grid cell text.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultColLabelSize(self) -> int:
        """ Returns the default height for column labels.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultColSize(self) -> int:
        """ Returns the current default width for grid columns.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultEditor(self) -> 'grid.GridCellEditor':
        """ Returns a pointer to the current default grid cell editor.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultEditorForCell(self, *args, **kw) -> 'grid.GridCellEditor':
        """ Returns the default editor for the specified cell.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultEditorForType(self, typeName: str) -> 'grid.GridCellEditor':
        """ Returns the default editor for the cells containing values of the given type.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultGridLinePen(self) -> 'Pen':
        """ Returns the pen used for grid lines.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultRenderer(self) -> 'grid.GridCellRenderer':
        """ Returns a pointer to the current default grid cell renderer.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultRendererForCell(self, row, col) -> 'grid.GridCellRenderer':
        """ Returns the default renderer for the given cell.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultRendererForType(self, typeName: str) -> 'grid.GridCellRenderer':
        """ Returns the default renderer for the cell containing values of the given type.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultRowLabelSize(self) -> int:
        """ Returns the default width for the row labels.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultRowSize(self) -> int:
        """ Returns the current default height for grid rows.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetFirstFullyVisibleColumn(self) -> int:
        """ Returns the leftmost column of the current visible area.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetFirstFullyVisibleRow(self) -> int:
        """ Returns the topmost row of the current visible area.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetFrozenColGridWindow(self) -> 'Window':
        """ Return the columns grid window containing column frozen cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetFrozenCornerGridWindow(self) -> 'Window':
        """ Return the corner grid window containing frozen cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetFrozenRowGridWindow(self) -> 'Window':
        """ Return the rows grid window containing row frozen cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridColHeader(self) -> 'HeaderCtrl':
        """ Return the header control used for column labels display.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridColLabelWindow(self) -> 'Window':
        """ Return the column labels window.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridCornerLabelWindow(self) -> 'Window':
        """ Return the window in the top left grid corner.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridCursorCol(self) -> int:
        """ Returns the current grid cell column position.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridCursorCoords(self) -> 'grid.GridCellCoords':
        """ Returns the current grid cursor position.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridCursorRow(self) -> int:
        """ Returns the current grid cell row position.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridLineColour(self) -> 'Colour':
        """ Returns the colour used for grid lines.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridRowLabelWindow(self) -> 'Window':
        """ Return the row labels window.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridWindow(self) -> 'Window':
        """ Return the main grid window containing the grid cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridWindowOffset(self, gridWindow: 'grid.GridWindow') -> 'Point':
        """ This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetLabelBackgroundColour(self) -> 'Colour':
        """ Returns the colour used for the background of row and column labels.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetLabelFont(self) -> 'Font':
        """ Returns the font used for row and column labels.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetLabelTextColour(self) -> 'Colour':
        """ Returns the colour used for row and column label text.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetNumberCols(self) -> int:
        """ Returns the total number of grid columns.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetNumberFrozenCols(self) -> int:
        """ Returns the number of frozen grid columns.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetNumberFrozenRows(self) -> int:
        """ Returns the number of frozen grid rows.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetNumberRows(self) -> int:
        """ Returns the total number of grid rows.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetOrCreateCellAttr(self, row, col) -> 'grid.GridCellAttr':
        """ Returns the attribute for the given cell creating one if necessary.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetOrCreateCellAttrPtr(self, row, col) -> 'grid.GridCellAttrPtr':
        """ Returns the attribute for the given cell creating one if necessary.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowAt(self, rowPos: int) -> int:
        """ Returns the row ID of the specified row position.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowGridLinePen(self, row: int) -> 'Pen':
        """ Returns the pen used for horizontal grid lines.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowLabelAlignment(self) -> tuple:
        """ Returns the alignment used for row labels.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowLabelSize(self) -> int:
        """ Returns the current width of the row labels.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowLabelValue(self, row: int) -> str:
        """ Returns the specified row label.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowMinimalAcceptableHeight(self) -> int:
        """ Returns the minimal size to which rows can be resized.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowMinimalHeight(self, col: int) -> int:
        """ Returns the minimal size for the given column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowPos(self, rowID: int) -> int:
        """ Returns the position of the specified row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowSize(self, row: int) -> int:
        """ Returns the height of the specified row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowSizes(self) -> 'grid.GridSizesInfo':
        """ Get size information for all row at once.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetScrollLineX(self) -> int:
        """ Returns the number of pixels per horizontal scroll increment.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetScrollLineY(self) -> int:
        """ Returns the number of pixels per vertical scroll increment.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectedBlocks(self) -> 'grid.GridBlocks':
        """ Returns a range of grid selection blocks.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectedCells(self) -> 'grid.GridCellCoordsArray':
        """ Returns an array of individually selected cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectedColBlocks(self) -> Any:
        """ Returns an ordered range of non-overlapping selected columns.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectedCols(self) -> list[int]:
        """ Returns an array of selected columns.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectedRowBlocks(self) -> Any:
        """ Returns an ordered range of non-overlapping selected rows.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectedRows(self) -> list[int]:
        """ Returns an array of selected rows.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectionBackground(self) -> 'Colour':
        """ Returns the colour used for drawing the selection background.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectionBlockBottomRight(self) -> 'grid.GridCellCoordsArray':
        """ Returns an array of the bottom right corners of blocks of selected cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectionBlockTopLeft(self) -> 'grid.GridCellCoordsArray':
        """ Returns an array of the top left corners of blocks of selected cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectionForeground(self) -> 'Colour':
        """ Returns the colour used for drawing the selection foreground.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectionMode(self) -> 'grid.GridSelectionModes':
        """ Returns the current selection mode.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSortingColumn(self) -> int:
        """ Return the column in which the sorting indicator is currently displayed.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetTable(self) -> 'grid.GridTableBase':
        """ Returns a base pointer to the current table object.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GoToCell(self, *args, **kw) -> None:
        """ Make the given cell current and ensure it is visible.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GridLinesEnabled(self) -> bool:
        """ Returns True if drawing of grid lines is turned on, False otherwise.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def HideCellEditControl(self) -> None:
        """ Hides the in-place cell edit control.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def HideCol(self, col: int) -> None:
        """ Hides the specified column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def HideColLabels(self) -> None:
        """ Hides the column labels by calling SetColLabelSize   with a size of 0.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def HideRow(self, col: int) -> None:
        """ Hides the specified row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def HideRowLabels(self) -> None:
        """ Hides the row labels by calling SetRowLabelSize   with a size of 0.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def InsertCols(self, pos=0, numCols=1, updateLabels=True) -> bool:
        """ Inserts one or more new columns into a grid with the first new column at the specified position.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def InsertRows(self, pos=0, numRows=1, updateLabels=True) -> bool:
        """ Inserts one or more new rows into a grid with the first new row at the specified position.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsCellEditControlEnabled(self) -> bool:
        """ Returns True if the in-place edit control is currently enabled.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsCellEditControlShown(self) -> bool:
        """ Returns True if the in-place edit control is currently shown.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsColShown(self, col: int) -> bool:
        """ Returns True if the specified column is not currently hidden.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsCurrentCellReadOnly(self) -> bool:
        """ Returns True if the current cell is read-only.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsEditable(self) -> bool:
        """ Returns False if the whole grid has been set as read-only or True otherwise.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsInSelection(self, *args, **kw) -> bool:
        """ Returns True if the given cell is selected.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsReadOnly(self, row, col) -> bool:
        """ Returns True if the cell at the specified location canât be edited.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsRowShown(self, row: int) -> bool:
        """ Returns True if the specified row is not currently hidden.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsSelection(self) -> bool:
        """ Returns True if there are currently any selected cells, rows, columns or blocks.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsSortOrderAscending(self) -> bool:
        """ Return True if the current sorting order is ascending or False if it is descending.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsSortingBy(self, col: int) -> bool:
        """ Return True if this column is currently used for sorting.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsUsingNativeHeader(self) -> bool:
        """ Return True if native header control is currently being used.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsVisible(self, *args, **kw) -> bool:
        """ Returns True if a cell is either entirely or at least partially visible in the grid window.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MakeCellVisible(self, *args, **kw) -> None:
        """ Brings the specified cell into the visible grid cell area with minimal scrolling.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorDown(self, expandSelection: bool) -> bool:
        """ Moves the grid cursor down by one row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorDownBlock(self, expandSelection: bool) -> bool:
        """ Moves the grid cursor down in the current column such that it skips to the beginning or end of a block of non-empty cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorLeft(self, expandSelection: bool) -> bool:
        """ Moves the grid cursor left by one column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorLeftBlock(self, expandSelection: bool) -> bool:
        """ Moves the grid cursor left in the current row such that it skips to the beginning or end of a block of non-empty cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorRight(self, expandSelection: bool) -> bool:
        """ Moves the grid cursor right by one column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorRightBlock(self, expandSelection: bool) -> bool:
        """ Moves the grid cursor right in the current row such that it skips to the beginning or end of a block of non-empty cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorUp(self, expandSelection: bool) -> bool:
        """ Moves the grid cursor up by one row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorUpBlock(self, expandSelection: bool) -> bool:
        """ Moves the grid cursor up in the current column such that it skips to the beginning or end of a block of non-empty cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MovePageDown(self) -> bool:
        """ Moves the grid cursor down by some number of rows so that the previous bottom visible row becomes the top visible row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MovePageUp(self) -> bool:
        """ Moves the grid cursor up by some number of rows so that the previous top visible row becomes the bottom visible row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ProcessTableMessage(self, msg: 'grid.GridTableMessage') -> bool:
        """ Receive and handle a message from the table.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def RefreshAttr(self, row, col) -> None:
        """ Invalidates the cached attribute for the given cell.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def RegisterDataType(self, typeName, renderer, editor) -> None:
        """ Register a new data type.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def Render(*args, **kwargs) -> None:
        """ Draws part or all of a   wx.grid.Grid  on a   wx.DC  for printing or display.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ResetColPos(self) -> None:
        """ Resets the position of the columns to the default.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ResetRowPos(self) -> None:
        """ Resets the position of the rows to the default.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SaveEditControlValue(self) -> None:
        """ Sets the value of the current grid cell to the current in-place edit control value.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SelectAll(self) -> None:
        """ Selects all cells in the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SelectBlock(self, *args, **kw) -> None:
        """ Selects a rectangular block of cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SelectCol(self, col, addToSelected=False) -> None:
        """ Selects the specified column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SelectRow(self, row, addToSelected=False) -> None:
        """ Selects the specified row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetAttr(self, row, col, attr) -> None:
        """ Sets the cell attributes for the specified cell.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellAlignment(self, row, col, horiz, vert) -> None:
        """ Sets the horizontal and vertical alignment for grid cell text at the specified location.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellBackgroundColour(self, row, col, colour) -> None:
        """ Set the background colour for the given cell or all cells by default.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellEditor(self, row, col, editor) -> None:
        """ Sets the editor for the grid cell at the specified location.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellFitMode(self, row, col, fitMode) -> None:
        """ Specifies the behaviour of the cell contents if it doesnât fit into the available space.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellFont(self, row, col, font) -> None:
        """ Sets the font for text in the grid cell at the specified location.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellHighlightColour(self) -> None:
        """ `` (wx.Colour) â

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellHighlightPenWidth(self, width: int) -> None:
        """ width (int) â

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellHighlightROPenWidth(self, width: int) -> None:
        """ width (int) â

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellOverflow(self, row, col, allow) -> None:
        """ Sets the overflow permission of the cell.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellRenderer(self, row, col, renderer) -> None:
        """ Sets the renderer for the grid cell at the specified location.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellSize(self, row, col, num_rows, num_cols) -> None:
        """ Set the size of the cell.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellTextColour(self, row, col, colour) -> None:
        """ Sets the text colour for the given cell.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellValue(self, *args, **kw) -> None:
        """ Sets the string value for the cell at the specified location.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColAttr(self, col, attr) -> None:
        """ Sets the cell attributes for all cells in the specified column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColFormatBool(self, col: int) -> None:
        """ Sets the specified column to display boolean values.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColFormatCustom(self, col, typeName) -> None:
        """ Sets the specified column to display data in a custom format.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColFormatDate(self, col, format="") -> None:
        """ Sets the specified column to display date values.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColFormatFloat(self, col, width=-1, precision=-1) -> None:
        """ Sets the specified column to display floating point values with the given width and precision.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColFormatNumber(self, col: int) -> None:
        """ Sets the specified column to display integer values.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColLabelAlignment(self, horiz, vert) -> None:
        """ Sets the horizontal and vertical alignment of column label text.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColLabelSize(self, height: int) -> None:
        """ Sets the height of the column labels.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColLabelTextOrientation(self, textOrientation: int) -> None:
        """ Sets the orientation of the column labels (either  HORIZONTAL   or   VERTICAL ).

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColLabelValue(self, col, value) -> None:
        """ Set the value for the given column label.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColMinimalAcceptableWidth(self, width: int) -> None:
        """ Sets the minimal width  to which the user can resize columns.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColMinimalWidth(self, col, width) -> None:
        """ Sets the minimal width  for the specified column col.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColPos(self, colID, newPos) -> None:
        """ Sets the position of the specified column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColSize(self, col, width) -> None:
        """ Sets the width of the specified column.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColSizes(self, sizeInfo: 'grid.GridSizesInfo') -> None:
        """ Restore all columns sizes.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColumnsOrder(self, order: list[int]) -> None:
        """ Sets the positions of all columns at once.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCornerLabelAlignment(self, horiz, vert) -> None:
        """ Sets the horizontal and vertical alignment of the (top-left) corner label text.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCornerLabelTextOrientation(self, textOrientation: int) -> None:
        """ Sets the orientation of the (top-left) corner label (either  HORIZONTAL   or   VERTICAL ).

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCornerLabelValue(self) -> None:
        """ Set the value for the (top-left) corner label.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultCellAlignment(self, horiz, vert) -> None:
        """ Sets the default horizontal and vertical alignment for grid cell text.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultCellBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the default background colour for grid cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultCellFitMode(self, fitMode: 'grid.GridFitMode') -> None:
        """ Specifies the default behaviour of the cell contents if it doesnât fit into the available space.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultCellFont(self, font: 'Font') -> None:
        """ Sets the default font to be used for grid cell text.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultCellOverflow(self, allow: bool) -> None:
        """ Sets the default overflow permission of the cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultCellTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the current default colour for grid cell text.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultColSize(self, width, resizeExistingCols=False) -> None:
        """ Sets the default width for columns in the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultEditor(self, editor: 'grid.GridCellEditor') -> None:
        """ Sets the default editor for grid cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultRenderer(self, renderer: 'grid.GridCellRenderer') -> None:
        """ Sets the default renderer for grid cells.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultRowSize(self, height, resizeExistingRows=False) -> None:
        """ Sets the default height for rows in the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetGridCursor(self, *args, **kw) -> None:
        """ Set the grid cursor to the specified cell.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetGridFrozenBorderColour(self) -> None:
        """ `` (wx.Colour) â

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetGridFrozenBorderPenWidth(self, width: int) -> None:
        """ width (int) â

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetGridLineColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used to draw grid lines.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetLabelBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the background colour for row and column labels.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetLabelFont(self, font: 'Font') -> None:
        """ Sets the font for row and column labels.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetLabelTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour for row and column label text.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetMargins(self, extraWidth, extraHeight) -> None:
        """ Sets the extra margins used around the grid area.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetReadOnly(self, row, col, isReadOnly=True) -> None:
        """ Makes the cell at the specified location read-only or editable.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowAttr(self, row, attr) -> None:
        """ Sets the cell attributes for all cells in the specified row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowLabelAlignment(self, horiz, vert) -> None:
        """ Sets the horizontal and vertical alignment of row label text.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowLabelSize(self, width: int) -> None:
        """ Sets the width of the row labels.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowLabelValue(self, row, value) -> None:
        """ Sets the value for the given row label.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowMinimalAcceptableHeight(self, height: int) -> None:
        """ Sets the minimal row height  used by default.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowMinimalHeight(self, row, height) -> None:
        """ Sets the minimal height  for the specified row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowPos(self, rowID, newPos) -> None:
        """ Sets the position of the specified row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowSize(self, row, height) -> None:
        """ Sets the height of the specified row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowSizes(self, sizeInfo: 'grid.GridSizesInfo') -> None:
        """ Restore all rows sizes.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowsOrder(self, order: list[int]) -> None:
        """ Sets the positions of all rows at once.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetScrollLineX(self, x: int) -> None:
        """ Sets the number of pixels per horizontal scroll increment.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetScrollLineY(self, y: int) -> None:
        """ Sets the number of pixels per vertical scroll increment.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetSelectionBackground(self, c: Union[int, str, 'Colour']) -> None:
        """ Set the colour to be used for drawing the selection background.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetSelectionForeground(self, c: Union[int, str, 'Colour']) -> None:
        """ Set the colour to be used for drawing the selection foreground.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetSelectionMode(self, selmode: GridSelectionModes) -> None:
        """ Set the selection behaviour of the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetSortingColumn(self, col, ascending=True) -> None:
        """ Set the column to display the sorting indicator in and its direction.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetTabBehaviour(self, behaviour: TabBehaviour) -> None:
        """ Set the gridâs behaviour when the user presses the TAB key.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def _SetTable(self, table, takeOwnership=False, selmode=GridSelectCells) -> bool:
        """ Passes a pointer to a custom grid table to be used by the grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetTable(self, table, takeOwnership=False, selmode=Grid.GridSelectCells) -> None:
        """ Set the Grid Table to be used by this grid.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetUseNativeColLabels(self, native: bool=True) -> None:
        """ Call this in order to make the column labels use a native look by using wx.RendererNative.DrawHeaderButton   internally.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ShowCellEditControl(self) -> None:
        """ Displays the active in-place cell edit control for the current cell after it was hidden.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ShowCol(self, col: int) -> None:
        """ Shows the previously hidden column by resizing it to non-0 size.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ShowRow(self, col: int) -> None:
        """ Shows the previously hidden row.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def UnsetSortingColumn(self) -> None:
        """ Remove any currently shown sorting indicator.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def UseNativeColHeader(self, native: bool=True) -> bool:
        """ Enable the use of native header window for column labels.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def XToCol(self, x, clipToMinMax=False, gridWindow=None) -> int:
        """ Returns the column at the given pixel position depending on the window.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def XToEdgeOfCol(self, x: int) -> int:
        """ Returns the column whose right hand edge is close to the given logical x  position.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def XYToCell(self, *args, **kw) -> 'grid.GridCellCoords':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def YToEdgeOfRow(self, y: int) -> int:
        """ Returns the row whose bottom edge is close to the given logical y  position.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def YToRow(self, y, clipToMinMax=False, gridWindow=None) -> int:
        """ Returns the grid row that corresponds to the logical y  coordinate.

            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    BatchCount: int  # See GetBatchCount
    CellHighlightColour: 'Colour'  # See GetCellHighlightColour and SetCellHighlightColour
    CellHighlightPenWidth: int  # See GetCellHighlightPenWidth and SetCellHighlightPenWidth
    CellHighlightROPenWidth: int  # See GetCellHighlightROPenWidth and SetCellHighlightROPenWidth
    ColLabelSize: int  # See GetColLabelSize and SetColLabelSize
    ColLabelTextOrientation: int  # See GetColLabelTextOrientation and SetColLabelTextOrientation
    ColMinimalAcceptableWidth: int  # See GetColMinimalAcceptableWidth and SetColMinimalAcceptableWidth
    ColSizes: 'grid.GridSizesInfo'  # See GetColSizes and SetColSizes
    CornerLabelTextOrientation: int  # See GetCornerLabelTextOrientation and SetCornerLabelTextOrientation
    CornerLabelValue: str  # See GetCornerLabelValue and SetCornerLabelValue
    DefaultCellBackgroundColour: 'Colour'  # See GetDefaultCellBackgroundColour and SetDefaultCellBackgroundColour
    DefaultCellFitMode: 'grid.GridFitMode'  # See GetDefaultCellFitMode and SetDefaultCellFitMode
    DefaultCellFont: 'Font'  # See GetDefaultCellFont and SetDefaultCellFont
    DefaultCellOverflow: bool  # See GetDefaultCellOverflow and SetDefaultCellOverflow
    DefaultCellTextColour: 'Colour'  # See GetDefaultCellTextColour and SetDefaultCellTextColour
    DefaultColLabelSize: int  # See GetDefaultColLabelSize
    DefaultColSize: int  # See GetDefaultColSize and SetDefaultColSize
    DefaultEditor: 'grid.GridCellEditor'  # See GetDefaultEditor and SetDefaultEditor
    DefaultGridLinePen: 'Pen'  # See GetDefaultGridLinePen
    DefaultRenderer: 'grid.GridCellRenderer'  # See GetDefaultRenderer and SetDefaultRenderer
    DefaultRowLabelSize: int  # See GetDefaultRowLabelSize
    DefaultRowSize: int  # See GetDefaultRowSize and SetDefaultRowSize
    FirstFullyVisibleColumn: int  # See GetFirstFullyVisibleColumn
    FirstFullyVisibleRow: int  # See GetFirstFullyVisibleRow
    FrozenColGridWindow: 'Window'  # See GetFrozenColGridWindow
    FrozenCornerGridWindow: 'Window'  # See GetFrozenCornerGridWindow
    FrozenRowGridWindow: 'Window'  # See GetFrozenRowGridWindow
    GridColHeader: 'HeaderCtrl'  # See GetGridColHeader
    GridColLabelWindow: 'Window'  # See GetGridColLabelWindow
    GridCornerLabelWindow: 'Window'  # See GetGridCornerLabelWindow
    GridCursorCol: int  # See GetGridCursorCol
    GridCursorCoords: 'grid.GridCellCoords'  # See GetGridCursorCoords
    GridCursorRow: int  # See GetGridCursorRow
    GridLineColour: 'Colour'  # See GetGridLineColour and SetGridLineColour
    GridRowLabelWindow: 'Window'  # See GetGridRowLabelWindow
    GridWindow: 'Window'  # See GetGridWindow
    LabelBackgroundColour: 'Colour'  # See GetLabelBackgroundColour and SetLabelBackgroundColour
    LabelFont: 'Font'  # See GetLabelFont and SetLabelFont
    LabelTextColour: 'Colour'  # See GetLabelTextColour and SetLabelTextColour
    NumberCols: int  # See GetNumberCols
    NumberFrozenCols: int  # See GetNumberFrozenCols
    NumberFrozenRows: int  # See GetNumberFrozenRows
    NumberRows: int  # See GetNumberRows
    RowLabelSize: int  # See GetRowLabelSize and SetRowLabelSize
    RowMinimalAcceptableHeight: int  # See GetRowMinimalAcceptableHeight and SetRowMinimalAcceptableHeight
    RowSizes: 'grid.GridSizesInfo'  # See GetRowSizes and SetRowSizes
    ScrollLineX: int  # See GetScrollLineX and SetScrollLineX
    ScrollLineY: int  # See GetScrollLineY and SetScrollLineY
    SelectedBlocks: 'grid.GridBlocks'  # See GetSelectedBlocks
    SelectedCells: 'grid.GridCellCoordsArray'  # See GetSelectedCells
    SelectedColBlocks: Any  # See GetSelectedColBlocks
    SelectedCols: list[int]  # See GetSelectedCols
    SelectedRowBlocks: Any  # See GetSelectedRowBlocks
    SelectedRows: list[int]  # See GetSelectedRows
    SelectionBackground: 'Colour'  # See GetSelectionBackground and SetSelectionBackground
    SelectionBlockBottomRight: 'grid.GridCellCoordsArray'  # See GetSelectionBlockBottomRight
    SelectionBlockTopLeft: 'grid.GridCellCoordsArray'  # See GetSelectionBlockTopLeft
    SelectionForeground: 'Colour'  # See GetSelectionForeground and SetSelectionForeground
    SelectionMode: 'grid.GridSelectionModes'  # See GetSelectionMode and SetSelectionMode
    SortingColumn: int  # See GetSortingColumn and SetSortingColumn
    Table: 'grid.GridTableBase'  # See GetTable and SetTable



class GridCellAttrProvider(ClientDataContainer):
    """ Class providing attributes to be used for the grid cells.

        Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
    """
    def __init__(self) -> None:
        """ Trivial default constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def GetAttr(self, row, col, kind) -> 'grid.GridCellAttr':
        """ Get the attribute to use for the specified cell.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def GetAttrPtr(self, row, col, kind) -> 'grid.GridCellAttrPtr':
        """ Get the attribute to use for the specified cell.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def GetColumnHeaderRenderer(self, col: int) -> 'grid.GridColumnHeaderRenderer':
        """ Return the renderer used for drawing column headers.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def GetCornerRenderer(self) -> 'grid.GridCornerHeaderRenderer':
        """ Return the renderer used for drawing the corner window.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def GetRowHeaderRenderer(self, row: int) -> 'grid.GridRowHeaderRenderer':
        """ Return the renderer used for drawing row headers.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def SetAttr(self, attr, row, col) -> None:
        """ Set attribute for the specified cell.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def SetColAttr(self, attr, col) -> None:
        """ Set attribute for the specified column.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def SetRowAttr(self, attr, row) -> None:
        """ Set attribute for the specified row.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    CornerRenderer: 'grid.GridCornerHeaderRenderer'  # See GetCornerRenderer



class GridEditorCreatedEvent(CommandEvent):
    """ ^^

        Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def GetCol(self) -> int:
        """ Returns the column at which the event occurred.

            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def GetControl(self) -> 'Control':
        """ Returns the edit control.

            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def GetRow(self) -> int:
        """ Returns the row at which the event occurred.

            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def GetWindow(self) -> 'Window':
        """ Returns the edit window.

            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def SetCol(self, col: int) -> None:
        """ Sets the column at which the event occurred.

            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def SetControl(self, ctrl: 'Control') -> None:
        """ Sets the edit control.

            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def SetRow(self, row: int) -> None:
        """ Sets the row at which the event occurred.

            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def SetWindow(self, window: 'Window') -> None:
        """ Sets the edit window.

            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    Col: int  # See GetCol and SetCol
    Control: '_Control'  # See GetControl and SetControl
    Row: int  # See GetRow and SetRow
    Window: '_Window'  # See GetWindow and SetWindow



EVT_GRID_EDITOR_CREATED: int  # The editor for a cell was created. Processes a  wxEVT_GRID_EDITOR_CREATED   event type.

EVT_GRID_CMD_EDITOR_CREATED: int  # The editor for a cell was created; variant taking a window identifier. Processes a  wxEVT_GRID_EDITOR_CREATED   event type. ^^

class GridTableBase(Object):
    """ The almost abstract base class for grid tables.

        Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def AppendCols(self, numCols: int=1) -> bool:
        """ Exactly the same as AppendRows   but for columns.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def AppendRows(self, numRows: int=1) -> bool:
        """ Append additional rows at the end of the table.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def CanGetValueAs(self, row, col, typeName) -> bool:
        """ Returns True if the value of the given cell can be accessed as if it were of the specified type.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def CanHaveAttributes(self) -> bool:
        """ Returns True if this table supports attributes or False otherwise.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def CanMeasureColUsingSameAttr(self, col: int) -> bool:
        """ Override to return True if the same attribute can be used for measuring all cells in the given column.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def CanSetValueAs(self, row, col, typeName) -> bool:
        """ Returns True if the value of the given cell can be set as if it were of the specified type.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def Clear(self) -> None:
        """ Clear the table contents.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def DeleteCols(self, pos=0, numCols=1) -> bool:
        """ Exactly the same as DeleteRows   but for columns.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def DeleteRows(self, pos=0, numRows=1) -> bool:
        """ Delete rows from the table.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetAttr(self, row, col, kind) -> 'grid.GridCellAttr':
        """ Return the attribute for the given cell.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetAttrProvider(self) -> 'grid.GridCellAttrProvider':
        """ Returns the attribute provider currently being used.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetAttrPtr(self, row, col, kind) -> 'grid.GridCellAttrPtr':
        """ Return the attribute for the given cell.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetColLabelValue(self, col: int) -> str:
        """ Return the label of the specified column.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetColsCount(self) -> int:
        """ Return the number of columns in the table.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetCornerLabelValue(self) -> str:
        """ Return the label of the gridâs corner.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetNumberCols(self) -> int:
        """ Must be overridden to return the number of columns in the table.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetNumberRows(self) -> int:
        """ Must be overridden to return the number of rows in the table.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetRowLabelValue(self, row: int) -> str:
        """ Return the label of the specified row.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetRowsCount(self) -> int:
        """ Return the number of rows in the table.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetTypeName(self, row, col) -> str:
        """ Returns the type of the value in the given cell.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetValue(self, row, col) -> Any:
        """ Must be overridden to implement accessing the table values as text.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetValueAsBool(self, row, col) -> bool:
        """ Returns the value of the given cell as a boolean.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetValueAsDouble(self, row, col) -> float:
        """ Returns the value of the given cell as a double.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetValueAsLong(self, row, col) -> int:
        """ Returns the value of the given cell as a long.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetView(self) -> 'grid.Grid':
        """ Returns the last grid passed to SetView .

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def InsertCols(self, pos=0, numCols=1) -> bool:
        """ Exactly the same as InsertRows   but for columns.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def InsertRows(self, pos=0, numRows=1) -> bool:
        """ Insert additional rows into the table.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def IsEmpty(self, coords: 'grid.GridCellCoords') -> bool:
        """ Same as IsEmptyCell   but taking   wx.grid.GridCellCoords.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def IsEmptyCell(self, row, col) -> bool:
        """ May be overridden to implement testing for empty cells.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetAttr(self, attr, row, col) -> None:
        """ Set attribute of the specified cell.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetAttrProvider(self, attrProvider: 'grid.GridCellAttrProvider') -> None:
        """ Associate this attributes provider with the table.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetColAttr(self, attr, col) -> None:
        """ Set attribute of the specified column.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetColLabelValue(self, col, label) -> None:
        """ Exactly the same as SetRowLabelValue   but for columns.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetCornerLabelValue(self) -> None:
        """ Set the given label for the gridâs corner.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetRowAttr(self, attr, row) -> None:
        """ Set attribute of the specified row.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetRowLabelValue(self, row, label) -> None:
        """ Set the given label for the specified row.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetValue(self, row, col, value) -> None:
        """ Must be overridden to implement setting the table values as text.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetValueAsBool(self, row, col, value) -> None:
        """ Sets the value of the given cell as a boolean.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetValueAsDouble(self, row, col, value) -> None:
        """ Sets the value of the given cell as a double.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetValueAsLong(self, row, col, value) -> None:
        """ Sets the value of the given cell as a long.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetView(self, grid: 'grid.Grid') -> None:
        """ Called by the grid when the table is associated with it.

            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    AttrProvider: 'grid.GridCellAttrProvider'  # See GetAttrProvider and SetAttrProvider
    ColsCount: int  # See GetColsCount
    CornerLabelValue: str  # See GetCornerLabelValue and SetCornerLabelValue
    NumberCols: int  # See GetNumberCols
    NumberRows: int  # See GetNumberRows
    RowsCount: int  # See GetRowsCount
    View: 'grid.Grid'  # See GetView and SetView



class GridStringTable(GridTableBase):
    """ Simplest type of data table for a grid for small tables of strings
that are stored in memory.

        Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def AppendCols(self, numCols: int=1) -> bool:
        """ Exactly the same as AppendRows   but for columns.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def AppendRows(self, numRows: int=1) -> bool:
        """ Append additional rows at the end of the table.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def Clear(self) -> None:
        """ Clear the table contents.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def DeleteCols(self, pos=0, numCols=1) -> bool:
        """ Exactly the same as DeleteRows   but for columns.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def DeleteRows(self, pos=0, numRows=1) -> bool:
        """ Delete rows from the table.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def GetColLabelValue(self, col: int) -> str:
        """ Return the label of the specified column.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def GetCornerLabelValue(self) -> str:
        """ Return the label of the gridâs corner.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def GetNumberCols(self) -> int:
        """ Must be overridden to return the number of columns in the table.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def GetNumberRows(self) -> int:
        """ Must be overridden to return the number of rows in the table.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def GetRowLabelValue(self, row: int) -> str:
        """ Return the label of the specified row.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def GetValue(self, row, col) -> str:
        """ Must be overridden to implement accessing the table values as text.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def InsertCols(self, pos=0, numCols=1) -> bool:
        """ Exactly the same as InsertRows   but for columns.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def InsertRows(self, pos=0, numRows=1) -> bool:
        """ Insert additional rows into the table.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def SetColLabelValue(self, col, label) -> None:
        """ Exactly the same as SetRowLabelValue   but for columns.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def SetCornerLabelValue(self) -> None:
        """ Set the given label for the gridâs corner.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def SetRowLabelValue(self, row, label) -> None:
        """ Set the given label for the specified row.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def SetValue(self, row, col, value) -> None:
        """ Must be overridden to implement setting the table values as text.

            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    CornerLabelValue: str  # See GetCornerLabelValue and SetCornerLabelValue
    NumberCols: int  # See GetNumberCols
    NumberRows: int  # See GetNumberRows



class GridCellRenderer(SharedClientDataContainer,RefCounter):
    """ This class is responsible for actually drawing the cell in the grid.

        Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """

    def Clone(self) -> 'grid.GridCellRenderer':
        """ This function must be implemented in derived classes to return a copy of itself.

            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """

    def Draw(self, grid, attr, dc, rect, row, col, isSelected) -> None:
        """ Draw the given cell on the provided DC inside the given rectangle using the style specified by the attribute and the default or selected state corresponding to the isSelected value.

            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """

    def GetBestHeight(self, grid, attr, dc, row, col, width) -> int:
        """ Get the preferred height of the cell at the given width.

            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """

    def GetBestSize(self, grid, attr, dc, row, col) -> 'Size':
        """ Get the preferred size of the cell for its contents.

            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """

    def GetBestWidth(self, grid, attr, dc, row, col, height) -> int:
        """ Get the preferred width of the cell at the given height.

            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """

    def GetMaxBestSize(self, grid, attr, dc) -> 'Size':
        """ Get the maximum possible size for a cell using this renderer, if possible.

            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """



class GridCellBoolRenderer(GridCellRenderer):
    """ This class may be used to format boolean data in a cell.

        Source: https://docs.wxpython.org/wx.grid.GridCellBoolRenderer.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellBoolRenderer.html
        """



class GridCellFloatRenderer(GridCellStringRenderer):
    """ This class may be used to format floating point data in a cell.

        Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
    """
    def __init__(self, width=-1, precision=-1, format=GRID_FLOAT_FORMAT_DEFAULT) -> None:
        """ Float cell renderer constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def GetFormat(self) -> int:
        """ Returns the specifier used to format the data to string.

            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def GetPrecision(self) -> int:
        """ Returns the precision.

            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def GetWidth(self) -> int:
        """ Returns the width.

            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def SetFormat(self, format: int) -> None:
        """ Set the format to use for display the number.

            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def SetParameters(self, params: str) -> None:
        """ The parameters string format is âwidth[,precision[,format]]â where  format   should be chosen between f|e|g|E|G (f is used by default)

            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def SetPrecision(self, precision: int) -> None:
        """ Sets the precision.

            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def SetWidth(self, width: int) -> None:
        """ Sets the width.

            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    Format: int  # See GetFormat and SetFormat
    Precision: int  # See GetPrecision and SetPrecision
    Width: int  # See GetWidth and SetWidth



class GridCellNumberRenderer(GridCellStringRenderer):
    """ This class may be used to format integer data in a cell.

        Source: https://docs.wxpython.org/wx.grid.GridCellNumberRenderer.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellNumberRenderer.html
        """



class GridCellStringRenderer(GridCellRenderer):
    """ This class may be used to format string data in a cell; it is the
default for string cells.

        Source: https://docs.wxpython.org/wx.grid.GridCellStringRenderer.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellStringRenderer.html
        """



class GridCellDateRenderer(GridCellStringRenderer):
    """ This class may be used to show a date, without time, in a cell.

        Source: https://docs.wxpython.org/wx.grid.GridCellDateRenderer.html
    """
    def __init__(self, outformat: str="") -> None:
        """ Date renderer constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellDateRenderer.html
        """

    def SetParameters(self, params: str) -> None:
        """ Sets the strftime()-like format string which will be used to render the date.

            Source: https://docs.wxpython.org/wx.grid.GridCellDateRenderer.html
        """



class GridCellDateTimeRenderer(GridCellDateRenderer):
    """ This class may be used to format a date/time data in a cell.

        Source: https://docs.wxpython.org/wx.grid.GridCellDateTimeRenderer.html
    """
    def __init__(self, outformat=DefaultDateTimeFormat, informat=DefaultDateTimeFormat) -> None:
        """ Date/time renderer constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellDateTimeRenderer.html
        """



class GridCellAttr(SharedClientDataContainer,RefCounter):
    """ This class can be used to alter the cellsâ appearance in the grid by
changing their attributes from the defaults.

        Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def CanOverflow(self) -> bool:
        """ Returns True if the cell will draw an overflowed text into the neighbouring cells.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def Clone(self) -> 'grid.GridCellAttr':
        """ Creates a new copy of this object.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def DecRef(self) -> None:
        """ This class is reference counted: it is created with ref count of 1, so calling DecRef   once will delete it.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetAlignment(self) -> tuple:
        """ Get the alignment to use for the cell with the given attribute.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ Returns the background colour.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetEditor(self, grid, row, col) -> 'grid.GridCellEditor':
        """ Returns the cell editor.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetEditorPtr(self, grid, row, col) -> 'grid.GridCellEditor':
        """ Returns the cell editor.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetFitMode(self) -> 'grid.GridFitMode':
        """ Returns the fitting mode for the cells using this attribute.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetFont(self) -> 'Font':
        """ Returns the font.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetKind(self) -> 'grid.AttrKind':
        """ wx.grid.GridCellAttr.AttrKind

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetNonDefaultAlignment(self) -> tuple:
        """ Get the alignment defined by this attribute.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetOverflow(self) -> bool:
        """ Returns True if the cells using this attribute overflow into the neighbouring cells.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetRenderer(self, grid, row, col) -> 'grid.GridCellRenderer':
        """ Returns the cell renderer.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetSize(self) -> tuple:
        """ tuple

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetTextColour(self) -> 'Colour':
        """ Returns the text colour.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasAlignment(self) -> bool:
        """ Returns True if this attribute has a valid alignment set.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasBackgroundColour(self) -> bool:
        """ Returns True if this attribute has a valid background colour set.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasEditor(self) -> bool:
        """ Returns True if this attribute has a valid cell editor set.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasFont(self) -> bool:
        """ Returns True if this attribute has a valid font set.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasOverflowMode(self) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasReadWriteMode(self) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasRenderer(self) -> bool:
        """ Returns True if this attribute has a valid cell renderer set.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasSize(self) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasTextColour(self) -> bool:
        """ Returns True if this attribute has a valid text colour set.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def IncRef(self) -> None:
        """ This class is reference counted: it is created with ref count of 1, so calling DecRef   once will delete it.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def IsReadOnly(self) -> bool:
        """ Returns True if this cell is set as read-only.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def MergeWith(self, mergefrom: 'grid.GridCellAttr') -> None:
        """ mergefrom (wx.grid.GridCellAttr) â

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetAlignment(self, hAlign, vAlign) -> None:
        """ Sets the alignment.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ Sets the background colour.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetDefAttr(self, defAttr: 'grid.GridCellAttr') -> None:
        """ defAttr (wx.grid.GridCellAttr) â

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetEditor(self, editor: 'grid.GridCellEditor') -> None:
        """ Sets the editor to be used with the cells with this attribute.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetFitMode(self, fitMode: 'grid.GridFitMode') -> None:
        """ Specifies the behaviour of the cell contents if it doesnât fit into the available space.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the font.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetKind(self, kind: AttrKind) -> None:
        """ kind (AttrKind) â

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetOverflow(self, allow: bool=True) -> None:
        """ Specifies if cells using this attribute should overflow or clip their contents.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetReadOnly(self, isReadOnly: bool=True) -> None:
        """ Sets the cell as read-only.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetRenderer(self, renderer: 'grid.GridCellRenderer') -> None:
        """ Sets the renderer to be used for cells with this attribute.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetSize(self, num_rows, num_cols) -> None:
        """ num_rows (int) â

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ Sets the text colour.

            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    BackgroundColour: 'Colour'  # See GetBackgroundColour and SetBackgroundColour
    FitMode: 'grid.GridFitMode'  # See GetFitMode and SetFitMode
    Font: '_Font'  # See GetFont and SetFont
    Kind: 'grid.AttrKind'  # See GetKind and SetKind
    Overflow: bool  # See GetOverflow and SetOverflow
    TextColour: 'Colour'  # See GetTextColour and SetTextColour



ALIGN_LEFT: int

ALIGN_INVALID: int

class GridCellEditor(SharedClientDataContainer,RefCounter):
    """ This class is responsible for providing and manipulating the in-place
edit controls for the grid.

        Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def ApplyEdit(self, row, col, grid) -> None:
        """ Effectively save the changes in the grid.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def BeginEdit(self, row, col, grid) -> None:
        """ Fetch the value from the table and prepare the edit control to begin editing.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def Clone(self) -> 'grid.GridCellEditor':
        """ Create a new object which is the copy of this one.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def Create(self, parent, id, evtHandler) -> None:
        """ Creates the actual edit control.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def Destroy(self) -> None:
        """ Final cleanup.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def DoActivate(self, row, col, grid) -> None:
        """ Function which must be overridden for âactivatableâ editors.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ End editing the cell.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def GetControl(self) -> 'Control':
        """ Get the   wx.Control  used by this editor.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def GetValue(self) -> str:
        """ Returns the value currently in the editor control.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def GetWindow(self) -> 'Window':
        """ Get the edit window used by this editor.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def HandleReturn(self, event: 'KeyEvent') -> None:
        """ Some types of controls on some platforms may need some help with the Return key.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def IsAcceptedKey(self, event: 'KeyEvent') -> bool:
        """ Return True to allow the given key to start editing: the base class version only checks that the event has no modifiers.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def IsCreated(self) -> bool:
        """ Returns True if the edit control has been created.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def PaintBackground(self, dc, rectCell, attr) -> None:
        """ Draws the part of the cell not occupied by the control: the base class version just fills it with background colour from the attribute.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def Reset(self) -> None:
        """ Reset the value in the control back to its starting value.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def SetControl(self, control: 'Control') -> None:
        """ Set the   wx.Control  that will be used by this cell editor for editing the value.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def SetSize(self, rect: 'Rect') -> None:
        """ Size and position the edit control.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def SetWindow(self, window: 'Window') -> None:
        """ Set the   wx.Window  that will be used by this cell editor for editing the value.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def Show(self, show, attr=None) -> None:
        """ Show or hide the edit control, use the specified attributes to set colours/fonts for it.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def StartingClick(self) -> None:
        """ If the editor is enabled by clicking on the cell, this method will be called.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def StartingKey(self, event: 'KeyEvent') -> None:
        """ If the editor is enabled by pressing keys on the grid, this will be called to let the editor do something about that first key if desired.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def TryActivate(self, row, col, grid, actSource) -> 'grid.GridActivationResult':
        """ Function allowing to create an âactivatableâ editor.

            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    Control: '_Control'  # See GetControl and SetControl
    Value: str  # See GetValue
    Window: '_Window'  # See GetWindow and SetWindow



class GridCellBoolEditor(GridCellEditor):
    """ Grid cell editor for boolean data.

        Source: https://docs.wxpython.org/wx.grid.GridCellBoolEditor.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellBoolEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ End editing the cell.

            Source: https://docs.wxpython.org/wx.grid.GridCellBoolEditor.html
        """

    @staticmethod
    def IsTrueValue(value: str) -> bool:
        """ Returns True if the given value  is equal to the string representation of the truth value we currently use (see UseStringValues ).

            Source: https://docs.wxpython.org/wx.grid.GridCellBoolEditor.html
        """

    @staticmethod
    def UseStringValues(valueTrue="1", valueFalse="") -> None:
        """ This method allows you to customize the values returned by GetValue   for the cell using this editor.

            Source: https://docs.wxpython.org/wx.grid.GridCellBoolEditor.html
        """



class GridCellChoiceEditor(GridCellEditor):
    """ Grid cell editor for string data providing the user a choice from a
list of strings.

        Source: https://docs.wxpython.org/wx.grid.GridCellChoiceEditor.html
    """
    def __init__(self, choices, allowOthers=False) -> None:
        """ Choice cell renderer constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellChoiceEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ End editing the cell.

            Source: https://docs.wxpython.org/wx.grid.GridCellChoiceEditor.html
        """

    def SetParameters(self, params: str) -> None:
        """ Parameters string format is âitem1[,item2[â¦,itemN]]â.

            Source: https://docs.wxpython.org/wx.grid.GridCellChoiceEditor.html
        """



class GridCellFloatEditor(GridCellTextEditor):
    """ The editor for floating point numbers data.

        Source: https://docs.wxpython.org/wx.grid.GridCellFloatEditor.html
    """
    def __init__(self, width=-1, precision=-1, format=GRID_FLOAT_FORMAT_DEFAULT) -> None:
        """ Float cell editor constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellFloatEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ End editing the cell.

            Source: https://docs.wxpython.org/wx.grid.GridCellFloatEditor.html
        """

    def SetParameters(self, params: str) -> None:
        """ The parameters string format is âwidth[,precision[,format]]â where  format   should be chosen between f|e|g|E|G (f is used by default)

            Source: https://docs.wxpython.org/wx.grid.GridCellFloatEditor.html
        """



class GridCellNumberEditor(GridCellTextEditor):
    """ Grid cell editor for numeric integer data.

        Source: https://docs.wxpython.org/wx.grid.GridCellNumberEditor.html
    """
    def __init__(self, min=-1, max=-1) -> None:
        """ Allows you to specify the range for acceptable data.

            Source: https://docs.wxpython.org/wx.grid.GridCellNumberEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ End editing the cell.

            Source: https://docs.wxpython.org/wx.grid.GridCellNumberEditor.html
        """

    def SetParameters(self, params: str) -> None:
        """ Parameters string format is âmin,maxâ.

            Source: https://docs.wxpython.org/wx.grid.GridCellNumberEditor.html
        """



class GridCellTextEditor(GridCellEditor):
    """ Grid cell editor for string/text data.

        Source: https://docs.wxpython.org/wx.grid.GridCellTextEditor.html
    """
    def __init__(self, maxChars: int=0) -> None:
        """ Text cell editor constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellTextEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ End editing the cell.

            Source: https://docs.wxpython.org/wx.grid.GridCellTextEditor.html
        """

    def SetParameters(self, params: str) -> None:
        """ The parameters string format is ânâ where n is a number representing the maximum width.

            Source: https://docs.wxpython.org/wx.grid.GridCellTextEditor.html
        """

    def SetValidator(self, validator: 'Validator') -> None:
        """ Set validator to validate user input.

            Source: https://docs.wxpython.org/wx.grid.GridCellTextEditor.html
        """



class GridCellDateEditor(GridCellEditor):
    """ Grid cell editor for dates.

        Source: https://docs.wxpython.org/wx.grid.GridCellDateEditor.html
    """
    def __init__(self, format: str="") -> None:
        """ Date editor constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellDateEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ End editing the cell.

            Source: https://docs.wxpython.org/wx.grid.GridCellDateEditor.html
        """



class GridEvent(NotifyEvent):
    """ This event class contains information about various grid events.

        Source: https://docs.wxpython.org/wx.grid.GridEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def AltDown(self) -> bool:
        """ Returns True if the Alt key was down at the time of the event.

            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def ControlDown(self) -> bool:
        """ Returns True if the Control key was down at the time of the event.

            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def GetCol(self) -> int:
        """ Column at which the event occurred.

            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def GetPosition(self) -> 'Point':
        """ Position in pixels at which the event occurred.

            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def GetRow(self) -> int:
        """ Row at which the event occurred.

            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def MetaDown(self) -> bool:
        """ Returns True if the Meta key was down at the time of the event.

            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def Selecting(self) -> bool:
        """ Returns True if the user is selecting grid cells, or False if deselecting.

            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def ShiftDown(self) -> bool:
        """ Returns True if the Shift key was down at the time of the event.

            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    Col: int  # See GetCol
    Position: 'Point'  # See GetPosition
    Row: int  # See GetRow



EVT_GRID_CELL_CHANGING: int  # The user is about to change the data in a cell. The new cell value as string is available from GetString  event object method. This event can be vetoed if the change is not allowed. Processes a  wxEVT_GRID_CELL_CHANGING   event type.

EVT_GRID_CELL_CHANGED: int  # The user changed the data in a cell. The old cell value as string is available from GetString  event object method. Notice that vetoing this event still works for backwards compatibility reasons but any new code should only veto EVT_GRID_CELL_CHANGING event and not this one. Processes a  wxEVT_GRID_CELL_CHANGED   event type.

EVT_GRID_CELL_LEFT_CLICK: int  # The user clicked a cell with the left mouse button. Processes a  wxEVT_GRID_CELL_LEFT_CLICK   event type.

EVT_GRID_CELL_LEFT_DCLICK: int  # The user double-clicked a cell with the left mouse button. Processes a  wxEVT_GRID_CELL_LEFT_DCLICK   event type.

EVT_GRID_CELL_RIGHT_CLICK: int  # The user clicked a cell with the right mouse button. Processes a  wxEVT_GRID_CELL_RIGHT_CLICK   event type.

EVT_GRID_CELL_RIGHT_DCLICK: int  # The user double-clicked a cell with the right mouse button. Processes a  wxEVT_GRID_CELL_RIGHT_DCLICK   event type.

EVT_GRID_EDITOR_HIDDEN: int  # The editor for a cell was hidden. Processes a  wxEVT_GRID_EDITOR_HIDDEN   event type.

EVT_GRID_EDITOR_SHOWN: int  # The editor for a cell was shown. Processes a  wxEVT_GRID_EDITOR_SHOWN   event type.

EVT_GRID_LABEL_LEFT_CLICK: int  # The user clicked a label with the left mouse button. Processes a  wxEVT_GRID_LABEL_LEFT_CLICK   event type.

EVT_GRID_LABEL_LEFT_DCLICK: int  # The user double-clicked a label with the left mouse button. Processes a  wxEVT_GRID_LABEL_LEFT_DCLICK   event type.

EVT_GRID_LABEL_RIGHT_CLICK: int  # The user clicked a label with the right mouse button. Processes a  wxEVT_GRID_LABEL_RIGHT_CLICK   event type.

EVT_GRID_LABEL_RIGHT_DCLICK: int  # The user double-clicked a label with the right mouse button. Processes a  wxEVT_GRID_LABEL_RIGHT_DCLICK   event type.

EVT_GRID_SELECT_CELL: int  # The given cell was made current, either by user or by the program via a call to SetGridCursor() or GoToCell(). Processes a  wxEVT_GRID_SELECT_CELL   event type.

EVT_GRID_ROW_MOVE: int  # The user tries to change the order of the rows in the grid by dragging the row specified by GetRow. This event can be vetoed to either prevent the user from reordering the row change completely (but notice that if you donât want to allow it at all, you simply shouldnât call wx.grid.Grid.EnableDragRowMove   in the first place), vetoed but handled in some way in the handler, e.g. by really moving the row to the new position at the associated table level, or allowed to proceed in which case wx.grid.Grid.SetRowPos   is used to reorder the rows display order without affecting the use of the row indices otherwise. This event macro corresponds to  wxEVT_GRID_ROW_MOVE   event type. It is only available since wxWidgets 3.1.7.

EVT_GRID_COL_MOVE: int  # The user tries to change the order of the columns in the grid by dragging the column specified by GetCol. This event can be vetoed to either prevent the user from reordering the column change completely (but notice that if you donât want to allow it at all, you simply shouldnât call wx.grid.Grid.EnableDragColMove   in the first place), vetoed but handled in some way in the handler, e.g. by really moving the column to the new position at the associated table level, or allowed to proceed in which case wx.grid.Grid.SetColPos   is used to reorder the columns display order without affecting the use of the column indices otherwise. This event macro corresponds to  wxEVT_GRID_COL_MOVE   event type.

EVT_GRID_COL_SORT: int  # This event is generated when a column is clicked by the user and its name is explained by the fact that the custom reaction to a click on a column is to sort the grid contents by this column. However the grid itself has no special support for sorting and itâs up to the handler of this event to update the associated table. But if the event is handled (and not vetoed) the grid supposes that the table was indeed resorted and updates the column to indicate the new sort order and refreshes itself. This event macro corresponds to  wxEVT_GRID_COL_SORT   event type.

EVT_GRID_TABBING: int  # This event is generated when the user presses TAB or Shift-TAB in the grid. It can be used to customize the simple default TAB handling logic, e.g. to go to the next non-empty cell instead of just the next cell. See also wx.grid.Grid.SetTabBehaviour . This event is new since wxWidgets 2.9.5. ^^

class GridSizeEvent(NotifyEvent):
    """ This event class contains information about a row/column resize event.

        Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    def AltDown(self) -> bool:
        """ Returns True if the Alt key was down at the time of the event.

            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    def ControlDown(self) -> bool:
        """ Returns True if the Control key was down at the time of the event.

            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    def GetPosition(self) -> 'Point':
        """ Position in pixels at which the event occurred.

            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    def GetRowOrCol(self) -> int:
        """ Row or column at that was resized.

            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    def MetaDown(self) -> bool:
        """ Returns True if the Meta key was down at the time of the event.

            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    def ShiftDown(self) -> bool:
        """ Returns True if the Shift key was down at the time of the event.

            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    Position: 'Point'  # See GetPosition
    RowOrCol: int  # See GetRowOrCol



EVT_GRID_CMD_COL_SIZE: int  # The user resized a column, corresponds to  wxEVT_GRID_COL_SIZE   event type.

EVT_GRID_CMD_ROW_SIZE: int  # The user resized a row, corresponds to  wxEVT_GRID_ROW_SIZE   event type.

EVT_GRID_ROW_AUTO_SIZE: int  # This event is sent when a row must be resized to its best size, e.g. when the user double clicks the row divider. The default implementation simply resizes the row to fit the row label (but not its contents as this could be too slow for big grids). This macro corresponds to  wxEVT_GRID_ROW_AUTO_SIZE   event type and is new since wxWidgets 3.1.7.

EVT_GRID_COL_SIZE: int  # Same as EVT_GRID_CMD_COL_SIZE() but uses  ID_ANY   id.

EVT_GRID_COL_AUTO_SIZE: int  # This event is sent when a column must be resized to its best size, e.g. when the user double clicks the column divider. The default implementation simply resizes the column to fit the column label (but not its contents as this could be too slow for big grids). This macro corresponds to  wxEVT_GRID_COL_AUTO_SIZE   event type and is new since wxWidgets 2.9.5.

EVT_GRID_ROW_SIZE: int  # Same as EVT_GRID_CMD_ROW_SIZE() but uses  ID_ANY   id. ^^

class GridRangeSelectEvent(NotifyEvent):
    """ Events of this class notify about a range of cells being selected.

        Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def AltDown(self) -> bool:
        """ Returns True if the Alt key was down at the time of the event.

            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def ControlDown(self) -> bool:
        """ Returns True if the Control key was down at the time of the event.

            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def GetBottomRightCoords(self) -> 'grid.GridCellCoords':
        """ Top left corner of the rectangular area that was (de)selected.

            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def GetBottomRow(self) -> int:
        """ Bottom row of the rectangular area that was (de)selected.

            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def GetLeftCol(self) -> int:
        """ Left column of the rectangular area that was (de)selected.

            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def GetRightCol(self) -> int:
        """ Right column of the rectangular area that was (de)selected.

            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def GetTopLeftCoords(self) -> 'grid.GridCellCoords':
        """ Top left corner of the rectangular area that was (de)selected.

            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def GetTopRow(self) -> int:
        """ Top row of the rectangular area that was (de)selected.

            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def MetaDown(self) -> bool:
        """ Returns True if the Meta key was down at the time of the event.

            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def Selecting(self) -> bool:
        """ Returns True if the area was selected, False otherwise.

            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def ShiftDown(self) -> bool:
        """ Returns True if the Shift key was down at the time of the event.

            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    BottomRightCoords: 'grid.GridCellCoords'  # See GetBottomRightCoords
    BottomRow: int  # See GetBottomRow
    LeftCol: int  # See GetLeftCol
    RightCol: int  # See GetRightCol
    TopLeftCoords: 'grid.GridCellCoords'  # See GetTopLeftCoords
    TopRow: int  # See GetTopRow



EVT_GRID_RANGE_SELECTING: int  # The user is selecting a group of contiguous cells. Processes a  wxEVT_GRID_RANGE_SELECTING   event type. This event is available in wxWidgets 3.1.5 and later only.

EVT_GRID_CMD_RANGE_SELECTING: int  # The user is selecting a group of contiguous cells; variant taking a window identifier. Processes a  wxEVT_GRID_RANGE_SELECTING   event type. This event is available in wxWidgets 3.1.5 and later only.

EVT_GRID_RANGE_SELECTED: int  # The user selected a group of contiguous cells. Processes a  wxEVT_GRID_RANGE_SELECTED   event type. This event is available in wxWidgets 3.1.5 and later only and was called   wxEVT_GRID_RANGE_SELECT   in the previous versions.

EVT_GRID_CMD_RANGE_SELECTED: int  # The user selected a group of contiguous cells; variant taking a window identifier. Processes a  wxEVT_GRID_RANGE_SELECTED   event type. This event is available in wxWidgets 3.1.5 and later only and was called   wxEVT_GRID_CMD_RANGE_SELECT   in the previous versions. ^^

class GridUpdateLocker:
    """ This small class can be used to prevent Grid from redrawing during
its lifetime by calling Grid.BeginBatch() in its constructor and
Grid.EndBatch() in its destructor.

        Source: https://docs.wxpython.org/wx.grid.GridUpdateLocker.html
    """
    def __init__(self, grid: Optional['grid.Grid']=None) -> None:
        """ Creates an object preventing the updates of the specified grid.

            Source: https://docs.wxpython.org/wx.grid.GridUpdateLocker.html
        """

    def Create(self, grid: 'grid.Grid') -> None:
        """ This method can be called if the object had been constructed using the default constructor.

            Source: https://docs.wxpython.org/wx.grid.GridUpdateLocker.html
        """

    def __enter__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.grid.GridUpdateLocker.html
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.grid.GridUpdateLocker.html
        """



class GridCellCoords:
    """ Represents coordinates of a grid cell.

        Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def Get(self) -> tuple:
        """ Return the row and col properties as a tuple.

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def GetCol(self) -> int:
        """ Return the column of the coordinate.

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def GetIM(self) -> None:
        """ Returns an immutable representation of the wx.GridCellCoords object, based on namedtuple.

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def GetRow(self) -> int:
        """ Return the row of the coordinate.

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def Set(self, row, col) -> None:
        """ Set the row and column of the coordinate.

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def SetCol(self, n: int) -> None:
        """ Set the column of the coordinate.

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def SetRow(self, n: int) -> None:
        """ Set the row of the coordinate.

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __bool__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __getitem__(self, idx) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __len__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __nonzero__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __reduce__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __repr__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __setitem__(self, idx, val) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __str__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __ne__(self, item: Any) -> bool:
        """ Inequality operator.

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.

            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    Col: int  # See GetCol and SetCol
    Row: int  # See GetRow and SetRow



class GridFitMode:
    """ Allows to specify the behaviour when the cell contents doesnât fit
into its allotted space.

        Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
    """
    def __init__(self) -> None:
        """ Default constructor creates an object not specifying any behaviour.

            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    @staticmethod
    def Clip() -> 'grid.GridFitMode':
        """ Pseudo-constructor for object specifying clipping behaviour.

            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    @staticmethod
    def Ellipsize(ellipsize: EllipsizeMode=ELLIPSIZE_END) -> 'grid.GridFitMode':
        """ Pseudo-constructor for object specifying ellipsize behaviour.

            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    def GetEllipsizeMode(self) -> 'EllipsizeMode':
        """ Return ellipsize mode, possibly  ELLIPSIZE_NONE .

            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    def IsClip(self) -> bool:
        """ Return True if the object specifies clipping behaviour.

            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    def IsOverflow(self) -> bool:
        """ Return True if the object specifies overflow behaviour.

            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    def IsSpecified(self) -> bool:
        """ Return True if the object specifies some particular behaviour.

            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    @staticmethod
    def Overflow() -> 'grid.GridFitMode':
        """ Pseudo-constructor for object specifying overflow behaviour.

            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    EllipsizeMode: '_EllipsizeMode'  # See GetEllipsizeMode



class GridSizesInfo:
    """ GridSizesInfo stores information about sizes of all Grid rows or
columns.

        Source: https://docs.wxpython.org/wx.grid.GridSizesInfo.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.GridSizesInfo.html
        """

    def GetSize(self, pos: Any) -> int:
        """ Get the element size.

            Source: https://docs.wxpython.org/wx.grid.GridSizesInfo.html
        """

    m_sizeDefault: Any  # A public C++ attribute of type int. Default size.



class GridBlocks:
    """ Represents a collection of grid blocks that can be iterated over.

        Source: https://docs.wxpython.org/wx.grid.GridBlocks.html
    """
    def __iter__(self) -> None:
        """ Returns a Python iterator for accessing the collection of grid blocks.

            Source: https://docs.wxpython.org/wx.grid.GridBlocks.html
        """

    def begin(self) -> 'grid.GridBlocks.iterator':
        """ Return iterator corresponding to the beginning of the range.

            Source: https://docs.wxpython.org/wx.grid.GridBlocks.html
        """

    def end(self) -> 'grid.GridBlocks.iterator':
        """ Return iterator corresponding to the end of the range.

            Source: https://docs.wxpython.org/wx.grid.GridBlocks.html
        """



class GridTableMessage:
    """ Message class used by the grid table to send requests and
notifications to the grid view.

        Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def GetCommandInt(self) -> int:
        """ Get the position after which the insertion/deletion occur.

            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def GetCommandInt2(self) -> int:
        """ Get the number of rows to be inserted/deleted.

            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def GetId(self) -> int:
        """ Gets an id.

            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def GetTableObject(self) -> 'grid.GridTableBase':
        """ Gets the table object.

            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def SetCommandInt(self, comInt1: int) -> None:
        """ Set the position after which the insertion/deletion occur.

            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def SetCommandInt2(self, comInt2: int) -> None:
        """ Set the number of rows to be inserted/deleted.

            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def SetId(self, id: int) -> None:
        """ Sets an id.

            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def SetTableObject(self, table: 'grid.GridTableBase') -> None:
        """ Sets the table object.

            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    CommandInt: int  # See GetCommandInt and SetCommandInt
    CommandInt2: int  # See GetCommandInt2 and SetCommandInt2
    Id: int  # See GetId and SetId
    TableObject: 'grid.GridTableBase'  # See GetTableObject and SetTableObject



class GridColumnHeaderRendererDefault(GridColumnHeaderRenderer):
    """ Default column header renderer.

        Source: https://docs.wxpython.org/wx.grid.GridColumnHeaderRendererDefault.html
    """
    def DrawBorder(self, grid, dc, rect) -> None:
        """ Implement border drawing for the column labels.

            Source: https://docs.wxpython.org/wx.grid.GridColumnHeaderRendererDefault.html
        """



class GridColumnHeaderRenderer(GridHeaderLabelsRenderer):
    """ Base class for column headers renderer.

        Source: https://docs.wxpython.org/wx.grid.GridColumnHeaderRenderer.html
    """


class GridCornerHeaderRendererDefault(GridCornerHeaderRenderer):
    """ Default corner window renderer.

        Source: https://docs.wxpython.org/wx.grid.GridCornerHeaderRendererDefault.html
    """
    def DrawBorder(self, grid, dc, rect) -> None:
        """ Implement border drawing for the corner window.

            Source: https://docs.wxpython.org/wx.grid.GridCornerHeaderRendererDefault.html
        """



class GridCornerHeaderRenderer(GridHeaderLabelsRenderer):
    """ Base class for corner header renderer.

        Source: https://docs.wxpython.org/wx.grid.GridCornerHeaderRenderer.html
    """


class GridRowHeaderRendererDefault(GridRowHeaderRenderer):
    """ Default row header renderer.

        Source: https://docs.wxpython.org/wx.grid.GridRowHeaderRendererDefault.html
    """
    def DrawBorder(self, grid, dc, rect) -> None:
        """ Implement border drawing for the row labels.

            Source: https://docs.wxpython.org/wx.grid.GridRowHeaderRendererDefault.html
        """



class GridRowHeaderRenderer(GridHeaderLabelsRenderer):
    """ Base class for row headers renderer.

        Source: https://docs.wxpython.org/wx.grid.GridRowHeaderRenderer.html
    """


class GridCellAutoWrapStringRenderer(GridCellStringRenderer):
    """ This class may be used to format string data in a cell.

        Source: https://docs.wxpython.org/wx.grid.GridCellAutoWrapStringRenderer.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellAutoWrapStringRenderer.html
        """



class GridCellEnumRenderer(GridCellStringRenderer):
    """ This class may be used to render in a cell a number as a textual
equivalent.

        Source: https://docs.wxpython.org/wx.grid.GridCellEnumRenderer.html
    """
    def __init__(self, choices: str="") -> None:
        """ Enum renderer constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellEnumRenderer.html
        """

    def SetParameters(self, params: str) -> None:
        """ Sets the comma separated string content of the enum.

            Source: https://docs.wxpython.org/wx.grid.GridCellEnumRenderer.html
        """



GridCellFloatFormat: TypeAlias = int  # Enumeration

GRID_FLOAT_FORMAT_FIXED: int

GRID_FLOAT_FORMAT_SCIENTIFIC: int

GRID_FLOAT_FORMAT_COMPACT: int

GRID_FLOAT_FORMAT_UPPER: int

GRID_FLOAT_FORMAT_DEFAULT: int

class GridCellActivatableEditor(GridCellEditor):
    """ Base class for activatable editors.

        Source: https://docs.wxpython.org/wx.grid.GridCellActivatableEditor.html
    """
    def DoActivate(self, row, col, grid) -> None:
        """ Same method as in   wx.grid.GridCellEditor, but pure virtual.

            Source: https://docs.wxpython.org/wx.grid.GridCellActivatableEditor.html
        """

    def TryActivate(self, row, col, grid, actSource) -> 'grid.GridActivationResult':
        """ Same method as in   wx.grid.GridCellEditor, but pure virtual.

            Source: https://docs.wxpython.org/wx.grid.GridCellActivatableEditor.html
        """



class GridCellAutoWrapStringEditor(GridCellTextEditor):
    """ Grid cell editor for wrappable string/text data.

        Source: https://docs.wxpython.org/wx.grid.GridCellAutoWrapStringEditor.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.grid.GridCellAutoWrapStringEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ End editing the cell.

            Source: https://docs.wxpython.org/wx.grid.GridCellAutoWrapStringEditor.html
        """



class GridCellEnumEditor(GridCellChoiceEditor):
    """ Grid cell editor which displays an enum number as a textual equivalent
(e.g.

        Source: https://docs.wxpython.org/wx.grid.GridCellEnumEditor.html
    """
    def __init__(self, choices: str="") -> None:
        """ Enum cell editor constructor.

            Source: https://docs.wxpython.org/wx.grid.GridCellEnumEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ End editing the cell.

            Source: https://docs.wxpython.org/wx.grid.GridCellEnumEditor.html
        """



class GridActivationSource:
    """ Represents a source of cell activation, which may be either a user
event (mouse or keyboard) or the program itself.

        Source: https://docs.wxpython.org/wx.grid.GridActivationSource.html
    """
    def GetKeyEvent(self) -> 'KeyEvent':
        """ Get the key event corresponding to the key press activating the cell.

            Source: https://docs.wxpython.org/wx.grid.GridActivationSource.html
        """

    def GetMouseEvent(self) -> 'MouseEvent':
        """ Get the mouse event corresponding to the click activating the cell.

            Source: https://docs.wxpython.org/wx.grid.GridActivationSource.html
        """

    def GetOrigin(self) -> 'grid.GridActivationSource.Origin':
        """ Get the origin of the activation.

            Source: https://docs.wxpython.org/wx.grid.GridActivationSource.html
        """

    KeyEvent: '_KeyEvent'  # See GetKeyEvent
    MouseEvent: '_MouseEvent'  # See GetMouseEvent



class GridActivationResult:
    """ Represents the result of GridCellEditor.TryActivate().

        Source: https://docs.wxpython.org/wx.grid.GridActivationResult.html
    """
    @staticmethod
    def DoChange(newval: str) -> 'grid.GridActivationResult':
        """ Indicate that activating the cell is possible and would change its value to the given one.

            Source: https://docs.wxpython.org/wx.grid.GridActivationResult.html
        """

    @staticmethod
    def DoEdit() -> 'grid.GridActivationResult':
        """ Indicate that the editor control should be shown and the cell should be edited normally.

            Source: https://docs.wxpython.org/wx.grid.GridActivationResult.html
        """

    @staticmethod
    def DoNothing() -> 'grid.GridActivationResult':
        """ Indicate that nothing should be done and the cell shouldnât be edited at all.

            Source: https://docs.wxpython.org/wx.grid.GridActivationResult.html
        """



class GridHeaderLabelsRenderer:
    """ Base class for header cells renderers.

        Source: https://docs.wxpython.org/wx.grid.GridHeaderLabelsRenderer.html
    """
    def DrawBorder(self, grid, dc, rect) -> None:
        """ Called by the grid to draw the border around the cell header.

            Source: https://docs.wxpython.org/wx.grid.GridHeaderLabelsRenderer.html
        """

    def DrawLabel(self, grid, dc, value, rect, horizAlign, vertAlign, textOrientation) -> None:
        """ Called by the grid to draw the specified label.

            Source: https://docs.wxpython.org/wx.grid.GridHeaderLabelsRenderer.html
        """



GridCellCoordsArray: TypeAlias = list['GridCellCoords']

GridSelectionModes: TypeAlias = int

AttrKind: TypeAlias = int

GridWindow: TypeAlias = Any

GridCellAttrPtr: TypeAlias = Any

TabBehaviour: TypeAlias = int  # Enumeration

