# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

from ...adv import PropertySheetDialog
from .. import (Bitmap, BitmapType, Char, Choice, Colour, ColourData,
                ComboCtrl, Command, CommandProcessor, Control, Cursor,
                DataFormat, DataObjectSimple, DateTime, Dialog, Event, Font,
                HtmlListBox, ImageList, Menu, NotifyEvent, Object,
                PageSetupDialogData, Panel, Point, Position, PrintData,
                Printout, Rect, Size, TextAttr, TextPos, VisualAttributes,
                Window, _Bitmap, _Colour, _CommandProcessor, _Font, _ImageList,
                _PrintData, _Rect, _Size)

class RichTextCtrl(Control):
    """ RichTextCtrl provides a generic, ground-up implementation of a text
control capable of showing multiple styles and images.

        Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def AddImage(self, image: 'Image') -> 'RichTextRange':
        """ Adds an image to the controlâs buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def AddParagraph(self, text: str) -> 'RichTextRange':
        """ Adds a new paragraph of text to the end of the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def AppendText(self, text: str) -> None:
        """ Sets the insertion point to the end of the buffer and writes the text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyAlignmentToSelection(self, alignment: int) -> bool:
        """ Applies the given alignment to the selection or the default style (undoable).

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyBoldToSelection(self) -> bool:
        """ Apples bold to the selection or the default style (undoable).

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyItalicToSelection(self) -> bool:
        """ Applies italic to the selection or the default style (undoable).

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyStyle(self, styleDef: 'richtext.RichTextStyleDefinition') -> bool:
        """ Applies the style sheet to the buffer, matching paragraph styles in the sheet against named styles in the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyStyleSheet(self, styleSheet: Optional['richtext.RichTextStyleSheet']=None) -> bool:
        """ Applies the style sheet to the buffer, for example if the styles have changed.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyTextEffectToSelection(self, flags: int) -> bool:
        """ Applies one or more TextAttrEffects flags to the selection (undoable).

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyUnderlineToSelection(self) -> bool:
        """ Applies underline to the selection or the default style (undoable).

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def AutoComplete(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def AutoCompleteDirectories(self) -> bool:
        """ Call this function to enable auto-completion of the text using the file system directories.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def AutoCompleteFileNames(self) -> bool:
        """ Call this function to enable auto-completion of the text typed in a single-line text control using all valid file system paths.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BatchingUndo(self) -> bool:
        """ Returns True if undo commands are being batched.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginAlignment(self, alignment: int) -> bool:
        """ Begins using alignment.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginBatchUndo(self, cmdName: str) -> bool:
        """ Starts batching undo history for commands.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginBold(self) -> bool:
        """ Begins using bold.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginCharacterStyle(self, characterStyle: str) -> bool:
        """ Begins using the named character style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginFont(self, font: 'Font') -> bool:
        """ Begins using this font.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginFontSize(self, pointSize: int) -> bool:
        """ Begins using the given point size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginItalic(self) -> bool:
        """ Begins using italic.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginLeftIndent(self, leftIndent, leftSubIndent=0) -> bool:
        """ Begins applying a left indent and subindent in tenths of a millimetre.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginLineSpacing(self, lineSpacing: int) -> bool:
        """ Begins applying line spacing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginListStyle(self, listStyle, level=1, number=1) -> bool:
        """ Begins using a specified list style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginNumberedBullet(self, bulletNumber, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_ARABIC|TEXT_ATTR_BULLET_STYLE_PERIOD) -> bool:
        """ Begins a numbered bullet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginParagraphSpacing(self, before, after) -> bool:
        """ Begins paragraph spacing; pass the before-paragraph and after-paragraph spacing in tenths of a millimetre.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginParagraphStyle(self, paragraphStyle: str) -> bool:
        """ Begins applying the named paragraph style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginRightIndent(self, rightIndent: int) -> bool:
        """ Begins a right indent, specified in tenths of a millimetre.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginStandardBullet(self, bulletName, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_STANDARD) -> bool:
        """ Begins applying a symbol bullet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginStyle(self, style: 'richtext.RichTextAttr') -> bool:
        """ Begins applying a style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginSuppressUndo(self) -> bool:
        """ Starts suppressing undo history for commands.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginSymbolBullet(self, symbol, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_SYMBOL) -> bool:
        """ Begins applying a symbol bullet, using a character from the current font.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginTextColour(self, colour: Union[int, str, 'Colour']) -> bool:
        """ Begins using this colour.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginURL(self, url, characterStyle="") -> bool:
        """ Begins applying wx.TEXT_ATTR_URL to the content.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginUnderline(self) -> bool:
        """ Begins using underlining.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanCopy(self) -> bool:
        """ Returns True if selected content can be copied to the clipboard.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanCut(self) -> bool:
        """ Returns True if selected content can be copied to the clipboard and deleted.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanDeleteRange(self, container, range) -> bool:
        """ Can we delete this range? Sends an event to the control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanDeleteSelection(self) -> bool:
        """ Returns True if selected content can be deleted.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanEditProperties(self, obj: 'richtext.RichTextObject') -> bool:
        """ Returns True if we can edit the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanInsertContent(self, container, pos) -> bool:
        """ Can we insert content at this position? Sends an event to the control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanPaste(self) -> bool:
        """ Returns True if the clipboard content can be pasted to the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanRedo(self) -> bool:
        """ Returns True if there is a command in the command history that can be redone.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanUndo(self) -> bool:
        """ Returns True if there is a command in the command history that can be undone.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ChangeValue(self, value: str) -> None:
        """ Sets the new text control value.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Clear(self) -> None:
        """ Clears the buffer content, leaving a single empty paragraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    @staticmethod
    def ClearAvailableFontNames() -> None:
        """ Clears the cache of available font names.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ClearListStyle(self, range, flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool:
        """ Clears the list style from the given range, clearing list-related attributes and applying any named paragraph style associated with each paragraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Command(self, event: 'CommandEvent') -> None:
        """ Sends the event to the control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Copy(self) -> None:
        """ Copies the selected content (if any) to the clipboard.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Create(self, parent, id=-1, value="", pos=DefaultPosition, size=DefaultSize, style=RE_MULTILINE, validator=DefaultValidator, name=TextCtrlNameStr) -> bool:
        """ Creates the underlying window.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Cut(self) -> None:
        """ Copies the selected content (if any) to the clipboard and deletes the selection.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Delete(self, range: 'richtext.RichTextRange') -> bool:
        """ Deletes the content within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DeleteSelectedContent(self, newPos=None) -> None:
        """ Deletes content if there is a selection, e.g.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DeleteSelection(self) -> None:
        """ Deletes the content in the selection, if any.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DiscardEdits(self) -> None:
        """ Sets the bufferâs modified status to False, and clears the bufferâs command history.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoGetBestSize(self) -> 'Size':
        """ Currently this simply returns    wx.Size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoGetValue(self) -> str:
        """ string

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoLayoutBuffer(self, buffer, dc, context, rect, parentRect, flags) -> None:
        """ Implements layout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoLoadFile(self, file, fileType) -> bool:
        """ Helper function for LoadFile .

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoSaveFile(self, file="", fileType=RICHTEXT_TYPE_ANY) -> bool:
        """ Helper function for SaveFile .

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoThaw(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoWriteText(self, value, flags=0) -> None:
        """ value (string) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoesSelectionHaveTextEffectFlag(self, flag: int) -> bool:
        """ Returns True if all of the selection, or the content at the current caret position, has the supplied TextAttrEffects flag(s).

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EditProperties(self, obj, parent) -> bool:
        """ Edits the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EnableDelayedImageLoading(self, b: bool) -> None:
        """ Enable or disable delayed image loading.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EnableImages(self, b: bool) -> None:
        """ Enable or disable images.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EnableVerticalScrollbar(self, enable: bool) -> None:
        """ Enable or disable the vertical scrollbar.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EnableVirtualAttributes(self, b: bool) -> None:
        """ Pass True to let the control use virtual attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndAlignment(self) -> bool:
        """ Ends alignment.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndAllStyles(self) -> bool:
        """ Ends application of all styles in the current style stack.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndBatchUndo(self) -> bool:
        """ Ends batching undo command history.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndBold(self) -> bool:
        """ Ends using bold.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndCharacterStyle(self) -> bool:
        """ Ends application of a named character style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndFont(self) -> bool:
        """ Ends using a font.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndFontSize(self) -> bool:
        """ Ends using a point size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndItalic(self) -> bool:
        """ Ends using italic.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndLeftIndent(self) -> bool:
        """ Ends left indent.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndLineSpacing(self) -> bool:
        """ Ends line spacing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndListStyle(self) -> bool:
        """ Ends using a specified list style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndNumberedBullet(self) -> bool:
        """ Ends application of a numbered bullet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndParagraphSpacing(self) -> bool:
        """ Ends paragraph spacing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndParagraphStyle(self) -> bool:
        """ Ends application of a named paragraph style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndRightIndent(self) -> bool:
        """ Ends right indent.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndStandardBullet(self) -> bool:
        """ Begins applying a standard bullet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndStyle(self) -> bool:
        """ Ends the current style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndSuppressUndo(self) -> bool:
        """ Ends suppressing undo command history.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndSymbolBullet(self) -> bool:
        """ Ends applying a symbol bullet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndTextColour(self) -> bool:
        """ Ends applying a text colour.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndURL(self) -> bool:
        """ Ends applying a URL.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndUnderline(self) -> bool:
        """ End applying underlining.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ExtendCellSelection(self, table, noRowSteps, noColSteps) -> bool:
        """ Extends a table selection in the given direction.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ExtendSelection(self, oldPosition, newPosition, flags) -> bool:
        """ Helper function for extending the selection, returning True if the selection was changed.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def FindCaretPositionForCharacterPosition(self, position, hitTestFlags, container, caretLineStart) -> int:
        """ Find the caret position for the combination of hit-test flags and character position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def FindContainerAtPoint(self, pt, position, hit, hitObj, flags=0) -> 'RichTextParagraphLayoutBox':
        """ Finds the container at the given point, which is assumed to be in client coordinates.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def FindNextWordPosition(self, direction: int=1) -> int:
        """ Helper function for finding the caret position for the next word.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def FindRangeForList(self, pos, isNumberedList) -> 'RichTextRange':
        """ Given a character position at which there is a list style, find the range encompassing the same list style by looking backwards and forwards.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ForceDelayedLayout(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ForceUpper(self) -> None:
        """ Convert all text entered into the control to upper case.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetAdjustedCaretPosition(self, caretPos: int) -> int:
        """ The adjusted caret position is the character position adjusted to take into account whether weâre at the start of a paragraph, in which case style information should be taken from the next position, not current one.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    @staticmethod
    def GetAvailableFontNames() -> list[str]:
        """ Font names take a long time to retrieve, so cache them (on demand).

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetBasicStyle(self) -> 'RichTextAttr':
        """ Gets the basic (overall) style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetBuffer(self) -> 'RichTextBuffer':
        """ Returns the buffer associated with the control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetCaretAtLineStart(self) -> bool:
        """ Returns True if we are showing the caret position at the start of a line instead of at the end of the previous one.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetCaretPosition(self) -> int:
        """ Returns the current caret position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetCaretPositionForDefaultStyle(self) -> int:
        """ Returns the caret position since the default formatting was changed.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetCaretPositionForIndex(self, position, rect, container=None) -> None:
        """ Returns the caret height and position for the given character position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetCommandProcessor(self) -> 'CommandProcessor':
        """ Gets the command processor associated with the controlâs buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetContextMenu(self) -> 'Menu':
        """ Returns the current context menu.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetContextMenuPropertiesInfo(self) -> 'RichTextContextMenuPropertiesInfo':
        """ Returns an object that stores information about context menu property item(s), in order to communicate between the context menu event handler and the code that responds to it.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDefaultStyleEx(self) -> 'RichTextAttr':
        """ Returns the current default style, which can be used to change how subsequently inserted text is displayed.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDelayedImageLoading(self) -> bool:
        """ Returns True if delayed image loading is enabled.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDelayedImageProcessingRequired(self) -> bool:
        """ Gets the flag indicating that delayed image processing is required.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDelayedImageProcessingTime(self) -> int:
        """ Returns the last time delayed image processing was performed.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDelayedLayoutThreshold(self) -> int:
        """ Gets the size of the buffer beyond which layout is delayed during resizing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDimensionScale(self) -> float:
        """ Returns the scale factor for displaying certain dimensions such as indentation and inter-paragraph spacing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDragStartPoint(self) -> 'Point':
        """ Get the possible DragânâDrop start point.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDragStartTime(self) -> 'DateTime':
        """ Get the possible DragânâDrop start time.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDragging(self) -> bool:
        """ Returns True if we are extending a selection.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFilename(self) -> str:
        """ Gets the current filename associated with the control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFirstVisiblePoint(self) -> 'Point':
        """ Returns the first visible point in the window.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFirstVisiblePosition(self) -> int:
        """ Returns the first visible position in the current view.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFocusObject(self) -> 'RichTextParagraphLayoutBox':
        """ Returns the   wx.richtext.RichTextObject  object that currently has the editing focus.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFontScale(self) -> float:
        """ Returns the scale factor for displaying fonts, for example for more comfortable editing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFullLayoutRequired(self) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFullLayoutSavedPosition(self) -> int:
        """ long

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFullLayoutTime(self) -> int:
        """ long

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetHandlerFlags(self) -> int:
        """ Returns flags that change the behaviour of loading or saving.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetHint(self) -> str:
        """ Returns the current hint string.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetImagesEnabled(self) -> bool:
        """ Returns True if images are enabled.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetInsertionPoint(self) -> int:
        """ Returns the current insertion point.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetInternalSelectionRange(self) -> 'RichTextRange':
        """ Returns the selection range in character positions.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetLastPosition(self) -> 'TextPos':
        """ Returns the last position in the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetLineLength(self, lineNo: int) -> int:
        """ Returns the length of the specified line in characters.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetLineText(self, lineNo: int) -> str:
        """ Returns the text for the given line.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetLogicalPoint(self, ptPhysical: Union[tuple[int, int], 'Point']) -> 'Point':
        """ Transforms physical window position to logical (unscrolled) position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetMargins(self) -> 'Point':
        """ Returns the margins used by the control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetNumberOfLines(self) -> int:
        """ Returns the number of lines in the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetPhysicalPoint(self, ptLogical: Union[tuple[int, int], 'Point']) -> 'Point':
        """ Transforms logical (unscrolled) position to physical window position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetPreDrag(self) -> bool:
        """ Are we trying to start DragânâDrop?

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetPropertiesMenuLabel(self, obj: 'richtext.RichTextObject') -> str:
        """ Gets the objectâs properties menu label.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetRange(self, from_, to_) -> str:
        """ Gets the text for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetScale(self) -> float:
        """ Returns an overall scale factor for displaying and editing the content.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetScaledPoint(self, pt: Union[tuple[int, int], 'Point']) -> 'Point':
        """ Returns a scaled point.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetScaledRect(self, rect: 'Rect') -> 'Rect':
        """ Returns a scaled rectangle.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetScaledSize(self, sz: Union[tuple[int, int], 'Size']) -> 'Size':
        """ Returns a scaled size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetSelection(self) -> 'RichTextSelection':
        """ Returns the range of the current selection.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetSelectionAnchor(self) -> int:
        """ Returns an anchor so we know how to extend the selection.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetSelectionAnchorObject(self) -> 'RichTextObject':
        """ Returns the anchor object if selecting multiple containers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetSelectionRange(self) -> 'RichTextRange':
        """ Returns the selection range in character positions.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetStringSelection(self) -> str:
        """ Returns the text within the current selection range, if any.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetStyle(self, *args, **kw) -> None:
        """ Gets the attributes at the given position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetStyleForRange(self, *args, **kw) -> None:
        """ Gets the attributes common to the specified range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ Returns the style sheet associated with the control, if any.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetTextCursor(self) -> 'Cursor':
        """ Returns the text (normal) cursor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetURLCursor(self) -> 'Cursor':
        """ Returns the cursor to be used over URLs.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetUncombinedStyle(self, *args, **kw) -> None:
        """ Gets the attributes at the given position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetUnscaledPoint(self, pt: Union[tuple[int, int], 'Point']) -> 'Point':
        """ Returns an unscaled point.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetUnscaledRect(self, rect: 'Rect') -> 'Rect':
        """ Returns an unscaled rectangle.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetUnscaledSize(self, sz: Union[tuple[int, int], 'Size']) -> 'Size':
        """ Returns an unscaled size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetValue(self) -> str:
        """ Returns the content of the entire control as a string.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetVerticalScrollbarEnabled(self) -> bool:
        """ Returns True if the vertical scrollbar is enabled.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetVirtualAttributesEnabled(self) -> bool:
        """ Returns True if this control can use virtual attributes and virtual text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetVisibleLineForCaretPosition(self, caretPosition: int) -> 'RichTextLine':
        """ Internal helper function returning the line for the visible caret position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def HasCharacterAttributes(self, range, style) -> bool:
        """ Test if this whole range has character attributes of the specified kind.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def HasParagraphAttributes(self, range, style) -> bool:
        """ Test if this whole range has paragraph attributes of the specified kind.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def HasSelection(self) -> bool:
        """ Returns True if there is a selection and the object containing the selection was the same as the current focus object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def HasUnfocusedSelection(self) -> bool:
        """ Returns True if there was a selection, whether or not the current focus object is the same as the selectionâs container object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def HitTest(self, pt: Union[tuple[int, int], 'Point']) -> tuple:
        """ Finds the character at the given position in pixels.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def HitTestXY(self, pt: Union[tuple[int, int], 'Point']) -> tuple:
        """ Finds the character at the given position in pixels.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Init(self) -> None:
        """ Initialises the members of the control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Invalidate(self) -> None:
        """ Invalidates the whole buffer to trigger painting later.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsDefaultStyleShowing(self) -> bool:
        """ Returns True if the user has recently set the default style without moving the caret, and therefore the UI needs to reflect the default style and not the style at the caret.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsEditable(self) -> bool:
        """ Returns True if the control is editable.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsEmpty(self) -> bool:
        """ Returns True if the control is currently empty.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsModified(self) -> bool:
        """ Returns True if the buffer has been modified.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsMultiLine(self) -> bool:
        """ Returns True if the control is multiline.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsPositionVisible(self, pos: int) -> bool:
        """ Returns True if the given position is visible on the screen.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsSelectionAligned(self, alignment: int) -> bool:
        """ Returns True if all of the selection is aligned according to the specified flag.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsSelectionBold(self) -> bool:
        """ Returns True if all of the selection, or the content at the caret position, is bold.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsSelectionItalics(self) -> bool:
        """ Returns True if all of the selection, or the content at the caret position, is italic.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsSelectionUnderlined(self) -> bool:
        """ Returns True if all of the selection, or the content at the caret position, is underlined.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsSingleLine(self) -> bool:
        """ Returns True if the control is single-line.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def KeyboardNavigate(self, keyCode, flags) -> bool:
        """ Helper function implementing keyboard navigation.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def LayoutContent(self, onlyVisibleRect: bool=False) -> bool:
        """ Lays out the buffer, which must be done before certain operations, such as setting the caret position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def LineBreak(self) -> bool:
        """ Inserts a line break at the current insertion point.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def LoadFile(self, file, type=RICHTEXT_TYPE_ANY) -> bool:
        """ Loads content into the controlâs buffer using the given type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MarkDirty(self) -> None:
        """ Marks the buffer as modified.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveCaret(self, pos, showAtLineStart=False, container=None) -> bool:
        """ Move the caret to the given character position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveCaretBack(self, oldPosition: int) -> None:
        """ Move the caret one visual step forward: this may mean setting a flag and keeping the same position if weâre going from the end of one line to the start of the next, which may be the exact same caret position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveCaretForward(self, oldPosition: int) -> None:
        """ Move the caret one visual step forward: this may mean setting a flag and keeping the same position if weâre going from the end of one line to the start of the next, which may be the exact same caret position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveDown(self, noLines=1, flags=0) -> bool:
        """ Moves the caret down.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveEnd(self, flags: int=0) -> bool:
        """ Moves to the end of the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveHome(self, flags: int=0) -> bool:
        """ Moves to the start of the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveLeft(self, noPositions=1, flags=0) -> bool:
        """ Moves left.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveRight(self, noPositions=1, flags=0) -> bool:
        """ Moves right.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveToLineEnd(self, flags: int=0) -> bool:
        """ Moves to the end of the line.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveToLineStart(self, flags: int=0) -> bool:
        """ Moves to the start of the line.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveToParagraphEnd(self, flags: int=0) -> bool:
        """ Moves to the end of the paragraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveToParagraphStart(self, flags: int=0) -> bool:
        """ Moves to the start of the paragraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveUp(self, noLines=1, flags=0) -> bool:
        """ Moves to the start of the paragraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Newline(self) -> bool:
        """ Inserts a new paragraph at the current insertion point.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def NumberList(self, *args, **kw) -> bool:
        """ Numbers the paragraphs in the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnCaptureLost(self, event: 'MouseCaptureLostEvent') -> None:
        """ event (wx.MouseCaptureLostEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnChar(self, event: 'KeyEvent') -> None:
        """ event (wx.KeyEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnClear(self, event: 'CommandEvent') -> None:
        """ Standard handler for the wx.ID_CLEAR command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnContextMenu(self, event: 'ContextMenuEvent') -> None:
        """ Shows a standard context menu with undo, redo, cut, copy, paste, clear, and select all commands.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnCopy(self, event: 'CommandEvent') -> None:
        """ Standard handler for the wx.ID_COPY command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnCut(self, event: 'CommandEvent') -> None:
        """ Standard handler for the wx.ID_CUT command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnDropFiles(self, event: 'DropFilesEvent') -> None:
        """ Loads the first dropped file.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnEraseBackground(self, event: 'EraseEvent') -> None:
        """ event (wx.EraseEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnIdle(self, event: 'IdleEvent') -> None:
        """ event (wx.IdleEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnKillFocus(self, event: 'FocusEvent') -> None:
        """ event (wx.FocusEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnLeftClick(self, event: 'MouseEvent') -> None:
        """ event (wx.MouseEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnLeftDClick(self, event: 'MouseEvent') -> None:
        """ event (wx.MouseEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnLeftUp(self, event: 'MouseEvent') -> None:
        """ event (wx.MouseEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnMiddleClick(self, event: 'MouseEvent') -> None:
        """ event (wx.MouseEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnMoveMouse(self, event: 'MouseEvent') -> None:
        """ event (wx.MouseEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnPaint(self, event: 'PaintEvent') -> None:
        """ event (wx.PaintEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnPaste(self, event: 'CommandEvent') -> None:
        """ Standard handler for the wx.ID_PASTE command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnProperties(self, event: 'CommandEvent') -> None:
        """ Standard handler for property commands.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnRedo(self, event: 'CommandEvent') -> None:
        """ Standard handler for the wx.ID_REDO command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnRightClick(self, event: 'MouseEvent') -> None:
        """ event (wx.MouseEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnScroll(self, event: 'ScrollWinEvent') -> None:
        """ event (wx.ScrollWinEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnSelectAll(self, event: 'CommandEvent') -> None:
        """ Standard handler for the wx.ID_SELECTALL command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnSetFocus(self, event: 'FocusEvent') -> None:
        """ event (wx.FocusEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ event (wx.SizeEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnSysColourChanged(self, event: 'SysColourChangedEvent') -> None:
        """ event (wx.SysColourChangedEvent) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnTimer(self, event: 'TimerEvent') -> None:
        """ Respond to timer events.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUndo(self, event: 'CommandEvent') -> None:
        """ Standard handler for the wx.ID_UNDO command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateClear(self, event: 'UpdateUIEvent') -> None:
        """ Standard update handler for the wx.ID_CLEAR command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateCopy(self, event: 'UpdateUIEvent') -> None:
        """ Standard update handler for the wx.ID_COPY command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateCut(self, event: 'UpdateUIEvent') -> None:
        """ Standard update handler for the wx.ID_CUT command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdatePaste(self, event: 'UpdateUIEvent') -> None:
        """ Standard update handler for the wx.ID_PASTE command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateProperties(self, event: 'UpdateUIEvent') -> None:
        """ Standard update handler for property commands.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateRedo(self, event: 'UpdateUIEvent') -> None:
        """ Standard update handler for the wx.ID_REDO command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateSelectAll(self, event: 'UpdateUIEvent') -> None:
        """ Standard update handler for the wx.ID_SELECTALL command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateUndo(self, event: 'UpdateUIEvent') -> None:
        """ Standard update handler for the wx.ID_UNDO command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PageDown(self, noPages=1, flags=0) -> bool:
        """ Moves one or more pages down.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PageUp(self, noPages=1, flags=0) -> bool:
        """ Moves one or more pages up.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PaintAboveContent(self, WXUNUSED: 'DC') -> None:
        """ Other user defined painting after everything else (i.e. all text) is painted.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PaintBackground(self, dc: 'DC') -> None:
        """ Paints the background.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Paste(self) -> None:
        """ Pastes content from the clipboard to the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PopStyleSheet(self) -> 'RichTextStyleSheet':
        """ Pops the style sheet from top of stack.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PositionCaret(self, container: Optional['richtext.RichTextParagraphLayoutBox']=None) -> None:
        """ Internal function to position the visible caret according to the current caret position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PositionToXY(self, pos: int) -> tuple:
        """ Converts a text position to zero-based column and line numbers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PrepareContent(self, container: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ Prepares the content just before insertion (or after buffer reset).

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PrepareContextMenu(self, menu, pt, addPropertyCommands) -> int:
        """ Prepares the context menu, optionally adding appropriate property-editing commands.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ProcessBackKey(self, event, flags) -> bool:
        """ Processes the back key.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ProcessDelayedImageLoading(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ProcessMouseMovement(self, container, obj, position, pos) -> bool:
        """ Processes mouse movement in order to change the cursor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PromoteList(self, *args, **kw) -> bool:
        """ Promotes or demotes the paragraphs in the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PushStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> bool:
        """ Push the style sheet to top of stack.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Redo(self) -> None:
        """ Redoes the current command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def RefreshForSelectionChange(self, oldSelection, newSelection) -> bool:
        """ Refreshes the area affected by a selection change.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Remove(self, from_, to_) -> None:
        """ Removes the content in the specified range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Replace(self, from_, to_, value) -> None:
        """ Replaces the content in the specified range with the string specified by value.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def RequestDelayedImageProcessing(self) -> None:
        """ Request delayed image processing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SaveFile(self, file="", type=RICHTEXT_TYPE_ANY) -> bool:
        """ Saves the buffer content using the given type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ScrollIntoView(self, position, keyCode) -> bool:
        """ Scrolls position  into view.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SelectAll(self) -> None:
        """ Selects all the text in the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SelectNone(self) -> None:
        """ Cancels any selection.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SelectWord(self, position: int) -> bool:
        """ Selects the word at the given character position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetAndShowDefaultStyle(self, attr: 'richtext.RichTextAttr') -> None:
        """ Sets attr  as the default style and tells the control that the UI should reflect this attribute until the user moves the caret.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetBasicStyle(self, style: 'richtext.RichTextAttr') -> None:
        """ Sets the basic (overall) style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetCaretAtLineStart(self, atStart: bool) -> None:
        """ Sets a flag to remember that we are showing the caret position at the start of a line instead of at the end of the previous one.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetCaretPosition(self, position, showAtLineStart=False) -> None:
        """ Sets the caret position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetCaretPositionAfterClick(self, container, position, hitTestFlags, extendSelection=False) -> bool:
        """ Sets up the caret for the given position and container, after a mouse click.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetCaretPositionForDefaultStyle(self, pos: int) -> None:
        """ Set the caret position for the default style that the user is selecting.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetContextMenu(self, menu: 'Menu') -> None:
        """ Sets the current context menu.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDefaultStyle(self, *args, **kw) -> bool:
        """ Sets the current default style, which can be used to change how subsequently inserted text is displayed.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDefaultStyleToCursorStyle(self) -> bool:
        """ Sets the default style to the style under the cursor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDelayedImageProcessingRequired(self, b: bool) -> None:
        """ Sets the flag indicating that delayed image processing is required.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDelayedImageProcessingTime(self, t: int) -> None:
        """ Sets the last time delayed image processing was performed.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDelayedLayoutThreshold(self, threshold: int) -> None:
        """ Sets the size of the buffer beyond which layout is delayed during resizing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDimensionScale(self, dimScale, refresh=False) -> None:
        """ Sets the scale factor for displaying certain dimensions such as indentation and inter-paragraph spacing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDragStartPoint(self, sp: Union[tuple[int, int], 'Point']) -> None:
        """ Set the possible DragânâDrop start point.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDragStartTime(self, st: 'DateTime') -> None:
        """ Set the possible DragânâDrop start time.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDragging(self, dragging: bool) -> None:
        """ Sets a flag to remember if we are extending a selection.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetEditable(self, editable: bool) -> None:
        """ Makes the control editable, or not.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFilename(self, filename: str) -> None:
        """ Sets the current filename.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFocusObject(self, obj, setCaretPosition=True) -> bool:
        """ Sets the   wx.richtext.RichTextObject  object that currently has the editing focus.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFont(self, font: 'Font') -> bool:
        """ Sets the font, and also the basic and default attributes (see wx.richtext.RichTextCtrl.SetDefaultStyle ).

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFontScale(self, fontScale, refresh=False) -> None:
        """ Sets the scale factor for displaying fonts, for example for more comfortable editing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFullLayoutRequired(self, b: bool) -> None:
        """ b (bool) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFullLayoutSavedPosition(self, p: int) -> None:
        """ p (long) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFullLayoutTime(self, t: int) -> None:
        """ t (long) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetHandlerFlags(self, flags: int) -> None:
        """ Sets flags that change the behaviour of loading or saving.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetHint(self, hint: str) -> bool:
        """ Sets a hint shown in an empty unfocused text control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetInsertionPoint(self, pos: int) -> None:
        """ Sets the insertion point and causes the current editing style to be taken from the new position (unlike wx.richtext.RichTextCtrl.SetCaretPosition ).

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetInsertionPointEnd(self) -> None:
        """ Sets the insertion point to the end of the text control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetInternalSelectionRange(self, range: 'richtext.RichTextRange') -> None:
        """ Sets the selection range in character positions.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetListStyle(self, *args, **kw) -> bool:
        """ Sets the list attributes for the given range, passing flags to determine how the attributes are set.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetMargins(self, *args, **kw) -> None:
        """ Attempts to set the control margins.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetMaxLength(self, len: int) -> None:
        """ Sets the maximum number of characters that may be entered in a single line text control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetModified(self, modified: bool) -> None:
        """ modified (bool) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetPreDrag(self, pd: bool) -> None:
        """ Set if weâre trying to start DragânâDrop.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetProperties(self, range, properties, flags=RICHTEXT_SETPROPERTIES_WITH_UNDO) -> bool:
        """ Sets the properties for the given range, passing flags to determine how the attributes are set.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetScale(self, scale, refresh=False) -> None:
        """ Sets an overall scale factor for displaying and editing the content.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetSelection(self, *args, **kw) -> None:
        """ Sets the selection to the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetSelectionAnchor(self, anchor: int) -> None:
        """ Sets an anchor so we know how to extend the selection.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetSelectionAnchorObject(self, anchor: 'richtext.RichTextObject') -> None:
        """ Sets the anchor object if selecting multiple containers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetSelectionRange(self, range: 'richtext.RichTextRange') -> None:
        """ Sets the selection to the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetStyle(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetStyleEx(self, range, style, flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool:
        """ Sets the attributes for the given range, passing flags to determine how the attributes are set.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> None:
        """ Sets the style sheet associated with the control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetTextCursor(self, cursor: 'Cursor') -> None:
        """ Sets the text (normal) cursor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetURLCursor(self, cursor: 'Cursor') -> None:
        """ Sets the cursor to be used over URLs.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetValue(self, value: str) -> None:
        """ Replaces existing content with the given text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetupScrollbars(self, atTop: bool=False) -> None:
        """ A helper function setting up scrollbars, for example after a resize.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ShouldInheritColours(self) -> bool:
        """ Return True from here to allow the colours of this window to be changed by InheritAttributes .

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ShowContextMenu(self, menu, pt, addPropertyCommands) -> bool:
        """ Shows the given context menu, optionally adding appropriate property-editing commands for the current position in the object hierarchy.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ShowPosition(self, pos: int) -> None:
        """ Scrolls the buffer so that the given position is in view.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def StartCellSelection(self, table, newCell) -> bool:
        """ Starts selecting table cells.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def StoreFocusObject(self, obj: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ Setter for m_focusObject.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SuppressingUndo(self) -> bool:
        """ Returns True if undo history suppression is on.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Undo(self) -> None:
        """ Undoes the command at the top of the command history, if there is one.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WordLeft(self, noPages=1, flags=0) -> bool:
        """ Moves a number of words to the left.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WordRight(self, noPages=1, flags=0) -> bool:
        """ Move a number of words to the right.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WriteField(*args, **kwargs) -> 'RichTextField':
        """ Writes a field at the current insertion point.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WriteImage(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WriteTable(*args, **kwargs) -> 'RichTextTable':
        """ Write a table at the current insertion point, returning the table.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WriteText(self, text: str) -> None:
        """ Writes text at the current position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WriteTextBox(*args, **kwargs) -> 'RichTextBox':
        """ Write a text box at the current insertion point, returning the text box.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def XYToPosition(self, x, y) -> int:
        """ Translates from column and line number to position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    BasicStyle: 'RichTextAttr'  # See GetBasicStyle and SetBasicStyle
    Buffer: 'RichTextBuffer'  # See GetBuffer
    CaretAtLineStart: bool  # See GetCaretAtLineStart and SetCaretAtLineStart
    CaretPosition: int  # See GetCaretPosition and SetCaretPosition
    CaretPositionForDefaultStyle: int  # See GetCaretPositionForDefaultStyle and SetCaretPositionForDefaultStyle
    CommandProcessor: '_CommandProcessor'  # See GetCommandProcessor
    ContextMenu: 'Menu'  # See GetContextMenu and SetContextMenu
    ContextMenuPropertiesInfo: 'RichTextContextMenuPropertiesInfo'  # See GetContextMenuPropertiesInfo
    DefaultStyle: Any  # See GetDefaultStyle and SetDefaultStyle
    DefaultStyleEx: 'RichTextAttr'  # See GetDefaultStyleEx
    DelayedImageLoading: bool  # See GetDelayedImageLoading
    DelayedImageProcessingRequired: bool  # See GetDelayedImageProcessingRequired and SetDelayedImageProcessingRequired
    DelayedImageProcessingTime: int  # See GetDelayedImageProcessingTime and SetDelayedImageProcessingTime
    DelayedLayoutThreshold: int  # See GetDelayedLayoutThreshold and SetDelayedLayoutThreshold
    DimensionScale: float  # See GetDimensionScale and SetDimensionScale
    DragStartPoint: 'Point'  # See GetDragStartPoint and SetDragStartPoint
    DragStartTime: 'DateTime'  # See GetDragStartTime and SetDragStartTime
    Dragging: bool  # See GetDragging and SetDragging
    Filename: str  # See GetFilename and SetFilename
    FirstVisiblePoint: 'Point'  # See GetFirstVisiblePoint
    FirstVisiblePosition: int  # See GetFirstVisiblePosition
    FocusObject: 'RichTextParagraphLayoutBox'  # See GetFocusObject and SetFocusObject
    FontScale: float  # See GetFontScale and SetFontScale
    FullLayoutRequired: bool  # See GetFullLayoutRequired and SetFullLayoutRequired
    FullLayoutSavedPosition: int  # See GetFullLayoutSavedPosition and SetFullLayoutSavedPosition
    FullLayoutTime: int  # See GetFullLayoutTime and SetFullLayoutTime
    HandlerFlags: int  # See GetHandlerFlags and SetHandlerFlags
    Hint: str  # See GetHint and SetHint
    ImagesEnabled: bool  # See GetImagesEnabled
    InsertionPoint: int  # See GetInsertionPoint and SetInsertionPoint
    InternalSelectionRange: 'RichTextRange'  # See GetInternalSelectionRange and SetInternalSelectionRange
    LastPosition: 'TextPos'  # See GetLastPosition
    Margins: 'Point'  # See GetMargins and SetMargins
    NumberOfLines: int  # See GetNumberOfLines
    PreDrag: bool  # See GetPreDrag and SetPreDrag
    Scale: float  # See GetScale and SetScale
    Selection: 'RichTextSelection'  # See GetSelection and SetSelection
    SelectionAnchor: int  # See GetSelectionAnchor and SetSelectionAnchor
    SelectionAnchorObject: 'RichTextObject'  # See GetSelectionAnchorObject and SetSelectionAnchorObject
    SelectionRange: 'RichTextRange'  # See GetSelectionRange and SetSelectionRange
    StringSelection: str  # See GetStringSelection
    StyleSheet: 'RichTextStyleSheet'  # See GetStyleSheet and SetStyleSheet
    TextCursor: 'Cursor'  # See GetTextCursor and SetTextCursor
    URLCursor: 'Cursor'  # See GetURLCursor and SetURLCursor
    Value: str  # See GetValue and SetValue
    VerticalScrollbarEnabled: bool  # See GetVerticalScrollbarEnabled
    VirtualAttributesEnabled: bool  # See GetVirtualAttributesEnabled



RE_CENTRE_CARET: int  # The control will try to keep the caret line centred vertically while editing. wx.richtext.RE_CENTER_CARET is a synonym for this style.

RE_MULTILINE: int  # The control will be multiline (mandatory).

RE_READONLY: int  # The control will not be editable. ^^

RE_CENTER_CARET: int

TEXT_ATTR_URL: int

ID_CLEAR: int

ID_COPY: int

ID_CUT: int

ID_PASTE: int

ID_REDO: int

ID_SELECTALL: int

ID_UNDO: int

RICHTEXT_SETSTYLE_WITH_UNDO: int

RICHTEXT_TYPE_ANY: int

RICHTEXT_SETSTYLE_RENUMBER: int

RICHTEXT_SETSTYLE_SPECIFY_LEVEL: int

RICHTEXT_SETPROPERTIES_WITH_UNDO: int

RICHTEXT_SETPROPERTIES_PARAGRAPHS_ONLY: int

RICHTEXT_SETPROPERTIES_CHARACTERS_ONLY: int

RICHTEXT_SETPROPERTIES_RESET: int

RICHTEXT_SETPROPERTIES_REMOVE: int

RICHTEXT_SETSTYLE_NONE: int

RICHTEXT_SETSTYLE_OPTIMIZE: int

RICHTEXT_SETSTYLE_PARAGRAPHS_ONLY: int

RICHTEXT_SETSTYLE_CHARACTERS_ONLY: int

RICHTEXT_SETSTYLE_RESET: int

RICHTEXT_SETSTYLE_REMOVE: int

class RichTextStyleComboCtrl(ComboCtrl):
    """ This is a combo control that can display the styles in a
RichTextStyleSheet, and apply the selection to an associated
RichTextCtrl.

        Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ Creates the windows.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    def GetRichTextCtrl(self) -> 'RichTextCtrl':
        """ Returns the   wx.richtext.RichTextCtrl  associated with this control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ Returns the style sheet associated with this control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    def SetRichTextCtrl(self, ctrl: 'richtext.RichTextCtrl') -> None:
        """ Associates the control with a   wx.richtext.RichTextCtrl.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    def SetStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> None:
        """ Associates the control with a style sheet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    def UpdateStyles(self) -> None:
        """ Updates the combo control from the associated style sheet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    RichTextCtrl: 'RichTextCtrl'  # See GetRichTextCtrl and SetRichTextCtrl
    StyleSheet: 'RichTextStyleSheet'  # See GetStyleSheet and SetStyleSheet



class RichTextCommand(Command):
    """ Implements a command on the undo/redo stack.

        Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
        """

    def AddAction(self, action: 'richtext.RichTextAction') -> None:
        """ Adds an action to the action list.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
        """

    def ClearActions(self) -> None:
        """ Clears the action list.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
        """

    def Do(self) -> bool:
        """ Performs the command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
        """

    def GetActions(self) -> 'RichTextActionList':
        """ Returns the action list.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
        """

    def Undo(self) -> bool:
        """ Undoes the command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
        """

    Actions: 'RichTextActionList'  # See GetActions



class RichTextStyleListCtrl(Control):
    """ This class incorporates a RichTextStyleListBox and a choice control
that allows the user to select the category of style to view.

        Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Constructors.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ Creates the windows.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def GetRichTextCtrl(self) -> 'RichTextCtrl':
        """ Returns the associated rich text control, if any.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def GetStyleChoice(self) -> 'Choice':
        """ Returns the   wx.Choice  control used for selecting the style category.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def GetStyleListBox(self) -> 'RichTextStyleListBox':
        """ Returns the   wx.ListBox  control used to view the style list.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ Returns the associated style sheet, if any.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def GetStyleType(self) -> 'wxRichTextStyleType':
        """ Returns the type of style to show in the list box.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def SetRichTextCtrl(self, ctrl: 'richtext.RichTextCtrl') -> None:
        """ Associates the control with a   wx.richtext.RichTextCtrl.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def SetStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> None:
        """ Associates the control with a style sheet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def SetStyleType(self, styleType: RichTextStyleListBox.wxRichTextStyleType) -> None:
        """ Sets the style type to display.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def UpdateStyles(self) -> None:
        """ Updates the style list box.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    RichTextCtrl: 'RichTextCtrl'  # See GetRichTextCtrl and SetRichTextCtrl
    StyleChoice: 'Choice'  # See GetStyleChoice
    StyleListBox: 'RichTextStyleListBox'  # See GetStyleListBox
    StyleSheet: 'RichTextStyleSheet'  # See GetStyleSheet and SetStyleSheet
    StyleType: 'wxRichTextStyleType'  # See GetStyleType and SetStyleType



RICHTEXTSTYLELIST_HIDE_TYPE_SELECTOR: int  # This style hides the category selection control. ^^

class RichTextBufferDataObject(DataObjectSimple):
    """ Implements a rich text data object for clipboard transfer.

        Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
    """
    def __init__(self, richTextBuffer: Optional['richtext.RichTextBuffer']=None) -> None:
        """ The constructor doesnât copy the pointer, so it shouldnât go away while this object is alive.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    def GetDataHere(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    def GetDataSize(self, *args, **kw) -> int:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    def GetPreferredFormat(self, dir: int) -> 'DataFormat':
        """ Returns the preferred format for either rendering the data (if dir  is  Get , its default value) or for setting it.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    def GetRichTextBuffer(self) -> 'RichTextBuffer':
        """ After a call to this function, the buffer is owned by the caller and it is responsible for deleting it.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    @staticmethod
    def GetRichTextBufferFormatId() -> 'Char':
        """ Returns the id for the new data format.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    def SetData(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    DataSize: int  # See GetDataSize
    RichTextBuffer: 'RichTextBuffer'  # See GetRichTextBuffer



class RichTextStyleOrganiserDialog(Dialog):
    """ This class shows a style sheet and allows the user to edit, add and
remove styles.

        Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def ApplyStyle(self, ctrl: Optional['richtext.RichTextCtrl']=None) -> bool:
        """ Applies the selected style to selection in the given control or the control passed to the constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def Create(*args, **kwargs) -> bool:
        """ Creates the dialog.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def GetFlags(self) -> int:
        """ Returns the flags used to control the interface presented to the user.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def GetRestartNumbering(self) -> bool:
        """ Returns True if the user has opted to restart numbering.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def GetRichTextCtrl(self) -> 'RichTextCtrl':
        """ Returns the associated rich text control (if any).

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def GetSelectedStyle(self) -> str:
        """ Returns selected style name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def GetSelectedStyleDefinition(self) -> 'RichTextStyleDefinition':
        """ Returns selected style definition.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ Returns the associated style sheet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def SetFlags(self, flags: int) -> None:
        """ Sets the flags used to control the interface presented to the user.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def SetRestartNumbering(self, restartNumbering: bool) -> None:
        """ Checks or unchecks the restart numbering checkbox.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def SetRichTextCtrl(self, ctrl: 'richtext.RichTextCtrl') -> None:
        """ Sets the control to be associated with the dialog, for the purposes of applying a style to the selection.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    @staticmethod
    def SetShowToolTips(show: bool) -> None:
        """ Determines whether tooltips will be shown.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def SetStyleSheet(self, sheet: 'richtext.RichTextStyleSheet') -> None:
        """ Sets the associated style sheet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    Flags: int  # See GetFlags and SetFlags
    RestartNumbering: bool  # See GetRestartNumbering and SetRestartNumbering
    RichTextCtrl: 'RichTextCtrl'  # See GetRichTextCtrl and SetRichTextCtrl
    SelectedStyle: str  # See GetSelectedStyle
    SelectedStyleDefinition: 'RichTextStyleDefinition'  # See GetSelectedStyleDefinition
    StyleSheet: 'RichTextStyleSheet'  # See GetStyleSheet and SetStyleSheet



RICHTEXT_ORGANISER_DELETE_STYLES: int

RICHTEXT_ORGANISER_CREATE_STYLES: int

RICHTEXT_ORGANISER_APPLY_STYLES: int

RICHTEXT_ORGANISER_EDIT_STYLES: int

RICHTEXT_ORGANISER_RENAME_STYLES: int

RICHTEXT_ORGANISER_OK_CANCEL: int

OK: int

RICHTEXT_ORGANISER_RENUMBER: int

RICHTEXT_ORGANISER_SHOW_CHARACTER: int

RICHTEXT_ORGANISER_SHOW_PARAGRAPH: int

RICHTEXT_ORGANISER_SHOW_LIST: int

RICHTEXT_ORGANISER_SHOW_ALL: int

RICHTEXT_ORGANISER_ORGANISE: int

RICHTEXT_ORGANISER_BROWSE: int

RICHTEXT_ORGANISER_BROWSE_NUMBERING: int

class SymbolPickerDialog(Dialog):
    """ SymbolPickerDialog presents the user with a choice of fonts and a
grid of available characters.

        Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def Create(*args, **kwargs) -> bool:
        """ Creation: see the constructor  for details about the parameters.

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def GetFontName(self) -> str:
        """ Returns the font name (the font reflected in the font list).

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def GetFromUnicode(self) -> bool:
        """ Returns True if the dialog is showing the full range of Unicode characters.

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def GetNormalTextFontName(self) -> str:
        """ Gets the font name used for displaying symbols in the absence of a selected font.

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def GetSymbol(self) -> str:
        """ Gets the current or initial symbol as a string.

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def GetSymbolChar(self) -> int:
        """ Gets the selected symbol character as an integer.

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def HasSelection(self) -> bool:
        """ Returns True if a symbol is selected.

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def SetFontName(self, value: str) -> None:
        """ Sets the initial/selected font name.

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def SetFromUnicode(self, value: bool) -> None:
        """ Sets the internal flag indicating that the full Unicode range should be displayed.

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def SetNormalTextFontName(self, value: str) -> None:
        """ Sets the name of the font to be used in the absence of a selected font.

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def SetSymbol(self, value: str) -> None:
        """ Sets the symbol as a one or zero character string.

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def SetUnicodeMode(self, unicodeMode: bool) -> None:
        """ Sets Unicode display mode.

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def UseNormalFont(self) -> bool:
        """ Returns True if the has specified normal text - that is, there is no selected font.

            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    FontName: str  # See GetFontName and SetFontName
    FromUnicode: bool  # See GetFromUnicode and SetFromUnicode
    NormalTextFontName: str  # See GetNormalTextFontName and SetNormalTextFontName
    Symbol: str  # See GetSymbol and SetSymbol
    SymbolChar: int  # See GetSymbolChar



class RichTextEvent(NotifyEvent):
    """ This is the event class for RichTextCtrl notifications.

        Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def Clone(self) -> 'Event':
        """ Returns a copy of the event.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetCharacter(self) -> 'Char':
        """ Returns the character pressed, within a  wxEVT_RICHTEXT_CHARACTER   event.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetContainer(self) -> 'RichTextParagraphLayoutBox':
        """ Returns the container for which the event is relevant.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetFlags(self) -> int:
        """ Returns flags indicating modifier keys pressed.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetNewStyleSheet(self) -> 'RichTextStyleSheet':
        """ Returns the new style sheet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetOldContainer(self) -> 'RichTextParagraphLayoutBox':
        """ Returns the old container, for a focus change event.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetOldStyleSheet(self) -> 'RichTextStyleSheet':
        """ Returns the old style sheet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetPosition(self) -> int:
        """ Returns the buffer position at which the event occurred.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetRange(self) -> 'RichTextRange':
        """ Gets the range for the current operation.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetCharacter(self, ch: 'Char') -> None:
        """ Sets the character variable.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetContainer(self, container: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ Sets the container for which the event is relevant.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetFlags(self, flags: int) -> None:
        """ Sets flags indicating modifier keys pressed.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetNewStyleSheet(self, sheet: 'richtext.RichTextStyleSheet') -> None:
        """ Sets the new style sheet variable.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetOldContainer(self, container: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ Sets the old container, for a focus change event.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetOldStyleSheet(self, sheet: 'richtext.RichTextStyleSheet') -> None:
        """ Sets the old style sheet variable.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetPosition(self, pos: int) -> None:
        """ Sets the buffer position variable.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetRange(self, range: 'richtext.RichTextRange') -> None:
        """ Sets the range variable.

            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    Character: 'Char'  # See GetCharacter and SetCharacter
    Container: 'RichTextParagraphLayoutBox'  # See GetContainer and SetContainer
    Flags: int  # See GetFlags and SetFlags
    NewStyleSheet: 'RichTextStyleSheet'  # See GetNewStyleSheet and SetNewStyleSheet
    OldContainer: 'RichTextParagraphLayoutBox'  # See GetOldContainer and SetOldContainer
    OldStyleSheet: 'RichTextStyleSheet'  # See GetOldStyleSheet and SetOldStyleSheet
    Position: int  # See GetPosition and SetPosition
    Range: 'RichTextRange'  # See GetRange and SetRange



EVT_RICHTEXT_LEFT_CLICK: int  # Process a  wxEVT_RICHTEXT_LEFT_CLICK   event, generated when the user releases the left mouse button over an object.

EVT_RICHTEXT_RIGHT_CLICK: int  # Process a  wxEVT_RICHTEXT_RIGHT_CLICK   event, generated when the user releases the right mouse button over an object.

EVT_RICHTEXT_MIDDLE_CLICK: int  # Process a  wxEVT_RICHTEXT_MIDDLE_CLICK   event, generated when the user releases the middle mouse button over an object.

EVT_RICHTEXT_LEFT_DCLICK: int  # Process a  wxEVT_RICHTEXT_LEFT_DCLICK   event, generated when the user double-clicks an object.

EVT_RICHTEXT_RETURN: int  # Process a  wxEVT_RICHTEXT_RETURN   event, generated when the user presses the return key. Valid event functions: GetFlags, GetPosition.

EVT_RICHTEXT_CHARACTER: int  # Process a  wxEVT_RICHTEXT_CHARACTER   event, generated when the user presses a character key. Valid event functions: GetFlags, GetPosition, GetCharacter.

EVT_RICHTEXT_CONSUMING_CHARACTER: int  # Process a  wxEVT_RICHTEXT_CONSUMING_CHARACTER   event, generated when the user presses a character key but before it is processed and inserted into the control. Call Veto to prevent normal processing. Valid event functions: GetFlags, GetPosition, GetCharacter, Veto.

EVT_RICHTEXT_DELETE: int  # Process a  wxEVT_RICHTEXT_DELETE   event, generated when the user presses the backspace or delete key. Valid event functions: GetFlags, GetPosition.

EVT_RICHTEXT_STYLE_CHANGED: int  # Process a  wxEVT_RICHTEXT_STYLE_CHANGED   event, generated when styling has been applied to the control. Valid event functions: GetPosition, GetRange.

EVT_RICHTEXT_STYLESHEET_CHANGED: int  # Process a  wxEVT_RICHTEXT_STYLESHEET_CHANGING   event, generated when the controlâs stylesheet has changed, for example the user added, edited or deleted a style. Valid event functions: GetRange, GetPosition.

EVT_RICHTEXT_STYLESHEET_REPLACING: int  # Process a  wxEVT_RICHTEXT_STYLESHEET_REPLACING   event, generated when the controlâs stylesheet is about to be replaced, for example when a file is loaded into the control. Valid event functions: Veto, GetOldStyleSheet, GetNewStyleSheet.

EVT_RICHTEXT_STYLESHEET_REPLACED: int  # Process a  wxEVT_RICHTEXT_STYLESHEET_REPLACED   event, generated when the controlâs stylesheet has been replaced, for example when a file is loaded into the control. Valid event functions: GetOldStyleSheet, GetNewStyleSheet.

EVT_RICHTEXT_PROPERTIES_CHANGED: int  # Process a  wxEVT_RICHTEXT_PROPERTIES_CHANGED   event, generated when properties have been applied to the control. Valid event functions: GetPosition, GetRange.

EVT_RICHTEXT_CONTENT_INSERTED: int  # Process a  wxEVT_RICHTEXT_CONTENT_INSERTED   event, generated when content has been inserted into the control. Valid event functions: GetPosition, GetRange.

EVT_RICHTEXT_CONTENT_DELETED: int  # Process a  wxEVT_RICHTEXT_CONTENT_DELETED   event, generated when content has been deleted from the control. Valid event functions: GetPosition, GetRange.

EVT_RICHTEXT_BUFFER_RESET: int  # Process a  wxEVT_RICHTEXT_BUFFER_RESET   event, generated when the buffer has been reset by deleting all content. You can use this to set a default style for the first new paragraph.

EVT_RICHTEXT_SELECTION_CHANGED: int  # Process a  wxEVT_RICHTEXT_SELECTION_CHANGED   event, generated when the selection range has changed.

EVT_RICHTEXT_FOCUS_OBJECT_CHANGED: int  # Process a  wxEVT_RICHTEXT_FOCUS_OBJECT_CHANGED   event, generated when the current focus object has changed. ^^

class RichTextAction(Object):
    """ Implements a part of a command.

        Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
    """
    def __init__(self, cmd, name, id, buffer, container, ctrl, ignoreFirstTime=False) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def ApplyParagraphs(self, fragment: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ Replaces the buffer paragraphs with the given fragment.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def CalculateRefreshOptimizations(self, optimizationLineCharPositions, optimizationLineYPositions, oldFloatRect) -> None:
        """ Calculate arrays for refresh optimization.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def Do(self) -> bool:
        """ Performs the action.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetAttributes(self) -> 'RichTextAttr':
        """ Returns the attributes, for single-object commands.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetContainer(self) -> 'RichTextParagraphLayoutBox':
        """ Returns the container that this action refers to, using the container address and top-level buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetContainerAddress(self) -> 'RichTextObjectAddress':
        """ Returns the address (nested position) of the container within the buffer being manipulated.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetIgnoreFirstTime(self) -> bool:
        """ Returns True if the first Do   command should be skipped as itâs already been applied.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetName(self) -> str:
        """ Returns the action name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetNewParagraphs(self) -> 'RichTextParagraphLayoutBox':
        """ Returns the new fragments.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetObject(self) -> 'RichTextObject':
        """ Returns the object to replace the one at the position defined by the container address and the actionâs range start position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetOldParagraphs(self) -> 'RichTextParagraphLayoutBox':
        """ Returns the old fragments.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetPosition(self) -> int:
        """ Returns the position used for e.g.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetRange(self) -> 'RichTextRange':
        """ Returns the range for e.g.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def MakeObject(self, obj: 'richtext.RichTextObject') -> None:
        """ Makes an address from the given object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def SetContainerAddress(self, *args, **kw) -> None:
        """ Sets the address (nested position) of the container within the buffer being manipulated.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def SetIgnoreFirstTime(self, b: bool) -> None:
        """ Instructs the first Do   command should be skipped as itâs already been applied.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def SetObject(self, obj: 'richtext.RichTextObject') -> None:
        """ Sets the object to replace the one at the position defined by the container address and the actionâs range start position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def SetOldAndNewObjects(self, oldObj, newObj) -> None:
        """ Sets the existing and new objects, for use with wx.richtext.RICHTEXT_CHANGE_OBJECT.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def SetPosition(self, pos: int) -> None:
        """ Sets the position used for e.g.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def SetRange(self, range: 'richtext.RichTextRange') -> None:
        """ Sets the range for e.g.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def StoreObject(self, obj: 'richtext.RichTextObject') -> None:
        """ Stores the object to replace the one at the position defined by the container address without making an address for it.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def Undo(self) -> bool:
        """ Undoes the action.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def UpdateAppearance(*args, **kwargs) -> None:
        """ Updates the control appearance, optimizing if possible given information from the call to Layout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    Attributes: 'RichTextAttr'  # See GetAttributes
    Container: 'RichTextParagraphLayoutBox'  # See GetContainer
    ContainerAddress: 'RichTextObjectAddress'  # See GetContainerAddress and SetContainerAddress
    IgnoreFirstTime: bool  # See GetIgnoreFirstTime and SetIgnoreFirstTime
    Name: str  # See GetName
    NewParagraphs: 'RichTextParagraphLayoutBox'  # See GetNewParagraphs
    Object: 'RichTextObject'  # See GetObject and SetObject
    OldParagraphs: 'RichTextParagraphLayoutBox'  # See GetOldParagraphs
    Position: int  # See GetPosition and SetPosition
    Range: 'RichTextRange'  # See GetRange and SetRange



RICHTEXT_CHANGE_OBJECT: int

class RichTextDrawingContext(Object):
    """ A class for passing information to drawing and measuring functions.

        Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
    """
    def __init__(self, buffer: 'richtext.RichTextBuffer') -> None:
        """ Pass the buffer to the context so the context can retrieve information such as virtual attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def ApplyVirtualAttributes(self, attr, obj) -> bool:
        """ Applies any virtual attributes relevant to this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def EnableDelayedImageLoading(self, b: bool) -> None:
        """ Enable or disable delayed image loading.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def EnableImages(self, b: bool) -> None:
        """ Enable or disable images.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def EnableVirtualAttributes(self, b: bool) -> None:
        """ Enables virtual attribute processing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetDelayedImageLoading(self) -> bool:
        """ Returns True if delayed image loading is enabled.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetImagesEnabled(self) -> bool:
        """ Returns True if images are enabled.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetLayingOut(self) -> bool:
        """ Returns True if laying out.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetVirtualAttributes(self, obj: 'richtext.RichTextObject') -> 'RichTextAttr':
        """ Returns the virtual attributes for this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetVirtualAttributesEnabled(self) -> bool:
        """ Returns True if virtual attribute processing is enabled.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetVirtualSubobjectAttributes(self, obj, positions, attributes) -> int:
        """ Gets the mixed virtual attributes for individual positions within the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetVirtualSubobjectAttributesCount(self, obj: 'richtext.RichTextObject') -> int:
        """ Gets the count for mixed virtual attributes for individual positions within the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetVirtualText(self, obj, text) -> bool:
        """ Gets the virtual text for this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def HasVirtualAttributes(self, obj: 'richtext.RichTextObject') -> bool:
        """ Does this object have virtual attributes? Virtual attributes can be provided for visual cues without affecting the actual styling.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def HasVirtualText(self, obj: 'richtext.RichTextPlainText') -> bool:
        """ Do we have virtual text for this object? Virtual text allows an application to replace characters in an object for editing and display purposes, for example for highlighting special characters.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def Init(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def SetLayingOut(self, b: bool) -> None:
        """ Set laying out flag.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    DelayedImageLoading: bool  # See GetDelayedImageLoading
    ImagesEnabled: bool  # See GetImagesEnabled
    LayingOut: bool  # See GetLayingOut and SetLayingOut
    VirtualAttributesEnabled: bool  # See GetVirtualAttributesEnabled
    m_buffer: Any  # A public C++ attribute of type RichTextBuffer     .
    m_enableDelayedImageLoading: Any  # A public C++ attribute of type bool.
    m_enableImages: Any  # A public C++ attribute of type bool.
    m_enableVirtualAttributes: Any  # A public C++ attribute of type bool.
    m_layingOut: Any  # A public C++ attribute of type bool.



class RichTextDrawingHandler(Object):
    """ The base class for custom drawing handlers.

        Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
    """
    def __init__(self, name: str="") -> None:
        """ Creates a drawing handler object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def GetName(self) -> str:
        """ Returns the name of the handler.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def GetVirtualAttributes(self, attr, obj) -> bool:
        """ Provides virtual attributes that we can provide.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def GetVirtualSubobjectAttributes(self, obj, positions, attributes) -> int:
        """ Gets the mixed virtual attributes for individual positions within the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def GetVirtualSubobjectAttributesCount(self, obj: 'richtext.RichTextObject') -> int:
        """ Gets the count for mixed virtual attributes for individual positions within the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def GetVirtualText(self, obj, text) -> bool:
        """ Gets the virtual text for this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def HasVirtualAttributes(self, obj: 'richtext.RichTextObject') -> bool:
        """ Returns True if this object has virtual attributes that we can provide.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def HasVirtualText(self, obj: 'richtext.RichTextPlainText') -> bool:
        """ Do we have virtual text for this object? Virtual text allows an application to replace characters in an object for editing and display purposes, for example for highlighting special characters.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def SetName(self, name: str) -> None:
        """ Sets the name of the handler.

            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    Name: str  # See GetName and SetName



class RichTextFieldType(Object):
    """ The base class for custom field types.

        Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def CanEditProperties(self, obj: 'richtext.RichTextField') -> bool:
        """ Returns True if we can edit the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def Copy(self, fieldType: 'richtext.RichTextFieldType') -> None:
        """ fieldType (wx.richtext.RichTextFieldType) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def Draw(self, obj, dc, context, range, selection, rect, descent, style) -> bool:
        """ Draw the item, within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def EditProperties(self, obj, parent, buffer) -> bool:
        """ Edits the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def GetName(self) -> str:
        """ Returns the field type name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def GetPropertiesMenuLabel(self, obj: 'richtext.RichTextField') -> str:
        """ Returns the label to be used for the properties context menu item.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ Returns the object size for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def IsTopLevel(self, obj: 'richtext.RichTextField') -> bool:
        """ Returns True if this object is top-level, i.e. contains its own paragraphs, such as a text box.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def Layout(self, obj, dc, context, rect, parentRect, style) -> bool:
        """ Lay the item out at the specified position with the given size constraint.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def SetName(self, name: str) -> None:
        """ Sets the field type name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def UpdateField(self, buffer, obj) -> bool:
        """ Update the field.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    Name: str  # See GetName and SetName



class RichTextFileHandler(Object):
    """ The base class for file handlers.

        Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
    """
    def __init__(self, name="", ext="", type=0) -> None:
        """ Creates a file handler object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def CanHandle(self, filename: str) -> bool:
        """ Returns True if we handle this filename (if using files).

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def CanLoad(self) -> bool:
        """ Returns True if we can load using this handler.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def CanSave(self) -> bool:
        """ Returns True if we can save using this handler.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def DoLoadFile(self, buffer, stream) -> bool:
        """ Override to load content from stream  into buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def DoSaveFile(self, buffer, stream) -> bool:
        """ Override to save content to stream  from buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def GetEncoding(self) -> str:
        """ Returns the encoding to use when saving a file.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def GetExtension(self) -> str:
        """ Returns the default extension to recognise.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def GetFlags(self) -> int:
        """ Returns flags controlling how loading and saving is done.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def GetName(self) -> str:
        """ Returns the name of the handler.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def GetType(self) -> int:
        """ Returns the handler type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def IsVisible(self) -> bool:
        """ Returns True if this handler should be visible to the user.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def LoadFile(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SaveFile(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SetEncoding(self, encoding: str) -> None:
        """ Sets the encoding to use when saving a file.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SetExtension(self, ext: str) -> None:
        """ Sets the default extension to recognise.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SetFlags(self, flags: int) -> None:
        """ Sets flags that change the behaviour of loading or saving.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SetName(self, name: str) -> None:
        """ Sets the name of the handler.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SetType(self, type: int) -> None:
        """ Sets the handler type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SetVisible(self, visible: bool) -> None:
        """ Sets whether the handler should be visible to the user (via the applicationâs load and save dialogs).

            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    Encoding: str  # See GetEncoding and SetEncoding
    Extension: str  # See GetExtension and SetExtension
    Flags: int  # See GetFlags and SetFlags
    Name: str  # See GetName and SetName
    Type: int  # See GetType and SetType



class RichTextFontTable(Object):
    """ Manages quick access to a pool of fonts for rendering rich text.

        Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """

    def Clear(self) -> None:
        """ Clears the font table.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """

    def FindFont(self, fontSpec: 'richtext.RichTextAttr') -> 'Font':
        """ Finds a font for the given attribute object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """

    def IsOk(self) -> bool:
        """ Returns True if the font table is valid.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """

    def SetFontScale(self, fontScale: float) -> None:
        """ Set the font scale factor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """

    def __ne__(self, item: Any) -> bool:
        """ Inequality operator.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """



class RichTextFormattingDialogFactory(Object):
    """ This class provides pages for RichTextFormattingDialog, and allows
other customization of the dialog.

        Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def CreateButtons(self, dialog: 'richtext.RichTextFormattingDialog') -> bool:
        """ Creates the main dialog buttons.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def CreatePage(self, page, title, dialog) -> 'Panel':
        """ Creates a page, given a page identifier.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def CreatePages(self, pages, dialog) -> bool:
        """ Creates all pages under the dialogâs book control, also calling AddPage().

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def GetPageId(self, i: int) -> int:
        """ Enumerate all available page identifiers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def GetPageIdCount(self) -> int:
        """ Gets the number of available page identifiers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def GetPageImage(self, id: int) -> int:
        """ Gets the image index for the given page identifier.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def SetSheetStyle(self, dialog: 'richtext.RichTextFormattingDialog') -> bool:
        """ Set the property sheet style, called at the start of wx.richtext.RichTextFormattingDialog.Create .

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def ShowHelp(self, page, dialog) -> bool:
        """ Invokes help for the dialog.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    PageIdCount: int  # See GetPageIdCount



class RichTextHeaderFooterData(Object):
    """ This class represents header and footer data to be passed to the
RichTextPrinting and RichTextPrintout classes.

        Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Constructors.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def Clear(self) -> None:
        """ Clears all text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def Copy(self, data: 'richtext.RichTextHeaderFooterData') -> None:
        """ Copies the data.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetFont(self) -> 'Font':
        """ Returns the font specified for printing the header and footer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetFooterMargin(self) -> int:
        """ Returns the margin between the text and the footer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetFooterText(self, page=RICHTEXT_PAGE_EVEN, location=RICHTEXT_PAGE_CENTRE) -> str:
        """ Returns the footer text on odd or even pages, and at a given position on the page (left, centre or right).

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetHeaderMargin(self) -> int:
        """ Returns the margin between the text and the header.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetHeaderText(self, page=RICHTEXT_PAGE_EVEN, location=RICHTEXT_PAGE_CENTRE) -> str:
        """ Returns the header text on odd or even pages, and at a given position on the page (left, centre or right).

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetShowOnFirstPage(self) -> bool:
        """ Returns True if the header and footer will be shown on the first page.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetText(self, headerFooter, page, location) -> str:
        """ Helper function for getting the header or footer text, odd or even pages, and at a given position on the page (left, centre or right).

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetTextColour(self) -> 'Colour':
        """ Returns the text colour for drawing the header and footer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def Init(self) -> None:
        """ Initialises the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the font for drawing the header and footer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetFooterText(self, text, page=RICHTEXT_PAGE_ALL, location=RICHTEXT_PAGE_CENTRE) -> None:
        """ Sets the footer text on odd or even pages, and at a given position on the page (left, centre or right).

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetHeaderText(self, text, page=RICHTEXT_PAGE_ALL, location=RICHTEXT_PAGE_CENTRE) -> None:
        """ Sets the header text on odd or even pages, and at a given position on the page (left, centre or right).

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetMargins(self, headerMargin, footerMargin) -> None:
        """ Sets the margins between text and header or footer, in tenths of a millimeter.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetShowOnFirstPage(self, showOnFirstPage: bool) -> None:
        """ Pass True to show the header or footer on first page (the default).

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetText(self, text, headerFooter, page, location) -> None:
        """ Helper function for setting the header or footer text, odd or even pages, and at a given position on the page (left, centre or right).

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetTextColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets the text colour for drawing the header and footer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    Font: '_Font'  # See GetFont and SetFont
    FooterMargin: int  # See GetFooterMargin
    FooterText: str  # See GetFooterText and SetFooterText
    HeaderMargin: int  # See GetHeaderMargin
    HeaderText: str  # See GetHeaderText and SetHeaderText
    ShowOnFirstPage: bool  # See GetShowOnFirstPage and SetShowOnFirstPage
    TextColour: 'Colour'  # See GetTextColour and SetTextColour



class RichTextImageBlock(Object):
    """ This class stores information about an image, in binary in-memory
form.

        Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def Clear(self) -> None:
        """ Clears the block.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def Copy(self, block: 'richtext.RichTextImageBlock') -> None:
        """ Copy from block.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def DoMakeImageBlock(self, image, imageType) -> bool:
        """ Makes the image block.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def GetData(self) -> int:
        """ Returns the raw data.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def GetDataSize(self) -> int:
        """ Returns the data size in bytes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def GetExtension(self) -> str:
        """ Gets the extension for the blockâs type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def GetImageType(self) -> 'BitmapType':
        """ Returns the image type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def Init(self) -> None:
        """ Initialises the block.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def IsOk(self) -> bool:
        """ Returns True if the data is not None.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def Load(self, image: 'Image') -> bool:
        """ image (wx.Image) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def MakeImageBlock(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def MakeImageBlockDefaultQuality(self, image, imageType) -> bool:
        """ Uses a    wx.Image  for efficiency, but canât set quality (only relevant for JPEG)

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def Ok(self) -> bool:
        """ bool

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    @staticmethod
    def ReadBlock(*args, **kw) -> int:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def ReadHex(self, stream, length, imageType) -> bool:
        """ Reads the data in hex from a stream.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def SetData(self, image: int) -> None:
        """ image (int) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def SetDataSize(self, size: int) -> None:
        """ Sets the data size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def SetImageType(self, imageType: BitmapType) -> None:
        """ Sets the image type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def Write(self, filename: str) -> bool:
        """ Writes the block to a file.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    @staticmethod
    def WriteBlock(*args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def WriteHex(self, stream: 'OutputStream') -> bool:
        """ Writes the data in hex to a stream.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    Data: int  # See GetData and SetData
    DataSize: int  # See GetDataSize and SetDataSize
    Extension: str  # See GetExtension
    ImageType: 'BitmapType'  # See GetImageType and SetImageType



class RichTextObject(Object):
    """ This is the base for drawable rich text objects.

        Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
    """
    def __init__(self, parent: Optional['richtext.RichTextObject']=None) -> None:
        """ Constructor, taking an optional parent pointer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def AcceptsFocus(self) -> bool:
        """ Returns True if objects of this class can accept the focus, i.e. a call to SetFocusObject is possible.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def AdjustAttributes(self, attr, context) -> bool:
        """ Adjusts the attributes for virtual attribute provision, collapsed borders, etc.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    @staticmethod
    def AdjustAvailableSpace(dc, buffer, parentAttr, childAttr, availableParentSpace, availableContainerSpace) -> 'Rect':
        """ Returns the rectangle which the child has available to it given restrictions specified in the child attribute, e.g.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def CalculateRange(self, start: int) -> None:
        """ Calculates the range of the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def CanEditProperties(self) -> bool:
        """ Returns True if we can edit the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def CanMerge(self, object, context) -> bool:
        """ Returns True if this object can merge itself with the given one.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def CanSplit(self, context: 'richtext.RichTextDrawingContext') -> bool:
        """ Returns True if this object can potentially be split, by virtue of having different virtual attributes for individual sub-objects.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Clone(self) -> 'RichTextObject':
        """ Clones the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def ConvertPixelsToTenthsMM(self, *args, **kw) -> int:
        """ Convert units in pixels to tenths of a millimetre.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def ConvertTenthsMMToPixels(self, *args, **kw) -> int:
        """ Converts units in tenths of a millimetre to device units.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Copy(self, obj: 'richtext.RichTextObject') -> None:
        """ Copies the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def DeleteRange(self, range: 'richtext.RichTextRange') -> bool:
        """ Deletes the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Dereference(self) -> None:
        """ Reference-counting allows us to use the same object in multiple lists (not yet used).

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def DoSplit(self, pos: int) -> 'RichTextObject':
        """ Do a split from pos, returning an object containing the second part, and setting the first part in âthisâ.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ Draw the item, within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    @staticmethod
    def DrawBorder(dc, buffer, attr, borders, rect, flags=0) -> bool:
        """ Draws a border.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    @staticmethod
    def DrawBoxAttributes(dc, buffer, attr, boxRect, flags=0, obj=None) -> bool:
        """ Draws the borders and background for the given rectangle and attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def EditProperties(self, parent, buffer) -> bool:
        """ Edits the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def FindPosition(self, dc, context, index, forceLineStart) -> tuple:
        """ Finds the absolute position and row height for the given character position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetAbsolutePosition(self) -> 'Point':
        """ Returns the absolute object position, by traversing up the child/parent hierarchy.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetAttributes(self) -> 'RichTextAttr':
        """ Returns the objectâs attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetAvailableContentArea(self, dc, context, outerRect) -> 'Rect':
        """ Calculates the available content space in the given rectangle, given the margins, border and padding specified in the objectâs attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetBestSize(self) -> 'Size':
        """ Returns the best size, i.e. the ideal starting size for this object irrespective of available space.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetBottomMargin(self) -> int:
        """ Returns the bottom margin of the object, in pixels.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    @staticmethod
    def GetBoxRects(dc, buffer, attr) -> tuple:
        """ Returns the various rectangles of the box model in pixels.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetBuffer(self) -> 'RichTextBuffer':
        """ Returns the containing buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetCachedSize(self) -> 'Size':
        """ Gets the cached object size as calculated by Layout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetContainer(self) -> 'RichTextParagraphLayoutBox':
        """ Returns the top-level container of this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetDescent(self) -> int:
        """ Returns the stored descent value.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetFloatDirection(self) -> int:
        """ Returns the floating direction.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetLeftMargin(self) -> int:
        """ Returns the left margin of the object, in pixels.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetMaxSize(self) -> 'Size':
        """ Gets the maximum object size as calculated by Layout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetMinSize(self) -> 'Size':
        """ Gets the minimum object size as calculated by Layout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetName(self) -> str:
        """ Returns the identifying name for this object from the properties, using the ânameâ key.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetNaturalSize(self) -> 'TextAttrSize':
        """ Gets the ânaturalâ size for an object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetOwnRange(self) -> 'RichTextRange':
        """ Returns the objectâs own range (valid if top-level).

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetOwnRangeIfTopLevel(self) -> 'RichTextRange':
        """ Returns the objectâs own range only if a top-level object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetParent(self) -> 'RichTextObject':
        """ Returns a pointer to the parent object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetParentContainer(self) -> 'RichTextParagraphLayoutBox':
        """ Returns the top-level container of this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetPosition(self) -> 'Point':
        """ Returns the object position in pixels.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetProperties(self) -> 'RichTextProperties':
        """ Returns the objectâs properties.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetPropertiesMenuLabel(self) -> str:
        """ Returns the label to be used for the properties context menu item.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetRange(self) -> 'RichTextRange':
        """ Returns the objectâs range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ Returns the object size for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetRect(self) -> 'Rect':
        """ Returns the rectangle enclosing the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetRightMargin(self) -> int:
        """ Returns the right margin of the object, in pixels.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetSelection(self, start, end) -> 'RichTextSelection':
        """ Returns a selection object specifying the selections between start and end character positions.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetTextForRange(self, range: 'richtext.RichTextRange') -> str:
        """ Returns any text in this object for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetTopMargin(self) -> int:
        """ Returns the top margin of the object, in pixels.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    @staticmethod
    def GetTotalMargin(dc, buffer, attr) -> tuple:
        """ Returns the total margin for the object in pixels, taking into account margin, padding and border size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetXMLNodeName(self) -> str:
        """ Returns the XML node name of this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def HandlesChildSelections(self) -> bool:
        """ Returns True if this object can handle the selections of its children, fOr example a table.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ Hit-testing: returns a flag indicating hit test details, plus information about position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def ImportFromXML(self, buffer, node, handler, recurse) -> bool:
        """ Imports this object from XML.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Invalidate(self, invalidRange: 'richtext.RichTextRange'=RICHTEXT_ALL) -> None:
        """ Invalidates the object at the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsAtomic(self) -> bool:
        """ Returns True if no user editing can be done inside the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsComposite(self) -> bool:
        """ Returns True if this object is composite.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsEmpty(self) -> bool:
        """ Returns True if the object is empty.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsFloatable(self) -> bool:
        """ Returns True if this class of object is floatable.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsFloating(self) -> bool:
        """ Returns True if this object is currently floating.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsShown(self) -> bool:
        """ Returns True if the object will be shown, False otherwise.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsTopLevel(self) -> bool:
        """ Returns True if this object is top-level, i.e. contains its own paragraphs, such as a text box.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ Lay the item out at the specified position with the given size constraint.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def LayoutToBestSize(self, dc, context, buffer, parentAttr, attr, availableParentSpace, availableContainerSpace, style) -> bool:
        """ Lays out the object first with a given amount of space, and then if no width was specified in attr, lays out the object again using the minimum size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Merge(self, object, context) -> bool:
        """ Returns True if this object merged itself with the given one.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Move(self, pt: Union[tuple[int, int], 'Point']) -> None:
        """ Moves the object recursively, by adding the offset from old to new.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Reference(self) -> None:
        """ Reference-counting allows us to use the same object in multiple lists (not yet used).

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetAttributes(self, attr: 'richtext.RichTextAttr') -> None:
        """ Sets the objectâs attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetCachedSize(self, sz: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the cached object size as calculated by Layout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetDescent(self, descent: int) -> None:
        """ Sets the stored descent value.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetMargins(self, *args, **kw) -> None:
        """ Set the margin around the object, in pixels.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetMaxSize(self, sz: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the maximum object size as calculated by Layout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetMinSize(self, sz: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the minimum object size as calculated by Layout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetName(self, name: str) -> None:
        """ Sets the identifying name for this object as a property using the ânameâ key.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetOwnRange(self, range: 'richtext.RichTextRange') -> None:
        """ Set the objectâs own range, for a top-level object with its own position space.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetParent(self, parent: 'richtext.RichTextObject') -> None:
        """ Sets the pointer to the parent object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetPosition(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ Sets the object position in pixels.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetProperties(self, props: 'richtext.RichTextProperties') -> None:
        """ Sets the objectâs properties.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetRange(self, range: 'richtext.RichTextRange') -> None:
        """ Sets the objectâs range within its container.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Show(self, show: bool) -> None:
        """ Call to show or hide this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Split(self, context: 'richtext.RichTextDrawingContext') -> 'RichTextObject':
        """ Returns the final object in the split objects if this object was split due to differences between sub-object virtual attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def UsesParagraphAttributes(self) -> bool:
        """ Returns True if this object takes note of paragraph attributes (text and image objects donât).

            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    AbsolutePosition: 'Point'  # See GetAbsolutePosition
    Attributes: 'RichTextAttr'  # See GetAttributes and SetAttributes
    BestSize: 'Size'  # See GetBestSize
    BottomMargin: int  # See GetBottomMargin
    Buffer: 'RichTextBuffer'  # See GetBuffer
    CachedSize: 'Size'  # See GetCachedSize and SetCachedSize
    Container: 'RichTextParagraphLayoutBox'  # See GetContainer
    Descent: int  # See GetDescent and SetDescent
    FloatDirection: int  # See GetFloatDirection
    LeftMargin: int  # See GetLeftMargin
    MaxSize: 'Size'  # See GetMaxSize and SetMaxSize
    MinSize: 'Size'  # See GetMinSize and SetMinSize
    Name: str  # See GetName and SetName
    NaturalSize: 'TextAttrSize'  # See GetNaturalSize
    OwnRange: 'RichTextRange'  # See GetOwnRange and SetOwnRange
    OwnRangeIfTopLevel: 'RichTextRange'  # See GetOwnRangeIfTopLevel
    Parent: 'RichTextObject'  # See GetParent and SetParent
    ParentContainer: 'RichTextParagraphLayoutBox'  # See GetParentContainer
    Position: 'Point'  # See GetPosition and SetPosition
    Properties: 'RichTextProperties'  # See GetProperties and SetProperties
    PropertiesMenuLabel: str  # See GetPropertiesMenuLabel
    Range: 'RichTextRange'  # See GetRange and SetRange
    Rect: '_Rect'  # See GetRect
    RightMargin: int  # See GetRightMargin
    TopMargin: int  # See GetTopMargin
    XMLNodeName: str  # See GetXMLNodeName



class RichTextPrinting(Object):
    """ This class provides a simple interface for performing RichTextBuffer
printing and previewing.

        Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
    """
    def __init__(self, name="Printing", parentWindow=None) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetFooterText(self, page=RICHTEXT_PAGE_EVEN, location=RICHTEXT_PAGE_CENTRE) -> str:
        """ A convenience function to get the footer text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetHeaderFooterData(self) -> 'RichTextHeaderFooterData':
        """ Returns the internal   wx.richtext.RichTextHeaderFooterData  object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetHeaderText(self, page=RICHTEXT_PAGE_EVEN, location=RICHTEXT_PAGE_CENTRE) -> str:
        """ A convenience function to get the header text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetPageSetupData(self) -> 'PageSetupDialogData':
        """ Returns a pointer to the internal page setup data.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetParentWindow(self) -> 'Window':
        """ Returns the parent window to be used for the preview window and printing wait dialog.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetPreviewRect(self) -> 'Rect':
        """ Returns the dimensions to be used for the preview window.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetPrintData(self) -> 'PrintData':
        """ Returns a pointer to the internal print data.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetTitle(self) -> str:
        """ Returns the title of the preview window or printing wait caption.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def PageSetup(self) -> None:
        """ Shows the page setup dialog.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def PreviewBuffer(self, buffer: 'richtext.RichTextBuffer') -> bool:
        """ Shows a preview window for the given buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def PreviewFile(self, richTextFile: str) -> bool:
        """ Shows a preview window for the given file.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def PrintBuffer(self, buffer, showPrintDialog=True) -> bool:
        """ Prints the given buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def PrintFile(self, richTextFile, showPrintDialog=True) -> bool:
        """ Prints the given file.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetFooterText(self, text, page=RICHTEXT_PAGE_ALL, location=RICHTEXT_PAGE_CENTRE) -> None:
        """ A convenience function to set the footer text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetHeaderFooterData(self, data: 'richtext.RichTextHeaderFooterData') -> None:
        """ Sets the internal   wx.richtext.RichTextHeaderFooterData  object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetHeaderFooterFont(self, font: 'Font') -> None:
        """ Sets the   wx.richtext.RichTextHeaderFooterData  font.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetHeaderFooterTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the   wx.richtext.RichTextHeaderFooterData  text colour.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetHeaderText(self, text, page=RICHTEXT_PAGE_ALL, location=RICHTEXT_PAGE_CENTRE) -> None:
        """ A convenience function to set the header text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetPageSetupData(self, pageSetupData: 'PageSetupDialogData') -> None:
        """ Sets the page setup data.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetParentWindow(self, parent: 'Window') -> None:
        """ Sets the parent window to be used for the preview window and printing wait dialog.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetPreviewRect(self, rect: 'Rect') -> None:
        """ Sets the dimensions to be used for the preview window.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetPrintData(self, printData: 'PrintData') -> None:
        """ Sets the print data.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetShowOnFirstPage(self, show: bool) -> None:
        """ Pass True to show the header and footer on the first page.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetTitle(self, title: str) -> None:
        """ Pass the title of the preview window or printing wait caption.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    FooterText: str  # See GetFooterText and SetFooterText
    HeaderFooterData: 'RichTextHeaderFooterData'  # See GetHeaderFooterData and SetHeaderFooterData
    HeaderText: str  # See GetHeaderText and SetHeaderText
    PageSetupData: 'PageSetupDialogData'  # See GetPageSetupData and SetPageSetupData
    ParentWindow: 'Window'  # See GetParentWindow and SetParentWindow
    PreviewRect: 'Rect'  # See GetPreviewRect and SetPreviewRect
    PrintData: '_PrintData'  # See GetPrintData and SetPrintData
    Title: str  # See GetTitle and SetTitle



class RichTextProperties(Object):
    """ A simple property class using Variants.

        Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def Clear(self) -> None:
        """ Clears the properties.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def Copy(self, props: 'richtext.RichTextProperties') -> None:
        """ Copies from props.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def Find(self, name: str) -> int:
        """ Finds the given property.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def FindOrCreateProperty(self, name: str) -> Any:
        """ Finds or creates a property with the given name, returning a pointer to the variant.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetCount(self) -> int:
        """ Returns a count of the properties.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetProperties(self) -> 'RichTextVariantArray':
        """ Returns the array of variants implementing the properties.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetProperty(self, name: str) -> Any:
        """ Gets the property variant by name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetPropertyBool(self, name: str) -> bool:
        """ Gets the value of the named property as a boolean.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetPropertyDouble(self, name: str) -> float:
        """ Gets the value of the named property as a double.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetPropertyLong(self, name: str) -> int:
        """ Gets the value of the named property as a long integer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetPropertyNames(self) -> list[str]:
        """ Returns all the property names.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetPropertyString(self, name: str) -> str:
        """ Gets the value of the named property as a string.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def HasProperty(self, name: str) -> bool:
        """ Returns True if the given property is found.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def MergeProperties(self, properties: 'richtext.RichTextProperties') -> None:
        """ Merges the given properties with these properties.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def Remove(self, name: str) -> bool:
        """ Removes the given property.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def RemoveProperties(self, properties: 'richtext.RichTextProperties') -> None:
        """ Removes the given properties from these properties.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def SetProperties(self, props: RichTextVariantArray) -> None:
        """ Sets the array of variants.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def SetProperty(self, props: Any) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.

            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    Count: int  # See GetCount
    Properties: 'RichTextVariantArray'  # See GetProperties and SetProperties
    PropertyNames: list[str]  # See GetPropertyNames



class RichTextRenderer(Object):
    """ This class isolates some common drawing functionality.

        Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
        """

    def DrawBitmapBullet(self, paragraph, dc, attr, rect) -> bool:
        """ Draws a bitmap bullet, where the bullet bitmap is specified by the value of GetBulletName.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
        """

    def DrawStandardBullet(self, paragraph, dc, attr, rect) -> bool:
        """ Draws a standard bullet, as specified by the value of GetBulletName.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
        """

    def DrawTextBullet(self, paragraph, dc, attr, rect, text) -> bool:
        """ Draws a bullet that can be described by text, such as numbered or symbol bullets.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
        """

    def EnumerateStandardBulletNames(self, bulletNames: list[str]) -> bool:
        """ Enumerate the standard bullet names currently supported.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
        """

    def MeasureBullet(self, paragraph, dc, attr, sz) -> bool:
        """ Measure the bullet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
        """



class RichTextStyleDefinition(Object):
    """ This is a base class for paragraph and character styles.

        Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
    """
    def __init__(self, name: str="") -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def GetBaseStyle(self) -> str:
        """ Returns the style on which this style is based.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def GetDescription(self) -> str:
        """ Returns the styleâs description.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def GetName(self) -> str:
        """ Returns the style name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def GetProperties(self) -> 'RichTextProperties':
        """ Returns the definitionâs properties.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def GetStyle(self) -> 'RichTextAttr':
        """ Returns the attributes associated with this style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def GetStyleMergedWithBase(self, sheet: 'richtext.RichTextStyleSheet') -> 'RichTextAttr':
        """ Returns the style attributes combined with the attributes of the specified base style, if any.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def SetBaseStyle(self, name: str) -> None:
        """ Sets the name of the style that this style is based on.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def SetDescription(self, descr: str) -> None:
        """ Sets the style description.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def SetName(self, name: str) -> None:
        """ Sets the name of the style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def SetProperties(self, props: 'richtext.RichTextProperties') -> None:
        """ Sets the definitionâs properties.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def SetStyle(self, style: 'richtext.RichTextAttr') -> None:
        """ Sets the attributes for this style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    BaseStyle: str  # See GetBaseStyle and SetBaseStyle
    Description: str  # See GetDescription and SetDescription
    Name: str  # See GetName and SetName
    Properties: 'RichTextProperties'  # See GetProperties and SetProperties
    Style: 'RichTextAttr'  # See GetStyle and SetStyle



class RichTextStyleSheet(Object):
    """ A style sheet contains named paragraph and character styles that make
it easy for a user to apply combinations of attributes to a
RichTextCtrl.

        Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def AddCharacterStyle(self, styleDef: 'richtext.RichTextCharacterStyleDefinition') -> bool:
        """ Adds a definition to the character style list.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def AddListStyle(self, styleDef: 'richtext.RichTextListStyleDefinition') -> bool:
        """ Adds a definition to the list style list.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def AddParagraphStyle(self, styleDef: 'richtext.RichTextParagraphStyleDefinition') -> bool:
        """ Adds a definition to the paragraph style list.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def AddStyle(self, styleDef: 'richtext.RichTextStyleDefinition') -> bool:
        """ Adds a definition to the appropriate style list.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def DeleteStyles(self) -> None:
        """ Deletes all styles.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def FindCharacterStyle(self, name, recurse=True) -> 'RichTextCharacterStyleDefinition':
        """ Finds a character definition by name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def FindListStyle(self, name, recurse=True) -> 'RichTextListStyleDefinition':
        """ Finds a list definition by name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def FindParagraphStyle(self, name, recurse=True) -> 'RichTextParagraphStyleDefinition':
        """ Finds a paragraph definition by name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def FindStyle(self, name: str) -> 'RichTextStyleDefinition':
        """ Finds a style definition by name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetCharacterStyle(self, n: int) -> 'RichTextCharacterStyleDefinition':
        """ Returns the nth  character style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetCharacterStyleCount(self) -> int:
        """ Returns the number of character styles.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetDescription(self) -> str:
        """ Returns the style sheetâs description.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetListStyle(self, n: int) -> 'RichTextListStyleDefinition':
        """ Returns the nth  list style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetListStyleCount(self) -> int:
        """ Returns the number of list styles.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetName(self) -> str:
        """ Returns the style sheetâs name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetParagraphStyle(self, n: int) -> 'RichTextParagraphStyleDefinition':
        """ Returns the nth  paragraph style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetParagraphStyleCount(self) -> int:
        """ Returns the number of paragraph styles.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetProperties(self) -> 'RichTextProperties':
        """ Returns the sheetâs properties.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def RemoveCharacterStyle(self, styleDef, deleteStyle=False) -> bool:
        """ Removes a character style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def RemoveListStyle(self, styleDef, deleteStyle=False) -> bool:
        """ Removes a list style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def RemoveParagraphStyle(self, styleDef, deleteStyle=False) -> bool:
        """ Removes a paragraph style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def RemoveStyle(self, styleDef, deleteStyle=False) -> bool:
        """ Removes a style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def SetDescription(self, descr: str) -> None:
        """ Sets the style sheetâs description.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def SetName(self, name: str) -> None:
        """ Sets the style sheetâs name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def SetProperties(self, props: 'richtext.RichTextProperties') -> None:
        """ Sets the sheetâs properties.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    CharacterStyleCount: int  # See GetCharacterStyleCount
    Description: str  # See GetDescription and SetDescription
    ListStyleCount: int  # See GetListStyleCount
    Name: str  # See GetName and SetName
    ParagraphStyleCount: int  # See GetParagraphStyleCount
    Properties: 'RichTextProperties'  # See GetProperties and SetProperties



class RichTextPrintout(Printout):
    """ This class implements print layout for RichTextBuffer.

        Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
    """
    def __init__(self, title: str="Printout") -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def CalculateScaling(self, dc, textRect, headerRect, footerRect) -> None:
        """ Calculates scaling and text, header and footer rectangles.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def GetHeaderFooterData(self) -> 'RichTextHeaderFooterData':
        """ Returns the header and footer data associated with the printout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def GetPageInfo(self) -> tuple:
        """ Gets the page information.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def GetRichTextBuffer(self) -> 'RichTextBuffer':
        """ Returns a pointer to the buffer being rendered.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def HasPage(self, page: int) -> bool:
        """ Returns True if the given page exists in the printout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def OnPreparePrinting(self) -> None:
        """ Prepares for printing, laying out the buffer and calculating pagination.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def OnPrintPage(self, page: int) -> bool:
        """ Does the actual printing for this page.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def SetHeaderFooterData(self, data: 'richtext.RichTextHeaderFooterData') -> None:
        """ Sets the header and footer data associated with the printout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def SetMargins(self, top=254, bottom=254, left=254, right=254) -> None:
        """ Sets margins in 10ths of millimetre.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def SetRichTextBuffer(self, buffer: 'richtext.RichTextBuffer') -> None:
        """ Sets the buffer to print.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    HeaderFooterData: 'RichTextHeaderFooterData'  # See GetHeaderFooterData and SetHeaderFooterData
    RichTextBuffer: 'RichTextBuffer'  # See GetRichTextBuffer and SetRichTextBuffer



class RichTextAttr(TextAttr):
    """ A class representing enhanced attributes for rich text objects.

        Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def Apply(self, style, compareWith=None) -> bool:
        """ Merges the given attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def Copy(self, attr: 'richtext.RichTextAttr') -> None:
        """ Copy function.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def EqPartial(self, attr, weakTest=True) -> bool:
        """ Partial equality test.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def GetTextBoxAttr(self) -> 'TextBoxAttr':
        """ Returns the text box attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def IsDefault(self) -> bool:
        """ Returns True if no attributes are set.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def RemoveStyle(self, attr: 'richtext.RichTextAttr') -> bool:
        """ Removes the specified attributes from this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def SetTextBoxAttr(self, attr: 'richtext.TextBoxAttr') -> None:
        """ Set the text box attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality test.

            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    TextBoxAttr: 'TextBoxAttr'  # See GetTextBoxAttr and SetTextBoxAttr
    m_textBoxAttr: Any  # A public C++ attribute of type TextBoxAttr     .



class RichTextStdRenderer(RichTextRenderer):
    """ The standard renderer for drawing bullets.

        Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
        """

    def DrawBitmapBullet(self, paragraph, dc, attr, rect) -> bool:
        """ Draws a bitmap bullet, where the bullet bitmap is specified by the value of GetBulletName.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
        """

    def DrawStandardBullet(self, paragraph, dc, attr, rect) -> bool:
        """ Draws a standard bullet, as specified by the value of GetBulletName.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
        """

    def DrawTextBullet(self, paragraph, dc, attr, rect, text) -> bool:
        """ Draws a bullet that can be described by text, such as numbered or symbol bullets.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
        """

    def EnumerateStandardBulletNames(self, bulletNames: list[str]) -> bool:
        """ Enumerate the standard bullet names currently supported.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
        """

    def MeasureBullet(self, paragraph, dc, attr, sz) -> bool:
        """ Measure the bullet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
        """



class RichTextBuffer(RichTextParagraphLayoutBox):
    """ This is a kind of paragraph layout box, used to represent the whole
buffer.

        Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def AddDrawingHandler(handler: 'richtext.RichTextDrawingHandler') -> None:
        """ Adds a drawing handler to the end.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def AddEventHandler(self, handler: 'EvtHandler') -> bool:
        """ Adds an event handler.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def AddFieldType(fieldType: 'richtext.RichTextFieldType') -> None:
        """ Adds a field type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def AddHandler(handler: 'richtext.RichTextFileHandler') -> None:
        """ Adds a file handler to the end.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def AddParagraph(self, text, paraStyle=None) -> 'RichTextRange':
        """ Convenience function to add a paragraph of text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BatchingUndo(self) -> bool:
        """ Returns True if we are collapsing commands.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginAlignment(self, alignment: int) -> bool:
        """ Begins using alignment.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginBatchUndo(self, cmdName: str) -> bool:
        """ Begin collapsing undo/redo commands.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginBold(self) -> bool:
        """ Begins using bold.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginCharacterStyle(self, characterStyle: str) -> bool:
        """ Begins named character style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginFont(self, font: 'Font') -> bool:
        """ Begins using this font.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginFontSize(self, pointSize: int) -> bool:
        """ Begins using point size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginItalic(self) -> bool:
        """ Begins using italic.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginLeftIndent(self, leftIndent, leftSubIndent=0) -> bool:
        """ Begins using leftIndent  for the left indent, and optionally leftSubIndent  for the sub-indent.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginLineSpacing(self, lineSpacing: int) -> bool:
        """ Begins line spacing using the specified value.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginListStyle(self, listStyle, level=1, number=1) -> bool:
        """ Begins named list style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginNumberedBullet(self, bulletNumber, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_ARABIC|TEXT_ATTR_BULLET_STYLE_PERIOD) -> bool:
        """ Begins numbered bullet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginParagraphSpacing(self, before, after) -> bool:
        """ Begins paragraph spacing; pass the before-paragraph and after-paragraph spacing in tenths of a millimetre.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginParagraphStyle(self, paragraphStyle: str) -> bool:
        """ Begins named paragraph style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginRightIndent(self, rightIndent: int) -> bool:
        """ Begins a right indent, specified in tenths of a millimetre.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginStandardBullet(self, bulletName, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_STANDARD) -> bool:
        """ Begins applying a standard bullet, using one of the standard bullet names (currently  standard/circle   or   standard/square .

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginStyle(self, style: 'richtext.RichTextAttr') -> bool:
        """ Begin using a style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginSuppressUndo(self) -> bool:
        """ Begin suppressing undo/redo commands.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginSymbolBullet(self, symbol, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_SYMBOL) -> bool:
        """ Begins applying a symbol bullet, using a character from the current font.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginTextColour(self, colour: Union[int, str, 'Colour']) -> bool:
        """ Begins using this colour.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginURL(self, url, characterStyle="") -> bool:
        """ Begins applying wx.TEXT_ATTR_URL to the content.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginUnderline(self) -> bool:
        """ Begins using underline.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def CanPasteFromClipboard(self) -> bool:
        """ Returns True if we can paste from the clipboard.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def CleanUpDrawingHandlers() -> None:
        """ Clean up drawing handlers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def CleanUpFieldTypes() -> None:
        """ Cleans up field types.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def CleanUpHandlers() -> None:
        """ Clean up file handlers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def ClearEventHandlers(self) -> None:
        """ Clear event handlers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def ClearStyleStack(self) -> None:
        """ Clears the style stack.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def Clone(self) -> 'RichTextObject':
        """ Clones the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def Copy(self, obj: 'richtext.RichTextBuffer') -> None:
        """ Copies the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def CopyToClipboard(self, range: 'richtext.RichTextRange') -> bool:
        """ Copy the range to the clipboard.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def DeleteRangeWithUndo(self, range, ctrl) -> bool:
        """ Submits a command to delete this range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndAlignment(self) -> bool:
        """ Ends alignment.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndAllStyles(self) -> bool:
        """ End all styles.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndBatchUndo(self) -> bool:
        """ End collapsing undo/redo commands.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndBold(self) -> bool:
        """ Ends using bold.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndCharacterStyle(self) -> bool:
        """ Ends named character style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndFont(self) -> bool:
        """ Ends using a font.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndFontSize(self) -> bool:
        """ Ends using point size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndItalic(self) -> bool:
        """ Ends using italic.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndLeftIndent(self) -> bool:
        """ Ends left indent.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndLineSpacing(self) -> bool:
        """ Ends line spacing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndListStyle(self) -> bool:
        """ Ends named character style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndNumberedBullet(self) -> bool:
        """ Ends numbered bullet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndParagraphSpacing(self) -> bool:
        """ Ends paragraph spacing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndParagraphStyle(self) -> bool:
        """ Ends named character style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndRightIndent(self) -> bool:
        """ Ends right indent.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndStandardBullet(self) -> bool:
        """ Ends standard bullet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndStyle(self) -> bool:
        """ End the style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndSuppressUndo(self) -> bool:
        """ End suppressing undo/redo commands.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndSymbolBullet(self) -> bool:
        """ Ends symbol bullet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndTextColour(self) -> bool:
        """ Ends using a colour.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndURL(self) -> bool:
        """ Ends URL.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndUnderline(self) -> bool:
        """ Ends using underline.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def FindDrawingHandler(name: str) -> 'RichTextDrawingHandler':
        """ Finds a drawing handler by name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def FindFieldType(name: str) -> 'RichTextFieldType':
        """ Finds a field type by name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def FindHandlerByType(imageType: RichTextFileType) -> 'RichTextFileHandler':
        """ Finds a handler by type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def FindHandlerByExtension(extension, imageType) -> 'RichTextFileHandler':
        """ Finds a file handler by extension and type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def FindHandlerByName(name: str) -> 'RichTextFileHandler':
        """ Finds a file handler by name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def FindHandlerByFilename(filename, imageType) -> 'RichTextFileHandler':
        """ Finds a handler by filename or, if supplied, type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetBatchedCommand(self) -> 'RichTextCommand':
        """ Returns the collapsed command.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetBulletProportion() -> float:
        """ Returns the factor to multiply by character height to get a reasonable bullet size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetBulletRightMargin() -> int:
        """ Returns the minimum margin between bullet and paragraph in 10ths of a mm.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetCommandProcessor(self) -> 'CommandProcessor':
        """ Returns the command processor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetDimensionScale(self) -> float:
        """ Returns the scale factor for displaying certain dimensions such as indentation and inter-paragraph spacing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetDrawingHandlers() -> list['richtext.RichTextDrawingHandler']:
        """ Returns the drawing handlers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetExtWildcard(combine=False, save=False) -> Any:
        """ Gets a wildcard string for the file dialog based on all the currently
loaded richtext file handlers, and a list that can be used to map
those filter types to the file handler type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetFloatingLayoutMode() -> bool:
        """ Returns the floating layout mode.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetFontScale(self) -> float:
        """ Returns the scale factor for displaying fonts, for example for more comfortable editing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetFontTable(self) -> 'RichTextFontTable':
        """ Returns the table storing fonts, for quick access and font reuse.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetHandlerFlags(self) -> int:
        """ Gets the handler flags, controlling loading and saving.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetHandlers() -> list['richtext.RichTextFileHandler']:
        """ Returns the file handlers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetRenderer() -> 'RichTextRenderer':
        """ Returns the renderer object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetScale(self) -> float:
        """ Returns the scale factor for calculating dimensions.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ Returns the style sheet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetStyleStackSize(self) -> int:
        """ Returns the size of the style stack, for example to check correct nesting.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ Hit-testing: returns a flag indicating hit test details, plus information about position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def Init(self) -> None:
        """ Initialisation.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def InitStandardHandlers() -> None:
        """ Initialise the standard file handlers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def InsertDrawingHandler(handler: 'richtext.RichTextDrawingHandler') -> None:
        """ Inserts a drawing handler at the front.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def InsertHandler(handler: 'richtext.RichTextFileHandler') -> None:
        """ Inserts a file handler at the front.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def InsertImageWithUndo(*args, **kwargs) -> bool:
        """ Submits a command to insert the given image.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def InsertNewlineWithUndo(self, pos, ctrl, flags=0) -> bool:
        """ Submits a command to insert a newline.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def InsertObjectWithUndo(self, pos, object, ctrl, flags) -> 'RichTextObject':
        """ Submits a command to insert an object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def InsertParagraphsWithUndo(self, pos, paragraphs, ctrl, flags=0) -> bool:
        """ Submits a command to insert paragraphs.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def InsertTextWithUndo(self, pos, text, ctrl, flags=0) -> bool:
        """ Submits a command to insert the given text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def IsModified(self) -> bool:
        """ Returns True if the buffer was modified.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def LoadFile(self, *args, **kw) -> bool:
        """ Loads content from a stream or file.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def Modify(self, modify: bool=True) -> None:
        """ Mark modified.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def PasteFromClipboard(self, position: int) -> bool:
        """ Paste the clipboard content to the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def PopStyleSheet(self) -> 'RichTextStyleSheet':
        """ Pops the style sheet from the top of the style sheet stack.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def PushStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> bool:
        """ Pushes the style sheet to the top of the style sheet stack.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def RemoveDrawingHandler(name: str) -> bool:
        """ Removes a drawing handler.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def RemoveEventHandler(self, handler, deleteHandler=False) -> bool:
        """ Removes an event handler from the bufferâs list of handlers, deleting the object if deleteHandler  is True.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def RemoveFieldType(name: str) -> bool:
        """ Removes a field type by name.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def RemoveHandler(name: str) -> bool:
        """ Removes a file handler.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def ResetAndClearCommands(self) -> None:
        """ Clears the buffer, adds an empty paragraph, and clears the command processor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SaveFile(self, *args, **kw) -> bool:
        """ Saves content to a stream or file.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SendEvent(self, event, sendToAll=True) -> bool:
        """ Send event to event handlers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def SetBulletProportion(prop: float) -> None:
        """ Sets the factor to multiply by character height to get a reasonable bullet size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def SetBulletRightMargin(margin: int) -> None:
        """ Sets the minimum margin between bullet and paragraph in 10ths of a mm.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetDimensionScale(self, dimScale: float) -> None:
        """ Sets the scale factor for displaying certain dimensions such as indentation and inter-paragraph spacing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def SetFloatingLayoutMode(mode: bool) -> None:
        """ Sets the floating layout mode.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetFontScale(self, fontScale: float) -> None:
        """ Sets the scale factor for displaying fonts, for example for more comfortable editing.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetFontTable(self, table: 'richtext.RichTextFontTable') -> None:
        """ Sets table storing fonts, for quick access and font reuse.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetHandlerFlags(self, flags: int) -> None:
        """ Sets the handler flags, controlling loading and saving.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def SetRenderer(renderer: 'richtext.RichTextRenderer') -> None:
        """ Sets renderer  as the object to be used to render certain aspects of the content, such as bullets.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetScale(self, scale: float) -> None:
        """ Sets the scale factor for calculating dimensions.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> None:
        """ Sets style sheet, if any.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetStyleSheetAndNotify(self, sheet: 'richtext.RichTextStyleSheet') -> bool:
        """ Sets the style sheet and sends a notification of the change.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SubmitAction(self, action: 'richtext.RichTextAction') -> bool:
        """ Submit the action immediately, or delay according to whether collapsing is on.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SuppressingUndo(self) -> bool:
        """ Are we suppressing undo??

            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    BatchedCommand: 'RichTextCommand'  # See GetBatchedCommand
    CommandProcessor: '_CommandProcessor'  # See GetCommandProcessor
    DimensionScale: float  # See GetDimensionScale and SetDimensionScale
    FontScale: float  # See GetFontScale and SetFontScale
    FontTable: 'RichTextFontTable'  # See GetFontTable and SetFontTable
    HandlerFlags: int  # See GetHandlerFlags and SetHandlerFlags
    Scale: float  # See GetScale and SetScale
    StyleSheet: 'RichTextStyleSheet'  # See GetStyleSheet and SetStyleSheet
    StyleStackSize: int  # See GetStyleStackSize



class RichTextRange:
    """ This stores beginning and end positions for a range of data.

        Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def Contains(self, pos: int) -> bool:
        """ Returns True if pos  was within the range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def FromInternal(self) -> 'RichTextRange':
        """ Converts the internal range, which uses the first and last character positions of the range, to the API-standard range, whose end is one past the last character in the range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def Get(self) -> tuple:
        """ Return the start and end properties as a tuple.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def GetEnd(self) -> int:
        """ Gets the end position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def GetIM(self) -> None:
        """ Returns an immutable representation of the wx.RichTextRange object, based on namedtuple.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def GetLength(self) -> int:
        """ Gets the length of the range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def GetStart(self) -> int:
        """ Returns the start position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def IsOutside(self, range: 'richtext.RichTextRange') -> bool:
        """ Returns True if this range is completely outside range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def IsWithin(self, range: 'richtext.RichTextRange') -> bool:
        """ Returns True if this range is completely within range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def LimitTo(self, range: 'richtext.RichTextRange') -> bool:
        """ Limit this range to be within range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def SetEnd(self, end: int) -> None:
        """ Sets the end position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def SetRange(self, start, end) -> None:
        """ Sets the range start and end positions.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def SetStart(self, start: int) -> None:
        """ Sets the start position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def Swap(self) -> None:
        """ Swaps the start and end.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def ToInternal(self) -> 'RichTextRange':
        """ Converts the API-standard range, whose end is one past the last character in the range, to the internal form, which uses the first and last character positions of the range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __bool__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __getitem__(self, idx) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __len__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __nonzero__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __reduce__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __repr__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __setitem__(self, idx, val) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __str__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __ne__(self, item: Any) -> bool:
        """ Inequality operator.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __add__(self) -> None:
        """ Adds a range to this range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __sub__(self) -> None:
        """ Subtracts a range from this range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.

            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    End: int  # See GetEnd and SetEnd
    Length: int  # See GetLength
    Start: int  # See GetStart and SetStart



class RichTextParagraphLayoutBox(RichTextCompositeObject):
    """ This class knows how to lay out paragraphs.

        Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def AcceptsFocus(self) -> bool:
        """ Returns True if objects of this class can accept the focus, i.e. a call to SetFocusObject is possible.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def AddImage(self, image, paraStyle=None) -> 'RichTextRange':
        """ Convenience function to add an image.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def AddParagraph(self, text, paraStyle=None) -> 'RichTextRange':
        """ Convenience function to add a paragraph of text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def AddParagraphs(self, text, paraStyle=None) -> 'RichTextRange':
        """ Adds multiple paragraphs, based on newlines.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def ApplyStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> bool:
        """ Apply the style sheet to the buffer, for example if the styles have changed.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Clear(self) -> None:
        """ Clears all the children.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def ClearListStyle(self, range, flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool:
        """ Clears the list style from the given range, clearing list-related attributes and applying any named paragraph style associated with each paragraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Clone(self) -> 'RichTextObject':
        """ Clones the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def CollectStyle(self, currentStyle, style, clashingAttr, absentAttr) -> bool:
        """ Combines style  with currentStyle  for the purpose of summarising the attributes of a range of content.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Copy(self, obj: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ obj (wx.richtext.RichTextParagraphLayoutBox) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def CopyFragment(self, range, fragment) -> bool:
        """ Make a copy of the fragment corresponding to the given range, putting it in fragment.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def DeleteRange(self, range: 'richtext.RichTextRange') -> bool:
        """ Deletes the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def DeleteRangeWithUndo(self, range, ctrl, buffer) -> bool:
        """ Submits a command to delete this range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def DoGetStyle(self, position, style, combineStyles=True) -> bool:
        """ Implementation helper for GetStyle.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def DoInvalidate(self, invalidRange: 'richtext.RichTextRange') -> None:
        """ Do the (in)validation for this object only.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def DoNumberList(self, range, promotionRange, promoteBy, styleDef, flags=RICHTEXT_SETSTYLE_WITH_UNDO, startFrom=1, specifiedLevel=-1) -> bool:
        """ Helper for NumberList and PromoteList, that does renumbering and promotion simultaneously def  can be NULL/empty to indicate that the existing list style should be used.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ Draw the item, within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def DrawFloats(self, dc, context, range, selection, rect, descent, style) -> None:
        """ Draws the floating objects in this buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def FindNextParagraphNumber(self, previousParagraph, attr) -> bool:
        """ Fills in the attributes for numbering a paragraph after previousParagraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetBasicStyle(self) -> 'RichTextAttr':
        """ Returns the basic (overall) style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetDefaultStyle(self) -> 'RichTextAttr':
        """ Returns the current default style, affecting the style currently being applied (for example, setting the default style to bold will cause subsequently inserted text to be bold).

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetFloatCollector(self) -> 'RichTextFloatCollector':
        """ Returns the RichTextFloatCollector of this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetFloatingObjectCount(self) -> int:
        """ Returns the number of floating objects at this level.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetFloatingObjects(self, objects: RichTextObjectList) -> bool:
        """ Returns a list of floating objects.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetInvalidRange(self, wholeParagraphs: bool=False) -> 'RichTextRange':
        """ Get invalid range, rounding to entire paragraphs if argument is True.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetLeafObjectAtPosition(self, position: int) -> 'RichTextObject':
        """ Returns the leaf object in a paragraph at this position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetLineAtPosition(self, pos, caretPosition=False) -> 'RichTextLine':
        """ Returns the line at the given position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetLineAtYPosition(self, y: int) -> 'RichTextLine':
        """ Returns the line at the given y pixel position, or the last line.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetLineCount(self) -> int:
        """ Returns the number of visible lines.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetLineForVisibleLineNumber(self, lineNumber: int) -> 'RichTextLine':
        """ Given a line number, returns the corresponding   wx.richtext.RichTextLine  object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetLineSizeAtPosition(self, pos, caretPosition=False) -> 'Size':
        """ Returns the line size at the given position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetParagraphAtLine(self, paragraphNumber: int) -> 'RichTextParagraph':
        """ Returns the paragraph by number.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetParagraphAtPosition(self, pos, caretPosition=False) -> 'RichTextParagraph':
        """ Returns the paragraph at the given character or caret position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetParagraphCount(self) -> int:
        """ Returns the number of paragraphs.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetParagraphForLine(self, line: 'richtext.RichTextLine') -> 'RichTextParagraph':
        """ Returns the paragraph for a given line.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetParagraphLength(self, paragraphNumber: int) -> int:
        """ Returns the length of the paragraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetParagraphText(self, paragraphNumber: int) -> str:
        """ Returns the text of the paragraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetPartialParagraph(self) -> bool:
        """ Returns a flag indicating whether the last paragraph is partial or complete.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ Returns the object size for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetRichTextCtrl(self) -> 'RichTextCtrl':
        """ Returns the associated control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetStyle(self, position, style) -> bool:
        """ Returns the combined text attributes for this position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetStyleForNewParagraph(self, buffer, pos, caretPosition=False, lookUpNewParaStyle=False) -> 'RichTextAttr':
        """ Returns the style that is appropriate for a new paragraph at this position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetStyleForRange(self, range, style) -> bool:
        """ This function gets a style representing the common, combined attributes in the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ Returns the style sheet associated with the overall buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetText(self) -> str:
        """ Get all the text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetTextForRange(self, range: 'richtext.RichTextRange') -> str:
        """ Returns any text in this object for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetUncombinedStyle(self, position, style) -> bool:
        """ Returns the content (uncombined) attributes for this position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetVisibleLineNumber(self, pos, caretPosition=False, startOfLine=False) -> int:
        """ Given a position, returns the number of the visible line (potentially many to a paragraph), starting from zero at the start of the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetXMLNodeName(self) -> str:
        """ Returns the XML node name of this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def HasCharacterAttributes(self, range, style) -> bool:
        """ Test if this whole range has character attributes of the specified kind.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def HasParagraphAttributes(self, range, style) -> bool:
        """ Test if this whole range has paragraph attributes of the specified kind.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ Hit-testing: returns a flag indicating hit test details, plus information about position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def ImportFromXML(self, buffer, node, handler, recurse) -> bool:
        """ Imports this object from XML.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Init(self) -> None:
        """ Initializes the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertFieldWithUndo(self, buffer, pos, fieldType, properties, ctrl, flags, textAttr) -> 'RichTextField':
        """ Submits a command to insert the given field.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertFragment(self, position, fragment) -> bool:
        """ Insert fragment into this box at the given position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertImageWithUndo(self, buffer, pos, imageBlock, ctrl, flags, textAttr) -> bool:
        """ Submits a command to insert the given image.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertNewlineWithUndo(self, buffer, pos, ctrl, flags=0) -> bool:
        """ Submits a command to insert the given text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertObjectWithUndo(self, buffer, pos, object, ctrl, flags=0) -> 'RichTextObject':
        """ Inserts an object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertParagraphsWithUndo(self, buffer, pos, paragraphs, ctrl, flags=0) -> bool:
        """ Submits a command to insert paragraphs.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertTextWithUndo(self, buffer, pos, text, ctrl, flags=0) -> bool:
        """ Submits a command to insert the given text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Invalidate(self, invalidRange: 'richtext.RichTextRange'=RICHTEXT_ALL) -> None:
        """ Invalidates the buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InvalidateHierarchy(self, invalidRange: 'richtext.RichTextRange'=RICHTEXT_ALL) -> None:
        """ Do the (in)validation both up and down the hierarchy.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def IsDirty(self) -> bool:
        """ Returns True if this object needs layout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def IsTopLevel(self) -> bool:
        """ Returns True if this object is top-level, i.e. contains its own paragraphs, such as a text box.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ Lay the item out at the specified position with the given size constraint.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def MoveAnchoredObjectToParagraph(self, from_, to_, obj) -> None:
        """ Moves an anchored object to another paragraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def NumberList(self, *args, **kw) -> bool:
        """ Numbers the paragraphs in the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def PositionToXY(self, pos, x, y) -> bool:
        """ Converts a zero-based position to line column and paragraph number.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def PrepareContent(self, container: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ Prepares the content just before insertion (or after buffer reset).

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def PromoteList(self, *args, **kw) -> bool:
        """ Promotes the list items within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Reset(self) -> None:
        """ Clears and initializes with one blank paragraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetBasicStyle(self, style: 'richtext.RichTextAttr') -> None:
        """ Sets the basic (overall) style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetDefaultStyle(self, style: 'richtext.RichTextAttr') -> bool:
        """ Sets the default style, affecting the style currently being applied (for example, setting the default style to bold will cause subsequently inserted text to be bold).

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetListStyle(self, *args, **kw) -> bool:
        """ Sets the list attributes for the given range, passing flags to determine how the attributes are set.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetObjectPropertiesWithUndo(self, obj, properties, objToSet=None) -> bool:
        """ Sets with undo the properties for the given object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetPartialParagraph(self, partialPara: bool) -> None:
        """ Sets a flag indicating whether the last paragraph is partial or complete.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetProperties(self, range, properties, flags=RICHTEXT_SETPROPERTIES_WITH_UNDO) -> bool:
        """ Sets the properties for the given range, passing flags to determine how the attributes are set.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetRichTextCtrl(self, ctrl: 'richtext.RichTextCtrl') -> None:
        """ Associates a control with the buffer, for operations that for example require refreshing the window.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetStyle(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def UpdateFloatingObjects(self, availableRect, untilObj=None) -> bool:
        """ Gather information about floating objects.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def UpdateRanges(self) -> None:
        """ Calculate ranges.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def XYToPosition(self, x, y) -> int:
        """ Converts zero-based line column and paragraph number to a position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    BasicStyle: 'RichTextAttr'  # See GetBasicStyle and SetBasicStyle
    DefaultStyle: 'RichTextAttr'  # See GetDefaultStyle and SetDefaultStyle
    FloatCollector: 'RichTextFloatCollector'  # See GetFloatCollector
    FloatingObjectCount: int  # See GetFloatingObjectCount
    InvalidRange: 'RichTextRange'  # See GetInvalidRange
    LineCount: int  # See GetLineCount
    ParagraphCount: int  # See GetParagraphCount
    PartialParagraph: bool  # See GetPartialParagraph and SetPartialParagraph
    RichTextCtrl: 'RichTextCtrl'  # See GetRichTextCtrl and SetRichTextCtrl
    StyleSheet: 'RichTextStyleSheet'  # See GetStyleSheet
    Text: str  # See GetText
    XMLNodeName: str  # See GetXMLNodeName



RICHTEXT_SETPROPERTIES_NONE: int

class RichTextTable(RichTextBox):
    """ RichTextTable represents a table with arbitrary columns and rows.

        Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def AcceptsFocus(self) -> bool:
        """ Returns True if objects of this class can accept the focus, i.e. a call to SetFocusObject is possible.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def AddColumns(*args, **kwargs) -> bool:
        """ Adds columns from the given column position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def AddRows(*args, **kwargs) -> bool:
        """ Adds rows from the given row position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def CalculateRange(self, start: int) -> None:
        """ Calculates the range of the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def CanEditProperties(self) -> bool:
        """ Returns True if we can edit the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def ClearTable(self) -> None:
        """ Clears the table.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def Clone(self) -> 'RichTextObject':
        """ Clones the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def Copy(self, obj: 'richtext.RichTextTable') -> None:
        """ obj (wx.richtext.RichTextTable) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def CreateTable(self, rows, cols) -> bool:
        """ Creates a table of the given dimensions.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def DeleteColumns(self, startCol, noCols=1) -> bool:
        """ Deletes columns from the given column position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def DeleteRange(self, range: 'richtext.RichTextRange') -> bool:
        """ Deletes the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def DeleteRows(self, startRow, noRows=1) -> bool:
        """ Deletes rows from the given row position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ Draw the item, within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def EditProperties(self, parent, buffer) -> bool:
        """ Edits the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def FindPosition(self, dc, context, index, forceLineStart) -> tuple:
        """ Finds the absolute position and row height for the given character position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetCell(self, *args, **kw) -> 'RichTextCell':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetCellRowColumnPosition(self, pos, row, col) -> bool:
        """ Returns the row/column for a given character position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetCells(self) -> 'RichTextObjectPtrArrayArray':
        """ Returns the cells array.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetColumnCount(self) -> int:
        """ Returns the column count.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetFocusedCell(self) -> 'Position':
        """ Returns the coordinates of the cell with keyboard focus, or (-1,-1) if none.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetPropertiesMenuLabel(self) -> str:
        """ Returns the label to be used for the properties context menu item.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ Returns the object size for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetRowCount(self) -> int:
        """ Returns the row count.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetSelection(self, start, end) -> 'RichTextSelection':
        """ Returns a selection object specifying the selections between start and end character positions.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetTextForRange(self, range: 'richtext.RichTextRange') -> str:
        """ Returns any text in this object for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetXMLNodeName(self) -> str:
        """ Returns the XML node name of this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def HandlesChildSelections(self) -> bool:
        """ Returns True if this object can handle the selections of its children, fOr example a table.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ Hit-testing: returns a flag indicating hit test details, plus information about position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def ImportFromXML(self, buffer, node, handler, recurse) -> bool:
        """ Imports this object from XML.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ Lay the item out at the specified position with the given size constraint.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def SetCellStyle(self, selection, style, flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool:
        """ Sets the attributes for the cells specified by the selection.

            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    Cells: 'RichTextObjectPtrArrayArray'  # See GetCells
    ColumnCount: int  # See GetColumnCount
    FocusedCell: 'Position'  # See GetFocusedCell
    PropertiesMenuLabel: str  # See GetPropertiesMenuLabel
    RowCount: int  # See GetRowCount
    XMLNodeName: str  # See GetXMLNodeName



class RichTextContextMenuPropertiesInfo:
    """ RichTextContextMenuPropertiesInfo keeps track of objects that appear
in the context menu, whose properties are available to be edited.

        Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def AddItem(self, label, obj) -> bool:
        """ Adds an item.

            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def AddItems(self, ctrl, container, obj) -> int:
        """ Adds appropriate menu items for the current container and clicked on object (and containerâs parent, if appropriate).

            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def AddMenuItems(self, menu, startCmd=ID_RICHTEXT_PROPERTIES1) -> int:
        """ Returns the number of menu items that were added.

            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def Clear(self) -> None:
        """ Clears the items.

            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def GetCount(self) -> int:
        """ Returns the number of items.

            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def GetLabel(self, n: int) -> str:
        """ Returns the nth label.

            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def GetLabels(self) -> list[str]:
        """ Returns the array of labels.

            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def GetObject(self, n: int) -> 'RichTextObject':
        """ Returns the nth object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def GetObjects(self) -> 'RichTextObjectPtrArray':
        """ Returns the array of objects.

            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def Init(self) -> None:
        """ Initialisation.

            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    Count: int  # See GetCount
    Labels: list[str]  # See GetLabels
    Objects: 'RichTextObjectPtrArray'  # See GetObjects
    m_labels: Any  # A public C++ attribute of type list of strings.
    m_objects: Any  # A public C++ attribute of type RichTextObjectPtrArray.



class RichTextSelection:
    """ Stores selection information.

        Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def Add(self, range: 'richtext.RichTextRange') -> None:
        """ Adds a range to the selection.

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def Copy(self, sel: 'richtext.RichTextSelection') -> None:
        """ Copies from sel.

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def GetContainer(self) -> 'RichTextParagraphLayoutBox':
        """ Returns the container for which the selection is valid.

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def GetCount(self) -> int:
        """ Returns the number of ranges in the selection.

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def GetRange(self, *args, **kw) -> 'RichTextRange':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def GetRanges(self) -> 'RichTextRangeArray':
        """ Returns the selection ranges.

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def GetSelectionForObject(self, obj: 'richtext.RichTextObject') -> 'RichTextRangeArray':
        """ Returns the selection appropriate to the specified object, if any; returns an empty array if none at the level of the objectâs container.

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def IsValid(self) -> bool:
        """ Returns True if the selection is valid.

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def Reset(self) -> None:
        """ Resets the selection.

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def Set(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def SetContainer(self, container: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ Sets the container for which the selection is valid.

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def SetRange(self, range: 'richtext.RichTextRange') -> None:
        """ Sets a single range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def SetRanges(self, ranges: RichTextRangeArray) -> None:
        """ Sets the selection ranges.

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def WithinSelection(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def __bool__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def __nonzero__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.

            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    Container: 'RichTextParagraphLayoutBox'  # See GetContainer and SetContainer
    Count: int  # See GetCount
    Range: 'RichTextRange'  # See GetRange and SetRange
    Ranges: 'RichTextRangeArray'  # See GetRanges and SetRanges
    m_container: Any  # A public C++ attribute of type RichTextParagraphLayoutBox     .
    m_ranges: Any  # A public C++ attribute of type RichTextRangeArray.



RICHTEXT_NO_SELECTION: int

class RichTextLine:
    """ This object represents a line in a paragraph, and stores offsets from
the start of the paragraph representing the start and end positions of
the line.

        Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def Clone(self) -> 'RichTextLine':
        """ wx.richtext.RichTextLine

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def Copy(self, obj: 'richtext.RichTextLine') -> None:
        """ Copies from obj.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetAbsolutePosition(self) -> 'Point':
        """ Returns the absolute object position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetAbsoluteRange(self) -> 'RichTextRange':
        """ Returns the absolute range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetDescent(self) -> int:
        """ Returns the stored descent.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetParent(self) -> 'RichTextParagraph':
        """ Returns the parent paragraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetPosition(self) -> 'Point':
        """ Returns the object position relative to the parent.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetRange(self) -> 'RichTextRange':
        """ Returns the range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetRect(self) -> 'Rect':
        """ Returns the rectangle enclosing the line.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetSize(self) -> 'Size':
        """ Returns the line size as calculated by Layout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def Init(self, parent: 'richtext.RichTextParagraph') -> None:
        """ Initialises the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def SetDescent(self, descent: int) -> None:
        """ Sets the stored descent.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def SetPosition(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ Sets the object position relative to the parent.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def SetRange(self, *args, **kw) -> None:
        """ Sets the range associated with this line.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def SetSize(self, sz: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the line size as calculated by Layout.

            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    AbsolutePosition: 'Point'  # See GetAbsolutePosition
    AbsoluteRange: 'RichTextRange'  # See GetAbsoluteRange
    Descent: int  # See GetDescent and SetDescent
    Parent: 'RichTextParagraph'  # See GetParent
    Position: 'Point'  # See GetPosition and SetPosition
    Range: 'RichTextRange'  # See GetRange and SetRange
    Rect: '_Rect'  # See GetRect
    Size: '_Size'  # See GetSize and SetSize



class RichTextListStyleDefinition(RichTextParagraphStyleDefinition):
    """ This class represents a list style definition, usually added to a
RichTextStyleSheet.

        Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
    """
    def __init__(self, name: str="") -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def CombineWithParagraphStyle(self, indent, paraStyle, styleSheet=None) -> 'RichTextAttr':
        """ This function combines the given paragraph style with the list styleâs base attributes and level style matching the given indent, returning the combined attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def FindLevelForIndent(self, indent: int) -> int:
        """ This function finds the level (from 0 to 9) whose indentation attribute mostly closely matches indent  (expressed in tenths of a millimetre).

            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def GetCombinedStyle(self, indent, styleSheet=None) -> 'RichTextAttr':
        """ This function combines the list styleâs base attributes and the level style matching the given indent, returning the combined attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def GetCombinedStyleForLevel(self, level, styleSheet=None) -> 'RichTextAttr':
        """ This function combines the list styleâs base attributes and the style for the specified level, returning the combined attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def GetLevelAttributes(self, level: int) -> 'RichTextAttr':
        """ Returns the style for the given level.

            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def GetLevelCount(self) -> int:
        """ Returns the number of levels.

            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def IsNumbered(self, level: int) -> bool:
        """ Returns True if the given level has numbered list attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def SetLevelAttributes(self, level, attr) -> None:
        """ Sets the style for the given level.

            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    LevelCount: int  # See GetLevelCount



class RichTextField(RichTextParagraphLayoutBox):
    """ This class implements the general concept of a field, an object that
represents additional functionality such as a footnote, a bookmark, a
page number, a table of contents, and so on.

        Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def AcceptsFocus(self) -> bool:
        """ Returns True if objects of this class can accept the focus, i.e. a call to SetFocusObject is possible.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def CalculateRange(self, start: int) -> None:
        """ Calculates the range of the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def CanEditProperties(self) -> bool:
        """ Returns True if we can edit the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def Clone(self) -> 'RichTextObject':
        """ Clones the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def Copy(self, obj: 'richtext.RichTextField') -> None:
        """ obj (wx.richtext.RichTextField) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ Draw the item, within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def EditProperties(self, parent, buffer) -> bool:
        """ Edits the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def GetFieldType(self) -> str:
        """ string

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def GetPropertiesMenuLabel(self) -> str:
        """ Returns the label to be used for the properties context menu item.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ Returns the object size for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def GetXMLNodeName(self) -> str:
        """ Returns the XML node name of this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def IsAtomic(self) -> bool:
        """ If a field has children, we donât want the user to be able to edit it.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def IsEmpty(self) -> bool:
        """ Returns True if the buffer is empty.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def IsTopLevel(self) -> bool:
        """ Returns True if this object is top-level, i.e. contains its own paragraphs, such as a text box.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ Lay the item out at the specified position with the given size constraint.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def SetFieldType(self, fieldType: str) -> None:
        """ fieldType (string) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def UpdateField(self, buffer: 'richtext.RichTextBuffer') -> bool:
        """ Update the field; delegated to the associated field type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    FieldType: str  # See GetFieldType and SetFieldType
    PropertiesMenuLabel: str  # See GetPropertiesMenuLabel
    XMLNodeName: str  # See GetXMLNodeName



class RichTextFieldTypeStandard(RichTextFieldType):
    """ A field type that can handle fields with text or bitmap labels, with a
small range of styles for implementing rectangular fields and fields
that can be used for start and end tags.

        Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def Copy(self, field: 'richtext.RichTextFieldTypeStandard') -> None:
        """ Copies the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def Draw(self, obj, dc, context, range, selection, rect, descent, style) -> bool:
        """ Draw the item, within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ Gets the colour used for drawing the field background.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetBitmap(self) -> 'Bitmap':
        """ Gets the bitmap label for fields of this type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetBorderColour(self) -> 'Colour':
        """ Gets the colour used for drawing the field border.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetDisplayStyle(self) -> int:
        """ Gets the display style for fields of this type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetFont(self) -> 'Font':
        """ Gets the font used for drawing the text label.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetHorizontalMargin(self) -> int:
        """ Gets the horizontal margin surrounding the field object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetHorizontalPadding(self) -> int:
        """ Sets the horizontal padding (the distance between the border and the text).

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetLabel(self) -> str:
        """ Returns the text label for fields of this type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ Returns the object size for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetSize(self, obj, dc, context, style) -> 'Size':
        """ Get the size of the field, given the label, font size, and so on.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetTextColour(self) -> 'Colour':
        """ Gets the colour used for drawing the text label.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetVerticalMargin(self) -> int:
        """ Gets the vertical margin surrounding the field object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetVerticalPadding(self) -> int:
        """ Gets the vertical padding (the distance between the border and the text).

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def Init(self) -> None:
        """ Initialises the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def IsTopLevel(self, obj: 'richtext.RichTextField') -> bool:
        """ Returns True if the display type is RICHTEXT_FIELD_STYLE_COMPOSITE, False otherwise.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def Layout(self, obj, dc, context, rect, parentRect, style) -> bool:
        """ Lay the item out at the specified position with the given size constraint.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used for drawing the field background.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetBitmap(self, bitmap: 'Bitmap') -> None:
        """ Sets the bitmap label for fields of this type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetBorderColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used for drawing the field border.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetDisplayStyle(self, displayStyle: int) -> None:
        """ Sets the display style for fields of this type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the font used for drawing the text label.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetHorizontalMargin(self, margin: int) -> None:
        """ Sets the horizontal margin surrounding the field object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetHorizontalPadding(self, padding: int) -> None:
        """ Sets the horizontal padding (the distance between the border and the text).

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetLabel(self, label: str) -> None:
        """ Sets the text label for fields of this type.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour used for drawing the text label.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetVerticalMargin(self, margin: int) -> None:
        """ Sets the vertical margin surrounding the field object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetVerticalPadding(self, padding: int) -> None:
        """ Sets the vertical padding (the distance between the border and the text).

            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    BackgroundColour: 'Colour'  # See GetBackgroundColour and SetBackgroundColour
    Bitmap: '_Bitmap'  # See GetBitmap and SetBitmap
    BorderColour: 'Colour'  # See GetBorderColour and SetBorderColour
    DisplayStyle: int  # See GetDisplayStyle and SetDisplayStyle
    Font: '_Font'  # See GetFont and SetFont
    HorizontalMargin: int  # See GetHorizontalMargin and SetHorizontalMargin
    HorizontalPadding: int  # See GetHorizontalPadding and SetHorizontalPadding
    Label: str  # See GetLabel and SetLabel
    TextColour: 'Colour'  # See GetTextColour and SetTextColour
    VerticalMargin: int  # See GetVerticalMargin and SetVerticalMargin
    VerticalPadding: int  # See GetVerticalPadding and SetVerticalPadding



RICHTEXT_FIELD_STYLE_COMPOSITE: int  # Creates a composite field; you will probably need to derive a new class to implement UpdateField.

RICHTEXT_FIELD_STYLE_RECTANGLE: int  # Shows a rounded rectangle background.

RICHTEXT_FIELD_STYLE_NO_BORDER: int  # Suppresses the background and border; mostly used with a bitmap label.

RICHTEXT_FIELD_STYLE_START_TAG: int  # Shows a start tag background, with the pointy end facing right.

RICHTEXT_FIELD_STYLE_END_TAG: int  # Shows an end tag background, with the pointy end facing left. ^^

class RichTextBox(RichTextParagraphLayoutBox):
    """ This class implements a floating or inline text box, containing
paragraphs.

        Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def CanEditProperties(self) -> bool:
        """ Returns True if we can edit the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def Clone(self) -> 'RichTextObject':
        """ Clones the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def Copy(self, obj: 'richtext.RichTextBox') -> None:
        """ obj (wx.richtext.RichTextBox) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ Draw the item, within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def EditProperties(self, parent, buffer) -> bool:
        """ Edits the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def GetPropertiesMenuLabel(self) -> str:
        """ Returns the label to be used for the properties context menu item.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def GetXMLNodeName(self) -> str:
        """ Returns the XML node name of this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    PropertiesMenuLabel: str  # See GetPropertiesMenuLabel
    XMLNodeName: str  # See GetXMLNodeName



class RichTextStyleListBox(HtmlListBox):
    """ This is a listbox that can display the styles in a
RichTextStyleSheet, and apply the selection to an associated
RichTextCtrl.

        Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def ApplyStyle(self, i: int) -> None:
        """ Applies the ith  style to the associated rich text control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def ConvertTenthsMMToPixels(self, dc, units) -> int:
        """ Converts units in tenths of a millimetre to device units.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ Creates the window.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def CreateHTML(self, styleDef: 'richtext.RichTextStyleDefinition') -> str:
        """ Creates a suitable HTML fragment for a definition.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def GetApplyOnSelection(self) -> bool:
        """ If the return value is True, clicking on a style name in the list will immediately apply the style to the associated rich text control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def GetRichTextCtrl(self) -> 'RichTextCtrl':
        """ Returns the   wx.richtext.RichTextCtrl  associated with this listbox.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def GetStyle(self, i: int) -> 'RichTextStyleDefinition':
        """ Gets a style for a listbox index.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ Returns the style sheet associated with this listbox.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def GetStyleType(self) -> 'wxRichTextStyleType':
        """ Returns the type of style to show in the list box.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def OnGetItem(self, n: int) -> str:
        """ Returns the HTML for this item.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def OnLeftDown(self, event: 'MouseEvent') -> None:
        """ Implements left click behaviour, applying the clicked style to the   wx.richtext.RichTextCtrl.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def SetApplyOnSelection(self, applyOnSelection: bool) -> None:
        """ If applyOnSelection  is True, clicking on a style name in the list will immediately apply the style to the associated rich text control.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def SetRichTextCtrl(self, ctrl: 'richtext.RichTextCtrl') -> None:
        """ Associates the listbox with a   wx.richtext.RichTextCtrl.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def SetStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> None:
        """ Associates the control with a style sheet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def SetStyleType(self, styleType: RichTextStyleListBox.wxRichTextStyleType) -> None:
        """ Sets the style type to display.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def UpdateStyles(self) -> None:
        """ Updates the list from the associated style sheet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    ApplyOnSelection: bool  # See GetApplyOnSelection and SetApplyOnSelection
    RichTextCtrl: 'RichTextCtrl'  # See GetRichTextCtrl and SetRichTextCtrl
    StyleSheet: 'RichTextStyleSheet'  # See GetStyleSheet and SetStyleSheet
    StyleType: 'wxRichTextStyleType'  # See GetStyleType and SetStyleType



RichTextCommandId: TypeAlias = int  # Enumeration

RICHTEXT_INSERT: int

RICHTEXT_DELETE: int

RICHTEXT_CHANGE_ATTRIBUTES: int

RICHTEXT_CHANGE_STYLE: int

class RichTextFormattingDialog(PropertySheetDialog):
    """ This dialog allows the user to edit a character and/or paragraph
style.

        Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def ApplyStyle(self, ctrl, range, flags=RICHTEXT_SETSTYLE_WITH_UNDO|RICHTEXT_SETSTYLE_OPTIMIZE) -> bool:
        """ Apply attributes to the given range, only changing attributes that need to be changed.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def Create(*args, **kwargs) -> bool:
        """ Creation: see   wx.richtext.RichTextFormattingDialog  âthe constructorâ for details about the parameters.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def GetAttributes(self) -> 'TextAttr':
        """ Gets the attributes being edited.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetColourData() -> 'ColourData':
        """ Returns the custom colour data for use by the colour dialog.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetDialog(win: 'Window') -> 'RichTextFormattingDialog':
        """ Helper for pages to get the top-level dialog.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetDialogAttributes(win: 'Window') -> 'TextAttr':
        """ Helper for pages to get the attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetDialogStyleDefinition(win: 'Window') -> 'RichTextStyleDefinition':
        """ Helper for pages to get the style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetFormattingDialogFactory() -> 'RichTextFormattingDialogFactory':
        """ Returns the object to be used to customize the dialog and provide pages.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def GetImageList(self) -> 'ImageList':
        """ Returns the image list associated with the dialog, used for example if showing the dialog as a toolbook.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetLastPage() -> int:
        """ Returns the page identifier of the last page selected (not the control id).

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def GetOptions(self) -> int:
        """ Gets the dialog options, determining what the interface presents to the user.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetRestoreLastPage() -> bool:
        """ Returns True if the dialog will restore the last-selected page.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def GetStyle(self, ctrl, range) -> bool:
        """ Gets common attributes from the given range and calls SetAttributes .

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def GetStyleDefinition(self) -> 'RichTextStyleDefinition':
        """ Gets the associated style definition, if any.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ Gets the associated style sheet, if any.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def HasOption(self, option: int) -> bool:
        """ Returns True if the given option is present.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def SetAttributes(self, attr: 'TextAttr') -> None:
        """ Sets the attributes to be edited.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def SetColourData(colourData: 'ColourData') -> None:
        """ Sets the custom colour data for use by the colour dialog.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def SetFormattingDialogFactory(factory: 'richtext.RichTextFormattingDialogFactory') -> None:
        """ Sets the formatting factory object to be used for customization and page creation.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def SetImageList(self, imageList: 'ImageList') -> None:
        """ Sets the image list associated with the dialogâs property sheet.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def SetLastPage(lastPage: int) -> None:
        """ Sets the page identifier of the last page selected (not the control id).

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def SetOptions(self, options: int) -> None:
        """ Sets the dialog options, determining what the interface presents to the user.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def SetRestoreLastPage(b: bool) -> None:
        """ Pass True if the dialog should restore the last-selected page.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def SetStyle(self, style, update=True) -> bool:
        """ Sets the attributes and optionally updates the display, if update  is True.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def SetStyleDefinition(self, styleDef, sheet, update=True) -> bool:
        """ Sets the style definition and optionally update the display, if update  is True.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def UpdateDisplay(self) -> bool:
        """ Updates the display.

            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    Attributes: 'TextAttr'  # See GetAttributes and SetAttributes
    ImageList: '_ImageList'  # See GetImageList and SetImageList
    Options: int  # See GetOptions and SetOptions
    StyleDefinition: 'RichTextStyleDefinition'  # See GetStyleDefinition and SetStyleDefinition
    StyleSheet: 'RichTextStyleSheet'  # See GetStyleSheet



class RichTextObjectAddress:
    """ A class for specifying an object anywhere in an object hierarchy,
without using a pointer, necessary since RTC commands may delete and
recreate sub-objects so physical object addresses change.

        Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    def Copy(self, address: 'richtext.RichTextObjectAddress') -> None:
        """ Copies the address.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    def Create(self, topLevelContainer, obj) -> bool:
        """ Creates the address given a container and an object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    def GetAddress(self) -> int:
        """ Returns the array of integers representing the object address.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    def GetObject(self, topLevelContainer: 'richtext.RichTextParagraphLayoutBox') -> 'RichTextObject':
        """ Returns the object specified by the address, given a top level container.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    def Init(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    def SetAddress(self, address: int) -> None:
        """ Sets the address from an array of integers.

            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    Address: int  # See GetAddress and SetAddress



class RichTextPlainText(RichTextObject):
    """ This object represents a single piece of text.

        Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def CalculateRange(self, start: int) -> None:
        """ Calculates the range of the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def CanMerge(self, object, context) -> bool:
        """ Returns True if this object can merge itself with the given one.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def CanSplit(self, context: 'richtext.RichTextDrawingContext') -> bool:
        """ Returns True if this object can potentially be split, by virtue of having different virtual attributes for individual sub-objects.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def Clone(self) -> 'RichTextObject':
        """ Clones the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def Copy(self, obj: 'richtext.RichTextPlainText') -> None:
        """ obj (wx.richtext.RichTextPlainText) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def DeleteRange(self, range: 'richtext.RichTextRange') -> bool:
        """ Deletes the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def DoSplit(self, pos: int) -> 'RichTextObject':
        """ Do a split from pos, returning an object containing the second part, and setting the first part in âthisâ.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ Draw the item, within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def GetFirstLineBreakPosition(self, pos: int) -> int:
        """ Get the first position from pos that has a line break character.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ Returns the object size for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def GetText(self) -> str:
        """ Returns the text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def GetTextForRange(self, range: 'richtext.RichTextRange') -> str:
        """ Returns any text in this object for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def GetXMLNodeName(self) -> str:
        """ Returns the XML node name of this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def ImportFromXML(self, buffer, node, handler, recurse) -> bool:
        """ Imports this object from XML.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def IsEmpty(self) -> bool:
        """ Returns True if the object is empty.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ Lay the item out at the specified position with the given size constraint.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def Merge(self, object, context) -> bool:
        """ Returns True if this object merged itself with the given one.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def SetText(self, text: str) -> None:
        """ Sets the text.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def Split(self, context: 'richtext.RichTextDrawingContext') -> 'RichTextObject':
        """ Returns the final object in the split objects if this object was split due to differences between sub-object virtual attributes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def UsesParagraphAttributes(self) -> bool:
        """ Does this object take note of paragraph attributes? Text and image objects donât.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    Text: str  # See GetText and SetText
    XMLNodeName: str  # See GetXMLNodeName



class RichTextHTMLHandler(RichTextFileHandler):
    """ Handles HTML output (only) for RichTextCtrl content.

        Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
    """
    def __init__(self, name="HTML", ext="html", type=RICHTEXT_TYPE_HTML) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def ClearTemporaryImageLocations(self) -> None:
        """ Clears the image locations generated by the last operation.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def DeleteTemporaryImages(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def GetFontSizeMapping(self) -> int:
        """ Returns the mapping for converting point sizes to HTML font sizes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def GetTempDir(self) -> str:
        """ Returns the directory used to store temporary image files.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def GetTemporaryImageLocations(self) -> list[str]:
        """ Returns the image locations for the last operation.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    @staticmethod
    def SetFileCounter(counter: int) -> None:
        """ Reset the file counter, in case, for example, the same names are required each time.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def SetFontSizeMapping(self, fontSizeMapping: int) -> None:
        """ Sets the mapping for converting point sizes to HTML font sizes.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def SetTempDir(self, tempDir: str) -> None:
        """ Sets the directory for storing temporary files.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def SetTemporaryImageLocations(self, locations: list[str]) -> None:
        """ Sets the list of image locations generated by the last operation.

            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    FontSizeMapping: int  # See GetFontSizeMapping and SetFontSizeMapping
    TempDir: str  # See GetTempDir and SetTempDir
    TemporaryImageLocations: list[str]  # See GetTemporaryImageLocations and SetTemporaryImageLocations



RICHTEXT_HANDLER_SAVE_IMAGES_TO_BASE64: int

RICHTEXT_HANDLER_SAVE_IMAGES_TO_MEMORY: int

RICHTEXT_HANDLER_SAVE_IMAGES_TO_FILES: int

RICHTEXT_HANDLER_NO_HEADER_FOOTER: int

RICHTEXT_HANDLER_USE_CSS: int

class RichTextPlainTextHandler(RichTextFileHandler):
    """ Implements saving a buffer to plain text.

        Source: https://docs.wxpython.org/wx.richtext.RichTextPlainTextHandler.html
    """
    def __init__(self, name="Text", ext="txt", type=RICHTEXT_TYPE_TEXT) -> None:
        """ name (string) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainTextHandler.html
        """

    def CanLoad(self) -> bool:
        """ Returns True if we can load using this handler.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainTextHandler.html
        """

    def CanSave(self) -> bool:
        """ Returns True if we can save using this handler.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainTextHandler.html
        """

    def DoLoadFile(self, buffer, stream) -> bool:
        """ Override to load content from stream  into buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainTextHandler.html
        """

    def DoSaveFile(self, buffer, stream) -> bool:
        """ Override to save content to stream  from buffer.

            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainTextHandler.html
        """



class RichTextXMLHandler(RichTextFileHandler):
    """ A handler for loading and saving content in an XML format specific to
RichTextBuffer.

        Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
    """
    def __init__(self, name="XML", ext="xml", type=RICHTEXT_TYPE_XML) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """

    def CanLoad(self) -> bool:
        """ Returns True.

            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """

    def CanSave(self) -> bool:
        """ Returns True.

            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """

    @staticmethod
    def ClearNodeToClassMap() -> None:
        """ Cleans up the mapping between node name and C++ class.

            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """

    def ExportXML(self, stream, obj, level) -> bool:
        """ Recursively exports an object to the stream.

            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """

    def ImportXML(self, buffer, obj, node) -> bool:
        """ Recursively imports an object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """

    @staticmethod
    def RegisterNodeName(nodeName, className) -> None:
        """ Call with XML node name, C++ class name so that RTC can read in the node.

            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """



RICHTEXT_HANDLER_INCLUDE_STYLESHEET: int

RichTextOddEvenPage: TypeAlias = int  # Enumeration

RICHTEXT_PAGE_ODD: int

RICHTEXT_PAGE_EVEN: int

RICHTEXT_PAGE_ALL: int

RichTextPageLocation: TypeAlias = int  # Enumeration

RICHTEXT_PAGE_LEFT: int

RICHTEXT_PAGE_CENTRE: int

RICHTEXT_PAGE_RIGHT: int

class RichTextCompositeObject(RichTextObject):
    """ Objects of this class can contain other objects.

        Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
    """
    def __init__(self, parent: Optional['richtext.RichTextObject']=None) -> None:
        """ parent (wx.richtext.RichTextObject) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def AppendChild(self, child: 'richtext.RichTextObject') -> int:
        """ Appends a child, returning the position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def CalculateRange(self, start: int) -> None:
        """ Calculates the range of the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def Copy(self, obj: 'richtext.RichTextCompositeObject') -> None:
        """ obj (wx.richtext.RichTextCompositeObject) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def Defragment(self, context, range=RICHTEXT_ALL) -> bool:
        """ Recursively merges all pieces that can be merged.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def DeleteChildren(self) -> bool:
        """ Deletes all the children.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def DeleteRange(self, range: 'richtext.RichTextRange') -> bool:
        """ Deletes the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def FindPosition(self, dc, context, index, forceLineStart) -> tuple:
        """ Finds the absolute position and row height for the given character position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def GetChild(self, n: int) -> 'RichTextObject':
        """ Returns the nth child.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def GetChildAtPosition(self, pos: int) -> 'RichTextObject':
        """ Returns the child object at the given character position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def GetChildCount(self) -> int:
        """ Returns the number of children.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def GetChildren(self) -> 'RichTextObjectList':
        """ Returns the children.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ Returns the object size for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def GetTextForRange(self, range: 'richtext.RichTextRange') -> str:
        """ Returns any text in this object for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ Hit-testing: returns a flag indicating hit test details, plus information about position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def InsertChild(self, child, inFrontOf) -> bool:
        """ Inserts the child in front of the given object, or at the beginning.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def Invalidate(self, invalidRange: 'richtext.RichTextRange'=RICHTEXT_ALL) -> None:
        """ Invalidates the object at the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def IsAtomic(self) -> bool:
        """ Returns True if no user editing can be done inside the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def IsComposite(self) -> bool:
        """ Returns True if this object is composite.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def IsEmpty(self) -> bool:
        """ Returns True if the buffer is empty.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def Move(self, pt: Union[tuple[int, int], 'Point']) -> None:
        """ Moves the object recursively, by adding the offset from old to new.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def RemoveChild(self, child, deleteChild=False) -> bool:
        """ Removes and optionally deletes the specified child.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    ChildCount: int  # See GetChildCount
    Children: 'RichTextObjectList'  # See GetChildren



class RichTextImage(RichTextObject):
    """ This class implements a graphic object.

        Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def CanEditProperties(self) -> bool:
        """ Returns True if we can edit the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def Clone(self) -> 'RichTextObject':
        """ Clones the image object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def Copy(self, obj: 'richtext.RichTextImage') -> None:
        """ Copies the image object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ Draw the item, within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def EditProperties(self, parent, buffer) -> bool:
        """ Edits the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetImageBlock(self) -> 'RichTextImageBlock':
        """ Returns the image block containing the raw data.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetImageCache(self) -> 'Bitmap':
        """ Returns the image cache (a scaled bitmap).

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetImageState(self) -> int:
        """ Gets the image state.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetNaturalSize(self) -> 'TextAttrSize':
        """ Returns the ânaturalâ size for this object - the image size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetOriginalImageSize(self) -> 'Size':
        """ Gets the original image size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetPropertiesMenuLabel(self) -> str:
        """ Returns the label to be used for the properties context menu item.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ Returns the object size for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetXMLNodeName(self) -> str:
        """ Returns the XML node name of this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def ImportFromXML(self, buffer, node, handler, recurse) -> bool:
        """ Imports this object from XML.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def IsEmpty(self) -> bool:
        """ Returns True if the object is empty.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def IsFloatable(self) -> bool:
        """ Returns True if this class of object is floatable.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ Lay the item out at the specified position with the given size constraint.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def LoadAndScaleImageCache(self, image, sz, context, changed) -> tuple:
        """ Do the loading and scaling.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def LoadImageCache(self, dc, context, retImageSize, resetCache=False, parentSize=DefaultSize) -> bool:
        """ Creates a cached image at the required size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def ResetImageCache(self) -> None:
        """ Resets the image cache.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def SetImageCache(self, bitmap: 'Bitmap') -> None:
        """ Sets the image cache.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def SetImageState(self, state: int) -> None:
        """ Sets the image state.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def SetOriginalImageSize(self, sz: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the original image size.

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def UsesParagraphAttributes(self) -> bool:
        """ Returns True if this object takes note of paragraph attributes (text and image objects donât).

            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    ImageBlock: 'RichTextImageBlock'  # See GetImageBlock
    ImageCache: 'Bitmap'  # See GetImageCache and SetImageCache
    ImageState: int  # See GetImageState and SetImageState
    NaturalSize: 'TextAttrSize'  # See GetNaturalSize
    OriginalImageSize: 'Size'  # See GetOriginalImageSize and SetOriginalImageSize
    PropertiesMenuLabel: str  # See GetPropertiesMenuLabel
    XMLNodeName: str  # See GetXMLNodeName



class TextAttrBorders:
    """ A class representing a rich text objectâs borders.

        Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def Apply(self, borders, compareWith=None) -> bool:
        """ Applies border to this object, but not if the same as compareWith.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def EqPartial(self, borders, weakTest=True) -> bool:
        """ Partial equality test.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def GetBottom(self) -> 'TextAttrBorder':
        """ wx.richtext.TextAttrBorder

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def GetLeft(self) -> 'TextAttrBorder':
        """ wx.richtext.TextAttrBorder

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def GetRight(self) -> 'TextAttrBorder':
        """ wx.richtext.TextAttrBorder

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def GetTop(self) -> 'TextAttrBorder':
        """ wx.richtext.TextAttrBorder

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def IsValid(self) -> bool:
        """ Returns True if at least one border is valid.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def RemoveStyle(self, attr: 'richtext.TextAttrBorders') -> bool:
        """ Removes the specified attributes from this object.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def Reset(self) -> None:
        """ Resets all borders.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def SetColour(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def SetStyle(self, style: int) -> None:
        """ Sets the style of all borders.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def SetWidth(self, *args, **kw) -> None:
        """ Sets the width of all borders.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def __bool__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def __nonzero__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    Bottom: 'TextAttrBorder'  # See GetBottom
    Left: 'TextAttrBorder'  # See GetLeft
    Right: 'TextAttrBorder'  # See GetRight
    Top: 'TextAttrBorder'  # See GetTop
    m_bottom: Any  # A public C++ attribute of type TextAttrBorder     .
    m_left: Any  # A public C++ attribute of type TextAttrBorder     .
    m_right: Any  # A public C++ attribute of type TextAttrBorder     .
    m_top: Any  # A public C++ attribute of type TextAttrBorder     .



class TextAttrSize:
    """ A class for representing width and height.

        Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def Apply(self, dims, compareWith=None) -> bool:
        """ Apply to this object, but not if the same as compareWith.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def EqPartial(self, size, weakTest=True) -> bool:
        """ Partial equality test.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def GetHeight(self) -> 'TextAttrDimension':
        """ Gets the height.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def GetWidth(self) -> 'TextAttrDimension':
        """ Returns the width.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def IsValid(self) -> bool:
        """ Is the size valid?

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def RemoveStyle(self, attr: 'richtext.TextAttrSize') -> bool:
        """ Removes the specified attributes from this object.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def Reset(self) -> None:
        """ Resets the width and height dimensions.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def SetHeight(self, *args, **kw) -> None:
        """ Sets the height.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def SetWidth(self, *args, **kw) -> None:
        """ Sets the width.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def __bool__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def __nonzero__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    Height: 'TextAttrDimension'  # See GetHeight and SetHeight
    Width: 'TextAttrDimension'  # See GetWidth and SetWidth
    m_height: Any  # A public C++ attribute of type TextAttrDimension     .
    m_width: Any  # A public C++ attribute of type TextAttrDimension     .



class RichTextParagraph(RichTextCompositeObject):
    """ This object represents a single paragraph containing various objects
such as text content, images, and further paragraph layout objects.

        Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def AllocateLine(self, pos: int) -> 'RichTextLine':
        """ Allocates or reuses a line object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def ApplyParagraphStyle(self, line, attr, rect, dc) -> None:
        """ Applies paragraph styles such as centering to the wrapped lines.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def CalculateRange(self, start: int) -> None:
        """ Calculates the range of the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    @staticmethod
    def ClearDefaultTabs() -> None:
        """ Clears the default tabstop array.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def ClearLines(self) -> None:
        """ Clears the cached lines.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def ClearUnusedLines(self, lineCount: int) -> bool:
        """ Clears remaining unused line objects, if any.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def Clone(self) -> 'RichTextObject':
        """ Clones the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def Copy(self, obj: 'richtext.RichTextParagraph') -> None:
        """ Copies the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ Draw the item, within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def FindObjectAtPosition(self, position: int) -> 'RichTextObject':
        """ Finds the object at the given position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def FindPosition(self, dc, context, index, forceLineStart) -> tuple:
        """ Finds the absolute position and row height for the given character position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def FindWrapPosition(self, range, dc, context, availableSpace, wrapPosition, partialExtents) -> bool:
        """ Finds a suitable wrap position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetBulletText(self) -> str:
        """ Returns the bullet text for this paragraph.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetCombinedAttributes(self, *args, **kw) -> 'RichTextAttr':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetContiguousPlainText(self, text, range, fromStart=True) -> bool:
        """ Returns the plain text searching from the start or end of the range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    @staticmethod
    def GetDefaultTabs() -> int:
        """ Returns the default tabstop array.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetFirstLineBreakPosition(self, pos: int) -> int:
        """ Returns the first position from pos that has a line break character.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetImpactedByFloatingObjects(self) -> int:
        """ Whether the paragraph is impacted by floating objects from above.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetLines(self) -> Any:
        """ Returns the cached lines.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ Returns the object size for the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetXMLNodeName(self) -> str:
        """ Returns the XML node name of this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ Hit-testing: returns a flag indicating hit test details, plus information about position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def Init(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    @staticmethod
    def InitDefaultTabs() -> None:
        """ Creates a default tabstop array.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def InsertText(self, pos, text) -> bool:
        """ Inserts text at the given position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ Lay the item out at the specified position with the given size constraint.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def LayoutFloat(self, dc, context, rect, parentRect, style, floatCollector) -> None:
        """ Lays out the floating objects.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def MoveFromList(self, list: list['richtext.RichTextList']) -> None:
        """ Adds content back from a list.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def MoveToList(self, obj, list) -> None:
        """ Moves content to a list from this point.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def SetImpactedByFloatingObjects(self, i: int) -> None:
        """ Sets whether the paragraph is impacted by floating objects from above.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def SplitAt(self, pos, previousObject=None) -> 'RichTextObject':
        """ Splits an object at this position if necessary, and returns the previous object, or None if inserting at the beginning.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    BulletText: str  # See GetBulletText
    CombinedAttributes: 'RichTextAttr'  # See GetCombinedAttributes
    ImpactedByFloatingObjects: int  # See GetImpactedByFloatingObjects and SetImpactedByFloatingObjects
    Lines: Any  # See GetLines
    XMLNodeName: str  # See GetXMLNodeName



class RichTextCharacterStyleDefinition(RichTextStyleDefinition):
    """ This class represents a character style definition, usually added to a
RichTextStyleSheet.

        Source: https://docs.wxpython.org/wx.richtext.RichTextCharacterStyleDefinition.html
    """
    def __init__(self, name: str="") -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCharacterStyleDefinition.html
        """



class RichTextParagraphStyleDefinition(RichTextStyleDefinition):
    """ This class represents a paragraph style definition, usually added to a
RichTextStyleSheet.

        Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphStyleDefinition.html
    """
    def __init__(self, name: str="") -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphStyleDefinition.html
        """

    def GetNextStyle(self) -> str:
        """ Returns the style that should normally follow this style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphStyleDefinition.html
        """

    def SetNextStyle(self, name: str) -> None:
        """ Sets the style that should normally follow this style.

            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphStyleDefinition.html
        """

    NextStyle: str  # See GetNextStyle and SetNextStyle



class TextBoxAttr:
    """ A class representing the box attributes of a rich text object.

        Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def AddFlag(self, flag: TextBoxAttrFlags) -> None:
        """ Adds this flag.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def Apply(self, style, compareWith=None) -> bool:
        """ Merges the given attributes.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def EqPartial(self, attr, weakTest=True) -> bool:
        """ Partial equality test, ignoring unset attributes.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBorder(self) -> 'TextAttrBorders':
        """ Returns the borders.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBottom(self) -> 'TextAttrDimension':
        """ Returns the bottom position.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBottomBorder(self) -> 'TextAttrBorder':
        """ Returns the bottom border.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBottomMargin(self) -> 'TextAttrDimension':
        """ Returns the bottom margin.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBottomOutline(self) -> 'TextAttrBorder':
        """ Returns the bottom outline.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBottomPadding(self) -> 'TextAttrDimension':
        """ Returns the bottom padding value.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBoxStyleName(self) -> str:
        """ Returns the box style name.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetClearMode(self) -> 'TextBoxAttrClearStyle':
        """ Returns the clear mode - whether to wrap text after object.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetCollapseBorders(self) -> 'TextBoxAttrCollapseMode':
        """ Returns the collapse mode - whether to collapse borders.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetCornerRadius(self) -> 'TextAttrDimension':
        """ wx.richtext.TextAttrDimension

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetFlags(self) -> int:
        """ Returns the flags.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetFloatMode(self) -> 'TextBoxAttrFloatStyle':
        """ Returns the float mode.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetHeight(self) -> 'TextAttrDimension':
        """ Returns the object height.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetLeft(self) -> 'TextAttrDimension':
        """ Returns the left position.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetLeftBorder(self) -> 'TextAttrBorder':
        """ Returns the left border.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetLeftMargin(self) -> 'TextAttrDimension':
        """ Returns the left margin.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetLeftOutline(self) -> 'TextAttrBorder':
        """ Returns the left outline.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetLeftPadding(self) -> 'TextAttrDimension':
        """ Returns the left padding value.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetMargins(self) -> 'TextAttrDimensions':
        """ Returns the margin values.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetMaxSize(self) -> 'TextAttrSize':
        """ Returns the object maximum size.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetMinSize(self) -> 'TextAttrSize':
        """ Returns the object minimum size.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetOutline(self) -> 'TextAttrBorders':
        """ Returns the outline.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetPadding(self) -> 'TextAttrDimensions':
        """ Returns the padding values.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetPosition(self) -> 'TextAttrDimensions':
        """ Returns the position.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetRight(self) -> 'TextAttrDimension':
        """ Returns the right position.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetRightBorder(self) -> 'TextAttrBorder':
        """ Returns the right border.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetRightMargin(self) -> 'TextAttrDimension':
        """ Returns the right margin.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetRightOutline(self) -> 'TextAttrBorder':
        """ Returns the right outline.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetRightPadding(self) -> 'TextAttrDimension':
        """ Returns the right padding value.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetShadow(self) -> 'TextAttrShadow':
        """ Returns the box shadow attributes.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetSize(self) -> 'TextAttrSize':
        """ Returns the object size.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetTop(self) -> 'TextAttrDimension':
        """ Returns the top position.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetTopBorder(self) -> 'TextAttrBorder':
        """ Returns the top border.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetTopMargin(self) -> 'TextAttrDimension':
        """ Returns the top margin.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetTopOutline(self) -> 'TextAttrBorder':
        """ Returns the top outline.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetTopPadding(self) -> 'TextAttrDimension':
        """ Returns the top padding value.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetVerticalAlignment(self) -> int:
        """ Returns the vertical alignment.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetWhitespaceMode(self) -> 'TextBoxAttrWhitespaceMode':
        """ Returns the whitespace mode.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetWidth(self) -> 'TextAttrDimension':
        """ Returns the object width.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasBoxStyleName(self) -> bool:
        """ Returns True if the box style name is present.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasClearMode(self) -> bool:
        """ Returns True if we have a clear flag.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasCollapseBorders(self) -> bool:
        """ Returns True if the collapse borders flag is present.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasCornerRadius(self) -> bool:
        """ Returns True if the corner radius flag is present.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasFlag(self, flag: TextBoxAttrFlags) -> bool:
        """ Is this flag present?

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasFloatMode(self) -> bool:
        """ Returns True if float mode is active.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasVerticalAlignment(self) -> bool:
        """ Returns True if a vertical alignment flag is present.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasWhitespaceMode(self) -> bool:
        """ Returns True if the whitespace flag is present.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def Init(self) -> None:
        """ Initialises this object.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def IsDefault(self) -> bool:
        """ Returns True if no attributes are set.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def IsFloating(self) -> bool:
        """ Returns True if this object is floating.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def RemoveFlag(self, flag: TextBoxAttrFlags) -> None:
        """ Removes this flag.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def RemoveStyle(self, attr: 'richtext.TextBoxAttr') -> bool:
        """ Removes the specified attributes from this object.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def Reset(self) -> None:
        """ Resets this object.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetBoxStyleName(self, name: str) -> None:
        """ Sets the box style name.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetClearMode(self, mode: TextBoxAttrClearStyle) -> None:
        """ Set the clear mode.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetCollapseBorders(self, collapse: TextBoxAttrCollapseMode) -> None:
        """ Sets the collapse mode - whether to collapse borders.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetCornerRadius(self, dim: 'richtext.TextAttrDimension') -> None:
        """ Sets the corner radius value.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetFlags(self, flags: int) -> None:
        """ Sets the flags.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetFloatMode(self, mode: TextBoxAttrFloatStyle) -> None:
        """ Sets the float mode.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetMaxSize(self, sz: 'richtext.TextAttrSize') -> None:
        """ Sets the object maximum size.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetMinSize(self, sz: 'richtext.TextAttrSize') -> None:
        """ Sets the object minimum size.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetSize(self, sz: 'richtext.TextAttrSize') -> None:
        """ Sets the object size.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetVerticalAlignment(self, verticalAlignment: int) -> None:
        """ Sets the vertical alignment.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetWhitespaceMode(self, whitespace: TextBoxAttrWhitespaceMode) -> None:
        """ Sets the whitespace mode.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality test.

            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    Border: 'TextAttrBorders'  # See GetBorder
    Bottom: 'TextAttrDimension'  # See GetBottom
    BottomBorder: 'TextAttrBorder'  # See GetBottomBorder
    BottomMargin: 'TextAttrDimension'  # See GetBottomMargin
    BottomOutline: 'TextAttrBorder'  # See GetBottomOutline
    BottomPadding: 'TextAttrDimension'  # See GetBottomPadding
    BoxStyleName: str  # See GetBoxStyleName and SetBoxStyleName
    ClearMode: 'TextBoxAttrClearStyle'  # See GetClearMode and SetClearMode
    CollapseBorders: 'TextBoxAttrCollapseMode'  # See GetCollapseBorders and SetCollapseBorders
    CornerRadius: 'TextAttrDimension'  # See GetCornerRadius and SetCornerRadius
    Flags: int  # See GetFlags and SetFlags
    FloatMode: 'TextBoxAttrFloatStyle'  # See GetFloatMode and SetFloatMode
    Height: 'TextAttrDimension'  # See GetHeight
    Left: 'TextAttrDimension'  # See GetLeft
    LeftBorder: 'TextAttrBorder'  # See GetLeftBorder
    LeftMargin: 'TextAttrDimension'  # See GetLeftMargin
    LeftOutline: 'TextAttrBorder'  # See GetLeftOutline
    LeftPadding: 'TextAttrDimension'  # See GetLeftPadding
    Margins: 'TextAttrDimensions'  # See GetMargins
    MaxSize: 'TextAttrSize'  # See GetMaxSize and SetMaxSize
    MinSize: 'TextAttrSize'  # See GetMinSize and SetMinSize
    Outline: 'TextAttrBorders'  # See GetOutline
    Padding: 'TextAttrDimensions'  # See GetPadding
    Position: 'TextAttrDimensions'  # See GetPosition
    Right: 'TextAttrDimension'  # See GetRight
    RightBorder: 'TextAttrBorder'  # See GetRightBorder
    RightMargin: 'TextAttrDimension'  # See GetRightMargin
    RightOutline: 'TextAttrBorder'  # See GetRightOutline
    RightPadding: 'TextAttrDimension'  # See GetRightPadding
    Shadow: 'TextAttrShadow'  # See GetShadow
    Size: 'TextAttrSize'  # See GetSize and SetSize
    Top: 'TextAttrDimension'  # See GetTop
    TopBorder: 'TextAttrBorder'  # See GetTopBorder
    TopMargin: 'TextAttrDimension'  # See GetTopMargin
    TopOutline: 'TextAttrBorder'  # See GetTopOutline
    TopPadding: 'TextAttrDimension'  # See GetTopPadding
    VerticalAlignment: int  # See GetVerticalAlignment and SetVerticalAlignment
    WhitespaceMode: 'TextBoxAttrWhitespaceMode'  # See GetWhitespaceMode and SetWhitespaceMode
    Width: 'TextAttrDimension'  # See GetWidth
    m_border: Any  # A public C++ attribute of type TextAttrBorders     .
    m_boxStyleName: Any  # A public C++ attribute of type string.
    m_clearMode: Any  # A public C++ attribute of type TextBoxAttrClearStyle     .
    m_collapseMode: Any  # A public C++ attribute of type TextBoxAttrCollapseMode     .
    m_cornerRadius: Any  # A public C++ attribute of type TextAttrDimension     .
    m_flags: Any  # A public C++ attribute of type int.
    m_floatMode: Any  # A public C++ attribute of type TextBoxAttrFloatStyle     .
    m_margins: Any  # A public C++ attribute of type TextAttrDimensions     .
    m_maxSize: Any  # A public C++ attribute of type TextAttrSize     .
    m_minSize: Any  # A public C++ attribute of type TextAttrSize     .
    m_outline: Any  # A public C++ attribute of type TextAttrBorders     .
    m_padding: Any  # A public C++ attribute of type TextAttrDimensions     .
    m_position: Any  # A public C++ attribute of type TextAttrDimensions     .
    m_shadow: Any  # A public C++ attribute of type TextAttrShadow     .
    m_size: Any  # A public C++ attribute of type TextAttrSize     .
    m_verticalAlignment: Any  # A public C++ attribute of type TextBoxAttrVerticalAlignment     .
    m_whitespaceMode: Any  # A public C++ attribute of type TextBoxAttrWhitespaceMode     .



RichTextFileType: TypeAlias = int  # Enumeration

RICHTEXT_TYPE_TEXT: int

RICHTEXT_TYPE_XML: int

RICHTEXT_TYPE_HTML: int

RICHTEXT_TYPE_RTF: int

RICHTEXT_TYPE_PDF: int

class RichTextCell(RichTextBox):
    """ RichTextCell is the cell in a table, in which the user can type.

        Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def CanEditProperties(self) -> bool:
        """ Returns True if we can edit the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def Clone(self) -> 'RichTextObject':
        """ Clones the object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def Copy(self, obj: 'richtext.RichTextCell') -> None:
        """ obj (wx.richtext.RichTextCell) â

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ Draw the item, within the given range.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def EditProperties(self, parent, buffer) -> bool:
        """ Edits the objectâs properties via a GUI.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def GetColSpan(self) -> int:
        """ Returns the number of columns spanned by the cell.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def GetPropertiesMenuLabel(self) -> str:
        """ Returns the label to be used for the properties context menu item.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def GetRowSpan(self) -> int:
        """ Returns the number of rows spanned by the cell.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def GetXMLNodeName(self) -> str:
        """ Returns the XML node name of this object.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ Hit-testing: returns a flag indicating hit test details, plus information about position.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def SetColSpan(self, span: int) -> None:
        """ Set the number of columns spanned by the cell.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def SetRowSpan(self, span: int) -> None:
        """ Set the number of rows spanned by the cell.

            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    ColSpan: int  # See GetColSpan and SetColSpan
    PropertiesMenuLabel: str  # See GetPropertiesMenuLabel
    RowSpan: int  # See GetRowSpan and SetRowSpan
    XMLNodeName: str  # See GetXMLNodeName



class TextAttrBorder:
    """ A class representing a rich text object border.

        Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def AddFlag(self, flag: int) -> None:
        """ Adds a border flag.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def Apply(self, border, compareWith=None) -> bool:
        """ Applies the border to this object, but not if the same as compareWith.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def EqPartial(self, border, weakTest=True) -> bool:
        """ Partial equality test.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def GetColour(self) -> 'Colour':
        """ Gets the colour.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def GetColourLong(self) -> int:
        """ Gets the colour as a long.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def GetFlags(self) -> int:
        """ Returns the border flags.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def GetStyle(self) -> int:
        """ Gets the border style.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def GetWidth(self) -> 'TextAttrDimension':
        """ Gets the border width.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def HasColour(self) -> bool:
        """ True if the border has a valid colour.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def HasStyle(self) -> bool:
        """ True if the border has a valid style.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def HasWidth(self) -> bool:
        """ True if the border has a valid width.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def IsDefault(self) -> bool:
        """ True if the border has no attributes set.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def IsValid(self) -> bool:
        """ True if the border is valid.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def MakeValid(self) -> None:
        """ Set the valid flag for this border.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def RemoveFlag(self, flag: int) -> None:
        """ Removes a border flag.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def RemoveStyle(self, attr: 'richtext.TextAttrBorder') -> bool:
        """ Removes the specified attributes from this object.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def Reset(self) -> None:
        """ Resets the border style, colour, width and flags.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def SetColour(self, *args, **kw) -> None:
        """ Sets the border colour.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def SetFlags(self, flags: int) -> None:
        """ Sets the border flags.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def SetStyle(self, style: int) -> None:
        """ Sets the border style.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def SetWidth(self, *args, **kw) -> None:
        """ Sets the border width.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def __bool__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def __nonzero__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    Colour: '_Colour'  # See GetColour and SetColour
    ColourLong: int  # See GetColourLong
    Flags: int  # See GetFlags and SetFlags
    Style: int  # See GetStyle and SetStyle
    Width: 'TextAttrDimension'  # See GetWidth and SetWidth
    m_borderColour: Any  # A public C++ attribute of type long.
    m_borderStyle: Any  # A public C++ attribute of type int.
    m_borderWidth: Any  # A public C++ attribute of type TextAttrDimension     .
    m_flags: Any  # A public C++ attribute of type int.



class TextAttrDimension:
    """ A class representing a rich text dimension, including units and
position.

        Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def Apply(self, dim, compareWith=None) -> bool:
        """ Apply the dimension, but not those identical to compareWith  if present.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def EqPartial(self, dim, weakTest=True) -> bool:
        """ Partial equality test.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def GetFlags(self) -> 'TextAttrDimensionFlags':
        """ Gets the dimension flags.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def GetPosition(self) -> 'TextBoxAttrPosition':
        """ Gets the position flags.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def GetUnits(self) -> 'TextAttrUnits':
        """ Gets the units of the dimension.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def GetValue(self) -> int:
        """ Returns the integer value of the dimension.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def GetValueMM(self) -> float:
        """ Returns the floating-pointing value of the dimension in mm.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def IsValid(self) -> bool:
        """ Returns True if the dimension is valid.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def Reset(self) -> None:
        """ Resets the dimension value and flags.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def SetFlags(self, flags: 'richtext.TextAttrDimensionFlags') -> None:
        """ Sets the dimension flags.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def SetPosition(self, pos: TextBoxAttrPosition) -> None:
        """ Sets the position flags.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def SetUnits(self, units: TextAttrUnits) -> None:
        """ Sets the units of the dimension.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def SetValid(self, b: bool) -> None:
        """ Sets the valid flag.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def SetValue(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def SetValueMM(self, value: float) -> None:
        """ Sets the value of the dimension in mm.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def __bool__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def __nonzero__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    Flags: 'TextAttrDimensionFlags'  # See GetFlags and SetFlags
    Position: 'TextBoxAttrPosition'  # See GetPosition and SetPosition
    Units: 'TextAttrUnits'  # See GetUnits and SetUnits
    Value: int  # See GetValue and SetValue
    ValueMM: float  # See GetValueMM and SetValueMM
    m_flags: Any  # A public C++ attribute of type TextAttrDimensionFlags     .
    m_value: Any  # A public C++ attribute of type int.



TextAttrUnits: TypeAlias = int  # Enumeration

TEXT_ATTR_UNITS_TENTHS_MM: int

TEXT_ATTR_UNITS_PIXELS: int

TEXT_ATTR_UNITS_PERCENTAGE: int

TEXT_ATTR_UNITS_POINTS: int

TEXT_ATTR_UNITS_HUNDREDTHS_POINT: int

TEXT_ATTR_UNITS_MASK: int

class TextAttrDimensions:
    """ A class for left, right, top and bottom dimensions.

        Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def Apply(self, dims, compareWith=None) -> bool:
        """ Apply to âthisâ, but not if the same as compareWith.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def EqPartial(self, dims, weakTest=True) -> bool:
        """ Partial equality test.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def GetBottom(self) -> 'TextAttrDimension':
        """ wx.richtext.TextAttrDimension

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def GetLeft(self) -> 'TextAttrDimension':
        """ wx.richtext.TextAttrDimension

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def GetRight(self) -> 'TextAttrDimension':
        """ wx.richtext.TextAttrDimension

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def GetTop(self) -> 'TextAttrDimension':
        """ wx.richtext.TextAttrDimension

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def IsValid(self) -> bool:
        """ Are all dimensions valid?

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def RemoveStyle(self, attr: 'richtext.TextAttrDimensions') -> bool:
        """ Remove specified attributes from this object.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def Reset(self) -> None:
        """ Resets the value and flags for all dimensions.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def __bool__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def __nonzero__(self) -> int:
        """ int

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    Bottom: 'TextAttrDimension'  # See GetBottom
    Left: 'TextAttrDimension'  # See GetLeft
    Right: 'TextAttrDimension'  # See GetRight
    Top: 'TextAttrDimension'  # See GetTop
    m_bottom: Any  # A public C++ attribute of type TextAttrDimension     .
    m_left: Any  # A public C++ attribute of type TextAttrDimension     .
    m_right: Any  # A public C++ attribute of type TextAttrDimension     .
    m_top: Any  # A public C++ attribute of type TextAttrDimension     .



class TextAttrShadow:
    """ A class representing a shadow.

        Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def AddFlag(self, flag: int) -> None:
        """ Adds a border flag.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def Apply(self, shadow, compareWith=None) -> bool:
        """ Applies the border to this object, but not if the same as compareWith.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def EqPartial(self, shadow, weakTest=True) -> bool:
        """ Partial equality test.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetBlurDistance(self) -> 'TextAttrDimension':
        """ Gets the shadow blur distance.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetColour(self) -> 'Colour':
        """ Gets the colour.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetColourLong(self) -> int:
        """ Gets the colour as a long.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetFlags(self) -> int:
        """ Returns the border flags.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetOffsetX(self) -> 'TextAttrDimension':
        """ Gets the shadow horizontal offset.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetOffsetY(self) -> 'TextAttrDimension':
        """ Gets the shadow vertical offset.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetOpacity(self) -> 'TextAttrDimension':
        """ Gets the shadow opacity.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetSpread(self) -> 'TextAttrDimension':
        """ Gets the shadow spread size.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def HasColour(self) -> bool:
        """ True if the shadow has a valid colour.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def IsDefault(self) -> bool:
        """ True if the shadow has no attributes set.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def IsValid(self) -> bool:
        """ Returns True if the dimension is valid.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def RemoveFlag(self, flag: int) -> None:
        """ Removes a border flag.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def RemoveStyle(self, attr: 'richtext.TextAttrShadow') -> bool:
        """ Removes the specified attributes from this object.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def Reset(self) -> None:
        """ Resets the shadow.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetBlurDistance(self, blur: 'richtext.TextAttrDimension') -> None:
        """ Sets the shadow blur distance.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetColour(self, *args, **kw) -> None:
        """ Sets the shadow colour.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetFlags(self, flags: int) -> None:
        """ Sets the border flags.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetOffsetX(self, offset: 'richtext.TextAttrDimension') -> None:
        """ Sets the shadow horizontal offset.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetOffsetY(self, offset: 'richtext.TextAttrDimension') -> None:
        """ Sets the shadow vertical offset.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetOpacity(self, opacity: 'richtext.TextAttrDimension') -> None:
        """ Sets the shadow opacity.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetSpread(self, spread: 'richtext.TextAttrDimension') -> None:
        """ Sets the shadow spread size.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetValid(self, b: bool) -> None:
        """ Sets the valid flag.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.

            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    BlurDistance: 'TextAttrDimension'  # See GetBlurDistance and SetBlurDistance
    Colour: '_Colour'  # See GetColour and SetColour
    ColourLong: int  # See GetColourLong
    Flags: int  # See GetFlags and SetFlags
    OffsetX: 'TextAttrDimension'  # See GetOffsetX and SetOffsetX
    OffsetY: 'TextAttrDimension'  # See GetOffsetY and SetOffsetY
    Opacity: 'TextAttrDimension'  # See GetOpacity and SetOpacity
    Spread: 'TextAttrDimension'  # See GetSpread and SetSpread
    m_blurDistance: Any  # A public C++ attribute of type TextAttrDimension     .
    m_flags: Any  # A public C++ attribute of type int.
    m_offsetX: Any  # A public C++ attribute of type TextAttrDimension     .
    m_offsetY: Any  # A public C++ attribute of type TextAttrDimension     .
    m_opacity: Any  # A public C++ attribute of type TextAttrDimension     .
    m_shadowColour: Any  # A public C++ attribute of type long.
    m_spread: Any  # A public C++ attribute of type TextAttrDimension     .



TextBoxAttrFlags: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_FLOAT: int

TEXT_BOX_ATTR_CLEAR: int

TEXT_BOX_ATTR_COLLAPSE_BORDERS: int

TEXT_BOX_ATTR_VERTICAL_ALIGNMENT: int

TEXT_BOX_ATTR_BOX_STYLE_NAME: int

TEXT_BOX_ATTR_WHITESPACE: int

TEXT_BOX_ATTR_CORNER_RADIUS: int

TextBoxAttrClearStyle: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_CLEAR_NONE: int

TEXT_BOX_ATTR_CLEAR_LEFT: int

TEXT_BOX_ATTR_CLEAR_RIGHT: int

TEXT_BOX_ATTR_CLEAR_BOTH: int

TextBoxAttrCollapseMode: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_COLLAPSE_NONE: int

TEXT_BOX_ATTR_COLLAPSE_FULL: int

TextBoxAttrFloatStyle: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_FLOAT_NONE: int

TEXT_BOX_ATTR_FLOAT_LEFT: int

TEXT_BOX_ATTR_FLOAT_RIGHT: int

TextBoxAttrVerticalAlignment: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_NONE: int

TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_TOP: int

TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_CENTRE: int

TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_BOTTOM: int

TextBoxAttrWhitespaceMode: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_WHITESPACE_NONE: int

TEXT_BOX_ATTR_WHITESPACE_NORMAL: int

TEXT_BOX_ATTR_WHITESPACE_NO_WRAP: int

TEXT_BOX_ATTR_WHITESPACE_PREFORMATTED: int

TEXT_BOX_ATTR_WHITESPACE_PREFORMATTED_LINE: int

TEXT_BOX_ATTR_WHITESPACE_PREFORMATTED_WRAP: int

TextBoxAttrPosition: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_POSITION_STATIC: int

TEXT_BOX_ATTR_POSITION_RELATIVE: int

TEXT_BOX_ATTR_POSITION_ABSOLUTE: int

TEXT_BOX_ATTR_POSITION_FIXED: int

TEXT_BOX_ATTR_POSITION_MASK: int

RichTextActionList: TypeAlias = list['RichTextAction']

wxRichTextStyleType: TypeAlias = int

RichTextVariantArray: TypeAlias = list[Any]

RichTextFloatCollector: TypeAlias = Any

RichTextObjectPtrArrayArray: TypeAlias = list[Any]

RichTextObjectPtrArray: TypeAlias = list[Any]

RichTextRangeArray: TypeAlias = list['RichTextRange']

RichTextObjectList: TypeAlias = list['RichTextObject']

TextAttrDimensionFlags: TypeAlias = int

