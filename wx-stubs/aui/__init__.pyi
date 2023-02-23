# -*- coding: utf-8 -*-
from typing import Optional, Any


class AuiNotebook('BookCtrlBase'):
	""" AuiNotebook is part of the AUI class framework, which represents a
notebook control, managing multiple windows with associated tabs.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def AddPage(self, *args, **kw) -> bool:
		""" Overloaded Implementations:
		"""

	def AdvanceSelection(self, forward: bool=True) -> None:
		""" Sets the selection to the next or previous page.
		"""

	def ChangeSelection(self, n: int) -> int:
		""" Changes the selection for the given page, returning the previous selection.
		"""

	def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
		""" Creates the notebook window.
		"""

	def DeleteAllPages(self) -> bool:
		""" Deletes all pages.
		"""

	def DeletePage(self, page: int) -> bool:
		""" Deletes a page at the given index.
		"""

	def FindTab(self, page, ctrl, idx) -> bool:
		""" Finds tab control associated with a given window and its tab index.
		"""

	def GetActiveTabCtrl(self) -> 'aui.AuiTabCtrl':
		""" Returns active tab control for this notebook.
		"""

	def GetArtProvider(self) -> 'aui.AuiTabArt':
		""" Returns the associated art provider.
		"""

	@staticmethod
	def GetClassDefaultAttributes(variant: WindowVariant=WINDOW_VARIANT_NORMAL) -> VisualAttributes:
		""" variant (WindowVariant) â
		"""

	def GetCurrentPage(self) -> Window:
		""" Returns the currently selected page or None.
		"""

	def GetHeightForPageHeight(self, pageHeight: int) -> int:
		""" Returns the desired height of the notebook for the given page height.
		"""

	def GetPage(self, page_idx: int) -> Window:
		""" Returns the page specified by the given index.
		"""

	def GetPageBitmap(self, page: int) -> Bitmap:
		""" Returns the tab bitmap for the page.
		"""

	def GetPageCount(self) -> int:
		""" Returns the number of pages in the notebook.
		"""

	def GetPageImage(self, nPage: int) -> int:
		""" Returns the image index for the given page.
		"""

	def GetPageIndex(self, page_wnd: 'Window') -> int:
		""" Returns the page index for the specified window.
		"""

	def GetPageText(self, page: int) -> str:
		""" Returns the tab label for the page.
		"""

	def GetPageToolTip(self, pageIdx: int) -> str:
		""" Returns the tooltip for the tab label of the page.
		"""

	def GetSelection(self) -> int:
		""" Returns the currently selected page.
		"""

	def GetTabCtrlFromPoint(self, pt: 'Point') -> 'aui.AuiTabCtrl':
		""" Returns tab control based on point coordinates inside the tab frame.
		"""

	def GetTabCtrlHeight(self) -> int:
		""" Returns the height of the tab control.
		"""

	def InsertPage(self, *args, **kw) -> bool:
		""" Overloaded Implementations:
		"""

	def RemovePage(self, page: int) -> bool:
		""" Removes a page, without deleting the window pointer.
		"""

	def SetArtProvider(self, art: 'aui.AuiTabArt') -> None:
		""" Sets the art provider to be used by the notebook.
		"""

	def SetFont(self, font: 'Font') -> bool:
		""" Sets the font for drawing the tab labels, using a bold version of the font for selected tab labels.
		"""

	def SetMeasuringFont(self, font: 'Font') -> None:
		""" Sets the font for measuring tab labels.
		"""

	def SetNormalFont(self, font: 'Font') -> None:
		""" Sets the font for drawing unselected tab labels.
		"""

	def SetPageBitmap(self, page, bitmap) -> bool:
		""" Sets the bitmap for the page.
		"""

	def SetPageImage(self, n, imageId) -> bool:
		""" Sets the image index for the given page.
		"""

	def SetPageText(self, page, text) -> bool:
		""" Sets the tab label for the page.
		"""

	def SetPageToolTip(self, page, text) -> bool:
		""" Sets the tooltip displayed when hovering over the tab label of the page.
		"""

	def SetSelectedFont(self, font: 'Font') -> None:
		""" Sets the font for drawing selected tab labels.
		"""

	def SetSelection(self, new_page: int) -> int:
		""" Sets the page selection.
		"""

	def SetTabCtrlHeight(self, height: int) -> None:
		""" Sets the tab height.
		"""

	def SetUniformBitmapSize(self, size: 'Size') -> None:
		""" Ensure that all tabs have the same height, even if some of them donât have bitmaps.
		"""

	def ShowWindowMenu(self) -> bool:
		""" Shows the window menu for the active tab control associated with this notebook, and returns True if a selection was made.
		"""

	def Split(self, page, direction) -> None:
		""" Split performs a split operation programmatically.
		"""

aui.AUI_NB_DEFAULT_STYLE: int  #  Defined as wx.aui.AUI_NB_TOP | wx.aui.AUI_NB_TAB_SPLIT | wx.aui.AUI_NB_TAB_MOVE | wx.aui.AUI_NB_SCROLL_BUTTONS | wx.aui.AUI_NB_CLOSE_ON_ACTIVE_TAB | wx.aui.AUI_NB_MIDDLE_CLICK_CLOSE.
aui.AUI_NB_TAB_SPLIT: int  #  Allows the tab control to be split by dragging a tab.
aui.AUI_NB_TAB_MOVE: int  #  Allows a tab to be moved horizontally by dragging.
aui.AUI_NB_TAB_EXTERNAL_MOVE: int  #  Allows a tab to be moved to another tab control.
aui.AUI_NB_TAB_FIXED_WIDTH: int  #  With this style, all tabs have the same width.
aui.AUI_NB_SCROLL_BUTTONS: int  #  With this style, left and right scroll buttons are displayed.
aui.AUI_NB_WINDOWLIST_BUTTON: int  #  With this style, a drop-down list of windows is available.
aui.AUI_NB_CLOSE_BUTTON: int  #  With this style, a close button is available on the tab bar.
aui.AUI_NB_CLOSE_ON_ACTIVE_TAB: int  #  With this style, the close button is visible on the active tab.
aui.AUI_NB_CLOSE_ON_ALL_TABS: int  #  With this style, the close button is visible on all tabs.
aui.AUI_NB_MIDDLE_CLICK_CLOSE: int  #  With this style, middle click on a tab closes the tab.
aui.AUI_NB_TOP: int  #  With this style, tabs are drawn along the top of the notebook.
aui.AUI_NB_BOTTOM: int  #  With this style, tabs are drawn along the bottom of the notebook. ^^
EVT_AUINOTEBOOK_PAGE_CLOSE: int  #  A page is about to be closed. Processes a  wxEVT_AUINOTEBOOK_PAGE_CLOSE   event.
EVT_AUINOTEBOOK_PAGE_CLOSED(winid,  fn): int  #  A page has been closed. Processes a  wxEVT_AUINOTEBOOK_PAGE_CLOSED   event.
EVT_AUINOTEBOOK_PAGE_CHANGED: int  #  The page selection was changed. Processes a  wxEVT_AUINOTEBOOK_PAGE_CHANGED   event.
EVT_AUINOTEBOOK_PAGE_CHANGING: int  #  The page selection is about to be changed. Processes a  wxEVT_AUINOTEBOOK_PAGE_CHANGING   event. This event can be vetoed.
EVT_AUINOTEBOOK_BUTTON: int  #  The window list button has been pressed. Processes a  wxEVT_AUINOTEBOOK_BUTTON   event.
EVT_AUINOTEBOOK_BEGIN_DRAG: int  #  Dragging is about to begin. Processes a  wxEVT_AUINOTEBOOK_BEGIN_DRAG   event.
EVT_AUINOTEBOOK_END_DRAG: int  #  Dragging has ended. Processes a  wxEVT_AUINOTEBOOK_END_DRAG   event.
EVT_AUINOTEBOOK_DRAG_MOTION: int  #  Emitted during a drag and drop operation. Processes a  wxEVT_AUINOTEBOOK_DRAG_MOTION   event.
EVT_AUINOTEBOOK_ALLOW_DND: int  #  Whether to allow a tab to be dropped. Processes a  wxEVT_AUINOTEBOOK_ALLOW_DND   event. This event must be specially allowed.
EVT_AUINOTEBOOK_DRAG_DONE(winid,  fn): int  #  Notify that the tab has been dragged. Processes a  wxEVT_AUINOTEBOOK_DRAG_DONE   event.
EVT_AUINOTEBOOK_TAB_MIDDLE_DOWN(winid,  fn): int  #  The middle mouse button is pressed on a tab. Processes a  wxEVT_AUINOTEBOOK_TAB_MIDDLE_DOWN   event.
EVT_AUINOTEBOOK_TAB_MIDDLE_UP(winid,  fn): int  #  The middle mouse button is released on a tab. Processes a  wxEVT_AUINOTEBOOK_TAB_MIDDLE_UP   event.
EVT_AUINOTEBOOK_TAB_RIGHT_DOWN(winid,  fn): int  #  The right mouse button is pressed on a tab. Processes a  wxEVT_AUINOTEBOOK_TAB_RIGHT_DOWN   event.
EVT_AUINOTEBOOK_TAB_RIGHT_UP(winid,  fn): int  #  The right mouse button is released on a tab. Processes a  wxEVT_AUINOTEBOOK_TAB_RIGHT_UP   event.
EVT_AUINOTEBOOK_BG_DCLICK(winid,  fn): int  #  Double clicked on the tabs background area. Processes a  wxEVT_AUINOTEBOOK_BG_DCLICK   event. ^^


