# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class AuiToolBar(Control):
    """ AuiToolBar is a completely owner-drawn toolbar perfectly integrated with the AUI layout system.
This allows drag and drop of toolbars, docking/floating behaviour and the possibility to define
âoverflowâ items in the toolbar itself.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=AUI_TB_DEFAULT_STYLE) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddCheckTool(self, tool_id, label, bitmap, disabled_bitmap, short_help_string="", long_help_string="", client_data=None) -> None:
        """ Adds a new check (or toggle) tool to the AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddControl(self, control, label="") -> None:
        """ Adds any control to the toolbar, typically e.g. a ComboBox.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddLabel(self, tool_id, label="", width=0) -> None:
        """ Adds a label tool to the AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddRadioTool(self, tool_id, label, bitmap, disabled_bitmap, short_help_string="", long_help_string="", client_data=None) -> None:
        """ Adds a new radio tool to the toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddSeparator(self) -> None:
        """ Adds a separator for spacing groups of tools.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddSimpleTool(self, tool_id, label, bitmap, short_help_string="", kind=ITEM_NORMAL, target=None) -> None:
        """ Adds a tool to the toolbar. This is the simplest method you can use to
add an item to the AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddSpacer(self, pixels: int) -> None:
        """ Adds a spacer for spacing groups of tools.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddStretchSpacer(self, proportion: int=1) -> None:
        """ Adds a stretchable spacer for spacing groups of tools.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddToggleTool(self, tool_id, bitmap, disabled_bitmap, toggle=False, client_data=None, short_help_string="", long_help_string="") -> None:
        """ Adds a toggle tool to the toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddTool(self, tool_id, label, bitmap, disabled_bitmap, kind, short_help_string='', long_help_string='', client_data=None, target=None) -> None:
        """ Adds a tool to the toolbar. This is the full feature version of AddTool.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def Clear(self) -> None:
        """ Deletes all the tools in the AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def ClearTools(self) -> None:
        """ Deletes all the tools in the AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def DeleteTool(self, tool_id: int) -> None:
        """ Removes the specified tool from the toolbar and deletes it.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def DeleteToolByPos(self, pos: int) -> None:
        """ This function behaves like DeleteTool but it deletes the tool at the specified position and not the one with the given id.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def DoGetBestSize(self) -> None:
        """ Gets the size which best suits the window: for a control, it would be the
minimal size which doesnât truncate the control, for a panel - the same
size as it would have after a call to Fit().

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def DoIdleUpdate(self) -> None:
        """ Updates the toolbar during idle times.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def DoSetSize(self, x, y, width, height, sizeFlags=wx.SIZE_AUTO) -> None:
        """ Sets the position and size of the window in pixels. The sizeFlags
parameter indicates the interpretation of the other params if they are
equal to -1.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def EnableTool(self, tool_id, state) -> None:
        """ Enables or disables the tool.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def FindControl(self, id: int) -> None:
        """ Returns a pointer to the control identified by id or None if no corresponding control is found.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def FindTool(self, tool_id: int) -> None:
        """ Finds a tool for the given tool id.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def FindToolByIndex(self, pos: int) -> None:
        """ Finds a tool for the given tool position in the AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def FindToolByLabel(self, label: str) -> None:
        """ Finds a tool for the given label.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def FindToolForPosition(self, x, y) -> None:
        """ Finds a tool for the given mouse position.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def FindToolForPositionWithPacking(self, x, y) -> None:
        """ Finds a tool for the given mouse position, taking into account also the tool packing.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetAGWWindowStyleFlag(self) -> None:
        """ Returns the AGW-specific window style flag.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetArtProvider(self) -> None:
        """ Returns the current art provider being used.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetAuiManager(self) -> None:
        """ Returns the AuiManager which manages the toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetGripperVisible(self) -> None:
        """ Returns whether the toolbar gripper is visible or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetLabelSize(self, label: str) -> None:
        """ Returns the standard size of a toolbar item.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetOverflowRect(self) -> None:
        """ Returns the rectangle of the overflow button.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetOverflowState(self) -> None:
        """ Returns the state of the overflow button.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetOverflowVisible(self) -> None:
        """ Returns whether the overflow button is visible or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolBarFits(self) -> None:
        """ Returns whether the AuiToolBar size fits in a specified size.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolBitmap(self, tool_id: int) -> None:
        """ Returns the tool bitmap for the tool identified by tool_id.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolBitmapSize(self) -> None:
        """ Returns the size of bitmap that the toolbar expects to have. The default bitmap size is 16 by 15 pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolBorderPadding(self) -> None:
        """ Returns the padding between the tool border and the label, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolCount(self) -> None:
        """ Returns the number of tools in the AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolDropDown(self, tool_id: int) -> None:
        """ Returns whether the toolbar item identified by tool_id has an associated drop down window menu or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolEnabled(self, tool_id: int) -> None:
        """ Returns whether the tool identified by tool_id is enabled or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolFits(self, tool_id: int) -> None:
        """ Returns whether the tool identified by tool_id fits into the toolbar or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolFitsByIndex(self, tool_id: int) -> None:
        """ Returns whether the tool identified by tool_id fits into the toolbar or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolIndex(self, tool_id: int) -> None:
        """ Returns the position of the tool in the toolbar given its identifier.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolLabel(self, tool_id: int) -> None:
        """ Returns the tool label for the tool identified by tool_id.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolLongHelp(self, tool_id: int) -> None:
        """ Returns the long help for the given tool.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolOrientation(self) -> None:
        """ Returns the orientation for the toolbar items.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolPacking(self) -> None:
        """ Returns the value used for spacing tools. The default value is 1 pixel.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolPos(self, tool_id: int) -> None:
        """ Returns the position of the tool in the toolbar given its identifier.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolProportion(self, tool_id: int) -> None:
        """ Returns the tool proportion in the toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolRect(self, tool_id: int) -> None:
        """ Returns the toolbar item rectangle

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolSeparation(self) -> None:
        """ Returns the separator size for the toolbar, in pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolShortHelp(self, tool_id: int) -> None:
        """ Returns the short help for the given tool.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolSticky(self, tool_id: int) -> None:
        """ Returns whether the toolbar item identified by tool_id has a sticky behaviour or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolTextOrientation(self) -> None:
        """ Returns the label orientation for the toolbar items.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolToggled(self, tool_id: int) -> None:
        """ Returns whether a tool is toggled or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def HitTest(self, x, y) -> None:
        """ Finds a tool for the given mouse position.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def IsPaneMinimized(self) -> None:
        """ Returns whether this AuiToolBar contains a minimized pane tool.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnCustomRender(self, dc, item, rect) -> None:
        """ Handles custom render for single AuiToolBar items.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ Handles the wx.EVT_ERASE_BACKGROUND event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnIdle(self, event: IdleEvent) -> None:
        """ Handles the wx.EVT_IDLE event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnLeaveWindow(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEAVE_WINDOW event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnLeftDown(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEFT_DOWN event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnLeftUp(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEFT_UP event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnMiddleDown(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_MIDDLE_DOWN event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnMiddleUp(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_MIDDLE_UP event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnMotion(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_MOTION event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ Handles the wx.EVT_PAINT event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnRightDown(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_RIGHT_DOWN event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnRightUp(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_RIGHT_UP event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnSetCursor(self, event: SetCursorEvent) -> None:
        """ Handles the wx.EVT_SET_CURSOR event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ Handles the wx.EVT_SIZE event for AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def Realize(self) -> None:
        """ Realizes the toolbar. This function should be called after you have added tools.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def RefreshOverflowState(self) -> None:
        """ Refreshes the overflow button.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetAGWWindowStyleFlag(self, agwStyle: int) -> None:
        """ Sets the AGW-specific style of the window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetArtProvider(self, art: Any) -> None:
        """ Instructs AuiToolBar to use art provider specified by parameter art
for all drawing calls. This allows pluggable look-and-feel features.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetAuiManager(self, auiManager) -> None:
        """ Sets the AuiManager which manages the toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetCustomOverflowItems(self, prepend, append) -> None:
        """ Sets the two lists prepend and append as custom overflow items.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the AuiToolBar font.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetGripperVisible(self, visible: bool) -> None:
        """ Sets whether the toolbar gripper is visible or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetHoverItem(self, pitem: AuiToolBarItem) -> None:
        """ Sets a toolbar item to be currently hovered by the mouse.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetMargins(self, left=-1, right=-1, top=-1, bottom=-1) -> None:
        """ Set the values to be used as margins for the toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetMarginsSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Set the values to be used as margins for the toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetMarginsXY(self, x, y) -> None:
        """ Set the values to be used as margins for the toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetOrientation(self, orientation: int) -> None:
        """ Sets the toolbar orientation.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetOverflowVisible(self, visible: bool) -> None:
        """ Sets whether the overflow button is visible or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetPressedItem(self, pitem: AuiToolBarItem) -> None:
        """ Sets a toolbar item to be currently in a âpressedâ state.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolAlignment(self, alignment: int=wx.EXPAND) -> None:
        """ This sets the alignment for all of the tools within the toolbar
(only has an effect when the toolbar is expanded).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolBitmap(self, tool_id, bitmap) -> None:
        """ Sets the tool bitmap for the tool identified by tool_id.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolBitmapSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the default size of each tool bitmap. The default bitmap size is 16 by 15 pixels.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolBorderPadding(self, padding: int) -> None:
        """ Sets the padding between the tool border and the label.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolDisabledBitmap(self, tool_id, bitmap) -> None:
        """ Sets the tool disabled bitmap for the tool identified by tool_id.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolDropDown(self, tool_id, dropdown) -> None:
        """ Assigns a drop down window menu to the toolbar item.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolLabel(self, tool_id, label) -> None:
        """ Sets the tool label for the tool identified by tool_id.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolLongHelp(self, tool_id, help_string) -> None:
        """ Sets the long help for the given tool.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolNormalBitmap(self, tool_id, bitmap) -> None:
        """ Sets the tool bitmap for the tool identified by tool_id.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolOrientation(self, orientation: int) -> None:
        """ Sets the tool orientation for the toolbar items.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolPacking(self, packing: int) -> None:
        """ Sets the value used for spacing tools. The default value is 1 pixel.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolProportion(self, tool_id, proportion) -> None:
        """ Sets the tool proportion in the toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolSeparation(self, separation: int) -> None:
        """ Sets the separator size for the toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolShortHelp(self, tool_id, help_string) -> None:
        """ Sets the short help for the given tool.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolSticky(self, tool_id, sticky) -> None:
        """ Sets the toolbar item as sticky or non-sticky.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolTextOrientation(self, orientation: int) -> None:
        """ Sets the label orientation for the toolbar items.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetWindowStyleFlag(self, style: int) -> None:
        """ Sets the style of the window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def StartPreviewTimer(self) -> None:
        """ Starts a timer in AuiManager to slide-in/slide-out the minimized pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def StopPreviewTimer(self) -> None:
        """ Stops a timer in AuiManager to slide-in/slide-out the minimized pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def ToggleTool(self, tool_id, state) -> None:
        """ Toggles a tool on or off. This does not cause any event to get emitted.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """



EVT_ERASE_BACKGROUND: int

EVT_IDLE: int

EVT_LEAVE_WINDOW: int

EVT_LEFT_DOWN: int

EVT_LEFT_UP: int

EVT_MIDDLE_DOWN: int

EVT_MIDDLE_UP: int

EVT_MOTION: int

EVT_PAINT: int

EVT_RIGHT_DOWN: int

EVT_RIGHT_UP: int

EVT_SET_CURSOR: int

EVT_SIZE: int

SIZE_AUTO: int

SIZE_AUTO_WIDTH: int

SIZE_AUTO_HEIGHT: int

SIZE_USE_EXISTING: int

SIZE_ALLOW_MINUS_ONE: int

SIZE_FORCE: int

VERTICAL: int

HORIZONTAL: int

ALIGN_CENTER_HORIZONTAL: int

ALIGN_CENTER_VERTICAL: int

class AuiDefaultToolBarArt:
    """ Toolbar art provider code - a tab provider provides all drawing functionality to the AuiToolBar.
This allows the AuiToolBar to have a pluggable look-and-feel.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
    """
    def __init__(self) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def Clone(self) -> None:
        """ Clones the AuiDefaultToolBarArt art.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawBackground(self, dc, wnd, _rect, horizontal=True) -> None:
        """ Draws a toolbar background with a gradient shading.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawButton(self, dc, wnd, item, rect) -> None:
        """ Draws a toolbar item button.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawControlLabel(self, dc, wnd, item, rect) -> None:
        """ Draws a label for a toolbar control.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawDropDownButton(self, dc, wnd, item, rect) -> None:
        """ Draws a toolbar dropdown button.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawGripper(self, dc, wnd, rect) -> None:
        """ Draws the toolbar gripper.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawLabel(self, dc, wnd, item, rect) -> None:
        """ Draws a toolbar item label.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawOverflowButton(self, dc, wnd, rect, state) -> None:
        """ Draws the overflow button for the AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawPlainBackground(self, dc, wnd, _rect) -> None:
        """ Draws a toolbar background with a plain colour.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawSeparator(self, dc, wnd, _rect) -> None:
        """ Draws a toolbar separator.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetAGWFlags(self) -> None:
        """ Returns the AuiDefaultToolBarArt flags.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetElementSize(self, element_id: int) -> None:
        """ Returns the size of a UI element in the AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetFont(self) -> None:
        """ Returns the AuiDefaultToolBarArt font.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetLabelSize(self, dc, wnd, item) -> None:
        """ Returns the label size for a toolbar item.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetOrientation(self) -> None:
        """ Returns the toolbar orientation.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetTextOrientation(self) -> None:
        """ Returns the AuiDefaultToolBarArt text orientation.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetToolSize(self, dc, wnd, item) -> None:
        """ Returns the toolbar item size.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetToolsPosition(self, dc, item, rect) -> None:
        """ Returns the bitmap and text rectangles for a toolbar item.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def SetAGWFlags(self, agwFlags: int) -> None:
        """ Sets the toolbar art flags.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def SetDefaultColours(self, base_colour: Optional[Union[int, str, 'Colour']]=None) -> None:
        """ Sets the default colours, which are calculated from the given base colour.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def SetElementSize(self, element_id, size) -> None:
        """ Sets the size of a UI element in the AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the AuiDefaultToolBarArt font.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def SetOrientation(self, orientation: int) -> None:
        """ Sets the toolbar tool orientation.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def SetTextOrientation(self, orientation: int) -> None:
        """ Sets the text orientation.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def ShowDropDown(self, wnd, items) -> None:
        """ Shows the drop down window menu for overflow items.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """



class AuiToolBarItem:
    """ AuiToolBarItem is a toolbar element.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
    """
    def __init__(self, item: Optional[AuiToolBarItem]=None) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def Assign(self, c: AuiToolBarItem) -> None:
        """ Assigns the properties of the AuiToolBarItem c to self.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetAlignment(self) -> None:
        """ Returns the toolbar item alignment.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetBitmap(self) -> None:
        """ Returns the toolbar item bitmap.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetDisabledBitmap(self) -> None:
        """ Returns the toolbar item disabled bitmap.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetHoverBitmap(self) -> None:
        """ Returns the toolbar item hover bitmap.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetId(self) -> None:
        """ Returns the toolbar item identifier.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetKind(self) -> None:
        """ Returns the toolbar item kind.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetLabel(self) -> None:
        """ Returns the toolbar item label.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetLongHelp(self) -> None:
        """ Returns the long help string for the AuiToolBarItem.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetMinSize(self) -> None:
        """ Returns the toolbar item minimum size.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetOrientation(self) -> None:
        """ Returns the toolbar tool orientation.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetProportion(self) -> None:
        """ Returns the AuiToolBarItem proportion in the toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetRotatedBitmap(self, disabled: bool) -> None:
        """ Returns the correct bitmap depending on the tool orientation.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetShortHelp(self) -> None:
        """ Returns the short help string for the AuiToolBarItem.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetSizerItem(self) -> None:
        """ Returns the associated sizer item.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetSpacerPixels(self) -> None:
        """ Returns the number of pixels for a toolbar item with kind = ITEM_SEPARATOR.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetState(self) -> None:
        """ Returns the toolbar item state.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetUserData(self) -> None:
        """ Returns the associated user data.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetWindow(self) -> None:
        """ Returns window associated to the toolbar item.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def HasDropDown(self) -> None:
        """ Returns whether the toolbar item has an associated dropdown menu or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def IsActive(self) -> None:
        """ Returns whether the toolbar item is active or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def IsSticky(self) -> None:
        """ Returns whether the toolbar item has a sticky behaviour or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetActive(self, b: bool) -> None:
        """ Activates/deactivates the toolbar item.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetAlignment(self, align: int) -> None:
        """ Sets the toolbar item alignment.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetBitmap(self, bmp: 'Bitmap') -> None:
        """ Sets the toolbar item bitmap.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetDisabledBitmap(self, bmp: 'Bitmap') -> None:
        """ Sets the toolbar item disabled bitmap.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetHasDropDown(self, b: bool) -> None:
        """ Sets whether the toolbar item has an associated dropdown menu.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetHoverBitmap(self, bmp: 'Bitmap') -> None:
        """ Sets the toolbar item hover bitmap.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetId(self, new_id: int) -> None:
        """ Sets the toolbar item identifier.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetKind(self, new_kind: int) -> None:
        """ Sets the AuiToolBarItem kind.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetLabel(self, s: str) -> None:
        """ Sets the toolbar item label.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetLongHelp(self, s: str) -> None:
        """ Sets the long help string for the toolbar item. This string is shown in the
statusbar (if any) of the parent frame when the mouse pointer is inside the
tool.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetMinSize(self, s: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the toolbar item minimum size.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetOrientation(self, a: int) -> None:
        """ Sets the toolbar tool orientation.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetProportion(self, p: int) -> None:
        """ Sets the AuiToolBarItem proportion in the toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetShortHelp(self, s: str) -> None:
        """ Sets the short help string for the AuiToolBarItem, to be displayed in a
ToolTip when the mouse hover over the toolbar item.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetSizerItem(self, s: 'SizerItem') -> None:
        """ Associates a sizer item to this toolbar item.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetSpacerPixels(self, s: int) -> None:
        """ Sets the number of pixels for a toolbar item with kind = ITEM_SEPARATOR.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetState(self, new_state: AUI_BUTTON_STATE_NORMAL) -> None:
        """ Sets the toolbar item state.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetSticky(self, b: bool) -> None:
        """ Sets whether the toolbar item is sticky (permanent highlight after mouse enter)
or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetUserData(self, data: Any) -> None:
        """ Associates some kind of user data to the toolbar item.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetWindow(self, w: 'Window') -> None:
        """ Assigns a window to the toolbar item.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """



AUI_BUTTON_STATE_NORMAL: int

AUI_BUTTON_STATE_HOVER: int

AUI_BUTTON_STATE_PRESSED: int

AUI_BUTTON_STATE_DISABLED: int

AUI_BUTTON_STATE_HIDDEN: int

AUI_BUTTON_STATE_CHECKED: int

