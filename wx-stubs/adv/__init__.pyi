# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class CommandLinkButton(Button):
    """ Objects of this class are similar in appearance to the normal
Buttons but are similar to the links in a web page in functionality.

        Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def Create(self, parent, id=ID_ANY, mainLabel="", note="", pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=ButtonNameStr) -> bool:
        """ Button creation function for two-step creation.

            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def GetLabel(self) -> str:
        """ Returns the string label for the button.

            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def GetMainLabel(self) -> str:
        """ Returns the current main label.

            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def GetNote(self) -> str:
        """ Returns the currently used note.

            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def SetLabel(self, label: str) -> None:
        """ Sets the string label and note for the button.

            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def SetMainLabel(self, mainLabel: str) -> None:
        """ Changes the main label.

            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def SetMainLabelAndNote(self, mainLabel, note) -> None:
        """ Sets a new main label and note for the button.

            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def SetNote(self, note: str) -> None:
        """ Changes the note.

            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    Label: str  # See GetLabel and SetLabel
    MainLabel: str  # See GetMainLabel and SetMainLabel
    Note: str  # See GetNote and SetNote



ID_ANY: int

class EditableListBox(Panel):
    """ An editable listbox is composite control that lets the user easily
enter, delete and reorder a list of strings.

        Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def Create(self, parent, id=ID_ANY, label="", pos=DefaultPosition, size=DefaultSize, style=EL_DEFAULT_STYLE, name=EditableListBoxNameStr) -> bool:
        """ Creates the editable listbox for two-step construction.

            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetDelButton(self) -> 'BitmapButton':
        """ Returns a reference to the delete button used in the EditableListBox.

            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetDownButton(self) -> 'BitmapButton':
        """ Returns a reference to the down button used in the EditableListBox.

            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetEditButton(self) -> 'BitmapButton':
        """ Returns a reference to the edit button used in the EditableListBox.

            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetListCtrl(self) -> 'ListCtrl':
        """ Returns a reference to the listctrl used in the EditableListBox.

            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetNewButton(self) -> 'BitmapButton':
        """ Returns a reference to the new button used in the EditableListBox.

            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetStrings(self) -> list[str]:
        """ Returns a list of the current contents of the control.

            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetUpButton(self) -> 'BitmapButton':
        """ Returns a reference to the up button used in the EditableListBox.

            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def SetStrings(self, strings: list[str]) -> None:
        """ Replaces current contents with given strings.

            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    DelButton: 'BitmapButton'  # See GetDelButton
    DownButton: 'BitmapButton'  # See GetDownButton
    EditButton: 'BitmapButton'  # See GetEditButton
    ListCtrl: '_ListCtrl'  # See GetListCtrl
    NewButton: 'BitmapButton'  # See GetNewButton
    Strings: list[str]  # See GetStrings and SetStrings
    UpButton: 'BitmapButton'  # See GetUpButton



EL_ALLOW_NEW: int  # Allows the user to enter new strings.

EL_ALLOW_EDIT: int  # Allows the user to edit existing strings.

EL_ALLOW_DELETE: int  # Allows the user to delete existing strings.

EL_NO_REORDER: int  # Does not allow the user to reorder the strings.

EL_DEFAULT_STYLE: int  # Default style: EL_ALLOW_NEW|wxEL_ALLOW_EDIT|wxEL_ALLOW_DELETE. ^^

class OwnerDrawnComboBox(ComboCtrl,ItemContainer):
    """ OwnerDrawnComboBox is a combobox with owner-drawn list items.

        Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def Create(self, parent, id=ID_ANY, value="", pos=DefaultPosition, size=DefaultSize, choices=[], style=0, validator=DefaultValidator, name=ComboBoxNameStr) -> bool:
        """ Creates the combobox for two-step construction.

            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def GetWidestItem(self) -> int:
        """ Returns index to the widest item in the list.

            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def GetWidestItemWidth(self) -> int:
        """ Returns width of the widest item in the list.

            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def IsListEmpty(self) -> bool:
        """ Returns True if the list of combobox choices is empty.

            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def IsTextEmpty(self) -> bool:
        """ Returns True if the text of the combobox is empty.

            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def OnDrawBackground(self, dc, rect, item, flags) -> None:
        """ This method is used to draw the items background and, maybe, a border around it.

            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def OnDrawItem(self, dc, rect, item, flags) -> None:
        """ The derived class may implement this function to actually draw the item with the given index on the provided DC.

            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def OnMeasureItem(self, item: int) -> 'Coord':
        """ The derived class may implement this method to return the height of the specified item (in pixels).

            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def OnMeasureItemWidth(self, item: int) -> 'Coord':
        """ The derived class may implement this method to return the width of the specified item (in pixels).

            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    WidestItem: int  # See GetWidestItem
    WidestItemWidth: int  # See GetWidestItemWidth



ODCB_DCLICK_CYCLES: int  # Double-clicking cycles item if wx.CB_READONLY is also used. Synonymous with wx.CC_SPECIAL_DCLICK.

ODCB_STD_CONTROL_PAINT: int  # Control itself is not custom painted using OnDrawItem. Even if this style is not used, writable   wx.adv.OwnerDrawnComboBox  is never custom painted unless SetCustomPaintWidth  is called. ^^

EVT_COMBOBOX: int  # Process a wxEVT_COMBOBOX event, when an item on the list is selected. Note that calling GetValue  returns the new value of selection. ^^

CB_READONLY: int

CC_SPECIAL_DCLICK: int

class BitmapComboBox(ComboBox):
    """ A combobox that displays bitmap in front of the list items.

        Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def Append(self, *args, **kw) -> int:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def Create(self, parent, id=ID_ANY, value="", pos=DefaultPosition, size=DefaultSize, choices=[], style=0, validator=DefaultValidator, name=BitmapComboBoxNameStr) -> bool:
        """ Creates the combobox for two-step construction.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def Dismiss(self) -> None:
        """ Hides the list box portion of the combo box.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def FindString(self, string, caseSensitive=False) -> int:
        """ Finds an item whose label matches the given string.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetBitmapSize(self) -> 'Size':
        """ Returns the size of the bitmaps used in the combo box.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetCount(self) -> int:
        """ Returns the number of items in the control.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetInsertionPoint(self) -> int:
        """ Same as wx.TextEntry.GetInsertionPoint .

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetItemBitmap(self, n: int) -> 'Bitmap':
        """ Returns the bitmap of the item with the given index.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetSelection(self) -> int:
        """ Returns the index of the selected item or  NOT_FOUND   if no item is selected.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetTextSelection(self) -> tuple:
        """ Gets the current selection span.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetString(self, n: int) -> str:
        """ Returns the label of the item with the given index.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def Insert(self, *args, **kw) -> int:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def IsListEmpty(self) -> bool:
        """ Returns True if the list of combobox choices is empty.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def IsTextEmpty(self) -> bool:
        """ Returns True if the text of the combobox is empty.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def Popup(self) -> None:
        """ Shows the list box portion of the combo box.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def SetItemBitmap(self, n, bitmap) -> None:
        """ Sets the bitmap for the given item.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def SetSelection(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def SetString(self, n, text) -> None:
        """ Changes the text of the specified combobox item.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def SetTextSelection(self, from_, to_) -> None:
        """ Same as wx.TextEntry.SetSelection .

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def SetValue(self, text: str) -> None:
        """ Sets the text for the combobox text field.

            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    BitmapSize: 'Size'  # See GetBitmapSize
    Count: int  # See GetCount
    InsertionPoint: int  # See GetInsertionPoint
    Selection: int  # See GetSelection and SetSelection



CB_SORT: int  # Sorts the entries in the list alphabetically.

TE_PROCESS_ENTER: int  # The control will generate the event wxEVT_TEXT_ENTER (otherwise pressing Enter key is either processed internally by the control or used for navigation between dialog controls). Windows only. ^^

EVT_TEXT: int  # Process a  wxEVT_TEXT   event, when the combobox text changes.

EVT_TEXT_ENTER: int  # Process a  wxEVT_TEXT_ENTER   event, when RETURN is pressed in the combobox. ^^

NOT_FOUND: int

class DateEvent(CommandEvent):
    """ This event class holds information about a date change and is used
together with DatePickerCtrl.

        Source: https://docs.wxpython.org/wx.adv.DateEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.DateEvent.html
        """

    def GetDate(self) -> 'DateTime':
        """ Returns the date.

            Source: https://docs.wxpython.org/wx.adv.DateEvent.html
        """

    def PyGetDate(self) -> None:
        """ Return the date as a Python datetime.date object.

            Source: https://docs.wxpython.org/wx.adv.DateEvent.html
        """

    def SetDate(self, date: 'DateTime') -> None:
        """ Sets the date carried by the event, normally only used by the library internally.

            Source: https://docs.wxpython.org/wx.adv.DateEvent.html
        """

    Date: 'DateTime'  # See GetDate and SetDate



class HyperlinkEvent(CommandEvent):
    """ This event class is used for the events generated by HyperlinkCtrl.

        Source: https://docs.wxpython.org/wx.adv.HyperlinkEvent.html
    """
    def __init__(self, generator, id, url) -> None:
        """ The constructor is not normally used by the user code.

            Source: https://docs.wxpython.org/wx.adv.HyperlinkEvent.html
        """

    def GetURL(self) -> str:
        """ Returns the URL of the hyperlink where the user has just clicked.

            Source: https://docs.wxpython.org/wx.adv.HyperlinkEvent.html
        """

    def SetURL(self, url: str) -> None:
        """ Sets the URL associated with the event.

            Source: https://docs.wxpython.org/wx.adv.HyperlinkEvent.html
        """

    URL: str  # See GetURL and SetURL



EVT_HYPERLINK: int  # User clicked on a hyperlink. ^^

class SashEvent(CommandEvent):
    """ A sash event is sent when the sash of a SashWindow has been dragged
by the user.

        Source: https://docs.wxpython.org/wx.adv.SashEvent.html
    """
    def __init__(self, id=0, edge=SASH_NONE) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    def GetDragRect(self) -> 'Rect':
        """ Returns the rectangle representing the new size the window would be if the resize was applied.

            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    def GetDragStatus(self) -> 'adv.SashDragStatus':
        """ Returns the status of the sash: one of wx.adv.SASH_STATUS_OK, wx.adv.SASH_STATUS_OUT_OF_RANGE.

            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    def GetEdge(self) -> 'adv.SashEdgePosition':
        """ Returns the dragged edge.

            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    def SetDragRect(self, rect: 'Rect') -> None:
        """ rect (wx.Rect) â

            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    def SetDragStatus(self, status: SashDragStatus) -> None:
        """ status (SashDragStatus) â

            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    def SetEdge(self, edge: SashEdgePosition) -> None:
        """ edge (SashEdgePosition) â

            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    DragRect: 'Rect'  # See GetDragRect and SetDragRect
    DragStatus: 'adv.SashDragStatus'  # See GetDragStatus and SetDragStatus
    Edge: 'adv.SashEdgePosition'  # See GetEdge and SetEdge



EVT_SASH_DRAGGED: int  # Process a  wxEVT_SASH_DRAGGED   event, when the user has finished dragging a sash.

EVT_SASH_DRAGGED_RANGE: int  # Process a  wxEVT_SASH_DRAGGED_RANGE   event, when the user has finished dragging a sash. The event handler is called when windows with ids in the given range have their sashes dragged. ^^

OK: int

SASH_STATUS_OK: int

SASH_STATUS_OUT_OF_RANGE: int

SASH_TOP: int

SASH_RIGHT: int

SASH_BOTTOM: int

SASH_LEFT: int

class BannerWindow(Window):
    """ A simple banner window showing either a bitmap or text.

        Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
        """

    def Create(self, parent, winid=ID_ANY, dir=LEFT, pos=DefaultPosition, size=DefaultSize, style=0, name=BannerWindowNameStr) -> bool:
        """ Really create the banner window for the objects created using the default constructor.

            Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
        """

    def SetBitmap(self, bmp: 'BitmapBundle') -> None:
        """ Provide the bitmap to use as background.

            Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
        """

    def SetGradient(self, start, end) -> None:
        """ Set the colours between which the gradient runs.

            Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
        """

    def SetText(self, title, message) -> None:
        """ Set the text to display.

            Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
        """



TOP: int

LEFT: int

BOTTOM: int

RIGHT: int

class SashWindow(Window):
    """ SashWindow allows any of its edges to have a sash which can be
dragged to resize the window.

        Source: https://docs.wxpython.org/wx.adv.SashWindow.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetDefaultBorderSize(self) -> int:
        """ Gets the default sash border size.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetEdgeMargin(self, edge: SashEdgePosition) -> int:
        """ Get border size.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetExtraBorderSize(self) -> int:
        """ Gets the addition border size between child and sash window.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetMaximumSizeX(self) -> int:
        """ Gets the maximum window size in the x direction.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetMaximumSizeY(self) -> int:
        """ Gets the maximum window size in the y direction.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetMinimumSizeX(self) -> int:
        """ Gets the minimum window size in the x direction.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetMinimumSizeY(self) -> int:
        """ Gets the minimum window size in the y direction.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetSashVisible(self, edge: SashEdgePosition) -> bool:
        """ Returns True if a sash is visible on the given edge, False otherwise.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SashHitTest(self, x, y, tolerance=2) -> 'adv.SashEdgePosition':
        """ Tests for x, y over sash.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetDefaultBorderSize(self, width: int) -> None:
        """ Sets the default sash border size.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetExtraBorderSize(self, width: int) -> None:
        """ Sets the additional border size between child and sash window.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetMaximumSizeX(self, min: int) -> None:
        """ Sets the maximum window size in the x direction.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetMaximumSizeY(self, min: int) -> None:
        """ Sets the maximum window size in the y direction.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetMinimumSizeX(self, min: int) -> None:
        """ Sets the minimum window size in the x direction.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetMinimumSizeY(self, min: int) -> None:
        """ Sets the minimum window size in the y direction.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetSashVisible(self, edge, visible) -> None:
        """ Call this function to make a sash visible or invisible on a particular edge.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SizeWindows(self) -> None:
        """ Resizes subwindows.

            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    DefaultBorderSize: int  # See GetDefaultBorderSize and SetDefaultBorderSize
    ExtraBorderSize: int  # See GetExtraBorderSize and SetExtraBorderSize
    MaximumSizeX: int  # See GetMaximumSizeX and SetMaximumSizeX
    MaximumSizeY: int  # See GetMaximumSizeY and SetMaximumSizeY
    MinimumSizeX: int  # See GetMinimumSizeX and SetMinimumSizeX
    MinimumSizeY: int  # See GetMinimumSizeY and SetMinimumSizeY



SW_3D: int  # Draws a 3D effect sash and border.

SW_3DSASH: int  # Draws a 3D effect sash.

SW_3DBORDER: int  # Draws a 3D effect border.

SW_BORDER: int  # Draws a thin black border. ^^

class AnimationCtrl(Control):
    """ This is a static control which displays an animation.

        Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
    """
    def __init__(self, parent, id=ID_ANY, anim=NullAnimation, pos=DefaultPosition, size=DefaultSize, style=AC_DEFAULT_STYLE, name=AnimationCtrlNameStr) -> None:
        """ Initializes the object and calls Create   with all the parameters.

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def Create(self, parent, id=ID_ANY, anim=NullAnimation, pos=DefaultPosition, size=DefaultSize, style=AC_DEFAULT_STYLE, name=AnimationCtrlNameStr) -> bool:
        """ Creates the control with the given anim  animation.

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def CreateAnimation(self) -> 'adv.Animation':
        """ Create a new animation object compatible with this control.

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    @staticmethod
    def CreateCompatibleAnimation() -> 'adv.Animation':
        """ Create a new animation object compatible with this control.

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def GetAnimation(self) -> 'adv.Animation':
        """ Returns the animation associated with this control.

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def GetInactiveBitmap(self) -> 'Bitmap':
        """ Returns the inactive bitmap shown in this control when the; see SetInactiveBitmap   for more info.

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def IsPlaying(self) -> bool:
        """ Returns True if the animation is being played.

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def Load(self, file, animType=ANIMATION_TYPE_ANY) -> bool:
        """ Loads the animation from the given stream and calls SetAnimation .

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def LoadFile(self, file, animType=ANIMATION_TYPE_ANY) -> bool:
        """ Loads the animation from the given file and calls SetAnimation .

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def Play(self) -> bool:
        """ Starts playing the animation.

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def SetAnimation(self, anim: 'adv.Animation') -> None:
        """ Sets the animation to play in this control.

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def SetInactiveBitmap(self, bmp: 'BitmapBundle') -> None:
        """ Sets the bitmap to show on the control when itâs not playing an animation.

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def Stop(self) -> None:
        """ Stops playing the animation.

            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    Animation: 'adv.Animation'  # See GetAnimation and SetAnimation
    InactiveBitmap: 'Bitmap'  # See GetInactiveBitmap and SetInactiveBitmap



AC_DEFAULT_STYLE: int  # The default style: wx.BORDER_NONE.

AC_NO_AUTORESIZE: int  # By default, the control will adjust its size to exactly fit to the size of the animation when SetAnimation is called. If this style flag is given, the control will not change its size ^^

BORDER_NONE: int

class CalendarCtrl(Control):
    """ The calendar control allows the user to pick a date.

        Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def Create(self, parent, id=ID_ANY, date=DefaultDateTime, pos=DefaultPosition, size=DefaultSize, style=CAL_SHOW_HOLIDAYS, name=CalendarNameStr) -> bool:
        """ Creates the control.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def EnableHolidayDisplay(self, display: bool=True) -> None:
        """ This function should be used instead of changing  CAL_SHOW_HOLIDAYS   style bit directly.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def EnableMonthChange(self, enable: bool=True) -> bool:
        """ This function should be used instead of changing  CAL_NO_MONTH_CHANGE   style bit.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetAttr(self, day: int) -> 'adv.CalendarDateAttr':
        """ Returns the attribute for the given date (should be in the range 1â¦31).

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetDate(self) -> 'DateTime':
        """ Gets the currently selected date.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetDateRange(self) -> tuple:
        """ Returns the limits currently being used.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetHeaderColourBg(self) -> 'Colour':
        """ Gets the background colour of the header part of the calendar window.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetHeaderColourFg(self) -> 'Colour':
        """ Gets the foreground colour of the header part of the calendar window.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetHighlightColourBg(self) -> 'Colour':
        """ Gets the background highlight colour.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetHighlightColourFg(self) -> 'Colour':
        """ Gets the foreground highlight colour.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetHolidayColourBg(self) -> 'Colour':
        """ Return the background colour currently used for holiday highlighting.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetHolidayColourFg(self) -> 'Colour':
        """ Return the foreground colour currently used for holiday highlighting.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def HitTest(self, pos: Union[tuple[int, int], 'Point']) -> tuple:
        """ Returns one of CalendarHitTestResult constants and fills either date  or wd  pointer with the corresponding value depending on the hit test code.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def Mark(self, day, mark) -> None:
        """ Mark or unmark the day.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def PyGetDate(self) -> None:
        """ Return the date as a Python datetime.date object.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def ResetAttr(self, day: int) -> None:
        """ Clears any attributes associated with the given day (in the range 1â¦31).

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetAttr(self, day, attr) -> None:
        """ Associates the attribute with the specified date (in the range 1â¦31).

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetDate(self, date: 'DateTime') -> bool:
        """ Sets the current date.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetDateRange(self, lowerdate=DefaultDateTime, upperdate=DefaultDateTime) -> bool:
        """ Restrict the dates that can be selected in the control to the specified range.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetHeaderColours(self, colFg, colBg) -> None:
        """ Set the colours used for painting the weekdays at the top of the control.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetHighlightColours(self, colFg, colBg) -> None:
        """ Set the colours to be used for highlighting the currently selected date.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetHoliday(self, day: int) -> None:
        """ Marks the specified day as being a holiday in the current month.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetHolidayColours(self, colFg, colBg) -> None:
        """ Sets the colours to be used for the holidays highlighting.

            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    Date: 'DateTime'  # See GetDate and SetDate
    DateRange: tuple  # See GetDateRange and SetDateRange
    HeaderColourBg: 'Colour'  # See GetHeaderColourBg
    HeaderColourFg: 'Colour'  # See GetHeaderColourFg
    HighlightColourBg: 'Colour'  # See GetHighlightColourBg
    HighlightColourFg: 'Colour'  # See GetHighlightColourFg
    HolidayColourBg: 'Colour'  # See GetHolidayColourBg
    HolidayColourFg: 'Colour'  # See GetHolidayColourFg



CAL_SUNDAY_FIRST: int  # Show Sunday as the first day in the week (not in wxGTK)

CAL_MONDAY_FIRST: int  # Show Monday as the first day in the week (not in wxGTK)

CAL_SHOW_HOLIDAYS: int  # Highlight holidays in the calendar (only generic)

CAL_NO_YEAR_CHANGE: int  # Disable the year changing (deprecated, only generic)

CAL_NO_MONTH_CHANGE: int  # Disable the month (and, implicitly, the year) changing

CAL_SHOW_SURROUNDING_WEEKS: int  # Show the neighbouring weeks in the previous and next months (only generic, always on for the native controls)

CAL_SEQUENTIAL_MONTH_SELECTION: int  # Use alternative, more compact, style for the month and year selection controls. (only generic)

CAL_SHOW_WEEK_NUMBERS: int  # Show week numbers on the left side of the calendar. (not in generic) ^^

EVT_CALENDAR: int  # A day was double clicked in the calendar.

EVT_CALENDAR_SEL_CHANGED: int  # The selected date changed.

EVT_CALENDAR_PAGE_CHANGED: int  # The selected month (and/or year) changed.

EVT_CALENDAR_WEEKDAY_CLICKED: int  # User clicked on the week day header (only generic).

EVT_CALENDAR_WEEK_CLICKED: int  # User clicked on the week of the year number (only generic). ^^

class DatePickerCtrl(Control):
    """ This control allows the user to select a date.

        Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    def Create(self, parent, id=ID_ANY, dt=DefaultDateTime, pos=DefaultPosition, size=DefaultSize, style=DP_DEFAULT|DP_SHOWCENTURY, validator=DefaultValidator, name="datectrl") -> bool:
        """ Create the control window.

            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    def GetRange(self) -> tuple:
        """ If the control had been previously limited to a range of dates using SetRange , returns the lower and upper bounds of this range.

            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    def GetValue(self) -> 'DateTime':
        """ Returns the currently entered date.

            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    def SetNullText(self, text: str) -> None:
        """ Set the text to show when there is no valid value.

            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    def SetRange(self, dt1, dt2) -> None:
        """ Sets the valid range for the date selection.

            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    def SetValue(self, dt: 'DateTime') -> None:
        """ Changes the current value of the control.

            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    Value: 'DateTime'  # See GetValue and SetValue



DP_SPIN: int  # Creates a control without a month calendar drop down but with spin-control-like arrows to change individual date components. This style is not supported by the generic version.

DP_DROPDOWN: int  # Creates a control with a month calendar drop-down part from which the user can select a date. This style is not supported in OSX/Cocoa native version.

DP_DEFAULT: int  # Creates a control with the style that is best supported for the current platform (currently wx.adv.DP_SPIN under Windows and OSX/Cocoa and wx.adv.DP_DROPDOWN elsewhere).

DP_ALLOWNONE: int  # With this style, the control allows the user to not enter any valid date at all. Without it - the default - the control always has some valid date. This style is not supported in OSX/Cocoa native version.

DP_SHOWCENTURY: int  # Forces display of the century in the default date format. Without this style the century could be displayed, or not, depending on the default date representation in the system. This style is not supported in OSX/Cocoa native version currently. ^^

EVT_DATE_CHANGED: int  # Process a wxEVT_DATE_CHANGED event, which fires when the user changes the current selection in the control. ^^

class HyperlinkCtrl(Control):
    """ This class shows a static text element which links to an URL.

        Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def Create(self, parent, id=ID_ANY, label="", url="", pos=DefaultPosition, size=DefaultSize, style=HL_DEFAULT_STYLE, name=HyperlinkCtrlNameStr) -> bool:
        """ Creates the hyperlink control.

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def GetHoverColour(self) -> 'Colour':
        """ Returns the colour used to print the label of the hyperlink when the mouse is over the control.

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def GetNormalColour(self) -> 'Colour':
        """ Returns the colour used to print the label when the link has never been clicked before (i.e. the link has not been visited) and the mouse is not over the control.

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def GetURL(self) -> str:
        """ Returns the URL associated with the hyperlink.

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def GetVisited(self) -> bool:
        """ Returns True if the hyperlink has already been clicked by the user at least one time.

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def GetVisitedColour(self) -> 'Colour':
        """ Returns the colour used to print the label when the mouse is not over the control and the link has already been clicked before (i.e. the link has been visited).

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def SetHoverColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used to print the label of the hyperlink when the mouse is over the control.

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def SetNormalColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used to print the label when the link has never been clicked before (i.e. the link has not been visited) and the mouse is not over the control.

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def SetURL(self, url: str) -> None:
        """ Sets the URL associated with the hyperlink.

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def SetVisited(self, visited: bool=True) -> None:
        """ Marks the hyperlink as visited (see wx.adv.HyperlinkCtrl.SetVisitedColour ).

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def SetVisitedColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used to print the label when the mouse is not over the control and the link has already been clicked before (i.e. the link has been visited).

            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    HoverColour: 'Colour'  # See GetHoverColour and SetHoverColour
    NormalColour: 'Colour'  # See GetNormalColour and SetNormalColour
    URL: str  # See GetURL and SetURL
    Visited: bool  # See GetVisited and SetVisited
    VisitedColour: 'Colour'  # See GetVisitedColour and SetVisitedColour



HL_ALIGN_LEFT: int  # Align the text to the left.

HL_ALIGN_RIGHT: int  # Align the text to the right. This style is not supported under Windows.

HL_ALIGN_CENTRE: int  # Center the text (horizontally). This style is not supported under Windows.

HL_CONTEXTMENU: int  # Pop up a context menu when the hyperlink is right-clicked. The context menu contains a âCopy URLâ menu item which is automatically handled by the hyperlink and which just copies in the clipboard the URL (not the label) of the control.

HL_DEFAULT_STYLE: int  # The default style for   wx.adv.HyperlinkCtrl: BORDER_NONE|wxHL_CONTEXTMENU|wxHL_ALIGN_CENTRE. ^^

class TimePickerCtrl(Control):
    """ This control allows the user to enter time.

        Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    def Create(self, parent, id=ID_ANY, dt=DefaultDateTime, pos=DefaultPosition, size=DefaultSize, style=TP_DEFAULT, validator=DefaultValidator, name=TimePickerCtrlNameStr) -> bool:
        """ Create the control window.

            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    def GetTime(self) -> tuple:
        """ Returns the currently entered time as hours, minutes and seconds.

            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    def GetValue(self) -> 'DateTime':
        """ Returns the currently entered time.

            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    def SetTime(self, hour, min, sec) -> bool:
        """ Changes the current time of the control.

            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    def SetValue(self, dt: 'DateTime') -> None:
        """ Changes the current value of the control.

            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    Value: 'DateTime'  # See GetValue and SetValue



EVT_TIME_CHANGED: int  # Process a wxEVT_TIME_CHANGED event, which fires when the user changes the current selection in the control. ^^

class PropertySheetDialog(Dialog):
    """ This class represents a property sheet dialog: a tabbed dialog for
showing settings.

        Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def AddBookCtrl(self, sizer: 'Sizer') -> None:
        """ Override this if you wish to add the book control in a way different from the standard way (for example, using different spacing).

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def Create(self, parent, id=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize, style=DEFAULT_DIALOG_STYLE, name=DialogNameStr) -> bool:
        """ Call this from your own Create function, before adding buttons and pages.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def CreateBookCtrl(self) -> 'BookCtrlBase':
        """ Override this if you wish to create a different kind of book control; by default, the value passed to SetSheetStyle   is used to determine the control.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def CreateButtons(self, flags: int=OK|CANCEL) -> None:
        """ Call this to create the buttons for the dialog.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def GetBookCtrl(self) -> 'BookCtrlBase':
        """ Returns the book control that will contain your settings pages.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def GetContentWindow(self) -> 'Window':
        """ Override this to return a window containing the main content of the dialog.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def GetInnerSizer(self) -> 'Sizer':
        """ Returns the inner sizer that contains the book control and button sizer.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def GetSheetInnerBorder(self) -> int:
        """ Returns the border around the book control only.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def GetSheetOuterBorder(self) -> int:
        """ Returns the border around the whole dialog.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def GetSheetStyle(self) -> int:
        """ Returns the sheet style.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def LayoutDialog(self, centreFlags: int=BOTH) -> None:
        """ Call this to lay out the dialog.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def SetBookCtrl(self, bookCtrl: 'BookCtrlBase') -> None:
        """ Sets the book control used for the dialog.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def SetInnerSizer(self, sizer: 'Sizer') -> None:
        """ Set the inner sizer that contains the book control and button sizer.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def SetSheetInnerBorder(self, border: int) -> None:
        """ Set the border around the book control only.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def SetSheetOuterBorder(self, border: int) -> None:
        """ Set the border around the whole dialog.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def SetSheetStyle(self, style: int) -> None:
        """ You can customize the look and feel of the dialog by setting the sheet style.

            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    BookCtrl: 'BookCtrlBase'  # See GetBookCtrl and SetBookCtrl
    ContentWindow: 'Window'  # See GetContentWindow
    InnerSizer: 'Sizer'  # See GetInnerSizer and SetInnerSizer
    SheetInnerBorder: int  # See GetSheetInnerBorder and SetSheetInnerBorder
    SheetOuterBorder: int  # See GetSheetOuterBorder and SetSheetOuterBorder
    SheetStyle: int  # See GetSheetStyle and SetSheetStyle



class Wizard(Dialog):
    """ Wizard is the central class for implementing âwizard-likeâ dialogs.

        Source: https://docs.wxpython.org/wx.adv.Wizard.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def Create(*args, **kwargs) -> bool:
        """ Creates the wizard dialog.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def FitToPage(self, firstPage: 'adv.WizardPage') -> None:
        """ This method is obsolete, use GetPageAreaSizer   instead.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetBitmap(self) -> 'Bitmap':
        """ Returns the bitmap used for the wizard.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetBitmapBackgroundColour(self) -> 'Colour':
        """ Returns the colour that should be used to fill the area not taken up by the wizard or page bitmap, if a non-zero bitmap placement flag has been set.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetBitmapPlacement(self) -> int:
        """ Returns the flags indicating how the wizard or page bitmap should be expanded and positioned to fit the page height.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetCurrentPage(self) -> 'adv.WizardPage':
        """ Get the current page while the wizard is running.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetMinimumBitmapWidth(self) -> int:
        """ Returns the minimum width for the bitmap that will be constructed to contain the actual wizard or page bitmap if a non-zero bitmap placement flag has been set.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetPageAreaSizer(self) -> 'Sizer':
        """ Returns pointer to page area sizer.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetPageSize(self) -> 'Size':
        """ Returns the size available for the pages.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def HasNextPage(self, page: 'adv.WizardPage') -> bool:
        """ Return True if this page is not the last one in the wizard.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def HasPrevPage(self, page: 'adv.WizardPage') -> bool:
        """ Returns True if this page is not the first one in the wizard.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def IsRunning(self) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def RunWizard(self, firstPage: 'adv.WizardPage') -> bool:
        """ Executes the wizard starting from the given page, returning True if it was successfully finished or False if user cancelled it.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def SetBitmap(self, bitmap: 'BitmapBundle') -> None:
        """ Sets the bitmap used for the wizard.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def SetBitmapBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour that should be used to fill the area not taken up by the wizard or page bitmap, if a non-zero bitmap placement flag has been set.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def SetBitmapPlacement(self, placement: int) -> None:
        """ Sets the flags indicating how the wizard or page bitmap should be expanded and positioned to fit the page height.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def SetBorder(self, border: int) -> None:
        """ Sets width of border around page area.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def SetMinimumBitmapWidth(self, width: int) -> None:
        """ Sets the minimum width for the bitmap that will be constructed to contain the actual wizard or page bitmap if a non-zero bitmap placement flag has been set.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def SetPageSize(self, sizePage: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the minimal size to be made available for the wizard pages.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def ShowPage(self, page, goingForward=True) -> bool:
        """ Show the given wizard page.

            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    Bitmap: '_Bitmap'  # See GetBitmap and SetBitmap
    BitmapBackgroundColour: 'Colour'  # See GetBitmapBackgroundColour and SetBitmapBackgroundColour
    BitmapPlacement: int  # See GetBitmapPlacement and SetBitmapPlacement
    CurrentPage: 'adv.WizardPage'  # See GetCurrentPage
    MinimumBitmapWidth: int  # See GetMinimumBitmapWidth and SetMinimumBitmapWidth
    PageAreaSizer: 'Sizer'  # See GetPageAreaSizer
    PageSize: 'Size'  # See GetPageSize and SetPageSize



EVT_WIZARD_PAGE_CHANGED: int  # The page has just been changed (this event cannot be vetoed).

EVT_WIZARD_PAGE_CHANGING: int  # The page is being changed (this event can be vetoed).

EVT_WIZARD_BEFORE_PAGE_CHANGED: int  # Called after Next is clicked but before GetNext is called. Unlike EVT_WIZARD_CHANGING, the handler for this function can change state that might affect the return value of GetNext. This event can be vetoed.

EVT_WIZARD_PAGE_SHOWN: int  # The page was shown and laid out (this event cannot be vetoed).

EVT_WIZARD_CANCEL: int  # The user attempted to cancel the wizard (this event may also be vetoed).

EVT_WIZARD_HELP: int  # The wizard help button was pressed.

EVT_WIZARD_FINISHED: int  # The wizard finished button was pressed. ^^

WIZARD_EX_HELPBUTTON: int

ID_HELP: int

WIZARD_VALIGN_TOP: int

WIZARD_VALIGN_CENTRE: int

WIZARD_VALIGN_BOTTOM: int

WIZARD_HALIGN_LEFT: int

WIZARD_HALIGN_CENTRE: int

WIZARD_HALIGN_RIGHT: int

WIZARD_TILE: int

class CalculateLayoutEvent(Event):
    """ This event is sent by LayoutAlgorithm to calculate the amount of the
remaining client area that the window should occupy.

        Source: https://docs.wxpython.org/wx.adv.CalculateLayoutEvent.html
    """
    def __init__(self, id: int=0) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.adv.CalculateLayoutEvent.html
        """

    def GetFlags(self) -> int:
        """ Returns the flags associated with this event.

            Source: https://docs.wxpython.org/wx.adv.CalculateLayoutEvent.html
        """

    def GetRect(self) -> 'Rect':
        """ Before the event handler is entered, returns the remaining parent client area that the window could occupy.

            Source: https://docs.wxpython.org/wx.adv.CalculateLayoutEvent.html
        """

    def SetFlags(self, flags: int) -> None:
        """ Sets the flags associated with this event.

            Source: https://docs.wxpython.org/wx.adv.CalculateLayoutEvent.html
        """

    def SetRect(self, rect: 'Rect') -> None:
        """ Call this to specify the new remaining parent client area, after the space occupied by the window has been subtracted.

            Source: https://docs.wxpython.org/wx.adv.CalculateLayoutEvent.html
        """

    Flags: int  # See GetFlags and SetFlags
    Rect: '_Rect'  # See GetRect and SetRect



EVT_CALCULATE_LAYOUT: int  # Process a  wxEVT_CALCULATE_LAYOUT   event, which asks the window to take a âbiteâ out of a rectangle provided by the algorithm. ^^

class QueryLayoutInfoEvent(Event):
    """ This event is sent when LayoutAlgorithm wishes to get the size,
orientation and alignment of a window.

        Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
    """
    def __init__(self, id: int=0) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def GetAlignment(self) -> int:
        """ Specifies the alignment of the window (which side of the remaining parent client area the window sticks to).

            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def GetFlags(self) -> int:
        """ Returns the flags associated with this event.

            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def GetOrientation(self) -> 'adv.LayoutOrientation':
        """ Returns the orientation that the event handler specified to the event object.

            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def GetRequestedLength(self) -> int:
        """ Returns the requested length of the window in the direction of the window orientation.

            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def GetSize(self) -> 'Size':
        """ Returns the size that the event handler specified to the event object as being the requested size of the window.

            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def SetAlignment(self, alignment: int) -> None:
        """ Call this to specify the alignment of the window (which side of the remaining parent client area the window sticks to).

            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def SetFlags(self, flags: int) -> None:
        """ Sets the flags associated with this event.

            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def SetOrientation(self, orientation: LayoutOrientation) -> None:
        """ Call this to specify the orientation of the window.

            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def SetRequestedLength(self, length: int) -> None:
        """ Sets the requested length of the window in the direction of the window orientation.

            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def SetSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Call this to let the calling code know what the size of the window is.

            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    Alignment: int  # See GetAlignment and SetAlignment
    Flags: int  # See GetFlags and SetFlags
    Orientation: 'adv.LayoutOrientation'  # See GetOrientation and SetOrientation
    RequestedLength: int  # See GetRequestedLength and SetRequestedLength
    Size: '_Size'  # See GetSize and SetSize



EVT_QUERY_LAYOUT_INFO: int  # Process a  wxEVT_QUERY_LAYOUT_INFO   event, to get size, orientation and alignment from a window. ^^

LAYOUT_TOP: int

LAYOUT_LEFT: int

LAYOUT_RIGHT: int

LAYOUT_BOTTOM: int

LAYOUT_HORIZONTAL: int

LAYOUT_VERTICAL: int

class TaskBarIconEvent(Event):
    """ The event class used by TaskBarIcon.

        Source: https://docs.wxpython.org/wx.adv.TaskBarIconEvent.html
    """
    def __init__(self, evtType, tbIcon) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.adv.TaskBarIconEvent.html
        """



class NotificationMessage(EvtHandler):
    """ This class allows showing the user a message non intrusively.

        Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def AddAction(self, actionid, label="") -> bool:
        """ Add an action to the notification.

            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def Close(self) -> bool:
        """ Hides the notification.

            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    @staticmethod
    def MSWUseToasts(shortcutPath="", appId="") -> bool:
        """ Enables toast notifications available since Windows 8 and suppresses the additional icon in the notification area on Windows 10.

            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def SetFlags(self, flags: int) -> None:
        """ This parameter can be currently used to specify the icon to show in the notification.

            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def SetIcon(self, icon: 'Icon') -> None:
        """ Specify a custom icon to be displayed in the notification.

            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def SetMessage(self, message: str) -> None:
        """ Set the main text of the notification.

            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def SetParent(self, parent: 'Window') -> None:
        """ Set the parent for this notification: the notification will be associated with the top level parent of this window or, if this method is not called, with the main application window by default.

            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def SetTitle(self, title: str) -> None:
        """ Set the title, it must be a concise string (not more than 64 characters), use SetMessage   to give the user more details.

            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def Show(self, timeout: int=Timeout_Auto) -> bool:
        """ Show the notification to the user and hides it after timeout  seconds are elapsed.

            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    @staticmethod
    def UseTaskBarIcon(icon: 'adv.TaskBarIcon') -> 'adv.TaskBarIcon':
        """ If the application already uses a   wx.adv.TaskBarIcon, it should be connected to notifications by using this method.

            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """



EVT_NOTIFICATION_MESSAGE_CLICK: int  # Process a  wxEVT_NOTIFICATION_MESSAGE_CLICK   event, when a notification is clicked.

EVT_NOTIFICATION_MESSAGE_DISMISSED: int  # Process a  wxEVT_NOTIFICATION_MESSAGE_DISMISSED   event, when a notification is dismissed by the user or times out.

EVT_NOTIFICATION_MESSAGE_ACTION: int  # Process a  wxEVT_NOTIFICATION_MESSAGE_ACTION   event, when the user selects on of the actions added by  AddAction  ^^

class TaskBarIcon(EvtHandler):
    """ This class represents a taskbar icon.

        Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
    """
    def __init__(self, iconType: TaskBarIconType=TBI_DEFAULT_TYPE) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def CreatePopupMenu(self) -> 'Menu':
        """ Called by the library when the user requests popup menu if GetPopupMenu   is not overridden.

            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def Destroy(self) -> None:
        """ This method is similar to wx.Window.Destroy   and can be used to schedule the task bar icon object for the delayed destruction: it will be deleted during the next event loop iteration, which allows the task bar icon to process any pending events for it before being destroyed.

            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def GetPopupMenu(self) -> 'Menu':
        """ Called by the library when the user requests popup menu.

            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    @staticmethod
    def IsAvailable() -> bool:
        """ Returns True if system tray is available in the desktop environment the app runs under.

            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def IsIconInstalled(self) -> bool:
        """ Returns True if SetIcon   was called with no subsequent RemoveIcon .

            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def IsOk(self) -> bool:
        """ Returns True if the object initialized successfully.

            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def PopupMenu(self, menu: 'Menu') -> bool:
        """ Pops up a menu at the current mouse position.

            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def RemoveIcon(self) -> bool:
        """ Removes the icon previously set with SetIcon .

            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def SetIcon(self, icon, tooltip="") -> bool:
        """ Sets the icon, and optional tooltip text.

            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def ShowBalloon(self, title, text, msec=0, flags=0) -> bool:
        """ Show a balloon notification (the icon must have been already
initialized using SetIcon).  Only implemented for Windows.

            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """



EVT_TASKBAR_MOVE: int  # Process a  wxEVT_TASKBAR_MOVE   event.

EVT_TASKBAR_LEFT_DOWN: int  # Process a  wxEVT_TASKBAR_LEFT_DOWN   event.

EVT_TASKBAR_LEFT_UP: int  # Process a  wxEVT_TASKBAR_LEFT_UP   event.

EVT_TASKBAR_RIGHT_DOWN: int  # Process a  wxEVT_TASKBAR_RIGHT_DOWN   event.

EVT_TASKBAR_RIGHT_UP: int  # Process a  wxEVT_TASKBAR_RIGHT_UP   event.

EVT_TASKBAR_LEFT_DCLICK: int  # Process a  wxEVT_TASKBAR_LEFT_DCLICK   event.

EVT_TASKBAR_RIGHT_DCLICK: int  # Process a  wxEVT_TASKBAR_RIGHT_DCLICK   event.

EVT_TASKBAR_CLICK: int  # This is a synonym for either EVT_TASKBAR_RIGHT_DOWN or wx.UP depending on the platform, use this event macro to catch the event which should result in the menu being displayed on the current platform. ^^

UP: int

class SplashScreen(Frame):
    """ SplashScreen shows a window with a thin border, displaying a bitmap
describing your application.

        Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
    """
    def __init__(self, bitmap, splashStyle, milliseconds, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=BORDER_SIMPLE|FRAME_NO_TASKBAR|STAY_ON_TOP) -> None:
        """ Construct the splash screen passing a bitmap, a style, a timeout, a window id, optional position and size, and a window style.

            Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
        """

    def GetBitmap(self) -> 'Bitmap':
        """ Get the spash screenâs bitmap

            Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
        """

    def GetSplashStyle(self) -> int:
        """ Returns the splash style (see   wx.adv.SplashScreen  for details).

            Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
        """

    def GetTimeout(self) -> int:
        """ Returns the timeout in milliseconds.

            Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
        """

    def SetBitmap(self, bitmap) -> None:
        """ Set a new bitmap for the splash screen.

            Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
        """

    Bitmap: '_Bitmap'  # See GetBitmap and SetBitmap
    SplashStyle: int  # See GetSplashStyle
    Timeout: int  # See GetTimeout



SPLASH_CENTRE_ON_PARENT: int

SPLASH_CENTRE_ON_SCREEN: int

SPLASH_NO_CENTRE: int

SPLASH_TIMEOUT: int

SPLASH_NO_TIMEOUT: int

class ExtHelpController(HelpControllerBase):
    """ This class implements help via an external browser.

        Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
    """
    def __init__(self, parentWindow: Optional['Window']=None) -> None:
        """ parentWindow (wx.Window) â

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def DisplayBlock(self, blockNo: int) -> bool:
        """ Display help for URL (using DisplayHelp) or keyword (using KeywordSearch)

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def DisplayContents(self) -> bool:
        """ Display list of all help entries.

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def DisplayHelp(self, relativeURL: str) -> bool:
        """ Call the browser using a relative URL.

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def DisplaySection(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def GetFrameParameters(self, size=None, pos=None, newFrameEachTime=None) -> 'Frame':
        """ Obtains the latest settings used by the help frame and the help frame.

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def Initialize(self, dir: str) -> bool:
        """ This must be called to tell the controller where to find the documentation.

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def KeywordSearch(self, k, mode=HELP_SEARCH_ALL) -> bool:
        """ Search comment/documentation fields in map file and present a list to chose from.

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def LoadFile(self, file: str="") -> bool:
        """ If file is ââ, reloads file given in Initialize.

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def OnQuit(self) -> None:
        """ Does nothing.

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def Quit(self) -> bool:
        """ Does nothing.

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def SetFrameParameters(self, titleFormat, size, pos=DefaultPosition, newFrameEachTime=False) -> None:
        """ Allows one to override the default settings for the help frame.

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def SetViewer(self, viewer="", flags=HELP_NETSCAPE) -> None:
        """ Tell it which browser to use.

            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    FrameParameters: 'Frame'  # See GetFrameParameters



HELP_NETSCAPE: int

class Joystick(Object):
    """ Joystick allows an application to control one or more joysticks.

        Source: https://docs.wxpython.org/wx.adv.Joystick.html
    """
    def __init__(self, joystick: int=JOYSTICK1) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetButtonState(self, *args, **kw) -> int:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetManufacturerId(self) -> int:
        """ Returns the manufacturer id.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetMaxAxes(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetMaxButtons(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetMovementThreshold(self) -> int:
        """ Returns the movement threshold, the number of steps outside which the joystick is deemed to have moved.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetNumberAxes(self) -> int:
        """ Returns the number of axes for this joystick.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetNumberButtons(self) -> int:
        """ Returns the number of buttons for this joystick.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    @staticmethod
    def GetNumberJoysticks() -> int:
        """ Returns the number of joysticks currently attached to the computer.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetPOVCTSPosition(self) -> int:
        """ Returns the point-of-view position, expressed in continuous, one-hundredth of a degree units.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetPOVPosition(self) -> int:
        """ Returns the point-of-view position, expressed in continuous, one-hundredth of a degree units, but limited to return 0, 9000, 18000 or 27000.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetPollingMax(self) -> int:
        """ Returns the maximum polling frequency.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetPollingMin(self) -> int:
        """ Returns the minimum polling frequency.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetPosition(self, *args, **kw) -> 'Point':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetProductId(self) -> int:
        """ Returns the product id for the joystick.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetProductName(self) -> str:
        """ Returns the product name for the joystick.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetRudderMax(self) -> int:
        """ Returns the maximum rudder position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetRudderMin(self) -> int:
        """ Returns the minimum rudder position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetRudderPosition(self) -> int:
        """ Returns the rudder position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetUMax(self) -> int:
        """ Returns the maximum U position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetUMin(self) -> int:
        """ Returns the minimum U position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetUPosition(self) -> int:
        """ Gets the position of the fifth axis of the joystick, if it exists.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetVMax(self) -> int:
        """ Returns the maximum V position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetVMin(self) -> int:
        """ Returns the minimum V position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetVPosition(self) -> int:
        """ Gets the position of the sixth axis of the joystick, if it exists.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetXMax(self) -> int:
        """ Returns the maximum x position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetXMin(self) -> int:
        """ Returns the minimum x position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetYMax(self) -> int:
        """ Returns the maximum y position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetYMin(self) -> int:
        """ Returns the minimum y position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetZMax(self) -> int:
        """ Returns the maximum z position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetZMin(self) -> int:
        """ Returns the minimum z position.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetZPosition(self) -> int:
        """ Returns the z position of the joystick.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasPOV(self) -> bool:
        """ Returns True if the joystick has a point of view control.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasPOV4Dir(self) -> bool:
        """ Returns True if the joystick point-of-view supports discrete values (centered, forward, backward, left, and right).

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasPOVCTS(self) -> bool:
        """ Returns True if the joystick point-of-view supports continuous degree bearings.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasRudder(self) -> bool:
        """ Returns True if there is a rudder attached to the computer.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasU(self) -> bool:
        """ Returns True if the joystick has a U axis.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasV(self) -> bool:
        """ Returns True if the joystick has a V axis.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasZ(self) -> bool:
        """ Returns True if the joystick has a Z axis.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def IsOk(self) -> bool:
        """ Returns True if the joystick is functioning.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def ReleaseCapture(self) -> bool:
        """ Releases the capture set by SetCapture.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def SetCapture(self, win, pollingFreq=0) -> bool:
        """ Sets the capture to direct joystick events to win.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def SetMovementThreshold(self, threshold: int) -> None:
        """ Sets the movement threshold, the number of steps outside which the joystick is deemed to have moved.

            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    ButtonState: int  # See GetButtonState
    ManufacturerId: int  # See GetManufacturerId
    MaxAxes: int  # See GetMaxAxes
    MaxButtons: int  # See GetMaxButtons
    MovementThreshold: int  # See GetMovementThreshold and SetMovementThreshold
    NumberAxes: int  # See GetNumberAxes
    NumberButtons: int  # See GetNumberButtons
    POVCTSPosition: int  # See GetPOVCTSPosition
    POVPosition: int  # See GetPOVPosition
    PollingMax: int  # See GetPollingMax
    PollingMin: int  # See GetPollingMin
    Position: 'Point'  # See GetPosition
    ProductId: int  # See GetProductId
    ProductName: str  # See GetProductName
    RudderMax: int  # See GetRudderMax
    RudderMin: int  # See GetRudderMin
    RudderPosition: int  # See GetRudderPosition
    UMax: int  # See GetUMax
    UMin: int  # See GetUMin
    UPosition: int  # See GetUPosition
    VMax: int  # See GetVMax
    VMin: int  # See GetVMin
    VPosition: int  # See GetVPosition
    XMax: int  # See GetXMax
    XMin: int  # See GetXMin
    YMax: int  # See GetYMax
    YMin: int  # See GetYMin
    ZMax: int  # See GetZMax
    ZMin: int  # See GetZMin
    ZPosition: int  # See GetZPosition



JOYSTICK1: int

JOYSTICK2: int

class WizardEvent(NotifyEvent):
    """ WizardEvent class represents an event generated by the Wizard:
this event is first sent to the page itself and, if not processed
there, goes up the window hierarchy as usual.

        Source: https://docs.wxpython.org/wx.adv.WizardEvent.html
    """
    def __init__(self, type=wxEVT_NULL, id=ID_ANY, direction=True, page=0) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.adv.WizardEvent.html
        """

    def GetDirection(self) -> bool:
        """ Return the direction in which the page is changing: for  EVT_WIZARD_PAGE_CHANGING , return True if weâre going forward or False otherwise and for   EVT_WIZARD_PAGE_CHANGED   return True if we came from the previous page and False if we returned from the next one.

            Source: https://docs.wxpython.org/wx.adv.WizardEvent.html
        """

    def GetPage(self) -> 'adv.WizardPage':
        """ Returns the   wx.adv.WizardPage  which was active when this event was generated.

            Source: https://docs.wxpython.org/wx.adv.WizardEvent.html
        """

    Direction: bool  # See GetDirection
    Page: 'adv.WizardPage'  # See GetPage



class Animation(Object):
    """ The Animation class handles the interface between the animation
control and the details of the animation image or data.

        Source: https://docs.wxpython.org/wx.adv.Animation.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    @staticmethod
    def AddHandler(handler: 'adv.AnimationDecoder') -> None:
        """ Add a new decoder to the list of animation decoders.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    @staticmethod
    def CleanUpHandlers() -> None:
        """ Clear out the animation decoder list.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    @staticmethod
    def FindHandler(animType: AnimationType) -> 'adv.AnimationDecoder':
        """ Search for an animation decoder by type.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def GetDelay(self, frame: int) -> int:
        """ Returns the delay for the i-th frame in milliseconds.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def GetFrame(self, frame: int) -> 'Image':
        """ Returns the i-th frame as a   wx.Image.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def GetFrameCount(self) -> int:
        """ Returns the number of frames for this animation.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    @staticmethod
    def GetHandlers() -> list['adv.AnimationHandler']:
        """ Returns the list of animation decoders used by the generic animation and    wx.adv.GenericAnimationCtrl.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def GetSize(self) -> 'Size':
        """ Returns the size of the animation.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    @staticmethod
    def InitStandardHandlers() -> None:
        """ Load the stock animation decoders (currently GIF and ANI) into the list of decoders.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    @staticmethod
    def InsertHandler(handler: 'adv.AnimationDecoder') -> None:
        """ Insert a new decoder to the front of the list of animation decoders.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def IsCompatibleWith(self, ci: 'ClassInfo') -> bool:
        """ Returns True if animation can be used with controls of the given type.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def IsOk(self) -> bool:
        """ Returns True if animation data is present.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def Load(self, stream, type=ANIMATION_TYPE_ANY) -> bool:
        """ Loads an animation from the given stream.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def LoadFile(self, name, type=ANIMATION_TYPE_ANY) -> bool:
        """ Loads an animation from a file.

            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    FrameCount: int  # See GetFrameCount
    Size: '_Size'  # See GetSize



ANIMATION_TYPE_ANY: int

class LayoutAlgorithm(Object):
    """ LayoutAlgorithm implements layout of subwindows in MDI or SDI
frames.

        Source: https://docs.wxpython.org/wx.adv.LayoutAlgorithm.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.adv.LayoutAlgorithm.html
        """

    def LayoutFrame(self, frame, mainWindow=None) -> bool:
        """ Lays out the children of a normal frame.

            Source: https://docs.wxpython.org/wx.adv.LayoutAlgorithm.html
        """

    def LayoutMDIFrame(self, frame, rect=None) -> bool:
        """ Lays out the children of an MDI parent frame.

            Source: https://docs.wxpython.org/wx.adv.LayoutAlgorithm.html
        """

    def LayoutWindow(self, parent, mainWindow=None) -> bool:
        """ Lays out the children of a normal frame or other window.

            Source: https://docs.wxpython.org/wx.adv.LayoutAlgorithm.html
        """



class Sound(Object):
    """ This class represents a short sound (loaded from Windows WAV file),
that can be stored in memory and played.

        Source: https://docs.wxpython.org/wx.adv.Sound.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    def Create(self, fileName: str) -> bool:
        """ Constructs a wave object from a file or resource.

            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    def CreateFromData(self, data) -> bool:
        """ Create a sound object from data in a memory buffer in WAV format.

            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    def IsOk(self) -> bool:
        """ Returns True if the object contains a successfully loaded file or resource, False otherwise.

            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    def Play(self, flags: Any=SOUND_ASYNC) -> bool:
        """ Plays the sound file.

            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    @staticmethod
    def PlaySound(filename, flags=SOUND_ASYNC) -> bool:
        """ Plays the sound file.

            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    @staticmethod
    def Stop() -> None:
        """ If a sound is played, this function stops it.

            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    def __bool__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    def __nonzero__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """



SOUND_SYNC: int

SOUND_ASYNC: int

class WizardPage(Panel):
    """ WizardPage is one of the screens in Wizard: it must know what are
the following and preceding pages (which may be None for the
first/last page).

        Source: https://docs.wxpython.org/wx.adv.WizardPage.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.WizardPage.html
        """

    def Create(*args, **kwargs) -> bool:
        """ Creates the wizard page.

            Source: https://docs.wxpython.org/wx.adv.WizardPage.html
        """

    def GetBitmap(self) -> 'Bitmap':
        """ This method is called by   wx.adv.Wizard  to get the bitmap to display alongside the page.

            Source: https://docs.wxpython.org/wx.adv.WizardPage.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.WizardPage.html
        """

    def GetNext(self) -> 'adv.WizardPage':
        """ Get the page which should be shown when the user chooses the  "Next"   button: if None is returned, this button will be disabled.

            Source: https://docs.wxpython.org/wx.adv.WizardPage.html
        """

    def GetPrev(self) -> 'adv.WizardPage':
        """ Get the page which should be shown when the user chooses the  "Back"   button: if None is returned, this button will be disabled.

            Source: https://docs.wxpython.org/wx.adv.WizardPage.html
        """

    Bitmap: '_Bitmap'  # See GetBitmap
    Next: 'adv.WizardPage'  # See GetNext
    Prev: 'adv.WizardPage'  # See GetPrev



OwnerDrawnComboBoxPaintingFlags: TypeAlias = int  # Enumeration

ODCB_PAINTING_CONTROL: int

ODCB_PAINTING_SELECTED: int

class CalendarEvent(DateEvent):
    """ The CalendarEvent class is used together with CalendarCtrl.

        Source: https://docs.wxpython.org/wx.adv.CalendarEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.CalendarEvent.html
        """

    def GetWeekDay(self) -> 'WeekDay':
        """ Returns the week day on which the user clicked in  EVT_CALENDAR_WEEKDAY_CLICKED   handler.

            Source: https://docs.wxpython.org/wx.adv.CalendarEvent.html
        """

    def SetWeekDay(self, day: DateTime.WeekDay) -> None:
        """ Sets the week day carried by the event, normally only used by the library internally.

            Source: https://docs.wxpython.org/wx.adv.CalendarEvent.html
        """

    WeekDay: 'WeekDay'  # See GetWeekDay and SetWeekDay



SashEdgePosition: TypeAlias = int  # Enumeration

SASH_NONE: int

SashDragStatus: TypeAlias = int  # Enumeration

class SashLayoutWindow(SashWindow):
    """ SashLayoutWindow responds to OnCalculateLayout events generated by
LayoutAlgorithm.

        Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=CLIP_CHILDREN|SW_3D, name="layoutWindow") -> bool:
        """ Initializes a sash layout window, which can be a child of a frame, dialog or any other non-control window.

            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def GetAlignment(self) -> int:
        """ Returns the alignment of the window: one of wx.adv.LAYOUT_TOP, wx.adv.LAYOUT_LEFT, wx.adv.LAYOUT_RIGHT, wx.adv.LAYOUT_BOTTOM.

            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def GetOrientation(self) -> 'adv.LayoutOrientation':
        """ Returns the orientation of the window: one of wx.adv.LAYOUT_HORIZONTAL, wx.adv.LAYOUT_VERTICAL.

            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def OnCalculateLayout(self, event: 'adv.CalculateLayoutEvent') -> None:
        """ The default handler for the event that is generated by   wx.adv.LayoutAlgorithm.

            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def OnQueryLayoutInfo(self, event: 'adv.QueryLayoutInfoEvent') -> None:
        """ The default handler for the event that is generated by OnCalculateLayout to get size, alignment and orientation information for the window.

            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def SetAlignment(self, alignment: int) -> None:
        """ Sets the alignment of the window (which edge of the available parent client area the window is attached to).

            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def SetDefaultSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the default dimensions of the window.

            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def SetOrientation(self, orientation: LayoutOrientation) -> None:
        """ Sets the orientation of the window (the direction the window will stretch in, to fill the available parent client area).

            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    Alignment: int  # See GetAlignment and SetAlignment
    Orientation: 'adv.LayoutOrientation'  # See GetOrientation and SetOrientation



class GenericAnimationCtrl(AnimationCtrl):
    """ Generic implementation of AnimationCtrl interface.

        Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
    """
    def __init__(self, parent, id=ID_ANY, anim=NullAnimation, pos=DefaultPosition, size=DefaultSize, style=AC_DEFAULT_STYLE, name=AnimationCtrlNameStr) -> None:
        """ Initializes the object and calls Create   with all the parameters.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def Create(self, parent, id=ID_ANY, anim=NullAnimation, pos=DefaultPosition, size=DefaultSize, style=AC_DEFAULT_STYLE, name=AnimationCtrlNameStr) -> bool:
        """ Creates the control with the given anim  animation.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def CreateAnimation(self) -> 'adv.Animation':
        """ Create a new animation object compatible with this control.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    @staticmethod
    def CreateCompatibleAnimation() -> 'adv.Animation':
        """ Create a new animation object compatible with this control.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def DrawCurrentFrame(self, dc: 'DC') -> None:
        """ Draw the current frame of the animation into given DC.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def GetAnimation(self) -> 'adv.Animation':
        """ Returns the animation associated with this control.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def GetBackingStore(self) -> 'Bitmap':
        """ Returns a   wx.Bitmap  with the current frame drawn in it.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def GetInactiveBitmap(self) -> 'Bitmap':
        """ Returns the inactive bitmap shown in this control when the; see SetInactiveBitmap   for more info.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def IsPlaying(self) -> bool:
        """ Returns True if the animation is being played.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def IsUsingWindowBackgroundColour(self) -> bool:
        """ Returns  true   if the windowâs background colour is being used.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def Load(self, file, animType=ANIMATION_TYPE_ANY) -> bool:
        """ Loads the animation from the given stream and calls SetAnimation .

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def LoadFile(self, file, animType=ANIMATION_TYPE_ANY) -> bool:
        """ Loads the animation from the given file and calls SetAnimation .

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def Play(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def SetAnimation(self, anim: 'adv.Animation') -> None:
        """ Sets the animation to play in this control.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def SetInactiveBitmap(self, bmp: 'BitmapBundle') -> None:
        """ Sets the bitmap to show on the control when itâs not playing an animation.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def SetUseWindowBackgroundColour(self, useWinBackground: bool=True) -> None:
        """ Specify whether the animationâs background colour is to be shown (the default), or whether the window background should show through.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def Stop(self) -> None:
        """ Stops playing the animation.

            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    Animation: 'adv.Animation'  # See GetAnimation and SetAnimation
    BackingStore: 'Bitmap'  # See GetBackingStore
    InactiveBitmap: 'Bitmap'  # See GetInactiveBitmap and SetInactiveBitmap



AnimationType: TypeAlias = int  # Enumeration

ANIMATION_TYPE_INVALID: int

ANIMATION_TYPE_GIF: int

ANIMATION_TYPE_ANI: int

class CalendarDateAttr:
    """ CalendarDateAttr is a custom attributes for a calendar date.

        Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ Returns the background colour set for the calendar date.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def GetBorder(self) -> 'adv.CalendarDateBorder':
        """ Returns the border set for the calendar date.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def GetBorderColour(self) -> 'Colour':
        """ Returns the border colour set for the calendar date.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def GetFont(self) -> 'Font':
        """ Returns the font set for the calendar date.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    @staticmethod
    def GetMark() -> 'adv.CalendarDateAttr':
        """ Used (internally) by the generic wx.adv.CalendarCtrl.Mark .

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def GetTextColour(self) -> 'Colour':
        """ Returns the text colour set for the calendar date.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def HasBackgroundColour(self) -> bool:
        """ Returns True if a non-default text background colour is set.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def HasBorder(self) -> bool:
        """ Returns True if a non-default (i.e. any) border is set.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def HasBorderColour(self) -> bool:
        """ Returns True if a non-default border colour is set.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def HasFont(self) -> bool:
        """ Returns True if a non-default font is set.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def HasTextColour(self) -> bool:
        """ Returns True if a non-default text foreground colour is set.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def IsHoliday(self) -> bool:
        """ Returns True if this calendar day is displayed as a holiday.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def SetBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ Sets the text background colour to use.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def SetBorder(self, border: CalendarDateBorder) -> None:
        """ Sets the border to use.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def SetBorderColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets the border colour to use.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the font to use.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def SetHoliday(self, holiday: bool) -> None:
        """ If holiday  is True, this calendar day will be displayed as a holiday.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    @staticmethod
    def SetMark(m: 'adv.CalendarDateAttr') -> None:
        """ Set the attributes that will be used to Mark() days on the generic   wx.adv.CalendarCtrl.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def SetTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ Sets the text (foreground) colour to use.

            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    BackgroundColour: 'Colour'  # See GetBackgroundColour and SetBackgroundColour
    Border: 'adv.CalendarDateBorder'  # See GetBorder and SetBorder
    BorderColour: 'Colour'  # See GetBorderColour and SetBorderColour
    Font: '_Font'  # See GetFont and SetFont
    TextColour: 'Colour'  # See GetTextColour and SetTextColour



CalendarHitTestResult: TypeAlias = int  # Enumeration

CAL_HITTEST_NOWHERE: int

CAL_HITTEST_HEADER: int

CAL_HITTEST_DAY: int

CAL_HITTEST_INCMONTH: int

CAL_HITTEST_DECMONTH: int

CAL_HITTEST_SURROUNDING_WEEK: int

CAL_HITTEST_WEEK: int

PropertySheetDialogFlags: TypeAlias = int  # Enumeration

PROPSHEET_DEFAULT: int

PROPSHEET_NOTEBOOK: int

PROPSHEET_TOOLBOOK: int

PROPSHEET_CHOICEBOOK: int

PROPSHEET_LISTBOOK: int

PROPSHEET_BUTTONTOOLBOOK: int

PROPSHEET_TREEBOOK: int

PROPSHEET_SHRINKTOFIT: int

LayoutAlignment: TypeAlias = int  # Enumeration

LAYOUT_NONE: int

LayoutOrientation: TypeAlias = int  # Enumeration

TaskBarIconType: TypeAlias = int  # Enumeration

TBI_DOCK: int

TBI_CUSTOM_STATUSITEM: int

TBI_DEFAULT_TYPE: int

class AnimationDecoder(ObjectRefData):
    """ AnimationDecoder is used by Animation for loading frames and other
information for the animation from the animation image file.

        Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def CanRead(self, stream: 'InputStream') -> bool:
        """ Returns True if this decoder supports loading from the given stream.

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def Clone(self) -> 'adv.AnimationDecoder':
        """ Create a copy of this decoder.

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def ConvertToImage(self, frame, image) -> bool:
        """ Convert given frame to    wx.Image.

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Checks the signature of the data in the given stream and returns True if it appears to be a valid animation format recognized by the animation decoder; this function should modify the stream current position without taking care of restoring it since  CanRead   will do it.

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetAnimationSize(self) -> 'Size':
        """ Size

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ Colour

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetDelay(self, frame: int) -> int:
        """ Return the number of milliseconds this frame should be displayed.

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetDisposalMethod(self, frame: int) -> 'adv.AnimationDisposal':
        """ What should be done after displaying this frame.

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetFrameCount(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetFramePosition(self, frame: int) -> 'Point':
        """ frame (int) â

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetFrameSize(self, frame: int) -> 'Size':
        """ frame (int) â

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetTransparentColour(self, frame: int) -> 'Colour':
        """ The transparent colour for this frame, if any, or  NullColour .

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetType(self) -> 'adv.AnimationType':
        """ Return the animation type this decoder implements.

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def Load(self, stream: 'InputStream') -> bool:
        """ Load the animation image frames from the given stream.

            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    AnimationSize: 'Size'  # See GetAnimationSize
    BackgroundColour: 'Colour'  # See GetBackgroundColour
    FrameCount: int  # See GetFrameCount
    Type: 'adv.AnimationType'  # See GetType



class WizardPageSimple(WizardPage):
    """ WizardPageSimple is the simplest possible WizardPage
implementation: it just returns the pointers given to its constructor
from WizardPage.GetNext() and WizardPage.GetPrev() functions.

        Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
        """

    def Chain(self, *args, **kw) -> 'adv.WizardPageSimple':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
        """

    def Create(*args, **kwargs) -> bool:
        """ Creates the wizard page.

            Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
        """

    def SetNext(self, next: 'adv.WizardPage') -> None:
        """ Sets the next page.

            Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
        """

    def SetPrev(self, prev: 'adv.WizardPage') -> None:
        """ Sets the previous page.

            Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
        """



CalendarDateBorder: TypeAlias = int  # Enumeration

CAL_BORDER_NONE: int

CAL_BORDER_SQUARE: int

CAL_BORDER_ROUND: int

class ANIDecoder(AnimationDecoder):
    """ An animation decoder supporting animated cursor (.ani) files.

        Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def Clone(self) -> 'adv.AnimationDecoder':
        """ Create a copy of this decoder.

            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def ConvertToImage(self, frame, image) -> bool:
        """ Convert given frame to    wx.Image.

            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Checks the signature of the data in the given stream and returns True if it appears to be a valid animation format recognized by the animation decoder; this function should modify the stream current position without taking care of restoring it since  CanRead   will do it.

            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def GetDelay(self, frame: int) -> int:
        """ Return the number of milliseconds this frame should be displayed.

            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def GetDisposalMethod(self, frame: int) -> 'adv.AnimationDisposal':
        """ What should be done after displaying this frame.

            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def GetFramePosition(self, frame: int) -> 'Point':
        """ frame (int) â

            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def GetFrameSize(self, frame: int) -> 'Size':
        """ frame (int) â

            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def GetTransparentColour(self, frame: int) -> 'Colour':
        """ The transparent colour for this frame, if any, or  NullColour .

            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def GetType(self) -> 'adv.AnimationType':
        """ Return the animation type this decoder implements.

            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def Load(self, stream: 'InputStream') -> bool:
        """ Load the animation image frames from the given stream.

            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    Type: 'adv.AnimationType'  # See GetType



class GIFDecoder(AnimationDecoder):
    """ An animation decoder supporting animated GIF files.

        Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def Clone(self) -> 'adv.AnimationDecoder':
        """ Create a copy of this decoder.

            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def ConvertToImage(self, frame, image) -> bool:
        """ Convert given frame to    wx.Image.

            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Checks the signature of the data in the given stream and returns True if it appears to be a valid animation format recognized by the animation decoder; this function should modify the stream current position without taking care of restoring it since  CanRead   will do it.

            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def GetDelay(self, frame: int) -> int:
        """ Return the number of milliseconds this frame should be displayed.

            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def GetDisposalMethod(self, frame: int) -> 'adv.AnimationDisposal':
        """ What should be done after displaying this frame.

            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def GetFramePosition(self, frame: int) -> 'Point':
        """ frame (int) â

            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def GetFrameSize(self, frame: int) -> 'Size':
        """ frame (int) â

            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def GetTransparentColour(self, frame: int) -> 'Colour':
        """ The transparent colour for this frame, if any, or  NullColour .

            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def GetType(self) -> 'adv.AnimationType':
        """ Return the animation type this decoder implements.

            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def Load(self, stream: 'InputStream') -> bool:
        """ Load the animation image frames from the given stream.

            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    Type: 'adv.AnimationType'  # See GetType



AnimationDisposal: TypeAlias = int  # Enumeration

ANIM_UNSPECIFIED: int

ANIM_DONOTREMOVE: int

ANIM_TOBACKGROUND: int

ANIM_TOPREVIOUS: int

