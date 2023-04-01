# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class PropertyGridEvent(CommandEvent):
    """ A property grid event holds information about events associated with
PropertyGrid objects.

        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def CanVeto(self) -> bool:
        """ Returns True if you can veto the action that the event is signaling.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetColumn(self) -> int:
        """ Returns the column index associated with this event.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetMainParent(self) -> 'propgrid.PGProperty':
        """ Returns highest level non-category, non-root parent of property for which event occurred.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetProperty(self) -> 'propgrid.PGProperty':
        """ Returns property associated with this event.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetPropertyName(self) -> str:
        """ Returns name of the associated property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetPropertyValue(self) -> 'propgrid.PGVariant':
        """ Returns value of the associated property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetValidationFailureBehavior(self) -> 'propgrid.byte':
        """ Returns current validation failure flags.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetValue(self) -> 'propgrid.PGVariant':
        """ Returns value of the associated property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def SetCanVeto(self, canVeto: bool) -> None:
        """ Set if event can be vetoed.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def SetProperty(self, p: 'propgrid.PGProperty') -> None:
        """ Changes the property associated with this event.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def SetValidationFailureBehavior(self, flags: 'byte') -> None:
        """ Set override validation failure behaviour.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def SetValidationFailureMessage(self, message: str) -> None:
        """ Sets custom failure message for this time only.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def Veto(self, veto: bool=True) -> None:
        """ Call this from your event handler to veto action that the event is signaling.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def WasVetoed(self) -> bool:
        """ Returns True if event was vetoed.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    Column: int  # See GetColumn
    MainParent: 'propgrid.PGProperty'  # See GetMainParent
    Property: 'propgrid.PGProperty'  # See GetProperty and SetProperty
    PropertyName: str  # See GetPropertyName
    PropertyValue: 'propgrid.PGVariant'  # See GetPropertyValue
    ValidationFailureBehavior: 'propgrid.byte'  # See GetValidationFailureBehavior and SetValidationFailureBehavior
    Value: 'propgrid.PGVariant'  # See GetValue



EVT_PG_SELECTED : int  # Respond to  wxEVT_PG_SELECTED   event, generated when a property selection has been changed, either by user action or by indirect program function. For instance, collapsing a parent property programmatically causes any selected child property to become unselected, and may therefore cause this event to be generated.

EVT_PG_CHANGED: int  # Respond to  wxEVT_PG_CHANGED   event, generated when property value has been changed by the user.

EVT_PG_CHANGING: int  # Respond to  wxEVT_PG_CHANGING   event, generated when property value is about to be changed by user. Use  wx.propgrid.PropertyGridEvent.GetValue   to take a peek at the pending value, and wx.propgrid.PropertyGridEvent.Veto   to prevent change from taking place, if necessary.

EVT_PG_HIGHLIGHTED: int  # Respond to  wxEVT_PG_HIGHLIGHTED   event, which occurs when mouse moves over a property. Eventâs property is None if hovered area does not belong to any property.

EVT_PG_RIGHT_CLICK: int  # Respond to  wxEVT_PG_RIGHT_CLICK   event, which occurs when property is clicked on with right mouse button.

EVT_PG_DOUBLE_CLICK: int  # Respond to  wxEVT_PG_DOUBLE_CLICK   event, which occurs when property is double-clicked on with left mouse button.

EVT_PG_ITEM_COLLAPSED: int  # Respond to  wxEVT_PG_ITEM_COLLAPSED   event, generated when user collapses a property or category.

EVT_PG_ITEM_EXPANDED: int  # Respond to  wxEVT_PG_ITEM_EXPANDED   event, generated when user expands a property or category.

EVT_PG_LABEL_EDIT_BEGIN: int  # Respond to  wxEVT_PG_LABEL_EDIT_BEGIN   event, generated when user is about to begin editing a property label. You can veto this event to prevent the action.

EVT_PG_LABEL_EDIT_ENDING: int  # Respond to  wxEVT_PG_LABEL_EDIT_ENDING   event, generated when user is about to end editing of a property label. You can veto this event to prevent the action.

EVT_PG_COL_BEGIN_DRAG: int  # Respond to  wxEVT_PG_COL_BEGIN_DRAG   event, generated when user starts resizing a column - can be vetoed.

EVT_PG_COL_DRAGGING: int  # Respond to  wxEVT_PG_COL_DRAGGING , event, generated when a column resize by user is in progress. This event is also generated when user double-clicks the splitter in order to recenter it.

EVT_PG_COL_END_DRAG: int  # Respond to  wxEVT_PG_COL_END_DRAG   event, generated after column resize by user has finished. ^^

class PGMultiButton(Window):
    """ This class can be used to have multiple buttons in a property editor.

        Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
    """
    def __init__(self, pg, sz) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def Add(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def AddBitmapButton(self, bitmap, id=-2) -> None:
        """ A simple wrapper around the PGMultiButton.Add method, for backwards compatibility.

            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def AddButton(self, label, id=-2) -> None:
        """ A simple wrapper around the PGMultiButton.Add method, for backwards compatibility.

            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def Finalize(self, propGrid, pos) -> None:
        """ Call this in CreateControls() of your custom editor class after all buttons have been added.

            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def GetButton(self, i: int) -> 'Window':
        """ Returns pointer to one of the buttons.

            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def GetButtonId(self, i: int) -> int:
        """ Returns Id of one of the buttons.

            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def GetCount(self) -> int:
        """ Returns number of buttons.

            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def GetPrimarySize(self) -> 'Size':
        """ Returns size of primary editor control, as appropriately reduced by number of buttons present.

            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    Count: int  # See GetCount
    PrimarySize: 'Size'  # See GetPrimarySize



class PGArrayEditorDialog(Dialog):
    """ index (int) â 

        Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def ArrayGet(self, index: int) -> str:
        """ index (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def ArrayGetCount(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def ArrayInsert(self, str, index) -> bool:
        """ str (string) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def ArrayRemoveAt(self, index: int) -> None:
        """ index (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def ArraySet(self, index, str) -> bool:
        """ index (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def ArraySwap(self, first, second) -> None:
        """ first (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def Create(self, parent, message, caption, style=AEDIALOG_STYLE, pos=DefaultPosition, sz=DefaultSize) -> bool:
        """ parent (wx.Window) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def EnableCustomNewAction(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def GetDialogValue(self) -> 'propgrid.PGVariant':
        """ Return value modified by dialog.

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def GetSelection(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def GetTextCtrlValidator(self) -> 'Validator':
        """ Override to return   wx.Validator  to be used with the   wx.TextCtrl  in dialog.

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def Init(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def IsModified(self) -> bool:
        """ Returns True if array was actually modified.

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def OnCustomNewAction(self, resString: str) -> bool:
        """ resString (string) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def SetDialogValue(self, value: PGVariant) -> None:
        """ Set value modified by dialog.

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def SetNewButtonText(self, text: str) -> None:
        """ Sets tooltip text for button allowing the user to enter new string.

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    DialogValue: 'propgrid.PGVariant'  # See GetDialogValue and SetDialogValue
    Selection: int  # See GetSelection
    TextCtrlValidator: 'Validator'  # See GetTextCtrlValidator



class PropertyGridPage(EvtHandler,PropertyGridInterface,PropertyGridPageState):
    """ Holder of property grid page information.

        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def Clear(self) -> None:
        """ Deletes all properties on page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def FitColumns(self) -> 'Size':
        """ Reduces column sizes to minimum possible that contents are still visibly (naturally some margin space will be applied as well).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def GetIndex(self) -> int:
        """ Returns page index in manager;.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def GetRoot(self) -> 'propgrid.PGProperty':
        """ Returns âroot propertyâ.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def GetSplitterPosition(self, col: int=0) -> int:
        """ Returns x-coordinate position of splitter on a page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def GetStatePtr(self) -> 'propgrid.PropertyGridPageState':
        """ Returns pointer to contained property grid state.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def GetToolId(self) -> int:
        """ Returns id of the tool bar item that represents this page on   wx.propgrid.PropertyGridManagerâs   wx.ToolBar.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def Init(self) -> None:
        """ Do any member initialization in this method.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def IsHandlingAllEvents(self) -> bool:
        """ Return False here to indicate unhandled events should be propagated to managerâs parent, as normal.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def OnShow(self) -> None:
        """ Called every time page is about to be shown.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def RefreshProperty(self, p: 'propgrid.PGProperty') -> None:
        """ Refreshes given property on page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def SetSplitterPosition(self, splitterPos, col=0) -> None:
        """ Sets splitter position on page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    Index: int  # See GetIndex
    Root: 'propgrid.PGProperty'  # See GetRoot
    SplitterPosition: int  # See GetSplitterPosition and SetSplitterPosition
    StatePtr: 'propgrid.PropertyGridPageState'  # See GetStatePtr
    ToolId: int  # See GetToolId



class ColourPropertyValue(Object):
    """ Because text, background and other colours tend to differ between
platforms, SystemColourProperty must be able to select between
system colour and, when necessary, to pick a custom one.

        Source: https://docs.wxpython.org/wx.propgrid.ColourPropertyValue.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.ColourPropertyValue.html
        """

    def Init(self, type, colour) -> None:
        """ type (wx.int) â

            Source: https://docs.wxpython.org/wx.propgrid.ColourPropertyValue.html
        """

    m_colour: Any  # A public C++ attribute of type Colour     . Resulting colour.
    m_type: Any  # A public C++ attribute of type int     . An integer value relating to the colour, and which exact meaning depends on the property with which it is used.



class PGCell(Object):
    """ Base class for PropertyGrid cell information.

        Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def GetBgCol(self) -> 'Colour':
        """ Colour

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def GetBitmap(self) -> 'BitmapBundle':
        """ BitmapBundle

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def GetData(self) -> 'propgrid.PGCellData':
        """ wx.propgrid.PGCellData

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def GetFgCol(self) -> 'Colour':
        """ Colour

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def GetFont(self) -> 'Font':
        """ Returns font of the cell.

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def GetText(self) -> str:
        """ string

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def HasText(self) -> bool:
        """ Returns True if this cell has custom text stored within.

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def MergeFrom(self, srcCell: 'propgrid.PGCell') -> None:
        """ Merges valid data from srcCell into this.

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def SetBgCol(self, col: Union[int, str, 'Colour']) -> None:
        """ col (wx.Colour) â

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def SetBitmap(self, bitmap: 'BitmapBundle') -> None:
        """ bitmap (wx.BitmapBundle) â

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def SetEmptyData(self) -> None:
        """ Sets empty but valid data to this cell object.

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def SetFgCol(self, col: Union[int, str, 'Colour']) -> None:
        """ col (wx.Colour) â

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets font of the cell.

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def SetText(self, text: str) -> None:
        """ text (string) â

            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    BgCol: 'Colour'  # See GetBgCol and SetBgCol
    Bitmap: 'BitmapBundle'  # See GetBitmap and SetBitmap
    Data: 'propgrid.PGCellData'  # See GetData
    FgCol: 'Colour'  # See GetFgCol and SetFgCol
    Font: '_Font'  # See GetFont and SetFont
    Text: str  # See GetText and SetText



class PGEditor(Object):
    """ Base class for custom PropertyGrid editors.

        Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def CanContainCustomImage(self) -> bool:
        """ Returns True if control itself can contain the custom image.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'propgrid.PGWindowList':
        """ Instantiates editor controls.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def DeleteItem(self, ctrl, index) -> None:
        """ Deletes item from existing control.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def DrawValue(self, dc, rect, property, text) -> None:
        """ Draws value for given property.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def GetName(self) -> str:
        """ Returns pointer to the name of the editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def GetValueFromControl(self, property, ctrl) -> tuple:
        """ Returns value from control, via parameter variant.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def InsertItem(self, ctrl, label, index) -> int:
        """ Inserts item to existing control.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def OnEvent(self, propgrid, property, wnd_primary, event) -> bool:
        """ Handles events.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def OnFocus(self, property, wnd) -> None:
        """ Extra processing when control gains focus.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def SetControlAppearance(self, pg, property, ctrl, appearance, oldAppearance, unspecified) -> None:
        """ Called by property grid to set new appearance for the control.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def SetControlIntValue(self, property, ctrl, value) -> None:
        """ Sets controlâs value specifically from int (applies to choice etc.).

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def SetControlStringValue(self, property, ctrl, txt) -> None:
        """ Sets controlâs value specifically from string.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def SetValueToUnspecified(self, property, ctrl) -> None:
        """ Sets value in control to unspecified.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def UpdateControl(self, property, ctrl) -> None:
        """ Loads value from property to the control.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    Name: str  # See GetName
    m_clientData: Any  # A public C++ attribute of type ````.



class PGEditorDialogAdapter(Object):
    """ Derive a class from this to adapt an existing editor dialog or
function to be used when editor button of a property is pushed.

        Source: https://docs.wxpython.org/wx.propgrid.PGEditorDialogAdapter.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGEditorDialogAdapter.html
        """

    def DoShowDialog(self, propGrid, property) -> bool:
        """ propGrid (wx.propgrid.PropertyGrid) â

            Source: https://docs.wxpython.org/wx.propgrid.PGEditorDialogAdapter.html
        """

    def GetValue(self) -> 'propgrid.PGVariant':
        """ This method is typically only used if deriving class from existing adapter with value conversion purposes.

            Source: https://docs.wxpython.org/wx.propgrid.PGEditorDialogAdapter.html
        """

    def SetValue(self, value: PGVariant) -> None:
        """ value (PGVariant) â

            Source: https://docs.wxpython.org/wx.propgrid.PGEditorDialogAdapter.html
        """

    def ShowDialog(self, propGrid, property) -> bool:
        """ propGrid (wx.propgrid.PropertyGrid) â

            Source: https://docs.wxpython.org/wx.propgrid.PGEditorDialogAdapter.html
        """

    Value: 'propgrid.PGVariant'  # See GetValue and SetValue
    m_clientData: Any  # A public C++ attribute of type ````.



class PGProperty(Object):
    """ PGProperty is base class for all PropertyGrid properties and as
such it is not intended to be instantiated directly.

        Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
    """
    def AdaptListToValue(self, list, value) -> None:
        """ Adapts list variant into proper value using consecutive ChildChanged   calls.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def AddChoice(self, label, value=PG_INVALID_VALUE) -> int:
        """ Append a new choice to propertyâs list of choices.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def AddPrivateChild(self, prop: 'propgrid.PGProperty') -> None:
        """ Adds a private child property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def AppendChild(self, childProperty: 'propgrid.PGProperty') -> 'propgrid.PGProperty':
        """ Use this member function to add independent (i.e.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def AreAllChildrenSpecified(self, pendingList: Optional[PGVariant]=None) -> bool:
        """ Determines, recursively, if all children are not unspecified.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def AreChildrenComponents(self) -> bool:
        """ Returns True if children of this property are component values (for instance, points size, face name, and is_underlined are component values of a font).

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def ChangeFlag(self, flag, set) -> None:
        """ Sets or clears given property flag.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def ChildChanged(self, thisValue, childIndex, childValue) -> 'propgrid.PGVariant':
        """ Called after value of a child property has been altered.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DeleteChildren(self) -> None:
        """ Deletes children of the property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DeleteChoice(self, index: int) -> None:
        """ Removes entry from propertyâs   wx.propgrid.PGChoices  and editor control (if it is active).

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DoGetAttribute(self, name: str) -> 'propgrid.PGVariant':
        """ Returns value of an attribute.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DoGetEditorClass(self) -> 'propgrid.PGEditor':
        """ Returns pointer to an instance of used editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DoGetValidator(self) -> 'Validator':
        """ Returns pointer to the   wx.Validator  that should be used with the editor of this property (None for no validator).

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DoGetValue(self) -> 'propgrid.PGVariant':
        """ Override this to return something else than m_value as the value.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ Reimplement this member function to add special handling for attributes of this property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ Enables or disables the property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def EnableCommonValue(self, enable: bool=True) -> None:
        """ Call to enable or disable usage of common value (integer value that can be selected for properties instead of their normal values) for this property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GenerateComposedValue(self) -> str:
        """ Composes text from values of child properties.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetAttribute(self, *args, **kw) -> 'propgrid.PGVariant':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetAttributeAsDouble(self, name, defVal) -> float:
        """ Returns named attribute, as double, if found.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetAttributeAsLong(self, name, defVal) -> int:
        """ Returns named attribute, as long, if found.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetAttributes(self) -> Any:
        """ Returns map-like storage of propertyâs attributes.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetAttributesAsList(self) -> 'propgrid.PGVariant':
        """ Returns attributes as list Variant     .

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetBaseName(self) -> str:
        """ Returns propertyâs base name (i.e.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetCell(self, column: int) -> 'propgrid.PGCell':
        """ Returns   wx.propgrid.PGCell  of given column, creating one if necessary.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetCellRenderer(self, column: int) -> 'propgrid.PGCellRenderer':
        """ Returns used   wx.propgrid.PGCellRenderer  instance for given property column (label=0, value=1).

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetChildCount(self) -> int:
        """ Returns number of child properties.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetChildrenHeight(self, lh, iMax=-1) -> int:
        """ Returns height of children, recursively, and by taking expanded/collapsed status into account.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetChoiceSelection(self) -> int:
        """ Returns which choice is currently selected.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetChoices(self) -> 'propgrid.PGChoices':
        """ Returns read-only reference to propertyâs list of choices.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetClientData(self) -> 'ClientData':
        """ Gets managed client object of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetClientObject(self, n) -> Any:
        """ Alias for GetClientData

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetColumnEditor(self, column: int) -> 'propgrid.PGEditor':
        """ Returns editor used for given column.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetCommonValue(self) -> int:
        """ Returns common value selected for this property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetDefaultValue(self) -> 'propgrid.PGVariant':
        """ Returns propertyâs default value.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetDepth(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetDisplayedCommonValueCount(self) -> int:
        """ Return number of displayed common values for this property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetDisplayedString(self) -> str:
        """ Returns propertyâs displayed text.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetEditorClass(self) -> 'propgrid.PGEditor':
        """ Returns   wx.propgrid.PGEditor  that will be used and created when property becomes selected.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetEditorDialog(self) -> 'propgrid.PGEditorDialogAdapter':
        """ Returns instance of a new   wx.propgrid.PGEditorDialogAdapter  instance, which is used when user presses the (optional) button next to the editor control;.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetFlagsAsString(self, flagsMask: FlagType) -> str:
        """ Gets flags as aâ|â delimited string.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetGrid(self) -> 'propgrid.PropertyGrid':
        """ Returns property grid where property lies.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetGridIfDisplayed(self) -> 'propgrid.PropertyGrid':
        """ Returns owner   wx.propgrid.PropertyGrid, but only if one is currently on a page displaying this property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetHelpString(self) -> str:
        """ Returns propertyâs help or description text.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetHintText(self) -> str:
        """ Returns propertyâs hint text (shown in empty value cell).

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetImageOffset(self, imageWidth: int) -> int:
        """ Converts image width into full image offset, with margins.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetIndexInParent(self) -> int:
        """ Returns position in parentâs array.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetItemAtY(self, y: int) -> 'propgrid.PGProperty':
        """ Returns property at given virtual y coordinate.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetLabel(self) -> str:
        """ Returns propertyâs label.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetLastVisibleSubItem(self) -> 'propgrid.PGProperty':
        """ Returns last visible child property, recursively.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetMainParent(self) -> 'propgrid.PGProperty':
        """ Returns highest level non-category, non-root parent.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetMaxLength(self) -> int:
        """ Returns maximum allowed length of the text the user can enter in the property text editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetName(self) -> str:
        """ Returns propertyâs name with all (non-category, non-root) parents.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetOrCreateCell(self, column: int) -> 'propgrid.PGCell':
        """ Returns   wx.propgrid.PGCell  of given column, creating one if necessary.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetParent(self) -> 'propgrid.PGProperty':
        """ Return parent of property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetPropertyByName(self, name: str) -> 'propgrid.PGProperty':
        """ Returns (direct) child property with given name (or None if not found).

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetValidator(self) -> 'Validator':
        """ Gets assignable version of propertyâs validator.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetValue(self) -> 'propgrid.PGVariant':
        """ Returns propertyâs value.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetValueAsString(self, argFlags: int=0) -> str:
        """ Returns text representation of propertyâs value.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetValueImage(self) -> 'Bitmap':
        """ Returns bitmap that appears next to value text.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetValueType(self) -> str:
        """ Returns value type used by this property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetY(self) -> int:
        """ Returns coordinate to the top y of the property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def HasFlag(self, flag: PGPropertyFlags) -> bool:
        """ Returns True if property has given flag set.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def HasFlagsExact(self, flags: FlagType) -> bool:
        """ Returns True if property has all given flags set.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def HasVisibleChildren(self) -> bool:
        """ Returns True if property has even one visible child.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def Hide(self, hide, flags=PG_RECURSE) -> bool:
        """ Hides or reveals the property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def Index(self, p: 'propgrid.PGProperty') -> int:
        """ Returns index of given child property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def InsertChild(self, index, childProperty) -> 'propgrid.PGProperty':
        """ Use this member function to add independent (i.e.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def InsertChoice(self, label, index, value=PG_INVALID_VALUE) -> int:
        """ Inserts a new choice to propertyâs list of choices.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IntToValue(self, number, argFlags=0) -> tuple:
        """ Converts integer (possibly a choice selection) into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsCategory(self) -> bool:
        """ Returns True if this property is actually a   wx.propgrid.PropertyCategory.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsEnabled(self) -> bool:
        """ Returns True if property is enabled.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsExpanded(self) -> bool:
        """ Returns True if property has visible children.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsRoot(self) -> bool:
        """ Returns True if this property is actually a RootProperty.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsSomeParent(self, candidateParent: 'propgrid.PGProperty') -> bool:
        """ Returns True if candidateParent is some parent of this property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsSubProperty(self) -> bool:
        """ Returns True if this is a sub-property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsTextEditable(self) -> bool:
        """ Returns True if property has editable   wx.TextCtrl  when selected.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsValueUnspecified(self) -> bool:
        """ Returns True if propertyâs value is considered unspecified.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsVisible(self) -> bool:
        """ Returns True if all parents expanded.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def Item(self, i: int) -> 'propgrid.PGProperty':
        """ Returns child property at index i.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def Last(self) -> 'propgrid.PGProperty':
        """ Returns last sub-property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def OnCustomPaint(self, dc, rect, paintdata) -> None:
        """ Override to paint an image in front of the property value text or drop-down list item (but only if wx.propgrid.PGProperty.OnMeasureImage   is overridden as well).

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def OnEvent(self, propgrid, wnd_primary, event) -> None:
        """ Events received by editor widgets are processed here.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def OnMeasureImage(self, item: int=-1) -> 'Size':
        """ Returns size of the custom painted image in front of property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def OnSetValue(self) -> None:
        """ This virtual function is called after m_value has been set.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def OnValidationFailure(self, pendingValue: PGVariant) -> None:
        """ Called whenever validation has failed with given pending value.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def RecreateEditor(self) -> bool:
        """ If propertyâs editor is created this forces its recreation.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def RefreshChildren(self) -> None:
        """ Refresh values of child properties.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def RefreshEditor(self) -> None:
        """ If propertyâs editor is active, then update itâs value.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetAttribute(self, name, value) -> None:
        """ Sets an attribute for this property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetAttributes(self, attributes) -> None:
        """ Set the propertyâs attributes from a Python dictionary.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetAutoUnspecified(self, enable: bool=True) -> None:
        """ Set if user can change the propertyâs value to unspecified by modifying the value of the editor control (usually by clearing it).

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetBackgroundColour(self, colour, flags=PG_RECURSE) -> None:
        """ Sets propertyâs background colour.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetCell(self, column, cell) -> None:
        """ Sets cell information for given column.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetChoiceSelection(self, newValue: int) -> None:
        """ Sets selected choice and changes property value.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetChoices(self, choices: 'propgrid.PGChoices') -> bool:
        """ Sets new set of choices for the property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetClientData(self, data: ClientData) -> None:
        """ Sets client object of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetClientObject(self, n, data) -> Any:
        """ Alias for SetClientData

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetCommonValue(self, commonValue: int) -> None:
        """ Sets common value selected for this property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetDefaultColours(self, flags: int=PG_RECURSE) -> None:
        """ Sets propertyâs default text and background colours.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetDefaultValue(self, value: PGVariant) -> None:
        """ Set default value of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetEditor(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetExpanded(self, expanded: bool) -> None:
        """ expanded (bool) â

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetFlagRecursively(self, flag, set) -> None:
        """ Sets or clears given property flag, recursively.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetFlagsFromString(self, str: str) -> None:
        """ Sets flags from a â|â delimited string.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetHelpString(self, helpString: str) -> None:
        """ Sets propertyâs help string, which is shown, for example, in   wx.propgrid.PropertyGridManagerâs description text box.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetLabel(self, label: str) -> None:
        """ Sets propertyâs label.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetMaxLength(self, maxLen: int) -> bool:
        """ Set maximum length of the text the user can enter in the text editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetModifiedStatus(self, modified: bool) -> None:
        """ Sets propertyâs âis it modified?â flag.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetName(self, newName: str) -> None:
        """ Sets new (base) name for property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetParentalType(self, flag: int) -> None:
        """ Changes what sort of parent this property is for its children.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetTextColour(self, colour, flags=PG_RECURSE) -> None:
        """ Sets propertyâs text colour.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValidator(self, validator: 'Validator') -> None:
        """ Sets   wx.Validator  for a property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValue(self, value, pList=None, flags=PG_SETVAL_REFRESH_EDITOR) -> None:
        """ Call this to set value of the property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValueFromInt(self, value, flags=0) -> bool:
        """ Converts integer to a value, and if successful, calls SetValue   on it.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValueFromString(self, text, flags=PG_PROGRAMMATIC_VALUE) -> bool:
        """ Converts string to a value, and if successful, calls SetValue   on it.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValueImage(self, bmp: 'BitmapBundle') -> None:
        """ Set   wx.Bitmap  taken from   wx.BitmapBundle  in front of the value.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValueInEvent(self, value: PGVariant) -> None:
        """ Call this function in OnEvent , OnButtonClick() etc.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValueToUnspecified(self) -> None:
        """ Sets propertyâs value to unspecified (i.e.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetWasModified(self, set: bool=True) -> None:
        """ Call with False in OnSetValue   to cancel value changes after all (i.e.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def UpdateParentValues(self) -> 'propgrid.PGProperty':
        """ Updates composed values of parent non-category properties, recursively.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def UsesAutoUnspecified(self) -> bool:
        """ Returns True if containing grid uses PG_EX_AUTO_UNSPECIFIED_VALUES.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def ValidateValue(self, value, validationInfo) -> bool:
        """ Implement this function in derived class to check the value.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    m_clientData: Any  # A public C++ attribute of type ````. This member is public so scripting language bindings wrapper code can access it freely.
    m_value: Any  # See GetValue and SetValue



NOT_FOUND: int

class PropertyGridManager(Panel,PropertyGridInterface):
    """ PropertyGridManager is an efficient multi-page version of
PropertyGrid, which can optionally have toolbar for mode and page
selection, a help text box, and a header.

        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def AddPage(*args, **kwargs) -> 'propgrid.PropertyGridPage':
        """ Creates new property page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def Clear(self) -> None:
        """ Deletes all properties and all pages.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def ClearPage(self, page: int) -> None:
        """ Deletes all properties on given page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def CommitChangesFromEditor(self, flags: 'int'=0) -> bool:
        """ Forces updating the value of property from the editor control.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=PGMAN_DEFAULT_STYLE, name=PropertyGridManagerNameStr) -> bool:
        """ Two step creation.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def CreatePropertyGrid(self) -> 'propgrid.PropertyGrid':
        """ Creates property grid for the manager.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def EnableCategories(self, enable: bool) -> bool:
        """ Enables or disables (shows/hides) categories according to parameter enable.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def EnsureVisible(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Selects page, scrolls and/or expands items to ensure that the given item is visible.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetColumnCount(self, page: int=-1) -> int:
        """ Returns number of columns on given page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetCurrentPage(self) -> 'propgrid.PropertyGridPage':
        """ Returns currently selected page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetDescBoxHeight(self) -> int:
        """ Returns height of the description text box.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetGrid(self) -> 'propgrid.PropertyGrid':
        """ Returns pointer to the contained   wx.propgrid.PropertyGrid.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetPage(self, *args, **kw) -> 'propgrid.PropertyGridPage':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetPageByName(self, name: str) -> int:
        """ Returns index for a page name.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetPageByState(self, pstate: 'propgrid.PropertyGridPageState') -> int:
        """ Returns index for a relevant propertygrid state.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetPageCount(self) -> int:
        """ Returns number of managed pages.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetPageName(self, index: int) -> str:
        """ Returns name of given page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetPageRoot(self, index: int) -> 'propgrid.PGProperty':
        """ Returns âroot propertyâ of the given page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetSelectedPage(self) -> int:
        """ Returns index to currently selected page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetSelectedProperty(self) -> 'propgrid.PGProperty':
        """ Alias for GetSelection .

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetSelection(self) -> 'propgrid.PGProperty':
        """ Shortcut for GetGrid . GetSelection .

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetToolBar(self) -> 'ToolBar':
        """ Returns a pointer to the toolbar currently associated with the   wx.propgrid.PropertyGridManager  (if any).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetVIterator(self, flags: int) -> 'propgrid.PGVIterator':
        """ Similar to GetIterator , but instead returns   wx.propgrid.PGVIterator  instance, which can be useful for forward-iterating through arbitrary property containers.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def InsertPage(*args, **kwargs) -> 'propgrid.PropertyGridPage':
        """ Creates new property page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def IsAnyModified(self) -> bool:
        """ Returns True if any property on any page has been modified by the user.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def IsPageModified(self, index: int) -> bool:
        """ Returns True if any property on given page has been modified by the user.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def IsPropertySelected(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Returns True if property is selected.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def RemovePage(self, page: int) -> bool:
        """ Removes a page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SelectPage(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SelectProperty(self, id, focus=False) -> bool:
        """ Select a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetColumnCount(self, colCount, page=-1) -> None:
        """ Sets number of columns on given page (default is current page).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetColumnTitle(self, idx, title) -> None:
        """ Sets a column title.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetDescBoxHeight(self, ht, refresh=True) -> None:
        """ Sets y coordinate of the description box splitter.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetDescription(self, label, content) -> None:
        """ Sets label and text in description box.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetPageSplitterLeft(self, page, subProps=False) -> None:
        """ Moves splitter as left as possible on an individual page, while still allowing all labels to be shown in full.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetPageSplitterPosition(self, page, pos, column=0) -> None:
        """ Sets splitter position on individual page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetSplitterLeft(self, subProps=False, allPages=True) -> None:
        """ Moves splitter as left as possible, while still allowing all labels to be shown in full.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetSplitterPosition(self, pos, column=0) -> None:
        """ Sets splitter position for all pages.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def ShowHeader(self, show: bool=True) -> None:
        """ Show or hide the property grid header control.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    ColumnCount: int  # See GetColumnCount and SetColumnCount
    CurrentPage: 'propgrid.PropertyGridPage'  # See GetCurrentPage
    DescBoxHeight: int  # See GetDescBoxHeight and SetDescBoxHeight
    Grid: 'propgrid.PropertyGrid'  # See GetGrid
    PageCount: int  # See GetPageCount
    SelectedPage: int  # See GetSelectedPage
    SelectedProperty: 'propgrid.PGProperty'  # See GetSelectedProperty
    Selection: 'propgrid.PGProperty'  # See GetSelection
    ToolBar: '_ToolBar'  # See GetToolBar



class PropertyGrid(Scrolled,PropertyGridInterface):
    """ PropertyGrid is a specialized grid for editing properties - in other
words name = value pairs.

        Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def AddActionTrigger(self, action, keycode, modifiers=0) -> None:
        """ Adds given key combination to trigger given action.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def AddToSelection(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Adds given property into selection.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def AdjustScrollbars(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    @staticmethod
    def AutoGetTranslation(enable: bool) -> None:
        """ This static function enables or disables automatic use of wx.GetTranslation       for following strings:   wx.propgrid.EnumProperty  list labels,   wx.propgrid.FlagsProperty  child property labels.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def BeginLabelEdit(self, colIndex: int=0) -> None:
        """ Creates label editor   wx.TextCtrl  for given column, for property that is currently selected.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def CalcScrolledPosition(self, *args, **kw) -> 'Point':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def CalcUnscrolledPosition(self, *args, **kw) -> 'Point':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def CenterSplitter(self, enableAutoResizing: bool=False) -> None:
        """ Centers the splitter.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ChangePropertyValue(self, id, newValue) -> bool:
        """ Changes value of a property, as if from an editor.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def Clear(self) -> None:
        """ Deletes all properties.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ClearActionTriggers(self, action: int) -> None:
        """ Clears action triggers for given action.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def CommitChangesFromEditor(self, flags: 'int'=0) -> bool:
        """ Forces updating the value of property from the editor control.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=PG_DEFAULT_STYLE, name=PropertyGridNameStr) -> bool:
        """ Two step creation.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DedicateKey(self, keycode: int) -> None:
        """ Dedicates a specific keycode to   wx.propgrid.PropertyGrid.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DisableKeyboardScrolling(self) -> None:
        """ Disable use of keyboard keys for scrolling.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DoHidePropertyError(self, property: 'propgrid.PGProperty') -> None:
        """ Override in derived class to hide an error displayed by DoShowPropertyError .

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DoOnValidationFailure(self, property, invalidValue) -> bool:
        """ Override to customize property validation failure behaviour.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DoOnValidationFailureReset(self, property: 'propgrid.PGProperty') -> None:
        """ Override to customize resetting of property validation failure status.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DoPrepareDC(self, dc: 'DC') -> None:
        """ Call this function to prepare the device context for drawing a scrolled image.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    @staticmethod
    def DoRegisterEditorClass(editor, name, noDefCheck=False) -> 'propgrid.PGEditor':
        """ Registers a new editor class.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DoShowPropertyError(self, property, msg) -> None:
        """ Override in derived class to display error messages in custom manner (these message usually only result from validation failure).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DrawItemAndValueRelated(self, p: 'propgrid.PGProperty') -> None:
        """ Draws item, children, and consecutive parents as long as category is not met.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def EditorsValueWasModified(self) -> None:
        """ Call when editor widgetâs contents is modified.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def EditorsValueWasNotModified(self) -> None:
        """ Reverse of EditorsValueWasModified .

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def EnableCategories(self, enable: bool) -> bool:
        """ Enables or disables (shows/hides) categories according to parameter enable.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def EnableScrolling(self, xScrolling, yScrolling) -> None:
        """ Enable or disable use of wx.Window.ScrollWindow   for scrolling.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def EndLabelEdit(self, commit: bool=True) -> None:
        """ Destroys label editor   wx.TextCtrl, if any.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def EnsureVisible(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Scrolls and/or expands items to ensure that the given item is visible.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def FitColumns(self) -> 'Size':
        """ Reduces column sizes to minimum possible, while still retaining fully visible grid contents (labels, images).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetCaptionBackgroundColour(self) -> 'Colour':
        """ Returns current category caption background colour.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetCaptionFont(self) -> 'Font':
        """ Returns current category caption font.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetCaptionForegroundColour(self) -> 'Colour':
        """ Returns current category caption text colour.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetCellBackgroundColour(self) -> 'Colour':
        """ Returns current cell background colour.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetCellDisabledTextColour(self) -> 'Colour':
        """ Returns current cell text colour when disabled.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetCellTextColour(self) -> 'Colour':
        """ Returns current cell text colour.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetColumnCount(self) -> int:
        """ Returns number of columns currently on grid.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetEditorTextCtrl(self) -> 'TextCtrl':
        """ Returns   wx.TextCtrl  active in currently selected property, if any.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetEmptySpaceColour(self) -> 'Colour':
        """ Returns colour of empty space below properties.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetFontHeight(self) -> int:
        """ Returns height of highest characters of used font.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetGrid(self) -> 'propgrid.PropertyGrid':
        """ Returns pointer to itself.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetImageRect(self, property, item) -> 'Rect':
        """ Returns rectangle of custom paint image.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetImageSize(self, property=None, item=-1) -> 'Size':
        """ Returns size of the custom paint image in front of property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetLabelEditor(self) -> 'TextCtrl':
        """ Returns currently active label editor, None if none.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetLastItem(self, flags: int=PG_ITERATE_DEFAULT) -> 'propgrid.PGProperty':
        """ Returns last item which could be iterated using given flags.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetLineColour(self) -> 'Colour':
        """ Returns colour of lines between cells.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetMarginColour(self) -> 'Colour':
        """ Returns background colour of margin.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetMarginWidth(self) -> int:
        """ Returns margin width.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetPanel(self) -> 'Window':
        """ Returns   wx.Window  that the properties are painted on, and which should be used as the parent for editor controls.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetRoot(self) -> 'propgrid.PGProperty':
        """ Returns âroot propertyâ.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetRowHeight(self) -> int:
        """ Returns height of a single grid row (in pixels).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetScaleX(self) -> float:
        """ float

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetScaleY(self) -> float:
        """ float

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetScrollLines(self, orient: int) -> int:
        """ orient (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetScrollPageSize(self, orient: int) -> int:
        """ orient (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetScrollPixelsPerUnit(self) -> tuple:
        """ Get the number of pixels per scroll unit (line), in each direction, as set by SetScrollbars .

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetSelectedProperty(self) -> 'propgrid.PGProperty':
        """ Returns currently selected property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetSelection(self) -> 'propgrid.PGProperty':
        """ Returns currently selected property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetSelectionBackgroundColour(self) -> 'Colour':
        """ Returns current selection background colour.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetSelectionForegroundColour(self) -> 'Colour':
        """ Returns current selection text colour.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetSizeAvailableForScrollTarget(self, size: Union[tuple[int, int], 'Size']) -> 'Size':
        """ Function which must be overridden to implement the size available for the scroll target for the given size of the main window.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetSplitterPosition(self, splitterIndex: int=0) -> int:
        """ Returns current splitter x position.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetStatusBar(self) -> 'StatusBar':
        """ Return   wx.StatusBar  that is used by this   wx.propgrid.PropertyGrid.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetTargetRect(self) -> 'Rect':
        """ wx.Rect

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetTargetWindow(self) -> 'Window':
        """ wx.Window

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetUncommittedPropertyValue(self) -> 'propgrid.PGVariant':
        """ Returns most up-to-date value of selected property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetUnspecifiedValueAppearance(self) -> 'propgrid.PGCell':
        """ Returns current appearance of unspecified value cells.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetUnspecifiedValueText(self, argFlags: int=0) -> str:
        """ Returns (visual) text representation of the unspecified property value.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetVerticalSpacing(self) -> int:
        """ Returns current vertical spacing.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetViewStart(self) -> tuple:
        """ Get the position at which the visible portion of the window starts.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def HitTest(self, pt: Union[tuple[int, int], 'Point']) -> 'propgrid.PropertyGridHitTestResult':
        """ Returns information about arbitrary position in the grid.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def IsAnyModified(self) -> bool:
        """ Returns True if any property has been modified by the user.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def IsAutoScrolling(self) -> bool:
        """ Are we generating the autoscroll events?

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def IsEditorFocused(self) -> bool:
        """ Returns True if a property editor control has focus.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def IsEditorsValueModified(self) -> bool:
        """ Returns True if editorâs value was marked modified.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def IsFrozen(self) -> bool:
        """ Returns True if updating is frozen (i.e.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def IsRetained(self) -> bool:
        """ Motif only: True if the window has a backing bitmap.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def MakeColumnEditable(self, column, editable=True) -> None:
        """ Makes given column editable by user.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def OnDraw(self, dc: 'DC') -> None:
        """ Called by the default paint event handler to allow the application to define painting behaviour without having to worry about calling DoPrepareDC .

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def OnTLPChanging(self, newTLP: 'Window') -> None:
        """ It is recommended that you call this function any time your code causes   wx.propgrid.PropertyGridâs top-level parent to change.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def PrepareDC(self, dc: 'DC') -> None:
        """ This function is for backwards compatibility only and simply calls DoPrepareDC   now.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def RefreshEditor(self) -> None:
        """ Refreshes any active editor control.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def RefreshProperty(self, p: 'propgrid.PGProperty') -> None:
        """ Redraws given property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    @staticmethod
    def RegisterEditorClass(editor, noDefCheck=False) -> 'propgrid.PGEditor':
        """ Forwards to DoRegisterEditorClass with empty name.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def RemoveFromSelection(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Removes given property from selection.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ResetColours(self) -> None:
        """ Resets all colours to the original system values.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ResetColumnSizes(self, enableAutoResizing: bool=False) -> None:
        """ Resets column sizes and splitter positions, based on proportions.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def Scroll(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SelectProperty(self, id, focus=False) -> bool:
        """ Selects a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SendAutoScrollEvents(self, event: 'ScrollWinEvent') -> bool:
        """ This method can be overridden in a derived class to forbid sending the auto scroll events - note that unlike StopAutoScrolling   it doesnât stop the timer, so it will be called repeatedly and will typically return different values depending on the current mouse position.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetCaptionBackgroundColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets category caption background colour.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetCaptionTextColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets category caption text colour.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetCellBackgroundColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets default cell background colour - applies to property cells.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetCellDisabledTextColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets cell text colour for disabled properties.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetCellTextColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets default cell text colour - applies to property name and value text.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetColumnCount(self, colCount: int) -> None:
        """ Set number of columns (2 or more).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetCurrentCategory(self, id: 'propgrid.PGPropArgCls') -> None:
        """ Sets the âcurrentâ category - Append will add non-category properties under it.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetEmptySpaceColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets colour of empty space below properties.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetLineColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets colour of lines between cells.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetMarginColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets background colour of margin.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetScale(self, xs, ys) -> None:
        """ xs (float) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetScrollPageSize(self, orient, pageSize) -> None:
        """ orient (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetScrollRate(self, xstep, ystep) -> None:
        """ Set the horizontal and vertical scrolling increment only.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetScrollbars(self, pixelsPerUnitX, pixelsPerUnitY, noUnitsX, noUnitsY, xPos=0, yPos=0, noRefresh=False) -> None:
        """ Sets up vertical and/or horizontal scrollbars.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetSelection(self, newSelection: ArrayPGProperty) -> None:
        """ Set entire new selection from given list of properties.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetSelectionBackgroundColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets selection background colour - applies to selected property name background.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetSelectionTextColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets selection foreground colour - applies to selected property name text.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetSplitterLeft(self, privateChildrenToo: bool=False) -> None:
        """ Moves splitter as left as possible, while still allowing all labels to be shown in full.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetSplitterPosition(self, newxpos, col=0) -> None:
        """ Sets x coordinate of the splitter.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetTargetRect(self, rect: 'Rect') -> None:
        """ rect (wx.Rect) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetTargetWindow(self, window: 'Window') -> None:
        """ Call this function to tell   wx.Scrolled  to perform the actual scrolling on a different window (and not on itself).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetUnspecifiedValueAppearance(self, cell: 'propgrid.PGCell') -> None:
        """ Sets appearance of value cells representing an unspecified property value.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetVerticalSpacing(self, vspacing: int) -> None:
        """ Sets vertical spacing.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetVirtualWidth(self, width: int) -> None:
        """ Set virtual width for this particular page.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetupTextCtrlValue(self, text: str) -> None:
        """ Must be called in wx.propgrid.PGEditor.CreateControls   if primary editor window is   wx.TextCtrl, just before textctrl is created.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ShouldScrollToChildOnFocus(self, child: 'Window') -> bool:
        """ This method can be overridden in a derived class to prevent scrolling the child window into view automatically when it gets focus.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ShowPropertyError(self, id, msg) -> None:
        """ Shows a brief error message that is related to a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ShowScrollbars(self, horz, vert) -> None:
        """ Set the scrollbar visibility.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def StopAutoScrolling(self) -> None:
        """ Stop generating the scroll events when mouse is held outside the window.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def UnfocusEditor(self) -> bool:
        """ Unfocuses or closes editor if one was open, but does not deselect property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ValueChangeInEvent(self, variant: PGVariant) -> None:
        """ Call this from wx.propgrid.PGProperty.OnEvent   to cause property value to be changed after the function returns (with True as return value).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def WasValueChangedInEvent(self) -> bool:
        """ You can use this member function, for instance, to detect in wx.propgrid.PGProperty.OnEvent   if wx.propgrid.PGProperty.SetValueInEvent   was already called in wx.propgrid.PGEditor.OnEvent .

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    CaptionBackgroundColour: 'Colour'  # See GetCaptionBackgroundColour and SetCaptionBackgroundColour
    CaptionFont: 'Font'  # See GetCaptionFont
    CaptionForegroundColour: 'Colour'  # See GetCaptionForegroundColour
    CellBackgroundColour: 'Colour'  # See GetCellBackgroundColour and SetCellBackgroundColour
    CellDisabledTextColour: 'Colour'  # See GetCellDisabledTextColour and SetCellDisabledTextColour
    CellTextColour: 'Colour'  # See GetCellTextColour and SetCellTextColour
    ColumnCount: int  # See GetColumnCount and SetColumnCount
    EditorTextCtrl: 'TextCtrl'  # See GetEditorTextCtrl
    EmptySpaceColour: 'Colour'  # See GetEmptySpaceColour and SetEmptySpaceColour
    FontHeight: int  # See GetFontHeight
    Grid: 'propgrid.PropertyGrid'  # See GetGrid
    ImageSize: 'Size'  # See GetImageSize
    LabelEditor: 'TextCtrl'  # See GetLabelEditor
    LastItem: 'propgrid.PGProperty'  # See GetLastItem
    LineColour: 'Colour'  # See GetLineColour and SetLineColour
    MarginColour: 'Colour'  # See GetMarginColour and SetMarginColour
    MarginWidth: int  # See GetMarginWidth
    Panel: 'Window'  # See GetPanel
    Root: 'propgrid.PGProperty'  # See GetRoot
    RowHeight: int  # See GetRowHeight
    ScaleX: float  # See GetScaleX
    ScaleY: float  # See GetScaleY
    SelectedProperty: 'propgrid.PGProperty'  # See GetSelectedProperty
    Selection: 'propgrid.PGProperty'  # See GetSelection and SetSelection
    SelectionBackgroundColour: 'Colour'  # See GetSelectionBackgroundColour and SetSelectionBackgroundColour
    SelectionForegroundColour: 'Colour'  # See GetSelectionForegroundColour
    SplitterPosition: int  # See GetSplitterPosition and SetSplitterPosition
    StatusBar: '_StatusBar'  # See GetStatusBar
    TargetRect: 'Rect'  # See GetTargetRect and SetTargetRect
    TargetWindow: 'Window'  # See GetTargetWindow and SetTargetWindow
    UncommittedPropertyValue: 'propgrid.PGVariant'  # See GetUncommittedPropertyValue
    UnspecifiedValueAppearance: 'propgrid.PGCell'  # See GetUnspecifiedValueAppearance and SetUnspecifiedValueAppearance
    UnspecifiedValueText: str  # See GetUnspecifiedValueText
    VerticalSpacing: int  # See GetVerticalSpacing and SetVerticalSpacing



SHOW_SB_ALWAYS: int

SHOW_SB_NEVER: int

SHOW_SB_DEFAULT: int

class PGWindowList:
    """ Contains a list of editor windows returned by CreateControls.

        Source: https://docs.wxpython.org/wx.propgrid.PGWindowList.html
    """
    def __init__(self, primary, secondary=None) -> None:
        """ primary (wx.Window) â

            Source: https://docs.wxpython.org/wx.propgrid.PGWindowList.html
        """

    def GetPrimary(self) -> 'Window':
        """ Gets window of primary editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGWindowList.html
        """

    def GetSecondary(self) -> 'Window':
        """ Gets window of secondary editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGWindowList.html
        """

    def SetSecondary(self, secondary: 'Window') -> None:
        """ secondary (wx.Window) â

            Source: https://docs.wxpython.org/wx.propgrid.PGWindowList.html
        """

    Primary: 'Window'  # See GetPrimary
    Secondary: 'Window'  # See GetSecondary and SetSecondary



class PGArrayStringEditorDialog(PGArrayEditorDialog):
    """ index (int) â 

        Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def ArrayGet(self, index: int) -> str:
        """ index (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def ArrayGetCount(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def ArrayInsert(self, str, index) -> bool:
        """ str (string) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def ArrayRemoveAt(self, index: int) -> None:
        """ index (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def ArraySet(self, index, str) -> bool:
        """ index (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def ArraySwap(self, first, second) -> None:
        """ first (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def GetDialogValue(self) -> 'propgrid.PGVariant':
        """ Return value modified by dialog.

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def Init(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def OnCustomNewAction(self, resString: str) -> bool:
        """ resString (string) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def SetCustomButton(self, custBtText, pcc) -> None:
        """ custBtText (string) â

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def SetDialogValue(self, value: PGVariant) -> None:
        """ Set value modified by dialog.

            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    DialogValue: 'propgrid.PGVariant'  # See GetDialogValue and SetDialogValue



class PropertyGridInterface:
    """ Most of the shared property manipulation interface shared by
PropertyGrid, PropertyGridPage, and PropertyGridManager is
defined in this class.

        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
    """
    def Append(self, property: 'propgrid.PGProperty') -> 'propgrid.PGProperty':
        """ Appends property to the list.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def AppendIn(self, id, newProperty) -> 'propgrid.PGProperty':
        """ Same as Append , but appends under given parent property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def AutoFill(self, obj, parent=None) -> None:
        """ âClears properties and re-fills to match members and values of
the given object or dictionary obj.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def BeginAddChildren(self, id: 'propgrid.PGPropArgCls') -> None:
        """ In order to add new items into a property with private children (for instance,   wx.propgrid.FlagsProperty), you need to call this method.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def ChangePropertyValue(self, id, newValue) -> bool:
        """ Changes value of a property, as if by user.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def Clear(self) -> None:
        """ Deletes all properties.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def ClearModifiedStatus(self) -> None:
        """ Resets modified status of all properties.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def ClearSelection(self, validation: bool=False) -> bool:
        """ Clears current selection, if any.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def Collapse(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Collapses given category or property with children.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def CollapseAll(self) -> bool:
        """ Collapses all items that can be collapsed.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def DeleteProperty(self, id: 'propgrid.PGPropArgCls') -> None:
        """ Removes and deletes a property and any children.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def DisableProperty(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Disables a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def DoDefaultTypeMappings(self) -> None:
        """ Add built-in properties to the map.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def DoDefaultValueTypeMappings(self) -> None:
        """ Map pg value type ids to getter methods.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def EditorValidate(self) -> bool:
        """ Returns True if all property grid data changes have been committed.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def EnableProperty(self, id, enable=True) -> bool:
        """ Enables or disables property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def EndAddChildren(self, id: 'propgrid.PGPropArgCls') -> None:
        """ Called after population of property with fixed children has finished.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def Expand(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Expands given category or property with children.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def ExpandAll(self, expand: bool=True) -> bool:
        """ Expands all items that can be expanded.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetColumnProportion(self, column: int) -> int:
        """ Returns auto-resize proportion of the given column.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    @staticmethod
    def GetEditorByName(editorName: str) -> 'propgrid.PGEditor':
        """ Returns editor pointer of editor with given name.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetFirst(self, flags: int=PG_ITERATE_ALL) -> 'propgrid.PGProperty':
        """ Returns id of first item that matches given criteria.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetFirstChild(self, id: 'propgrid.PGPropArgCls') -> 'propgrid.PGProperty':
        """ Returns id of first child of given property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetIterator(self, *args, **kw) -> 'propgrid.PropertyGridIterator':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertiesWithFlag(self, targetArr, flags, inverse=False, iterFlags=PG_ITERATE_PROPERTIES|PG_ITERATE_HIDDEN|PG_ITERATE_CATEGORIES) -> None:
        """ Adds to targetArr  pointers to properties that have given flags  set.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetProperty(self, name: str) -> 'propgrid.PGProperty':
        """ Returns pointer to a property with given name (case-sensitive).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyAttribute(self, id, attrName) -> 'propgrid.PGVariant':
        """ Returns value of given attribute.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyAttributes(self, id: 'propgrid.PGPropArgCls') -> 'propgrid.PGAttributeStorage':
        """ Returns map-like storage of propertyâs attributes.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyBackgroundColour(self, id: 'propgrid.PGPropArgCls') -> 'Colour':
        """ Returns background colour of first cell of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyByLabel(self, label: str) -> 'propgrid.PGProperty':
        """ Returns first property which label matches given string.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyByName(self, *args, **kw) -> 'propgrid.PGProperty':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyByNameA(self, name: str) -> 'propgrid.PGProperty':
        """ GetPropertyByName   with assertion error message.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyCategory(self, id: 'propgrid.PGPropArgCls') -> 'propgrid.PropertyCategory':
        """ Returns pointer of propertyâs nearest parent category.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyClientData(self, p) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyEditor(self, id: 'propgrid.PGPropArgCls') -> 'propgrid.PGEditor':
        """ Returns propertyâs editor.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyHelpString(self, id: 'propgrid.PGPropArgCls') -> str:
        """ Returns help string associated with a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyImage(self, id: 'propgrid.PGPropArgCls') -> 'Bitmap':
        """ Returns propertyâs custom value image (None of none).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyLabel(self, id: 'propgrid.PGPropArgCls') -> str:
        """ Returns label of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyName(self, property: 'propgrid.PGProperty') -> str:
        """ Returns propertyâs name, by which it is globally accessible.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyParent(self, id: 'propgrid.PGPropArgCls') -> 'propgrid.PGProperty':
        """ Returns parent item of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyTextColour(self, id: 'propgrid.PGPropArgCls') -> 'Colour':
        """ Returns text colour of first cell of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValidator(self, id: 'propgrid.PGPropArgCls') -> 'Validator':
        """ Returns validator of a property as a reference, which you can pass to any number of SetPropertyValidator.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValue(self, id: 'propgrid.PGPropArgCls') -> 'propgrid.PGVariant':
        """ Returns propertyâs value as Variant     .

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsArrayInt(self, id: 'propgrid.PGPropArgCls') -> list[int]:
        """ Returnâs propertyâs value as ArrayInt.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsArrayString(self, id: 'propgrid.PGPropArgCls') -> list[str]:
        """ Returns propertyâs value as list of strings     .

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsBool(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Returns propertyâs value as bool.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsDateTime(self, id: 'propgrid.PGPropArgCls') -> 'DateTime':
        """ Returnâs propertyâs value as   wx.DateTime.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsDouble(self, id: 'propgrid.PGPropArgCls') -> float:
        """ Returns propertyâs value as double-precision floating point number.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsInt(self, id: 'propgrid.PGPropArgCls') -> int:
        """ Returns propertyâs value as integer.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsLong(self, id: 'propgrid.PGPropArgCls') -> int:
        """ Returns propertyâs value as integer.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsLongLong(self, id: 'propgrid.PGPropArgCls') -> 'LongLong_t':
        """ Returns propertyâs value as native signed 64-bit integer.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsString(self, id: 'propgrid.PGPropArgCls') -> str:
        """ Returns propertyâs value as String     .

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsULong(self, id: 'propgrid.PGPropArgCls') -> int:
        """ Returns propertyâs value as  integer.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsULongLong(self, id: 'propgrid.PGPropArgCls') -> int:
        """ Returns propertyâs value as native  64-bit integer.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValues(self, dict_=None, as_strings=False, inc_attributes=False, flags=PG_ITERATE_PROPERTIES) -> None:
        """ Returns all property values in the grid.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPyIterator(self, flags=PG_ITERATE_DEFAULT, firstProperty=None) -> None:
        """ Returns a pythonic property iterator for a single PropertyGrid
or page in PropertyGridManager     . Arguments are same as for
GetIterator     .

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPyVIterator(self, flags=PG_ITERATE_DEFAULT) -> None:
        """ Similar to GetVIterator      but returns a pythonic iterator.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetSelectedProperties(self) -> 'propgrid.ArrayPGProperty':
        """ Returns list of currently selected properties.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetSelection(self) -> 'propgrid.PGProperty':
        """ Returns currently selected property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetVIterator(self, flags: int) -> 'propgrid.PGVIterator':
        """ Similar to GetIterator , but instead returns   wx.propgrid.PGVIterator  instance, which can be useful for forward-iterating through arbitrary property containers.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def HideProperty(self, id, hide=True, flags=PG_RECURSE) -> bool:
        """ Hides or reveals a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    @staticmethod
    def InitAllTypeHandlers() -> None:
        """ Initializes all  property types.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def Insert(self, *args, **kw) -> 'propgrid.PGProperty':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertyCategory(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Returns True if property is a category.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertyEnabled(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Returns True if property is enabled.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertyExpanded(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Returns True if given property is expanded.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertyModified(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Returns True if property has been modified after value set or modify flag clear by software.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertySelected(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Returns True if property is selected.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertyShown(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Returns True if property is shown (i.e.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertyValueUnspecified(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ Returns True if property value is set to unspecified.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def LimitPropertyEditing(self, id, limit=True) -> None:
        """ Disables (limit  = True) or enables (limit  = False)   wx.TextCtrl  editor of a property, if it is not the sole mean to edit the value.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def MapType(self, class_, factory: Any) -> None:
        """ Registers Python type/class to property mapping.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def RefreshGrid(self, state: Optional['propgrid.PropertyGridPageState']=None) -> None:
        """ If state is shown in its grid, refresh it now.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def RefreshProperty(self, p: 'propgrid.PGProperty') -> None:
        """ p (wx.propgrid.PGProperty) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    @staticmethod
    def RegisterAdditionalEditors() -> None:
        """ Initializes additional property editors (SpinCtrl etc.).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def RegisterEditor(self, editor, editorName=None) -> None:
        """ Register a new editor, either an instance or a class.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def RemoveProperty(self, id: 'propgrid.PGPropArgCls') -> 'propgrid.PGProperty':
        """ Removes a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def ReplaceProperty(self, id, property) -> 'propgrid.PGProperty':
        """ Replaces property with id with newly created one.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def RestoreEditableState(self, src, restoreStates=AllStates) -> bool:
        """ Restores user-editable state.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SaveEditableState(self, includedStates: int=AllStates) -> str:
        """ Used to acquire user-editable state (selected property, expanded properties, scrolled position, splitter positions).

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    @staticmethod
    def SetBoolChoices(trueChoice, falseChoice) -> None:
        """ Sets strings listed in the choice dropdown of a   wx.propgrid.BoolProperty.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetColumnProportion(self, column, proportion) -> bool:
        """ Set proportion of an auto-stretchable column.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropVal(self, id, value) -> None:
        """ Sets value (Variant     &) of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyAttribute(self, id, attrName, value, argFlags=0) -> None:
        """ Sets an attribute for this property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyAttributeAll(self, attrName, value) -> None:
        """ Sets property attribute for all applicable properties.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyBackgroundColour(self, id, colour, flags=PG_RECURSE) -> None:
        """ Sets background colour of given property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyCell(*args, **kwargs) -> None:
        """ Sets text, bitmap, and colours for given columnâs cell.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyClientData(self, p, data) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyColoursToDefault(self, id, flags=PG_DONT_RECURSE) -> None:
        """ Resets text and background colours of given property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyEditor(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyHelpString(self, id, helpString) -> None:
        """ Associates the help string with property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyImage(self, id, bmp) -> None:
        """ Set   wx.Bitmap  taken from   wx.BitmapBundle  in front of the value.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyLabel(self, id, newproplabel) -> None:
        """ Sets label of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyMaxLength(self, id, maxLen) -> bool:
        """ Sets maximum length of text in property text editor.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyName(self, id, newName) -> None:
        """ Sets name of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyReadOnly(self, id, set=True, flags=PG_RECURSE) -> None:
        """ Sets property (and, recursively, its children) to have read-only value.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyTextColour(self, id, colour, flags=PG_RECURSE) -> None:
        """ Sets text colour of given property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyValidator(self, id, validator) -> None:
        """ Sets validator of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyValue(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyValueString(self, id, value) -> None:
        """ Sets value (String     ) of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyValueUnspecified(self, id: 'propgrid.PGPropArgCls') -> None:
        """ Sets propertyâs value to unspecified.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyValues(self, dict_, autofill=False) -> None:
        """ Sets property values from a dictionary.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetValidationFailureBehavior(self, vfbFlags: int) -> None:
        """ Adjusts how   wx.propgrid.PropertyGrid  behaves when invalid value is entered in a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def Sort(self, flags: int=0) -> None:
        """ Sorts all properties recursively.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SortChildren(self, id, flags=0) -> None:
        """ Sorts children of a property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def _AutoFillMany(self, cat, dict_) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def _AutoFillOne(self, cat, k, v) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def _Items(self) -> None:
        """ This attribute is a pythonic iterator over all items in this
PropertyGrid property container, excluding only private child
properties. Usage is simple:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def _Properties(self) -> None:
        """ This attribute is a pythonic iterator over all properties in
this PropertyGrid property container. It will only skip
categories and private child properties. Usage is simple:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    Items: Any  # See _Items
    Properties: Any  # See _Properties



PG_VFB_STAY_IN_PROPERTY: int

PG_ITERATE_DEFAULT: int

TOP: int

BOTTOM: int

PG_EX_MULTIPLE_SELECTION: int

PG_DONT_RECURSE: int

PG_SPLITTER_AUTO_CENTER: int

PG_RECURSE: int

PG_LABEL: int

PG_EX_HELP_AS_TOOLTIPS: int

PG_SORT_TOP_LEVEL_ONLY: int

PG_AUTO_SORT: int

class PropertyGridPageState:
    """ Contains low-level property page information (properties, column
widths, etc.) of a single PropertyGrid or single PropertyGridPage.

        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def CheckColumnWidths(self, widthChange: int=0) -> None:
        """ Makes sure all columns have minimum width.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def DoDelete(self, item, doDelete=True) -> None:
        """ Override this member function to add custom behaviour on property deletion.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def DoInsert(self, parent, index, property) -> 'propgrid.PGProperty':
        """ Override this member function to add custom behaviour on property insertion.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def DoSetSplitterPosition(self, pos, splitterColumn=0, flags=0) -> None:
        """ This needs to be overridden in grid used the manager so that splitter changes can be propagated to other pages.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def EnableCategories(self, enable: bool) -> bool:
        """ enable (bool) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def EnsureVirtualHeight(self) -> None:
        """ Make sure virtual height is up-to-date.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetActualVirtualHeight(self) -> int:
        """ Returns actual height of contained visible properties.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetColumnCount(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetColumnFullWidth(self, p, col) -> int:
        """ p (wx.propgrid.PGProperty) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetColumnMinWidth(self, column: int) -> int:
        """ column (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetColumnWidth(self, column: int) -> int:
        """ column (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetGrid(self) -> 'propgrid.PropertyGrid':
        """ wx.propgrid.PropertyGrid

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetLastItem(self, flags: int=PG_ITERATE_DEFAULT) -> 'propgrid.PGProperty':
        """ Returns last item which could be iterated using given flags.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetPropertyCategory(self, p: 'propgrid.PGProperty') -> 'propgrid.PropertyCategory':
        """ p (wx.propgrid.PGProperty) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetSelection(self) -> 'propgrid.PGProperty':
        """ Returns currently selected property.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetVirtualHeight(self) -> int:
        """ Returns (precalculated) height of contained visible properties.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetVirtualWidth(self) -> int:
        """ Returns combined width of margin and all the columns.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def HitTest(self, pt: Union[tuple[int, int], 'Point']) -> 'propgrid.PropertyGridHitTestResult':
        """ Returns information about arbitrary position in the grid.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def IsDisplayed(self) -> bool:
        """ Returns True if page is visibly displayed.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def IsInNonCatMode(self) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def VirtualHeightChanged(self) -> None:
        """ Called after virtual height needs to be recalculated.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    ActualVirtualHeight: int  # See GetActualVirtualHeight
    ColumnCount: int  # See GetColumnCount
    Grid: 'propgrid.PropertyGrid'  # See GetGrid
    LastItem: 'propgrid.PGProperty'  # See GetLastItem
    Selection: 'propgrid.PGProperty'  # See GetSelection
    VirtualHeight: int  # See GetVirtualHeight
    VirtualWidth: int  # See GetVirtualWidth



class SystemColourProperty(EnumProperty):
    """ Has dropdown list of wxWidgets system colours.

        Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
    """
    def __init__(*args, **kwargs) -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def ColourToString(self, col, index, argFlags=0) -> str:
        """ Override in derived class to customize how colours are printed as strings.

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ Reimplement this member function to add special handling for attributes of this property.

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def GetColour(self, index: int) -> 'Colour':
        """ Default is to use SystemSettings.GetColour(index).

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def GetCustomColourIndex(self) -> int:
        """ Returns index of entry that triggers colour picker dialog (default is last).

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def GetVal(self, pVariant: Optional[PGVariant]=None) -> 'propgrid.ColourPropertyValue':
        """ pVariant (PGVariant) â

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def IntToValue(self, number, argFlags=0) -> tuple:
        """ Converts integer (possibly a choice selection) into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def OnCustomPaint(self, dc, rect, paintdata) -> None:
        """ Override to paint an image in front of the property value text or drop-down list item (but only if wx.propgrid.PGProperty.OnMeasureImage   is overridden as well).

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def OnEvent(self, propgrid, wnd_primary, event) -> None:
        """ Events received by editor widgets are processed here.

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def OnMeasureImage(self, item: int) -> 'Size':
        """ Returns size of the custom painted image in front of property.

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def OnSetValue(self) -> None:
        """ This virtual function is called after m_value has been set.

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def QueryColourFromUser(self, variant: PGVariant) -> bool:
        """ variant (PGVariant) â

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    CustomColourIndex: int  # See GetCustomColourIndex
    Val: 'propgrid.ColourPropertyValue'  # See GetVal



class PGChoiceEntry(PGCell):
    """ Data of a single PGChoices choice.

        Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEntry.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEntry.html
        """

    def GetValue(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEntry.html
        """

    def SetValue(self, value: int) -> None:
        """ value (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEntry.html
        """

    Value: int  # See GetValue and SetValue



class PGCellData(ObjectRefData):
    """ col (wx.Colour) â 

        Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
        """

    def SetBgCol(self, col: Union[int, str, 'Colour']) -> None:
        """ col (wx.Colour) â

            Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
        """

    def SetBitmap(self, bitmap: 'BitmapBundle') -> None:
        """ bitmap (wx.BitmapBundle) â

            Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
        """

    def SetFgCol(self, col: Union[int, str, 'Colour']) -> None:
        """ col (wx.Colour) â

            Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ font (wx.Font) â

            Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
        """

    def SetText(self, text: str) -> None:
        """ text (string) â

            Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
        """



class PGCheckBoxEditor(PGEditor):
    """ Instantiates editor controls.

        Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'propgrid.PGWindowList':
        """ Instantiates editor controls.

            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def DrawValue(self, dc, rect, property, text) -> None:
        """ Draws value for given property.

            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def GetName(self) -> str:
        """ Returns pointer to the name of the editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def GetValueFromControl(self, variant, property, ctrl) -> bool:
        """ Returns value from control, via parameter variant.

            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def OnEvent(self, propgrid, property, wnd_primary, event) -> bool:
        """ Handles events.

            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def SetControlIntValue(self, property, ctrl, value) -> None:
        """ Sets controlâs value specifically from int (applies to choice etc.).

            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def SetValueToUnspecified(self, property, ctrl) -> None:
        """ Sets value in control to unspecified.

            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def UpdateControl(self, property, ctrl) -> None:
        """ Loads value from property to the control.

            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    Name: str  # See GetName



class PGChoiceEditor(PGEditor):
    """ Returns True if control itself can contain the custom image.

        Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def CanContainCustomImage(self) -> bool:
        """ Returns True if control itself can contain the custom image.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'propgrid.PGWindowList':
        """ Instantiates editor controls.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def CreateControlsBase(self, propgrid, property, pos, sz, extraStyle) -> 'Window':
        """ propgrid (wx.propgrid.PropertyGrid) â

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def DeleteItem(self, ctrl, index) -> None:
        """ Deletes item from existing control.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def GetName(self) -> str:
        """ Returns pointer to the name of the editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def GetValueFromControl(self, variant, property, ctrl) -> bool:
        """ Returns value from control, via parameter variant.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def InsertItem(self, ctrl, label, index) -> int:
        """ Inserts item to existing control.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def OnEvent(self, propgrid, property, wnd_primary, event) -> bool:
        """ Handles events.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def SetControlIntValue(self, property, ctrl, value) -> None:
        """ Sets controlâs value specifically from int (applies to choice etc.).

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def SetControlStringValue(self, property, ctrl, txt) -> None:
        """ Sets controlâs value specifically from string.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def SetValueToUnspecified(self, property, ctrl) -> None:
        """ Sets value in control to unspecified.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def UpdateControl(self, property, ctrl) -> None:
        """ Loads value from property to the control.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    Name: str  # See GetName



class PGTextCtrlEditor(PGEditor):
    """ Instantiates editor controls.

        Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'propgrid.PGWindowList':
        """ Instantiates editor controls.

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def GetName(self) -> str:
        """ Returns pointer to the name of the editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    @staticmethod
    def GetTextCtrlValueFromControl(variant, property, ctrl) -> bool:
        """ variant (PGVariant) â

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def GetValueFromControl(self, variant, property, ctrl) -> bool:
        """ Returns value from control, via parameter variant.

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def OnEvent(self, propgrid, property, wnd_primary, event) -> bool:
        """ Handles events.

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def OnFocus(self, property, wnd) -> None:
        """ Extra processing when control gains focus.

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    @staticmethod
    def OnTextCtrlEvent(propgrid, property, ctrl, event) -> bool:
        """ propgrid (wx.propgrid.PropertyGrid) â

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def SetControlStringValue(self, property, ctrl, txt) -> None:
        """ Sets controlâs value specifically from string.

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def UpdateControl(self, property, ctrl) -> None:
        """ Loads value from property to the control.

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    Name: str  # See GetName



class ArrayStringProperty(EditorDialogProperty):
    """ Property that manages a list of strings.

        Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value=[]) -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    @staticmethod
    def ArrayStringToString(src, delimiter, flags) -> str:
        """ Generates string based on the contents of list of strings       src.

            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def ConvertArrayToString(self, arr, delimiter) -> str:
        """ Implement in derived class for custom array-to-string conversion.

            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def CreateEditorDialog(self) -> 'propgrid.PGArrayEditorDialog':
        """ Creates   wx.propgrid.PGArrayEditorDialog  for string editing.

            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def DisplayEditorDialog(self, pg, value) -> tuple:
        """ Shows editor dialog.

            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ Reimplement this member function to add special handling for attributes of this property.

            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def GenerateValueAsString(self) -> None:
        """ Previously this was to be implemented in derived class for array-to- string conversion.

            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def OnCustomStringEdit(self, parent, value) -> bool:
        """ Shows string editor dialog to edit the individual item.

            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def OnSetValue(self) -> None:
        """ This virtual function is called after m_value has been set.

            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """



class BoolProperty(PGProperty):
    """ Basic property with boolean value.

        Source: https://docs.wxpython.org/wx.propgrid.BoolProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value=False) -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.BoolProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ Reimplement this member function to add special handling for attributes of this property.

            Source: https://docs.wxpython.org/wx.propgrid.BoolProperty.html
        """

    def IntToValue(self, number, argFlags=0) -> tuple:
        """ Converts integer (possibly a choice selection) into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.BoolProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.BoolProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.BoolProperty.html
        """



class ColourProperty(SystemColourProperty):
    """ Allows to select a colour from the list or with colour dialog.

        Source: https://docs.wxpython.org/wx.propgrid.ColourProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value=WHITE) -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.ColourProperty.html
        """

    def GetColour(self, index: int) -> 'Colour':
        """ Default is to use SystemSettings.GetColour(index).

            Source: https://docs.wxpython.org/wx.propgrid.ColourProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.ColourProperty.html
        """



class CursorProperty(EnumProperty):
    """ Property representing Cursor.

        Source: https://docs.wxpython.org/wx.propgrid.CursorProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value=0) -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.CursorProperty.html
        """

    def OnCustomPaint(self, dc, rect, paintdata) -> None:
        """ Override to paint an image in front of the property value text or drop-down list item (but only if wx.propgrid.PGProperty.OnMeasureImage   is overridden as well).

            Source: https://docs.wxpython.org/wx.propgrid.CursorProperty.html
        """

    def OnMeasureImage(self, item: int) -> 'Size':
        """ Returns size of the custom painted image in front of property.

            Source: https://docs.wxpython.org/wx.propgrid.CursorProperty.html
        """



class DateProperty(PGProperty):
    """ Property representing DateTime.

        Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
    """
    def __init__(*args, **kwargs) -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ Reimplement this member function to add special handling for attributes of this property.

            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def GetDatePickerStyle(self) -> int:
        """ long

            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def GetDateValue(self) -> 'DateTime':
        """ DateTime

            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def GetFormat(self) -> str:
        """ string

            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def OnSetValue(self) -> None:
        """ This virtual function is called after m_value has been set.

            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def SetDateValue(self, dt: 'DateTime') -> None:
        """ dt (wx.DateTime) â

            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def SetFormat(self, format: str) -> None:
        """ format (string) â

            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    DatePickerStyle: int  # See GetDatePickerStyle
    DateValue: 'DateTime'  # See GetDateValue and SetDateValue
    Format: str  # See GetFormat and SetFormat



class DirProperty(EditorDialogProperty):
    """ Like LongStringProperty, but the button triggers directory selector
instead.

        Source: https://docs.wxpython.org/wx.propgrid.DirProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value="") -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.DirProperty.html
        """

    def DisplayEditorDialog(self, pg, value) -> tuple:
        """ Shows editor dialog.

            Source: https://docs.wxpython.org/wx.propgrid.DirProperty.html
        """

    def DoGetValidator(self) -> 'Validator':
        """ Returns pointer to the   wx.Validator  that should be used with the editor of this property (None for no validator).

            Source: https://docs.wxpython.org/wx.propgrid.DirProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.DirProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.DirProperty.html
        """



class EditEnumProperty(EnumProperty):
    """ EnumProperty with string value and writable combo box editor.

        Source: https://docs.wxpython.org/wx.propgrid.EditEnumProperty.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.EditEnumProperty.html
        """



class EnumProperty(PGProperty):
    """ You can derive custom properties with choices from this class.

        Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def GetChoiceSelection(self) -> int:
        """ Returns which choice is currently selected.

            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def GetIndexForValue(self, value: int) -> int:
        """ value (int) â

            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def GetItemCount(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def IntToValue(self, number, argFlags=0) -> tuple:
        """ Converts integer (possibly a choice selection) into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def OnSetValue(self) -> None:
        """ This virtual function is called after m_value has been set.

            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def ValidateValue(self, value, validationInfo) -> bool:
        """ Implement this function in derived class to check the value.

            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    ChoiceSelection: int  # See GetChoiceSelection
    ItemCount: int  # See GetItemCount



class FileProperty(EditorDialogProperty):
    """ Like LongStringProperty, but the button triggers file selector
instead.

        Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value="") -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def DisplayEditorDialog(self, pg, value) -> tuple:
        """ Shows editor dialog.

            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def DoGetValidator(self) -> 'Validator':
        """ Returns pointer to the   wx.Validator  that should be used with the editor of this property (None for no validator).

            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ Reimplement this member function to add special handling for attributes of this property.

            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    @staticmethod
    def GetClassValidator() -> 'Validator':
        """ Validator

            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def GetFileName(self) -> str:
        """ Returns filename to file represented by current value.

            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def OnSetValue(self) -> None:
        """ This virtual function is called after m_value has been set.

            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    FileName: str  # See GetFileName



class FlagsProperty(PGProperty):
    """ Represents a bit set that fits in a long integer.

        Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def ChildChanged(self, thisValue, childIndex, childValue) -> 'propgrid.PGVariant':
        """ Called after value of a child property has been altered.

            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ Reimplement this member function to add special handling for attributes of this property.

            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def GetChoiceSelection(self) -> int:
        """ Returns which choice is currently selected.

            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def GetItemCount(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def GetLabel(self, ind: int) -> str:
        """ ind (int) â

            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def OnSetValue(self) -> None:
        """ This virtual function is called after m_value has been set.

            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def RefreshChildren(self) -> None:
        """ Refresh values of child properties.

            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def StringToValue(self, text, argFlags) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    ChoiceSelection: int  # See GetChoiceSelection
    ItemCount: int  # See GetItemCount



class FloatProperty(NumericProperty):
    """ Basic property with double-precision floating point value.

        Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value=0.0) -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    def AddSpinStepValue(self, stepScale: int) -> 'propgrid.PGVariant':
        """ Returns what would be the new value of the property after adding SpinCtrl editor step to the current value.

            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    def DoGetValidator(self) -> 'Validator':
        """ Returns pointer to the   wx.Validator  that should be used with the editor of this property (None for no validator).

            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ Reimplement this member function to add special handling for attributes of this property.

            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    @staticmethod
    def GetClassValidator() -> 'Validator':
        """ Validator

            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    def ValidateValue(self, value, validationInfo) -> bool:
        """ Implement this function in derived class to check the value.

            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """



class FontProperty(EditorDialogProperty):
    """ Property representing Font.

        Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
    """
    def __init__(*args, **kwargs) -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
        """

    def ChildChanged(self, thisValue, childIndex, childValue) -> 'propgrid.PGVariant':
        """ Called after value of a child property has been altered.

            Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
        """

    def DisplayEditorDialog(self, pg, value) -> tuple:
        """ Shows editor dialog.

            Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
        """

    def OnSetValue(self) -> None:
        """ This virtual function is called after m_value has been set.

            Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
        """

    def RefreshChildren(self) -> None:
        """ Refresh values of child properties.

            Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
        """



class ImageFileProperty(FileProperty):
    """ Property representing image file(name).

        Source: https://docs.wxpython.org/wx.propgrid.ImageFileProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value="") -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.ImageFileProperty.html
        """

    def OnCustomPaint(self, dc, rect, paintdata) -> None:
        """ Override to paint an image in front of the property value text or drop-down list item (but only if wx.propgrid.PGProperty.OnMeasureImage   is overridden as well).

            Source: https://docs.wxpython.org/wx.propgrid.ImageFileProperty.html
        """

    def OnMeasureImage(self, item: int) -> 'Size':
        """ Returns size of the custom painted image in front of property.

            Source: https://docs.wxpython.org/wx.propgrid.ImageFileProperty.html
        """

    def OnSetValue(self) -> None:
        """ This virtual function is called after m_value has been set.

            Source: https://docs.wxpython.org/wx.propgrid.ImageFileProperty.html
        """



class IntProperty(NumericProperty):
    """ Basic property with integer value.

        Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    def AddSpinStepValue(self, stepScale: int) -> 'propgrid.PGVariant':
        """ Returns what would be the new value of the property after adding SpinCtrl editor step to the current value.

            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    def DoGetValidator(self) -> 'Validator':
        """ Returns pointer to the   wx.Validator  that should be used with the editor of this property (None for no validator).

            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    @staticmethod
    def GetClassValidator() -> 'Validator':
        """ Validator

            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    def IntToValue(self, number, argFlags=0) -> tuple:
        """ Converts integer (possibly a choice selection) into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    def ValidateValue(self, value, validationInfo) -> bool:
        """ Implement this function in derived class to check the value.

            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """



class LongStringProperty(EditorDialogProperty):
    """ Like StringProperty, but has a button that triggers a small text
editor dialog.

        Source: https://docs.wxpython.org/wx.propgrid.LongStringProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value="") -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.LongStringProperty.html
        """

    def DisplayEditorDialog(self, pg, value) -> tuple:
        """ Shows editor dialog.

            Source: https://docs.wxpython.org/wx.propgrid.LongStringProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.LongStringProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.LongStringProperty.html
        """



class MultiChoiceProperty(EditorDialogProperty):
    """ Property that manages a value resulting from MultiChoiceDialog.

        Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
        """

    def DisplayEditorDialog(self, pg, value) -> tuple:
        """ Shows editor dialog.

            Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
        """

    def GetValueAsArrayInt(self) -> list[int]:
        """ list of integers

            Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
        """

    def OnSetValue(self) -> None:
        """ This virtual function is called after m_value has been set.

            Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
        """

    ValueAsArrayInt: list[int]  # See GetValueAsArrayInt



class PropertyCategory(PGProperty):
    """ Category (caption) property.

        Source: https://docs.wxpython.org/wx.propgrid.PropertyCategory.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyCategory.html
        """

    def GetTextExtent(self, wnd, font) -> int:
        """ wnd (wx.Window) â

            Source: https://docs.wxpython.org/wx.propgrid.PropertyCategory.html
        """

    def GetValueAsString(self, argFlags: int=0) -> str:
        """ Returns text representation of propertyâs value.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyCategory.html
        """

    def ValueToString(self, value, argFlags) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyCategory.html
        """

    ValueAsString: str  # See GetValueAsString



class StringProperty(PGProperty):
    """ Basic property with string value.

        Source: https://docs.wxpython.org/wx.propgrid.StringProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value="") -> None:
        """ label (string) â

            Source: https://docs.wxpython.org/wx.propgrid.StringProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ Reimplement this member function to add special handling for attributes of this property.

            Source: https://docs.wxpython.org/wx.propgrid.StringProperty.html
        """

    def OnSetValue(self) -> None:
        """ This is updated so â<composed>â special value can be handled.

            Source: https://docs.wxpython.org/wx.propgrid.StringProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.StringProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.StringProperty.html
        """



class UIntProperty(NumericProperty):
    """ Basic property with  integer value.

        Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def AddSpinStepValue(self, stepScale: int) -> 'propgrid.PGVariant':
        """ Returns what would be the new value of the property after adding SpinCtrl editor step to the current value.

            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def DoGetValidator(self) -> 'Validator':
        """ Returns pointer to the   wx.Validator  that should be used with the editor of this property (None for no validator).

            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ Reimplement this member function to add special handling for attributes of this property.

            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def IntToValue(self, number, argFlags=0) -> tuple:
        """ Converts integer (possibly a choice selection) into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ Converts text into Variant       value appropriate for this property.

            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def ValidateValue(self, value, validationInfo) -> bool:
        """ Implement this function in derived class to check the value.

            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ Converts property value into a text representation.

            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """



class NumericProperty(PGProperty):
    """ This is an abstract class which serves as a base class for numeric
properties, like IntProperty, UIntProperty, FloatProperty.

        Source: https://docs.wxpython.org/wx.propgrid.NumericProperty.html
    """
    def AddSpinStepValue(self, stepScale: int) -> 'propgrid.PGVariant':
        """ Returns what would be the new value of the property after adding SpinCtrl editor step to the current value.

            Source: https://docs.wxpython.org/wx.propgrid.NumericProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ Reimplement this member function to add special handling for attributes of this property.

            Source: https://docs.wxpython.org/wx.propgrid.NumericProperty.html
        """

    def UseSpinMotion(self) -> bool:
        """ Return True if value can be changed with SpinCtrl editor by moving the mouse.

            Source: https://docs.wxpython.org/wx.propgrid.NumericProperty.html
        """

    def __init__(self, label, name) -> None:
        """ Constructor is protected because   wx.propgrid.NumericProperty  is only a base class for other numeric property classes.

            Source: https://docs.wxpython.org/wx.propgrid.NumericProperty.html
        """



class EditorDialogProperty(PGProperty):
    """ This is an abstract class which serves as a base class for the
properties having a button triggering an editor dialog, like e.g.

        Source: https://docs.wxpython.org/wx.propgrid.EditorDialogProperty.html
    """
    def DisplayEditorDialog(self, pg, value) -> bool:
        """ Shows editor dialog.

            Source: https://docs.wxpython.org/wx.propgrid.EditorDialogProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ Reimplement this member function to add special handling for attributes of this property.

            Source: https://docs.wxpython.org/wx.propgrid.EditorDialogProperty.html
        """

    def GetEditorDialog(self) -> 'propgrid.PGEditorDialogAdapter':
        """ Returns instance of a new   wx.propgrid.PGEditorDialogAdapter  instance, which is used when user presses the (optional) button next to the editor control;.

            Source: https://docs.wxpython.org/wx.propgrid.EditorDialogProperty.html
        """

    def __init__(self, label, name) -> None:
        """ Constructor is protected because   wx.propgrid.EditorDialogProperty  is only the base class for other property classes.

            Source: https://docs.wxpython.org/wx.propgrid.EditorDialogProperty.html
        """

    EditorDialog: 'propgrid.PGEditorDialogAdapter'  # See GetEditorDialog



class PGChoices:
    """ Helper class for managing choices of PropertyGrid properties.

        Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Add(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def AddAsSorted(self, label, value=PG_INVALID_VALUE) -> 'propgrid.PGChoiceEntry':
        """ Adds a single item, sorted.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def AllocExclusive(self) -> None:
        """ Creates exclusive copy of current choices.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Assign(self, a: 'propgrid.PGChoices') -> None:
        """ Assigns choices data, using reference counting.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def AssignData(self, data: 'propgrid.PGChoicesData') -> None:
        """ Assigns data from another set of choices.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Clear(self) -> None:
        """ Deletes all items.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Copy(self) -> 'propgrid.PGChoices':
        """ Returns a real copy of the choices.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def EnsureData(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def ExtractData(self) -> 'propgrid.PGChoicesData':
        """ Changes ownership of data to you.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetCount(self) -> int:
        """ Returns number of items.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetData(self) -> 'propgrid.PGChoicesData':
        """ Returns data, increases refcount.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetDataPtr(self) -> 'propgrid.PGChoicesData':
        """ Returns plain data ptr - no refcounting stuff is done.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetId(self) -> int:
        """ Gets an  number identifying this list.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetIndicesForStrings(self, strings, unmatched=None) -> list[int]:
        """ Returns array of indices matching given strings.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetLabel(self, ind: int) -> str:
        """ Returns label of item.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetLabels(self) -> list[str]:
        """ Returns array of choice labels.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetValue(self, ind: int) -> int:
        """ Returns value of item.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetValuesForStrings(self, strings: list[str]) -> list[int]:
        """ Returns array of values matching the given strings.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Index(self, *args, **kw) -> int:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Insert(self, *args, **kw) -> 'propgrid.PGChoiceEntry':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def IsOk(self) -> bool:
        """ Returns False if this is a constant empty set of choices, which should not be modified.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Item(self, i: int) -> 'propgrid.PGChoiceEntry':
        """ Returns item at given index.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def RemoveAt(self, nIndex, count=1) -> None:
        """ Removes count items starting at position nIndex.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Set(self, labels, values=[]) -> None:
        """ This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def __getitem__(self, index) -> None:
        """ Returns a reference to a :class:PGChoiceEntry using Python list syntax.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def __len__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    Count: int  # See GetCount
    Data: 'propgrid.PGChoicesData'  # See GetData
    DataPtr: 'propgrid.PGChoicesData'  # See GetDataPtr
    Id: int  # See GetId
    Labels: list[str]  # See GetLabels



class PGCellRenderer(ObjectRefData):
    """ Base class for PropertyGrid cell renderers.

        Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def DrawCaptionSelectionRect(self, dc, x, y, w, h) -> None:
        """ Paints property category selection rectangle.

            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def DrawEditorValue(self, dc, rect, xOffset, text, property, editor) -> None:
        """ Utility to draw editorâs value, or vertically aligned text if editor is None.

            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def DrawText(self, dc, rect, imageWidth, text) -> None:
        """ Utility to draw vertically centered text.

            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def GetImageSize(self, property, column, item) -> 'Size':
        """ Returns size of the image in front of the editable area.

            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def PostDrawCell(self, dc, propGrid, cell, flags) -> None:
        """ Utility to be called after drawing is done, to revert whatever changes PreDrawCell   did.

            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def PreDrawCell(self, dc, rect, propGrid, cell, flags) -> int:
        """ Utility to render cell bitmap and set text colour plus bg brush colour.

            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def Render(self, dc, rect, propertyGrid, property, column, item, flags) -> bool:
        """ Returns True if rendered something in the foreground (text or bitmap).

            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """



PGPropertyFlags: TypeAlias = int  # Enumeration

PG_PROP_MODIFIED: int

PG_PROP_DISABLED: int

PG_PROP_HIDDEN: int

PG_PROP_CUSTOMIMAGE: int

PG_PROP_NOEDITOR: int

PG_PROP_COLLAPSED: int

PG_PROP_INVALID_VALUE: int

PG_PROP_WAS_MODIFIED: int

PG_PROP_AGGREGATE: int

PG_PROP_CHILDREN_ARE_COPIES: int

PG_PROP_PROPERTY: int

PG_PROP_CATEGORY: int

PG_PROP_MISC_PARENT: int

PG_PROP_READONLY: int

PG_PROP_COMPOSED_VALUE: int

PG_PROP_USES_COMMON_VALUE: int

PG_PROP_AUTO_UNSPECIFIED: int

PG_PROP_CLASS_SPECIFIC_1: int

PG_PROP_CLASS_SPECIFIC_2: int

PG_PROP_BEING_DELETED: int

class PGPaintData:
    """ Contains information related to propertyâs OnCustomPaint.

        Source: https://docs.wxpython.org/wx.propgrid.PGPaintData.html
    """
    m_choiceItem: Any  # A public C++ attribute of type int. Normally -1, otherwise index to drop-down list item that has to be drawn.
    m_drawnHeight: Any  # A public C++ attribute of type int. In a measure item call, set this to the height of item at m_choiceItem index.
    m_drawnWidth: Any  # A public C++ attribute of type int. Set to drawn width in OnCustomPaint (optional).
    m_parent: Any  # A public C++ attribute of type PropertyGrid     .   wx.propgrid.PropertyGrid



class PGValidationInfo:
    """ Used to convey validation information to and from functions that
actually perform validation.

        Source: https://docs.wxpython.org/wx.propgrid.PGValidationInfo.html
    """
    def GetFailureBehavior(self) -> 'propgrid.byte':
        """ wx.byte

            Source: https://docs.wxpython.org/wx.propgrid.PGValidationInfo.html
        """

    def GetFailureMessage(self) -> str:
        """ Returns current failure message.

            Source: https://docs.wxpython.org/wx.propgrid.PGValidationInfo.html
        """

    def GetValue(self) -> 'propgrid.PGVariant':
        """ Returns reference to pending value.

            Source: https://docs.wxpython.org/wx.propgrid.PGValidationInfo.html
        """

    def SetFailureBehavior(self, failureBehavior: 'byte') -> None:
        """ Set validation failure behaviour.

            Source: https://docs.wxpython.org/wx.propgrid.PGValidationInfo.html
        """

    def SetFailureMessage(self, message: str) -> None:
        """ Set current failure message.

            Source: https://docs.wxpython.org/wx.propgrid.PGValidationInfo.html
        """

    FailureBehavior: 'propgrid.byte'  # See GetFailureBehavior and SetFailureBehavior
    FailureMessage: str  # See GetFailureMessage and SetFailureMessage
    Value: 'propgrid.PGVariant'  # See GetValue



class PGVIterator:
    """  Overloaded Implementations:

        Source: https://docs.wxpython.org/wx.propgrid.PGVIterator.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGVIterator.html
        """

    def AtEnd(self) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.propgrid.PGVIterator.html
        """

    def GetProperty(self) -> 'propgrid.PGProperty':
        """ wx.propgrid.PGProperty

            Source: https://docs.wxpython.org/wx.propgrid.PGVIterator.html
        """

    def Next(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGVIterator.html
        """

    def UnRef(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGVIterator.html
        """

    Property: 'propgrid.PGProperty'  # See GetProperty



class PGPropArgCls:
    """  Overloaded Implementations:

        Source: https://docs.wxpython.org/wx.propgrid.PGPropArgCls.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGPropArgCls.html
        """

    def GetName(self) -> str:
        """ string

            Source: https://docs.wxpython.org/wx.propgrid.PGPropArgCls.html
        """

    def GetPtr(self, *args, **kw) -> 'propgrid.PGProperty':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PGPropArgCls.html
        """

    def GetPtr0(self) -> 'propgrid.PGProperty':
        """ wx.propgrid.PGProperty

            Source: https://docs.wxpython.org/wx.propgrid.PGPropArgCls.html
        """

    def HasName(self) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.propgrid.PGPropArgCls.html
        """

    Name: str  # See GetName
    Ptr: 'propgrid.PGProperty'  # See GetPtr
    Ptr0: 'propgrid.PGProperty'  # See GetPtr0



class PropertyGridHitTestResult:
    """ Returns column hit.

        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridHitTestResult.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridHitTestResult.html
        """

    def GetColumn(self) -> int:
        """ Returns column hit.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridHitTestResult.html
        """

    def GetProperty(self) -> 'propgrid.PGProperty':
        """ Returns property hit.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridHitTestResult.html
        """

    def GetSplitter(self) -> int:
        """ Returns index of splitter hit, -1 for none.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridHitTestResult.html
        """

    def GetSplitterHitOffset(self) -> int:
        """ If splitter hit, then this member function returns offset to the exact splitter position.

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridHitTestResult.html
        """

    Column: int  # See GetColumn
    Property: 'propgrid.PGProperty'  # See GetProperty
    Splitter: int  # See GetSplitter
    SplitterHitOffset: int  # See GetSplitterHitOffset



PG_ITERATE_PROPERTIES: int

PG_ITERATE_HIDDEN: int

PG_ITERATE_FIXED_CHILDREN: int

PG_ITERATE_CATEGORIES: int

PG_ITERATE_ALL_PARENTS: int

PG_ITERATE_ALL_PARENTS_RECURSIVELY: int

PG_ITERATOR_FLAGS_ALL: int

PG_ITERATOR_MASK_OP_ITEM: int

PG_ITERATOR_MASK_OP_PARENT: int

PG_ITERATE_VISIBLE: int

PG_ITERATE_ALL: int

PG_ITERATE_NORMAL: int

class PropertyGridIterator(PropertyGridIteratorBase):
    """  Overloaded Implementations:

        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridIterator.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridIterator.html
        """



class PGAttributeStorage:
    """ PGAttributeStorage is somewhat optimized storage for key=variant
pairs (i.e.

        Source: https://docs.wxpython.org/wx.propgrid.PGAttributeStorage.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGAttributeStorage.html
        """

    def FindValue(self, name: str) -> 'propgrid.PGVariant':
        """ name (string) â

            Source: https://docs.wxpython.org/wx.propgrid.PGAttributeStorage.html
        """

    def GetCount(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.propgrid.PGAttributeStorage.html
        """

    def Set(self, name, value) -> None:
        """ name (string) â

            Source: https://docs.wxpython.org/wx.propgrid.PGAttributeStorage.html
        """

    Count: int  # See GetCount



class PGChoiceAndButtonEditor(PGChoiceEditor):
    """ Instantiates editor controls.

        Source: https://docs.wxpython.org/wx.propgrid.PGChoiceAndButtonEditor.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceAndButtonEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'propgrid.PGWindowList':
        """ Instantiates editor controls.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceAndButtonEditor.html
        """

    def GetName(self) -> str:
        """ Returns pointer to the name of the editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceAndButtonEditor.html
        """

    Name: str  # See GetName



class PGComboBoxEditor(PGChoiceEditor):
    """ Instantiates editor controls.

        Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'propgrid.PGWindowList':
        """ Instantiates editor controls.

            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    def GetName(self) -> str:
        """ Returns pointer to the name of the editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    def GetValueFromControl(self, variant, property, ctrl) -> bool:
        """ Returns value from control, via parameter variant.

            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    def OnEvent(self, propgrid, property, wnd_primary, event) -> bool:
        """ Handles events.

            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    def OnFocus(self, property, wnd) -> None:
        """ Extra processing when control gains focus.

            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    def UpdateControl(self, property, ctrl) -> None:
        """ Loads value from property to the control.

            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    Name: str  # See GetName



class PGSpinCtrlEditor(PGTextCtrlEditor):
    """ Instantiates editor controls.

        Source: https://docs.wxpython.org/wx.propgrid.PGSpinCtrlEditor.html
    """
    def CreateControls(self, propgrid, property, pos, size) -> 'propgrid.PGWindowList':
        """ Instantiates editor controls.

            Source: https://docs.wxpython.org/wx.propgrid.PGSpinCtrlEditor.html
        """

    def GetName(self) -> str:
        """ Returns pointer to the name of the editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGSpinCtrlEditor.html
        """

    def OnEvent(self, propgrid, property, wnd_primary, event) -> bool:
        """ Handles events.

            Source: https://docs.wxpython.org/wx.propgrid.PGSpinCtrlEditor.html
        """

    Name: str  # See GetName



class PGTextCtrlAndButtonEditor(PGTextCtrlEditor):
    """ Instantiates editor controls.

        Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlAndButtonEditor.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlAndButtonEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'propgrid.PGWindowList':
        """ Instantiates editor controls.

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlAndButtonEditor.html
        """

    def GetName(self) -> str:
        """ Returns pointer to the name of the editor.

            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlAndButtonEditor.html
        """

    Name: str  # See GetName



class PGChoicesData(ObjectRefData):
    """ data (wx.propgrid.PGChoicesData) â 

        Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
        """

    def Clear(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
        """

    def CopyDataFrom(self, data: 'propgrid.PGChoicesData') -> None:
        """ data (wx.propgrid.PGChoicesData) â

            Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
        """

    def GetCount(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
        """

    def Insert(self, index, item) -> 'propgrid.PGChoiceEntry':
        """ index (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
        """

    def Item(self, i: int) -> 'propgrid.PGChoiceEntry':
        """ i (int) â

            Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
        """

    Count: int  # See GetCount



class PGDefaultRenderer(PGCellRenderer):
    """ Default cell renderer, that can handles the common scenarios.

        Source: https://docs.wxpython.org/wx.propgrid.PGDefaultRenderer.html
    """
    def GetImageSize(self, property, column, item) -> 'Size':
        """ Returns size of the image in front of the editable area.

            Source: https://docs.wxpython.org/wx.propgrid.PGDefaultRenderer.html
        """

    def Render(self, dc, rect, propertyGrid, property, column, item, flags) -> bool:
        """ Returns True if rendered something in the foreground (text or bitmap.

            Source: https://docs.wxpython.org/wx.propgrid.PGDefaultRenderer.html
        """



PGVariant: TypeAlias = Any

byte: TypeAlias = bytes

ArrayPGProperty: TypeAlias = list['PGProperty']

FlagType: TypeAlias = int  # Enumeration

