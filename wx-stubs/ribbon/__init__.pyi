# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class RibbonButtonBarEvent(CommandEvent):
    """ Event used to indicate various actions relating to a button on a
RibbonButtonBar.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
    """
    def __init__(self, command_type=wxEVT_NULL, win_id=0, bar=None, button=None) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
        """

    def GetBar(self) -> 'ribbon.RibbonButtonBar':
        """ Returns the bar which contains the button which the event relates to.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
        """

    def GetButton(self) -> 'ribbon.RibbonButtonBarButtonBase':
        """ Returns the button which the event relates to.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
        """

    def PopupMenu(self, menu: 'Menu') -> bool:
        """ Display a popup menu as a result of this (dropdown clicked) event.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
        """

    def SetBar(self, bar: 'ribbon.RibbonButtonBar') -> None:
        """ Sets the button bar relating to this event.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
        """

    def SetButton(self, bar: RibbonButtonBarButtonBase) -> None:
        """ Sets the button relating to this event.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
        """

    Bar: 'ribbon.RibbonButtonBar'  # See GetBar and SetBar
    Button: 'ribbon.RibbonButtonBarButtonBase'  # See GetButton and SetButton



class RibbonGalleryEvent(CommandEvent):
    """ Constructor.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html
    """
    def __init__(self, command_type=wxEVT_NULL, win_id=0, gallery=None, item=None) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html
        """

    def GetGallery(self) -> 'ribbon.RibbonGallery':
        """ Returns the gallery which the event relates to.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html
        """

    def GetGalleryItem(self) -> 'ribbon.RibbonGalleryItem':
        """ Returns the gallery item which the event relates to, or None if it does not relate to an item.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html
        """

    def SetGallery(self, gallery: 'ribbon.RibbonGallery') -> None:
        """ Sets the gallery relating to this event.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html
        """

    def SetGalleryItem(self, item: RibbonGalleryItem) -> None:
        """ Sets the gallery item relating to this event.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html
        """

    Gallery: 'ribbon.RibbonGallery'  # See GetGallery and SetGallery
    GalleryItem: 'ribbon.RibbonGalleryItem'  # See GetGalleryItem and SetGalleryItem



class RibbonPanelEvent(CommandEvent):
    """ Event used to indicate various actions relating to a RibbonPanel.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonPanelEvent.html
    """
    def __init__(self, command_type=wxEVT_NULL, win_id=0, panel=None) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanelEvent.html
        """

    def GetPanel(self) -> 'ribbon.RibbonPanel':
        """ Returns the panel relating to this event.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanelEvent.html
        """

    def SetPanel(self, page: 'ribbon.RibbonPanel') -> None:
        """ Sets the page relating to this event.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanelEvent.html
        """

    Panel: 'ribbon.RibbonPanel'  # See GetPanel and SetPanel



class RibbonToolBarEvent(CommandEvent):
    """ command_type (wx.EventType) â 

        Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBarEvent.html
    """
    def __init__(self, command_type=wxEVT_NULL, win_id=0, bar=None) -> None:
        """ command_type (wx.EventType) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBarEvent.html
        """

    def GetBar(self) -> 'ribbon.RibbonToolBar':
        """ wx.ribbon.RibbonToolBar

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBarEvent.html
        """

    def PopupMenu(self, menu: 'Menu') -> bool:
        """ menu (wx.Menu) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBarEvent.html
        """

    def SetBar(self, bar: 'ribbon.RibbonToolBar') -> None:
        """ bar (wx.ribbon.RibbonToolBar) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBarEvent.html
        """

    Bar: 'ribbon.RibbonToolBar'  # See GetBar and SetBar



class RibbonControl(Control):
    """ RibbonControl serves as a base class for all controls which share
the ribbon characteristics of having a ribbon art provider, and
(optionally) non-continuous resizing.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def DoGetNextLargerSize(self, direction, relative_to) -> 'Size':
        """ Implementation of GetNextLargerSize .

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def DoGetNextSmallerSize(self, direction, relative_to) -> 'Size':
        """ Implementation of GetNextSmallerSize .

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def GetAncestorRibbonBar(self) -> 'ribbon.RibbonBar':
        """ Get the first ancestor which is a   wx.ribbon.RibbonBar  (or derived) or None if not having such parent.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def GetArtProvider(self) -> 'ribbon.RibbonArtProvider':
        """ Get the art provider to be used.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def GetBestSizeForParentSize(self, parentSize: Union[tuple[int, int], 'Size']) -> 'Size':
        """ Finds the best width and height given the parentâs width and height.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def GetNextLargerSize(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def GetNextSmallerSize(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def IsSizingContinuous(self) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def Realise(self) -> bool:
        """ Alias for Realize .

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def Realize(self) -> bool:
        """ Perform initial size and layout calculations after children have been added, and/or realize children.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def SetArtProvider(self, art: 'ribbon.RibbonArtProvider') -> None:
        """ Set the art provider to be used.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    AncestorRibbonBar: 'ribbon.RibbonBar'  # See GetAncestorRibbonBar
    ArtProvider: 'ribbon.RibbonArtProvider'  # See GetArtProvider and SetArtProvider



RIBBON_PANEL_FLEXIBLE: int

class RibbonBarEvent(NotifyEvent):
    """ Event used to indicate various actions relating to a RibbonBar.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonBarEvent.html
    """
    def __init__(self, command_type=wxEVT_NULL, win_id=0, page=None) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBarEvent.html
        """

    def GetPage(self) -> 'ribbon.RibbonPage':
        """ Returns the page being changed to, or being clicked on.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBarEvent.html
        """

    def SetPage(self, page: 'ribbon.RibbonPage') -> None:
        """ Sets the page relating to this event.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBarEvent.html
        """

    Page: 'ribbon.RibbonPage'  # See GetPage and SetPage



class RibbonButtonBar(RibbonControl):
    """ A ribbon button bar is similar to a traditional toolbar.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def AddButton(self, *args, **kw) -> 'ribbon.RibbonButtonBarButtonBase':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def AddDropdownButton(self, button_id, label, bitmap, help_string="") -> 'ribbon.RibbonButtonBarButtonBase':
        """ Add a dropdown button to the button bar (simple version).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def AddHybridButton(self, button_id, label, bitmap, help_string="") -> 'ribbon.RibbonButtonBarButtonBase':
        """ Add a hybrid button to the button bar (simple version).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def AddToggleButton(self, button_id, label, bitmap, help_string="") -> 'ribbon.RibbonButtonBarButtonBase':
        """ Add a toggle button to the button bar (simple version).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def ClearButtons(self) -> None:
        """ Delete all buttons from the button bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ Create a button bar in two-step button bar construction.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def DeleteButton(self, button_id: int) -> bool:
        """ Delete a single button from the button bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def EnableButton(self, button_id, enable=True) -> None:
        """ Enable or disable a single button on the bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetActiveItem(self) -> 'ribbon.RibbonButtonBarButtonBase':
        """ Returns the active item of the button bar or None if there is none.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetButtonCount(self) -> int:
        """ Returns the number of buttons in this button bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetHoveredItem(self) -> 'ribbon.RibbonButtonBarButtonBase':
        """ Returns the hovered item of the button bar or None if there is none.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetItem(self, n: int) -> 'ribbon.RibbonButtonBarButtonBase':
        """ Returns the N-th button of the bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetItemById(self, id: int) -> 'ribbon.RibbonButtonBarButtonBase':
        """ Returns the first button having a given id or None if none matches.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetItemClientData(self, item: RibbonButtonBarButtonBase) -> 'ClientData':
        """ Get the client object associated with a button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetItemId(self, item: RibbonButtonBarButtonBase) -> int:
        """ Returns the id of a button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetItemRect(self, button_id: int) -> 'Rect':
        """ Returns the itemsâs rect with coordinates relative to the button barâs parent, or a default-constructed rect if the tool is not found.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetShowToolTipsForDisabled(self) -> bool:
        """ Sets whether tooltips should be shown for disabled buttons or not.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def InsertButton(self, *args, **kw) -> 'ribbon.RibbonButtonBarButtonBase':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def InsertDropdownButton(self, pos, button_id, label, bitmap, help_string="") -> 'ribbon.RibbonButtonBarButtonBase':
        """ Inserts a dropdown button to the button bar (simple version) at the given position.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def InsertHybridButton(self, pos, button_id, label, bitmap, help_string="") -> 'ribbon.RibbonButtonBarButtonBase':
        """ Inserts a hybrid button to the button bar (simple version) at the given position.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def InsertToggleButton(self, pos, button_id, label, bitmap, help_string="") -> 'ribbon.RibbonButtonBarButtonBase':
        """ Inserts a toggle button to the button bar (simple version) at the given position.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def Realize(self) -> bool:
        """ Calculate button layouts and positions.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetButtonIcon(self, button_id, bitmap, bitmap_small=NullBitmap, bitmap_disabled=NullBitmap, bitmap_small_disabled=NullBitmap) -> None:
        """ Changes the bitmap of an existing button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetButtonMaxSizeClass(self, button_id, max_size_class) -> None:
        """ Sets the maximum size class of a ribbon button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetButtonMinSizeClass(self, button_id, min_size_class) -> None:
        """ Sets the minimum size class of a ribbon button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetButtonText(self, button_id, label) -> None:
        """ Changes the label text of an existing button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetButtonTextMinWidth(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetItemClientData(self, item, data) -> None:
        """ Set the client object associated with a button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetShowToolTipsForDisabled(self, show: bool) -> None:
        """ Indicates whether tooltips are shown for disabled buttons.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def ToggleButton(self, button_id, checked) -> None:
        """ Set a toggle button to the checked or unchecked state.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    ActiveItem: 'ribbon.RibbonButtonBarButtonBase'  # See GetActiveItem
    ButtonCount: int  # See GetButtonCount
    HoveredItem: 'ribbon.RibbonButtonBarButtonBase'  # See GetHoveredItem
    ShowToolTipsForDisabled: bool  # See GetShowToolTipsForDisabled and SetShowToolTipsForDisabled



EVT_RIBBONBUTTONBAR_CLICKED: int  # Triggered when the normal (non-dropdown) region of a button on the button bar is clicked.

EVT_RIBBONBUTTONBAR_DROPDOWN_CLICKED: int  # Triggered when the dropdown region of a button on the button bar is clicked. wx.ribbon.RibbonButtonBarEvent.PopupMenu   should be called by the event handler if it wants to display a popup menu (which is what most dropdown buttons should be doing). ^^

RIBBON_BUTTONBAR_BUTTON_SMALL: int

RIBBON_BUTTONBAR_BUTTON_MEDIUM: int

RIBBON_BUTTONBAR_BUTTON_LARGE: int

class RibbonBar(RibbonControl):
    """ Top-level control in a ribbon user interface.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def AddPageHighlight(self, page, highlight=True) -> None:
        """ Highlight the specified tab.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def ArePanelsShown(self) -> bool:
        """ Indicates whether the panel area of the ribbon bar is shown.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def ClearPages(self) -> None:
        """ Delete all pages from the ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=RIBBON_BAR_DEFAULT_STYLE) -> bool:
        """ Create a ribbon bar in two-step ribbon bar construction.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def DeletePage(self, n: int) -> None:
        """ Delete a single page from this ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def DismissExpandedPanel(self) -> bool:
        """ Dismiss the expanded panel of the currently active page.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def GetActivePage(self) -> int:
        """ Get the index of the active page.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def GetDisplayMode(self) -> 'ribbon.RibbonDisplayMode':
        """ Returns the current display mode of the panel area.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def GetPage(self, n: int) -> 'ribbon.RibbonPage':
        """ Get a page by index.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def GetPageCount(self) -> int:
        """ Get the number of pages in this bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def GetPageNumber(self, page: 'ribbon.RibbonPage') -> int:
        """ Returns the number for a given ribbon bar page.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def HidePage(self, page: int) -> None:
        """ Hides the tab for a given page.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def HidePanels(self) -> None:
        """ Hides the panel area of the ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def IsPageHighlighted(self, page: int) -> bool:
        """ Indicates whether a tab is currently highlighted.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def IsPageShown(self, page: int) -> bool:
        """ Indicates whether the tab for the given page is shown to the user or not.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def Realize(self) -> bool:
        """ Perform initial layout and size calculations of the bar and its children.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def RemovePageHighlight(self, page: int) -> None:
        """ Changes a tab to not be highlighted.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def SetActivePage(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def SetArtProvider(self, art: 'ribbon.RibbonArtProvider') -> None:
        """ Set the art provider to be used be the ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def SetTabCtrlMargins(self, left, right) -> None:
        """ Set the margin widths (in pixels) on the left and right sides of the tab bar region of the ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def ShowPage(self, page, show_tab=True) -> None:
        """ Show or hide the tab for a given page.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def ShowPanels(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    ActivePage: int  # See GetActivePage and SetActivePage
    DisplayMode: 'ribbon.RibbonDisplayMode'  # See GetDisplayMode
    PageCount: int  # See GetPageCount



RIBBON_BAR_DEFAULT_STYLE: int  # Defined as wx.ribbon.RIBBON_BAR_FLOW_HORIZONTAL | wx.ribbon.RIBBON_BAR_SHOW_PAGE_LABELS | wx.ribbon.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS | wx.ribbon.RIBBON_BAR_SHOW_TOGGLE_BUTTON | wx.ribbon.RIBBON_BAR_SHOW_HELP_BUTTON.

RIBBON_BAR_FOLDBAR_STYLE: int  # Defined as wx.ribbon.RIBBON_BAR_FLOW_VERTICAL | wx.ribbon.RIBBON_BAR_SHOW_PAGE_ICONS | wx.ribbon.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS | wx.ribbon.RIBBON_BAR_SHOW_PANEL_MINIMISE_BUTTONS

RIBBON_BAR_SHOW_PAGE_LABELS: int  # Causes labels to be shown on the tabs in the ribbon bar.

RIBBON_BAR_SHOW_PAGE_ICONS: int  # Causes icons to be shown on the tabs in the ribbon bar.

RIBBON_BAR_FLOW_HORIZONTAL: int  # Causes panels within pages to stack horizontally.

RIBBON_BAR_FLOW_VERTICAL: int  # Causes panels within pages to stack vertically.

RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS: int  # Causes extension buttons to be shown on panels (where the panel has such a button).

RIBBON_BAR_SHOW_PANEL_MINIMISE_BUTTONS: int  # Causes minimise buttons to be shown on panels (where the panel has such a button).

RIBBON_BAR_SHOW_TOGGLE_BUTTON: int  # Causes a toggle button to appear on the ribbon bar at top-right corner. This style is new since wxWidgets 2.9.5.

RIBBON_BAR_SHOW_HELP_BUTTON: int  # Causes a help button to appear on the ribbon bar at the top-right corner. This style is new since wxWidgets 2.9.5. ^^

EVT_RIBBONBAR_PAGE_CHANGED: int  # Triggered after the transition from one page being active to a different page being active.

EVT_RIBBONBAR_PAGE_CHANGING: int  # Triggered prior to the transition from one page being active to a different page being active, and can veto the change.

EVT_RIBBONBAR_TAB_MIDDLE_DOWN: int  # Triggered when the middle mouse button is pressed on a tab.

EVT_RIBBONBAR_TAB_MIDDLE_UP: int  # Triggered when the middle mouse button is released on a tab.

EVT_RIBBONBAR_TAB_RIGHT_DOWN: int  # Triggered when the right mouse button is pressed on a tab.

EVT_RIBBONBAR_TAB_RIGHT_UP: int  # Triggered when the right mouse button is released on a tab.

EVT_RIBBONBAR_TAB_LEFT_DCLICK: int  # Triggered when the left mouse button is double clicked on a tab.

EVT_RIBBONBAR_TOGGLED: int  # Triggered when the button triggering the ribbon bar is clicked. This event is new since wxWidgets 2.9.5.

EVT_RIBBONBAR_HELP_CLICK: int  # Triggered when the help button is clicked. This even is new since wxWidgets 2.9.5. ^^

class RibbonGallery(RibbonControl):
    """ A ribbon gallery is like a ListBox, but for bitmaps rather than
strings.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def Append(self, *args, **kw) -> 'ribbon.RibbonGalleryItem':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def Clear(self) -> None:
        """ Remove all items from the gallery.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ Create a gallery in two-step gallery construction.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def EnsureVisible(self, item: RibbonGalleryItem) -> None:
        """ Scroll the gallery to ensure that the given item is visible.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetActiveItem(self) -> 'ribbon.RibbonGalleryItem':
        """ Get the currently active item, or None if there is none.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetCount(self) -> int:
        """ Get the number of items in the gallery.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetDownButtonState(self) -> 'ribbon.RibbonGalleryButtonState':
        """ Get the state of the scroll down button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetExtensionButtonState(self) -> 'ribbon.RibbonGalleryButtonState':
        """ Get the state of the âextensionâ button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetHoveredItem(self) -> 'ribbon.RibbonGalleryItem':
        """ Get the currently hovered item, or None if there is none.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetItem(self, n: int) -> 'ribbon.RibbonGalleryItem':
        """ Get an item by index.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetItemClientData(self, item: RibbonGalleryItem) -> 'ClientData':
        """ Get the client object associated with a gallery item.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetSelection(self) -> 'ribbon.RibbonGalleryItem':
        """ Get the currently selected item, or None if there is none.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetUpButtonState(self) -> 'ribbon.RibbonGalleryButtonState':
        """ Get the state of the scroll up button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def IsEmpty(self) -> bool:
        """ Query if the gallery has no items in it.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def IsHovered(self) -> bool:
        """ Query is the mouse is currently hovered over the gallery.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def ScrollLines(self, lines: int) -> bool:
        """ Scroll the gallery contents by some amount.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def ScrollPixels(self, pixels: int) -> bool:
        """ Scroll the gallery contents by some fine-grained amount.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def SetItemClientData(self, item, data) -> None:
        """ Set the client object associated with a gallery item.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def SetSelection(self, item: RibbonGalleryItem) -> None:
        """ Set the selection to the given item, or removes the selection if item  == None.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    ActiveItem: 'ribbon.RibbonGalleryItem'  # See GetActiveItem
    Count: int  # See GetCount
    DownButtonState: 'ribbon.RibbonGalleryButtonState'  # See GetDownButtonState
    ExtensionButtonState: 'ribbon.RibbonGalleryButtonState'  # See GetExtensionButtonState
    HoveredItem: 'ribbon.RibbonGalleryItem'  # See GetHoveredItem
    Selection: 'ribbon.RibbonGalleryItem'  # See GetSelection and SetSelection
    UpButtonState: 'ribbon.RibbonGalleryButtonState'  # See GetUpButtonState



EVT_RIBBONGALLERY_SELECTED: int  # Triggered when the user selects an item from the gallery. Note that the ID is that of the gallery, not of the item.

EVT_RIBBONGALLERY_CLICKED: int  # Similar to EVT_RIBBONGALLERY_SELECTED but triggered every time a gallery item is clicked, even if it is already selected. Note that the ID of the event is that of the gallery, not of the item, just as above. This event is available since wxWidgets 2.9.2.

EVT_RIBBONGALLERY_HOVER_CHANGED: int  # Triggered when the item being hovered over by the user changes. The item in the event will be the new item being hovered, or None if there is no longer an item being hovered. Note that the ID is that of the gallery, not of the item. ^^ ^^

class RibbonPanel(RibbonControl):
    """ Serves as a container for a group of (ribbon) controls.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def CanAutoMinimise(self) -> bool:
        """ Query if the panel can automatically minimise itself at small sizes.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def Create(self, parent, id=ID_ANY, label="", icon=NullBitmap, pos=DefaultPosition, size=DefaultSize, style=RIBBON_PANEL_DEFAULT_STYLE) -> bool:
        """ Create a ribbon panel in two-step ribbon panel construction.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def GetExpandedDummy(self) -> 'ribbon.RibbonPanel':
        """ Get the dummy panel of an expanded panel.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def GetExpandedPanel(self) -> 'ribbon.RibbonPanel':
        """ Get the expanded panel of a dummy panel.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def GetMinimisedIcon(self) -> 'Bitmap':
        """ Get the bitmap to be used in place of the panel children when it is minimised.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def HasExtButton(self) -> bool:
        """ Test if the panel has an extension button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def HideExpanded(self) -> bool:
        """ Hide the panelâs external expansion.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def IsExtButtonHovered(self) -> bool:
        """ Query if the mouse is currently hovered over the extension button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def IsHovered(self) -> bool:
        """ Query is the mouse is currently hovered over the panel.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def IsMinimised(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def Realize(self) -> bool:
        """ Realize all children of the panel.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def SetArtProvider(self, art: 'ribbon.RibbonArtProvider') -> None:
        """ Set the art provider to be used.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def ShowExpanded(self) -> bool:
        """ Show the panel externally expanded.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    ExpandedDummy: 'ribbon.RibbonPanel'  # See GetExpandedDummy
    ExpandedPanel: 'ribbon.RibbonPanel'  # See GetExpandedPanel
    MinimisedIcon: 'Bitmap'  # See GetMinimisedIcon



RIBBON_PANEL_DEFAULT_STYLE: int  # Defined as no other flags set.

RIBBON_PANEL_NO_AUTO_MINIMISE: int  # Prevents the panel from automatically minimising to conserve screen space.

RIBBON_PANEL_EXT_BUTTON: int  # Causes an extension button to be shown in the panelâs chrome (if the bar in which it is contained has wx.ribbon.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS set). The behaviour of this button is application controlled, but typically will show an extended drop-down menu relating to the panel.

RIBBON_PANEL_MINIMISE_BUTTON: int  # Causes a (de)minimise button to be shown in the panelâs chrome (if the bar in which it is contained has the wx.ribbon.RIBBON_BAR_SHOW_PANEL_MINIMISE_BUTTONS style set). This flag is typically combined with wx.ribbon.RIBBON_PANEL_NO_AUTO_MINIMISE to make a panel which the user always has manual control over when it minimises.

RIBBON_PANEL_STRETCH: int  # Stretches a single panel to fit the parent page.

EVT_RIBBONPANEL_EXTBUTTON_ACTIVATED: int  # Triggered when the user activate the panel extension button. ^^

class RibbonToolBar(RibbonControl):
    """ A ribbon tool bar is similar to a traditional toolbar which has no
labels.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def AddDropdownTool(self, tool_id, bitmap, help_string="") -> 'ribbon.RibbonToolBarToolBase':
        """ Add a dropdown tool to the tool bar (simple version).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def AddHybridTool(self, tool_id, bitmap, help_string="") -> 'ribbon.RibbonToolBarToolBase':
        """ Add a hybrid tool to the tool bar (simple version).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def AddSeparator(self) -> 'ribbon.RibbonToolBarToolBase':
        """ Add a separator to the tool bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def AddToggleTool(self, tool_id, bitmap, help_string) -> 'ribbon.RibbonToolBarToolBase':
        """ Add a toggle tool to the tool bar (simple version).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def AddTool(self, *args, **kw) -> 'ribbon.RibbonToolBarToolBase':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def ClearTools(self) -> None:
        """ Deletes all the tools in the toolbar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ Create a tool bar in two-step tool bar construction.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def DeleteTool(self, tool_id: int) -> bool:
        """ Removes the specified tool from the toolbar and deletes it.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def DeleteToolByPos(self, pos: int) -> bool:
        """ This function behaves like DeleteTool   but it deletes the tool at the specified position and not the one with the given id.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def EnableTool(self, tool_id, enable=True) -> None:
        """ Enable or disable a single tool on the bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def FindById(self, tool_id: int) -> 'ribbon.RibbonToolBarToolBase':
        """ Returns a pointer to the tool opaque structure by id  or None if no corresponding tool is found.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetActiveTool(self) -> 'ribbon.RibbonToolBarToolBase':
        """ Returns the active item of the tool bar or None if there is none.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolByPos(self, *args, **kw) -> 'ribbon.RibbonToolBarToolBase':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolClientData(self, tool_id: int) -> 'PyUserData':
        """ Get any client data associated with the tool.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolCount(self) -> int:
        """ Returns the number of tools in the toolbar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolEnabled(self, tool_id: int) -> bool:
        """ Called to determine whether a tool is enabled (responds to user input).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolHelpString(self, tool_id: int) -> str:
        """ Returns the help string for the given tool.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolId(self, tool: RibbonToolBarToolBase) -> int:
        """ Return the id associated to the tool opaque structure.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolKind(self, tool_id: int) -> 'ribbon.RibbonButtonKind':
        """ Return the kind of the given tool.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolPos(self, tool_id: int) -> int:
        """ Returns the tool position in the toolbar, or  NOT_FOUND   if the tool is not found.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolRect(self, tool_id: int) -> 'Rect':
        """ Returns the toolâs rect with coordinates relative to the toolbarâs parent, or a default-constructed rect if the tool is not found.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolState(self, tool_id: int) -> bool:
        """ Gets the on/off state of a toggle tool.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def InsertDropdownTool(self, pos, tool_id, bitmap, help_string="") -> 'ribbon.RibbonToolBarToolBase':
        """ Insert a dropdown tool to the tool bar (simple version) as the specified position.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def InsertHybridTool(self, pos, tool_id, bitmap, help_string="") -> 'ribbon.RibbonToolBarToolBase':
        """ Insert a hybrid tool to the tool bar (simple version) as the specified position.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def InsertSeparator(self, pos: int) -> 'ribbon.RibbonToolBarToolBase':
        """ Insert a separator to the tool bar at the specified position.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def InsertToggleTool(self, pos, tool_id, bitmap, help_string="") -> 'ribbon.RibbonToolBarToolBase':
        """ Insert a toggle tool to the tool bar (simple version) as the specified position.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def InsertTool(self, *args, **kw) -> 'ribbon.RibbonToolBarToolBase':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def Realize(self) -> bool:
        """ Calculate tool layouts and positions.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def SetRows(self, nMin, nMax=-1) -> None:
        """ Set the number of rows to distribute tool groups over.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def SetToolClientData(self, tool_id, clientData) -> None:
        """ Sets the client data associated with the tool.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def SetToolDisabledBitmap(self, tool_id, bitmap) -> None:
        """ Sets the bitmap to be used by the tool with the given ID when the tool is in a disabled state.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def SetToolHelpString(self, tool_id, helpString) -> None:
        """ Sets the help string shown in tooltip for the given tool.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def SetToolNormalBitmap(self, tool_id, bitmap) -> None:
        """ Sets the bitmap to be used by the tool with the given ID.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def ToggleTool(self, tool_id, checked) -> None:
        """ Set a toggle tool to the checked or unchecked state.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    ActiveTool: 'ribbon.RibbonToolBarToolBase'  # See GetActiveTool
    ToolCount: int  # See GetToolCount



EVT_RIBBONTOOLBAR_CLICKED: int  # Triggered when the normal (non-dropdown) region of a tool on the tool bar is clicked.

EVT_RIBBONTOOLBAR_DROPDOWN_CLICKED: int  # Triggered when the dropdown region of a tool on the tool bar is clicked. wx.ribbon.RibbonToolBarEvent.PopupMenu   should be called by the event handler if it wants to display a popup menu (which is what most dropdown tools should be doing). ^^

class RibbonArtProvider:
    """ RibbonArtProvider is responsible for drawing all the components of
the ribbon interface.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def Clone(self) -> 'ribbon.RibbonArtProvider':
        """ Create a new art provider which is a clone of this one.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawButtonBarBackground(self, dc, wnd, rect) -> None:
        """ Draw the background for a   wx.ribbon.RibbonButtonBar  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawButtonBarButton(self, dc, wnd, rect, kind, state, label, bitmap_large, bitmap_small) -> None:
        """ Draw a single button for a   wx.ribbon.RibbonButtonBar  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawGalleryBackground(self, dc, wnd, rect) -> None:
        """ Draw the background and chrome for a   wx.ribbon.RibbonGallery  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawGalleryItemBackground(self, dc, wnd, rect, item) -> None:
        """ Draw the background of a single item in a   wx.ribbon.RibbonGallery  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawHelpButton(self, dc, wnd, rect) -> None:
        """ Draw help button on   wx.ribbon.RibbonBar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawMinimisedPanel(self, dc, wnd, rect, bitmap) -> None:
        """ Draw a minimised ribbon panel.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawPageBackground(self, dc, wnd, rect) -> None:
        """ Draw the background of a ribbon page.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawPanelBackground(self, dc, wnd, rect) -> None:
        """ Draw the background and chrome for a ribbon panel.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawScrollButton(self, dc, wnd, rect, style) -> None:
        """ Draw a ribbon-style scroll button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawTab(self, dc, wnd, tab) -> None:
        """ Draw a single tab in the tab region of a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawTabCtrlBackground(self, dc, wnd, rect) -> None:
        """ Draw the background of the tab region of a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawTabSeparator(self, dc, wnd, rect, visibility) -> None:
        """ Draw a separator between two tabs in a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawToggleButton(self, dc, wnd, rect, mode) -> None:
        """ Draw toggle button on   wx.ribbon.RibbonBar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawTool(self, dc, wnd, rect, bitmap, kind, state) -> None:
        """ Draw a single tool (for a   wx.ribbon.RibbonToolBar  control).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawToolBarBackground(self, dc, wnd, rect) -> None:
        """ Draw the background for a   wx.ribbon.RibbonToolBar  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawToolGroupBackground(self, dc, wnd, rect) -> None:
        """ Draw the background for a group of tools on a   wx.ribbon.RibbonToolBar  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetBarTabWidth(self, dc, wnd, label, bitmap, ideal, small_begin_need_separator, small_must_have_separator, minimum) -> None:
        """ Calculate the ideal and minimum width (in pixels) of a tab in a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetBarToggleButtonArea(self, rect: 'Rect') -> 'Rect':
        """ Calculate the position and size of the ribbonâs toggle button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetButtonBarButtonSize(self, dc, wnd, kind, size, label, text_min_width, bitmap_size_large, bitmap_size_small, button_size, normal_region, dropdown_region) -> bool:
        """ Calculate the size of a button within a   wx.ribbon.RibbonButtonBar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetButtonBarButtonTextWidth(self, dc, label, kind, size) -> 'Coord':
        """ Gets the width of the string if it is used as a   wx.ribbon.RibbonButtonBar  button label.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetColor(self, id: int) -> 'Colour':
        """ id (int) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetColour(self, id: int) -> 'Colour':
        """ Get the value of a certain colour setting.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetColourScheme(self) -> tuple:
        """ Get the current colour scheme.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetFlags(self) -> int:
        """ Get the previously set style flags.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetFont(self, id: int) -> 'Font':
        """ Get the value of a certain font setting.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetGalleryClientSize(self, dc, wnd, size, client_offset, scroll_up_button, scroll_down_button, extension_button) -> 'Size':
        """ Calculate the client size of a   wx.ribbon.RibbonGallery  control for a given size.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetGallerySize(self, dc, wnd, client_size) -> 'Size':
        """ Calculate the size of a   wx.ribbon.RibbonGallery  control for a given client size.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetMetric(self, id: int) -> int:
        """ Get the value of a certain integer setting.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetMinimisedPanelMinimumSize(self, dc, wnd, desired_bitmap_size, expanded_panel_direction) -> 'Size':
        """ Calculate the size of a minimised ribbon panel.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetPageBackgroundRedrawArea(self, dc, wnd, page_old_size, page_new_size) -> 'Rect':
        """ Calculate the portion of a page background which needs to be redrawn when a page is resized.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetPanelClientSize(self, dc, wnd, size, client_offset) -> 'Size':
        """ Calculate the client size of a panel for a given overall size.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetPanelExtButtonArea(self, dc, wnd, rect) -> 'Rect':
        """ Calculate the position and size of the panel extension button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetPanelSize(self, dc, wnd, client_size, client_offset) -> 'Size':
        """ Calculate the size of a panel for a given client size.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetRibbonHelpButtonArea(self, rect: 'Rect') -> 'Rect':
        """ Calculate the position and size of the ribbonâs help button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetScrollButtonMinimumSize(self, dc, wnd, style) -> 'Size':
        """ Calculate the minimum size (in pixels) of a scroll button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetTabCtrlHeight(self, dc, wnd, pages) -> int:
        """ Calculate the height (in pixels) of the tab region of a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetToolSize(self, dc, wnd, bitmap_size, kind, is_first, is_last, dropdown_region) -> 'Size':
        """ Calculate the size of a tool within a   wx.ribbon.RibbonToolBar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def SetColor(self, id, color) -> None:
        """ id (int) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def SetColour(self, id, colour) -> None:
        """ Set the value of a certain colour setting to the value colour.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def SetColourScheme(self, primary, secondary, tertiary) -> None:
        """ Set all applicable colour settings from a few base colours.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def SetFlags(self, flags: int) -> None:
        """ Set the style flags.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def SetFont(self, id, font) -> None:
        """ Set the value of a certain font setting to the value font.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def SetMetric(self, id, new_val) -> None:
        """ Set the value of a certain integer setting to the value new_val.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    Flags: int  # See GetFlags and SetFlags



RIBBON_BUTTONBAR_BUTTON_DISABLED: int

RIBBON_ART_GALLERY_BITMAP_PADDING_RIGHT_SIZE: int

RIBBON_ART_GALLERY_BITMAP_PADDING_TOP_SIZE: int

RIBBON_ART_GALLERY_BITMAP_PADDING_BOTTOM_SIZE: int

class RibbonPage(RibbonControl):
    """ Container for related ribbon panels, and a tab within a ribbon bar.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def AdjustRectToIncludeScrollButtons(self, rect: 'Rect') -> None:
        """ Expand a rectangle of the page to include external scroll buttons (if any).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def Create(self, parent, id=ID_ANY, label="", icon=NullBitmap, style=0) -> bool:
        """ Create a ribbon page in two-step ribbon page construction.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def DismissExpandedPanel(self) -> bool:
        """ Dismiss the current externally expanded panel, if there is one.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def GetIcon(self) -> 'Bitmap':
        """ Get the icon used for the page in the ribbon bar tab area (only displayed if the ribbon bar is actually showing icons).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def GetMajorAxis(self) -> 'Orientation':
        """ Get the direction in which ribbon panels are stacked within the page.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def Realize(self) -> bool:
        """ Perform a full re-layout of all panels on the page.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def ScrollLines(self, lines: int) -> bool:
        """ Scroll the page by some amount up / down / left / right.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def ScrollPixels(self, pixels: int) -> bool:
        """ Scroll the page by a set number of pixels up / down / left / right.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def ScrollSections(self, sections: int) -> bool:
        """ Scroll the page by an entire child section.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def SetArtProvider(self, art: 'ribbon.RibbonArtProvider') -> None:
        """ Set the art provider to be used.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def SetSizeWithScrollButtonAdjustment(self, x, y, width, height) -> None:
        """ Set the size of the page and the external scroll buttons (if any).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    Icon: 'Bitmap'  # See GetIcon
    MajorAxis: 'Orientation'  # See GetMajorAxis



HORIZONTAL: int

VERTICAL: int

BOTH: int

RibbonButtonKind: TypeAlias = int  # Enumeration

RIBBON_BUTTON_NORMAL: int

RIBBON_BUTTON_DROPDOWN: int

RIBBON_BUTTON_HYBRID: int

RIBBON_BUTTON_TOGGLE: int

RibbonButtonBarButtonState: TypeAlias = int  # Enumeration

RIBBON_BUTTONBAR_BUTTON_SIZE_MASK: int

RIBBON_BUTTONBAR_BUTTON_NORMAL_HOVERED: int

RIBBON_BUTTONBAR_BUTTON_DROPDOWN_HOVERED: int

RIBBON_BUTTONBAR_BUTTON_HOVER_MASK: int

RIBBON_BUTTONBAR_BUTTON_NORMAL_ACTIVE: int

RIBBON_BUTTONBAR_BUTTON_DROPDOWN_ACTIVE: int

RIBBON_BUTTONBAR_BUTTON_ACTIVE_MASK: int

RIBBON_BUTTONBAR_BUTTON_TOGGLED: int

RIBBON_BUTTONBAR_BUTTON_STATE_MASK: int

RibbonDisplayMode: TypeAlias = int  # Enumeration

RIBBON_BAR_PINNED: int

RIBBON_BAR_MINIMIZED: int

RIBBON_BAR_EXPANDED: int

RibbonGalleryButtonState: TypeAlias = int  # Enumeration

RIBBON_GALLERY_BUTTON_NORMAL: int

RIBBON_GALLERY_BUTTON_HOVERED: int

RIBBON_GALLERY_BUTTON_ACTIVE: int

RIBBON_GALLERY_BUTTON_DISABLED: int

class RibbonAUIArtProvider(RibbonMSWArtProvider):
    """ Create a new art provider which is a clone of this one.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def Clone(self) -> 'ribbon.RibbonArtProvider':
        """ Create a new art provider which is a clone of this one.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawButtonBarBackground(self, dc, wnd, rect) -> None:
        """ Draw the background for a   wx.ribbon.RibbonButtonBar  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawButtonBarButton(self, dc, wnd, rect, kind, state, label, bitmap_large, bitmap_small) -> None:
        """ Draw a single button for a   wx.ribbon.RibbonButtonBar  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawGalleryBackground(self, dc, wnd, rect) -> None:
        """ Draw the background and chrome for a   wx.ribbon.RibbonGallery  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawGalleryItemBackground(self, dc, wnd, rect, item) -> None:
        """ Draw the background of a single item in a   wx.ribbon.RibbonGallery  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawMinimisedPanel(self, dc, wnd, rect, bitmap) -> None:
        """ Draw a minimised ribbon panel.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawPageBackground(self, dc, wnd, rect) -> None:
        """ Draw the background of a ribbon page.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawPanelBackground(self, dc, wnd, rect) -> None:
        """ Draw the background and chrome for a ribbon panel.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawScrollButton(self, dc, wnd, rect, style) -> None:
        """ Draw a ribbon-style scroll button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawTab(self, dc, wnd, tab) -> None:
        """ Draw a single tab in the tab region of a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawTabCtrlBackground(self, dc, wnd, rect) -> None:
        """ Draw the background of the tab region of a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawTabSeparator(self, dc, wnd, rect, visibility) -> None:
        """ Draw a separator between two tabs in a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawTool(self, dc, wnd, rect, bitmap, kind, state) -> None:
        """ Draw a single tool (for a   wx.ribbon.RibbonToolBar  control).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawToolBarBackground(self, dc, wnd, rect) -> None:
        """ Draw the background for a   wx.ribbon.RibbonToolBar  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawToolGroupBackground(self, dc, wnd, rect) -> None:
        """ Draw the background for a group of tools on a   wx.ribbon.RibbonToolBar  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetBarTabWidth(self, dc, wnd, label, bitmap, ideal, small_begin_need_separator, small_must_have_separator, minimum) -> None:
        """ Calculate the ideal and minimum width (in pixels) of a tab in a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetColour(self, id: int) -> 'Colour':
        """ Get the value of a certain colour setting.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetPanelClientSize(self, dc, wnd, size, client_offset) -> 'Size':
        """ Calculate the client size of a panel for a given overall size.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetPanelExtButtonArea(self, dc, wnd, rect) -> 'Rect':
        """ Calculate the position and size of the panel extension button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetPanelSize(self, dc, wnd, client_size, client_offset) -> 'Size':
        """ Calculate the size of a panel for a given client size.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetScrollButtonMinimumSize(self, dc, wnd, style) -> 'Size':
        """ Calculate the minimum size (in pixels) of a scroll button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetTabCtrlHeight(self, dc, wnd, pages) -> int:
        """ Calculate the height (in pixels) of the tab region of a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def SetColour(self, id, colour) -> None:
        """ Set the value of a certain colour setting to the value colour.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def SetColourScheme(self, primary, secondary, tertiary) -> None:
        """ Set all applicable colour settings from a few base colours.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def SetFont(self, id, font) -> None:
        """ Set the value of a certain font setting to the value font.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """



class RibbonMSWArtProvider(RibbonArtProvider):
    """ set_colour_scheme (bool) â 

        Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
    """
    def __init__(self, set_colour_scheme: bool=True) -> None:
        """ set_colour_scheme (bool) â

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def Clone(self) -> 'ribbon.RibbonArtProvider':
        """ Create a new art provider which is a clone of this one.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawButtonBarBackground(self, dc, wnd, rect) -> None:
        """ Draw the background for a   wx.ribbon.RibbonButtonBar  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawButtonBarButton(self, dc, wnd, rect, kind, state, label, bitmap_large, bitmap_small) -> None:
        """ Draw a single button for a   wx.ribbon.RibbonButtonBar  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawGalleryBackground(self, dc, wnd, rect) -> None:
        """ Draw the background and chrome for a   wx.ribbon.RibbonGallery  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawGalleryItemBackground(self, dc, wnd, rect, item) -> None:
        """ Draw the background of a single item in a   wx.ribbon.RibbonGallery  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawHelpButton(self, dc, wnd, rect) -> None:
        """ Draw help button on   wx.ribbon.RibbonBar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawMinimisedPanel(self, dc, wnd, rect, bitmap) -> None:
        """ Draw a minimised ribbon panel.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawPageBackground(self, dc, wnd, rect) -> None:
        """ Draw the background of a ribbon page.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawPanelBackground(self, dc, wnd, rect) -> None:
        """ Draw the background and chrome for a ribbon panel.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawScrollButton(self, dc, wnd, rect, style) -> None:
        """ Draw a ribbon-style scroll button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawTab(self, dc, wnd, tab) -> None:
        """ Draw a single tab in the tab region of a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawTabCtrlBackground(self, dc, wnd, rect) -> None:
        """ Draw the background of the tab region of a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawTabSeparator(self, dc, wnd, rect, visibility) -> None:
        """ Draw a separator between two tabs in a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawToggleButton(self, dc, wnd, rect, mode) -> None:
        """ Draw toggle button on   wx.ribbon.RibbonBar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawTool(self, dc, wnd, rect, bitmap, kind, state) -> None:
        """ Draw a single tool (for a   wx.ribbon.RibbonToolBar  control).

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawToolBarBackground(self, dc, wnd, rect) -> None:
        """ Draw the background for a   wx.ribbon.RibbonToolBar  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawToolGroupBackground(self, dc, wnd, rect) -> None:
        """ Draw the background for a group of tools on a   wx.ribbon.RibbonToolBar  control.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetBarTabWidth(self, dc, wnd, label, bitmap, ideal, small_begin_need_separator, small_must_have_separator, minimum) -> None:
        """ Calculate the ideal and minimum width (in pixels) of a tab in a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetBarToggleButtonArea(self, rect: 'Rect') -> 'Rect':
        """ Calculate the position and size of the ribbonâs toggle button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetButtonBarButtonSize(self, dc, wnd, kind, size, label, text_min_width, bitmap_size_large, bitmap_size_small, button_size, normal_region, dropdown_region) -> bool:
        """ Calculate the size of a button within a   wx.ribbon.RibbonButtonBar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetButtonBarButtonTextWidth(self, dc, label, kind, size) -> 'Coord':
        """ Gets the width of the string if it is used as a   wx.ribbon.RibbonButtonBar  button label.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetColour(self, id: int) -> 'Colour':
        """ Get the value of a certain colour setting.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetColourScheme(self) -> tuple:
        """ Get the current colour scheme.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetFlags(self) -> int:
        """ Get the previously set style flags.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetFont(self, id: int) -> 'Font':
        """ Get the value of a certain font setting.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetGalleryClientSize(self, dc, wnd, size, client_offset, scroll_up_button, scroll_down_button, extension_button) -> 'Size':
        """ Calculate the client size of a   wx.ribbon.RibbonGallery  control for a given size.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetGallerySize(self, dc, wnd, client_size) -> 'Size':
        """ Calculate the size of a   wx.ribbon.RibbonGallery  control for a given client size.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetMetric(self, id: int) -> int:
        """ Get the value of a certain integer setting.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetMinimisedPanelMinimumSize(self, dc, wnd, desired_bitmap_size, expanded_panel_direction) -> 'Size':
        """ Calculate the size of a minimised ribbon panel.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetPageBackgroundRedrawArea(self, dc, wnd, page_old_size, page_new_size) -> 'Rect':
        """ Calculate the portion of a page background which needs to be redrawn when a page is resized.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetPanelClientSize(self, dc, wnd, size, client_offset) -> 'Size':
        """ Calculate the client size of a panel for a given overall size.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetPanelExtButtonArea(self, dc, wnd, rect) -> 'Rect':
        """ Calculate the position and size of the panel extension button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetPanelSize(self, dc, wnd, client_size, client_offset) -> 'Size':
        """ Calculate the size of a panel for a given client size.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetRibbonHelpButtonArea(self, rect: 'Rect') -> 'Rect':
        """ Calculate the position and size of the ribbonâs help button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetScrollButtonMinimumSize(self, dc, wnd, style) -> 'Size':
        """ Calculate the minimum size (in pixels) of a scroll button.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetTabCtrlHeight(self, dc, wnd, pages) -> int:
        """ Calculate the height (in pixels) of the tab region of a ribbon bar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetToolSize(self, dc, wnd, bitmap_size, kind, is_first, is_last, dropdown_region) -> 'Size':
        """ Calculate the size of a tool within a   wx.ribbon.RibbonToolBar.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def SetColour(self, id, colour) -> None:
        """ Set the value of a certain colour setting to the value colour.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def SetColourScheme(self, primary, secondary, tertiary) -> None:
        """ Set all applicable colour settings from a few base colours.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def SetFlags(self, flags: int) -> None:
        """ Set the style flags.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def SetFont(self, id, font) -> None:
        """ Set the value of a certain font setting to the value font.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def SetMetric(self, id, new_val) -> None:
        """ Set the value of a certain integer setting to the value new_val.

            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    Flags: int  # See GetFlags and SetFlags



RibbonScrollButtonStyle: TypeAlias = int  # Enumeration

RIBBON_SCROLL_BTN_LEFT: int

RIBBON_SCROLL_BTN_RIGHT: int

RIBBON_SCROLL_BTN_UP: int

RIBBON_SCROLL_BTN_DOWN: int

RIBBON_SCROLL_BTN_DIRECTION_MASK: int

RIBBON_SCROLL_BTN_NORMAL: int

RIBBON_SCROLL_BTN_HOVERED: int

RIBBON_SCROLL_BTN_ACTIVE: int

RIBBON_SCROLL_BTN_STATE_MASK: int

RIBBON_SCROLL_BTN_FOR_OTHER: int

RIBBON_SCROLL_BTN_FOR_TABS: int

RIBBON_SCROLL_BTN_FOR_PAGE: int

RIBBON_SCROLL_BTN_FOR_MASK: int

class RibbonPageTabInfo:
    """ A public C++ attribute of type bool.

        Source: https://docs.wxpython.org/wx.ribbon.RibbonPageTabInfo.html
    """
    active: Any  # A public C++ attribute of type bool.
    highlight: Any  # A public C++ attribute of type bool.
    hovered: Any  # A public C++ attribute of type bool.
    ideal_width: Any  # A public C++ attribute of type int.
    minimum_width: Any  # A public C++ attribute of type int.
    page: Any  # A public C++ attribute of type RibbonPage     .
    rect: Any  # A public C++ attribute of type Rect     .
    shown: Any  # A public C++ attribute of type bool.
    small_begin_need_separator_width: Any  # A public C++ attribute of type int.
    small_must_have_separator_width: Any  # A public C++ attribute of type int.



RibbonArtSetting: TypeAlias = int  # Enumeration

RIBBON_ART_TAB_SEPARATION_SIZE: int

RIBBON_ART_PAGE_BORDER_LEFT_SIZE: int

RIBBON_ART_PAGE_BORDER_TOP_SIZE: int

RIBBON_ART_PAGE_BORDER_RIGHT_SIZE: int

RIBBON_ART_PAGE_BORDER_BOTTOM_SIZE: int

RIBBON_ART_PANEL_X_SEPARATION_SIZE: int

RIBBON_ART_PANEL_Y_SEPARATION_SIZE: int

RIBBON_ART_TOOL_GROUP_SEPARATION_SIZE: int

RIBBON_ART_GALLERY_BITMAP_PADDING_LEFT_SIZE: int

RIBBON_ART_PANEL_LABEL_FONT: int

RIBBON_ART_BUTTON_BAR_LABEL_FONT: int

RIBBON_ART_TAB_LABEL_FONT: int

RIBBON_ART_BUTTON_BAR_LABEL_COLOUR: int

RIBBON_ART_BUTTON_BAR_LABEL_DISABLED_COLOUR: int

RIBBON_ART_BUTTON_BAR_HOVER_BORDER_COLOUR: int

RIBBON_ART_BUTTON_BAR_HOVER_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_BUTTON_BAR_HOVER_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_BUTTON_BAR_HOVER_BACKGROUND_COLOUR: int

RIBBON_ART_BUTTON_BAR_HOVER_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_BUTTON_BAR_ACTIVE_BORDER_COLOUR: int

RIBBON_ART_BUTTON_BAR_ACTIVE_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_BUTTON_BAR_ACTIVE_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_BUTTON_BAR_ACTIVE_BACKGROUND_COLOUR: int

RIBBON_ART_BUTTON_BAR_ACTIVE_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_GALLERY_BORDER_COLOUR: int

RIBBON_ART_GALLERY_HOVER_BACKGROUND_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_BACKGROUND_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_FACE_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_HOVER_BACKGROUND_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_HOVER_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_HOVER_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_HOVER_FACE_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_ACTIVE_BACKGROUND_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_ACTIVE_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_ACTIVE_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_ACTIVE_FACE_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_DISABLED_BACKGROUND_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_DISABLED_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_DISABLED_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_DISABLED_FACE_COLOUR: int

RIBBON_ART_GALLERY_ITEM_BORDER_COLOUR: int

RIBBON_ART_TAB_LABEL_COLOUR: int

RIBBON_ART_TAB_ACTIVE_LABEL_COLOUR: int

RIBBON_ART_TAB_HOVER_LABEL_COLOUR: int

RIBBON_ART_TAB_SEPARATOR_COLOUR: int

RIBBON_ART_TAB_SEPARATOR_GRADIENT_COLOUR: int

RIBBON_ART_TAB_CTRL_BACKGROUND_COLOUR: int

RIBBON_ART_TAB_CTRL_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_TAB_HOVER_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_TAB_HOVER_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_TAB_HOVER_BACKGROUND_COLOUR: int

RIBBON_ART_TAB_HOVER_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_TAB_ACTIVE_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_TAB_ACTIVE_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_TAB_ACTIVE_BACKGROUND_COLOUR: int

RIBBON_ART_TAB_ACTIVE_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_TAB_BORDER_COLOUR: int

RIBBON_ART_PANEL_BORDER_COLOUR: int

RIBBON_ART_PANEL_BORDER_GRADIENT_COLOUR: int

RIBBON_ART_PANEL_HOVER_BORDER_COLOUR: int

RIBBON_ART_PANEL_HOVER_BORDER_GRADIENT_COLOUR: int

RIBBON_ART_PANEL_MINIMISED_BORDER_COLOUR: int

RIBBON_ART_PANEL_MINIMISED_BORDER_GRADIENT_COLOUR: int

RIBBON_ART_PANEL_LABEL_BACKGROUND_COLOUR: int

RIBBON_ART_PANEL_LABEL_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_PANEL_LABEL_COLOUR: int

RIBBON_ART_PANEL_HOVER_LABEL_BACKGROUND_COLOUR: int

RIBBON_ART_PANEL_HOVER_LABEL_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_PANEL_HOVER_LABEL_COLOUR: int

RIBBON_ART_PANEL_MINIMISED_LABEL_COLOUR: int

RIBBON_ART_PANEL_ACTIVE_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_PANEL_ACTIVE_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_PANEL_ACTIVE_BACKGROUND_COLOUR: int

RIBBON_ART_PANEL_ACTIVE_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_PAGE_BORDER_COLOUR: int

RIBBON_ART_PAGE_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_PAGE_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_PAGE_BACKGROUND_COLOUR: int

RIBBON_ART_PAGE_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_PAGE_HOVER_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_PAGE_HOVER_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_PAGE_HOVER_BACKGROUND_COLOUR: int

RIBBON_ART_PAGE_HOVER_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_TOOLBAR_BORDER_COLOUR: int

RIBBON_ART_TOOLBAR_HOVER_BORDER_COLOUR: int

RIBBON_ART_TOOLBAR_FACE_COLOUR: int

RIBBON_ART_TOOL_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_TOOL_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_TOOL_BACKGROUND_COLOUR: int

RIBBON_ART_TOOL_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_TOOL_HOVER_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_TOOL_HOVER_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_TOOL_HOVER_BACKGROUND_COLOUR: int

RIBBON_ART_TOOL_HOVER_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_TOOL_ACTIVE_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_TOOL_ACTIVE_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_TOOL_ACTIVE_BACKGROUND_COLOUR: int

RIBBON_ART_TOOL_ACTIVE_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_BUTTON_BAR_LABEL_HIGHLIGHT_COLOUR: int

RIBBON_ART_BUTTON_BAR_LABEL_HIGHLIGHT_GRADIENT_COLOUR: int

RIBBON_ART_BUTTON_BAR_LABEL_HIGHLIGHT_TOP_COLOUR: int

RIBBON_ART_BUTTON_BAR_LABEL_HIGHLIGHT_GRADIENT_TOP_COLOUR: int

RibbonButtonBarButtonBase: TypeAlias = Any

RibbonToolBarToolBase: TypeAlias = Any

RibbonGalleryItem: TypeAlias = Any

