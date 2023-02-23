# -*- coding: utf-8 -*-
from typing import Optional, Any


class RibbonArtProvider:
	""" RibbonArtProvider is responsible for drawing all the components of
the ribbon interface.
	"""
	def __init__(self) -> None:
		""" Constructor.
		"""

	def Clone(self) -> 'ribbon.RibbonArtProvider':
		""" Create a new art provider which is a clone of this one.
		"""

	def DrawButtonBarBackground(self, dc, wnd, rect) -> None:
		""" Draw the background for a   wx.ribbon.RibbonButtonBar  control.
		"""

	def DrawButtonBarButton(self, dc, wnd, rect, kind, state, label, bitmap_large, bitmap_small) -> None:
		""" Draw a single button for a   wx.ribbon.RibbonButtonBar  control.
		"""

	def DrawGalleryBackground(self, dc, wnd, rect) -> None:
		""" Draw the background and chrome for a   wx.ribbon.RibbonGallery  control.
		"""

	def DrawGalleryItemBackground(self, dc, wnd, rect, item) -> None:
		""" Draw the background of a single item in a   wx.ribbon.RibbonGallery  control.
		"""

	def DrawHelpButton(self, dc, wnd, rect) -> None:
		""" Draw help button on   wx.ribbon.RibbonBar.
		"""

	def DrawMinimisedPanel(self, dc, wnd, rect, bitmap) -> None:
		""" Draw a minimised ribbon panel.
		"""

	def DrawPageBackground(self, dc, wnd, rect) -> None:
		""" Draw the background of a ribbon page.
		"""

	def DrawPanelBackground(self, dc, wnd, rect) -> None:
		""" Draw the background and chrome for a ribbon panel.
		"""

	def DrawScrollButton(self, dc, wnd, rect, style) -> None:
		""" Draw a ribbon-style scroll button.
		"""

	def DrawTab(self, dc, wnd, tab) -> None:
		""" Draw a single tab in the tab region of a ribbon bar.
		"""

	def DrawTabCtrlBackground(self, dc, wnd, rect) -> None:
		""" Draw the background of the tab region of a ribbon bar.
		"""

	def DrawTabSeparator(self, dc, wnd, rect, visibility) -> None:
		""" Draw a separator between two tabs in a ribbon bar.
		"""

	def DrawToggleButton(self, dc, wnd, rect, mode) -> None:
		""" Draw toggle button on   wx.ribbon.RibbonBar.
		"""

	def DrawTool(self, dc, wnd, rect, bitmap, kind, state) -> None:
		""" Draw a single tool (for a   wx.ribbon.RibbonToolBar  control).
		"""

	def DrawToolBarBackground(self, dc, wnd, rect) -> None:
		""" Draw the background for a   wx.ribbon.RibbonToolBar  control.
		"""

	def DrawToolGroupBackground(self, dc, wnd, rect) -> None:
		""" Draw the background for a group of tools on a   wx.ribbon.RibbonToolBar  control.
		"""

	def GetBarTabWidth(self, dc, wnd, label, bitmap, ideal, small_begin_need_separator, small_must_have_separator, minimum) -> None:
		""" Calculate the ideal and minimum width (in pixels) of a tab in a ribbon bar.
		"""

	def GetBarToggleButtonArea(self, rect: 'Rect') -> Rect:
		""" Calculate the position and size of the ribbonâs toggle button.
		"""

	def GetButtonBarButtonSize(self, dc, wnd, kind, size, label, text_min_width, bitmap_size_large, bitmap_size_small, button_size, normal_region, dropdown_region) -> bool:
		""" Calculate the size of a button within a   wx.ribbon.RibbonButtonBar.
		"""

	def GetButtonBarButtonTextWidth(self, dc, label, kind, size) -> 'Coord':
		""" Gets the width of the string if it is used as a   wx.ribbon.RibbonButtonBar  button label.
		"""

	def GetColor(self, id: int) -> Colour:
		""" id (int) â
		"""

	def GetColour(self, id: int) -> Colour:
		""" Get the value of a certain colour setting.
		"""

	def GetColourScheme(self) -> tuple:
		""" Get the current colour scheme.
		"""

	def GetFlags(self) -> long:
		""" Get the previously set style flags.
		"""

	def GetFont(self, id: int) -> Font:
		""" Get the value of a certain font setting.
		"""

	def GetGalleryClientSize(self, dc, wnd, size, client_offset, scroll_up_button, scroll_down_button, extension_button) -> Size:
		""" Calculate the client size of a   wx.ribbon.RibbonGallery  control for a given size.
		"""

	def GetGallerySize(self, dc, wnd, client_size) -> Size:
		""" Calculate the size of a   wx.ribbon.RibbonGallery  control for a given client size.
		"""

	def GetMetric(self, id: int) -> int:
		""" Get the value of a certain integer setting.
		"""

	def GetMinimisedPanelMinimumSize(self, dc, wnd, desired_bitmap_size, expanded_panel_direction) -> Size:
		""" Calculate the size of a minimised ribbon panel.
		"""

	def GetPageBackgroundRedrawArea(self, dc, wnd, page_old_size, page_new_size) -> Rect:
		""" Calculate the portion of a page background which needs to be redrawn when a page is resized.
		"""

	def GetPanelClientSize(self, dc, wnd, size, client_offset) -> Size:
		""" Calculate the client size of a panel for a given overall size.
		"""

	def GetPanelExtButtonArea(self, dc, wnd, rect) -> Rect:
		""" Calculate the position and size of the panel extension button.
		"""

	def GetPanelSize(self, dc, wnd, client_size, client_offset) -> Size:
		""" Calculate the size of a panel for a given client size.
		"""

	def GetRibbonHelpButtonArea(self, rect: 'Rect') -> Rect:
		""" Calculate the position and size of the ribbonâs help button.
		"""

	def GetScrollButtonMinimumSize(self, dc, wnd, style) -> Size:
		""" Calculate the minimum size (in pixels) of a scroll button.
		"""

	def GetTabCtrlHeight(self, dc, wnd, pages) -> int:
		""" Calculate the height (in pixels) of the tab region of a ribbon bar.
		"""

	def GetToolSize(self, dc, wnd, bitmap_size, kind, is_first, is_last, dropdown_region) -> Size:
		""" Calculate the size of a tool within a   wx.ribbon.RibbonToolBar.
		"""

	def SetColor(self, id, color) -> None:
		""" id (int) â
		"""

	def SetColour(self, id, colour) -> None:
		""" Set the value of a certain colour setting to the value colour.
		"""

	def SetColourScheme(self, primary, secondary, tertiary) -> None:
		""" Set all applicable colour settings from a few base colours.
		"""

	def SetFlags(self, flags: long) -> None:
		""" Set the style flags.
		"""

	def SetFont(self, id, font) -> None:
		""" Set the value of a certain font setting to the value font.
		"""

	def SetMetric(self, id, new_val) -> None:
		""" Set the value of a certain integer setting to the value new_val.
		"""



class RibbonAUIArtProvider('ribbon.RibbonMSWArtProvider'):
	""" Create a new art provider which is a clone of this one.
	"""
	def __init__(self) -> None:
		""" 
		"""

	def Clone(self) -> 'ribbon.RibbonArtProvider':
		""" Create a new art provider which is a clone of this one.
		"""

	def DrawButtonBarBackground(self, dc, wnd, rect) -> None:
		""" Draw the background for a   wx.ribbon.RibbonButtonBar  control.
		"""

	def DrawButtonBarButton(self, dc, wnd, rect, kind, state, label, bitmap_large, bitmap_small) -> None:
		""" Draw a single button for a   wx.ribbon.RibbonButtonBar  control.
		"""

	def DrawGalleryBackground(self, dc, wnd, rect) -> None:
		""" Draw the background and chrome for a   wx.ribbon.RibbonGallery  control.
		"""

	def DrawGalleryItemBackground(self, dc, wnd, rect, item) -> None:
		""" Draw the background of a single item in a   wx.ribbon.RibbonGallery  control.
		"""

	def DrawMinimisedPanel(self, dc, wnd, rect, bitmap) -> None:
		""" Draw a minimised ribbon panel.
		"""

	def DrawPageBackground(self, dc, wnd, rect) -> None:
		""" Draw the background of a ribbon page.
		"""

	def DrawPanelBackground(self, dc, wnd, rect) -> None:
		""" Draw the background and chrome for a ribbon panel.
		"""

	def DrawScrollButton(self, dc, wnd, rect, style) -> None:
		""" Draw a ribbon-style scroll button.
		"""

	def DrawTab(self, dc, wnd, tab) -> None:
		""" Draw a single tab in the tab region of a ribbon bar.
		"""

	def DrawTabCtrlBackground(self, dc, wnd, rect) -> None:
		""" Draw the background of the tab region of a ribbon bar.
		"""

	def DrawTabSeparator(self, dc, wnd, rect, visibility) -> None:
		""" Draw a separator between two tabs in a ribbon bar.
		"""

	def DrawTool(self, dc, wnd, rect, bitmap, kind, state) -> None:
		""" Draw a single tool (for a   wx.ribbon.RibbonToolBar  control).
		"""

	def DrawToolBarBackground(self, dc, wnd, rect) -> None:
		""" Draw the background for a   wx.ribbon.RibbonToolBar  control.
		"""

	def DrawToolGroupBackground(self, dc, wnd, rect) -> None:
		""" Draw the background for a group of tools on a   wx.ribbon.RibbonToolBar  control.
		"""

	def GetBarTabWidth(self, dc, wnd, label, bitmap, ideal, small_begin_need_separator, small_must_have_separator, minimum) -> None:
		""" Calculate the ideal and minimum width (in pixels) of a tab in a ribbon bar.
		"""

	def GetColour(self, id: int) -> Colour:
		""" Get the value of a certain colour setting.
		"""

	def GetPanelClientSize(self, dc, wnd, size, client_offset) -> Size:
		""" Calculate the client size of a panel for a given overall size.
		"""

	def GetPanelExtButtonArea(self, dc, wnd, rect) -> Rect:
		""" Calculate the position and size of the panel extension button.
		"""

	def GetPanelSize(self, dc, wnd, client_size, client_offset) -> Size:
		""" Calculate the size of a panel for a given client size.
		"""

	def GetScrollButtonMinimumSize(self, dc, wnd, style) -> Size:
		""" Calculate the minimum size (in pixels) of a scroll button.
		"""

	def GetTabCtrlHeight(self, dc, wnd, pages) -> int:
		""" Calculate the height (in pixels) of the tab region of a ribbon bar.
		"""

	def SetColour(self, id, colour) -> None:
		""" Set the value of a certain colour setting to the value colour.
		"""

	def SetColourScheme(self, primary, secondary, tertiary) -> None:
		""" Set all applicable colour settings from a few base colours.
		"""

	def SetFont(self, id, font) -> None:
		""" Set the value of a certain font setting to the value font.
		"""



class RibbonBar('ribbon.RibbonControl'):
	""" Top-level control in a ribbon user interface.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def AddPageHighlight(self, page, highlight=True) -> None:
		""" Highlight the specified tab.
		"""

	def ArePanelsShown(self) -> bool:
		""" Indicates whether the panel area of the ribbon bar is shown.
		"""

	def ClearPages(self) -> None:
		""" Delete all pages from the ribbon bar.
		"""

	def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=RIBBON_BAR_DEFAULT_STYLE) -> bool:
		""" Create a ribbon bar in two-step ribbon bar construction.
		"""

	def DeletePage(self, n: int) -> None:
		""" Delete a single page from this ribbon bar.
		"""

	def DismissExpandedPanel(self) -> bool:
		""" Dismiss the expanded panel of the currently active page.
		"""

	def GetActivePage(self) -> int:
		""" Get the index of the active page.
		"""

	@staticmethod
	def GetClassDefaultAttributes(variant: WindowVariant=WINDOW_VARIANT_NORMAL) -> VisualAttributes:
		""" variant (WindowVariant) â
		"""

	def GetDisplayMode(self) -> 'ribbon.RibbonDisplayMode':
		""" Returns the current display mode of the panel area.
		"""

	def GetPage(self, n: int) -> 'ribbon.RibbonPage':
		""" Get a page by index.
		"""

	def GetPageCount(self) -> int:
		""" Get the number of pages in this bar.
		"""

	def GetPageNumber(self, page: 'ribbon.RibbonPage') -> int:
		""" Returns the number for a given ribbon bar page.
		"""

	def HidePage(self, page: int) -> None:
		""" Hides the tab for a given page.
		"""

	def HidePanels(self) -> None:
		""" Hides the panel area of the ribbon bar.
		"""

	def IsPageHighlighted(self, page: int) -> bool:
		""" Indicates whether a tab is currently highlighted.
		"""

	def IsPageShown(self, page: int) -> bool:
		""" Indicates whether the tab for the given page is shown to the user or not.
		"""

	def Realize(self) -> bool:
		""" Perform initial layout and size calculations of the bar and its children.
		"""

	def RemovePageHighlight(self, page: int) -> None:
		""" Changes a tab to not be highlighted.
		"""

	def SetActivePage(self, *args, **kw) -> bool:
		""" Overloaded Implementations:
		"""

	def SetArtProvider(self, art: 'ribbon.RibbonArtProvider') -> None:
		""" Set the art provider to be used be the ribbon bar.
		"""

	def SetTabCtrlMargins(self, left, right) -> None:
		""" Set the margin widths (in pixels) on the left and right sides of the tab bar region of the ribbon bar.
		"""

	def ShowPage(self, page, show_tab=True) -> None:
		""" Show or hide the tab for a given page.
		"""

	def ShowPanels(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

ribbon.RIBBON_BAR_DEFAULT_STYLE: int  #  Defined as wx.ribbon.RIBBON_BAR_FLOW_HORIZONTAL | wx.ribbon.RIBBON_BAR_SHOW_PAGE_LABELS | wx.ribbon.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS | wx.ribbon.RIBBON_BAR_SHOW_TOGGLE_BUTTON | wx.ribbon.RIBBON_BAR_SHOW_HELP_BUTTON.
ribbon.RIBBON_BAR_FOLDBAR_STYLE: int  #  Defined as wx.ribbon.RIBBON_BAR_FLOW_VERTICAL | wx.ribbon.RIBBON_BAR_SHOW_PAGE_ICONS | wx.ribbon.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS | wx.ribbon.RIBBON_BAR_SHOW_PANEL_MINIMISE_BUTTONS
ribbon.RIBBON_BAR_SHOW_PAGE_LABELS: int  #  Causes labels to be shown on the tabs in the ribbon bar.
ribbon.RIBBON_BAR_SHOW_PAGE_ICONS: int  #  Causes icons to be shown on the tabs in the ribbon bar.
ribbon.RIBBON_BAR_FLOW_HORIZONTAL: int  #  Causes panels within pages to stack horizontally.
ribbon.RIBBON_BAR_FLOW_VERTICAL: int  #  Causes panels within pages to stack vertically.
ribbon.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS: int  #  Causes extension buttons to be shown on panels (where the panel has such a button).
ribbon.RIBBON_BAR_SHOW_PANEL_MINIMISE_BUTTONS: int  #  Causes minimise buttons to be shown on panels (where the panel has such a button).
ribbon.RIBBON_BAR_SHOW_TOGGLE_BUTTON: int  #  Causes a toggle button to appear on the ribbon bar at top-right corner. This style is new since wxWidgets 2.9.5.
ribbon.RIBBON_BAR_SHOW_HELP_BUTTON: int  #  Causes a help button to appear on the ribbon bar at the top-right corner. This style is new since wxWidgets 2.9.5. ^^
EVT_RIBBONBAR_PAGE_CHANGED: int  #  Triggered after the transition from one page being active to a different page being active.
EVT_RIBBONBAR_PAGE_CHANGING: int  #  Triggered prior to the transition from one page being active to a different page being active, and can veto the change.
EVT_RIBBONBAR_TAB_MIDDLE_DOWN: int  #  Triggered when the middle mouse button is pressed on a tab.
EVT_RIBBONBAR_TAB_MIDDLE_UP: int  #  Triggered when the middle mouse button is released on a tab.
EVT_RIBBONBAR_TAB_RIGHT_DOWN: int  #  Triggered when the right mouse button is pressed on a tab.
EVT_RIBBONBAR_TAB_RIGHT_UP: int  #  Triggered when the right mouse button is released on a tab.
EVT_RIBBONBAR_TAB_LEFT_DCLICK: int  #  Triggered when the left mouse button is double clicked on a tab.
EVT_RIBBONBAR_TOGGLED: int  #  Triggered when the button triggering the ribbon bar is clicked. This event is new since wxWidgets 2.9.5.
EVT_RIBBONBAR_HELP_CLICK: int  #  Triggered when the help button is clicked. This even is new since wxWidgets 2.9.5. ^^


class RibbonBarEvent('NotifyEvent'):
	""" Event used to indicate various actions relating to a RibbonBar.
	"""
	def __init__(self, command_type=wxEVT_NULL, win_id=0, page=None) -> None:
		""" Constructor.
		"""

	def GetPage(self) -> 'ribbon.RibbonPage':
		""" Returns the page being changed to, or being clicked on.
		"""

	def SetPage(self, page: 'ribbon.RibbonPage') -> None:
		""" Sets the page relating to this event.
		"""



class RibbonButtonBar('ribbon.RibbonControl'):
	""" A ribbon button bar is similar to a traditional toolbar.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def AddButton(self, *args, **kw) -> RibbonButtonBarButtonBase:
		""" Overloaded Implementations:
		"""

	def AddDropdownButton(self, button_id, label, bitmap, help_string="") -> RibbonButtonBarButtonBase:
		""" Add a dropdown button to the button bar (simple version).
		"""

	def AddHybridButton(self, button_id, label, bitmap, help_string="") -> RibbonButtonBarButtonBase:
		""" Add a hybrid button to the button bar (simple version).
		"""

	def AddToggleButton(self, button_id, label, bitmap, help_string="") -> RibbonButtonBarButtonBase:
		""" Add a toggle button to the button bar (simple version).
		"""

	def ClearButtons(self) -> None:
		""" Delete all buttons from the button bar.
		"""

	def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
		""" Create a button bar in two-step button bar construction.
		"""

	def DeleteButton(self, button_id: int) -> bool:
		""" Delete a single button from the button bar.
		"""

	def EnableButton(self, button_id, enable=True) -> None:
		""" Enable or disable a single button on the bar.
		"""

	def GetActiveItem(self) -> RibbonButtonBarButtonBase:
		""" Returns the active item of the button bar or None if there is none.
		"""

	def GetButtonCount(self) -> int:
		""" Returns the number of buttons in this button bar.
		"""

	@staticmethod
	def GetClassDefaultAttributes(variant: WindowVariant=WINDOW_VARIANT_NORMAL) -> VisualAttributes:
		""" variant (WindowVariant) â
		"""

	def GetHoveredItem(self) -> RibbonButtonBarButtonBase:
		""" Returns the hovered item of the button bar or None if there is none.
		"""

	def GetItem(self, n: int) -> RibbonButtonBarButtonBase:
		""" Returns the N-th button of the bar.
		"""

	def GetItemById(self, id: int) -> RibbonButtonBarButtonBase:
		""" Returns the first button having a given id or None if none matches.
		"""

	def GetItemClientData(self, item: RibbonButtonBarButtonBase) -> ClientData:
		""" Get the client object associated with a button.
		"""

	def GetItemId(self, item: RibbonButtonBarButtonBase) -> int:
		""" Returns the id of a button.
		"""

	def GetItemRect(self, button_id: int) -> Rect:
		""" Returns the itemsâs rect with coordinates relative to the button barâs parent, or a default-constructed rect if the tool is not found.
		"""

	def GetShowToolTipsForDisabled(self) -> bool:
		""" Sets whether tooltips should be shown for disabled buttons or not.
		"""

	def InsertButton(self, *args, **kw) -> RibbonButtonBarButtonBase:
		""" Overloaded Implementations:
		"""

	def InsertDropdownButton(self, pos, button_id, label, bitmap, help_string="") -> RibbonButtonBarButtonBase:
		""" Inserts a dropdown button to the button bar (simple version) at the given position.
		"""

	def InsertHybridButton(self, pos, button_id, label, bitmap, help_string="") -> RibbonButtonBarButtonBase:
		""" Inserts a hybrid button to the button bar (simple version) at the given position.
		"""

	def InsertToggleButton(self, pos, button_id, label, bitmap, help_string="") -> RibbonButtonBarButtonBase:
		""" Inserts a toggle button to the button bar (simple version) at the given position.
		"""

	def Realize(self) -> bool:
		""" Calculate button layouts and positions.
		"""

	def SetButtonIcon(self, button_id, bitmap, bitmap_small=NullBitmap, bitmap_disabled=NullBitmap, bitmap_small_disabled=NullBitmap) -> None:
		""" Changes the bitmap of an existing button.
		"""

	def SetButtonMaxSizeClass(self, button_id, max_size_class) -> None:
		""" Sets the maximum size class of a ribbon button.
		"""

	def SetButtonMinSizeClass(self, button_id, min_size_class) -> None:
		""" Sets the minimum size class of a ribbon button.
		"""

	def SetButtonText(self, button_id, label) -> None:
		""" Changes the label text of an existing button.
		"""

	def SetButtonTextMinWidth(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def SetItemClientData(self, item, data) -> None:
		""" Set the client object associated with a button.
		"""

	def SetShowToolTipsForDisabled(self, show: bool) -> None:
		""" Indicates whether tooltips are shown for disabled buttons.
		"""

	def ToggleButton(self, button_id, checked) -> None:
		""" Set a toggle button to the checked or unchecked state.
		"""

EVT_RIBBONBUTTONBAR_CLICKED: int  #  Triggered when the normal (non-dropdown) region of a button on the button bar is clicked.
EVT_RIBBONBUTTONBAR_DROPDOWN_CLICKED: int  #  Triggered when the dropdown region of a button on the button bar is clicked. wx.ribbon.RibbonButtonBarEvent.PopupMenu   should be called by the event handler if it wants to display a popup menu (which is what most dropdown buttons should be doing). ^^


class RibbonButtonBarEvent('CommandEvent'):
	""" Event used to indicate various actions relating to a button on a
RibbonButtonBar.
	"""
	def __init__(self, command_type=wxEVT_NULL, win_id=0, bar=None, button=None) -> None:
		""" Constructor.
		"""

	def GetBar(self) -> 'ribbon.RibbonButtonBar':
		""" Returns the bar which contains the button which the event relates to.
		"""

	def GetButton(self) -> RibbonButtonBarButtonBase:
		""" Returns the button which the event relates to.
		"""

	def PopupMenu(self, menu: 'Menu') -> bool:
		""" Display a popup menu as a result of this (dropdown clicked) event.
		"""

	def SetBar(self, bar: 'ribbon.RibbonButtonBar') -> None:
		""" Sets the button bar relating to this event.
		"""

	def SetButton(self, bar: RibbonButtonBarButtonBase) -> None:
		""" Sets the button relating to this event.
		"""



class RibbonControl('Control'):
	""" RibbonControl serves as a base class for all controls which share
the ribbon characteristics of having a ribbon art provider, and
(optionally) non-continuous resizing.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def DoGetNextLargerSize(self, direction, relative_to) -> Size:
		""" Implementation of GetNextLargerSize .
		"""

	def DoGetNextSmallerSize(self, direction, relative_to) -> Size:
		""" Implementation of GetNextSmallerSize .
		"""

	def GetAncestorRibbonBar(self) -> 'ribbon.RibbonBar':
		""" Get the first ancestor which is a   wx.ribbon.RibbonBar  (or derived) or None if not having such parent.
		"""

	def GetArtProvider(self) -> 'ribbon.RibbonArtProvider':
		""" Get the art provider to be used.
		"""

	def GetBestSizeForParentSize(self, parentSize: 'Size') -> Size:
		""" Finds the best width and height given the parentâs width and height.
		"""

	@staticmethod
	def GetClassDefaultAttributes(variant: WindowVariant=WINDOW_VARIANT_NORMAL) -> VisualAttributes:
		""" variant (WindowVariant) â
		"""

	def GetNextLargerSize(self, *args, **kw) -> Size:
		""" Overloaded Implementations:
		"""

	def GetNextSmallerSize(self, *args, **kw) -> Size:
		""" Overloaded Implementations:
		"""

	def IsSizingContinuous(self) -> bool:
		""" bool
		"""

	def Realise(self) -> bool:
		""" Alias for Realize .
		"""

	def Realize(self) -> bool:
		""" Perform initial size and layout calculations after children have been added, and/or realize children.
		"""

	def SetArtProvider(self, art: 'ribbon.RibbonArtProvider') -> None:
		""" Set the art provider to be used.
		"""



class RibbonGallery('ribbon.RibbonControl'):
	""" A ribbon gallery is like a ListBox, but for bitmaps rather than
strings.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def Append(self, *args, **kw) -> RibbonGalleryItem:
		""" Overloaded Implementations:
		"""

	def Clear(self) -> None:
		""" Remove all items from the gallery.
		"""

	def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
		""" Create a gallery in two-step gallery construction.
		"""

	def EnsureVisible(self, item: RibbonGalleryItem) -> None:
		""" Scroll the gallery to ensure that the given item is visible.
		"""

	def GetActiveItem(self) -> RibbonGalleryItem:
		""" Get the currently active item, or None if there is none.
		"""

	@staticmethod
	def GetClassDefaultAttributes(variant: WindowVariant=WINDOW_VARIANT_NORMAL) -> VisualAttributes:
		""" variant (WindowVariant) â
		"""

	def GetCount(self) -> int:
		""" Get the number of items in the gallery.
		"""

	def GetDownButtonState(self) -> 'ribbon.RibbonGalleryButtonState':
		""" Get the state of the scroll down button.
		"""

	def GetExtensionButtonState(self) -> 'ribbon.RibbonGalleryButtonState':
		""" Get the state of the âextensionâ button.
		"""

	def GetHoveredItem(self) -> RibbonGalleryItem:
		""" Get the currently hovered item, or None if there is none.
		"""

	def GetItem(self, n: int) -> RibbonGalleryItem:
		""" Get an item by index.
		"""

	def GetItemClientData(self, item: RibbonGalleryItem) -> ClientData:
		""" Get the client object associated with a gallery item.
		"""

	def GetSelection(self) -> RibbonGalleryItem:
		""" Get the currently selected item, or None if there is none.
		"""

	def GetUpButtonState(self) -> 'ribbon.RibbonGalleryButtonState':
		""" Get the state of the scroll up button.
		"""

	def IsEmpty(self) -> bool:
		""" Query if the gallery has no items in it.
		"""

	def IsHovered(self) -> bool:
		""" Query is the mouse is currently hovered over the gallery.
		"""

	def ScrollLines(self, lines: int) -> bool:
		""" Scroll the gallery contents by some amount.
		"""

	def ScrollPixels(self, pixels: int) -> bool:
		""" Scroll the gallery contents by some fine-grained amount.
		"""

	def SetItemClientData(self, item, data) -> None:
		""" Set the client object associated with a gallery item.
		"""

	def SetSelection(self, item: RibbonGalleryItem) -> None:
		""" Set the selection to the given item, or removes the selection if item  == None.
		"""

EVT_RIBBONGALLERY_SELECTED: int  #  Triggered when the user selects an item from the gallery. Note that the ID is that of the gallery, not of the item.
EVT_RIBBONGALLERY_CLICKED: int  #  Similar to EVT_RIBBONGALLERY_SELECTED but triggered every time a gallery item is clicked, even if it is already selected. Note that the ID of the event is that of the gallery, not of the item, just as above. This event is available since wxWidgets 2.9.2.
EVT_RIBBONGALLERY_HOVER_CHANGED: int  #  Triggered when the item being hovered over by the user changes. The item in the event will be the new item being hovered, or None if there is no longer an item being hovered. Note that the ID is that of the gallery, not of the item. ^^ ^^


class RibbonGalleryEvent('CommandEvent'):
	""" Constructor.
	"""
	def __init__(self, command_type=wxEVT_NULL, win_id=0, gallery=None, item=None) -> None:
		""" Constructor.
		"""

	def GetGallery(self) -> 'ribbon.RibbonGallery':
		""" Returns the gallery which the event relates to.
		"""

	def GetGalleryItem(self) -> RibbonGalleryItem:
		""" Returns the gallery item which the event relates to, or None if it does not relate to an item.
		"""

	def SetGallery(self, gallery: 'ribbon.RibbonGallery') -> None:
		""" Sets the gallery relating to this event.
		"""

	def SetGalleryItem(self, item: RibbonGalleryItem) -> None:
		""" Sets the gallery item relating to this event.
		"""



class RibbonMSWArtProvider('ribbon.RibbonArtProvider'):
	""" set_colour_scheme (bool) â 
	"""
	def __init__(self, set_colour_scheme: bool=True) -> None:
		""" set_colour_scheme (bool) â
		"""

	def Clone(self) -> 'ribbon.RibbonArtProvider':
		""" Create a new art provider which is a clone of this one.
		"""

	def DrawButtonBarBackground(self, dc, wnd, rect) -> None:
		""" Draw the background for a   wx.ribbon.RibbonButtonBar  control.
		"""

	def DrawButtonBarButton(self, dc, wnd, rect, kind, state, label, bitmap_large, bitmap_small) -> None:
		""" Draw a single button for a   wx.ribbon.RibbonButtonBar  control.
		"""

	def DrawGalleryBackground(self, dc, wnd, rect) -> None:
		""" Draw the background and chrome for a   wx.ribbon.RibbonGallery  control.
		"""

	def DrawGalleryItemBackground(self, dc, wnd, rect, item) -> None:
		""" Draw the background of a single item in a   wx.ribbon.RibbonGallery  control.
		"""

	def DrawHelpButton(self, dc, wnd, rect) -> None:
		""" Draw help button on   wx.ribbon.RibbonBar.
		"""

	def DrawMinimisedPanel(self, dc, wnd, rect, bitmap) -> None:
		""" Draw a minimised ribbon panel.
		"""

	def DrawPageBackground(self, dc, wnd, rect) -> None:
		""" Draw the background of a ribbon page.
		"""

	def DrawPanelBackground(self, dc, wnd, rect) -> None:
		""" Draw the background and chrome for a ribbon panel.
		"""

	def DrawScrollButton(self, dc, wnd, rect, style) -> None:
		""" Draw a ribbon-style scroll button.
		"""

	def DrawTab(self, dc, wnd, tab) -> None:
		""" Draw a single tab in the tab region of a ribbon bar.
		"""

	def DrawTabCtrlBackground(self, dc, wnd, rect) -> None:
		""" Draw the background of the tab region of a ribbon bar.
		"""

	def DrawTabSeparator(self, dc, wnd, rect, visibility) -> None:
		""" Draw a separator between two tabs in a ribbon bar.
		"""

	def DrawToggleButton(self, dc, wnd, rect, mode) -> None:
		""" Draw toggle button on   wx.ribbon.RibbonBar.
		"""

	def DrawTool(self, dc, wnd, rect, bitmap, kind, state) -> None:
		""" Draw a single tool (for a   wx.ribbon.RibbonToolBar  control).
		"""

	def DrawToolBarBackground(self, dc, wnd, rect) -> None:
		""" Draw the background for a   wx.ribbon.RibbonToolBar  control.
		"""

	def DrawToolGroupBackground(self, dc, wnd, rect) -> None:
		""" Draw the background for a group of tools on a   wx.ribbon.RibbonToolBar  control.
		"""

	def GetBarTabWidth(self, dc, wnd, label, bitmap, ideal, small_begin_need_separator, small_must_have_separator, minimum) -> None:
		""" Calculate the ideal and minimum width (in pixels) of a tab in a ribbon bar.
		"""

	def GetBarToggleButtonArea(self, rect: 'Rect') -> Rect:
		""" Calculate the position and size of the ribbonâs toggle button.
		"""

	def GetButtonBarButtonSize(self, dc, wnd, kind, size, label, text_min_width, bitmap_size_large, bitmap_size_small, button_size, normal_region, dropdown_region) -> bool:
		""" Calculate the size of a button within a   wx.ribbon.RibbonButtonBar.
		"""

	def GetButtonBarButtonTextWidth(self, dc, label, kind, size) -> 'Coord':
		""" Gets the width of the string if it is used as a   wx.ribbon.RibbonButtonBar  button label.
		"""

	def GetColour(self, id: int) -> Colour:
		""" Get the value of a certain colour setting.
		"""

	def GetColourScheme(self) -> tuple:
		""" Get the current colour scheme.
		"""

	def GetFlags(self) -> long:
		""" Get the previously set style flags.
		"""

	def GetFont(self, id: int) -> Font:
		""" Get the value of a certain font setting.
		"""

	def GetGalleryClientSize(self, dc, wnd, size, client_offset, scroll_up_button, scroll_down_button, extension_button) -> Size:
		""" Calculate the client size of a   wx.ribbon.RibbonGallery  control for a given size.
		"""

	def GetGallerySize(self, dc, wnd, client_size) -> Size:
		""" Calculate the size of a   wx.ribbon.RibbonGallery  control for a given client size.
		"""

	def GetMetric(self, id: int) -> int:
		""" Get the value of a certain integer setting.
		"""

	def GetMinimisedPanelMinimumSize(self, dc, wnd, desired_bitmap_size, expanded_panel_direction) -> Size:
		""" Calculate the size of a minimised ribbon panel.
		"""

	def GetPageBackgroundRedrawArea(self, dc, wnd, page_old_size, page_new_size) -> Rect:
		""" Calculate the portion of a page background which needs to be redrawn when a page is resized.
		"""

	def GetPanelClientSize(self, dc, wnd, size, client_offset) -> Size:
		""" Calculate the client size of a panel for a given overall size.
		"""

	def GetPanelExtButtonArea(self, dc, wnd, rect) -> Rect:
		""" Calculate the position and size of the panel extension button.
		"""

	def GetPanelSize(self, dc, wnd, client_size, client_offset) -> Size:
		""" Calculate the size of a panel for a given client size.
		"""

	def GetRibbonHelpButtonArea(self, rect: 'Rect') -> Rect:
		""" Calculate the position and size of the ribbonâs help button.
		"""

	def GetScrollButtonMinimumSize(self, dc, wnd, style) -> Size:
		""" Calculate the minimum size (in pixels) of a scroll button.
		"""

	def GetTabCtrlHeight(self, dc, wnd, pages) -> int:
		""" Calculate the height (in pixels) of the tab region of a ribbon bar.
		"""

	def GetToolSize(self, dc, wnd, bitmap_size, kind, is_first, is_last, dropdown_region) -> Size:
		""" Calculate the size of a tool within a   wx.ribbon.RibbonToolBar.
		"""

	def SetColour(self, id, colour) -> None:
		""" Set the value of a certain colour setting to the value colour.
		"""

	def SetColourScheme(self, primary, secondary, tertiary) -> None:
		""" Set all applicable colour settings from a few base colours.
		"""

	def SetFlags(self, flags: long) -> None:
		""" Set the style flags.
		"""

	def SetFont(self, id, font) -> None:
		""" Set the value of a certain font setting to the value font.
		"""

	def SetMetric(self, id, new_val) -> None:
		""" Set the value of a certain integer setting to the value new_val.
		"""



class RibbonPage('ribbon.RibbonControl'):
	""" Container for related ribbon panels, and a tab within a ribbon bar.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def AdjustRectToIncludeScrollButtons(self, rect: 'Rect') -> None:
		""" Expand a rectangle of the page to include external scroll buttons (if any).
		"""

	def Create(self, parent, id=ID_ANY, label="", icon=NullBitmap, style=0) -> bool:
		""" Create a ribbon page in two-step ribbon page construction.
		"""

	def DismissExpandedPanel(self) -> bool:
		""" Dismiss the current externally expanded panel, if there is one.
		"""

	@staticmethod
	def GetClassDefaultAttributes(variant: WindowVariant=WINDOW_VARIANT_NORMAL) -> VisualAttributes:
		""" variant (WindowVariant) â
		"""

	def GetIcon(self) -> Bitmap:
		""" Get the icon used for the page in the ribbon bar tab area (only displayed if the ribbon bar is actually showing icons).
		"""

	def GetMajorAxis(self) -> 'Orientation':
		""" Get the direction in which ribbon panels are stacked within the page.
		"""

	def Realize(self) -> bool:
		""" Perform a full re-layout of all panels on the page.
		"""

	def ScrollLines(self, lines: int) -> bool:
		""" Scroll the page by some amount up / down / left / right.
		"""

	def ScrollPixels(self, pixels: int) -> bool:
		""" Scroll the page by a set number of pixels up / down / left / right.
		"""

	def ScrollSections(self, sections: int) -> bool:
		""" Scroll the page by an entire child section.
		"""

	def SetArtProvider(self, art: 'ribbon.RibbonArtProvider') -> None:
		""" Set the art provider to be used.
		"""

	def SetSizeWithScrollButtonAdjustment(self, x, y, width, height) -> None:
		""" Set the size of the page and the external scroll buttons (if any).
		"""



class RibbonPageTabInfo:
	""" A public C++ attribute of type bool.
	"""


class RibbonPanel('ribbon.RibbonControl'):
	""" Serves as a container for a group of (ribbon) controls.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def CanAutoMinimise(self) -> bool:
		""" Query if the panel can automatically minimise itself at small sizes.
		"""

	def Create(self, parent, id=ID_ANY, label="", icon=NullBitmap, pos=DefaultPosition, size=DefaultSize, style=RIBBON_PANEL_DEFAULT_STYLE) -> bool:
		""" Create a ribbon panel in two-step ribbon panel construction.
		"""

	@staticmethod
	def GetClassDefaultAttributes(variant: WindowVariant=WINDOW_VARIANT_NORMAL) -> VisualAttributes:
		""" variant (WindowVariant) â
		"""

	def GetExpandedDummy(self) -> 'ribbon.RibbonPanel':
		""" Get the dummy panel of an expanded panel.
		"""

	def GetExpandedPanel(self) -> 'ribbon.RibbonPanel':
		""" Get the expanded panel of a dummy panel.
		"""

	def GetMinimisedIcon(self) -> Bitmap:
		""" Get the bitmap to be used in place of the panel children when it is minimised.
		"""

	def HasExtButton(self) -> bool:
		""" Test if the panel has an extension button.
		"""

	def HideExpanded(self) -> bool:
		""" Hide the panelâs external expansion.
		"""

	def IsExtButtonHovered(self) -> bool:
		""" Query if the mouse is currently hovered over the extension button.
		"""

	def IsHovered(self) -> bool:
		""" Query is the mouse is currently hovered over the panel.
		"""

	def IsMinimised(self, *args, **kw) -> bool:
		""" Overloaded Implementations:
		"""

	def Realize(self) -> bool:
		""" Realize all children of the panel.
		"""

	def SetArtProvider(self, art: 'ribbon.RibbonArtProvider') -> None:
		""" Set the art provider to be used.
		"""

	def ShowExpanded(self) -> bool:
		""" Show the panel externally expanded.
		"""

ribbon.RIBBON_PANEL_DEFAULT_STYLE: int  #  Defined as no other flags set.
ribbon.RIBBON_PANEL_NO_AUTO_MINIMISE: int  #  Prevents the panel from automatically minimising to conserve screen space.
ribbon.RIBBON_PANEL_EXT_BUTTON: int  #  Causes an extension button to be shown in the panelâs chrome (if the bar in which it is contained has wx.ribbon.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS set). The behaviour of this button is application controlled, but typically will show an extended drop-down menu relating to the panel.
ribbon.RIBBON_PANEL_MINIMISE_BUTTON: int  #  Causes a (de)minimise button to be shown in the panelâs chrome (if the bar in which it is contained has the wx.ribbon.RIBBON_BAR_SHOW_PANEL_MINIMISE_BUTTONS style set). This flag is typically combined with wx.ribbon.RIBBON_PANEL_NO_AUTO_MINIMISE to make a panel which the user always has manual control over when it minimises.
ribbon.RIBBON_PANEL_STRETCH: int  #  Stretches a single panel to fit the parent page.
ribbon.RIBBON_PANEL_FLEXIBLE: int  #  Allows the panel to size in both directions; currently only useful when a single   wx.ribbon.RibbonToolBar  is the child of the panel, particularly in vertical orientation where the number of rows is dependent on the amount of horizontal space available. Set the minimum and maximum toolbar rows to take full advantage of this wrapping behaviour. ^^
EVT_RIBBONPANEL_EXTBUTTON_ACTIVATED: int  #  Triggered when the user activate the panel extension button. ^^


class RibbonPanelEvent('CommandEvent'):
	""" Event used to indicate various actions relating to a RibbonPanel.
	"""
	def __init__(self, command_type=wxEVT_NULL, win_id=0, panel=None) -> None:
		""" Constructor.
		"""

	def GetPanel(self) -> 'ribbon.RibbonPanel':
		""" Returns the panel relating to this event.
		"""

	def SetPanel(self, page: 'ribbon.RibbonPanel') -> None:
		""" Sets the page relating to this event.
		"""



class RibbonToolBar('ribbon.RibbonControl'):
	""" A ribbon tool bar is similar to a traditional toolbar which has no
labels.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def AddDropdownTool(self, tool_id, bitmap, help_string="") -> RibbonToolBarToolBase:
		""" Add a dropdown tool to the tool bar (simple version).
		"""

	def AddHybridTool(self, tool_id, bitmap, help_string="") -> RibbonToolBarToolBase:
		""" Add a hybrid tool to the tool bar (simple version).
		"""

	def AddSeparator(self) -> RibbonToolBarToolBase:
		""" Add a separator to the tool bar.
		"""

	def AddToggleTool(self, tool_id, bitmap, help_string) -> RibbonToolBarToolBase:
		""" Add a toggle tool to the tool bar (simple version).
		"""

	def AddTool(self, *args, **kw) -> RibbonToolBarToolBase:
		""" Overloaded Implementations:
		"""

	def ClearTools(self) -> None:
		""" Deletes all the tools in the toolbar.
		"""

	def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
		""" Create a tool bar in two-step tool bar construction.
		"""

	def DeleteTool(self, tool_id: int) -> bool:
		""" Removes the specified tool from the toolbar and deletes it.
		"""

	def DeleteToolByPos(self, pos: int) -> bool:
		""" This function behaves like DeleteTool   but it deletes the tool at the specified position and not the one with the given id.
		"""

	def EnableTool(self, tool_id, enable=True) -> None:
		""" Enable or disable a single tool on the bar.
		"""

	def FindById(self, tool_id: int) -> RibbonToolBarToolBase:
		""" Returns a pointer to the tool opaque structure by id  or None if no corresponding tool is found.
		"""

	def GetActiveTool(self) -> RibbonToolBarToolBase:
		""" Returns the active item of the tool bar or None if there is none.
		"""

	@staticmethod
	def GetClassDefaultAttributes(variant: WindowVariant=WINDOW_VARIANT_NORMAL) -> VisualAttributes:
		""" variant (WindowVariant) â
		"""

	def GetToolByPos(self, *args, **kw) -> RibbonToolBarToolBase:
		""" Overloaded Implementations:
		"""

	def GetToolClientData(self, tool_id: int) -> PyUserData:
		""" Get any client data associated with the tool.
		"""

	def GetToolCount(self) -> int:
		""" Returns the number of tools in the toolbar.
		"""

	def GetToolEnabled(self, tool_id: int) -> bool:
		""" Called to determine whether a tool is enabled (responds to user input).
		"""

	def GetToolHelpString(self, tool_id: int) -> str:
		""" Returns the help string for the given tool.
		"""

	def GetToolId(self, tool: RibbonToolBarToolBase) -> int:
		""" Return the id associated to the tool opaque structure.
		"""

	def GetToolKind(self, tool_id: int) -> 'ribbon.RibbonButtonKind':
		""" Return the kind of the given tool.
		"""

	def GetToolPos(self, tool_id: int) -> int:
		""" Returns the tool position in the toolbar, or  NOT_FOUND   if the tool is not found.
		"""

	def GetToolRect(self, tool_id: int) -> Rect:
		""" Returns the toolâs rect with coordinates relative to the toolbarâs parent, or a default-constructed rect if the tool is not found.
		"""

	def GetToolState(self, tool_id: int) -> bool:
		""" Gets the on/off state of a toggle tool.
		"""

	def InsertDropdownTool(self, pos, tool_id, bitmap, help_string="") -> RibbonToolBarToolBase:
		""" Insert a dropdown tool to the tool bar (simple version) as the specified position.
		"""

	def InsertHybridTool(self, pos, tool_id, bitmap, help_string="") -> RibbonToolBarToolBase:
		""" Insert a hybrid tool to the tool bar (simple version) as the specified position.
		"""

	def InsertSeparator(self, pos: int) -> RibbonToolBarToolBase:
		""" Insert a separator to the tool bar at the specified position.
		"""

	def InsertToggleTool(self, pos, tool_id, bitmap, help_string="") -> RibbonToolBarToolBase:
		""" Insert a toggle tool to the tool bar (simple version) as the specified position.
		"""

	def InsertTool(self, *args, **kw) -> RibbonToolBarToolBase:
		""" Overloaded Implementations:
		"""

	def Realize(self) -> bool:
		""" Calculate tool layouts and positions.
		"""

	def SetRows(self, nMin, nMax=-1) -> None:
		""" Set the number of rows to distribute tool groups over.
		"""

	def SetToolClientData(self, tool_id, clientData) -> None:
		""" Sets the client data associated with the tool.
		"""

	def SetToolDisabledBitmap(self, tool_id, bitmap) -> None:
		""" Sets the bitmap to be used by the tool with the given ID when the tool is in a disabled state.
		"""

	def SetToolHelpString(self, tool_id, helpString) -> None:
		""" Sets the help string shown in tooltip for the given tool.
		"""

	def SetToolNormalBitmap(self, tool_id, bitmap) -> None:
		""" Sets the bitmap to be used by the tool with the given ID.
		"""

	def ToggleTool(self, tool_id, checked) -> None:
		""" Set a toggle tool to the checked or unchecked state.
		"""

EVT_RIBBONTOOLBAR_CLICKED: int  #  Triggered when the normal (non-dropdown) region of a tool on the tool bar is clicked.
EVT_RIBBONTOOLBAR_DROPDOWN_CLICKED: int  #  Triggered when the dropdown region of a tool on the tool bar is clicked. wx.ribbon.RibbonToolBarEvent.PopupMenu   should be called by the event handler if it wants to display a popup menu (which is what most dropdown tools should be doing). ^^


class RibbonToolBarEvent('CommandEvent'):
	""" command_type (wx.EventType) â 
	"""
	def __init__(self, command_type=wxEVT_NULL, win_id=0, bar=None) -> None:
		""" command_type (wx.EventType) â
		"""

	def GetBar(self) -> 'ribbon.RibbonToolBar':
		""" wx.ribbon.RibbonToolBar
		"""

	def PopupMenu(self, menu: 'Menu') -> bool:
		""" menu (wx.Menu) â
		"""

	def SetBar(self, bar: 'ribbon.RibbonToolBar') -> None:
		""" bar (wx.ribbon.RibbonToolBar) â
		"""



