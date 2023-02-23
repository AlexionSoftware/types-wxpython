# -*- coding: utf-8 -*-
from typing import Optional, Any


class RichTextCtrl('Control'):
	""" RichTextCtrl provides a generic, ground-up implementation of a text
control capable of showing multiple styles and images.
	"""
	def __init__(self, *args, **kw) -> None:
		""" Overloaded Implementations:
		"""

	def AddImage(self, image: 'Image') -> 'richtext.RichTextRange':
		""" Adds an image to the controlâs buffer.
		"""

	def AddParagraph(self, text: str) -> 'richtext.RichTextRange':
		""" Adds a new paragraph of text to the end of the buffer.
		"""

	def AppendText(self, text: str) -> None:
		""" Sets the insertion point to the end of the buffer and writes the text.
		"""

	def ApplyAlignmentToSelection(self, alignment: TextAttrAlignment) -> bool:
		""" Applies the given alignment to the selection or the default style (undoable).
		"""

	def ApplyBoldToSelection(self) -> bool:
		""" Apples bold to the selection or the default style (undoable).
		"""

	def ApplyItalicToSelection(self) -> bool:
		""" Applies italic to the selection or the default style (undoable).
		"""

	def ApplyStyle(self, styleDef: 'richtext.RichTextStyleDefinition') -> bool:
		""" Applies the style sheet to the buffer, matching paragraph styles in the sheet against named styles in the buffer.
		"""

	def ApplyStyleSheet(self, styleSheet: Optional['richtext.RichTextStyleSheet']=None) -> bool:
		""" Applies the style sheet to the buffer, for example if the styles have changed.
		"""

	def ApplyTextEffectToSelection(self, flags: int) -> bool:
		""" Applies one or more TextAttrEffects flags to the selection (undoable).
		"""

	def ApplyUnderlineToSelection(self) -> bool:
		""" Applies underline to the selection or the default style (undoable).
		"""

	def AutoComplete(self, *args, **kw) -> bool:
		""" Overloaded Implementations:
		"""

	def AutoCompleteDirectories(self) -> bool:
		""" Call this function to enable auto-completion of the text using the file system directories.
		"""

	def AutoCompleteFileNames(self) -> bool:
		""" Call this function to enable auto-completion of the text typed in a single-line text control using all valid file system paths.
		"""

	def BatchingUndo(self) -> bool:
		""" Returns True if undo commands are being batched.
		"""

	def BeginAlignment(self, alignment: TextAttrAlignment) -> bool:
		""" Begins using alignment.
		"""

	def BeginBatchUndo(self, cmdName: str) -> bool:
		""" Starts batching undo history for commands.
		"""

	def BeginBold(self) -> bool:
		""" Begins using bold.
		"""

	def BeginCharacterStyle(self, characterStyle: str) -> bool:
		""" Begins using the named character style.
		"""

	def BeginFont(self, font: 'Font') -> bool:
		""" Begins using this font.
		"""

	def BeginFontSize(self, pointSize: int) -> bool:
		""" Begins using the given point size.
		"""

	def BeginItalic(self) -> bool:
		""" Begins using italic.
		"""

	def BeginLeftIndent(self, leftIndent, leftSubIndent=0) -> bool:
		""" Begins applying a left indent and subindent in tenths of a millimetre.
		"""

	def BeginLineSpacing(self, lineSpacing: int) -> bool:
		""" Begins applying line spacing.
		"""

	def BeginListStyle(self, listStyle, level=1, number=1) -> bool:
		""" Begins using a specified list style.
		"""

	def BeginNumberedBullet(self, bulletNumber, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_ARABIC|TEXT_ATTR_BULLET_STYLE_PERIOD) -> bool:
		""" Begins a numbered bullet.
		"""

	def BeginParagraphSpacing(self, before, after) -> bool:
		""" Begins paragraph spacing; pass the before-paragraph and after-paragraph spacing in tenths of a millimetre.
		"""

	def BeginParagraphStyle(self, paragraphStyle: str) -> bool:
		""" Begins applying the named paragraph style.
		"""

	def BeginRightIndent(self, rightIndent: int) -> bool:
		""" Begins a right indent, specified in tenths of a millimetre.
		"""

	def BeginStandardBullet(self, bulletName, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_STANDARD) -> bool:
		""" Begins applying a symbol bullet.
		"""

	def BeginStyle(self, style: 'richtext.RichTextAttr') -> bool:
		""" Begins applying a style.
		"""

	def BeginSuppressUndo(self) -> bool:
		""" Starts suppressing undo history for commands.
		"""

	def BeginSymbolBullet(self, symbol, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_SYMBOL) -> bool:
		""" Begins applying a symbol bullet, using a character from the current font.
		"""

	def BeginTextColour(self, colour: 'Colour') -> bool:
		""" Begins using this colour.
		"""

	def BeginURL(self, url, characterStyle="") -> bool:
		""" Begins applying wx.TEXT_ATTR_URL to the content.
		"""

	def BeginUnderline(self) -> bool:
		""" Begins using underlining.
		"""

	def CanCopy(self) -> bool:
		""" Returns True if selected content can be copied to the clipboard.
		"""

	def CanCut(self) -> bool:
		""" Returns True if selected content can be copied to the clipboard and deleted.
		"""

	def CanDeleteRange(self, container, range) -> bool:
		""" Can we delete this range? Sends an event to the control.
		"""

	def CanDeleteSelection(self) -> bool:
		""" Returns True if selected content can be deleted.
		"""

	def CanEditProperties(self, obj: 'richtext.RichTextObject') -> bool:
		""" Returns True if we can edit the objectâs properties via a GUI.
		"""

	def CanInsertContent(self, container, pos) -> bool:
		""" Can we insert content at this position? Sends an event to the control.
		"""

	def CanPaste(self) -> bool:
		""" Returns True if the clipboard content can be pasted to the buffer.
		"""

	def CanRedo(self) -> bool:
		""" Returns True if there is a command in the command history that can be redone.
		"""

	def CanUndo(self) -> bool:
		""" Returns True if there is a command in the command history that can be undone.
		"""

	def ChangeValue(self, value: str) -> None:
		""" Sets the new text control value.
		"""

	def Clear(self) -> None:
		""" Clears the buffer content, leaving a single empty paragraph.
		"""

	@staticmethod
	def ClearAvailableFontNames() -> None:
		""" Clears the cache of available font names.
		"""

	def ClearListStyle(self, range, flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool:
		""" Clears the list style from the given range, clearing list-related attributes and applying any named paragraph style associated with each paragraph.
		"""

	def Command(self, event: 'CommandEvent') -> None:
		""" Sends the event to the control.
		"""

	def Copy(self) -> None:
		""" Copies the selected content (if any) to the clipboard.
		"""

	def Create(self, parent, id=-1, value="", pos=DefaultPosition, size=DefaultSize, style=RE_MULTILINE, validator=DefaultValidator, name=TextCtrlNameStr) -> bool:
		""" Creates the underlying window.
		"""

	def Cut(self) -> None:
		""" Copies the selected content (if any) to the clipboard and deletes the selection.
		"""

	def Delete(self, range: 'richtext.RichTextRange') -> bool:
		""" Deletes the content within the given range.
		"""

	def DeleteSelectedContent(self, newPos=None) -> None:
		""" Deletes content if there is a selection, e.g.
		"""

	def DeleteSelection(self) -> None:
		""" Deletes the content in the selection, if any.
		"""

	def DiscardEdits(self) -> None:
		""" Sets the bufferâs modified status to False, and clears the bufferâs command history.
		"""

	def DoGetBestSize(self) -> Size:
		""" Currently this simply returns    wx.Size.
		"""

	def DoGetValue(self) -> str:
		""" string
		"""

	def DoLayoutBuffer(self, buffer, dc, context, rect, parentRect, flags) -> None:
		""" Implements layout.
		"""

	def DoLoadFile(self, file, fileType) -> bool:
		""" Helper function for LoadFile .
		"""

	def DoSaveFile(self, file="", fileType=RICHTEXT_TYPE_ANY) -> bool:
		""" Helper function for SaveFile .
		"""

	def DoThaw(self) -> None:
		""" 
		"""

	def DoWriteText(self, value, flags=0) -> None:
		""" value (string) â
		"""

	def DoesSelectionHaveTextEffectFlag(self, flag: int) -> bool:
		""" Returns True if all of the selection, or the content at the current caret position, has the supplied TextAttrEffects flag(s).
		"""

	def EditProperties(self, obj, parent) -> bool:
		""" Edits the objectâs properties via a GUI.
		"""

	def EnableDelayedImageLoading(self, b: bool) -> None:
		""" Enable or disable delayed image loading.
		"""

	def EnableImages(self, b: bool) -> None:
		""" Enable or disable images.
		"""

	def EnableVerticalScrollbar(self, enable: bool) -> None:
		""" Enable or disable the vertical scrollbar.
		"""

	def EnableVirtualAttributes(self, b: bool) -> None:
		""" Pass True to let the control use virtual attributes.
		"""

	def EndAlignment(self) -> bool:
		""" Ends alignment.
		"""

	def EndAllStyles(self) -> bool:
		""" Ends application of all styles in the current style stack.
		"""

	def EndBatchUndo(self) -> bool:
		""" Ends batching undo command history.
		"""

	def EndBold(self) -> bool:
		""" Ends using bold.
		"""

	def EndCharacterStyle(self) -> bool:
		""" Ends application of a named character style.
		"""

	def EndFont(self) -> bool:
		""" Ends using a font.
		"""

	def EndFontSize(self) -> bool:
		""" Ends using a point size.
		"""

	def EndItalic(self) -> bool:
		""" Ends using italic.
		"""

	def EndLeftIndent(self) -> bool:
		""" Ends left indent.
		"""

	def EndLineSpacing(self) -> bool:
		""" Ends line spacing.
		"""

	def EndListStyle(self) -> bool:
		""" Ends using a specified list style.
		"""

	def EndNumberedBullet(self) -> bool:
		""" Ends application of a numbered bullet.
		"""

	def EndParagraphSpacing(self) -> bool:
		""" Ends paragraph spacing.
		"""

	def EndParagraphStyle(self) -> bool:
		""" Ends application of a named paragraph style.
		"""

	def EndRightIndent(self) -> bool:
		""" Ends right indent.
		"""

	def EndStandardBullet(self) -> bool:
		""" Begins applying a standard bullet.
		"""

	def EndStyle(self) -> bool:
		""" Ends the current style.
		"""

	def EndSuppressUndo(self) -> bool:
		""" Ends suppressing undo command history.
		"""

	def EndSymbolBullet(self) -> bool:
		""" Ends applying a symbol bullet.
		"""

	def EndTextColour(self) -> bool:
		""" Ends applying a text colour.
		"""

	def EndURL(self) -> bool:
		""" Ends applying a URL.
		"""

	def EndUnderline(self) -> bool:
		""" End applying underlining.
		"""

	def ExtendCellSelection(self, table, noRowSteps, noColSteps) -> bool:
		""" Extends a table selection in the given direction.
		"""

	def ExtendSelection(self, oldPosition, newPosition, flags) -> bool:
		""" Helper function for extending the selection, returning True if the selection was changed.
		"""

	def FindCaretPositionForCharacterPosition(self, position, hitTestFlags, container, caretLineStart) -> long:
		""" Find the caret position for the combination of hit-test flags and character position.
		"""

	def FindContainerAtPoint(self, pt, position, hit, hitObj, flags=0) -> 'richtext.RichTextParagraphLayoutBox':
		""" Finds the container at the given point, which is assumed to be in client coordinates.
		"""

	def FindNextWordPosition(self, direction: int=1) -> long:
		""" Helper function for finding the caret position for the next word.
		"""

	def FindRangeForList(self, pos, isNumberedList) -> 'richtext.RichTextRange':
		""" Given a character position at which there is a list style, find the range encompassing the same list style by looking backwards and forwards.
		"""

	def ForceDelayedLayout(self) -> None:
		""" 
		"""

	def ForceUpper(self) -> None:
		""" Convert all text entered into the control to upper case.
		"""

	def GetAdjustedCaretPosition(self, caretPos: long) -> long:
		""" The adjusted caret position is the character position adjusted to take into account whether weâre at the start of a paragraph, in which case style information should be taken from the next position, not current one.
		"""

	@staticmethod
	def GetAvailableFontNames() -> Any:
		""" Font names take a long time to retrieve, so cache them (on demand).
		"""

	def GetBasicStyle(self) -> 'richtext.RichTextAttr':
		""" Gets the basic (overall) style.
		"""

	def GetBuffer(self) -> 'richtext.RichTextBuffer':
		""" Returns the buffer associated with the control.
		"""

	def GetCaretAtLineStart(self) -> bool:
		""" Returns True if we are showing the caret position at the start of a line instead of at the end of the previous one.
		"""

	def GetCaretPosition(self) -> long:
		""" Returns the current caret position.
		"""

	def GetCaretPositionForDefaultStyle(self) -> long:
		""" Returns the caret position since the default formatting was changed.
		"""

	def GetCaretPositionForIndex(self, position, rect, container=None) -> None:
		""" Returns the caret height and position for the given character position.
		"""

	@staticmethod
	def GetClassDefaultAttributes(variant: WindowVariant=WINDOW_VARIANT_NORMAL) -> VisualAttributes:
		""" variant (WindowVariant) â
		"""

	def GetCommandProcessor(self) -> CommandProcessor:
		""" Gets the command processor associated with the controlâs buffer.
		"""

	def GetContextMenu(self) -> Menu:
		""" Returns the current context menu.
		"""

	def GetContextMenuPropertiesInfo(self) -> 'richtext.RichTextContextMenuPropertiesInfo':
		""" Returns an object that stores information about context menu property item(s), in order to communicate between the context menu event handler and the code that responds to it.
		"""

	def GetDefaultStyleEx(self) -> 'richtext.RichTextAttr':
		""" Returns the current default style, which can be used to change how subsequently inserted text is displayed.
		"""

	def GetDelayedImageLoading(self) -> bool:
		""" Returns True if delayed image loading is enabled.
		"""

	def GetDelayedImageProcessingRequired(self) -> bool:
		""" Gets the flag indicating that delayed image processing is required.
		"""

	def GetDelayedImageProcessingTime(self) -> long:
		""" Returns the last time delayed image processing was performed.
		"""

	def GetDelayedLayoutThreshold(self) -> long:
		""" Gets the size of the buffer beyond which layout is delayed during resizing.
		"""

	def GetDimensionScale(self) -> float:
		""" Returns the scale factor for displaying certain dimensions such as indentation and inter-paragraph spacing.
		"""

	def GetDragStartPoint(self) -> Point:
		""" Get the possible DragânâDrop start point.
		"""

	def GetDragStartTime(self) -> DateTime:
		""" Get the possible DragânâDrop start time.
		"""

	def GetDragging(self) -> bool:
		""" Returns True if we are extending a selection.
		"""

	def GetFilename(self) -> str:
		""" Gets the current filename associated with the control.
		"""

	def GetFirstVisiblePoint(self) -> Point:
		""" Returns the first visible point in the window.
		"""

	def GetFirstVisiblePosition(self) -> long:
		""" Returns the first visible position in the current view.
		"""

	def GetFocusObject(self) -> 'richtext.RichTextParagraphLayoutBox':
		""" Returns the   wx.richtext.RichTextObject  object that currently has the editing focus.
		"""

	def GetFontScale(self) -> float:
		""" Returns the scale factor for displaying fonts, for example for more comfortable editing.
		"""

	def GetFullLayoutRequired(self) -> bool:
		""" bool
		"""

	def GetFullLayoutSavedPosition(self) -> long:
		""" long
		"""

	def GetFullLayoutTime(self) -> long:
		""" long
		"""

	def GetHandlerFlags(self) -> int:
		""" Returns flags that change the behaviour of loading or saving.
		"""

	def GetHint(self) -> str:
		""" Returns the current hint string.
		"""

	def GetImagesEnabled(self) -> bool:
		""" Returns True if images are enabled.
		"""

	def GetInsertionPoint(self) -> long:
		""" Returns the current insertion point.
		"""

	def GetInternalSelectionRange(self) -> 'richtext.RichTextRange':
		""" Returns the selection range in character positions.
		"""

	def GetLastPosition(self) -> 'TextPos':
		""" Returns the last position in the buffer.
		"""

	def GetLineLength(self, lineNo: long) -> int:
		""" Returns the length of the specified line in characters.
		"""

	def GetLineText(self, lineNo: long) -> str:
		""" Returns the text for the given line.
		"""

	def GetLogicalPoint(self, ptPhysical: 'Point') -> Point:
		""" Transforms physical window position to logical (unscrolled) position.
		"""

	def GetMargins(self) -> 'Point':
		""" Returns the margins used by the control.
		"""

	def GetNumberOfLines(self) -> int:
		""" Returns the number of lines in the buffer.
		"""

	def GetPhysicalPoint(self, ptLogical: 'Point') -> Point:
		""" Transforms logical (unscrolled) position to physical window position.
		"""

	def GetPreDrag(self) -> bool:
		""" Are we trying to start DragânâDrop?
		"""

	def GetPropertiesMenuLabel(self, obj: 'richtext.RichTextObject') -> str:
		""" Gets the objectâs properties menu label.
		"""

	def GetRange(self, from_, to_) -> str:
		""" Gets the text for the given range.
		"""

	def GetScale(self) -> float:
		""" Returns an overall scale factor for displaying and editing the content.
		"""

	def GetScaledPoint(self, pt: 'Point') -> Point:
		""" Returns a scaled point.
		"""

	def GetScaledRect(self, rect: 'Rect') -> Rect:
		""" Returns a scaled rectangle.
		"""

	def GetScaledSize(self, sz: 'Size') -> Size:
		""" Returns a scaled size.
		"""

	def GetSelection(self) -> 'richtext.RichTextSelection':
		""" Returns the range of the current selection.
		"""

	def GetSelectionAnchor(self) -> long:
		""" Returns an anchor so we know how to extend the selection.
		"""

	def GetSelectionAnchorObject(self) -> 'richtext.RichTextObject':
		""" Returns the anchor object if selecting multiple containers.
		"""

	def GetSelectionRange(self) -> 'richtext.RichTextRange':
		""" Returns the selection range in character positions.
		"""

	def GetStringSelection(self) -> str:
		""" Returns the text within the current selection range, if any.
		"""

	def GetStyle(self, *args, **kw) -> None:
		""" Gets the attributes at the given position.
		"""

	def GetStyleForRange(self, *args, **kw) -> None:
		""" Gets the attributes common to the specified range.
		"""

	def GetStyleSheet(self) -> 'richtext.RichTextStyleSheet':
		""" Returns the style sheet associated with the control, if any.
		"""

	def GetTextCursor(self) -> Cursor:
		""" Returns the text (normal) cursor.
		"""

	def GetURLCursor(self) -> Cursor:
		""" Returns the cursor to be used over URLs.
		"""

	def GetUncombinedStyle(self, *args, **kw) -> None:
		""" Gets the attributes at the given position.
		"""

	def GetUnscaledPoint(self, pt: 'Point') -> Point:
		""" Returns an unscaled point.
		"""

	def GetUnscaledRect(self, rect: 'Rect') -> Rect:
		""" Returns an unscaled rectangle.
		"""

	def GetUnscaledSize(self, sz: 'Size') -> Size:
		""" Returns an unscaled size.
		"""

	def GetValue(self) -> str:
		""" Returns the content of the entire control as a string.
		"""

	def GetVerticalScrollbarEnabled(self) -> bool:
		""" Returns True if the vertical scrollbar is enabled.
		"""

	def GetVirtualAttributesEnabled(self) -> bool:
		""" Returns True if this control can use virtual attributes and virtual text.
		"""

	def GetVisibleLineForCaretPosition(self, caretPosition: long) -> 'richtext.RichTextLine':
		""" Internal helper function returning the line for the visible caret position.
		"""

	def HasCharacterAttributes(self, range, style) -> bool:
		""" Test if this whole range has character attributes of the specified kind.
		"""

	def HasParagraphAttributes(self, range, style) -> bool:
		""" Test if this whole range has paragraph attributes of the specified kind.
		"""

	def HasSelection(self) -> bool:
		""" Returns True if there is a selection and the object containing the selection was the same as the current focus object.
		"""

	def HasUnfocusedSelection(self) -> bool:
		""" Returns True if there was a selection, whether or not the current focus object is the same as the selectionâs container object.
		"""

	def HitTest(self, pt: 'Point') -> tuple:
		""" Finds the character at the given position in pixels.
		"""

	def HitTestXY(self, pt: 'Point') -> tuple:
		""" Finds the character at the given position in pixels.
		"""

	def Init(self) -> None:
		""" Initialises the members of the control.
		"""

	def Invalidate(self) -> None:
		""" Invalidates the whole buffer to trigger painting later.
		"""

	def IsDefaultStyleShowing(self) -> bool:
		""" Returns True if the user has recently set the default style without moving the caret, and therefore the UI needs to reflect the default style and not the style at the caret.
		"""

	def IsEditable(self) -> bool:
		""" Returns True if the control is editable.
		"""

	def IsEmpty(self) -> bool:
		""" Returns True if the control is currently empty.
		"""

	def IsModified(self) -> bool:
		""" Returns True if the buffer has been modified.
		"""

	def IsMultiLine(self) -> bool:
		""" Returns True if the control is multiline.
		"""

	def IsPositionVisible(self, pos: long) -> bool:
		""" Returns True if the given position is visible on the screen.
		"""

	def IsSelectionAligned(self, alignment: TextAttrAlignment) -> bool:
		""" Returns True if all of the selection is aligned according to the specified flag.
		"""

	def IsSelectionBold(self) -> bool:
		""" Returns True if all of the selection, or the content at the caret position, is bold.
		"""

	def IsSelectionItalics(self) -> bool:
		""" Returns True if all of the selection, or the content at the caret position, is italic.
		"""

	def IsSelectionUnderlined(self) -> bool:
		""" Returns True if all of the selection, or the content at the caret position, is underlined.
		"""

	def IsSingleLine(self) -> bool:
		""" Returns True if the control is single-line.
		"""

	def KeyboardNavigate(self, keyCode, flags) -> bool:
		""" Helper function implementing keyboard navigation.
		"""

	def LayoutContent(self, onlyVisibleRect: bool=False) -> bool:
		""" Lays out the buffer, which must be done before certain operations, such as setting the caret position.
		"""

	def LineBreak(self) -> bool:
		""" Inserts a line break at the current insertion point.
		"""

	def LoadFile(self, file, type=RICHTEXT_TYPE_ANY) -> bool:
		""" Loads content into the controlâs buffer using the given type.
		"""

	def MarkDirty(self) -> None:
		""" Marks the buffer as modified.
		"""

	def MoveCaret(self, pos, showAtLineStart=False, container=None) -> bool:
		""" Move the caret to the given character position.
		"""

	def MoveCaretBack(self, oldPosition: long) -> None:
		""" Move the caret one visual step forward: this may mean setting a flag and keeping the same position if weâre going from the end of one line to the start of the next, which may be the exact same caret position.
		"""

	def MoveCaretForward(self, oldPosition: long) -> None:
		""" Move the caret one visual step forward: this may mean setting a flag and keeping the same position if weâre going from the end of one line to the start of the next, which may be the exact same caret position.
		"""

	def MoveDown(self, noLines=1, flags=0) -> bool:
		""" Moves the caret down.
		"""

	def MoveEnd(self, flags: int=0) -> bool:
		""" Moves to the end of the buffer.
		"""

	def MoveHome(self, flags: int=0) -> bool:
		""" Moves to the start of the buffer.
		"""

	def MoveLeft(self, noPositions=1, flags=0) -> bool:
		""" Moves left.
		"""

	def MoveRight(self, noPositions=1, flags=0) -> bool:
		""" Moves right.
		"""

	def MoveToLineEnd(self, flags: int=0) -> bool:
		""" Moves to the end of the line.
		"""

	def MoveToLineStart(self, flags: int=0) -> bool:
		""" Moves to the start of the line.
		"""

	def MoveToParagraphEnd(self, flags: int=0) -> bool:
		""" Moves to the end of the paragraph.
		"""

	def MoveToParagraphStart(self, flags: int=0) -> bool:
		""" Moves to the start of the paragraph.
		"""

	def MoveUp(self, noLines=1, flags=0) -> bool:
		""" Moves to the start of the paragraph.
		"""

	def Newline(self) -> bool:
		""" Inserts a new paragraph at the current insertion point.
		"""

	def NumberList(self, *args, **kw) -> bool:
		""" Numbers the paragraphs in the given range.
		"""

	def OnCaptureLost(self, event: 'MouseCaptureLostEvent') -> None:
		""" event (wx.MouseCaptureLostEvent) â
		"""

	def OnChar(self, event: 'KeyEvent') -> None:
		""" event (wx.KeyEvent) â
		"""

	def OnClear(self, event: 'CommandEvent') -> None:
		""" Standard handler for the wx.ID_CLEAR command.
		"""

	def OnContextMenu(self, event: 'ContextMenuEvent') -> None:
		""" Shows a standard context menu with undo, redo, cut, copy, paste, clear, and select all commands.
		"""

	def OnCopy(self, event: 'CommandEvent') -> None:
		""" Standard handler for the wx.ID_COPY command.
		"""

	def OnCut(self, event: 'CommandEvent') -> None:
		""" Standard handler for the wx.ID_CUT command.
		"""

	def OnDropFiles(self, event: 'DropFilesEvent') -> None:
		""" Loads the first dropped file.
		"""

	def OnEraseBackground(self, event: 'EraseEvent') -> None:
		""" event (wx.EraseEvent) â
		"""

	def OnIdle(self, event: 'IdleEvent') -> None:
		""" event (wx.IdleEvent) â
		"""

	def OnKillFocus(self, event: 'FocusEvent') -> None:
		""" event (wx.FocusEvent) â
		"""

	def OnLeftClick(self, event: 'MouseEvent') -> None:
		""" event (wx.MouseEvent) â
		"""

	def OnLeftDClick(self, event: 'MouseEvent') -> None:
		""" event (wx.MouseEvent) â
		"""

	def OnLeftUp(self, event: 'MouseEvent') -> None:
		""" event (wx.MouseEvent) â
		"""

	def OnMiddleClick(self, event: 'MouseEvent') -> None:
		""" event (wx.MouseEvent) â
		"""

	def OnMoveMouse(self, event: 'MouseEvent') -> None:
		""" event (wx.MouseEvent) â
		"""

	def OnPaint(self, event: 'PaintEvent') -> None:
		""" event (wx.PaintEvent) â
		"""

	def OnPaste(self, event: 'CommandEvent') -> None:
		""" Standard handler for the wx.ID_PASTE command.
		"""

	def OnProperties(self, event: 'CommandEvent') -> None:
		""" Standard handler for property commands.
		"""

	def OnRedo(self, event: 'CommandEvent') -> None:
		""" Standard handler for the wx.ID_REDO command.
		"""

	def OnRightClick(self, event: 'MouseEvent') -> None:
		""" event (wx.MouseEvent) â
		"""

	def OnScroll(self, event: 'ScrollWinEvent') -> None:
		""" event (wx.ScrollWinEvent) â
		"""

	def OnSelectAll(self, event: 'CommandEvent') -> None:
		""" Standard handler for the wx.ID_SELECTALL command.
		"""

	def OnSetFocus(self, event: 'FocusEvent') -> None:
		""" event (wx.FocusEvent) â
		"""

	def OnSize(self, event: 'SizeEvent') -> None:
		""" event (wx.SizeEvent) â
		"""

	def OnSysColourChanged(self, event: 'SysColourChangedEvent') -> None:
		""" event (wx.SysColourChangedEvent) â
		"""

	def OnTimer(self, event: 'TimerEvent') -> None:
		""" Respond to timer events.
		"""

	def OnUndo(self, event: 'CommandEvent') -> None:
		""" Standard handler for the wx.ID_UNDO command.
		"""

	def OnUpdateClear(self, event: 'UpdateUIEvent') -> None:
		""" Standard update handler for the wx.ID_CLEAR command.
		"""

	def OnUpdateCopy(self, event: 'UpdateUIEvent') -> None:
		""" Standard update handler for the wx.ID_COPY command.
		"""

	def OnUpdateCut(self, event: 'UpdateUIEvent') -> None:
		""" Standard update handler for the wx.ID_CUT command.
		"""

	def OnUpdatePaste(self, event: 'UpdateUIEvent') -> None:
		""" Standard update handler for the wx.ID_PASTE command.
		"""

	def OnUpdateProperties(self, event: 'UpdateUIEvent') -> None:
		""" Standard update handler for property commands.
		"""

	def OnUpdateRedo(self, event: 'UpdateUIEvent') -> None:
		""" Standard update handler for the wx.ID_REDO command.
		"""

	def OnUpdateSelectAll(self, event: 'UpdateUIEvent') -> None:
		""" Standard update handler for the wx.ID_SELECTALL command.
		"""

	def OnUpdateUndo(self, event: 'UpdateUIEvent') -> None:
		""" Standard update handler for the wx.ID_UNDO command.
		"""

	def PageDown(self, noPages=1, flags=0) -> bool:
		""" Moves one or more pages down.
		"""

	def PageUp(self, noPages=1, flags=0) -> bool:
		""" Moves one or more pages up.
		"""

	def PaintAboveContent(self, WXUNUSED: 'DC') -> None:
		""" Other user defined painting after everything else (i.e. all text) is painted.
		"""

	def PaintBackground(self, dc: 'DC') -> None:
		""" Paints the background.
		"""

	def Paste(self) -> None:
		""" Pastes content from the clipboard to the buffer.
		"""

	def PopStyleSheet(self) -> 'richtext.RichTextStyleSheet':
		""" Pops the style sheet from top of stack.
		"""

	def PositionCaret(self, container: Optional['richtext.RichTextParagraphLayoutBox']=None) -> None:
		""" Internal function to position the visible caret according to the current caret position.
		"""

	def PositionToXY(self, pos: long) -> tuple:
		""" Converts a text position to zero-based column and line numbers.
		"""

	def PrepareContent(self, container: 'richtext.RichTextParagraphLayoutBox') -> None:
		""" Prepares the content just before insertion (or after buffer reset).
		"""

	def PrepareContextMenu(self, menu, pt, addPropertyCommands) -> int:
		""" Prepares the context menu, optionally adding appropriate property-editing commands.
		"""

	def ProcessBackKey(self, event, flags) -> bool:
		""" Processes the back key.
		"""

	def ProcessDelayedImageLoading(self, *args, **kw) -> bool:
		""" Overloaded Implementations:
		"""

	def ProcessMouseMovement(self, container, obj, position, pos) -> bool:
		""" Processes mouse movement in order to change the cursor.
		"""

	def PromoteList(self, *args, **kw) -> bool:
		""" Promotes or demotes the paragraphs in the given range.
		"""

	def PushStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> bool:
		""" Push the style sheet to top of stack.
		"""

	def Redo(self) -> None:
		""" Redoes the current command.
		"""

	def RefreshForSelectionChange(self, oldSelection, newSelection) -> bool:
		""" Refreshes the area affected by a selection change.
		"""

	def Remove(self, from_, to_) -> None:
		""" Removes the content in the specified range.
		"""

	def Replace(self, from_, to_, value) -> None:
		""" Replaces the content in the specified range with the string specified by value.
		"""

	def RequestDelayedImageProcessing(self) -> None:
		""" Request delayed image processing.
		"""

	def SaveFile(self, file="", type=RICHTEXT_TYPE_ANY) -> bool:
		""" Saves the buffer content using the given type.
		"""

	def ScrollIntoView(self, position, keyCode) -> bool:
		""" Scrolls position  into view.
		"""

	def SelectAll(self) -> None:
		""" Selects all the text in the buffer.
		"""

	def SelectNone(self) -> None:
		""" Cancels any selection.
		"""

	def SelectWord(self, position: long) -> bool:
		""" Selects the word at the given character position.
		"""

	def SetAndShowDefaultStyle(self, attr: 'richtext.RichTextAttr') -> None:
		""" Sets attr  as the default style and tells the control that the UI should reflect this attribute until the user moves the caret.
		"""

	def SetBasicStyle(self, style: 'richtext.RichTextAttr') -> None:
		""" Sets the basic (overall) style.
		"""

	def SetCaretAtLineStart(self, atStart: bool) -> None:
		""" Sets a flag to remember that we are showing the caret position at the start of a line instead of at the end of the previous one.
		"""

	def SetCaretPosition(self, position, showAtLineStart=False) -> None:
		""" Sets the caret position.
		"""

	def SetCaretPositionAfterClick(self, container, position, hitTestFlags, extendSelection=False) -> bool:
		""" Sets up the caret for the given position and container, after a mouse click.
		"""

	def SetCaretPositionForDefaultStyle(self, pos: long) -> None:
		""" Set the caret position for the default style that the user is selecting.
		"""

	def SetContextMenu(self, menu: 'Menu') -> None:
		""" Sets the current context menu.
		"""

	def SetDefaultStyle(self, *args, **kw) -> bool:
		""" Sets the current default style, which can be used to change how subsequently inserted text is displayed.
		"""

	def SetDefaultStyleToCursorStyle(self) -> bool:
		""" Sets the default style to the style under the cursor.
		"""

	def SetDelayedImageProcessingRequired(self, b: bool) -> None:
		""" Sets the flag indicating that delayed image processing is required.
		"""

	def SetDelayedImageProcessingTime(self, t: long) -> None:
		""" Sets the last time delayed image processing was performed.
		"""

	def SetDelayedLayoutThreshold(self, threshold: long) -> None:
		""" Sets the size of the buffer beyond which layout is delayed during resizing.
		"""

	def SetDimensionScale(self, dimScale, refresh=False) -> None:
		""" Sets the scale factor for displaying certain dimensions such as indentation and inter-paragraph spacing.
		"""

	def SetDragStartPoint(self, sp: 'Point') -> None:
		""" Set the possible DragânâDrop start point.
		"""

	def SetDragStartTime(self, st: 'DateTime') -> None:
		""" Set the possible DragânâDrop start time.
		"""

	def SetDragging(self, dragging: bool) -> None:
		""" Sets a flag to remember if we are extending a selection.
		"""

	def SetEditable(self, editable: bool) -> None:
		""" Makes the control editable, or not.
		"""

	def SetFilename(self, filename: str) -> None:
		""" Sets the current filename.
		"""

	def SetFocusObject(self, obj, setCaretPosition=True) -> bool:
		""" Sets the   wx.richtext.RichTextObject  object that currently has the editing focus.
		"""

	def SetFont(self, font: 'Font') -> bool:
		""" Sets the font, and also the basic and default attributes (see wx.richtext.RichTextCtrl.SetDefaultStyle ).
		"""

	def SetFontScale(self, fontScale, refresh=False) -> None:
		""" Sets the scale factor for displaying fonts, for example for more comfortable editing.
		"""

	def SetFullLayoutRequired(self, b: bool) -> None:
		""" b (bool) â
		"""

	def SetFullLayoutSavedPosition(self, p: long) -> None:
		""" p (long) â
		"""

	def SetFullLayoutTime(self, t: long) -> None:
		""" t (long) â
		"""

	def SetHandlerFlags(self, flags: int) -> None:
		""" Sets flags that change the behaviour of loading or saving.
		"""

	def SetHint(self, hint: str) -> bool:
		""" Sets a hint shown in an empty unfocused text control.
		"""

	def SetInsertionPoint(self, pos: long) -> None:
		""" Sets the insertion point and causes the current editing style to be taken from the new position (unlike wx.richtext.RichTextCtrl.SetCaretPosition ).
		"""

	def SetInsertionPointEnd(self) -> None:
		""" Sets the insertion point to the end of the text control.
		"""

	def SetInternalSelectionRange(self, range: 'richtext.RichTextRange') -> None:
		""" Sets the selection range in character positions.
		"""

	def SetListStyle(self, *args, **kw) -> bool:
		""" Sets the list attributes for the given range, passing flags to determine how the attributes are set.
		"""

	def SetMargins(self, *args, **kw) -> None:
		""" Attempts to set the control margins.
		"""

	def SetMaxLength(self, len: long) -> None:
		""" Sets the maximum number of characters that may be entered in a single line text control.
		"""

	def SetModified(self, modified: bool) -> None:
		""" modified (bool) â
		"""

	def SetPreDrag(self, pd: bool) -> None:
		""" Set if weâre trying to start DragânâDrop.
		"""

	def SetProperties(self, range, properties, flags=RICHTEXT_SETPROPERTIES_WITH_UNDO) -> bool:
		""" Sets the properties for the given range, passing flags to determine how the attributes are set.
		"""

	def SetScale(self, scale, refresh=False) -> None:
		""" Sets an overall scale factor for displaying and editing the content.
		"""

	def SetSelection(self, *args, **kw) -> None:
		""" Sets the selection to the given range.
		"""

	def SetSelectionAnchor(self, anchor: long) -> None:
		""" Sets an anchor so we know how to extend the selection.
		"""

	def SetSelectionAnchorObject(self, anchor: 'richtext.RichTextObject') -> None:
		""" Sets the anchor object if selecting multiple containers.
		"""

	def SetSelectionRange(self, range: 'richtext.RichTextRange') -> None:
		""" Sets the selection to the given range.
		"""

	def SetStyle(self, *args, **kw) -> bool:
		""" Overloaded Implementations:
		"""

	def SetStyleEx(self, range, style, flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool:
		""" Sets the attributes for the given range, passing flags to determine how the attributes are set.
		"""

	def SetStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> None:
		""" Sets the style sheet associated with the control.
		"""

	def SetTextCursor(self, cursor: 'Cursor') -> None:
		""" Sets the text (normal) cursor.
		"""

	def SetURLCursor(self, cursor: 'Cursor') -> None:
		""" Sets the cursor to be used over URLs.
		"""

	def SetValue(self, value: str) -> None:
		""" Replaces existing content with the given text.
		"""

	def SetupScrollbars(self, atTop: bool=False) -> None:
		""" A helper function setting up scrollbars, for example after a resize.
		"""

	def ShouldInheritColours(self) -> bool:
		""" Return True from here to allow the colours of this window to be changed by InheritAttributes .
		"""

	def ShowContextMenu(self, menu, pt, addPropertyCommands) -> bool:
		""" Shows the given context menu, optionally adding appropriate property-editing commands for the current position in the object hierarchy.
		"""

	def ShowPosition(self, pos: long) -> None:
		""" Scrolls the buffer so that the given position is in view.
		"""

	def StartCellSelection(self, table, newCell) -> bool:
		""" Starts selecting table cells.
		"""

	def StoreFocusObject(self, obj: 'richtext.RichTextParagraphLayoutBox') -> None:
		""" Setter for m_focusObject.
		"""

	def SuppressingUndo(self) -> bool:
		""" Returns True if undo history suppression is on.
		"""

	def Undo(self) -> None:
		""" Undoes the command at the top of the command history, if there is one.
		"""

	def WordLeft(self, noPages=1, flags=0) -> bool:
		""" Moves a number of words to the left.
		"""

	def WordRight(self, noPages=1, flags=0) -> bool:
		""" Move a number of words to the right.
		"""

richtext.RE_CENTRE_CARET: int  #  The control will try to keep the caret line centred vertically while editing. wx.richtext.RE_CENTER_CARET is a synonym for this style.
richtext.RE_MULTILINE: int  #  The control will be multiline (mandatory).
richtext.RE_READONLY: int  #  The control will not be editable. ^^


