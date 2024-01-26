# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class AuiManager(EvtHandler):
    """ AuiManager manages the panes associated with it for a particular wx.Frame,
using a paneâs AuiManager information to determine each paneâs docking and
floating behavior. AuiManager uses wxPythonâs sizer mechanism to plan the
layout of each frame. It uses a replaceable dock art class to do all drawing,
so all drawing is localized in one area, and may be customized depending on an
applicationsâ specific needs.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
    """
    def __init__(self, managed_window=None, agwFlags=None) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def ActivatePane(self, window: 'Window') -> None:
        """ Activates the pane to which window is associated.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def AddPane(self, window, arg1=None, arg2=None, target=None) -> None:
        """ Tells the frame manager to start managing a child window. There
are four versions of this function. The first version allows the full spectrum
of pane parameter possibilities ( AddPane1). The second version is used for
simpler user interfaces which do not require as much configuration ( AddPane2).
The AddPane3 version allows a drop position to be specified, which will determine
where the pane will be added. The AddPane4 version allows to turn the target
AuiPaneInfo pane into a notebook and the added pane into a page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def AddPane1(self, window, pane_info) -> None:
        """ See comments on AddPane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def AddPane2(self, window, direction, caption) -> None:
        """ See comments on AddPane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def AddPane3(self, window, pane_info, drop_pos) -> None:
        """ See comments on AddPane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def AddPane4(self, window, pane_info, target) -> None:
        """ See comments on AddPane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def AnimateDocking(self, win_rect, pane_rect) -> None:
        """ Animates the minimization/docking of a pane a la Eclipse, using a ScreenDC
to draw a âmoving docking rectangleâ on the screen.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CalculateDockSizerLimits(self, dock: AuiDockInfo) -> None:
        """ Calculates the minimum and maximum sizes allowed for the input dock.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CalculateHintRect(self, pane_window, pt, offset) -> None:
        """ Calculates the drop hint rectangle.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CalculatePaneSizerLimits(self, dock, pane) -> None:
        """ Calculates the minimum and maximum sizes allowed for the input pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CanDockPanel(self, p: AuiPaneInfo) -> None:
        """ Returns whether a pane can be docked or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CanUseModernDockArt(self) -> None:
        """ Returns whether dockart can be used (Windows XP / Vista / 7 only,
requires Mark Hammondsâs pywin32 package).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CheckMovableSizer(self, part: AuiDockUIPart) -> None:
        """ Checks if a UI part can be actually resized.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CheckPaneMove(self, pane: AuiPaneInfo) -> None:
        """ Checks if a pane has moved by a visible amount.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def ClosePane(self, pane_info: AuiPaneInfo) -> None:
        """ Destroys or hides the pane depending on its flags.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CopyTarget(self, target: AuiPaneInfo) -> None:
        """ Copies all the attributes of the input target into another AuiPaneInfo.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CreateFloatingFrame(self, parent, pane_info) -> None:
        """ Creates a floating frame for the windows.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CreateGuideWindows(self) -> None:
        """ Creates the VS2005 HUD guide windows.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CreateHintWindow(self) -> None:
        """ Creates the standard wxAUI hint window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CreateNotebook(self) -> None:
        """ Creates an automatic AuiNotebook when a pane is docked on
top of another pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CreateNotebookBase(self, panes, paneInfo) -> None:
        """ Creates an auto-notebook base from a pane, and then add that pane as a page.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DestroyGuideWindows(self) -> None:
        """ Destroys the VS2005 HUD guide windows.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DestroyHintWindow(self) -> None:
        """ Destroys the standard wxAUI hint window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DetachPane(self, window: 'Window') -> None:
        """ Tells the AuiManager to stop managing the pane specified
by window. The window, if in a floated frame, is reparented to the frame
managed by AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDrop(*args, **kwargs) -> None:
        """ This is an important function. It basically takes a mouse position,
and determines where the panes new position would be. If the pane is to be
dropped, it performs the drop operation using the specified dock and pane
arrays. By specifying copy dock and pane arrays when calling, a âwhat-ifâ
scenario can be performed, giving precise coordinates for drop hints.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDropFloatingPane(self, docks, panes, target, pt) -> None:
        """ Handles the situation in which the dropped pane contains a normal window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDropLayer(self, docks, target, dock_direction) -> None:
        """ Handles the situation in which target is a single dock guide.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDropNonFloatingPane(self, docks, panes, target, pt) -> None:
        """ Handles the situation in which the dropped pane is not floating.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDropPane(self, panes, target, dock_direction, dock_layer, dock_row, dock_pos) -> None:
        """ Drop a pane in the interface.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDropRow(self, panes, target, dock_direction, dock_layer, dock_row) -> None:
        """ Insert a row in the interface before dropping.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDropToolbar(self, docks, panes, target, pt, offset) -> None:
        """ Handles the situation in which the dropped pane contains a toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoEndResizeAction(self, event: MouseEvent) -> None:
        """ Ends a resize action, or for live update, resizes the sash.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoFrameLayout(self) -> None:
        """ This is an internal function which invokes wx.Sizer.Layout()
on the frameâs main sizer, then measures all the various UI items
and updates their internal rectangles.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoUpdate(self) -> None:
        """ This method is called after any number of changes are made to any of the
managed panes. Update must be invoked after AddPane
or InsertPane are called in order to ârealizeâ or âcommitâ the changes.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoUpdateEvt(self, evt) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DrawHintRect(self, pane_window, pt, offset) -> None:
        """ Calculates the hint rectangle by calling CalculateHintRect. If there is a
rectangle, it shows it by calling ShowHint, otherwise it hides any hint
rectangle currently shown.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DrawPaneButton(self, dc, part, pt) -> None:
        """ Draws a pane button in the caption (convenience function).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def FireEvent(self, evtType, pane, canVeto=False) -> None:
        """ Fires one of the EVT_AUI_PANE_FLOATED / FLOATING / DOCKING / DOCKED / ACTIVATED event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetAGWFlags(self) -> None:
        """ Returns the current managerâs flags.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetAllPanes(self) -> None:
        """ Returns a reference to all the pane info structures.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetAnimationStep(self) -> None:
        """ Returns the animation step speed (a float) to use in AnimateDocking.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetArtProvider(self) -> None:
        """ Returns the current art provider being used.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetAttributes(self, pane: AuiPaneInfo) -> None:
        """ Returns all the attributes of a AuiPaneInfo.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetAutoNotebookStyle(self) -> None:
        """ Returns the default AGW-specific window style for automatic notebooks.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetAutoNotebookTabArt(self) -> None:
        """ Returns the default tab art provider for automatic notebooks.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetDockPixelOffset(self, test: AuiPaneInfo) -> None:
        """ This is an internal function which returns a dockâs offset in pixels from
the left side of the window (for horizontal docks) or from the top of the
window (for vertical docks).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetDockSizeConstraint(self) -> None:
        """ Returns the current dock constraint values.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetFrame(self) -> None:
        """ Returns the window being managed by AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetManagedWindow(self) -> None:
        """ Returns the window being managed by AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetNotebooks(self) -> None:
        """ Returns all the automatic AuiNotebook in the AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetOppositeDockTotalSize(self, docks, direction) -> None:
        """ Returns the dimensions of the dock which lives opposite of the input dock.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPane(self, item: 'Window') -> None:
        """ Looks up a AuiPaneInfo structure based on the supplied window pointer. Upon failure,
GetPane returns an empty AuiPaneInfo, a condition which can be checked
by calling AuiPaneInfo.IsOk().

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPaneByName(self, name: str) -> None:
        """ This version of GetPane looks up a pane based on a âpane nameâ.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPaneByWidget(self, window: 'Window') -> None:
        """ This version of GetPane looks up a pane based on a âpane windowâ.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPanePart(self, wnd: 'Window') -> None:
        """ Looks up the pane border UI part of the
pane specified. This allows the caller to get the exact rectangle
of the pane in question, including decorations like caption and border.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPanePositionsAndSizes(self, dock: AuiDockInfo) -> None:
        """ Returns all the panes positions and sizes in a dock.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPartnerDock(self, dock: AuiDockInfo) -> None:
        """ Returns the partner dock for the input dock.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPartnerPane(self, dock, pane) -> None:
        """ Returns the partner pane for the input pane. They both need to live
in the same AuiDockInfo.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPartSizerRect(self, uiparts: list) -> None:
        """ Returns the rectangle surrounding the specified UI parts.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetSnapPosition(self) -> None:
        """ Returns the main frame snapping position.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetTotalPixSizeAndProportion(self, dock: AuiDockInfo) -> None:
        """ Returns the dimensions and proportion of the input dock.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def HideHint(self) -> None:
        """ Hides a transparent window hint if there is one.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def HitTest(self, x, y) -> None:
        """ This is an internal function which determines
which UI item the specified coordinates are over.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def InsertPane(self, window, pane_info, insert_level=AUI_INSERT_PANE) -> None:
        """ This method is used to insert either a previously unmanaged pane window
into the frame manager, or to insert a currently managed pane somewhere else.
InsertPane will push all panes, rows, or docks aside and insert the window
into the position specified by pane_info.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def IsPaneButtonVisible(self, part: AuiDockUIPart) -> None:
        """ Returns whether a pane button in the pane caption is visible.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def LayoutAddDock(self, cont, dock, uiparts, spacer_only) -> None:
        """ Adds a dock into the existing layout.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def LayoutAddPane(self, cont, dock, pane, uiparts, spacer_only) -> None:
        """ Adds a pane into the existing layout (in an existing dock).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def LayoutAll(self, panes, docks, uiparts, spacer_only=False, oncheck=True) -> None:
        """ Layouts all the UI structures in the interface.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def LoadPaneInfo(self, pane_part, pane) -> None:
        """ This method is similar to to LoadPerspective, with the exception that
it only loads information about a single pane. It is used in combination
with SavePaneInfo.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def LoadPerspective(self, layout, update=True, restorecaption=False) -> None:
        """ Loads a layout which was saved with SavePerspective.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def MaximizePane(self, pane_info, savesizes=True) -> None:
        """ Maximizes the input pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def MinimizePane(self, paneInfo, mgrUpdate=True) -> None:
        """ Minimizes a pane in a newly and automatically created AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnCaptionDoubleClicked(self, pane_window: 'Window') -> None:
        """ Handles the mouse double click on the pane caption.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnCaptureLost(self, event: MouseCaptureLostEvent) -> None:
        """ Handles the wx.EVT_MOUSE_CAPTURE_LOST event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnChildFocus(self, event: ChildFocusEvent) -> None:
        """ Handles the wx.EVT_CHILD_FOCUS event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnClose(self, event) -> None:
        """ Called when the managed window is closed. Makes sure that UnInit
is called.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnDestroy(self, event) -> None:
        """ Called when the managed window is destroyed. Makes sure that UnInit
is called.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ Handles the wx.EVT_ERASE_BACKGROUND event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnFindManager(self, event: AuiManagerEvent) -> None:
        """ Handles the EVT_AUI_FIND_MANAGER event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnFloatingPaneActivated(self, wnd: 'Window') -> None:
        """ Handles the activation event of a floating pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnFloatingPaneClosed(self, wnd, event) -> None:
        """ Handles the close event of a floating pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnFloatingPaneMoved(self, wnd, eventOrPt) -> None:
        """ Handles the move event of a floating pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnFloatingPaneResized(self, wnd, size) -> None:
        """ Handles the resizing of a floating pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnGripperClicked(self, pane_window, start, offset) -> None:
        """ Handles the mouse click on the pane gripper.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnHintFadeTimer(self, event: TimerEvent) -> None:
        """ Handles the wx.EVT_TIMER event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeaveWindow(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEAVE_WINDOW event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftDClick(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEFT_DCLICK event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftDown(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEFT_DOWN event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftUp(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_LEFT_UP event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftUp_ClickButton(self, event: MouseEvent) -> None:
        """ Sub-handler for the OnLeftUp event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftUp_DragFloatingPane(self, eventOrPt) -> None:
        """ Sub-handler for the OnLeftUp event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftUp_DragMovablePane(self, event: MouseEvent) -> None:
        """ Sub-handler for the OnLeftUp event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftUp_DragToolbarPane(self, eventOrPt) -> None:
        """ Sub-handler for the OnLeftUp event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftUp_Resize(self, event: MouseEvent) -> None:
        """ Sub-handler for the OnLeftUp event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion(self, event: MouseEvent) -> None:
        """ Handles the wx.EVT_MOTION event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion_ClickCaption(self, event: MouseEvent) -> None:
        """ Sub-handler for the OnMotion event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion_DragFloatingPane(self, eventOrPt) -> None:
        """ Sub-handler for the OnMotion event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion_DragMovablePane(self, eventOrPt) -> None:
        """ Sub-handler for the OnMotion event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion_DragToolbarPane(self, eventOrPt) -> None:
        """ Sub-handler for the OnMotion event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion_Other(self, event: MouseEvent) -> None:
        """ Sub-handler for the OnMotion event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion_Resize(self, event: MouseEvent) -> None:
        """ Sub-handler for the OnMotion event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMove(self, event: MoveEvent) -> None:
        """ Handles the wx.EVT_MOVE event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ Handles the wx.EVT_PAINT event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnPaneButton(self, event: AuiManagerEvent) -> None:
        """ Handles the EVT_AUI_PANE_BUTTON event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnPaneDocked(self, event: AuiManagerEvent) -> None:
        """ Handles the EVT_AUI_PANE_DOCKED event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnRender(self, event: AuiManagerEvent) -> None:
        """ Draws all of the pane captions, sashes, backgrounds, captions, grippers, pane borders and buttons.
It renders the entire user interface. It binds the EVT_AUI_RENDER event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnRestoreMinimizedPane(self, event: AuiManagerEvent) -> None:
        """ Handles the EVT_AUI_PANE_MIN_RESTORE event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnSetCursor(self, event: SetCursorEvent) -> None:
        """ Handles the wx.EVT_SET_CURSOR event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ Handles the wx.EVT_SIZE event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnSysColourChanged(self, event: SysColourChangedEvent) -> None:
        """ Handles the wx.EVT_SYS_COLOUR_CHANGED event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnTabBeginDrag(self, event: Any) -> None:
        """ Handles the EVT_AUINOTEBOOK_BEGIN_DRAG event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnTabEndDrag(self, event: Any) -> None:
        """ Handles the EVT_AUINOTEBOOK_END_DRAG event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnTabPageClose(self, event: Any) -> None:
        """ Handles the EVT_AUINOTEBOOK_PAGE_CLOSE event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnTabSelected(self, event: Any) -> None:
        """ Handles the EVT_AUINOTEBOOK_PAGE_CHANGED event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def PaneFromTabEvent(self, event: Any) -> None:
        """ Returns a AuiPaneInfo from a AuiNotebook event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def PaneHitTest(self, panes, pt) -> None:
        """ Similar to HitTest, but it checks in which AuiManager rectangle the
input point belongs to.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def ProcessDockResult(self, target, new_pos) -> None:
        """ This is a utility function used by DoDrop - it checks
if a dock operation is allowed, the new dock position is copied into
the target info. If the operation was allowed, the function returns True.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def ProcessMgrEvent(self, event: AuiManagerEvent) -> None:
        """ Process the AUI events sent to the manager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RefreshButton(self, part: AuiDockUIPart) -> None:
        """ Refreshes a pane button in the caption.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RefreshCaptions(self) -> None:
        """ Refreshes all pane captions.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RemoveAutoNBCaption(self, pane: AuiPaneInfo) -> None:
        """ Removes the caption on newly created automatic notebooks.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def Render(self, dc: 'DC') -> None:
        """ Fires a render event, which is normally handled by OnRender. This allows the
render function to be overridden via the render event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def Repaint(self, dc: Optional[None]=None) -> None:
        """ Repaints the entire frame decorations (sashes, borders, buttons and so on).
It renders the entire user interface.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RepositionPane(self, pane, wnd_pos, wnd_size) -> None:
        """ Repositions a pane after the main frame has been moved/resized.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RequestUserAttention(self, pane_window: 'Window') -> None:
        """ Requests the user attention by intermittently highlighting the pane caption.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RestoreMaximizedPane(self) -> None:
        """ Restores the current maximized pane (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RestoreMinimizedPane(self, paneInfo: AuiPaneInfo) -> None:
        """ Restores a previously minimized pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RestorePane(self, pane_info: AuiPaneInfo) -> None:
        """ Restores the input pane from a previous maximized or minimized state.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RestrictResize(self, clientPt, screenPt, createDC) -> None:
        """ Common method between DoEndResizeAction and OnLeftUp_Resize.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SavePaneInfo(self, pane: AuiPaneInfo) -> None:
        """ This method is similar to SavePerspective, with the exception
that it only saves information about a single pane. It is used in
combination with LoadPaneInfo.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SavePerspective(self) -> None:
        """ Saves the entire user interface layout into an encoded string, which can then
be stored by the application (probably using Config).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SavePreviousDockSizes(self, pane_info: AuiPaneInfo) -> None:
        """ Stores the previous dock sizes, to be used in a ârestoreâ action later.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetAGWFlags(self, agwFlags: int) -> None:
        """ This method is used to specify AuiManager âs settings flags.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetAnimationStep(self, step: float) -> None:
        """ Sets the animation step speed (a float) to use in AnimateDocking.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetArtProvider(self, art_provider: Any) -> None:
        """ Instructs AuiManager to use art provider specified by the parameter
art_provider for all drawing calls. This allows pluggable look-and-feel
features.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetAttributes(self, pane, attrs) -> None:
        """ Sets all the attributes contained in attrs to a AuiPaneInfo.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetAutoNotebookStyle(self, agwStyle: int) -> None:
        """ Sets the default AGW-specific window style for automatic notebooks.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetAutoNotebookTabArt(self, art: Any) -> None:
        """ Sets the default tab art provider for automatic notebooks.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetDockSizeConstraint(self, width_pct, height_pct) -> None:
        """ When a user creates a new dock by dragging a window into a docked position,
often times the large size of the window will create a dock that is unwieldy
large.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetFrame(self, managed_window: 'Window') -> None:
        """ Called to specify the frame or window which is to be managed by AuiManager.
Frame management is not restricted to just frames. Child windows or custom
controls are also allowed.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetManagedWindow(self, managed_window: 'Window') -> None:
        """ Called to specify the frame or window which is to be managed by AuiManager.
Frame management is not restricted to just frames. Child windows or custom
controls are also allowed.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetMasterManager(self, manager: AuiManager) -> None:
        """ Sets the master manager for an automatic AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetSnapLimits(self, x, y) -> None:
        """ Modifies the snap limits used when snapping the managed_window to the screen
(using SnapToScreen) or when snapping the floating panes to one side of the
managed_window (using SnapPane).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def ShowHint(self, rect: 'Rect') -> None:
        """ Shows the AUI hint window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def ShowPane(self, window, show) -> None:
        """ Shows or hides a pane based on the window passed as input.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SlideIn(self, event: TimerEvent) -> None:
        """ Handles the wx.EVT_TIMER event for AuiManager.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SlideOut(self) -> None:
        """ Slides out a preview of a minimized pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SmartShrink(self, docks, direction) -> None:
        """ Used to intelligently shrink the docksâ size (if needed).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SmoothDock(self, paneInfo: AuiPaneInfo) -> None:
        """ This method implements a smooth docking effect for floating panes, similar to
what the PyQT library does with its floating windows.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def Snap(self) -> None:
        """ Snaps the main frame to specified position on the screen.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SnapPane(self, pane, pane_pos, pane_size, toSnap=False) -> None:
        """ Snaps a floating pane to one of the main frame sides.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SnapToScreen(self, snap=True, monitor=0, hAlign=wx.RIGHT, vAlign=wx.TOP) -> None:
        """ Snaps the main frame to specified position on the screen.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def StartPreviewTimer(self, toolbar: Any) -> None:
        """ Starts a timer for sliding in and out a minimized pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def StopPreviewTimer(self) -> None:
        """ Stops a timer for sliding in and out a minimized pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SwitchToolBarOrientation(self, pane: AuiPaneInfo) -> None:
        """ Switches the toolbar orientation from vertical to horizontal and vice-versa.
This is especially useful for vertical docked toolbars once they float.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def UnInit(self) -> None:
        """ Uninitializes the framework and should be called before a managed frame or
window is destroyed. UnInit is usually called in the managed wx.Frame / wx.Window
destructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def Update(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def UpdateButtonOnScreen(self, button_ui_part, event) -> None:
        """ Updates/redraws the UI part containing a pane button.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def UpdateDockingGuides(self, paneInfo: AuiPaneInfo) -> None:
        """ Updates the docking guide windows positions and appearance.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def UpdateNotebook(self) -> None:
        """ Updates the automatic AuiNotebook in the layout (if any exists).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """



EVT_MOUSE_CAPTURE_LOST: int

EVT_CHILD_FOCUS: int

EVT_ERASE_BACKGROUND: int

EVT_TIMER: int

EVT_LEAVE_WINDOW: int

EVT_LEFT_DCLICK: int

EVT_LEFT_DOWN: int

EVT_LEFT_UP: int

EVT_MOTION: int

EVT_MOVE: int

EVT_PAINT: int

EVT_SET_CURSOR: int

EVT_SIZE: int

EVT_SYS_COLOUR_CHANGED: int

class AuiPaneInfo:
    """ AuiPaneInfo specifies all the parameters for a pane. These parameters specify where
the pane is on the screen, whether it is docked or floating, or hidden. In addition,
these parameters specify the paneâs docked position, floating position, preferred
size, minimum size, caption text among many other parameters.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
    """
    def __init__(self) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def BestSize(self, arg1=None, arg2=None) -> None:
        """ Sets the ideal size for the pane. The docking manager will attempt to use
this size as much as possible when docking or floating the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def BestSize1(self, size) -> None:
        """ Sets the best size of the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def BestSize2(self, x, y) -> None:
        """ Sets the best size of the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Bottom(self) -> None:
        """ Sets the pane dock position to the bottom of the frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def BottomDockable(self, b: bool=True) -> None:
        """ Indicates whether a pane can be docked at the bottom of the frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def BottomSnappable(self, b: bool=True) -> None:
        """ Indicates whether a pane can be snapped at the bottom of the main frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Caption(self, caption: str) -> None:
        """ Sets the caption of the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def CaptionVisible(self, visible=True, left=False) -> None:
        """ Indicates that a pane caption should be visible. If visible is False, no pane
caption is drawn.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Center(self) -> None:
        """ Sets the pane to the center position of the frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def CenterPane(self) -> None:
        """ Specifies that the pane should adopt the default center pane settings.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Centre(self) -> None:
        """ Sets the pane to the center position of the frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def CentrePane(self) -> None:
        """ Specifies that the pane should adopt the default center pane settings.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def CloseButton(self, visible: bool=True) -> None:
        """ Indicates that a close button should be drawn for the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def CountButtons(self) -> None:
        """ Returns the number of visible buttons in the docked pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def DefaultPane(self) -> None:
        """ Specifies that the pane should adopt the default pane settings.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def DestroyOnClose(self, b: bool=True) -> None:
        """ Indicates whether a pane should be destroyed when it is closed.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Direction(self, direction: int) -> None:
        """ Determines the direction of the docked pane. It is functionally the
same as calling Left, Right, Top or Bottom,
except that docking direction may be specified programmatically via the parameter direction.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Dock(self) -> None:
        """ Indicates that a pane should be docked. It is the opposite of Float.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def dock_direction_get(self) -> None:
        """ Getter for the dock_direction.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def dock_direction_set(self, value: int) -> None:
        """ Setter for the dock_direction.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Dockable(self, b: bool=True) -> None:
        """ Specifies whether a frame can be docked or not. It is the same as specifying
TopDockable . BottomDockable . LeftDockable . RightDockable .

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def DockFixed(self, b: bool=True) -> None:
        """ Causes the containing dock to have no resize sash. This is useful
for creating panes that span the entire width or height of a dock, but should
not be resizable in the other direction.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Fixed(self) -> None:
        """ Forces a pane to be fixed size so that it cannot be resized.
After calling Fixed, IsFixed will return True.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Float(self) -> None:
        """ Indicates that a pane should be floated. It is the opposite of Dock.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Floatable(self, b: bool=True) -> None:
        """ Sets whether the user will be able to undock a pane and turn it
into a floating window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def FloatingPosition(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ Sets the position of the floating pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def FloatingSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the size of the floating pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def FlyOut(self, b: bool=True) -> None:
        """ Indicates whether a pane, when floating, has a âfly-outâ effect
(i.e., floating panes which only show themselves when moused over).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def GetMinimizeMode(self) -> None:
        """ Returns the minimization style for this pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Gripper(self, visible: bool=True) -> None:
        """ Indicates that a gripper should be drawn for the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def GripperTop(self, attop: bool=True) -> None:
        """ Indicates that a gripper should be drawn at the top of the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasBorder(self) -> None:
        """ Returns True if the pane displays a border.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasCaption(self) -> None:
        """ Returns True if the pane displays a caption.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasCaptionLeft(self) -> None:
        """ Returns True if the pane displays a caption on the left (rotated by 90 degrees).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasCloseButton(self) -> None:
        """ Returns True if the pane displays a button to close the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasFlag(self, flag: int) -> None:
        """ Returns True if the the property specified by flag is active for the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasGripper(self) -> None:
        """ Returns True if the pane displays a gripper.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasGripperTop(self) -> None:
        """ Returns True if the pane displays a gripper at the top.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasMaximizeButton(self) -> None:
        """ Returns True if the pane displays a button to maximize the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasMinimizeButton(self) -> None:
        """ Returns True if the pane displays a button to minimize the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasNotebook(self) -> None:
        """ Returns whether a pane has a AuiNotebook or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasPinButton(self) -> None:
        """ Returns True if the pane displays a button to float the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Hide(self) -> None:
        """ Indicates that a pane should be hidden.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Icon(self, icon: Icon) -> None:
        """ Specifies whether an icon is drawn on the left of the caption text when
the pane is docked. If icon is None or NullIcon, no icon is drawn on
the caption space.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsBottomDockable(self) -> None:
        """ Returns True if the pane can be docked at the bottom
of the managed frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsBottomSnappable(self) -> None:
        """ Returns True if the pane can be snapped at the bottom of the managed frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsDestroyOnClose(self) -> None:
        """ Returns True if the pane should be destroyed when it is closed.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsDockable(self) -> None:
        """ Returns True if the pane can be docked.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsDocked(self) -> None:
        """ Returns True if the pane is docked.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsFixed(self) -> None:
        """ Returns True if the pane cannot be resized.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsFloatable(self) -> None:
        """ Returns True if the pane can be undocked and displayed as a
floating window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsFloating(self) -> None:
        """ Returns True if the pane is floating.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsFlyOut(self) -> None:
        """ Returns True if the floating pane has a âfly-outâ effect.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsHorizontal(self) -> None:
        """ Returns True if the pane dock_direction is horizontal.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsLeftDockable(self) -> None:
        """ Returns True if the pane can be docked at the left
of the managed frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsLeftSnappable(self) -> None:
        """ Returns True if the pane can be snapped on the left of the managed frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsMaximized(self) -> None:
        """ Returns True if the pane is maximized.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsMinimized(self) -> None:
        """ Returns True if the pane is minimized.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsMovable(self) -> None:
        """ Returns True if the docked frame can be undocked or moved to
another dock position.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsNotebookControl(self) -> None:
        """ Returns whether the pane is a notebook control (AuiNotebook).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsNotebookDockable(self) -> None:
        """ Returns True if a pane can be docked on top to another to create a
AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsNotebookPage(self) -> None:
        """ Returns whether the pane is a notebook page in a AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsOk(self) -> None:
        """ Returns True if the AuiPaneInfo structure is valid.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsResizeable(self) -> None:
        """ Returns True if the pane can be resized.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsRightDockable(self) -> None:
        """ Returns True if the pane can be docked at the right
of the managed frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsRightSnappable(self) -> None:
        """ Returns True if the pane can be snapped on the right of the managed frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsShown(self) -> None:
        """ Returns True if the pane is currently shown.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsSnappable(self) -> None:
        """ Returns True if the pane can be snapped.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsToolbar(self) -> None:
        """ Returns True if the pane contains a toolbar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsTopDockable(self) -> None:
        """ Returns True if the pane can be docked at the top
of the managed frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsTopSnappable(self) -> None:
        """ Returns True if the pane can be snapped at the top of the managed frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsVertical(self) -> None:
        """ Returns True if the pane dock_direction is vertical.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Layer(self, layer: int) -> None:
        """ Determines the layer of the docked pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Left(self) -> None:
        """ Sets the pane dock position to the left side of the frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def LeftDockable(self, b: bool=True) -> None:
        """ Indicates whether a pane can be docked on the left of the frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def LeftSnappable(self, b: bool=True) -> None:
        """ Indicates whether a pane can be snapped on the left of the main frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Maximize(self) -> None:
        """ Makes the pane take up the full area.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MaximizeButton(self, visible: bool=True) -> None:
        """ Indicates that a maximize button should be drawn for the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MaxSize(self, arg1=None, arg2=None) -> None:
        """ Sets the maximum size of the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MaxSize1(self, size) -> None:
        """ Sets the maximum size of the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MaxSize2(self, x, y) -> None:
        """ Sets the maximum size of the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Minimize(self) -> None:
        """ Makes the pane minimized in a AuiToolBar.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MinimizeButton(self, visible: bool=True) -> None:
        """ Indicates that a minimize button should be drawn for the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MinimizeMode(self, mode: int) -> None:
        """ Sets the expected minimized mode if the minimize button is visible.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MinimizeTarget(self, toolbarPane: AuiPaneInfo) -> None:
        """ Minimizes the panes using a AuiPaneInfo as a target. As AuiPaneInfo properties
need to be copied back and forth every time the perspective has changed, we
only store the toobar name.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MinSize(self, arg1=None, arg2=None) -> None:
        """ Sets the minimum size of the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MinSize1(self, size) -> None:
        """ Sets the minimum size of the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MinSize2(self, x, y) -> None:
        """ Sets the minimum size of the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Movable(self, b: bool=True) -> None:
        """ Indicates whether a pane can be moved.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Name(self, name: Any) -> None:
        """ Sets the name of the pane so it can be referenced in lookup functions.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def NotebookControl(self, id: int) -> None:
        """ Forces a pane to be a notebook control (AuiNotebook).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def NotebookDockable(self, b: bool=True) -> None:
        """ Indicates whether a pane can be docked in an automatic AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def NotebookPage(self, id, tab_position=1000) -> None:
        """ Forces a pane to be a notebook page, so that the pane can be
docked on top to another to create a AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def PaneBorder(self, visible: bool=True) -> None:
        """ Indicates that a border should be drawn for the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def PinButton(self, visible: bool=True) -> None:
        """ Indicates that a pin button should be drawn for the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Position(self, pos: int) -> None:
        """ Determines the position of the docked pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def ResetButtons(self) -> None:
        """ Resets all the buttons and recreates them from scratch depending on the
AuiManager flags.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Resizable(self, resizable: bool=True) -> None:
        """ Allows a pane to be resizable if resizable is True, and forces
it to be a fixed size if resizeable is False.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Restore(self) -> None:
        """ Is the reverse of Maximize and Minimize.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Right(self) -> None:
        """ Sets the pane dock position to the right side of the frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def RightDockable(self, b: bool=True) -> None:
        """ Indicates whether a pane can be docked on the right of the frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def RightSnappable(self, b: bool=True) -> None:
        """ Indicates whether a pane can be snapped on the right of the main frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Row(self, row: int) -> None:
        """ Determines the row of the docked pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def SetDockPos(self, source: AuiPaneInfo) -> None:
        """ Copies the source pane members that pertain to docking position to self.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def SetFlag(self, flag, option_state) -> None:
        """ Turns the property given by flag on or off with the option_state
parameter.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def SetNameFromNotebookId(self) -> None:
        """ Sets the pane name once docked in a AuiNotebook using the notebook id.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Show(self, show: bool=True) -> None:
        """ Indicates that a pane should be shown.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Snappable(self, b: bool=True) -> None:
        """ Indicates whether a pane can be snapped on the main frame. This is
equivalent as calling TopSnappable . BottomSnappable . LeftSnappable . RightSnappable .

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def ToolbarPane(self) -> None:
        """ Specifies that the pane should adopt the default toolbar pane settings.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Top(self) -> None:
        """ Sets the pane dock position to the top of the frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def TopDockable(self, b: bool=True) -> None:
        """ Indicates whether a pane can be docked at the top of the frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def TopSnappable(self, b: bool=True) -> None:
        """ Indicates whether a pane can be snapped at the top of the main frame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Transparent(self, alpha: int) -> None:
        """ Makes the pane transparent when floating.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Window(self, w: 'Window') -> None:
        """ Associate a wx.Window derived window to this pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    dock_direction: Any  # Getter for the dock_direction.



class AuiManager_DCP(AuiManager):
    """ A class similar to AuiManager but with a Dummy Center Pane (DCP).
The code for this class is still flickery due to the call to CallAfter
and the double-update call.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager_DCP.html
    """
    def __init__(self, *args, **keys) -> None:
        """ See AuiManager.__init__ for the class construction.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager_DCP.html
        """

    def Update(self) -> None:
        """ This method is called after any number of changes are made to any of the
managed panes. Update must be invoked after AuiManager.AddPane or
AuiManager.InsertPane are called in order to ârealizeâ or âcommitâ the changes.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager_DCP.html
        """



class AuiDockInfo:
    """ A class to store all properties of a dock.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockInfo.html
    """
    def __init__(self) -> None:
        """ Default class constructor.
Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockInfo.html
        """

    def IsHorizontal(self) -> None:
        """ Returns whether the dock is horizontal or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockInfo.html
        """

    def IsOk(self) -> None:
        """ Returns whether a dock is valid or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockInfo.html
        """

    def IsVertical(self) -> None:
        """ Returns whether the dock is vertical or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockInfo.html
        """



class AuiDockUIPart:
    """ A class which holds attributes for a UI part in the interface.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockUIPart.html
    """
    def __init__(self) -> None:
        """ Default class constructor.
Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockUIPart.html
        """



class AuiManagerEvent(PyCommandEvent):
    """ A specialized command event class for events sent by AuiManager.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
    """
    def __init__(self, eventType, id=1) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def CanVeto(self) -> None:
        """ Returns whether the event can be vetoed and has been vetoed.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def GetButton(self) -> None:
        """ Returns the associated AuiPaneButton instance (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def GetDC(self) -> None:
        """ Returns the associated wx.DC device context (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def GetManager(self) -> None:
        """ Returns the associated AuiManager (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def GetPane(self) -> None:
        """ Returns the associated AuiPaneInfo structure (if any).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def GetVeto(self) -> None:
        """ Returns whether the event has been vetoed or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def SetButton(self, b: AuiPaneButton) -> None:
        """ Associates a AuiPaneButton instance to this event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def SetCanVeto(self, can_veto: bool) -> None:
        """ Sets whether the event can be vetoed or not.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def SetDC(self, pdc: 'DC') -> None:
        """ Associates a wx.DC device context to this event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def SetManager(self, mgr: AuiManager) -> None:
        """ Associates a AuiManager to the current event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def SetPane(self, p: AuiPaneInfo) -> None:
        """ Associates a AuiPaneInfo instance to this event.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def Veto(self, veto: bool=True) -> None:
        """ Prevents the change announced by this event from happening.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """



class AuiPaneButton:
    """ A simple class which describes the caption pane button attributes.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneButton.html
    """
    def __init__(self, button_id: int) -> None:
        """ Default class constructor.
Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneButton.html
        """



class AuiCenterDockingGuide(AuiDockingGuide):
    """ A docking guide window for multiple docking hint (diamond-shaped HUD).

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
    """
    def __init__(self, parent: AuiManager) -> None:
        """ Default class constructor.
Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def AeroMove(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ Moves the docking guide window to the new position.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def CreateShapesWithStyle(self) -> None:
        """ Creates the docking guide window shape based on which docking bitmaps are used.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def HitTest(self, x, y) -> None:
        """ Checks if the mouse position is inside the target windows rect.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ Handles the wx.EVT_ERASE_BACKGROUND event for AuiCenterDockingGuide.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ Handles the wx.EVT_PAINT event for AuiCenterDockingGuide.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def SetGuideShape(self, event: Optional['WindowCreateEvent']=None) -> None:
        """ Sets the correct shape for the docking guide window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def UpdateDockGuide(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ Updates the docking guides images depending on the mouse position, using focused
images if the mouse is inside the docking guide or unfocused images if it is
outside.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def ValidateNotebookDocking(self, valid: bool) -> None:
        """ Sets whether a pane can be docked on top of another to create an automatic
AuiNotebook.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """



class AuiDockingGuide(Frame):
    """ Base class for AuiSingleDockingGuide and AuiCenterDockingGuide.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuide.html
    """
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.NO_BORDER, name="AuiDockingGuide") -> None:
        """ Default class constructor. Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuide.html
        """

    def HitTest(self, x, y) -> None:
        """ To be overridden by parent classes.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuide.html
        """

    def ValidateNotebookDocking(self, valid: bool) -> None:
        """ To be overridden by parent classes.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuide.html
        """



class AuiSingleDockingGuide(AuiDockingGuide):
    """ A docking guide window for single docking hint (not diamond-shaped HUD).

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
    """
    def __init__(self, parent, direction=0) -> None:
        """ Default class constructor. Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def AeroMove(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ Moves the docking window to the new position. Overridden in children classes.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def CreateShapesWithStyle(self, useWhidbey: bool) -> None:
        """ Creates the docking guide window shape based on which docking bitmaps are used.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def HitTest(self, x, y) -> None:
        """ Checks if the mouse position is inside the target window rect.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def IsValid(self) -> None:
        """ Returns whether the docking direction is valid.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def SetGuideShape(self, event: Optional['WindowCreateEvent']=None) -> None:
        """ Sets the correct shape for the docking guide window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def SetShape(self, region: Region) -> None:
        """ If the platform supports it, sets the shape of the window to that depicted by region.
The system will not display or respond to any mouse event for the pixels that lie
outside of the region. To reset the window to the normal rectangular shape simply call
SetShape again with an empty region.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def SetValid(self, valid: bool) -> None:
        """ Sets the docking direction as valid or invalid.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def UpdateDockGuide(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ Updates the docking guide images depending on the mouse position, using focused
images if the mouse is inside the docking guide or unfocused images if it is
outside.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """



TOP: int

BOTTOM: int

LEFT: int

RIGHT: int

class AuiDockingGuideInfo:
    """ A class which holds information about VS2005 docking guide windows.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
    """
    def __init__(self, other: Optional[AuiDockingGuideInfo]=None) -> None:
        """ Default class constructor.
Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Assign(self, other: AuiDockingGuideInfo) -> None:
        """ Assigns the properties of the other AuiDockingGuideInfo to self.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Bottom(self) -> None:
        """ Sets the guide window to bottom docking.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Center(self) -> None:
        """ Sets the guide window to center docking.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Centre(self) -> None:
        """ Sets the guide window to centre docking.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Host(self, h: AuiDockingGuideWindow) -> None:
        """ Hosts a docking guide window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Left(self) -> None:
        """ Sets the guide window to left docking.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Right(self) -> None:
        """ Sets the guide window to right docking.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Top(self) -> None:
        """ Sets the guide window to top docking.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """



class AuiDockingGuideWindow(Window):
    """ Target class for AuiDockingGuide and AuiCenterDockingGuide.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
    """
    def __init__(self, parent, rect, direction=0, center=False, useAero=False) -> None:
        """ Default class constructor. Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def Draw(self, dc: 'DC') -> None:
        """ Draws the whole docking guide window (not used if the docking guide images are ok).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def DrawArrow(self, dc: 'DC') -> None:
        """ Draws the docking guide arrow icon (not used if the docking guide images are ok).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def DrawBackground(self, dc: 'DC') -> None:
        """ Draws the docking guide background.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def DrawDottedLine(self, dc, point, length, vertical) -> None:
        """ Draws a dotted line (not used if the docking guide images are ok).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def DrawIcon(self, dc: 'DC') -> None:
        """ Draws the docking guide icon (not used if the docking guide images are ok).

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def IsValid(self) -> None:
        """ Returns whether the docking direction is valid.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ Handles the wx.EVT_ERASE_BACKGROUND event for AuiDockingGuideWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ Handles the wx.EVT_PAINT event for AuiDockingGuideWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def SetValid(self, valid: bool) -> None:
        """ Sets the docking direction as valid or invalid.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def UpdateDockGuide(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ Updates the docking guide images depending on the mouse position, using focused
images if the mouse is inside the docking guide or unfocused images if it is
outside.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """



CENTER: int

class AuiDockingHintWindow(Frame):
    """ The original wxAUI docking window hint.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
    """
    def __init__(*args, **kwargs) -> None:
        """ Default class constructor. Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """

    def MakeVenetianBlinds(self) -> None:
        """ Creates the âvenetian blindâ effect if AuiManager has the AUI_MGR_VENETIAN_BLINDS_HINT
flag set.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ Handles the wx.EVT_PAINT event for AuiDockingHintWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ Handles the wx.EVT_SIZE event for AuiDockingHintWindow.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """

    def SetBlindMode(self, agwFlags: int) -> None:
        """ Sets whether venetian blinds or transparent hints will be shown as docking hint.
This depends on the AuiManager flags.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """

    def SetShape(self, region: Region) -> None:
        """ If the platform supports it, sets the shape of the window to that depicted by region.
The system will not display or respond to any mouse event for the pixels that lie
outside of the region. To reset the window to the normal rectangular shape simply call
SetShape again with an empty region.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """

    def Show(self, show: bool=True) -> None:
        """ Show the hint window.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """



class AuiFloatingFrame(MiniFrame):
    """ AuiFloatingFrame is the frame class that holds floating panes.

        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
    """
    def __init__(self, parent, owner_mgr, pane=None, id=wx.ID_ANY, title="", style=wx.FRAME_TOOL_WINDOW | wx.FRAME_FLOAT_ON_PARENT | wx.FRAME_NO_TASKBAR | wx.CLIP_CHILDREN) -> None:
        """ Default class constructor. Used internally, do not call it in your code!

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def CopyAttributes(self, pane: AuiPaneInfo) -> None:
        """ Copies all the attributes of the input pane into another AuiPaneInfo.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def FadeOut(self) -> None:
        """ Actually starts the fading out of the floating pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def FlyOut(self) -> None:
        """ Starts the flying in and out of a floating pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def GetOwnerManager(self) -> None:
        """ Returns the AuiManager that manages the pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnActivate(self, event: ActivateEvent) -> None:
        """ Handles the wx.EVT_ACTIVATE event for AuiFloatingFrame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnCheckFlyTimer(self, event: TimerEvent) -> None:
        """ Handles the wx.EVT_TIMER event for AuiFloatingFrame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnClose(self, event: CloseEvent) -> None:
        """ Handles the wx.EVT_CLOSE event for AuiFloatingFrame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnFindManager(self, event: AuiManagerEvent) -> None:
        """ Handles the EVT_AUI_FIND_MANAGER event for AuiFloatingFrame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnFlyTimer(self, event: TimerEvent) -> None:
        """ Handles the wx.EVT_TIMER event for AuiFloatingFrame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnIdle(self, event: IdleEvent) -> None:
        """ Handles the wx.EVT_IDLE event for AuiFloatingFrame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnMove(self, event: MoveEvent) -> None:
        """ Handles the wx.EVT_MOVE event for AuiFloatingFrame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnMoveEvent(self, event: MoveEvent) -> None:
        """ Handles the wx.EVT_MOVE and wx.EVT_MOVING events for AuiFloatingFrame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnMoveFinished(self) -> None:
        """ The user has just finished moving the floating pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnMoveStart(self, event: MouseEvent) -> None:
        """ The user has just started moving the floating pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnMoving(self, rect, direction) -> None:
        """ The user is moving the floating pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ Handles the wx.EVT_SIZE event for AuiFloatingFrame.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def SetPaneWindow(self, pane: AuiPaneInfo) -> None:
        """ Sets all the properties of a pane.

            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """



EVT_ACTIVATE: int

EVT_CLOSE: int

EVT_IDLE: int

EVT_MOVING: int

NORTH: int

SOUTH: int

EAST: int

WEST: int

