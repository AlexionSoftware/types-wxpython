# -*- coding: utf-8 -*-
from typing import Any, Optional, Union

GROW: int  # Synonym for wx.EXPAND

RA_HORIZONTAL: int  # Synonym of wx.HORIZONTAL

RA_VERTICAL: int  # Synonym of wx.VERTICAL

NORMAL: int

DEFAULT: int

FONTFAMILY_DEFAULT: int
FONTFAMILY_DECORATIVE: int
FONTFAMILY_ROMAN: int
FONTFAMILY_SCRIPT: int
FONTFAMILY_SWISS: int
FONTFAMILY_MODERN: int
FONTFAMILY_TELETYPE: int
FONTFAMILY_MAX: int
FONTFAMILY_UNKNOWN: int


FONTWEIGHT_INVALID: int
FONTWEIGHT_THIN: int
FONTWEIGHT_EXTRALIGHT: int
FONTWEIGHT_LIGHT: int
FONTWEIGHT_NORMAL: int
FONTWEIGHT_MEDIUM: int
FONTWEIGHT_SEMIBOLD: int
FONTWEIGHT_BOLD: int
FONTWEIGHT_EXTRABOLD: int
FONTWEIGHT_HEAVY: int
FONTWEIGHT_EXTRAHEAVY: int
FONTWEIGHT_MAX: int


CURSOR_NONE: int
CURSOR_ARROW: int
CURSOR_RIGHT_ARROW: int
CURSOR_BULLSEYE: int
CURSOR_CHAR: int
CURSOR_CROSS: int
CURSOR_HAND: int
CURSOR_IBEAM: int
CURSOR_LEFT_BUTTON: int
CURSOR_MAGNIFIER: int
CURSOR_MIDDLE_BUTTON: int
CURSOR_NO_ENTRY: int
CURSOR_PAINT_BRUSH: int
CURSOR_PENCIL: int
CURSOR_POINT_LEFT: int
CURSOR_POINT_RIGHT: int
CURSOR_QUESTION_ARROW: int
CURSOR_RIGHT_BUTTON: int
CURSOR_SIZENESW: int
CURSOR_SIZENS: int
CURSOR_SIZENWSE: int
CURSOR_SIZEWE: int
CURSOR_SIZING: int
CURSOR_SPRAYCAN: int
CURSOR_WAIT: int
CURSOR_WATCH: int
CURSOR_BLANK: int
CURSOR_DEFAULT: int
CURSOR_COPY_ARROW: int
CURSOR_ARROWWAIT: int
CURSOR_MAX: int


ID_AUTO_LOWEST: int
ID_ANY: int
ID_AUTO_HIGHEST: int
ID_ANY: int
ID_NONE: int
ID_SEPARATOR: int
ID_ANY: int
ID_LOWEST: int
ID_OPEN: int
ID_CLOSE: int
ID_NEW: int
ID_SAVE: int
ID_SAVEAS: int
ID_REVERT: int
ID_EXIT: int
ID_UNDO: int
ID_REDO: int
ID_HELP: int
ID_PRINT: int
ID_PRINT_SETUP: int
ID_PAGE_SETUP: int
ID_PREVIEW: int
ID_ABOUT: int
ID_HELP_CONTENTS: int
ID_HELP_INDEX: int
ID_HELP_SEARCH: int
ID_HELP_COMMANDS: int
ID_HELP_PROCEDURES: int
ID_HELP_CONTEXT: int
ID_CLOSE_ALL: int
ID_PREFERENCES: int
ID_EDIT: int
ID_CUT: int
ID_COPY: int
ID_PASTE: int
ID_CLEAR: int
ID_FIND: int
ID_DUPLICATE: int
ID_SELECTALL: int
ID_DELETE: int
ID_REPLACE: int
ID_REPLACE_ALL: int
ID_PROPERTIES: int
ID_VIEW_DETAILS: int
ID_VIEW_LARGEICONS: int
ID_VIEW_SMALLICONS: int
ID_VIEW_LIST: int
ID_VIEW_SORTDATE: int
ID_VIEW_SORTNAME: int
ID_VIEW_SORTSIZE: int
ID_VIEW_SORTTYPE: int
ID_FILE: int
ID_FILE1: int
ID_FILE2: int
ID_FILE3: int
ID_FILE4: int
ID_FILE5: int
ID_FILE6: int
ID_FILE7: int
ID_FILE8: int
ID_FILE9: int
ID_OK: int
ID_CANCEL: int
ID_APPLY: int
ID_YES: int
ID_NO: int
ID_STATIC: int
ID_FORWARD: int
ID_BACKWARD: int
ID_DEFAULT: int
ID_MORE: int
ID_SETUP: int
ID_RESET: int
ID_CONTEXT_HELP: int
ID_YESTOALL: int
ID_NOTOALL: int
ID_ABORT: int
ID_RETRY: int
ID_IGNORE: int
ID_ADD: int
ID_REMOVE: int
ID_UP: int
ID_DOWN: int
ID_HOME: int
ID_REFRESH: int
ID_STOP: int
ID_INDEX: int
ID_BOLD: int
ID_ITALIC: int
ID_JUSTIFY_CENTER: int
ID_JUSTIFY_FILL: int
ID_JUSTIFY_RIGHT: int
ID_JUSTIFY_LEFT: int
ID_UNDERLINE: int
ID_INDENT: int
ID_UNINDENT: int
ID_ZOOM_100: int
ID_ZOOM_FIT: int
ID_ZOOM_IN: int
ID_ZOOM_OUT: int
ID_UNDELETE: int
ID_REVERT_TO_SAVED: int
ID_CDROM: int
ID_CONVERT: int
ID_EXECUTE: int
ID_FLOPPY: int
ID_HARDDISK: int
ID_BOTTOM: int
ID_FIRST: int
ID_LAST: int
ID_TOP: int
ID_INFO: int
ID_JUMP_TO: int
ID_NETWORK: int
ID_SELECT_COLOR: int
ID_SELECT_FONT: int
ID_SORT_ASCENDING: int
ID_SORT_DESCENDING: int
ID_SPELL_CHECK: int
ID_STRIKETHROUGH: int
ID_SYSTEM_MENU: int
ID_CLOSE_FRAME: int
ID_MOVE_FRAME: int
ID_RESIZE_FRAME: int
ID_MAXIMIZE_FRAME: int
ID_ICONIZE_FRAME: int
ID_RESTORE_FRAME: int
ID_MDI_WINDOW_FIRST: int
ID_MDI_WINDOW_CASCADE: int
ID_MDI_WINDOW_TILE_HORZ: int
ID_MDI_WINDOW_TILE_VERT: int
ID_MDI_WINDOW_ARRANGE_ICONS: int
ID_MDI_WINDOW_PREV: int
ID_MDI_WINDOW_NEXT: int
ID_MDI_WINDOW_LAST: int
ID_FILEDLGG: int
ID_FILECTRL: int
ID_HIGHEST: int


FONTENCODING_SYSTEM: int
FONTENCODING_DEFAULT: int
FONTENCODING_ISO8859_1: int
FONTENCODING_ISO8859_2: int
FONTENCODING_ISO8859_3: int
FONTENCODING_ISO8859_4: int
FONTENCODING_ISO8859_5: int
FONTENCODING_ISO8859_6: int
FONTENCODING_ISO8859_7: int
FONTENCODING_ISO8859_8: int
FONTENCODING_ISO8859_9: int
FONTENCODING_ISO8859_10: int
FONTENCODING_ISO8859_11: int
FONTENCODING_ISO8859_12: int
FONTENCODING_ISO8859_13: int
FONTENCODING_ISO8859_14: int
FONTENCODING_ISO8859_15: int
FONTENCODING_ISO8859_MAX: int
FONTENCODING_KOI8: int
FONTENCODING_KOI8_U: int
FONTENCODING_ALTERNATIVE: int
FONTENCODING_BULGARIAN: int
FONTENCODING_CP437: int
FONTENCODING_CP850: int
FONTENCODING_CP852: int
FONTENCODING_CP855: int
FONTENCODING_CP866: int
FONTENCODING_CP874: int
FONTENCODING_CP932: int
FONTENCODING_CP936: int
FONTENCODING_CP949: int
FONTENCODING_CP950: int
FONTENCODING_CP1250: int
FONTENCODING_CP1251: int
FONTENCODING_CP1252: int
FONTENCODING_CP1253: int
FONTENCODING_CP1254: int
FONTENCODING_CP1255: int
FONTENCODING_CP1256: int
FONTENCODING_CP1257: int
FONTENCODING_CP1258: int
FONTENCODING_CP1361: int
FONTENCODING_CP12_MAX: int
FONTENCODING_UTF7: int
FONTENCODING_UTF8: int
FONTENCODING_EUC_JP: int
FONTENCODING_UTF16BE: int
FONTENCODING_UTF16LE: int
FONTENCODING_UTF32BE: int
FONTENCODING_UTF32LE: int
FONTENCODING_MACROMAN: int
FONTENCODING_MACJAPANESE: int
FONTENCODING_MACCHINESETRAD: int
FONTENCODING_MACKOREAN: int
FONTENCODING_MACARABIC: int
FONTENCODING_MACHEBREW: int
FONTENCODING_MACGREEK: int
FONTENCODING_MACCYRILLIC: int
FONTENCODING_MACDEVANAGARI: int
FONTENCODING_MACGURMUKHI: int
FONTENCODING_MACGUJARATI: int
FONTENCODING_MACORIYA: int
FONTENCODING_MACBENGALI: int
FONTENCODING_MACTAMIL: int
FONTENCODING_MACTELUGU: int
FONTENCODING_MACKANNADA: int
FONTENCODING_MACMALAJALAM: int
FONTENCODING_MACSINHALESE: int
FONTENCODING_MACBURMESE: int
FONTENCODING_MACKHMER: int
FONTENCODING_MACTHAI: int
FONTENCODING_MACLAOTIAN: int
FONTENCODING_MACGEORGIAN: int
FONTENCODING_MACARMENIAN: int
FONTENCODING_MACCHINESESIMP: int
FONTENCODING_MACTIBETAN: int
FONTENCODING_MACMONGOLIAN: int
FONTENCODING_MACETHIOPIC: int
FONTENCODING_MACCENTRALEUR: int
FONTENCODING_MACVIATNAMESE: int
FONTENCODING_MACARABICEXT: int
FONTENCODING_MACSYMBOL: int
FONTENCODING_MACDINGBATS: int
FONTENCODING_MACTURKISH: int
FONTENCODING_MACCROATIAN: int
FONTENCODING_MACICELANDIC: int
FONTENCODING_MACROMANIAN: int
FONTENCODING_MACCELTIC: int
FONTENCODING_MACGAELIC: int
FONTENCODING_MACKEYBOARD: int
FONTENCODING_ISO2022_JP: int
FONTENCODING_MAX: int
FONTENCODING_MACMIN: int
FONTENCODING_MACMAX: int
FONTENCODING_UTF16: int
FONTENCODING_UTF32: int
FONTENCODING_UNICODE: int
FONTENCODING_GB2312: int
FONTENCODING_BIG5: int
FONTENCODING_SHIFT_JIS: int
FONTENCODING_EUC_KR: int
FONTENCODING_JOHAB: int
FONTENCODING_VIETNAMESE: int


FONTSTYLE_NORMAL: int
FONTSTYLE_ITALIC: int
FONTSTYLE_SLANT: int
FONTSTYLE_MAX: int


KILL_CHILDREN: int
EXEC_ASYNC: int
EXEC_SYNC: int
EXEC_SHOW_CONSOLE: int
EXEC_HIDE_CONSOLE: int
EXEC_MAKE_GROUP_LEADER: int
EXEC_NODISABLE: int
EXEC_NOEVENTS: int
EXEC_BLOCK: int
EXEC_SYNC: int
FD_OPEN: int
FD_SAVE: int
FD_OVERWRITE_PROMPT: int
FD_FILE_MUST_EXIST: int
FD_MULTIPLE: int
OK: int
OK: int
KILL_NOCHILDREN: int
KILL_CHILDREN: int
KILL_CHILDREN: int
EXEC_MAKE_GROUP_LEADER: int
ID_ANY: int
LOG_Warning: int
LOG_COMPONENT: int


class AcceleratorEntry:
    """ An object used by an application wishing to create an accelerator
table (see AcceleratorTable).
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def FromString(self, str: str) -> bool:
        """ Parses the given string and sets the accelerator accordingly.
        """

    def GetCommand(self) -> int:
        """ Returns the command identifier for the accelerator table entry.
        """

    def GetFlags(self) -> int:
        """ Returns the flags for the accelerator table entry.
        """

    def GetKeyCode(self) -> int:
        """ Returns the keycode for the accelerator table entry.
        """

    def GetMenuItem(self) -> 'MenuItem':
        """ Returns the menu item associated with this accelerator entry.
        """

    def IsOk(self) -> bool:
        """ Returns True if this object is correctly initialized.
        """

    def Set(self, flags, keyCode, cmd, item=None) -> None:
        """ Sets the accelerator entry parameters.
        """

    def ToRawString(self) -> str:
        """ Returns a textual representation of this accelerator which is appropriate for saving in configuration files.
        """

    def ToString(self) -> str:
        """ Returns a textual representation of this accelerator.
        """

    def __ne__(self, item: Any) -> bool:
        """ entry (wx.AcceleratorEntry) â
        """

    def __eq__(self, item: Any) -> bool:
        """ entry (wx.AcceleratorEntry) â
        """



class AcceleratorTable(Object):
    """ An accelerator table allows the application to specify a table of
keyboard shortcuts for menu or button commands.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def IsOk(self) -> bool:
        """ Returns True if the accelerator table is valid.
        """

OK: int


class Accessible(Object):
    """ The Accessible class allows wxWidgets applications, and wxWidgets
itself, to return extended information about user interface elements
to client applications such as screen readers.
    """
    def __init__(self, win: Optional['Window']=None) -> None:
        """ Constructor, taking an optional window.
        """

    def DoDefaultAction(self, childId: int) -> int:
        """ Performs the default action for the object.
        """

    def GetChild(self, childId: int) -> tuple:
        """ Gets the specified child (starting from 1).
        """

    def GetChildCount(self) -> tuple:
        """ Returns the number of children in childCount.
        """

    def GetDefaultAction(self, childId: int) -> tuple:
        """ Gets the default action for this object (0) or a child (greater than 0).
        """

    def GetDescription(self, childId: int) -> tuple:
        """ Returns the description for this object or a child.
        """

    def GetFocus(self, childId: int) -> tuple:
        """ Gets the window with the keyboard focus.
        """

    def GetHelpText(self, childId: int) -> tuple:
        """ Returns help text for this object or a child, similar to tooltip text.
        """

    def GetKeyboardShortcut(self, childId: int) -> tuple:
        """ Returns the keyboard shortcut for this object or child.
        """

    def GetLocation(self, elementId: int) -> tuple:
        """ Returns the rectangle for this object (id is 0) or a child element (id is greater than 0).
        """

    def GetName(self, childId: int) -> tuple:
        """ Gets the name of the specified object.
        """

    def GetParent(self) -> tuple:
        """ Returns the parent of this object, or None.
        """

    def GetRole(self, childId: int) -> tuple:
        """ Returns a role constant describing this object.
        """

    def GetSelections(self) -> tuple:
        """ Gets a variant representing the selected children of this object.
        """

    def GetState(self, childId: int) -> tuple:
        """ Returns a state constant.
        """

    def GetValue(self, childId: int) -> tuple:
        """ Returns a localized string representing the value for the object or child.
        """

    def GetWindow(self) -> 'Window':
        """ Returns the window associated with this object.
        """

    def HitTest(self, pt, childId, childObject) -> int:
        """ Returns a status value and object id to indicate whether the given point was on this or a child object.
        """

    def Navigate(self, navDir, fromId, toId, toObject) -> int:
        """ Navigates from fromId  to toId  or to toObject.
        """

    @staticmethod
    def NotifyEvent(eventType, window, objectType, objectId) -> None:
        """ Allows the application to send an event when something changes in an accessible object.
        """

    def Select(self, childId, selectFlags) -> int:
        """ Selects the object or child.
        """

    def SetWindow(self, window: 'Window') -> None:
        """ Sets the window associated with this object.
        """

ACC_NOT_SUPPORTED: int
ACC_OK: int
ACC_OK: int


class ActivateEvent(Event):
    """ An activate event is sent when a window or application is being
activated or deactivated.
    """
    def __init__(self, eventType=wxEVT_NULL, active=True, id=0, ActivationReason=Reason_Unknown) -> None:
        """ Constructor.
        """

    def GetActivationReason(self) -> 'ActivateEvent.Reason':
        """ Allows checking if the window was activated by clicking it with the mouse or in some other way.
        """

    def GetActive(self) -> bool:
        """ Returns True if the application or window is being activated, False otherwise.
        """

EVT_ACTIVATE: int  #  Process a  wxEVT_ACTIVATE   event.
EVT_ACTIVATE_APP: int  #  Process a  wxEVT_ACTIVATE_APP   event. This event is received by the App-derived instance only.
EVT_HIBERNATE: int  #  Process a hibernate event, supplying the member function. This event applies to   wx.App  only, and only on Windows SmartPhone and PocketPC. It is generated when the system is low on memory; the application should free up as much memory as possible, and restore full working state when it receives a  wxEVT_ACTIVATE   or   wxEVT_ACTIVATE_APP   event. ^^


class ActivityIndicator(Control):
    """ Small control showing an animation indicating that the program is
currently busy performing some background task.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, winid=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name="activityindicator") -> bool:
        """ Create the control initialized using the default constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def IsRunning(self) -> bool:
        """ Returns True if the control is currently showing activity.
        """

    def Start(self) -> None:
        """ Starts animation of the indicator.
        """

    def Stop(self) -> None:
        """ Stops the animation of the indicator.
        """



class AffineMatrix2D(AffineMatrix2DBase):
    """ A 3x2 matrix representing an affine 2D transformation.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def Concat(self, t: 'AffineMatrix2DBase') -> None:
        """ Concatenate this matrix with another one.
        """

    def Get(self) -> tuple:
        """ Get the component values of the matrix.
        """

    def Invert(self) -> bool:
        """ Invert this matrix.
        """

    def IsEqual(self, t: 'AffineMatrix2DBase') -> None:
        """ Check that this matrix is identical with t.
        """

    def IsIdentity(self) -> bool:
        """ Check if this is the identity matrix.
        """

    def Mirror(self, direction: int=HORIZONTAL) -> None:
        """ Add mirroring to this matrix.
        """

    def Rotate(self, cRadians: 'Double') -> None:
        """ Add clockwise rotation to this matrix.
        """

    def Scale(self, xScale, yScale) -> None:
        """ Add scaling to this matrix.
        """

    def Set(self, mat2D, tr) -> None:
        """ Set all elements of this matrix.
        """

    def TransformDistance(self, *args, **kw) -> Point2DDouble:
        """ Overloaded Implementations:
        """

    def TransformPoint(self, *args, **kw) -> Point2DDouble:
        """ Overloaded Implementations:
        """

    def Translate(self, dx, dy) -> None:
        """ Add the translation to this matrix.
        """

    def __ne__(self, item: Any) -> bool:
        """ Check that this matrix differs from t.
        """

    def __eq__(self, item: Any) -> bool:
        """ Check that this matrix is identical with t.
        """

HORIZONTAL: int
VERTICAL: int
BOTH: int


class AffineMatrix2DBase:
    """ A 2x3 matrix representing an affine 2D transformation.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def Concat(self, t: 'AffineMatrix2DBase') -> None:
        """ Concatenate this matrix with another one.
        """

    def Get(self) -> tuple:
        """ Get the component values of the matrix.
        """

    def Invert(self) -> bool:
        """ Invert this matrix.
        """

    def IsEqual(self, t: 'AffineMatrix2DBase') -> bool:
        """ Check that this matrix is identical with t.
        """

    def IsIdentity(self) -> bool:
        """ Check if this is the identity matrix.
        """

    def Mirror(self, direction: int=HORIZONTAL) -> None:
        """ Add mirroring to this matrix.
        """

    def Rotate(self, cRadians: 'Double') -> None:
        """ Add clockwise rotation to this matrix.
        """

    def Scale(self, xScale, yScale) -> None:
        """ Add scaling to this matrix.
        """

    def Set(self, mat2D, tr) -> None:
        """ Set all elements of this matrix.
        """

    def TransformDistance(self, *args, **kw) -> Point2DDouble:
        """ Overloaded Implementations:
        """

    def TransformPoint(self, *args, **kw) -> Point2DDouble:
        """ Overloaded Implementations:
        """

    def Translate(self, dx, dy) -> None:
        """ Add the translation to this matrix.
        """

    def __ne__(self, item: Any) -> bool:
        """ Check that this matrix differs from t.
        """

    def __eq__(self, item: Any) -> bool:
        """ Check that this matrix is identical with t.
        """

HORIZONTAL: int
VERTICAL: int
BOTH: int


class AlphaPixelData:
    """ A class providing direct access to a wx.Bitmapâs
internal data including the alpha channel (RGBA).
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetPixels(self) -> 'AlphaPixelData_Accessor':
        """ wx.AlphaPixelData_Accessor
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """



class Bitmap(GDIObject):
    """ This class encapsulates the concept of a platform-dependent bitmap,
either monochrome or colour or colour with alpha channel support.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def ConvertToDisabled(self, brightness: int=255) -> 'Bitmap':
        """ Returns disabled (dimmed) version of the bitmap.
        """

    def ConvertToImage(self) -> 'Image':
        """ Creates an image from a platform-dependent bitmap.
        """

    def CopyFromBuffer(self, data, format=BitmapBufferFormat_RGB, stride=-1) -> None:
        """ Copy data from a buffer object to replace the bitmap pixel data.
Default format is plain RGB, but other formats are now supported as
well.  The following symbols are used to specify the format of the
bytes in the buffer:
        """

    def CopyFromIcon(self, icon: 'Icon') -> bool:
        """ Creates the bitmap from an icon.
        """

    def CopyToBuffer(self, data, format=BitmapBufferFormat_RGB, stride=-1) -> None:
        """ Copy pixel data to a buffer object.  See CopyFromBuffer for buffer
format details.
        """

    def Create(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def CreateScaled(self, width, height, depth, logicalScale) -> bool:
        """ Create a bitmap with a scale factor.
        """

    def CreateWithDIPSize(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    @staticmethod
    def FromBuffer(width, height, data) -> 'Bitmap':
        """ Creates a wx.Bitmap from in-memory data.  The data parameter
must be a Python object that implements the buffer interface, such
as a string, bytearray, etc.  The data object is expected to contain
a series of RGB bytes and be at least (widthÂ  heightÂ  3) bytes long.
        """

    @staticmethod
    def FromBufferAndAlpha(width, height, data, alpha) -> 'Bitmap':
        """ Creates a wx.Bitmap from in-memory data.  The data and alpha
parameters must be a Python object that implements the buffer
interface, such as a string, bytearray, etc.  The data object
is expected to contain a series of RGB bytes and be at least
(widthÂ  heightÂ  3) bytes long, while the alpha object is expected
to be (widthÂ  height) bytes long and represents the imageâs alpha
channel.  On Windows and Mac the RGB values will be
âpremultipliedâ by the alpha values.  (The other platforms do
the multiplication themselves.)
        """

    @staticmethod
    def FromBufferRGBA(width, height, data) -> 'Bitmap':
        """ Creates a wx.Bitmap from in-memory data.  The data parameter
must be a Python object that implements the buffer interface, such
as a string, bytearray, etc.  The data object is expected to contain
a series of RGBA bytes and be at least (widthÂ  heightÂ  4) bytes long.
On Windows and Mac the RGB values will be âpremultipliedâ by the
alpha values.  (The other platforms do the multiplication themselves.)
        """

    @staticmethod
    def FromPNGData(data) -> 'Bitmap':
        """ Like NewFromPNGData, but with a simpler API accepting a Python
buffer-compatible object.
        """

    @staticmethod
    def FromRGBA(width, height, red=0, green=0, blue=0, alpha=0) -> 'Bitmap':
        """ Creates a new empty 32-bit wx.Bitmap where every pixel has been
initialized with the given RGBA values.
        """

    def GetDIPSize(self) -> 'Size':
        """ Returns the size of bitmap in DPI-independent units.
        """

    def GetDepth(self) -> int:
        """ Gets the colour depth of the bitmap.
        """

    def GetHandle(self) -> int:
        """ MSW-only method to fetch the windows handle for the bitmap.
        """

    def GetHeight(self) -> int:
        """ Returns the height of the bitmap in physical pixels.
        """

    def GetLogicalHeight(self) -> float:
        """ Returns the height of the bitmap in logical pixels.
        """

    def GetLogicalSize(self) -> 'Size':
        """ Returns the size of the bitmap in logical pixels.
        """

    def GetLogicalWidth(self) -> float:
        """ Returns the width of the bitmap in logical pixels.
        """

    def GetMask(self) -> 'Mask':
        """ Gets the associated mask (if any) which may have been loaded from a file or set for the bitmap.
        """

    def GetPalette(self) -> 'Palette':
        """ Gets the associated palette (if any) which may have been loaded from a file or set for the bitmap.
        """

    def GetScaleFactor(self) -> float:
        """ Returns the scale factor of this bitmap.
        """

    def GetScaledHeight(self) -> float:
        """ Returns the height of the bitmap in logical pixels.
        """

    def GetScaledSize(self) -> 'Size':
        """ Returns the size of the bitmap in logical pixels.
        """

    def GetScaledWidth(self) -> float:
        """ Returns the width of the bitmap in logical pixels.
        """

    def GetSize(self) -> 'Size':
        """ Returns the size of the bitmap in physical pixels.
        """

    def GetSubBitmap(self, rect: 'Rect') -> 'Bitmap':
        """ Returns a sub bitmap of the current one as long as the rect belongs entirely to the bitmap.
        """

    def GetWidth(self) -> int:
        """ Returns the width of the bitmap in physical pixels.
        """

    def HasAlpha(self) -> bool:
        """ Returns True if the bitmap has an alpha channel.
        """

    def IsOk(self) -> bool:
        """ Returns True if bitmap data is present.
        """

    def LoadFile(self, name, type=BITMAP_TYPE_ANY) -> bool:
        """ Loads a bitmap from a file or resource.
        """

    @staticmethod
    def NewFromPNGData(data, size) -> 'Bitmap':
        """ Loads a bitmap from the memory containing image data in PNG format.
        """

    @staticmethod
    def Rescale(bmp, sizeNeeded) -> None:
        """ Rescale the given bitmap to the requested size.
        """

    def ResetAlpha(self) -> None:
        """ Remove alpha channel from the bitmap.
        """

    def SaveFile(self, name, type, palette=None) -> bool:
        """ Saves a bitmap in the named file.
        """

    def SetDepth(self, depth: int) -> None:
        """ Sets the depth member (does not affect the bitmap data).
        """

    def SetHandle(self, handle) -> None:
        """ MSW-only method to set the windows handle for the bitmap.
        """

    def SetHeight(self, height: int) -> None:
        """ Sets the height member (does not affect the bitmap data).
        """

    def SetMask(self, mask: 'Mask') -> None:
        """ Sets the mask for this bitmap.
        """

    def SetMaskColour(self, colour) -> None:
        """ Create a mask for this bitmap based on the pixels with the given colour.
        """

    def SetPalette(self, palette: 'Palette') -> None:
        """ Sets the associated palette.
        """

    def SetScaleFactor(self, scale: float) -> None:
        """ Sets the bitmap scale factor.
        """

    def SetSize(self, size) -> None:
        """ Set the bitmap size (does not alter the existing native bitmap data or image size).
        """

    def SetWidth(self, width: int) -> None:
        """ Sets the width member (does not affect the bitmap data).
        """

    def UseAlpha(self, use: bool=True) -> None:
        """ Enable or disable use of alpha channel in this bitmap.
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """

ALPHA_OPAQUE: int


class AlphaPixelData_Accessor:
    """  Overloaded Implementations:
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Get(self) -> Any:
        """ PyObject
        """

    def IsOk(self) -> bool:
        """ bool
        """

    def MoveTo(self, data, x, y) -> None:
        """ data (AlphaPixelData) â
        """

    def Offset(self, data, x, y) -> None:
        """ data (AlphaPixelData) â
        """

    def OffsetX(self, data, x) -> None:
        """ data (AlphaPixelData) â
        """

    def OffsetY(self, data, y) -> None:
        """ data (AlphaPixelData) â
        """

    def Reset(self, data: AlphaPixelData) -> None:
        """ data (AlphaPixelData) â
        """

    def Set(self, red, green, blue, alpha) -> None:
        """ 
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """

    def nextPixel(self) -> None:
        """ 
        """



class AnyButton(Control):
    """ A class for common button functionality used as the base for the
various button classes.
    """
    def __init__(self) -> None:
        """ 
        """

    def GetBitmap(self) -> 'Bitmap':
        """ Return the bitmap shown by the button.
        """

    def GetBitmapCurrent(self) -> 'Bitmap':
        """ Returns the bitmap used when the mouse is over the button.
        """

    def GetBitmapDisabled(self) -> 'Bitmap':
        """ Returns the bitmap used for the disabled state.
        """

    def GetBitmapFocus(self) -> 'Bitmap':
        """ Returns the bitmap used for the focused state.
        """

    def GetBitmapLabel(self) -> 'Bitmap':
        """ Returns the bitmap for the normal state.
        """

    def GetBitmapMargins(self) -> 'Size':
        """ Get the margins between the bitmap and the text of the button.
        """

    def GetBitmapPressed(self) -> 'Bitmap':
        """ Returns the bitmap used when the button is pressed.
        """

    def SetBitmap(self, bitmap, dir=LEFT) -> None:
        """ Sets the bitmap to display in the button.
        """

    def SetBitmapCurrent(self, bitmap: 'BitmapBundle') -> None:
        """ Sets the bitmap to be shown when the mouse is over the button.
        """

    def SetBitmapDisabled(self, bitmap: 'BitmapBundle') -> None:
        """ Sets the bitmap for the disabled button appearance.
        """

    def SetBitmapFocus(self, bitmap: 'BitmapBundle') -> None:
        """ Sets the bitmap for the button appearance when it has the keyboard focus.
        """

    def SetBitmapLabel(self, bitmap: 'BitmapBundle') -> None:
        """ Sets the bitmap label for the button.
        """

    def SetBitmapMargins(self, *args, **kw) -> None:
        """ Set the margins between the bitmap and the text of the button.
        """

    def SetBitmapPosition(self, dir: int) -> None:
        """ Set the position at which the bitmap is displayed.
        """

    def SetBitmapPressed(self, bitmap: 'BitmapBundle') -> None:
        """ Sets the bitmap for the selected (depressed) button appearance.
        """

RIGHT: int
TOP: int
BOTTOM: int
LEFT: int
RIGHT: int
TOP: int
BOTTOM: int


class App(AppConsole):
    """ The wx.App class represents the application and is used to:
    """
    def __init__(self, redirect=False, filename=None, useBestVisual=False, clearSigInt=True) -> None:
        """ Construct a wx.App object.
        """

    @staticmethod
    def Get() -> None:
        """ A staticmethod returning the currently active application object.
Essentially just a more pythonic version of GetApp.
        """

    def InitLocale(self) -> None:
        """ Starting with version 3.8 on Windows, Python is now setting the locale
to what is defined by the system as the default locale. This causes
problems with wxWidgets which expects to be able to manage the locale
via the wx.Locale class, so the locale will be reset here to be the
default âCâ locale settings.
        """

    def MainLoop(self) -> None:
        """ Execute the main GUI event loop
        """

    def OnPreInit(self) -> None:
        """ Things that must be done after _BootstrapApp has done its thing, but
would be nice if they were already done by the time that OnInit is
called.  This can be overridden in derived classes, but be sure to call
this method from there.
        """

    def RedirectStdio(self, filename=None) -> None:
        """ Redirect sys.stdout and sys.stderr to a file or a popup window.
        """

    def ResetLocale(self) -> None:
        """ This method is now a NOP and will be deprecated.
        """

    def RestoreStdio(self) -> None:
        """ 
        """

    def SetOutputWindowAttributes(self, title=None, pos=None, size=None) -> None:
        """ Set the title, position and/or size of the output window if the stdio
has been redirected. This should be called before any output would
cause the output window to be created.
        """

    def SetTopWindow(self, frame) -> None:
        """ Set the âmainâ top level window, which will be used for the parent of
the on-demand output window as well as for dialogs that do not have
an explicit parent set.
        """

    def __del__(self) -> None:
        """ 
        """

App: int
App: int
App: int
App: int
App: int
PyApp: int
App: int
App: int
App: int
App: int
App: int
App: int
PyApp: int
App: int


class AppConsole(EvtHandler, EventFilter):
    """ This class is essential for writing console-only or hybrid apps
without having to define USE_GUI=0.
    """
    def DeletePendingEvents(self) -> None:
        """ Deletes the pending events of all EvtHandlers of this application.
        """

    def ExitMainLoop(self) -> None:
        """ Call this to explicitly exit the main message (event) loop.
        """

    def FilterEvent(self, event: 'Event') -> int:
        """ Overridden   wx.EventFilter  method.
        """

    def GetAppDisplayName(self) -> str:
        """ Returns the user-readable application name.
        """

    def GetAppName(self) -> str:
        """ Returns the application name.
        """

    def GetClassName(self) -> str:
        """ Gets the class name of the application.
        """

    @staticmethod
    def GetInstance() -> 'AppConsole':
        """ Returns the one and only global application object.
        """

    def GetMainLoop(self) -> 'EventLoopBase':
        """ Returns the main event loop instance, i.e. the event loop which is started by OnRun   and which dispatches all events sent from the native toolkit to the application (except when new event loops are temporarily set-up).
        """

    def GetTraits(self) -> 'AppTraits':
        """ Returns a pointer to the   wx.AppTraits  object for the application.
        """

    def GetVendorDisplayName(self) -> str:
        """ Returns the user-readable vendor name.
        """

    def GetVendorName(self) -> str:
        """ Returns the applicationâs vendor name.
        """

    def HasPendingEvents(self) -> bool:
        """ Returns True if there are pending events on the internal pending event list.
        """

    @staticmethod
    def IsMainLoopRunning() -> bool:
        """ Returns True if the main event loop is currently running, i.e. if the application is inside OnRun .
        """

    def IsScheduledForDestruction(self, object: 'Object') -> bool:
        """ Check if the object had been scheduled for destruction with ScheduleForDestruction .
        """

    def MainLoop(self) -> int:
        """ Called by wxWidgets on creation of the application.
        """

    def OnEventLoopEnter(self, loop: 'EventLoopBase') -> None:
        """ Called by wx.EventLoopBase.SetActive : you can override this function and put here the code which needs an active event loop.
        """

    def OnEventLoopExit(self, loop: 'EventLoopBase') -> None:
        """ Called by wx.EventLoopBase.OnExit   for each event loop which is exited.
        """

    def OnExit(self) -> int:
        """ Override this member function for any processing which needs to be done as the application is about to exit.
        """

    def OnInit(self) -> bool:
        """ This must be provided by the application, and will usually create the applicationâs main window, optionally calling SetTopWindow().
        """

    def OnRun(self) -> int:
        """ This virtual function is where the execution of a program written in wxWidgets starts.
        """

    def ProcessPendingEvents(self) -> None:
        """ Process all pending events; it is necessary to call this function to process events posted with wx.EvtHandler.QueueEvent   or wx.EvtHandler.AddPendingEvent .
        """

    def ResumeProcessingOfPendingEvents(self) -> None:
        """ Resume processing of the pending events previously stopped because of a call to SuspendProcessingOfPendingEvents .
        """

    def ScheduleForDestruction(self, object: 'Object') -> None:
        """ Delayed objects destruction.
        """

    def SetAppDisplayName(self, name: str) -> None:
        """ Set the application name to be used in the user-visible places such as window titles.
        """

    def SetAppName(self, name: str) -> None:
        """ Sets the name of the application.
        """

    def SetCLocale(self) -> None:
        """ Sets the C locale to the default locale for the current environment.
        """

    def SetClassName(self, name: str) -> None:
        """ Sets the class name of the application.
        """

    @staticmethod
    def SetInstance(app: 'AppConsole') -> None:
        """ Allows external code to modify global wx.TheApp     , but you should really know what youâre doing if you call it.
        """

    def SetVendorDisplayName(self, name: str) -> None:
        """ Set the vendor name to be used in the user-visible places.
        """

    def SetVendorName(self, name: str) -> None:
        """ Sets the name of applicationâs vendor.
        """

    def SuspendProcessingOfPendingEvents(self) -> None:
        """ Temporary suspends processing of the pending events.
        """

    def UsesEventLoop(self) -> bool:
        """ Returns True if the application is using an event loop.
        """

    def Yield(self, onlyIfNeeded: bool=False) -> bool:
        """ Yields control to pending messages in the event loop.
        """



class AppTraits:
    """ The AppTraits class defines various configurable aspects of a App.
    """
    def CreateConfig(self) -> 'ConfigBase':
        """ Called by wxWidgets to create the default configuration object for the application.
        """

    def CreateEventLoop(self) -> 'EventLoopBase':
        """ Used by wxWidgets to create the main event loop used by wx.App.OnRun .
        """

    def CreateLogTarget(self) -> 'Log':
        """ Creates a   wx.Log  class for the application to use for logging errors.
        """

    def GetAssertStackTrace(self) -> str:
        """ Helper function mostly useful for derived classes ShowAssertDialog   implementation.
        """

    def GetDesktopEnvironment(self) -> str:
        """ This method returns the name of the desktop environment currently running in a Unix desktop.
        """

    def GetStandardPaths(self) -> 'StandardPaths':
        """ Returns the   wx.StandardPaths  object for the application.
        """

    def GetToolkitVersion(self) -> tuple:
        """ Returns the wxWidgets port ID used by the running program and eventually fills the given pointers with the values of the major, minor, and micro digits of the native toolkit currently used.
        """

    def HasStderr(self) -> bool:
        """ Returns True if  fprintf(stderr)   goes somewhere, False otherwise.
        """

    def IsUsingUniversalWidgets(self) -> bool:
        """ Returns True if the library was built as wxUniversal.
        """

    def SafeMessageBox(self, text, title) -> bool:
        """ Shows a message box with the given text and title if possible.
        """

    def ShowAssertDialog(self, msg: str) -> bool:
        """ Shows the assert dialog with the specified message in GUI mode or just prints the string to stderr in console mode.
        """

PORT_GTK: int


class ArchiveFSHandler(FileSystemHandler):
    """ A file system handler for accessing files inside of archives.
    """
    def __init__(self) -> None:
        """ 
        """

    def Cleanup(self) -> None:
        """ 
        """



class ArtProvider(Object):
    """ ArtProvider class is used to customize the look of wxWidgets
application.
    """
    def CreateBitmap(self, id, client, size) -> 'Bitmap':
        """ Derived art provider classes may override this method to create requested art resource.
        """

    def CreateIconBundle(self, id, client) -> 'IconBundle':
        """ This method is similar to CreateBitmap   but can be used when a bitmap (or an icon) exists in several sizes.
        """

    @staticmethod
    def Delete(provider: 'ArtProvider') -> bool:
        """ Delete the given provider.
        """

    @staticmethod
    def GetBitmap(id, client=ART_OTHER, size=DefaultSize) -> 'Bitmap':
        """ Query registered providers for bitmap with given ID.
        """

    @staticmethod
    def GetBitmapBundle(id, client=ART_OTHER, size=DefaultSize) -> 'BitmapBundle':
        """ Query registered providers for a bundle of bitmaps with given ID.
        """

    @staticmethod
    def GetDIPSizeHint(client: 'ArtClient') -> 'Size':
        """ Returns a suitable size hint for the given ArtClient  in DIPs.
        """

    @staticmethod
    def GetIcon(id, client=ART_OTHER, size=DefaultSize) -> 'Icon':
        """ Same as wx.ArtProvider.GetBitmap , but return a   wx.Icon  object (or wx.NullIcon       on failure).
        """

    @staticmethod
    def GetIconBundle(id, client=ART_OTHER) -> 'IconBundle':
        """ Query registered providers for icon bundle with given ID.
        """

    @staticmethod
    def GetMessageBoxIcon(flags: int) -> 'Icon':
        """ Helper used by several generic classes: return the icon corresponding to the standard ICON_INFORMATION/WARNING/ERROR/QUESTION flags (only one can be set)
        """

    @staticmethod
    def GetMessageBoxIconId(flags: int) -> int:
        """ Helper used by GetMessageBoxIcon : return the art id corresponding to the standard ICON_INFORMATION/WARNING/ERROR/QUESTION flags (only one can be set)
        """

    @staticmethod
    def GetNativeDIPSizeHint(client: 'ArtClient') -> 'Size':
        """ Returns native icon size for use specified by client  hint in DIPs.
        """

    @staticmethod
    def GetNativeSizeHint(client, win=None) -> 'Size':
        """ Returns native icon size for use specified by client  hint.
        """

    @staticmethod
    def GetSizeHint(client, win=None) -> 'Size':
        """ Returns a suitable size hint for the given ArtClient.
        """

    @staticmethod
    def HasNativeProvider() -> bool:
        """ Returns True if the platform uses native icons provider that should take precedence over any customizations.
        """

    @staticmethod
    def Pop() -> bool:
        """ Remove latest added provider and delete it.
        """

    @staticmethod
    def Push(provider: 'ArtProvider') -> None:
        """ Register new art provider and add it to the top of providers stack (i.e.
        """

    @staticmethod
    def PushBack(provider: 'ArtProvider') -> None:
        """ Register new art provider and add it to the bottom of providers stack.
        """

    @staticmethod
    def Remove(provider: 'ArtProvider') -> bool:
        """ Remove a provider from the stack if it is on it.
        """

ART_ERROR: int
ART_GOTO_LAST: int
ART_FILE_SAVE_AS: int
ART_QUESTION: int
ART_PRINT: int
ART_DELETE: int
ART_WARNING: int
ART_HELP: int
ART_COPY: int
ART_INFORMATION: int
ART_TIP: int
ART_CUT: int
ART_ADD_BOOKMARK: int
ART_REPORT_VIEW: int
ART_PASTE: int
ART_DEL_BOOKMARK: int
ART_LIST_VIEW: int
ART_UNDO: int
ART_HELP_SIDE_PANEL: int
ART_NEW_DIR: int
ART_REDO: int
ART_HELP_SETTINGS: int
ART_FOLDER: int
ART_PLUS: int
ART_HELP_BOOK: int
ART_FOLDER_OPEN: int
ART_MINUS: int
ART_HELP_FOLDER: int
ART_GO_DIR_UP: int
ART_CLOSE: int
ART_HELP_PAGE: int
ART_EXECUTABLE_FILE: int
ART_QUIT: int
ART_GO_BACK: int
ART_NORMAL_FILE: int
ART_FIND: int
ART_GO_FORWARD: int
ART_TICK_MARK: int
ART_FIND_AND_REPLACE: int
ART_GO_UP: int
ART_CROSS_MARK: int
ART_HARDDISK: int
ART_GO_DOWN: int
ART_MISSING_IMAGE: int
ART_FLOPPY: int
ART_GO_TO_PARENT: int
ART_NEW: int
ART_CDROM: int
ART_GO_HOME: int
ART_FILE_OPEN: int
ART_GOTO_FIRST: int
ART_FILE_SAVE: int
ART_FILE_OPEN: int
ART_OTHER: int
ART_FRAME_ICON: int


class AutoBufferedPaintDC(BufferedPaintDC):
    """ This DC derivative can be used inside of an EVT_PAINT() event
handler to achieve double-buffered drawing.
    """
    def __init__(self, window: 'Window') -> None:
        """ Constructor.
        """

BG_STYLE_PAINT: int


class DC(Object):
    """ A DC is a âdevice contextâ onto which graphics and text can be
drawn.
    """
    def Blit(self, xdest, ydest, width, height, source, xsrc, ysrc, logicalFunc=COPY, useMask=False, xsrcMask=DefaultCoord, ysrcMask=DefaultCoord) -> bool:
        """ Copy from a source DC to this DC.
        """

    def CalcBoundingBox(self, x, y) -> None:
        """ Adds the specified point to the bounding box which can be retrieved with MinX , MaxX   and MinY , MaxY   functions.
        """

    def CanDrawBitmap(self) -> bool:
        """ Does the DC support drawing bitmaps?
        """

    def CanGetTextExtent(self) -> bool:
        """ Does the DC support calculating the size required to draw text?
        """

    def CanUseTransformMatrix(self) -> bool:
        """ Check if the use of transformation matrix is supported by the current system.
        """

    def Clear(self) -> None:
        """ Clears the device context using the current background brush.
        """

    def CopyAttributes(self, dc: 'DC') -> None:
        """ Copy attributes from another DC.
        """

    def CrossHair(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DestroyClippingRegion(self) -> None:
        """ Destroys the current clipping region so that none of the DC is clipped.
        """

    def DeviceToLogical(self, *args, **kw) -> 'Point':
        """ Overloaded Implementations:
        """

    def DeviceToLogicalRel(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:
        """

    def DeviceToLogicalX(self, x: int) -> 'Coord':
        """ Convert device  X coordinate to logical coordinate, using the current mapping mode, user scale factor, device origin and axis orientation.
        """

    def DeviceToLogicalXRel(self, x: int) -> 'Coord':
        """ Convert device  X coordinate to relative logical coordinate, using the current mapping mode and user scale factor but ignoring the axis orientation.
        """

    def DeviceToLogicalY(self, y: int) -> 'Coord':
        """ Converts device  Y coordinate to logical coordinate, using the current mapping mode, user scale factor, device origin and axis orientation.
        """

    def DeviceToLogicalYRel(self, y: int) -> 'Coord':
        """ Convert device  Y coordinate to relative logical coordinate, using the current mapping mode and user scale factor but ignoring the axis orientation.
        """

    def DrawArc(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawBitmap(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawCheckMark(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawCircle(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawEllipse(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawEllipseList(self, ellipses, pens=None, brushes=None) -> None:
        """ Draw a list of ellipses as quickly as possible.
        """

    def DrawEllipticArc(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawIcon(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawLabel(self, *args, **kw) -> 'Rect':
        """ Overloaded Implementations:
        """

    def DrawLine(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawLineList(self, lines, pens=None) -> None:
        """ Draw a list of lines as quickly as possible.
        """

    def DrawLines(self, points, xoffset=0, yoffset=0) -> None:
        """ This method uses a list of Points, adding the optional offset coordinate.
        """

    def DrawLinesFromBuffer(self, pyBuff: Any) -> None:
        """ Implementation of DrawLines that can use numpy arrays, or anything else that uses the
python buffer protocol directly without any element conversion.  This provides a
significant performance increase over the standard DrawLines function.
        """

    def DrawPoint(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawPointList(self, points, pens=None) -> None:
        """ Draw a list of points as quickly as possible.
        """

    def DrawPolygon(self, points, xoffset=0, yoffset=0, fill_style=ODDEVEN_RULE) -> None:
        """ This method draws a filled polygon using a list of Points, adding the optional offset coordinate.
        """

    def DrawPolygonList(self, polygons, pens=None, brushes=None) -> None:
        """ Draw a list of polygons, each of which is a list of points.
        """

    def DrawRectangle(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawRectangleList(self, rectangles, pens=None, brushes=None) -> None:
        """ Draw a list of rectangles as quickly as possible.
        """

    def DrawRotatedText(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawRoundedRectangle(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawSpline(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawText(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawTextList(self, textList, coords, foregrounds=None, backgrounds=None) -> None:
        """ Draw a list of strings using a list of coordinants for positioning each string.
        """

    def EndDoc(self) -> None:
        """ Ends a document (only relevant when outputting to a printer).
        """

    def EndPage(self) -> None:
        """ Ends a document page (only relevant when outputting to a printer).
        """

    def FloodFill(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def FromDIP(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:
        """

    def GetAsBitmap(self, subrect: Optional['Rect']=None) -> 'Bitmap':
        """ If supported by the platform and the type of DC, fetch the contents of the DC, or a subset of it, as a bitmap.
        """

    def GetBackground(self) -> 'Brush':
        """ Gets the brush used for painting the background.
        """

    def GetBackgroundMode(self) -> int:
        """ Returns the current background mode:  BRUSHSTYLE_SOLID   or   BRUSHSTYLE_TRANSPARENT .
        """

    def GetBoundingBox(self) -> None:
        """ Returns the min and max points used in drawing commands so far.
        """

    def GetBrush(self) -> 'Brush':
        """ Gets the current brush.
        """

    def GetCGContext(self) -> 'UIntPtr':
        """ wx.UIntPtr
        """

    def GetCharHeight(self) -> 'Coord':
        """ Gets the character height of the currently set font.
        """

    def GetCharWidth(self) -> 'Coord':
        """ Gets the average character width of the currently set font.
        """

    def GetClippingBox(self) -> tuple:
        """ Gets the rectangle surrounding the current clipping region.
        """

    def GetClippingRect(self) -> None:
        """ Returns the rectangle surrounding the current clipping region as a wx.Rect.
        """

    def GetContentScaleFactor(self) -> float:
        """ Returns the factor used for converting logical pixels to physical ones.
        """

    def GetDepth(self) -> int:
        """ Returns the depth (number of bits/pixel) of this DC.
        """

    def GetDeviceOrigin(self) -> 'Point':
        """ Returns the current device origin.
        """

    def GetFont(self) -> 'Font':
        """ Gets the current font.
        """

    def GetFontMetrics(self) -> 'FontMetrics':
        """ Returns the various font characteristics.
        """

    def GetGdkDrawable(self) -> 'UIntPtr':
        """ wx.UIntPtr
        """

    def GetGraphicsContext(self) -> 'GraphicsContext':
        """ If supported by the platform and the  `   wx.DC `   implementation, this method will return the  `   wx.GraphicsContext `   associated with the DC.
        """

    def GetHDC(self) -> int:
        """ long
        """

    def GetHandle(self) -> 'UIntPtr':
        """ Returns a value that can be used as a handle to the native drawing context, if this   wx.DC  has something that could be thought of in that way.
        """

    def GetLayoutDirection(self) -> int:
        """ Gets the current layout direction of the device context.
        """

    def GetLogicalFunction(self) -> 'RasterOperationMode':
        """ Gets the current logical function.
        """

    def GetLogicalOrigin(self) -> tuple:
        """ Return the coordinates of the logical point (0, 0).
        """

    def GetLogicalScale(self) -> tuple:
        """ Return the scale set by the last call to SetLogicalScale .
        """

    def GetMapMode(self) -> 'MappingMode':
        """ Gets the current mapping mode for the device context.
        """

    def GetFullMultiLineTextExtent(self, string, font=None) -> tuple:
        """ Gets the dimensions of the string as it would be drawn.
        """

    def GetMultiLineTextExtent(self, st: Any) -> None:
        """ Return the dimensions of the given stringâs text extent using the
currently selected font, taking into account multiple lines if
present in the string.
        """

    def GetPPI(self) -> 'Size':
        """ Returns the resolution of the device in pixels per inch.
        """

    def GetPartialTextExtents(self, text) -> None:
        """ Fills the widths  array with the widths from the beginning of text  to the corresponding character of text.
        """

    def GetPen(self) -> 'Pen':
        """ Gets the current pen.
        """

    def GetPixel(self, x, y) -> 'Colour':
        """ Gets the colour at the specified location on the DC.
        """

    def GetSize(self) -> 'Size':
        """ This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
        """

    def GetSizeMM(self) -> 'Size':
        """ This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
        """

    def GetTextBackground(self) -> 'Colour':
        """ Gets the current text background colour.
        """

    def GetFullTextExtent(self, string, font=None) -> tuple:
        """ Gets the dimensions of the string as it would be drawn.
        """

    def GetTextExtent(self, st: Any) -> None:
        """ Return the dimensions of the given stringâs text extent using the
currently selected font.
        """

    def GetTextForeground(self) -> 'Colour':
        """ Gets the current text foreground colour.
        """

    def GetTransformMatrix(self) -> 'AffineMatrix2D':
        """ Return the transformation matrix used by this device context.
        """

    def GetUserScale(self) -> None:
        """ Gets the current user scale factor.
        """

    def GradientFillConcentric(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GradientFillLinear(self, rect, initialColour, destColour, nDirection=RIGHT) -> None:
        """ Fill the area specified by rect  with a linear gradient, starting from initialColour  and eventually fading to destColour.
        """

    def IsOk(self) -> bool:
        """ Returns True if the DC is ok to use.
        """

    def LogicalToDevice(self, *args, **kw) -> 'Point':
        """ Overloaded Implementations:
        """

    def LogicalToDeviceRel(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:
        """

    def LogicalToDeviceX(self, x: int) -> 'Coord':
        """ Converts logical X coordinate to device coordinate, using the current mapping mode, user scale factor, device origin and axis orientation.
        """

    def LogicalToDeviceXRel(self, x: int) -> 'Coord':
        """ Converts logical X coordinate to relative device coordinate, using the current mapping mode and user scale factor but ignoring the axis orientation.
        """

    def LogicalToDeviceY(self, y: int) -> 'Coord':
        """ Converts logical Y coordinate to device coordinate, using the current mapping mode, user scale factor, device origin and axis orientation.
        """

    def LogicalToDeviceYRel(self, y: int) -> 'Coord':
        """ Converts logical Y coordinate to relative device coordinate, using the current mapping mode and user scale factor but ignoring the axis orientation.
        """

    def MaxX(self) -> 'Coord':
        """ Gets the maximum horizontal extent used in drawing commands so far.
        """

    def MaxY(self) -> 'Coord':
        """ Gets the maximum vertical extent used in drawing commands so far.
        """

    def MinX(self) -> 'Coord':
        """ Gets the minimum horizontal extent used in drawing commands so far.
        """

    def MinY(self) -> 'Coord':
        """ Gets the minimum vertical extent used in drawing commands so far.
        """

    def ResetBoundingBox(self) -> None:
        """ Resets the bounding box: after a call to this function, the bounding box doesnât contain anything.
        """

    def ResetTransformMatrix(self) -> None:
        """ Revert the transformation matrix to identity matrix.
        """

    def SetAxisOrientation(self, xLeftRight, yBottomUp) -> None:
        """ Sets the x and y axis orientation (i.e. the direction from lowest to highest values on the axis).
        """

    def SetBackground(self, brush: 'Brush') -> None:
        """ Sets the current background brush for the DC.
        """

    def SetBackgroundMode(self, mode: int) -> None:
        """ Change the current background mode.
        """

    def SetBrush(self, brush: 'Brush') -> None:
        """ Sets the current brush for the DC.
        """

    def SetClippingRegion(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetDeviceClippingRegion(self, region: 'Region') -> None:
        """ Sets the clipping region for this device context.
        """

    def SetDeviceOrigin(self, x, y) -> None:
        """ Sets the device origin (i.e. the origin in pixels after scaling has been applied).
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the current font for the DC.
        """

    def SetGraphicsContext(self, ctx: 'GraphicsContext') -> None:
        """ Associate a   wx.GraphicsContext  with the DC.
        """

    def SetLayoutDirection(self, dir: int) -> None:
        """ Sets the current layout direction for the device context.
        """

    def SetLogicalFunction(self, function: RasterOperationMode) -> None:
        """ Sets the current logical function for the device context.
        """

    def SetLogicalOrigin(self, x, y) -> None:
        """ Change the offset used for translating   wx.DC  coordinates.
        """

    def SetLogicalScale(self, x, y) -> None:
        """ Set the scale to use for translating   wx.DC  coordinates to the physical pixels.
        """

    def SetMapMode(self, mode: MappingMode) -> None:
        """ The mapping mode of the device context defines the unit of measurement used to convert logical  units to device  units.
        """

    def SetPalette(self, palette: 'Palette') -> None:
        """ If this is a window DC or memory DC, assigns the given palette to the window or bitmap associated with the DC.
        """

    def SetPen(self, pen: 'Pen') -> None:
        """ Sets the current pen for the DC.
        """

    def SetTextBackground(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the current text background colour for the DC.
        """

    def SetTextForeground(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the current text foreground colour for the DC.
        """

    def SetTransformMatrix(self, matrix: 'AffineMatrix2D') -> bool:
        """ Set the transformation matrix.
        """

    def SetUserScale(self, xScale, yScale) -> None:
        """ Sets the user scaling factor, useful for applications which require âzoomingâ.
        """

    def StartDoc(self, message: str) -> bool:
        """ Starts a document (only relevant when outputting to a printer).
        """

    def StartPage(self) -> None:
        """ Starts a document page (only relevant when outputting to a printer).
        """

    def StretchBlit(self, xdest, ydest, dstWidth, dstHeight, source, xsrc, ysrc, srcWidth, srcHeight, logicalFunc=COPY, useMask=False, xsrcMask=DefaultCoord, ysrcMask=DefaultCoord) -> bool:
        """ Copy from a source DC to this DC possibly changing the scale.
        """

    def ToDIP(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:
        """

    def _DrawEllipseList(self, pyCoords, pyPens, pyBrushes) -> Any:
        """ PyObject
        """

    def _DrawLineList(self, pyCoords, pyPens, pyBrushes) -> Any:
        """ PyObject
        """

    def _DrawLinesFromBuffer(self, pyBuff) -> Any:
        """ PyObject
        """

    def _DrawPointList(self, pyCoords, pyPens, pyBrushes) -> Any:
        """ PyObject
        """

    def _DrawPolygonList(self, pyCoords, pyPens, pyBrushes) -> Any:
        """ PyObject
        """

    def _DrawRectangleList(self, pyCoords, pyPens, pyBrushes) -> Any:
        """ PyObject
        """

    def _DrawTextList(self, textList, pyPoints, foregroundList, backgroundList) -> Any:
        """ PyObject
        """

    def __bool__(self) -> int:
        """ int
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """

    def __nonzero__(self) -> int:
        """ int
        """

BLACK: int
WHITE: int
BLACK: int
BLACK: int
BLACK: int
WHITE: int
ODDEVEN_RULE: int
WINDING_RULE: int
FLOOD_SURFACE: int
FLOOD_BORDER: int
PostScriptDC: int
MetafileDC: int
NullColour: int
PaintDC: int
BLACK: int
WHITE: int
BLACK: int
BLACK: int
BLACK: int
WHITE: int


class BitmapBundle:
    """ Contains representations of the same bitmap in different resolutions.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Clear(self) -> None:
        """ Clear the existing bundle contents.
        """

    @staticmethod
    def FromBitmap(bitmap: 'Bitmap') -> 'BitmapBundle':
        """ Create a bundle from a single bitmap.
        """

    @staticmethod
    def FromBitmaps(*args, **kw) -> 'BitmapBundle':
        """ Overloaded Implementations:
        """

    @staticmethod
    def FromFiles(*args, **kw) -> 'BitmapBundle':
        """ Overloaded Implementations:
        """

    @staticmethod
    def FromIconBundle(iconBundle: 'IconBundle') -> 'BitmapBundle':
        """ Create a bundle from an icon bundle.
        """

    @staticmethod
    def FromImage(image: 'Image') -> 'BitmapBundle':
        """ Create a bundle from a single image.
        """

    @staticmethod
    def FromImpl(impl: 'BitmapBundleImpl') -> 'BitmapBundle':
        """ Create a bundle from a custom bitmap bundle implementation.
        """

    @staticmethod
    def FromResources(name: str) -> 'BitmapBundle':
        """ Create a bundle from the bitmaps in the application resources.
        """

    @staticmethod
    def FromSVG(data, sizeDef) -> 'BitmapBundle':
        """ This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
        """

    @staticmethod
    def FromSVGFile(path, sizeDef) -> 'BitmapBundle':
        """ Create a bundle from the SVG image loaded from the given file.
        """

    @staticmethod
    def FromSVGResource(name, sizeDef) -> 'BitmapBundle':
        """ Create a bundle from the SVG image loaded from an application resource.
        """

    def GetBitmap(self, size: Union[tuple[int, int], 'Size']) -> 'Bitmap':
        """ Get bitmap of the specified size, creating a new bitmap from the closest available size by rescaling it if necessary.
        """

    def GetBitmapFor(self, window: 'Window') -> 'Bitmap':
        """ Get bitmap of the size appropriate for the DPI scaling used by the given window.
        """

    def GetDefaultSize(self) -> 'Size':
        """ Get the size of the bitmap represented by this bundle in default resolution or, equivalently, at 100% scaling.
        """

    def GetIcon(self, size: Union[tuple[int, int], 'Size']) -> 'Icon':
        """ Get icon of the specified size.
        """

    def GetIconFor(self, window: 'Window') -> 'Icon':
        """ Get icon of the size appropriate for the DPI scaling used by the given window.
        """

    def GetPreferredBitmapSizeAtScale(self, scale: float) -> 'Size':
        """ Get the size that would be best to use for this bundle at the given DPI scaling factor.
        """

    def GetPreferredBitmapSizeFor(self, window: 'Window') -> 'Size':
        """ Get the size that would be best to use for this bundle at the DPI scaling factor used by the given window.
        """

    def GetPreferredLogicalSizeFor(self, window: 'Window') -> 'Size':
        """ Get the size that would be best to use for this bundle at the DPI scaling factor used by the given window in logical size.
        """

    def IsOk(self) -> bool:
        """ Check if bitmap bundle is non-empty.
        """

    def IsSameAs(self, other: 'BitmapBundle') -> bool:
        """ Check if the two bundles refer to the same object.
        """



class BitmapBundleImpl(RefCounter):
    """ Base class for custom implementations of BitmapBundle.
    """
    def DoGetPreferredSize(self, scale: float) -> 'Size':
        """ Helper for implementing GetPreferredBitmapSizeAtScale   in the derived classes.
        """

    def GetBitmap(self, size: Union[tuple[int, int], 'Size']) -> 'Bitmap':
        """ Retrieve the bitmap of exactly the given size.
        """

    def GetDefaultSize(self) -> 'Size':
        """ Return the size of the bitmaps represented by this bundle in the default DPI.
        """

    def GetIndexToUpscale(self, size: Union[tuple[int, int], 'Size']) -> int:
        """ Return the index of the available scale most suitable to be upscaled to the given size.
        """

    def GetNextAvailableScale(self, idx: int) -> tuple:
        """ Return information about the available bitmaps.
        """

    def GetPreferredBitmapSizeAtScale(self, scale: float) -> 'Size':
        """ Return the preferred size that should be used at the given scale.
        """



class BitmapButton(Button):
    """ A bitmap button is a control that contains a bitmap.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, bitmap=NullBitmap, pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=ButtonNameStr) -> bool:
        """ Button creation function for two-step creation.
        """

    def CreateCloseButton(self, parent, winid, name="") -> bool:
        """ Creation function for two-step creation of âCloseâ button.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    @staticmethod
    def NewCloseButton(parent, winid, name="") -> 'BitmapButton':
        """ Helper function creating a standard-looking âCloseâ button.
        """

BU_LEFT: int  #  Left-justifies the bitmap label.
BU_TOP: int  #  Aligns the bitmap label to the top of the button.
BU_RIGHT: int  #  Right-justifies the bitmap label.
BU_BOTTOM: int  #  Aligns the bitmap label to the bottom of the button. ^^
EVT_BUTTON: int  #  Process a  wxEVT_BUTTON   event, when the button is clicked. ^^
BU_LEFT: int
BU_TOP: int
BU_RIGHT: int
BU_BOTTOM: int
BU_EXACTFIT: int
ID_ANY: int


class BitmapDataObject(DataObjectSimple):
    """ BitmapDataObject is a specialization of DataObject for bitmap
data.
    """
    def __init__(self, bitmap: 'Bitmap'=NullBitmap) -> None:
        """ Constructor, optionally passing a bitmap (otherwise use SetBitmap   later).
        """

    def GetAllFormats(self, dir=DataObject.Get) -> None:
        """ Returns a list of wx.DataFormat objects which this data object
supports transferring in the given direction.
        """

    def GetBitmap(self) -> 'Bitmap':
        """ Returns the bitmap associated with the data object.
        """

    def SetBitmap(self, bitmap: 'Bitmap') -> None:
        """ Sets the bitmap associated with the data object.
        """

    def SetData(self, format, buf) -> bool:
        """ bool
        """



class DataObject:
    """ A DataObject represents data that can be copied to or from the
clipboard, or dragged and dropped.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def GetAllFormats(self, dir=Get) -> None:
        """ Returns a list of wx.DataFormat objects which this data object
supports transferring in the given direction.
        """

    def GetDataHere(self, format, buf) -> bool:
        """ Copies this data objectâs data in the requested format to the buffer provided.
        """

    def GetDataSize(self, format: 'DataFormat') -> int:
        """ Returns the data size of the given format format.
        """

    def GetFormatCount(self, dir: int=Get) -> int:
        """ Returns the number of available formats for rendering or setting the data.
        """

    def GetPreferredFormat(self, dir: int=Get) -> 'DataFormat':
        """ Returns the preferred format for either rendering the data (if dir  is  Get , its default value) or for setting it.
        """

    def IsSupported(self, format, dir=Get) -> bool:
        """ Returns True if this format is supported.
        """

    def SetData(self, format, buf) -> bool:
        """ Copies data from the provided buffer to this data object for the specified format.
        """

    def _testGetAllFormats(self) -> None:
        """ 
        """



class BitmapToggleButton(ToggleButton):
    """ BitmapToggleButton is a ToggleButton that contains a bitmap
instead of text.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, label=NullBitmap, pos=DefaultPosition, size=DefaultSize, style=0, val=DefaultValidator, name=CheckBoxNameStr) -> bool:
        """ Create method for two-step construction.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetValue(self) -> bool:
        """ Gets the state of the toggle button.
        """

    def SetValue(self, state: bool) -> None:
        """ Sets the toggle button to the given state.
        """

EVT_TOGGLEBUTTON: int  #  Handles a wxEVT_TOGGLEBUTTON event. ^^


class ToggleButton(AnyButton):
    """ ToggleButton is a button that stays pressed when clicked by the
user.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, label="", pos=DefaultPosition, size=DefaultSize, style=0, val=DefaultValidator, name=CheckBoxNameStr) -> bool:
        """ Creates the toggle button for two-step construction.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetValue(self) -> bool:
        """ Gets the state of the toggle button.
        """

    def SetValue(self, state: bool) -> None:
        """ Sets the toggle button to the given state.
        """

EVT_TOGGLEBUTTON: int  #  Handles a wxEVT_TOGGLEBUTTON event. ^^
ID_ANY: int


class BookCtrlBase(Control, WithImages):
    """ A book control is a convenient way of displaying multiple pages of
information, displayed one page at a time.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddPage(self, page, text, select=False, imageId=NO_IMAGE) -> bool:
        """ Adds a new page.
        """

    def AdvanceSelection(self, forward: bool=True) -> None:
        """ Cycles through the tabs.
        """

    def ChangeSelection(self, page: int) -> int:
        """ Changes the selection to the given page, returning the previous selection.
        """

    def Create(self, parent, winid, pos=DefaultPosition, size=DefaultSize, style=0, name="") -> bool:
        """ Constructs the book control with the given parameters.
        """

    def DeleteAllPages(self) -> bool:
        """ Deletes all pages.
        """

    def DeletePage(self, page: int) -> bool:
        """ Deletes the specified page, and the associated window.
        """

    def FindPage(self, page: 'Window') -> int:
        """ Returns the index of the specified tab window or  NOT_FOUND   if not found.
        """

    def GetCurrentPage(self) -> 'Window':
        """ Returns the currently selected page or None.
        """

    def GetPage(self, page: int) -> 'Window':
        """ Returns the window at the given page position.
        """

    def GetPageCount(self) -> int:
        """ Returns the number of pages in the control.
        """

    def GetPageImage(self, nPage: int) -> int:
        """ Returns the image index for the given page.
        """

    def GetPageText(self, nPage: int) -> str:
        """ Returns the string for the given page.
        """

    def GetSelection(self) -> int:
        """ Returns the currently selected page, or  NOT_FOUND   if none was selected.
        """

    def HitTest(self, pt: 'Point') -> tuple:
        """ Returns the index of the tab at the specified position or  NOT_FOUND   if none.
        """

    def InsertPage(self, index, page, text, select=False, imageId=NO_IMAGE) -> bool:
        """ Inserts a new page at the specified position.
        """

    def RemovePage(self, page: int) -> bool:
        """ Deletes the specified page, without deleting the associated window.
        """

    def SetPageImage(self, page, image) -> bool:
        """ Sets the image index for the given page.
        """

    def SetPageSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the width and height of the pages.
        """

    def SetPageText(self, page, text) -> bool:
        """ Sets the text for the given page.
        """

    def SetSelection(self, page: int) -> int:
        """ Sets the selection to the given page, returning the previous selection.
        """



class BookCtrlEvent(NotifyEvent):
    """ This class represents the events generated by book controls
(wxNotebook, Listbook, Choicebook, Treebook, AuiNotebook).
    """
    def __init__(self, eventType=wxEVT_NULL, id=0, sel=NOT_FOUND, oldSel=NOT_FOUND) -> None:
        """ Constructor (used internally by wxWidgets only).
        """

    def GetOldSelection(self) -> int:
        """ Returns the page that was selected before the change,  NOT_FOUND   if none was selected.
        """

    def GetSelection(self) -> int:
        """ Returns the currently selected page, or  NOT_FOUND   if none was selected.
        """

    def SetOldSelection(self, page: int) -> None:
        """ Sets the id of the page selected before the change.
        """

    def SetSelection(self, page: int) -> None:
        """ Sets the selection member variable.
        """



class Notebook(BookCtrlBase):
    """ This class represents a notebook control, which manages multiple
windows with associated tabs.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def ChangeSelection(self, page: int) -> int:
        """ Changes the selection to the given page, returning the previous selection.
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=NotebookNameStr) -> bool:
        """ Creates a notebook control.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetPageImage(self, nPage: int) -> int:
        """ Returns the image index for the given page.
        """

    def GetPageText(self, nPage: int) -> str:
        """ Returns the string for the given page.
        """

    def GetRowCount(self) -> int:
        """ Returns the number of rows in the notebook control.
        """

    def GetSelection(self) -> int:
        """ Returns the currently selected page, or  NOT_FOUND   if none was selected.
        """

    def GetThemeBackgroundColour(self) -> 'Colour':
        """ If running under Windows and themes are enabled for the application, this function returns a suitable colour for painting the background of a notebook page, and can be passed to SetBackgroundColour .
        """

    def InsertPage(self, index, page, text, select=False, imageId=NO_IMAGE) -> bool:
        """ Inserts a new page at the specified position.
        """

    def SetPadding(self, padding: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the amount of space around each pageâs icon and label, in pixels.
        """

    def SetPageImage(self, page, image) -> bool:
        """ Sets the image index for the given page.
        """

    def SetPageText(self, page, text) -> bool:
        """ Sets the text for the given page.
        """

    def SetSelection(self, page: int) -> int:
        """ Sets the selection to the given page, returning the previous selection.
        """

NB_TOP: int  #  Place tabs on the top side.
NB_LEFT: int  #  Place tabs on the left side.
NB_RIGHT: int  #  Place tabs on the right side.
NB_BOTTOM: int  #  Place tabs under instead of above the notebook pages.
NB_FIXEDWIDTH: int  #  (Windows only) All tabs will have same width.
NB_MULTILINE: int  #  (Windows only) There can be several rows of tabs.
NB_NOPAGETHEME: int  #  (Windows only) Display a solid colour on notebook pages, and not a gradient, which can reduce performance. ^^
EVT_NOTEBOOK_PAGE_CHANGED: int  #  The page selection was changed. Processes a  wxEVT_NOTEBOOK_PAGE_CHANGED   event.
EVT_NOTEBOOK_PAGE_CHANGING: int  #  The page selection is about to be changed. Processes a  wxEVT_NOTEBOOK_PAGE_CHANGING   event. This event can be vetoed. ^^
NB_TOP: int
NB_LEFT: int
NB_RIGHT: int
NB_BOTTOM: int
NB_FIXEDWIDTH: int
NB_MULTILINE: int
NB_NOPAGETHEME: int
NB_LEFT: int
RIGHT: int
BOTTOM: int
CLIP_CHILDREN: int


class Listbook(BookCtrlBase):
    """ Listbook is a class similar to Notebook but which uses a
ListCtrl to show the labels instead of the tabs.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name="") -> bool:
        """ Create the list book control that has already been constructed with the default constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetListView(self, *args, **kw) -> 'ListView':
        """ Overloaded Implementations:
        """

LB_DEFAULT: int  #  Choose the default location for the labels depending on the current platform (left everywhere except Mac where it is top).
LB_TOP: int  #  Place labels above the page area.
LB_LEFT: int  #  Place labels on the left side.
LB_RIGHT: int  #  Place labels on the right side.
LB_BOTTOM: int  #  Place labels below the page area. ^^
EVT_LISTBOOK_PAGE_CHANGED: int  #  The page selection was changed. Processes a  wxEVT_LISTBOOK_PAGE_CHANGED   event.
EVT_LISTBOOK_PAGE_CHANGING: int  #  The page selection is about to be changed. Processes a  wxEVT_LISTBOOK_PAGE_CHANGING   event. This event can be vetoed. ^^
LB_DEFAULT: int
LB_TOP: int
LB_LEFT: int
LB_RIGHT: int
LB_BOTTOM: int


class Choicebook(BookCtrlBase):
    """ Choicebook is a class similar to Notebook, but uses a Choice
control to show the labels instead of the tabs.
    """
    def __init__(self, *args, **kw) -> None:
        """ Constructs a choicebook control.
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name="") -> bool:
        """ Create the choicebook control that has already been constructed with the default constructor.
        """

    def GetChoiceCtrl(self, *args, **kw) -> 'Choice':
        """ Overloaded Implementations:
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

CHB_DEFAULT: int  #  Choose the default location for the labels depending on the current platform (but currently itâs the same everywhere, namely wx.CHB_TOP).
CHB_TOP: int  #  Place labels above the page area.
CHB_LEFT: int  #  Place labels on the left side.
CHB_RIGHT: int  #  Place labels on the right side.
CHB_BOTTOM: int  #  Place labels below the page area. ^^
EVT_CHOICEBOOK_PAGE_CHANGED: int  #  The page selection was changed. Processes a  wxEVT_CHOICEBOOK_PAGE_CHANGED   event.
EVT_CHOICEBOOK_PAGE_CHANGING: int  #  The page selection is about to be changed. Processes a  wxEVT_CHOICEBOOK_PAGE_CHANGING   event. This event can be vetoed (using  wx.NotifyEvent.Veto ). ^^
CHB_DEFAULT: int
CHB_TOP: int
CHB_TOP: int
CHB_LEFT: int
CHB_RIGHT: int
CHB_BOTTOM: int


class Treebook(BookCtrlBase):
    """ This class is an extension of the Notebook class that allows a tree
structured set of pages to be shown in a control.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddPage(self, page, text, bSelect=False, imageId=NOT_FOUND) -> bool:
        """ Adds a new page.
        """

    def AddSubPage(self, page, text, bSelect=False, imageId=NOT_FOUND) -> bool:
        """ Adds a new child-page to the last top-level page.
        """

    def CollapseNode(self, pageId: int) -> bool:
        """ Shortcut for ExpandNode ( pageId, False ).
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=BK_DEFAULT, name="") -> bool:
        """ Creates a treebook control.
        """

    def DeletePage(self, pagePos: int) -> bool:
        """ Deletes the page at the specified position and all its children.
        """

    def ExpandNode(self, pageId, expand=True) -> bool:
        """ Expands (collapses) the pageId  node.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetPageParent(self, page: int) -> int:
        """ Returns the parent page of the given one or  NOT_FOUND   if this is a top-level page.
        """

    def GetSelection(self) -> int:
        """ Returns the currently selected page, or  NOT_FOUND   if none was selected.
        """

    def GetTreeCtrl(self) -> 'TreeCtrl':
        """ Returns the tree control used for selecting pages.
        """

    def InsertPage(self, pagePos, page, text, bSelect=False, imageId=NOT_FOUND) -> bool:
        """ Inserts a new page just before the page indicated by pagePos.
        """

    def InsertSubPage(self, pagePos, page, text, bSelect=False, imageId=NOT_FOUND) -> bool:
        """ Inserts a sub page under the specified page.
        """

    def IsNodeExpanded(self, pageId: int) -> bool:
        """ Returns True if the page represented by pageId  is expanded.
        """

EVT_TREEBOOK_PAGE_CHANGED: int  #  The page selection was changed. Processes a  wxEVT_TREEBOOK_PAGE_CHANGED   event.
EVT_TREEBOOK_PAGE_CHANGING: int  #  The page selection is about to be changed. Processes a  wxEVT_TREEBOOK_PAGE_CHANGING   event. This event can be  vetoed.
EVT_TREEBOOK_NODE_COLLAPSED: int  #  The page node is going to be collapsed. Processes a  wxEVT_TREEBOOK_NODE_COLLAPSED   event.
EVT_TREEBOOK_NODE_EXPANDED: int  #  The page node is going to be expanded. Processes a  wxEVT_TREEBOOK_NODE_EXPANDED   event. ^^


class BoxSizer(Sizer):
    """ The basic idea behind a box sizer is that windows will most often be
laid out in rather simple basic geometry, typically in a row or a
column or several hierarchies of either.
    """
    def __init__(self, orient: int=HORIZONTAL) -> None:
        """ Constructor for a   wx.BoxSizer.
        """

    def AddSpacer(self, size: int) -> 'SizerItem':
        """ Adds non-stretchable space to the main orientation of the sizer only.
        """

    def CalcMin(self) -> 'Size':
        """ Implements the calculation of a box sizerâs minimal.
        """

    def GetOrientation(self) -> int:
        """ Returns the orientation of the box sizer, either wx.VERTICAL or wx.HORIZONTAL.
        """

    def RepositionChildren(self, minSize: Union[tuple[int, int], 'Size']) -> None:
        """ Method which must be overridden in the derived sizer classes.
        """

    def SetOrientation(self, orient: int) -> None:
        """ Sets the orientation of the box sizer, either wx.VERTICAL or wx.HORIZONTAL.
        """

VERTICAL: int
HORIZONTAL: int
VERTICAL: int
HORIZONTAL: int
VERTICAL: int
HORIZONTAL: int
VERTICAL: int
HORIZONTAL: int
VERTICAL: int
HORIZONTAL: int


class Brush(GDIObject):
    """ A brush is a drawing tool for filling in areas.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetColour(self) -> 'Colour':
        """ Returns a reference to the brush colour.
        """

    def GetStipple(self) -> 'Bitmap':
        """ Gets a pointer to the stipple bitmap.
        """

    def GetStyle(self) -> 'BrushStyle':
        """ Returns the brush style, one of the   wx.BrushStyle  values.
        """

    def IsHatch(self) -> bool:
        """ Returns True if the style of the brush is any of hatched fills.
        """

    def IsNonTransparent(self) -> bool:
        """ Returns True if the brush is a valid non-transparent brush.
        """

    def IsOk(self) -> bool:
        """ Returns True if the brush is initialised.
        """

    def IsTransparent(self) -> bool:
        """ Returns True if the brush is transparent.
        """

    def MacSetTheme(self, macThemeBrushID) -> None:
        """ 
        """

    def SetColour(self, *args, **kw) -> None:
        """ Sets the brush colour using red, green and blue values.
        """

    def SetStipple(self, bitmap: 'Bitmap') -> None:
        """ Sets the stipple bitmap.
        """

    def SetStyle(self, style: BrushStyle) -> None:
        """ Sets the brush style.
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """

    def _copyFrom(self, other) -> None:
        """ For internal use only.
        """

    def __ne__(self, item: Any) -> bool:
        """ Inequality operator.
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.
        """

BRUSHSTYLE_TRANSPARENT: int
BRUSHSTYLE_TRANSPARENT: int
BRUSHSTYLE_TRANSPARENT: int


class BrushList:
    """ A brush list is a list containing all brushes which have been created.
    """
    def FindOrCreateBrush(self, colour, style=BRUSHSTYLE_SOLID) -> 'Brush':
        """ Finds a brush with the specified attributes and returns it, else creates a new brush, adds it to the brush list, and returns it.
        """



class BufferedDC(MemoryDC):
    """ This class provides a simple way to avoid flicker: when drawing on it,
everything is in fact first drawn on an in-memory buffer (a Bitmap)
and then copied to the screen, using the associated DC, only once,
when this object is destroyed.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetStyle(self) -> int:
        """ Get the style.
        """

    def Init(self, *args, **kw) -> None:
        """ Initializes the object created using the default constructor.
        """

    def SetStyle(self, style: int) -> None:
        """ Set the style.
        """

    def UnMask(self) -> None:
        """ Blits the buffer to the dc, and detaches the dc from the buffer (so it can be effectively used once only).
        """

BUFFER_CLIENT_AREA: int
BUFFER_VIRTUAL_AREA: int
BUFFER_CLIENT_AREA: int
BUFFER_VIRTUAL_AREA: int


class BufferedPaintDC(BufferedDC):
    """ This is a subclass of BufferedDC which can be used inside of an
EVT_PAINT() event handler to achieve double-buffered drawing.
    """
    def __init__(self, *args, **kw) -> None:
        """ As with   wx.BufferedDC, you may either provide the bitmap to be used for buffering or let this object create one internally (in the latter case, the size of the client part of the window is used).
        """

BG_STYLE_PAINT: int
BUFFER_CLIENT_AREA: int
BUFFER_VIRTUAL_AREA: int


class BusyCursor:
    """ This class makes it easy to tell your user that the program is
temporarily busy.
    """
    def __init__(self, cursor: 'Cursor'=HOURGLASS_CURSOR) -> None:
        """ Constructs a busy cursor object, calling wx.BeginBusyCursor     .
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class BusyInfo:
    """ This class makes it easy to tell your user that the program is
temporarily busy.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def UpdateLabel(self, str: str) -> None:
        """ Same as UpdateText   but doesnât interpret the string as containing markup.
        """

    def UpdateText(self, str: str) -> None:
        """ Update the information text.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class BusyInfoFlags:
    """ Parameters for BusyInfo.
    """
    def __init__(self) -> None:
        """ Default constructor initializes all attributes to default values.
        """

    def Background(self, background: Union[int, str, 'Colour']) -> 'BusyInfoFlags':
        """ Sets the background colour of   wx.BusyInfo  window.
        """

    def Foreground(self, foreground: Union[int, str, 'Colour']) -> 'BusyInfoFlags':
        """ Sets the foreground colour of the title and text strings.
        """

    def Icon(self, icon: 'Icon') -> 'BusyInfoFlags':
        """ Sets the icon to show in   wx.BusyInfo.
        """

    def Label(self, label: str) -> 'BusyInfoFlags':
        """ Same as Text   but doesnât interpret the string as containing markup.
        """

    def Parent(self, parent: 'Window') -> 'BusyInfoFlags':
        """ Sets the parent for   wx.BusyInfo.
        """

    def Text(self, text: str) -> 'BusyInfoFlags':
        """ Sets the more detailed text, shown under the title, if any.
        """

    def Title(self, title: str) -> 'BusyInfoFlags':
        """ Sets the title, shown prominently in   wx.BusyInfo  window.
        """

    def Transparency(self, alpha: 'Byte') -> 'BusyInfoFlags':
        """ Sets the transparency of   wx.BusyInfo  window.
        """

ALPHA_TRANSPARENT: int
ALPHA_OPAQUE: int


class Button(AnyButton):
    """ A button is a control that contains a text string, and is one of the
most common elements of a GUI.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, label="", pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=ButtonNameStr) -> bool:
        """ Button creation function for two-step creation.
        """

    def GetAuthNeeded(self) -> bool:
        """ Returns True if an authentication needed symbol is displayed on the button.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    @staticmethod
    def GetDefaultSize(win: Optional['Window']=None) -> 'Size':
        """ Returns the default size for the buttons.
        """

    def GetLabel(self) -> str:
        """ Returns the string label for the button.
        """

    def SetAuthNeeded(self, needed: bool=True) -> None:
        """ Sets whether an authentication needed symbol should be displayed on the button.
        """

    def SetDefault(self) -> 'Window':
        """ This sets the button to be the default item in its top-level window (e.g.
        """

    def SetLabel(self, label: str) -> None:
        """ Sets the string label for the button.
        """

BU_LEFT: int  #  Left-justifies the label. Windows and GTK+ only.
BU_TOP: int  #  Aligns the label to the top of the button. Windows and GTK+ only.
BU_RIGHT: int  #  Right-justifies the bitmap label. Windows and GTK+ only.
BU_BOTTOM: int  #  Aligns the label to the bottom of the button. Windows and GTK+ only.
BU_EXACTFIT: int  #  By default, all buttons are made of at least the standard button size, even if their contents is small enough to fit into a smaller size. This is done for consistency as most platforms use buttons of the same size in the native dialogs, but can be overridden by specifying this flag. If it is given, the button will be made just big enough for its contents. Notice that under MSW the button will still have at least the standard height, even with this style, if it has a non-empty label.
BU_NOTEXT: int  #  Disables the display of the text label in the button even if it has one or its id is one of the standard stock ids with an associated label: int  #  without using this style a button which is only supposed to show a bitmap but uses a standard id would display a label too.
BORDER_NONE: int  #  Creates a button without border. This is currently implemented in MSW, GTK2 and OSX/Cocoa. ^^
EVT_BUTTON: int  #  Process a  wxEVT_BUTTON   event, when the button is clicked. ^^
BU_LEFT: int
BU_TOP: int
BU_RIGHT: int
BU_BOTTOM: int
BU_EXACTFIT: int
BU_NOTEXT: int
BORDER_NONE: int


class CallLater:
    """ A convenience class for wx.Timer, that calls the given callable
object once after the given amount of milliseconds, passing any
positional or keyword args.  The return value of the callable is
available after it has been run with the GetResult
method.
    """
    def __init__(self, millis, callableObj, *args, **kwargs) -> None:
        """ Constructs a new wx.CallLater object.
        """

    def GetInterval(self) -> None:
        """ 
        """

    def GetResult(self) -> Any:
        """ Returns the value of the callable.
        """

    def HasRun(self) -> bool:
        """ Returns whether or not the callable has run.
        """

    def IsRunning(self) -> None:
        """ 
        """

    def Notify(self) -> None:
        """ The timer has expired so call the callable.
        """

    def SetArgs(self, *args, **kwargs) -> None:
        """ (Re)set the args passed to the callable object.  This is
useful in conjunction with Start if
you want to schedule a new call to the same callable
object but with different parameters.
        """

    def Start(self, millis=None, *args, **kwargs) -> None:
        """ (Re)start the timer
        """

    def Stop(self) -> None:
        """ Stop and destroy the timer.
        """

    def __del__(self) -> None:
        """ 
        """



class Timer(EvtHandler):
    """ The Timer class allows you to execute code at specified intervals.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetId(self) -> int:
        """ Returns the ID of the events generated by this timer.
        """

    def GetInterval(self) -> int:
        """ Returns the current interval for the timer (in milliseconds).
        """

    def GetOwner(self) -> 'EvtHandler':
        """ Returns the current owner  of the timer.
        """

    def IsOneShot(self) -> bool:
        """ Returns True if the timer is one shot, i.e. if it will stop after firing the first notification automatically.
        """

    def IsRunning(self) -> bool:
        """ Returns True if the timer is running, False if it is stopped.
        """

    def Notify(self) -> None:
        """ This member should be overridden by the user if the default constructor was used and SetOwner   wasnât called.
        """

    def SetOwner(self, owner, id=-1) -> None:
        """ Associates the timer with the given owner  object.
        """

    def Start(self, milliseconds=-1, oneShot=TIMER_CONTINUOUS) -> bool:
        """ (Re)starts the timer.
        """

    def StartOnce(self, milliseconds: int=-1) -> bool:
        """ Starts the timer for a once-only notification.
        """

    def Stop(self) -> None:
        """ Stops the timer.
        """

TIMER_CONTINUOUS: int
TIMER_ONE_SHOT: int


class Caret:
    """ A caret is a blinking cursor showing the position where the typed text
will appear.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, *args, **kw) -> bool:
        """ Creates a caret with the given size (in pixels) and associates it with the window  (same as the equivalent constructors).
        """

    @staticmethod
    def GetBlinkTime() -> int:
        """ Returns the blink time which is measured in milliseconds and is the time elapsed between 2 inversions of the caret (blink time of the caret is the same for all carets, so this functions is static).
        """

    def GetPosition(self) -> None:
        """ Get the caret position (in pixels).
        """

    def GetSize(self) -> None:
        """ Get the caret size.
        """

    def GetWindow(self) -> 'Window':
        """ Get the window the caret is associated with.
        """

    def Hide(self) -> None:
        """ Hides the caret, same as Show(false).
        """

    def IsOk(self) -> bool:
        """ Returns True if the caret was created successfully.
        """

    def IsVisible(self) -> bool:
        """ Returns True if the caret is visible and False if it is permanently hidden (if it is blinking and not shown currently but will be after the next blink, this method still returns True).
        """

    def Move(self, *args, **kw) -> None:
        """ Move the caret to given position (in logical coordinates).
        """

    @staticmethod
    def SetBlinkTime(milliseconds: int) -> None:
        """ Sets the blink time for all the carets.
        """

    def SetSize(self, *args, **kw) -> None:
        """ Changes the size of the caret.
        """

    def Show(self, show: bool=True) -> None:
        """ Shows or hides the caret.
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """



class CheckBox(Control):
    """ A checkbox is a labelled box which by default is either on (checkmark
is visible) or off (no checkmark).
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, label="", pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=CheckBoxNameStr) -> bool:
        """ Creates the checkbox for two-step construction.
        """

    def Get3StateValue(self) -> 'CheckBoxState':
        """ Gets the state of a 3-state checkbox.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetValue(self) -> bool:
        """ Gets the state of a 2-state checkbox.
        """

    def Is3State(self) -> bool:
        """ Returns whether or not the checkbox is a 3-state checkbox.
        """

    def Is3rdStateAllowedForUser(self) -> bool:
        """ Returns whether or not the user can set the checkbox to the third state.
        """

    def IsChecked(self) -> bool:
        """ This is just a maybe more readable synonym for GetValue : just as the latter, it returns True if the checkbox is checked and False otherwise.
        """

    def Set3StateValue(self, state: CheckBoxState) -> None:
        """ Sets the checkbox to the given state.
        """

    def SetValue(self, state: bool) -> None:
        """ Sets the checkbox to the given state.
        """

CHK_2STATE: int  #  Create a 2-state checkbox. This is the default.
CHK_3STATE: int  #  Create a 3-state checkbox.
CHK_ALLOW_3RD_STATE_FOR_USER: int  #  By default a user canât set a 3-state checkbox to the third state. It can only be done from code. Using this flags allows the user to set the checkbox to the third state by clicking.
ALIGN_RIGHT: int  #  Makes the text appear on the left of the checkbox. ^^
EVT_CHECKBOX: int  #  Process a  wxEVT_CHECKBOX   event, when the checkbox is clicked. ^^
CHK_3STATE: int
CHK_2STATE: int
CHK_3STATE: int
CHK_ALLOW_3RD_STATE_FOR_USER: int
ALIGN_RIGHT: int
ID_ANY: int
CHK_UNDETERMINED: int


class CheckListBox(ListBox):
    """ A CheckListBox is like a ListBox, but allows items to be checked
or unchecked.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Check(self, item, check=True) -> None:
        """ Checks the given item.
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, choices=[], style=0, validator=DefaultValidator, name=ListBoxNameStr) -> bool:
        """ parent (wx.Window) â
        """

    def GetCheckedItems(self) -> None:
        """ GetCheckedItems()
        """

    def GetCheckedStrings(self) -> None:
        """ GetCheckedStrings()
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetSelections(self) -> list[int]:
        """ Returns a list of the indices of the currently selected items.
        """

    def IsChecked(self, item: int) -> bool:
        """ Returns True if the given item is checked, False otherwise.
        """

    def SetCheckedItems(self, indexes) -> None:
        """ SetCheckedItems(indexes)
        """

    def SetCheckedStrings(self, strings) -> None:
        """ SetCheckedStrings(strings)
        """

EVT_CHECKLISTBOX: int  #  Process a  wxEVT_CHECKLISTBOX   event, when an item in the check list box is checked or unchecked.  wx.CommandEvent.GetInt   will contain the index of the item that was checked or unchecked. wx.CommandEvent.IsChecked   is not valid! Use wx.CheckListBox.IsChecked   instead. ^^
ID_ANY: int


class ListBox(Control, ItemContainer):
    """ A listbox is used to select one or more of a list of strings.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, choices=[], style=0, validator=DefaultValidator, name=ListBoxNameStr) -> bool:
        """ Creates the listbox for two-step construction.
        """

    def Deselect(self, n: int) -> None:
        """ Deselects an item in the list box.
        """

    def EnsureVisible(self, n: int) -> None:
        """ Ensure that the item with the given index is currently shown.
        """

    def FindString(self, string, caseSensitive=False) -> int:
        """ Finds an item whose label matches the given string.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetCount(self) -> int:
        """ Returns the number of items in the control.
        """

    def GetCountPerPage(self) -> int:
        """ Return the number of items that can fit vertically in the visible area of the listbox.
        """

    def GetSelection(self) -> int:
        """ Returns the index of the selected item or  NOT_FOUND   if no item is selected.
        """

    def GetSelections(self) -> list[int]:
        """ Fill an array of ints with the positions of the currently selected items.
        """

    def GetString(self, n: int) -> str:
        """ Returns the label of the item with the given index.
        """

    def GetTopItem(self) -> int:
        """ Return the index of the topmost visible item.
        """

    def HitTest(self, *args, **kw) -> int:
        """ Overloaded Implementations:
        """

    def InsertItems(self, items, pos) -> None:
        """ Insert the given number of strings before the specified position.
        """

    def IsSelected(self, n: int) -> bool:
        """ Determines whether an item is selected.
        """

    def IsSorted(self) -> bool:
        """ Return True if the listbox has LB_SORT  style.
        """

    def MSWSetTabStops(self, tabStops) -> None:
        """ 
        """

    def SetFirstItem(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetItemBackgroundColour(self, item, c) -> None:
        """ Set the background colour of an item in the ListBox.
Only valid on MSW and if the wx.LB_OWNERDRAW flag is set.
        """

    def SetItemFont(self, item, f) -> None:
        """ Set the font of an item in the ListBox.
Only valid on MSW and if the wx.LB_OWNERDRAW flag is set.
        """

    def SetItemForegroundColour(self, item, c) -> None:
        """ Set the foreground colour of an item in the ListBox.
Only valid on MSW and if the wx.LB_OWNERDRAW flag is set.
        """

    def SetSelection(self, n: int) -> None:
        """ Sets the selection to the given item n  or removes the selection entirely if n  ==  NOT_FOUND .
        """

    def SetString(self, n, string) -> None:
        """ Sets the label for the given item.
        """

    def SetStringSelection(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

LB_SINGLE: int  #  Single-selection list.
LB_MULTIPLE: int  #  Multiple-selection list: int  #  the user can toggle multiple items on and off. This is the same as wx.LB_EXTENDED in wxGTK2 port.
LB_EXTENDED: int  #  Extended-selection list: int  #  the user can extend the selection by using  SHIFT   or   CTRL   keys together with the cursor movement keys or the mouse.
LB_HSCROLL: int  #  Create horizontal scrollbar if contents are too wide (Windows only).
LB_ALWAYS_SB: int  #  Always show a vertical scrollbar.
LB_NEEDED_SB: int  #  Only create a vertical scrollbar if needed.
LB_NO_SB: int  #  Donât create vertical scrollbar (wxMSW and wxGTK only).
LB_SORT: int  #  The listbox contents are sorted in alphabetical order. ^^
EVT_LISTBOX: int  #  Process a  wxEVT_LISTBOX   event, when an item on the list is selected or the selection changes.
EVT_LISTBOX_DCLICK: int  #  Process a  wxEVT_LISTBOX_DCLICK   event, when the listbox is double-clicked. On some platforms (notably wxGTK2) pressing the enter key is handled as an equivalent of a double-click. ^^
LB_SINGLE: int
LB_MULTIPLE: int
LB_EXTENDED: int
LB_EXTENDED: int
LB_HSCROLL: int
LB_ALWAYS_SB: int
LB_NEEDED_SB: int
LB_NO_SB: int
LB_SORT: int
NOT_FOUND: int
LB_MULTIPLE: int
NOT_FOUND: int
LB_OWNERDRAW: int
LB_OWNERDRAW: int
LB_OWNERDRAW: int


class ChildFocusEvent(CommandEvent):
    """ A child focus event is sent to a (parent-)window when one of its child
windows gains focus, so that the window could restore the focus back
to its corresponding child if it loses it now and regains later.
    """
    def __init__(self, win: Optional['Window']=None) -> None:
        """ Constructor.
        """

    def GetWindow(self) -> 'Window':
        """ Returns the direct child which receives the focus, or a (grand-)parent of the control receiving the focus.
        """

EVT_CHILD_FOCUS: int  #  Process a  wxEVT_CHILD_FOCUS   event. ^^


class Choice(Control, ItemContainer):
    """ A choice item is used to select one of a list of strings.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, choices=[], style=0, validator=DefaultValidator, name=ChoiceNameStr) -> bool:
        """ Creates the choice for two-step construction.
        """

    def FindString(self, string, caseSensitive=False) -> int:
        """ Finds an item whose label matches the given string.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetColumns(self) -> int:
        """ Gets the number of columns in this choice item.
        """

    def GetCount(self) -> int:
        """ Returns the number of items in the control.
        """

    def GetCurrentSelection(self) -> int:
        """ Unlike wx.ControlWithItems.GetSelection   which only returns the accepted selection value (the selection in the control once the user closes the dropdown list), this function returns the current selection.
        """

    def GetSelection(self) -> int:
        """ Returns the index of the selected item or  NOT_FOUND   if no item is selected.
        """

    def GetString(self, n: int) -> str:
        """ Returns the label of the item with the given index.
        """

    def IsSorted(self) -> bool:
        """ bool
        """

    def SetColumns(self, n: int=1) -> None:
        """ Sets the number of columns in this choice item.
        """

    def SetSelection(self, n: int) -> None:
        """ Sets the selection to the given item n  or removes the selection entirely if n  ==  NOT_FOUND .
        """

    def SetString(self, n, string) -> None:
        """ Sets the label for the given item.
        """

CB_SORT: int  #  Sorts the entries alphabetically. ^^
EVT_CHOICE: int  #  Process a  wxEVT_CHOICE   event, when an item on the list is selected. ^^
CB_SORT: int
ID_ANY: int
NOT_FOUND: int


class ClassInfo:
    """ This class stores meta-information about classes.
    """
    def CreateObject(self) -> 'Window':
        """ Creates an object of the appropriate kind.
        """

    @staticmethod
    def FindClass(className: str) -> 'ClassInfo':
        """ Finds the   wx.ClassInfo  object for a class with the given name.
        """

    def GetBaseClassName1(self) -> 'Char':
        """ Returns the name of the first base class (None if none).
        """

    def GetBaseClassName2(self) -> 'Char':
        """ Returns the name of the second base class (None if none).
        """

    def GetClassName(self) -> 'Char':
        """ Returns the string form of the class name.
        """

    def GetSize(self) -> int:
        """ Returns the size of the class.
        """

    def IsDynamic(self) -> bool:
        """ Returns True if this class info can create objects of the associated class.
        """

    def IsKindOf(self, info: 'ClassInfo') -> bool:
        """ Returns True if this class is a kind of (inherits from) the given class.
        """



class ClientDataContainer:
    """ This class is a mixin that provides storage and management of âclient
dataâ.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def GetClientData(self) -> ClientData:
        """ Get a pointer to the client data object.
        """

    def GetClientObject(self) -> Any:
        """ Alias for GetClientData
        """

    def SetClientData(self, data: ClientData) -> None:
        """ Set the client data object.
        """

    def SetClientObject(self, data) -> Any:
        """ Alias for SetClientData
        """



class ClientDC(WindowDC):
    """ ClientDC is primarily useful for obtaining information about the
window from outside EVT_PAINT() handler.
    """
    def __init__(self, window: 'Window') -> None:
        """ Constructor.
        """



class Clipboard(Object):
    """ A class for manipulating the clipboard.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def AddData(self, data: 'DataObject') -> bool:
        """ Call this function to add the data object to the clipboard.
        """

    def Clear(self) -> None:
        """ Clears the global clipboard object and the systemâs clipboard if possible.
        """

    def Close(self) -> None:
        """ Call this function to close the clipboard, having opened it with Open .
        """

    def Flush(self) -> bool:
        """ Flushes the clipboard: this means that the data which is currently on clipboard will stay available even after the application exits (possibly eating memory), otherwise the clipboard will be emptied on exit.
        """

    @staticmethod
    def Get() -> 'Clipboard':
        """ Returns the global instance (wxTheClipboard) of the clipboard object.
        """

    def GetData(self, data: 'DataObject') -> bool:
        """ Call this function to fill data  with data on the clipboard, if available in the required format.
        """

    def IsOpened(self) -> bool:
        """ Returns True if the clipboard has been opened.
        """

    def IsSupported(self, format: 'DataFormat') -> bool:
        """ Returns True if there is data which matches the data format of the given data object currently available  on the clipboard.
        """

    def IsUsingPrimarySelection(self) -> bool:
        """ Returns True if we are using the primary selection, False if clipboard one.
        """

    def Open(self) -> bool:
        """ Call this function to open the clipboard before calling SetData   and GetData .
        """

    def SetData(self, data: 'DataObject') -> bool:
        """ Call this function to set the data object to the clipboard.
        """

    def UsePrimarySelection(self, primary: bool=False) -> None:
        """ On platforms supporting it (all X11-based ports),   wx.Clipboard  uses the CLIPBOARD X11 selection by default.
        """



class ClipboardTextEvent(CommandEvent):
    """ This class represents the events generated by a control (typically a
TextCtrl but other windows can generate these events as well) when
its content gets copied or cut to, or pasted from the clipboard.
    """
    def __init__(self, commandType=wxEVT_NULL, id=0) -> None:
        """ Constructor.
        """

EVT_TEXT_COPY: int  #  Some or all of the controls content was copied to the clipboard.
EVT_TEXT_CUT: int  #  Some or all of the controls content was cut (i.e. copied and deleted).
EVT_TEXT_PASTE: int  #  Clipboard content was pasted into the control. ^^
COPY: int
CB_READONLY: int


class TextCtrl(Control, TextEntry):
    """ A text control allows text to be displayed and edited.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, value="", pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=TextCtrlNameStr) -> bool:
        """ Creates the text control for two-step construction.
        """

    def DiscardEdits(self) -> None:
        """ Resets the internal modified flag as if the current changes had been saved.
        """

    def EmptyUndoBuffer(self) -> None:
        """ Delete the undo history.
        """

    def EmulateKeyPress(self, event: 'KeyEvent') -> bool:
        """ This function inserts into the control the character which would have been inserted if the given key event had occurred in the text control.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetDefaultStyle(self) -> 'TextAttr':
        """ Returns the style currently used for the new text.
        """

    def GetLineLength(self, lineNo: int) -> int:
        """ Gets the length of the specified line, not including any trailing newline character(s).
        """

    def GetLineText(self, lineNo: int) -> str:
        """ Returns the contents of a given line in the text control, not including any trailing newline character(s).
        """

    def GetNumberOfLines(self) -> int:
        """ Returns the number of lines in the text control buffer.
        """

    def GetStyle(self, position, style) -> bool:
        """ Returns the style at this position in the text control.
        """

    def HideNativeCaret(self) -> bool:
        """ Turn off the widgetâs native caret on Windows.
Ignored on other platforms.
        """

    def HitTestPos(self, pt) -> None:
        """ Finds the position of the character at the specified point.
        """

    def HitTest(self, pt) -> None:
        """ Finds the row and column of the character at the specified point.
        """

    def IsModified(self) -> bool:
        """ Returns True if the text has been modified by user.
        """

    def IsMultiLine(self) -> bool:
        """ Returns True if this is a multi line edit control and False otherwise.
        """

    def IsSingleLine(self) -> bool:
        """ Returns True if this is a single line edit control and False otherwise.
        """

    def LoadFile(self, filename, fileType=TEXT_TYPE_ANY) -> bool:
        """ Loads and displays the named file, if it exists.
        """

    def MacCheckSpelling(self, check) -> None:
        """ Turn on the native spell checking for the text widget on
OSX.  Ignored on other platforms.
        """

    def MarkDirty(self) -> None:
        """ Mark text as modified (dirty).
        """

    def OSXDisableAllSmartSubstitutions(self) -> None:
        """ Mac-only method to disable all automatic text substitutions.
        """

    def OSXEnableAutomaticDashSubstitution(self, enable) -> None:
        """ Mac-only method for turning on/off automatic dash substitutions.
        """

    def OSXEnableAutomaticQuoteSubstitution(self, enable) -> None:
        """ Mac-only method for turning on/off automatic quote substitutions.
        """

    def OSXEnableNewLineReplacement(self, enable: bool) -> None:
        """ Enable the automatic replacement of new lines characters in a single-line text field with spaces under macOS.
        """

    def PositionToCoords(self, pos: int) -> 'Point':
        """ Converts given text position to client coordinates in pixels.
        """

    def PositionToXY(self, pos: int) -> tuple:
        """ Converts given position to a zero-based column, line number pair.
        """

    def SaveFile(self, filename="", fileType=TEXT_TYPE_ANY) -> bool:
        """ Saves the contents of the control in a text file.
        """

    def SetDefaultStyle(self, style: 'TextAttr') -> bool:
        """ Changes the default style to use for the new text which is going to be added to the control.
        """

    def SetModified(self, modified: bool) -> None:
        """ Marks the control as being modified by the user or not.
        """

    def SetStyle(self, start, end, style) -> bool:
        """ Changes the style of the given range.
        """

    def ShowNativeCaret(self, show=True) -> bool:
        """ Turn on the widgetâs native caret on Windows.
Ignored on other platforms.
        """

    def ShowPosition(self, pos: int) -> None:
        """ Makes the line containing the given position visible.
        """

    def XYToPosition(self, x, y) -> int:
        """ Converts the given zero based column and line number to a position.
        """

    def flush(self) -> None:
        """ NOP, for file-like compatibility.
        """

    def write(self, text) -> None:
        """ Append text to the textctrl, for file-like compatibility.
        """

TE_PROCESS_ENTER: int  #  The control will generate the event  wxEVT_TEXT_ENTER   that can be handled by the program. Otherwise, i.e. either if this style not specified at all, or it is used, but there is no event handler for this event or the event handler called  wx.Event.Skip   to avoid overriding the default handling, pressing Enter key is either processed internally by the control or used to activate the default button of the dialog, if any.
TE_PROCESS_TAB: int  #  Normally, TAB key is used for keyboard navigation and pressing it in a control switches focus to the next one. With this style, this wonât happen and if the TAB is not otherwise processed (e.g. by  wxEVT_CHAR   event handler), a literal TAB character is inserted into the control. Notice that this style has no effect for single-line text controls when using wxGTK.
TE_MULTILINE: int  #  The text control allows multiple lines. If this style is not specified, line break characters should not be used in the controls value.
TE_PASSWORD: int  #  The text will be echoed as asterisks.
TE_READONLY: int  #  The text will not be user-editable.
TE_RICH: int  #  Use rich text control under MSW, this allows having more than 64KB of text in the control. This style is ignored under other platforms and it is recommended to use wx.TE_RICH2 instead of it under MSW.
TE_RICH2: int  #  Use rich text control version 2.0 or higher under MSW, this style is ignored under other platforms. Note that this style may be turned on automatically even if it is not used explicitly when creating a text control with a long (i.e. much more than 64KiB) initial text, as creating the control would simply fail in this case under MSW if neither this style nor wx.TE_RICH is used.
TE_AUTO_URL: int  #  Highlight the URLs and generate the TextUrlEvents when mouse events occur over them.
TE_NOHIDESEL: int  #  By default, the Windows text control doesnât show the selection when it doesnât have focus - use this style to force it to always show it. It doesnât do anything under other platforms.
HSCROLL: int  #  A horizontal scrollbar will be created and used, so that text wonât be wrapped.
TE_NO_VSCROLL: int  #  For multiline controls only: int  #  vertical scrollbar will never be created. This limits the amount of text which can be entered into the control to what can be displayed in it under wxMSW but not under wxGTK or wxOSX. Currently not implemented for the other platforms.
TE_LEFT: int  #  The text in the control will be left-justified (default).
TE_CENTRE: int  #  The text in the control will be centered (wxMSW, wxGTK, wxOSX).
TE_RIGHT: int  #  The text in the control will be right-justified (wxMSW, wxGTK, wxOSX).
TE_DONTWRAP: int  #  Same as wx.HSCROLL style: int  #  donât wrap at all, show horizontal scrollbar instead.
TE_CHARWRAP: int  #  For multiline controls only: int  #  wrap the lines too long to be shown entirely at any position (wxUniv, wxGTK, wxOSX).
TE_WORDWRAP: int  #  For multiline controls only: int  #  wrap the lines too long to be shown entirely at word boundaries (wxUniv, wxMSW, wxGTK, wxOSX).
TE_BESTWRAP: int  #  For multiline controls only: int  #  wrap the lines at word boundaries or at any other character if there are words longer than the window width (this is the default).
TE_CAPITALIZE: int  #  On PocketPC and Smartphone, causes the first letter to be capitalized. ^^
EVT_TEXT: int  #  Respond to a  wxEVT_TEXT   event, generated when the text changes. Notice that this event will be sent when the text controls contents changes  â wx.TextCtrl.SetValue   is called); see wx.TextCtrl.ChangeValue   for a function which does not send this event. This event is however not sent during the control creation.
EVT_TEXT_ENTER: int  #  Respond to a  wxEVT_TEXT_ENTER   event, generated when enter is pressed in a text control which must have wx.TE_PROCESS_ENTER style for this event to be generated.
EVT_TEXT_URL: int  #  A mouse event occurred over an URL in the text control.
EVT_TEXT_MAXLEN: int  #  This event is generated when the user tries to enter more text into the control than the limit set by wx.TextCtrl.SetMaxLength , see its description. ^^
TE_PROCESS_ENTER: int
TE_PROCESS_TAB: int
TE_MULTILINE: int
TE_PASSWORD: int
TE_READONLY: int
TE_RICH: int
TE_RICH2: int
TE_RICH2: int
TE_RICH: int
TE_AUTO_URL: int
TE_NOHIDESEL: int
HSCROLL: int
TE_NO_VSCROLL: int
TE_LEFT: int
TE_CENTRE: int
TE_RIGHT: int
TE_DONTWRAP: int
HSCROLL: int
TE_CHARWRAP: int
TE_WORDWRAP: int
TE_BESTWRAP: int
TE_CENTRE: int
TE_RIGHT: int
TE_READONLY: int
TE_PASSWORD: int
TE_PROCESS_ENTER: int
TE_RICH2: int
TE_MULTILINE: int
TE_MULTILINE: int
TE_MULTILINE: int


class CloseEvent(Event):
    """ This event class contains information about window and session close
events.
    """
    def __init__(self, commandEventType=wxEVT_NULL, id=0) -> None:
        """ Constructor.
        """

    def CanVeto(self) -> bool:
        """ Returns True if you can veto a system shutdown or a window close event.
        """

    def GetLoggingOff(self) -> bool:
        """ Returns True if the user is just logging off or False if the system is shutting down.
        """

    def GetVeto(self) -> bool:
        """ Returns whether the Veto flag was set.
        """

    def SetCanVeto(self, canVeto: bool) -> None:
        """ Sets the âcan vetoâ flag.
        """

    def SetLoggingOff(self, loggingOff: bool) -> None:
        """ Sets the âlogging offâ flag.
        """

    def Veto(self, veto: bool=True) -> None:
        """ Call this from your event handler to veto a system shutdown or to signal to the calling application that a window close did not happen.
        """

EVT_CLOSE: int  #  Process a  wxEVT_CLOSE_WINDOW   command event, supplying the member function. This event applies to    wx.Frame  and   wx.Dialog  classes.
EVT_QUERY_END_SESSION: int  #  Process a  wxEVT_QUERY_END_SESSION   session event, supplying the member function. This event can be handled in App-derived class only.
EVT_END_SESSION: int  #  Process a  wxEVT_END_SESSION   session event, supplying the member function. This event can be handled in App-derived class only. ^^


class CollapsibleHeaderCtrl(Control):
    """ Header control above a collapsible pane.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, label="", pos=DefaultPosition, size=DefaultSize, style=BORDER_NONE, validator=DefaultValidator, name=CollapsibleHeaderCtrlNameStr) -> bool:
        """ Create the control initialized using the default constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def IsCollapsed(self) -> bool:
        """ Returns  true   if the control is collapsed.
        """

    def SetCollapsed(self, collapsed: bool=True) -> None:
        """ Set collapsed state of the header.
        """

EVT_COLLAPSIBLEHEADER_CHANGED: int  #  User changed the collapsed state. ^^


class CollapsiblePane(Control):
    """ A collapsible pane is a container with an embedded button-like control
which can be used by the user to collapse or expand the paneâs
contents.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Collapse(self, collapse: bool=True) -> None:
        """ Collapses or expands the pane window.
        """

    def Create(self, parent, id=ID_ANY, label="", pos=DefaultPosition, size=DefaultSize, style=CP_DEFAULT_STYLE, validator=DefaultValidator, name=CollapsiblePaneNameStr) -> bool:
        """ parent (wx.Window) â Parent window, must not be not None.
        """

    def Expand(self) -> None:
        """ Same as calling Collapse(false).
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetPane(self) -> 'Window':
        """ Returns a pointer to the pane window.
        """

    def IsCollapsed(self) -> bool:
        """ Returns True if the pane window is currently hidden.
        """

    def IsExpanded(self) -> bool:
        """ Returns True if the pane window is currently shown.
        """

CP_DEFAULT_STYLE: int  #  The default style. It includes wx.TAB_TRAVERSAL and wx.BORDER_NONE.
CP_NO_TLW_RESIZE: int  #  By default   wx.CollapsiblePane  resizes the top level window containing it when its own size changes. This allows easily implementing dialogs containing an optionally shown part, for example, and so is the default behaviour but can be inconvenient in some specific cases â
EVT_COLLAPSIBLEPANE_CHANGED: int  #  The user expanded or collapsed the collapsible pane.
EVT_NAVIGATION_KEY: int  #  Process a navigation key event. ^^
CP_DEFAULT_STYLE: int
TAB_TRAVERSAL: int
BORDER_NONE: int
CP_NO_TLW_RESIZE: int


class CollapsiblePaneEvent(CommandEvent):
    """ This event class is used for the events generated by
CollapsiblePane.
    """
    def __init__(self, generator, id, collapsed) -> None:
        """ The constructor is not normally used by the user code.
        """

    def GetCollapsed(self) -> bool:
        """ Returns True if the pane has been collapsed.
        """

    def SetCollapsed(self, collapsed: bool) -> None:
        """ Sets this as a collapsed pane event (if collapsed  is True) or as an expanded pane event (if collapsed  is False).
        """

EVT_COLLAPSIBLEPANE_CHANGED: int  #  The user expanded or collapsed the collapsible pane. ^^


class Colour(Object):
    """ A colour is an object representing a combination of Red, Green, and
Blue (RGB) intensity values and an Alpha value, and is used to
determine drawing colours.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Alpha(self) -> int:
        """ Returns the alpha value, on platforms where alpha is not yet supported, this always returns wx.ALPHA_OPAQUE.
        """

    @staticmethod
    def AlphaBlend(fg, bg, alpha) -> int:
        """ Blend colour, taking alpha into account.
        """

    def Blue(self) -> int:
        """ Returns the blue intensity.
        """

    def ChangeLightness(self, *args, **kw) -> 'Colour':
        """ Overloaded Implementations:
        """

    def Get(self, includeAlpha=True) -> tuple:
        """ Returns the RGB intensity values as a tuple, optionally the alpha value as well.
        """

    def GetAlpha(self) -> int:
        """ Returns the alpha value, on platforms where alpha is not yet supported, this always returns wx.ALPHA_OPAQUE.
        """

    def GetAsString(self, flags: int=C2S_NAME|C2S_CSS_SYNTAX) -> str:
        """ Converts this colour to a String       using the given flags.
        """

    def GetBlue(self) -> int:
        """ Returns the blue intensity as  int.
        """

    def GetGreen(self) -> int:
        """ Returns the green intensity as  int.
        """

    def GetIM(self) -> None:
        """ Returns an immutable representation of the wx.Colour object, based on namedtuple.
        """

    def GetLuminance(self) -> float:
        """ Return the perceived brightness of the colour.
        """

    def GetPixel(self) -> 'IntPtr':
        """ wx.IntPtr
        """

    def GetRGB(self) -> 'int':
        """ Gets the RGB or RGBA colour values as a single 32 bit value.
        """

    def GetRGBA(self) -> 'int':
        """ Gets the RGB or RGBA colour values as a single 32 bit value.
        """

    def GetRed(self) -> int:
        """ Returns the red intensity as  int.
        """

    def Green(self) -> int:
        """ Returns the green intensity.
        """

    def IsOk(self) -> bool:
        """ Returns True if the colour object is valid (the colour has been initialised with RGB values).
        """

    def IsSolid(self) -> bool:
        """ Returns True if the color can be described using RGB values, i.e.
        """

    def MakeDisabled(self, *args, **kw) -> 'Colour':
        """ Overloaded Implementations:
        """

    @staticmethod
    def MakeGrey(*args, **kw) -> tuple:
        """ Overloaded Implementations:
        """

    @staticmethod
    def MakeMono(on: bool) -> tuple:
        """ Assigns the same value to r, g, b:  0 if on  is  false , 255 otherwise.
        """

    def Red(self) -> int:
        """ Returns the red intensity.
        """

    def Set(self, *args, **kw) -> None:
        """ Sets the RGB intensity values using the given values (first overload), extracting them from the packed long (second overload), using the given string (third overload).
        """

    def SetRGB(self, colRGB: 'int') -> None:
        """ Sets the RGB or RGBA colour values from a single 32 bit value.
        """

    def SetRGBA(self, colRGBA: 'int') -> None:
        """ Sets the RGB or RGBA colour values from a single 32 bit value.
        """

    def __bool__(self) -> int:
        """ int
        """

    def __getitem__(self, idx) -> None:
        """ 
        """

    def __len__(self) -> None:
        """ 
        """

    def __nonzero__(self) -> int:
        """ int
        """

    def __reduce__(self) -> None:
        """ 
        """

    def __repr__(self) -> None:
        """ 
        """

    def __setitem__(self, idx, val) -> None:
        """ 
        """

    def __str__(self) -> None:
        """ 
        """

    def _copyFrom(self, other) -> None:
        """ For internal use only.
        """

    def __ne__(self, item: Any) -> bool:
        """ Tests the inequality of two colours by comparing individual red, green, blue intensities and alpha values.
        """

    def __eq__(self, item: Any) -> bool:
        """ Tests the equality of two colours by comparing individual red, green, blue intensities and alpha values.
        """

ALPHA_OPAQUE: int
ALPHA_OPAQUE: int
Colour: int
ALPHA_OPAQUE: int
ALPHA_OPAQUE: int
Colour: int
Colour: int


class ColourData(Object):
    """ This class holds a variety of information related to colour dialogs.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def FromString(self, str: str) -> bool:
        """ Decodes the given string, which should be in the same format returned by wx.ToString     , and sets the internal colours.
        """

    def GetChooseAlpha(self) -> bool:
        """ Indicates whether the colour dialog will display alpha values and an opacity selector.
        """

    def GetChooseFull(self) -> bool:
        """ Under Windows, determines whether the Windows colour dialog will display the full dialog with custom colour selection controls.
        """

    def GetColour(self) -> 'Colour':
        """ Gets the current colour associated with the colour dialog.
        """

    def GetCustomColour(self, i: int) -> 'Colour':
        """ Returns custom colours associated with the colour dialog.
        """

    def SetChooseAlpha(self, flag: bool) -> None:
        """ Tells the colour dialog to show alpha values and an opacity selector (slider).
        """

    def SetChooseFull(self, flag: bool) -> None:
        """ Under Windows, tells the Windows colour dialog to display the full dialog with custom colour selection controls.
        """

    def SetColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the default colour for the colour dialog.
        """

    def SetCustomColour(self, i, colour) -> None:
        """ Sets custom colours for the colour dialog.
        """

    def ToString(self) -> str:
        """ Converts the colours saved in this class in a string form, separating the various colours with a comma.
        """



class ColourDatabase:
    """ wxWidgets maintains a database of standard RGB colours for a
predefined set of named colours.
    """
    def __init__(self) -> None:
        """ Constructs the colour database.
        """

    def AddColour(self, colourName, colour) -> None:
        """ Adds a colour to the database.
        """

    def Find(self, colourName: str) -> 'Colour':
        """ Finds a colour given the name.
        """

    def FindColour(self, colour) -> None:
        """ 
        """

    def FindName(self, colour: Union[int, str, 'Colour']) -> str:
        """ Finds a colour name given the colour.
        """



class ColourDialog(Dialog):
    """ This class represents the colour chooser dialog.
    """
    def __init__(self, parent, data=None) -> None:
        """ Constructor.
        """

    def Create(self, parent, data=None) -> bool:
        """ Same as   wx.ColourDialog.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetColourData(self) -> 'ColourData':
        """ Returns the colour data associated with the colour dialog.
        """

    def ShowModal(self) -> int:
        """ Shows the dialog, returning wx.ID_OK if the user pressed wx.OK, and wx.ID_CANCEL otherwise.
        """

ID_OK: int
OK: int
ID_CANCEL: int
ID_OK: int
OK: int
ID_CANCEL: int


class ColourDialogEvent(CommandEvent):
    """ This event class is used for the events generated by ColourDialog.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetColour(self) -> 'Colour':
        """ Retrieve the colour the user has just selected.
        """

    def SetColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Set the colour to be sent with the event.
        """

EVT_COLOUR_CHANGED: int  #  Generated whenever the currently selected colour in the dialog changes. This event is currently only implemented in wxMSW. ^^


class ColourPickerCtrl(PickerBase):
    """ This control allows the user to select a colour.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, colour=BLACK, pos=DefaultPosition, size=DefaultSize, style=CLRP_DEFAULT_STYLE, validator=DefaultValidator, name=ColourPickerCtrlNameStr) -> bool:
        """ Creates a colour picker with the given arguments.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetColour(self) -> 'Colour':
        """ Returns the currently selected colour.
        """

    def SetColour(self, *args, **kw) -> None:
        """ Sets the currently selected colour.
        """

CLRP_DEFAULT_STYLE: int  #  The default style: int  #  0.
CLRP_USE_TEXTCTRL: int  #  Creates a text control to the left of the picker button which is completely managed by the   wx.ColourPickerCtrl  and which can be used by the user to specify a colour (see SetColour). The text control is automatically synchronized with buttonâs value. Use functions defined in   wx.PickerBase  to modify the text control.
CLRP_SHOW_LABEL: int  #  Shows the colour in HTML form (AABBCC) as colour button label (instead of no label at all).
CLRP_SHOW_ALPHA: int  #  Allows selecting opacity in the colour-chooser (effective under wxGTK and wxOSX). ^^
EVT_COLOURPICKER_CHANGED: int  #  The user changed the colour selected in the control either using the button or using text control (see  CLRP_USE_TEXTCTRL ; note that in this case the event is fired only if the userâs input is valid, i.e. recognizable). When using a popup dialog for changing the colour, this event is sent only when the changes in the dialog are accepted by the user, unlike   EVT_COLOURPICKER_CURRENT_CHANGED .
EVT_COLOURPICKER_CURRENT_CHANGED: int  #  The user changed the currently selected colour in the dialog associated with the control. This event is sent immediately when the selection changes and you must also handle  EVT_COLOUR_CANCELLED   to revert to the previously selected colour if the selection ends up not being accepted. This event is new since wxWidgets 3.1.3 and currently is only implemented in wxMSW.
EVT_COLOURPICKER_DIALOG_CANCELLED: int  #  The user cancelled the colour dialog associated with the control, i.e. closed it without accepting the selection. This event is new since wxWidgets 3.1.3 and currently is only implemented in wxMSW. ^^
CLRP_DEFAULT_STYLE: int
CLRP_USE_TEXTCTRL: int
CLRP_SHOW_LABEL: int
CLRP_SHOW_ALPHA: int


class ColourPickerEvent(CommandEvent):
    """ This event class is used for the events generated by
ColourPickerCtrl.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetColour(self) -> 'Colour':
        """ Retrieve the colour the user has just selected.
        """

    def SetColour(self, pos: Union[int, str, 'Colour']) -> None:
        """ Set the colour associated with the event.
        """

EVT_COLOURPICKER_CHANGED: int  #  Generated whenever the selected colour changes.
EVT_COLOURPICKER_CURRENT_CHANGED: int  #  Generated whenever the currently selected colour in the dialog shown by the picker changes. This event is new since wxWidgets 3.1.3 and currently is only implemented in wxMSW.
EVT_COLOURPICKER_DIALOG_CANCELLED: int  #  Generated when the user cancels the colour dialog associated with the control, i.e. closes it without accepting the selection. This event is new since wxWidgets 3.1.3 and currently is only implemented in wxMSW. ^^


class ComboBox(Control, ItemContainer, TextEntry):
    """ A combobox is like a combination of an edit control and a listbox.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, value="", pos=DefaultPosition, size=DefaultSize, choices=[], style=0, validator=DefaultValidator, name=ComboBoxNameStr) -> bool:
        """ Creates the combobox for two-step construction.
        """

    def Dismiss(self) -> None:
        """ Hides the list box portion of the combo box.
        """

    def FindString(self, string, caseSensitive=False) -> int:
        """ Finds an item whose label matches the given string.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetCount(self) -> int:
        """ Returns the number of items in the control.
        """

    def GetCurrentSelection(self) -> int:
        """ Returns the item being selected right now.
        """

    def GetInsertionPoint(self) -> int:
        """ Same as wx.TextEntry.GetInsertionPoint .
        """

    def GetSelection(self) -> int:
        """ Returns the index of the selected item or  NOT_FOUND   if no item is selected.
        """

    def GetTextSelection(self) -> tuple:
        """ Gets the current selection span.
        """

    def GetString(self, n: int) -> str:
        """ Returns the label of the item with the given index.
        """

    def GetStringSelection(self) -> str:
        """ Gets the text currently selected in the control.
        """

    def IsListEmpty(self) -> bool:
        """ Returns True if the list of combobox choices is empty.
        """

    def IsTextEmpty(self) -> bool:
        """ Returns True if the text of the combobox is empty.
        """

    def Popup(self) -> None:
        """ Shows the list box portion of the combo box.
        """

    def SetSelection(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetString(self, n, text) -> None:
        """ Changes the text of the specified combobox item.
        """

    def SetTextSelection(self, from_, to_) -> None:
        """ Same as wx.TextEntry.SetSelection .
        """

    def SetValue(self, text: str) -> None:
        """ Sets the text for the combobox text field.
        """

CB_SIMPLE: int  #  Creates a combobox with a permanently displayed list. Windows only.
CB_DROPDOWN: int  #  Creates a combobox with a drop-down list. MSW and Motif only.
CB_READONLY: int  #  A combobox with this style behaves like a   wx.Choice  (and may look in the same way as well, although this is platform-dependent), i.e. it allows the user to choose from the list of options but doesnât allow to enter a value not present in the list.
CB_SORT: int  #  Sorts the entries in the list alphabetically.
TE_PROCESS_ENTER: int  #  The control will generate the event  wxEVT_TEXT_ENTER   that can be handled by the program. Otherwise, i.e. either if this style not specified at all, or it is used, but there is no event handler for this event or the event handler called  wx.Event.Skip   to avoid overriding the default handling, pressing Enter key is either processed internally by the control or used to activate the default button of the dialog, if any. ^^
EVT_COMBOBOX: int  #  Process a  wxEVT_COMBOBOX   event, when an item on the list is selected. Note that calling  GetValue  returns the new value of selection.
EVT_TEXT: int  #  Process a  wxEVT_TEXT   event, when the combobox text changes.
EVT_TEXT_ENTER: int  #  Process a  wxEVT_TEXT_ENTER   event, when RETURN is pressed in the combobox (notice that the combobox must have been created with wx.TE_PROCESS_ENTER style to receive this event).
EVT_COMBOBOX_DROPDOWN: int  #  Process a  wxEVT_COMBOBOX_DROPDOWN   event, which is generated when the list box part of the combo box is shown (drops down). Notice that this event is only supported by wxMSW, wxGTK with GTK+ 2.10 or later, and OSX/Cocoa.
EVT_COMBOBOX_CLOSEUP: int  #  Process a  wxEVT_COMBOBOX_CLOSEUP   event, which is generated when the list box of the combo box disappears (closes up). This event is only generated for the same platforms as   wxEVT_COMBOBOX_DROPDOWN   above. ^^
CB_READONLY: int
CB_SIMPLE: int
CB_DROPDOWN: int
CB_READONLY: int
CB_SORT: int
TE_PROCESS_ENTER: int
TE_PROCESS_ENTER: int
ID_ANY: int
NOT_FOUND: int


class ComboCtrl(Control, TextEntry):
    """ A combo control is a generic combobox that allows totally custom
popup.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AnimateShow(self, rect, flags) -> bool:
        """ This member function is not normally called in application code.
        """

    def Copy(self) -> None:
        """ Copies the selected text to the clipboard.
        """

    def Create(self, parent, id=ID_ANY, value="", pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=ComboBoxNameStr) -> bool:
        """ Creates the combo control for two-step construction.
        """

    def Cut(self) -> None:
        """ Copies the selected text to the clipboard and removes the selection.
        """

    def Dismiss(self) -> None:
        """ Dismisses the popup window.
        """

    def DoSetPopupControl(self, popup: 'ComboPopup') -> None:
        """ This member function is not normally called in application code.
        """

    def DoShowPopup(self, rect, flags) -> None:
        """ This member function is not normally called in application code.
        """

    def EnablePopupAnimation(self, enable: bool=True) -> None:
        """ Enables or disables popup animation, if any, depending on the value of the argument.
        """

    def GetBitmapDisabled(self) -> 'Bitmap':
        """ Returns disabled button bitmap that has been set with SetButtonBitmaps .
        """

    def GetBitmapHover(self) -> 'Bitmap':
        """ Returns button mouse hover bitmap that has been set with SetButtonBitmaps .
        """

    def GetBitmapNormal(self) -> 'Bitmap':
        """ Returns default button bitmap that has been set with SetButtonBitmaps .
        """

    def GetBitmapPressed(self) -> 'Bitmap':
        """ Returns depressed button bitmap that has been set with SetButtonBitmaps .
        """

    def GetButtonSize(self) -> 'Size':
        """ Returns current size of the dropdown button.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetCustomPaintWidth(self) -> int:
        """ Returns custom painted area in control.
        """

    @staticmethod
    def GetFeatures() -> int:
        """ Returns features supported by   wx.ComboCtrl.
        """

    def GetHint(self) -> str:
        """ Returns the current hint string.
        """

    def GetInsertionPoint(self) -> int:
        """ Returns the insertion point for the combo controlâs text field.
        """

    def GetLastPosition(self) -> int:
        """ Returns the last position in the combo control text field.
        """

    def GetMargins(self) -> 'Point':
        """ Returns the margins used by the control.
        """

    def GetPopupControl(self) -> 'ComboPopup':
        """ Returns current popup interface that has been set with SetPopupControl .
        """

    def GetPopupWindow(self) -> 'Window':
        """ Returns popup window containing the popup control.
        """

    def GetTextCtrl(self) -> 'TextCtrl':
        """ Get the text control which is part of the combo control.
        """

    def GetTextRect(self) -> 'Rect':
        """ Returns area covered by the text field (includes everything except borders and the dropdown button).
        """

    def GetValue(self) -> str:
        """ Returns text representation of the current value.
        """

    def HidePopup(self, generateEvent: bool=False) -> None:
        """ Dismisses the popup window.
        """

    def IsKeyPopupToggle(self, event: 'KeyEvent') -> bool:
        """ Returns True if given key combination should toggle the popup.
        """

    def IsPopupShown(self) -> bool:
        """ Returns True if the popup is currently shown.
        """

    def IsPopupWindowState(self, state: int) -> bool:
        """ Returns True if the popup window is in the given state.
        """

    def OnButtonClick(self) -> None:
        """ Implement in a derived class to define what happens on dropdown button click.
        """

    def Paste(self) -> None:
        """ Pastes text from the clipboard to the text field.
        """

    def Popup(self) -> None:
        """ Shows the popup portion of the combo control.
        """

    def PrepareBackground(self, dc, rect, flags) -> None:
        """ Prepare background of combo control or an item in a dropdown list in a way typical on platform.
        """

    def Remove(self, frm, to) -> None:
        """ Removes the text between the two positions in the combo control text field.
        """

    def Replace(self, frm, to, text) -> None:
        """ Replaces the text between two positions with the given text, in the combo control text field.
        """

CB_READONLY: int  #  Text will not be editable.
CB_SORT: int  #  Sorts the entries in the list alphabetically.
TE_PROCESS_ENTER: int  #  The control will generate the event  wxEVT_TEXT_ENTER   (otherwise pressing Enter key is either processed internally by the control or used for navigation between dialog controls). Windows only.
CC_SPECIAL_DCLICK: int  #  Double-clicking triggers a call to popupâs OnComboDoubleClick. Actual behaviour is defined by a derived class. For instance,   wx.adv.OwnerDrawnComboBox  will cycle an item. This style only applies if wx.CB_READONLY is used as well.
CC_STD_BUTTON: int  #  Drop button will behave more like a standard push button. ^^
EVT_TEXT: int  #  Process a  wxEVT_TEXT   event, when the text changes.
EVT_TEXT_ENTER: int  #  Process a  wxEVT_TEXT_ENTER   event, when RETURN is pressed in the combo control.
EVT_COMBOBOX_DROPDOWN: int  #  Process a  wxEVT_COMBOBOX_DROPDOWN   event, which is generated when the popup window is shown (drops down).
EVT_COMBOBOX_CLOSEUP: int  #  Process a  wxEVT_COMBOBOX_CLOSEUP   event, which is generated when the popup window of the combo control disappears (closes up). You should avoid adding or deleting items in this event. ^^
CB_READONLY: int
CB_SORT: int
TE_PROCESS_ENTER: int
CC_SPECIAL_DCLICK: int
CB_READONLY: int
CC_STD_BUTTON: int
ID_ANY: int
CONTROL_ISSUBMENU: int
CONTROL_SELECTED: int
CONTROL_DISABLED: int
LEFT: int
RIGHT: int


class ComboCtrlFeatures:
    """ Features enabled for ComboCtrl.
    """


class ComboPopup:
    """ In order to use a custom popup with ComboCtrl, an interface class
must be derived from ComboPopup.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def Create(self, parent: 'Window') -> bool:
        """ The derived class must implement this to create the popup control.
        """

    def DestroyPopup(self) -> None:
        """ You only need to implement this member function if you create your popup class in non-standard way.
        """

    def Dismiss(self) -> None:
        """ Utility function that hides the popup.
        """

    def FindItem(self, item, trueItem=None) -> bool:
        """ Implement to customize matching of value string to an item container entry.
        """

    def GetAdjustedSize(self, minWidth, prefHeight, maxHeight) -> 'Size':
        """ The derived class may implement this to return adjusted size for the popup control, according to the variables given.
        """

    def GetComboCtrl(self) -> 'ComboCtrl':
        """ Returns pointer to the associated parent   wx.ComboCtrl.
        """

    def GetControl(self) -> 'Window':
        """ The derived class must implement this to return pointer to the associated control created in Create .
        """

    def GetStringValue(self) -> str:
        """ The derived class must implement this to return string representation of the value.
        """

    def Init(self) -> None:
        """ The derived class must implement this to initialize its internal variables.
        """

    def IsCreated(self) -> bool:
        """ Utility method that returns True if Create has been called.
        """

    def LazyCreate(self) -> bool:
        """ The derived class may implement this to return True if it wants to delay call to Create   until the popup is shown for the first time.
        """

    def OnComboDoubleClick(self) -> None:
        """ The derived class may implement this to do something when the parent   wx.ComboCtrl  gets double-clicked.
        """

    def OnComboKeyEvent(self, event: 'KeyEvent') -> None:
        """ The derived class may implement this to receive key events from the parent   wx.ComboCtrl.
        """

    def OnDismiss(self) -> None:
        """ The derived class may implement this to do special processing when popup is hidden.
        """

    def OnPopup(self) -> None:
        """ The derived class may implement this to do special processing when popup is shown.
        """

    def PaintComboControl(self, dc, rect) -> None:
        """ The derived class may implement this to paint the parent   wx.ComboCtrl.
        """

    def SetStringValue(self, value: str) -> None:
        """ The derived class must implement this to receive string value changes from   wx.ComboCtrl.
        """



class Command(Object):
    """ Command is a base class for modelling an application command, which
is an action usually performed by selecting a menu item, pressing a
toolbar button or any other means provided by the application to
change the data or view.
    """
    def __init__(self, canUndo=False, name="") -> None:
        """ Constructor.
        """

    def CanUndo(self) -> bool:
        """ Returns True if the command can be undone, False otherwise.
        """

    def Do(self) -> bool:
        """ Override this member function to execute the appropriate action when called.
        """

    def GetName(self) -> str:
        """ Returns the command name.
        """

    def Undo(self) -> bool:
        """ Override this member function to un-execute a previous Do.
        """



class CommandEvent(Event):
    """ This event class contains information about command events, which
originate from a variety of simple controls.
    """
    def __init__(self, commandEventType=wxEVT_NULL, id=0) -> None:
        """ Constructor.
        """

    def GetClientData(self) -> ClientData:
        """ Returns client object pointer for a listbox or choice selection event (not valid for a deselection).
        """

    def GetClientObject(self) -> Any:
        """ Alias for GetClientData
        """

    def GetExtraLong(self) -> int:
        """ Returns extra information dependent on the event objects type.
        """

    def GetInt(self) -> int:
        """ Returns the integer identifier corresponding to a listbox, choice or radiobox selection (only if the event was a selection, not a deselection), or a boolean value representing the value of a checkbox.
        """

    def GetSelection(self) -> int:
        """ Returns item index for a listbox or choice selection event (not valid for a deselection).
        """

    def GetString(self) -> str:
        """ Returns item string for a listbox or choice selection event.
        """

    def IsChecked(self) -> bool:
        """ This method can be used with checkbox and menu events: for the checkboxes, the method returns True for a selection event and False for a deselection one.
        """

    def IsSelection(self) -> bool:
        """ For a listbox or similar event, returns True if it is a selection, False if it is a deselection.
        """

    def SetClientData(self, data: ClientData) -> None:
        """ Sets the client object for this event.
        """

    def SetClientObject(self, data) -> Any:
        """ Alias for SetClientData
        """

    def SetExtraLong(self, extraLong: int) -> None:
        """ Sets the m_extraLong  member.
        """

    def SetInt(self, intCommand: int) -> None:
        """ Sets the m_commandInt  member.
        """

    def SetString(self, string: str) -> None:
        """ Sets the m_commandString  member.
        """

EVT_COMMAND: int  #  Process a command, supplying the window identifier, command event identifier, and member function.
EVT_COMMAND_RANGE: int  #  Process a command for a range of window identifiers, supplying the minimum and maximum window identifiers, command event identifier, and member function.
EVT_BUTTON: int  #  Process a  wxEVT_BUTTON   command, which is generated by a    wx.Button  control.
EVT_CHECKBOX: int  #  Process a  wxEVT_CHECKBOX   command, which is generated by a    wx.CheckBox  control.
EVT_CHOICE: int  #  Process a  wxEVT_CHOICE   command, which is generated by a    wx.Choice  control.
EVT_COMBOBOX: int  #  Process a  wxEVT_COMBOBOX   command, which is generated by a    wx.ComboBox  control.
EVT_LISTBOX: int  #  Process a  wxEVT_LISTBOX   command, which is generated by a    wx.ListBox  control.
EVT_LISTBOX_DCLICK: int  #  Process a  wxEVT_LISTBOX_DCLICK   command, which is generated by a    wx.ListBox  control.
EVT_CHECKLISTBOX: int  #  Process a  wxEVT_CHECKLISTBOX   command, which is generated by a    wx.CheckListBox  control.
EVT_MENU: int  #  Process a  wxEVT_MENU   command, which is generated by a menu item.
EVT_MENU_RANGE: int  #  Process a  wxEVT_MENU   command, which is generated by a range of menu items.
EVT_CONTEXT_MENU: int  #  Process the event generated when the user has requested a popup menu to appear by pressing a special keyboard key (under Windows) or by right clicking the mouse.
EVT_RADIOBOX: int  #  Process a  wxEVT_RADIOBOX   command, which is generated by a    wx.RadioBox  control.
EVT_RADIOBUTTON: int  #  Process a  wxEVT_RADIOBUTTON   command, which is generated by a    wx.RadioButton  control.
EVT_SCROLLBAR: int  #  Process a  wxEVT_SCROLLBAR   command, which is generated by a    wx.ScrollBar  control. This is provided for compatibility only; more specific scrollbar event macros should be used instead (see   wx.ScrollEvent).
EVT_SLIDER: int  #  Process a  wxEVT_SLIDER   command, which is generated by a    wx.Slider  control.
EVT_TEXT: int  #  Process a  wxEVT_TEXT   command, which is generated by a    wx.TextCtrl  control.
EVT_TEXT_ENTER: int  #  Process a  wxEVT_TEXT_ENTER   command, which is generated by a    wx.TextCtrl  control. Note that you must use wx.TE_PROCESS_ENTER flag when creating the control if you want it to generate such events.
EVT_TEXT_MAXLEN: int  #  Process a  wxEVT_TEXT_MAXLEN   command, which is generated by a    wx.TextCtrl  control when the user tries to enter more characters into it than the limit previously set with SetMaxLength().
EVT_TOGGLEBUTTON: int  #  Process a  wxEVT_TOGGLEBUTTON   event.
EVT_TOOL: int  #  Process a  wxEVT_TOOL   event (a synonym for   wxEVT_MENU ). Pass the id of the tool.
EVT_TOOL_RANGE: int  #  Process a  wxEVT_TOOL   event for a range of identifiers. Pass the ids of the tools.
EVT_TOOL_RCLICKED: int  #  Process a  wxEVT_TOOL_RCLICKED   event. Pass the id of the tool. (Not available on wxOSX.)
EVT_TOOL_RCLICKED_RANGE: int  #  Process a  wxEVT_TOOL_RCLICKED   event for a range of ids. Pass the ids of the tools. (Not available on wxOSX.)
EVT_TOOL_ENTER: int  #  Process a  wxEVT_TOOL_ENTER   event. Pass the id of the toolbar itself. The value of  wx.CommandEvent.GetSelection   is the tool id, or -1 if the mouse cursor has moved off a tool. (Not available on wxOSX.)
EVT_COMMAND_LEFT_CLICK: int  #  Process a  wxEVT_COMMAND_LEFT_CLICK   command, which is generated by a control (wxMSW only).
EVT_COMMAND_LEFT_DCLICK: int  #  Process a  wxEVT_COMMAND_LEFT_DCLICK   command, which is generated by a control (wxMSW only).
EVT_COMMAND_RIGHT_CLICK: int  #  Process a  wxEVT_COMMAND_RIGHT_CLICK   command, which is generated by a control (wxMSW only).
EVT_COMMAND_SET_FOCUS: int  #  Process a  wxEVT_COMMAND_SET_FOCUS   command, which is generated by a control (wxMSW only).
EVT_COMMAND_KILL_FOCUS: int  #  Process a  wxEVT_COMMAND_KILL_FOCUS   command, which is generated by a control (wxMSW only).
EVT_COMMAND_ENTER: int  #  Process a  wxEVT_COMMAND_ENTER   command, which is generated by a control. ^^
TE_PROCESS_ENTER: int


class CommandProcessor(Object):
    """ CommandProcessor is a class that maintains a history of Commands,
with undo/redo functionality built-in.
    """
    def __init__(self, maxCommands: int=-1) -> None:
        """ Constructor.
        """

    def CanRedo(self) -> bool:
        """ Returns True if the currently-active command can be redone, False otherwise.
        """

    def CanUndo(self) -> bool:
        """ Returns True if the currently-active command can be undone, False otherwise.
        """

    def ClearCommands(self) -> None:
        """ Deletes all commands in the list and sets the current command pointer to None.
        """

    def GetCommands(self) -> CommandList:
        """ Returns the list of commands.
        """

    def GetCurrentCommand(self) -> 'Command':
        """ Returns the current command.
        """

    def GetEditMenu(self) -> 'Menu':
        """ Returns the edit menu associated with the command processor.
        """

    def GetMaxCommands(self) -> int:
        """ Returns the maximum number of commands that the command processor stores.
        """

    def GetRedoAccelerator(self) -> str:
        """ Returns the string that will be appended to the Redo menu item.
        """

    def GetRedoMenuLabel(self) -> str:
        """ Returns the string that will be shown for the redo menu item.
        """

    def GetUndoAccelerator(self) -> str:
        """ Returns the string that will be appended to the Undo menu item.
        """

    def GetUndoMenuLabel(self) -> str:
        """ Returns the string that will be shown for the undo menu item.
        """

    def Initialize(self) -> None:
        """ Initializes the command processor, setting the current command to the last in the list (if any), and updating the edit menu (if one has been specified).
        """

    def IsDirty(self) -> bool:
        """ Returns a boolean value that indicates if changes have been made since the last save operation.
        """

    def MarkAsSaved(self) -> None:
        """ You must call this method whenever the project is saved if you plan to use IsDirty .
        """

    def Redo(self) -> bool:
        """ Executes (redoes) the current command (the command that has just been undone if any).
        """

    def SetEditMenu(self, menu: 'Menu') -> None:
        """ Tells the command processor to update the Undo and Redo items on this menu as appropriate.
        """

    def SetMenuStrings(self) -> None:
        """ Sets the menu labels according to the currently set menu and the current command state.
        """

    def SetRedoAccelerator(self, accel: str) -> None:
        """ Sets the string that will be appended to the Redo menu item.
        """

    def SetUndoAccelerator(self, accel: str) -> None:
        """ Sets the string that will be appended to the Undo menu item.
        """

    def Store(self, command: 'Command') -> None:
        """ Just store the command without executing it.
        """

    def Submit(self, command, storeIt=True) -> bool:
        """ Submits a new command to the command processor.
        """

    def Undo(self) -> bool:
        """ Undoes the last command executed.
        """



class ConfigBase(Object):
    """ ConfigBase defines the basic interface of all config classes.
    """
    def __init__(self, appName="", vendorName="", localFilename="", globalFilename="", style=0) -> None:
        """ This is the default and only constructor of the   wx.ConfigBase  class, and derived classes.
        """

    @staticmethod
    def Create() -> 'ConfigBase':
        """ Create a new config object and sets it as the current one.
        """

    def DeleteAll(self) -> bool:
        """ Delete the whole underlying object (disk file, registry key, â¦).
        """

    def DeleteEntry(self, key, bDeleteGroupIfEmpty=True) -> bool:
        """ Deletes the specified entry and the group it belongs to if it was the last key in it and the second parameter is True.
        """

    def DeleteGroup(self, key: str) -> bool:
        """ Delete the group (with all subgroups).
        """

    @staticmethod
    def DontCreateOnDemand() -> None:
        """ Calling this function will prevent  ` Get  `   from automatically creating a new config object if the current one is None.
        """

    def Exists(self, strName: str) -> bool:
        """ strName (string) â
        """

    def Flush(self, bCurrentOnly: bool=False) -> bool:
        """ Permanently writes all changes (otherwise, theyâre only written from objectâs destructor).
        """

    @staticmethod
    def Get(CreateOnDemand: bool=True) -> 'ConfigBase':
        """ Get the current config object.
        """

    def GetAppName(self) -> str:
        """ Returns the application name.
        """

    def GetEntryType(self, name: str) -> 'ConfigBase.EntryType':
        """ Returns the type of the given entry or Unknown  if the entry doesnât exist.
        """

    def GetFirstEntry(self) -> Any:
        """ GetFirstEntry() . (more, value, index)
        """

    def GetFirstGroup(self) -> Any:
        """ GetFirstGroup() . (more, value, index)
        """

    def GetNextEntry(self, index) -> Any:
        """ GetNextEntry() . (more, value, index)
        """

    def GetNextGroup(self, index) -> Any:
        """ GetNextGroup(long index) . (more, value, index)
        """

    def GetNumberOfEntries(self, bRecursive: bool=False) -> int:
        """ Get number of entries in the current group.
        """

    def GetNumberOfGroups(self, bRecursive: bool=False) -> int:
        """ Get number of entries/subgroups in the current group, with or without its subgroups.
        """

    def GetPath(self) -> str:
        """ Retrieve the current path (always as absolute path).
        """

    def GetVendorName(self) -> str:
        """ Returns the vendor name.
        """

    def HasEntry(self, strName: str) -> bool:
        """ strName (string) â
        """

    def HasGroup(self, strName: str) -> bool:
        """ strName (string) â
        """

    def IsExpandingEnvVars(self) -> bool:
        """ Returns True if we are expanding environment variables in key values.
        """

    def IsRecordingDefaults(self) -> bool:
        """ Returns True if we are writing defaults back to the config file.
        """

    def Read(self, key, defaultVal="") -> None:
        """ Another version of Read , returning the string value directly.
        """

    def ReadBool(self, key, defaultVal=False) -> bool:
        """ bool
        """

    def ReadDouble(self, key, defaultVal) -> float:
        """ Reads a float value from the key and returns it.
        """

    def ReadFloat(self, key, defaultVal=0.0) -> float:
        """ float
        """

    def ReadInt(self, key, defaultVal=0) -> None:
        """ 
        """

    def ReadLong(self, key, defaultVal) -> int:
        """ Reads a long value from the key and returns it.
        """

    def ReadLongLong(self, key, defaultVal) -> LongLong_t:
        """ Reads a 64-bit long long value from the key and returns it.
        """

    def RenameEntry(self, oldName, newName) -> bool:
        """ Renames an entry in the current group.
        """

    def RenameGroup(self, oldName, newName) -> bool:
        """ Renames a subgroup of the current group.
        """

    @staticmethod
    def Set(pConfig: 'ConfigBase') -> 'ConfigBase':
        """ Sets the config object as the current one, returns the pointer to the previous current object (both the parameter and returned value may be None).
        """

    def SetExpandEnvVars(self, bDoIt: bool=True) -> None:
        """ Determine whether we wish to expand environment variables in key values.
        """

    def SetPath(self, strPath: str) -> None:
        """ Set current path: if the first character is â/â, it is the absolute path, otherwise it is a relative path.
        """

    def SetRecordDefaults(self, bDoIt: bool=True) -> None:
        """ Sets whether defaults are recorded to the config file whenever an attempt to read the value which is not present in it is done.
        """

    def Write(self, key, value) -> bool:
        """ Writes the String       value to the config file and returns True on success.
        """

    def WriteBool(self, key, value) -> bool:
        """ bool
        """

    def WriteFloat(self, key, value) -> bool:
        """ bool
        """

    def WriteInt(self, key, value) -> bool:
        """ bool
        """

    def _cpp_ReadInt(self, key, defaultVal=0) -> int:
        """ long
        """



class ConfigPathChanger:
    """ A handy little class which changes the current path in a Config
object and restores it in dtor.
    """
    def __init__(self, pContainer, strEntry) -> None:
        """ Changes the path of the given   wx.ConfigBase  object so that the key strEntry  is accessible (for read or write).
        """

    def Name(self) -> str:
        """ Returns the name of the key which was passed to the constructor.
        """

    def UpdateIfDeleted(self) -> None:
        """ This method must be called if the original path inside the Config object (i.e.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class ContextHelp(Object):
    """ This class changes the cursor to a query and puts the application into
a âcontext-sensitive help modeâ.
    """
    def __init__(self, window=None, doNow=True) -> None:
        """ Constructs a context help object, calling BeginContextHelp   if doNow  is True (the default).
        """

    def BeginContextHelp(self, window: 'Window') -> bool:
        """ Puts the application into context-sensitive help mode.
        """

    def EndContextHelp(self) -> bool:
        """ Ends context-sensitive help mode.
        """

DIALOG_EX_CONTEXTHELP: int
DIALOG_EX_CONTEXTHELP: int


class ContextHelpButton(BitmapButton):
    """ Instances of this class may be used to add a question mark button that
when pressed, puts the application into context-help mode.
    """
    def __init__(self, parent, id=ID_CONTEXT_HELP, pos=DefaultPosition, size=DefaultSize, style=0) -> None:
        """ Constructor, creating and showing a context help button.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

DIALOG_EX_CONTEXTHELP: int
OK: int
ID_CONTEXT_HELP: int


class ContextMenuEvent(CommandEvent):
    """ This class is used for context menu events, sent to give the
application a chance to show a context (popup) menu for a Window.
    """
    def __init__(self, type=wxEVT_NULL, id=0, pos=DefaultPosition) -> None:
        """ Constructor.
        """

    def GetPosition(self) -> 'Point':
        """ Returns the position in screen coordinates at which the menu should be shown.
        """

    def SetPosition(self, point: 'Point') -> None:
        """ Sets the position at which the menu should be shown.
        """

EVT_CONTEXT_MENU: int  #  A right click (or other context menu command depending on platform) has been detected. ^^


class Window(EvtHandler):
    """ Window is the base class for all windows and represents any visible
object on screen.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AcceptsFocus(self) -> bool:
        """ This method may be overridden in the derived classes to return False to indicate that this control doesnât accept input at all (i.e. behaves like e.g.   wx.StaticText) and so doesnât need focus.
        """

    def AcceptsFocusFromKeyboard(self) -> bool:
        """ This method may be overridden in the derived classes to return False to indicate that while this control can, in principle, have focus if the user clicks it with the mouse, it shouldnât be included in the TAB traversal chain when using the keyboard.
        """

    def AcceptsFocusRecursively(self) -> bool:
        """ Overridden to indicate whether this window or one of its children accepts focus.
        """

    def AddChild(self, child: 'WindowBase') -> None:
        """ Adds a child window.
        """

    def AdjustForLayoutDirection(self, x, width, widthTotal) -> 'Coord':
        """ Mirror coordinates for RTL layout if this window uses it and if the mirroring is not done automatically like Win32.
        """

    def AlwaysShowScrollbars(self, hflag=True, vflag=True) -> None:
        """ Call this function to force one or both scrollbars to be always shown, even if the window is big enough to show its entire contents without scrolling.
        """

    def AssociateHandle(self, handle) -> None:
        """ Associate the window with a new native handle
        """

    def BeginRepositioningChildren(self) -> bool:
        """ Prepare for changing positions of multiple child windows.
        """

    def CacheBestSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the cached best size value.
        """

    def CanAcceptFocus(self) -> bool:
        """ Can this window have focus right now?
        """

    def CanAcceptFocusFromKeyboard(self) -> bool:
        """ Can this window be assigned focus from keyboard right now?
        """

    def CanScroll(self, orient: int) -> bool:
        """ Returns True if this window can have a scroll bar in this orientation.
        """

    def CanSetTransparent(self) -> bool:
        """ Returns True if the system supports transparent windows and calling SetTransparent   may succeed.
        """

    def CaptureMouse(self) -> None:
        """ Directs all mouse input to this window.
        """

    def Center(self, dir: int=BOTH) -> None:
        """ A synonym for wx.Centre     .
        """

    def CenterOnParent(self, dir: int=BOTH) -> None:
        """ A synonym for CentreOnParent .
        """

    def Centre(self, direction: int=BOTH) -> None:
        """ Centres the window.
        """

    def CentreOnParent(self, direction: int=BOTH) -> None:
        """ Centres the window on its parent.
        """

    def ClearBackground(self) -> None:
        """ Clears the window by filling it with the current background colour.
        """

    def ClientToScreen(self, *args, **kw) -> tuple:
        """ Overloaded Implementations:
        """

    def ClientToWindowSize(self, size: Union[tuple[int, int], 'Size']) -> 'Size':
        """ Converts client area size size  to corresponding window size.
        """

    def Close(self, force: bool=False) -> bool:
        """ This function simply generates a   wx.CloseEvent  whose handler usually tries to close the window.
        """

    def ConvertDialogToPixels(self, *args, **kw) -> 'Point':
        """ Overloaded Implementations:
        """

    def ConvertPixelsToDialog(self, *args, **kw) -> 'Point':
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=PanelNameStr) -> bool:
        """ Construct the actual window object after creating the C++ object.
        """

    def DLG_UNIT(self, dlg_unit) -> None:
        """ A convenience wrapper for ConvertDialogToPixels.
        """

    def Destroy(self) -> bool:
        """ Destroys the window safely.
        """

    def DestroyChildren(self) -> bool:
        """ Destroys all children of a window.
        """

    def DestroyLater(self) -> None:
        """ Schedules the window to be destroyed in the near future.
        """

    def Disable(self) -> bool:
        """ Disables the window.
        """

    def DisableFocusFromKeyboard(self) -> None:
        """ Disable giving focus to this window using the keyboard navigation keys.
        """

    def DissociateHandle(self) -> None:
        """ Dissociate the current native handle from the window
        """

    def DoGetBestClientSize(self) -> 'Size':
        """ Override this method to return the best size for a custom control.
        """

    def DoGetBestSize(self) -> 'Size':
        """ Implementation of GetBestSize   that can be overridden.
        """

    def DoUpdateWindowUI(self, event: 'UpdateUIEvent') -> None:
        """ Does the window-specific updating after processing the update event.
        """

    def DragAcceptFiles(self, accept: bool) -> None:
        """ Enables or disables eligibility for drop file events (OnDropFiles).
        """

    def Enable(self, enable: bool=True) -> bool:
        """ Enable or disable the window for user input.
        """

    def EnableTouchEvents(self, eventsMask: int) -> bool:
        """ Request generation of touch events for this window.
        """

    def EnableVisibleFocus(self, enable: bool) -> None:
        """ Enables or disables visible indication of keyboard focus.
        """

    def EndRepositioningChildren(self) -> None:
        """ Fix child window positions after setting all of them at once.
        """

    @staticmethod
    def FindFocus() -> 'Window':
        """ Finds the window or control which currently has the keyboard focus.
        """

    def FindWindow(self, *args, **kw) -> 'Window':
        """ Overloaded Implementations:
        """

    @staticmethod
    def FindWindowById(id, parent=None) -> 'Window':
        """ Find the first window with the given id.
        """

    @staticmethod
    def FindWindowByLabel(label, parent=None) -> 'Window':
        """ Find a window by its label.
        """

    @staticmethod
    def FindWindowByName(name, parent=None) -> 'Window':
        """ Find a window by its name (as given in a window constructor or Create   function call).
        """

    def Fit(self) -> None:
        """ Sizes the window to fit its best size.
        """

    def FitInside(self) -> None:
        """ Similar to Fit , but sizes the interior (virtual) size of a window.
        """

    def Freeze(self) -> None:
        """ Freezes the window or, in other words, prevents any updates from taking place on screen, the window is not redrawn at all.
        """

    def FromDIP(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:
        """

    def FromPhys(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:
        """

    def GetAcceleratorTable(self) -> 'AcceleratorTable':
        """ Gets the accelerator table for this window.
        """

    def GetAccessible(self) -> 'Accessible':
        """ Returns the accessible object for this window, if any.
        """

    def GetAutoLayout(self) -> bool:
        """ Returns True if Layout   is called automatically when the window is resized.
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ Returns the background colour of the window.
        """

    def GetBackgroundStyle(self) -> 'BackgroundStyle':
        """ Returns the background style of the window.
        """

    def GetBestHeight(self, width: int) -> int:
        """ Returns the best height needed by this window if it had the given width.
        """

    def GetBestSize(self) -> 'Size':
        """ This functions returns the best acceptable minimal size for the window.
        """

    def GetBestVirtualSize(self) -> 'Size':
        """ Return the largest of ClientSize and BestSize (as determined by a sizer, interior children, or other means)
        """

    def GetBestWidth(self, height: int) -> int:
        """ Returns the best width needed by this window if it had the given height.
        """

    def GetBorder(self, *args, **kw) -> 'Border':
        """ Overloaded Implementations:
        """

    @staticmethod
    def GetCapture() -> 'Window':
        """ Returns the currently captured window.
        """

    def GetCaret(self) -> 'Caret':
        """ Returns the caret() associated with the window.
        """

    def GetCharHeight(self) -> int:
        """ Returns the character height for this window.
        """

    def GetCharWidth(self) -> int:
        """ Returns the average character width for this window.
        """

    def GetChildren(self) -> WindowList:
        """ Returns a reference to the list of the windowâs children.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ Returns the default font and colours which are used by the control.
        """

    def GetClientAreaOrigin(self) -> 'Point':
        """ Get the origin of the client area of the window relative to the window top left corner (the client area may be shifted because of the borders, scrollbars, other decorationsâ¦)
        """

    def GetClientRect(self) -> 'Rect':
        """ Get the client rectangle in window (i.e. client) coordinates.
        """

    def GetClientSize(self) -> None:
        """ Returns the size of the window âclient areaâ in pixels.
        """

    def GetConstraints(self) -> 'LayoutConstraints':
        """ Returns a pointer to the windowâs layout constraints, or None if there are none.
        """

    def GetContainingSizer(self) -> 'Sizer':
        """ Returns the sizer of which this window is a member, if any, otherwise None.
        """

    def GetContentScaleFactor(self) -> float:
        """ Returns the factor mapping logical pixels of this window to physical pixels.
        """

    def GetCursor(self) -> 'Cursor':
        """ Return the cursor associated with this window.
        """

    def GetDPI(self) -> 'Size':
        """ Return the DPI of the display used by this window.
        """

    def GetDPIScaleFactor(self) -> float:
        """ Returns the ratio of the DPI used by this window to the standard DPI.
        """

    def GetDefaultAttributes(self) -> 'VisualAttributes':
        """ Currently this is the same as calling Window.GetClassDefaultAttributes(wxWindow.GetWindowVariant()).
        """

    def GetDropTarget(self) -> 'DropTarget':
        """ Returns the associated drop target, which may be None.
        """

    def GetEffectiveMinSize(self) -> 'Size':
        """ Merges the windowâs best size into the min size and returns the result.
        """

    def GetEventHandler(self) -> 'EvtHandler':
        """ Returns the event handler for this window.
        """

    def GetExtraStyle(self) -> int:
        """ Returns the extra style bits for the window.
        """

    def GetFont(self) -> 'Font':
        """ Returns the font for this window.
        """

    def GetForegroundColour(self) -> 'Colour':
        """ Returns the foreground colour of the window.
        """

    def GetGrandParent(self) -> 'Window':
        """ Returns the grandparent of a window, or None if there isnât one.
        """

    def GetGtkWidget(self) -> None:
        """ 
        """

    def GetHandle(self) -> None:
        """ Returns the platform-specific handle of the physical window.
        """

    def GetHelpText(self) -> str:
        """ Gets the help text to be used as context-sensitive help for this window.
        """

    def GetHelpTextAtPoint(self, point, origin) -> str:
        """ Gets the help text to be used as context-sensitive help for this window.
        """

    def GetId(self) -> int:
        """ Returns the identifier of the window.
        """

    def GetLabel(self) -> str:
        """ Generic way of getting a label from any window, for identification purposes.
        """

    def GetLayoutDirection(self) -> int:
        """ Returns the layout direction for this window, Note that  Layout_Default   is returned if layout direction is not supported.
        """

    def GetMaxClientSize(self) -> 'Size':
        """ Returns the maximum size of windowâs client area.
        """

    def GetMaxHeight(self) -> int:
        """ Returns the vertical component of window maximal size.
        """

    def GetMaxSize(self) -> 'Size':
        """ Returns the maximum size of the window.
        """

    def GetMaxWidth(self) -> int:
        """ Returns the horizontal component of window maximal size.
        """

    def GetMinClientSize(self) -> 'Size':
        """ Returns the minimum size of windowâs client area, an indication to the sizer layout mechanism that this is the minimum required size of its client area.
        """

    def GetMinHeight(self) -> int:
        """ Returns the vertical component of window minimal size.
        """

    def GetMinSize(self) -> 'Size':
        """ Returns the minimum size of the window, an indication to the sizer layout mechanism that this is the minimum required size.
        """

    def GetMinWidth(self) -> int:
        """ Returns the horizontal component of window minimal size.
        """

    def GetName(self) -> str:
        """ Returns the windowâs name.
        """

    def GetNextSibling(self) -> 'Window':
        """ Returns the next window after this one among the parentâs children or None if this window is the last child.
        """

    def GetParent(self) -> 'Window':
        """ Returns the parent of the window, or None if there is no parent.
        """

    def GetPopupMenuSelectionFromUser(self, *args, **kw) -> int:
        """ Overloaded Implementations:
        """

    def GetPosition(self) -> 'Point':
        """ This gets the position of the window in pixels, relative to the parent window for the child windows or relative to the display origin for the top level windows.
        """

    def GetPrevSibling(self) -> 'Window':
        """ Returns the previous window before this one among the parentâs children or
        """

    def GetRect(self) -> 'Rect':
        """ Returns the position and size of the window as a   wx.Rect  object.
        """

    def GetScreenPosition(self) -> 'Point':
        """ Returns the window position in screen coordinates, whether the window is a child window or a top level one.
        """

    def GetScreenRect(self) -> 'Rect':
        """ Returns the position and size of the window on the screen as a   wx.Rect  object.
        """

    def GetScrollPos(self, orientation: int) -> int:
        """ Returns the built-in scrollbar position.
        """

    def GetScrollRange(self, orientation: int) -> int:
        """ Returns the built-in scrollbar range.
        """

    def GetScrollThumb(self, orientation: int) -> int:
        """ Returns the built-in scrollbar thumb size.
        """

    def GetSize(self) -> 'Size':
        """ Returns the size of the entire window in pixels, including title bar, border, scrollbars, etc.
        """

    def GetSizer(self) -> 'Sizer':
        """ Returns the sizer associated with the window by a previous call to SetSizer , or None.
        """

    def GetFullTextExtent(self, string, font=None) -> tuple:
        """ Gets the dimensions of the string as it would be drawn on the window with the currently selected font.
        """

    def GetTextExtent(self, string: str) -> 'Size':
        """ Gets the dimensions of the string as it would be drawn on the window with the currently selected font.
        """

    def GetThemeEnabled(self) -> bool:
        """ Returns True if the window uses the system theme for drawing its background.
        """

    def GetToolTip(self) -> 'ToolTip':
        """ Get the associated tooltip or None if none.
        """

    def GetToolTipText(self) -> str:
        """ Get the text of the associated tooltip or empty string if none.
        """

    def GetTopLevelParent(self) -> 'Window':
        """ Returns the first ancestor of this window which is a top-level window.
        """

    def GetUpdateClientRect(self) -> 'Rect':
        """ Get the update rectangle bounding box in client coords.
        """

    def GetUpdateRegion(self) -> 'Region':
        """ Returns the region specifying which parts of the window have been damaged.
        """

    def GetValidator(self) -> 'Validator':
        """ Validator functions.
        """

    def GetVirtualSize(self) -> 'Size':
        """ This gets the virtual size of the window in pixels.
        """

    def GetWindowBorderSize(self) -> 'Size':
        """ Returns the size of the left/right and top/bottom borders of this window in x and y components of the result respectively.
        """

    def GetWindowStyle(self) -> int:
        """ See GetWindowStyleFlag   for more info.
        """

    def GetWindowStyleFlag(self) -> int:
        """ Gets the window style that was passed to the constructor or Create   method.
        """

    def GetWindowVariant(self) -> int:
        """ Returns the value previously passed to SetWindowVariant .
        """

    def HandleAsNavigationKey(self, event: 'KeyEvent') -> bool:
        """ This function will generate the appropriate call to Navigate   if the key event is one normally used for keyboard navigation and return True in this case.
        """

    def HandleWindowEvent(self, event: 'Event') -> bool:
        """ Shorthand for:
        """

    def HasCapture(self) -> bool:
        """ Returns True if this window has the current mouse capture.
        """

    def HasExtraStyle(self, exFlag: int) -> bool:
        """ Returns True if the window has the given exFlag  bit set in its extra styles.
        """

    def HasFlag(self, flag: int) -> bool:
        """ Returns True if the window has the given flag  bit set.
        """

    def HasFocus(self) -> bool:
        """ Returns True if the window (or in case of composite controls, its main child window) has focus.
        """

    def HasMultiplePages(self) -> bool:
        """ This method should be overridden to return True if this window has multiple pages.
        """

    def HasScrollbar(self, orient: int) -> bool:
        """ Returns True if this window currently has a scroll bar for this orientation.
        """

    def HasTransparentBackground(self) -> bool:
        """ Returns True if this window background is transparent (as, for example, for   wx.StaticText) and should show the parent window background.
        """

    def Hide(self) -> bool:
        """ Equivalent to calling wx.Window.Show (False).
        """

    def HideWithEffect(self, effect, timeout=0) -> bool:
        """ This function hides a window, like Hide , but using a special visual effect if possible.
        """

    def HitTest(self, *args, **kw) -> 'HitTest':
        """ Overloaded Implementations:
        """

    def InformFirstDirection(self, direction, size, availableOtherDir) -> bool:
        """ wx.Sizer  and friends use this to give a chance to a component to recalc its min size once one of the final size components is known.
        """

    def InheritAttributes(self) -> None:
        """ This function is (or should be, in case of custom controls) called during window creation to intelligently set up the window visual attributes, that is the font and the foreground and background colours.
        """

    def InheritsBackgroundColour(self) -> bool:
        """ Return True if this window inherits the background colour from its parent.
        """

    def InheritsForegroundColour(self) -> bool:
        """ Return True if this window inherits the foreground colour from its parent.
        """

    def InitDialog(self) -> None:
        """ Sends an  wxEVT_INIT_DIALOG   event, whose handler usually transfers data to the dialog via validators.
        """

    def InvalidateBestSize(self) -> None:
        """ Resets the cached best size value so it will be recalculated the next time it is needed.
        """

    def IsBeingDeleted(self) -> bool:
        """ Returns True if this window is in process of being destroyed.
        """

    def IsDescendant(self, win: 'Window') -> bool:
        """ Check if the specified window is a descendant of this one.
        """

    def IsDoubleBuffered(self) -> bool:
        """ Returns True if the window contents is double-buffered by the system, i.e. if any drawing done on the window is really done on a temporary backing surface and transferred to the screen all at once later.
        """

    def IsEnabled(self) -> bool:
        """ Returns True if the window is enabled, i.e. if it accepts user input, False otherwise.
        """

    def IsExposed(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def IsFocusable(self) -> bool:
        """ Can this window itself have focus?
        """

    def IsFrozen(self) -> bool:
        """ Returns True if the window is currently frozen by a call to Freeze .
        """

    def IsRetained(self) -> bool:
        """ Returns True if the window is retained, False otherwise.
        """

    def IsScrollbarAlwaysShown(self, orient: int) -> bool:
        """ Return whether a scrollbar is always shown.
        """

    def IsShown(self) -> bool:
        """ Returns True if the window is shown, False if it has been hidden.
        """

    def IsShownOnScreen(self) -> bool:
        """ Returns True if the window is physically visible on the screen, i.e. it is shown and all its parents up to the toplevel window are shown as well.
        """

    def IsThisEnabled(self) -> bool:
        """ Returns True if this window is intrinsically enabled, False otherwise, i.e. if Enable   Enable(false) had been called.
        """

    def IsTopLevel(self) -> bool:
        """ Returns True if the given window is a top-level one.
        """

    def IsTransparentBackgroundSupported(self, reason: Optional[str]=None) -> bool:
        """ Checks whether using transparent background might work.
        """

    def Layout(self) -> bool:
        """ Lays out the children of this window using the associated sizer.
        """

    def LineDown(self) -> bool:
        """ Same as ScrollLines   (1).
        """

    def LineUp(self) -> bool:
        """ Same as ScrollLines   (-1).
        """

    def Lower(self) -> None:
        """ Lowers the window to the bottom of the window hierarchy (Z-order).
        """

    def MacIsWindowScrollbar(self, sb) -> None:
        """ Is the given widget one of this windowâs built-in scrollbars?  Only applicable on Mac.
        """

    def Move(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def MoveAfterInTabOrder(self, win: 'Window') -> None:
        """ Moves this window in the tab navigation order after the specified win.
        """

    def MoveBeforeInTabOrder(self, win: 'Window') -> None:
        """ Same as MoveAfterInTabOrder   except that it inserts this window just before win  instead of putting it right after it.
        """

    def Navigate(self, flags: int=NavigationKeyEvent.IsForward) -> bool:
        """ Performs a keyboard navigation action starting from this window.
        """

    def NavigateIn(self, flags: int=NavigationKeyEvent.IsForward) -> bool:
        """ Performs a keyboard navigation action inside this window.
        """

    @staticmethod
    def NewControlId(count: int=1) -> int:
        """ Create a new ID or range of IDs that are not currently in use.
        """

    def OnInternalIdle(self) -> None:
        """ This virtual function is normally only used internally, but sometimes an application may need it to implement functionality that should not be disabled by an application defining an OnIdle handler in a derived class.
        """

    def PageDown(self) -> bool:
        """ Same as ScrollPages   (1).
        """

    def PageUp(self) -> bool:
        """ Same as ScrollPages   (-1).
        """

    def PopEventHandler(self, deleteHandler: bool=False) -> 'EvtHandler':
        """ Removes and returns the top-most event handler on the event handler stack.
        """

    def PopupMenu(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def PostSizeEvent(self) -> None:
        """ Posts a size event to the window.
        """

    def PostSizeEventToParent(self) -> None:
        """ Posts a size event to the parent of this window.
        """

    def ProcessEvent(self, event: 'Event') -> bool:
        """ This function is public in   wx.EvtHandler  but protected in   wx.Window  because for Windows you should always call   wx.ProcessEvent  on the pointer returned by GetEventHandler   and not on the   wx.Window  object itself.
        """

    def ProcessWindowEvent(self, event: 'Event') -> bool:
        """ Convenient wrapper for   wx.ProcessEvent.
        """

    def ProcessWindowEventLocally(self, event: 'Event') -> bool:
        """ Wrapper for wx.EvtHandler.ProcessEventLocally .
        """

    def PushEventHandler(self, handler: 'EvtHandler') -> None:
        """ Pushes this event handler onto the event stack for the window.
        """

    def Raise(self) -> None:
        """ Raises the window to the top of the window hierarchy (Z-order).
        """

    def Refresh(self, eraseBackground=True, rect=None) -> None:
        """ Causes this window, and all of its children recursively, to be repainted.
        """

    def RefreshRect(self, rect, eraseBackground=True) -> None:
        """ Redraws the contents of the given rectangle: only the area inside it will be repainted.
        """

    def RegisterHotKey(self, hotkeyId, modifiers, virtualKeyCode) -> bool:
        """ Registers a system wide hotkey.
        """

    def ReleaseMouse(self) -> None:
        """ Releases mouse input captured with CaptureMouse .
        """

    def RemoveChild(self, child: 'WindowBase') -> None:
        """ Removes a child window.
        """

    def RemoveEventHandler(self, handler: 'EvtHandler') -> bool:
        """ Find the given handler  in the windows event handler stack and removes (but does not delete) it from the stack.
        """

    def Reparent(self, newParent: 'Window') -> bool:
        """ Reparents the window, i.e. the window will be removed from its current parent window (e.g.
        """

    def ScreenToClient(self, *args, **kw) -> tuple:
        """ Overloaded Implementations:
        """

    def ScrollLines(self, lines: int) -> bool:
        """ Scrolls the window by the given number of lines down (if lines  is positive) or up.
        """

    def ScrollPages(self, pages: int) -> bool:
        """ Scrolls the window by the given number of pages down (if pages  is positive) or up.
        """

    def ScrollWindow(self, dx, dy, rect=None) -> None:
        """ Physically scrolls the pixels in the window and move child windows accordingly.
        """

    def SendDestroyEvent(self) -> None:
        """ Generate   wx.WindowDestroyEvent  for this window.
        """

    def SendIdleEvents(self, event: 'IdleEvent') -> bool:
        """ Send idle event to window and all subwindows.
        """

    def SendSizeEvent(self, flags: int=0) -> None:
        """ This function sends a dummy size event  to the window allowing it to re-layout its children positions.
        """

    def SendSizeEventToParent(self, flags: int=0) -> None:
        """ Safe wrapper for GetParent . SendSizeEvent .
        """

    def SetAcceleratorTable(self, accel: 'AcceleratorTable') -> None:
        """ Sets the accelerator table for this window.
        """

    def SetAccessible(self, accessible: 'Accessible') -> None:
        """ Sets the accessible for this window.
        """

    def SetAutoLayout(self, autoLayout: bool) -> None:
        """ Determines whether the Layout   function will be called automatically when the window is resized.
        """

    def SetBackgroundColour(self, colour: Union[int, str, 'Colour']) -> bool:
        """ Sets the background colour of the window.
        """

    def SetBackgroundStyle(self, style: BackgroundStyle) -> bool:
        """ Sets the background style of the window.
        """

    def SetCanFocus(self, canFocus: bool) -> None:
        """ This method is only implemented by ports which have support for native TAB traversal (such as GTK+ 2.0).
        """

    def SetCaret(self, caret: 'Caret') -> None:
        """ Sets the caret() associated with the window.
        """

    def SetClientRect(self, rect) -> None:
        """ 
        """

    def SetClientSize(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetConstraints(self, constraints: 'LayoutConstraints') -> None:
        """ Sets the window to have the given layout constraints.
        """

    def SetContainingSizer(self, sizer: 'Sizer') -> None:
        """ Used by   wx.Sizer  internally to notify the window about being managed by the given sizer.
        """

    def SetCursor(self, cursor: 'Cursor') -> bool:
        """ Sets the windowâs cursor.
        """

    def SetDimensions(self, x, y, width, height, sizeFlags=SIZE_AUTO) -> None:
        """ 
        """

    def SetDoubleBuffered(self, on: bool) -> None:
        """ Turn on or off double buffering of the window if the system supports it.
        """

    def SetDropTarget(self, target: 'DropTarget') -> None:
        """ Associates a drop target with this window.
        """

    def SetEventHandler(self, handler: 'EvtHandler') -> None:
        """ Sets the event handler for this window.
        """

    def SetExtraStyle(self, exStyle: int) -> None:
        """ Sets the extra style bits for the window.
        """

    def SetFocus(self) -> None:
        """ This sets the window to receive keyboard input.
        """

    def SetFocusFromKbd(self) -> None:
        """ This function is called by wxWidgets keyboard navigation code when the user gives the focus to this window from keyboard (e.g. using  TAB   key).
        """

    def SetFont(self, font: 'Font') -> bool:
        """ Sets the font for this window.
        """

    def SetForegroundColour(self, colour: Union[int, str, 'Colour']) -> bool:
        """ Sets the foreground colour of the window.
        """

    def SetHelpText(self, helpText: str) -> None:
        """ Sets the help text to be used as context-sensitive help for this window.
        """

    def SetId(self, winid: int) -> None:
        """ Sets the identifier of the window.
        """

    def SetInitialSize(self, size: Union[tuple[int, int], 'Size']=DefaultSize) -> None:
        """ A smart  SetSize that will fill in default size components with the windowâs best  size values.
        """

    def SetLabel(self, label: str) -> None:
        """ Sets the windowâs label.
        """

    def SetLayoutDirection(self, dir: int) -> None:
        """ Sets the layout direction for this window.
        """

    def SetMaxClientSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the maximum client size of the window, to indicate to the sizer layout mechanism that this is the maximum possible size of its client area.
        """

    def SetMaxSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the maximum size of the window, to indicate to the sizer layout mechanism that this is the maximum possible size.
        """

    def SetMinClientSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the minimum client size of the window, to indicate to the sizer layout mechanism that this is the minimum required size of windowâs client area.
        """

    def SetMinSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the minimum size of the window, to indicate to the sizer layout mechanism that this is the minimum required size.
        """

    def SetName(self, name: str) -> None:
        """ Sets the windowâs name.
        """

    def SetNextHandler(self, handler: 'EvtHandler') -> None:
        """ Windows cannot be used to form event handler chains; this function thus will assert when called.
        """

    def SetOwnBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the background colour of the window but prevents it from being inherited by the children of this window.
        """

    def SetOwnFont(self, font: 'Font') -> None:
        """ Sets the font of the window but prevents it from being inherited by the children of this window.
        """

    def SetOwnForegroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the foreground colour of the window but prevents it from being inherited by the children of this window.
        """

    def SetPalette(self, pal: 'Palette') -> None:
        """ pal (wx.Palette) â
        """

    def SetPosition(self, pt: 'Point') -> None:
        """ Moves the window to the specified position.
        """

    def SetPreviousHandler(self, handler: 'EvtHandler') -> None:
        """ Windows cannot be used to form event handler chains; this function thus will assert when called.
        """

    def SetRect(self, rect) -> None:
        """ 
        """

    def SetScrollPos(self, orientation, pos, refresh=True) -> None:
        """ Sets the position of one of the built-in scrollbars.
        """

    def SetScrollbar(self, orientation, position, thumbSize, range, refresh=True) -> None:
        """ Sets the scrollbar properties of a built-in scrollbar.
        """

    def SetSize(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetSizeHints(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetSizer(self, sizer, deleteOld=True) -> None:
        """ Sets the window to have the given layout sizer.
        """

    def SetSizerAndFit(self, sizer, deleteOld=True) -> None:
        """ Associate the sizer with the window and set the window size and minimal size accordingly.
        """

    def SetThemeEnabled(self, enable: bool) -> None:
        """ This function tells a window if it should use the systemâs âthemeâ code to draw the windowsâ background instead of its own background drawing code.
        """

    def SetToolTip(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetTransparent(self, alpha: 'Byte') -> bool:
        """ Set the transparency of the window.
        """

    def SetValidator(self, validator: 'Validator') -> None:
        """ Deletes the current validator (if any) and sets the window validator, having called wx.Validator.Clone   to create a new validator of this type.
        """

    def SetVirtualSize(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetWindowStyle(self, style: int) -> None:
        """ See SetWindowStyleFlag   for more info.
        """

    def SetWindowStyleFlag(self, style: int) -> None:
        """ Sets the style of the window.
        """

    def SetWindowVariant(self, variant: int) -> None:
        """ Chooses a different variant of the window display to use.
        """

    def ShouldInheritColours(self) -> bool:
        """ Return True from here to allow the colours of this window to be changed by InheritAttributes .
        """

    def Show(self, show: bool=True) -> bool:
        """ Shows or hides the window.
        """

    def ShowWithEffect(self, effect, timeout=0) -> bool:
        """ This function shows a window, like Show , but using a special visual effect if possible.
        """

    def Thaw(self) -> None:
        """ Re-enables window updating after a previous call to Freeze .
        """

    def ToDIP(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:
        """

    def ToPhys(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:
        """

    def ToggleWindowStyle(self, flag: int) -> bool:
        """ Turns the given flag  on if itâs currently turned off and vice versa.
        """

    def TransferDataFromWindow(self) -> bool:
        """ Transfers values from child controls to data areas specified by their validators.
        """

    def TransferDataToWindow(self) -> bool:
        """ Transfers values to child controls from data areas specified by their validators.
        """

    def UnregisterHotKey(self, hotkeyId: int) -> bool:
        """ Unregisters a system wide hotkey.
        """

    @staticmethod
    def UnreserveControlId(id, count=1) -> None:
        """ Unreserve an ID or range of IDs that was reserved by NewControlId .
        """

    def UnsetToolTip(self) -> None:
        """ Unset any existing tooltip.
        """

    def Update(self) -> None:
        """ Calling this method immediately repaints the invalidated area of the window and all of its children recursively (this normally only happens when the flow of control returns to the event loop).
        """

    def UpdateWindowUI(self, flags: int=UPDATE_UI_NONE) -> None:
        """ This function sends one or more   wx.UpdateUIEvent  to the window.
        """

    def UseBackgroundColour(self) -> bool:
        """ Return True if a background colour has been set for this window.
        """

    def UseBgCol(self) -> bool:
        """ Return True if a background colour has been set for this window.
        """

    def UseForegroundColour(self) -> bool:
        """ Return True if a foreground colour has been set for this window.
        """

    def Validate(self) -> bool:
        """ Validates the current values of the child controls using their validators.
        """

    def WarpPointer(self, x, y) -> None:
        """ Moves the pointer to the given position on the window.
        """

    def WindowToClientSize(self, size: Union[tuple[int, int], 'Size']) -> 'Size':
        """ Converts window size size  to corresponding client area size In other words, the returned value is what would GetClientSize   return if this window had given window size.
        """

    def __nonzero__(self) -> None:
        """ Can be used to test if the C++ part of the window still exists, with
code like this:
        """

BORDER_DEFAULT: int  #  The window class will decide the kind of border to show, if any.
BORDER_SIMPLE: int  #  Displays a thin border around the window. wx.SIMPLE_BORDER is the old name for this style.
BORDER_SUNKEN: int  #  Displays a sunken border. wx.SUNKEN_BORDER is the old name for this style.
BORDER_RAISED: int  #  Displays a raised border. wx.RAISED_BORDER is the old name for this style.
BORDER_STATIC: int  #  Displays a border suitable for a static control. wx.STATIC_BORDER is the old name for this style. Windows only.
BORDER_THEME: int  #  Displays a native border suitable for a control, on the current platform. On Windows, this will be a themed border; on most other platforms a sunken border will be used. For more information for themed borders on Windows, please see Themed borders on Windows.
BORDER_NONE: int  #  Displays no border, overriding the default border style for the window. wx.NO_BORDER is the old name for this style.
BORDER_DOUBLE: int  #  This style is obsolete and should not be used.
TRANSPARENT_WINDOW: int  #  The window is transparent, that is, it will not receive paint events. Windows only.
TAB_TRAVERSAL: int  #  This style is used by wxWidgets for the windows supporting TAB navigation among their children, such as   wx.Dialog  and   wx.Panel. It should almost never be used in the application code.
WANTS_CHARS: int  #  Use this to indicate that the window wants to get all char/key events for all keys - even for keys like TAB or ENTER which are usually used for dialog navigation and which wouldnât be generated without this style. If you need to use this style in order to get the arrows or etc., but would still like to have normal keyboard navigation take place, you should call Navigate in response to the key events for Tab and Shift-Tab.
NO_FULL_REPAINT_ON_RESIZE: int  #  On Windows, this style used to disable repainting the window completely when its size is changed. Since this behaviour is now the default, the style is now obsolete and no longer has an effect.
VSCROLL: int  #  Use this style to enable a vertical scrollbar. Notice that this style cannot be used with native controls which donât support scrollbars nor with top-level windows in most ports.
HSCROLL: int  #  Use this style to enable a horizontal scrollbar. The same limitations as for wx.VSCROLL apply to this style.
ALWAYS_SHOW_SB: int  #  If a window has scrollbars, disable them instead of hiding them when they are not needed (i.e. when the size of the window is big enough to not require the scrollbars to navigate it). This style is currently implemented for wxMSW, wxGTK and wxUniversal and does nothing on the other platforms.
CLIP_CHILDREN: int  #  Use this style to eliminate flicker caused by the background being repainted, then children being painted over them. Windows only.
FULL_REPAINT_ON_RESIZE: int  #  Use this style to force a complete redraw of the window whenever it is resized instead of redrawing just the part of the window affected by resizing. Note that this was the behaviour by default before 2.5.1 release and that if you experience redraw problems with code which previously used to work you may want to try this. Currently this style applies on GTK+ 2 and Windows only, and full repainting is always done on other platforms. ^^
EVT_ACTIVATE: int  #  Process a  wxEVT_ACTIVATE   event. See    wx.ActivateEvent.
EVT_CHILD_FOCUS: int  #  Process a  wxEVT_CHILD_FOCUS   event. See    wx.ChildFocusEvent.
EVT_CONTEXT_MENU: int  #  A right click (or other context menu command depending on platform) has been detected. See   wx.ContextMenuEvent.
EVT_HELP: int  #  Process a  wxEVT_HELP   event. See    wx.HelpEvent.
EVT_HELP_RANGE: int  #  Process a  wxEVT_HELP   event for a range of ids. See    wx.HelpEvent.
EVT_DROP_FILES: int  #  Process a  wxEVT_DROP_FILES   event. See    wx.DropFilesEvent.
EVT_ERASE_BACKGROUND: int  #  Process a  wxEVT_ERASE_BACKGROUND   event. See    wx.EraseEvent.
EVT_SET_FOCUS: int  #  Process a  wxEVT_SET_FOCUS   event. See    wx.FocusEvent.
EVT_KILL_FOCUS: int  #  Process a  wxEVT_KILL_FOCUS   event. See    wx.FocusEvent.
EVT_IDLE: int  #  Process a  wxEVT_IDLE   event. See    wx.IdleEvent.
EVT_KEY_DOWN: int  #  Process a  wxEVT_KEY_DOWN   event (any key has been pressed). See    wx.KeyEvent.
EVT_KEY_UP: int  #  Process a  wxEVT_KEY_UP   event (any key has been released). See    wx.KeyEvent.
EVT_CHAR: int  #  Process a  wxEVT_CHAR   event. See    wx.KeyEvent.
EVT_CHAR_HOOK: int  #  Process a  wxEVT_CHAR_HOOK   event. See    wx.KeyEvent.
EVT_MOUSE_CAPTURE_LOST: int  #  Process a  wxEVT_MOUSE_CAPTURE_LOST   event. See    wx.MouseCaptureLostEvent.
EVT_MOUSE_CAPTURE_CHANGED: int  #  Process a  wxEVT_MOUSE_CAPTURE_CHANGED   event. See    wx.MouseCaptureChangedEvent.
EVT_PAINT: int  #  Process a  wxEVT_PAINT   event. See    wx.PaintEvent.
EVT_SET_CURSOR: int  #  Process a  wxEVT_SET_CURSOR   event. See    wx.SetCursorEvent.
EVT_SIZE: int  #  Process a  wxEVT_SIZE   event. See    wx.SizeEvent.
EVT_SYS_COLOUR_CHANGED: int  #  Process a  wxEVT_SYS_COLOUR_CHANGED   event. See    wx.SysColourChangedEvent. ^^
BORDER_DEFAULT: int
BORDER_SIMPLE: int
SIMPLE_BORDER: int
BORDER_SUNKEN: int
SUNKEN_BORDER: int
BORDER_RAISED: int
RAISED_BORDER: int
BORDER_STATIC: int
STATIC_BORDER: int
BORDER_THEME: int
BORDER_NONE: int
NO_BORDER: int
BORDER_DOUBLE: int
TRANSPARENT_WINDOW: int
TAB_TRAVERSAL: int
WANTS_CHARS: int
NO_FULL_REPAINT_ON_RESIZE: int
VSCROLL: int
HSCROLL: int
VSCROLL: int
ALWAYS_SHOW_SB: int
CLIP_CHILDREN: int
FULL_REPAINT_ON_RESIZE: int
WS_EX_BLOCK_EVENTS: int
WS_EX_TRANSIENT: int
WS_EX_CONTEXTHELP: int
WS_EX_PROCESS_IDLE: int
WS_EX_PROCESS_UI_UPDATES: int
BORDER_MASK: int
BORDER_DEFAULT: int
ID_ANY: int
HORIZONTAL: int
VERTICAL: int
HORIZONTAL: int
VERTICAL: int
BOTH: int
HORIZONTAL: int
VERTICAL: int
BOTH: int
ID_CANCEL: int
TOUCH_NONE: int
TOUCH_ALL_GESTURES: int
BORDER_MASK: int
BORDER_DEFAULT: int
ID_ANY: int
HORIZONTAL: int
VERTICAL: int
HORIZONTAL: int
VERTICAL: int
TE_PROCESS_TAB: int
ID_NONE: int
MOD_SHIFT: int
MOD_CONTROL: int
MOD_ALT: int
MOD_WIN: int
HORIZONTAL: int
VERTICAL: int
HORIZONTAL: int
VERTICAL: int
UPDATE_UI_FROMIDLE: int


class Control(Window):
    """ This is the base class for a control or âwidgetâ.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Command(self, event: 'CommandEvent') -> None:
        """ Simulates the effect of the user issuing a command to the item.
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=ControlNameStr) -> bool:
        """ parent (wx.Window) â
        """

    @staticmethod
    def Ellipsize(label, dc, mode, maxWidth, flags=ELLIPSIZE_FLAGS_DEFAULT) -> str:
        """ Replaces parts of the label  string with ellipsis, if needed, so that it fits into maxWidth  pixels if possible.
        """

    @staticmethod
    def EscapeMnemonics(text: str) -> str:
        """ Escapes the special mnemonics characters (â&â) in the given string.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetLabel(self) -> str:
        """ Returns the controlâs label, as it was passed to SetLabel .
        """

    def GetLabelText(self, *args, **kw) -> str:
        """ Overloaded Implementations:
        """

    def GetSizeFromText(self, text: str) -> 'Size':
        """ Determine the minimum size needed by the control to display the given text.
        """

    def GetSizeFromTextSize(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:
        """

    @staticmethod
    def RemoveMnemonics(str: str) -> str:
        """ Returns the given str  string without mnemonics (â&â characters).
        """

    def SetLabel(self, label: str) -> None:
        """ Sets the controlâs label.
        """

    def SetLabelMarkup(self, markup: str) -> bool:
        """ Sets the controls label to a string using markup.
        """

    def SetLabelText(self, text: str) -> None:
        """ Sets the controlâs label to exactly the given string.
        """

EVT_TEXT_COPY: int  #  Some or all of the controls content was copied to the clipboard.
EVT_TEXT_CUT: int  #  Some or all of the controls content was cut (i.e. copied and deleted).
EVT_TEXT_PASTE: int  #  Clipboard content was pasted into the control. ^^
ID_ANY: int


class ControlWithItems(Control, ItemContainer):
    """ This is convenience class that derives from both Control and
ItemContainer.
    """


class ItemContainer(ItemContainerImmutable):
    """ This class is an abstract base class for some wxWidgets controls which
contain several items such as ListBox, CheckListBox, ComboBox or
Choice.
    """
    def Append(self, *args, **kw) -> int:
        """ Overloaded Implementations:
        """

    def AppendItems(self, items) -> Any:
        """ Alias for Append
        """

    def Clear(self) -> None:
        """ Removes all items from the control.
        """

    def Delete(self, n: int) -> None:
        """ Deletes an item from the control.
        """

    def DetachClientObject(self, n: int) -> ClientData:
        """ Returns the client object associated with the given item and transfers its ownership to the caller.
        """

    def GetClientData(self, n: int) -> ClientData:
        """ Returns a pointer to the client data associated with the given item (if any).
        """

    def GetClientObject(self, n) -> Any:
        """ Alias for GetClientData
        """

    def GetItems(self) -> Any:
        """ Alias for GetStrings
        """

    def HasClientData(self) -> bool:
        """ Returns True, if either untyped data ( void* ) or object data (wxClientData) is associated with the items of the control.
        """

    def HasClientObjectData(self) -> bool:
        """ Returns True, if object data is associated with the items of the control.
        """

    def HasClientUntypedData(self) -> bool:
        """ Returns True, if untyped data ( void* ) is associated with the items of the control.
        """

    def Insert(self, *args, **kw) -> int:
        """ Overloaded Implementations:
        """

    def Set(self, items: list[str]) -> None:
        """ Replaces the current control contents with the given items.
        """

    def SetClientData(self, n, data) -> None:
        """ Associates the given typed client data pointer with the given item: the data  object will be deleted when the item is deleted (either explicitly by using Delete   or implicitly when the control itself is destroyed).
        """

    def SetClientObject(self, n, data) -> Any:
        """ Alias for SetClientData
        """

    def SetItems(self, items) -> Any:
        """ Alias for Set
        """

OK: int


class Cursor(GDIObject):
    """ A cursor is a small bitmap usually used for denoting where the mouse
pointer is, with a picture that might indicate the interpretation of a
mouse click.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetHandle(self) -> int:
        """ Get the handle for the Cursor.  Windows only.
        """

    def GetHotSpot(self) -> 'Point':
        """ Returns the coordinates of the cursor hot spot.
        """

    def IsOk(self) -> bool:
        """ Returns True if cursor data is present.
        """

    def SetHandle(self, handle) -> None:
        """ Set the handle to use for this Cursor.  Windows only.
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """

    def _copyFrom(self, other) -> None:
        """ For internal use only.
        """



class CustomDataObject(DataObjectSimple):
    """ CustomDataObject is a specialization of DataObjectSimple for some
application-specific data in arbitrary (either custom or one of the
standard ones).
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetAllFormats(self, dir=DataObject.Get) -> None:
        """ Returns a list of wx.DataFormat objects which this data object
supports transferring in the given direction.
        """

    def GetData(self) -> Any:
        """ Returns a reference to the data buffer.
        """

    def GetSize(self) -> int:
        """ Returns the data size in bytes.
        """

    def SetData(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """



class DataObjectSimple(DataObject):
    """ This is the simplest possible implementation of the DataObject
class.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetAllFormats(self, dir=DataObject.Get) -> None:
        """ Returns a list of wx.DataFormat objects which this data object
supports transferring in the given direction.
        """

    def GetDataHere(self, buf) -> bool:
        """ Copies this data objectâs data bytes to the given buffer
        """

    def GetDataSize(self) -> int:
        """ Gets the size of our data.
        """

    def GetFormat(self) -> 'DataFormat':
        """ Returns the (one and only one) format supported by this object.
        """

    def SetData(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def SetFormat(self, format: 'DataFormat') -> None:
        """ Sets the supported format.
        """



class DataFormat:
    """ A DataFormat is an encapsulation of a platform-specific format
handle which is used by the system for the clipboard and drag and drop
operations.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetId(self) -> str:
        """ Returns the name of a custom format (this function will fail for a standard format).
        """

    def GetType(self) -> 'DataFormatId':
        """ Returns the platform-specific number identifying the format.
        """

    def SetId(self, format: str) -> None:
        """ Sets the format to be the custom format identified by the given name.
        """

    def SetType(self, type: DataFormatId) -> None:
        """ Sets the format to the given value, which should be one of DF_XXX constants.
        """

    def __ne__(self, item: Any) -> bool:
        """ Returns True if the formats are different.
        """

    def __eq__(self, item: Any) -> bool:
        """ Returns True if the formats are equal.
        """

DF_INVALID: int
DF_TEXT: int
DF_BITMAP: int
DF_METAFILE: int
DF_UNICODETEXT: int
DF_FILENAME: int
DF_HTML: int
DF_PNG: int


class DataObjectComposite(DataObject):
    """ DataObjectComposite is the simplest DataObject derivation which
may be used to support multiple formats.
    """
    def __init__(self) -> None:
        """ The default constructor.
        """

    def Add(self, dataObject, preferred=False) -> None:
        """ Adds the dataObject  to the list of supported objects and it becomes the preferred object if preferred  is True.
        """

    def GetAllFormats(self, dir=DataObject.Get) -> None:
        """ Returns a list of wx.DataFormat objects which this data object
supports transferring in the given direction.
        """

    def GetObject(self, format, dir=DataObject.Get) -> 'DataObjectSimple':
        """ Returns the pointer to the object which supports the passed format for the specified direction.
        """

    def GetReceivedFormat(self) -> 'DataFormat':
        """ Report the format passed to the SetData   method.
        """

    def SetData(self, format, buf) -> bool:
        """ bool
        """



class DateSpan:
    """ This class is a âlogical time spanâ and is useful for implementing
program logic for such things as âadd one month to the dateâ which, in
general, doesnât mean to add 60x60x24x31 seconds to it, but to take
the same date the next month (to understand that this is indeed
different consider adding one month to Feb, 15  we want to get Mar,
15, of course).
    """
    def __init__(self, years=0, months=0, weeks=0, days=0) -> None:
        """ Constructs the date span object for the given number of years, months, weeks and days.
        """

    def Add(self, other: 'DateSpan') -> 'DateSpan':
        """ Adds the given   wx.DateSpan  to this   wx.DateSpan  and returns a reference to itself.
        """

    @staticmethod
    def Day() -> 'DateSpan':
        """ Returns a date span object corresponding to one day.
        """

    @staticmethod
    def Days(days: int) -> 'DateSpan':
        """ Returns a date span object corresponding to the given number of days.
        """

    def GetDays(self) -> int:
        """ Returns the number of days (not counting the weeks component) in this date span.
        """

    def GetMonths(self) -> int:
        """ Returns the number of the months (not counting the years) in this date span.
        """

    def GetTotalDays(self) -> int:
        """ Returns the combined number of days in this date span, counting both weeks and days.
        """

    def GetTotalMonths(self) -> int:
        """ Returns the combined number of months in this date span, counting both years and months.
        """

    def GetWeeks(self) -> int:
        """ Returns the number of weeks in this date span.
        """

    def GetYears(self) -> int:
        """ Returns the number of years in this date span.
        """

    @staticmethod
    def Month() -> 'DateSpan':
        """ Returns a date span object corresponding to one month.
        """

    @staticmethod
    def Months(mon: int) -> 'DateSpan':
        """ Returns a date span object corresponding to the given number of months.
        """

    def Multiply(self, factor: int) -> 'DateSpan':
        """ Multiplies this date span by the specified factor.
        """

    def Neg(self) -> 'DateSpan':
        """ Changes the sign of this date span.
        """

    def Negate(self) -> 'DateSpan':
        """ Returns a date span with the opposite sign.
        """

    def SetDays(self, n: int) -> 'DateSpan':
        """ Sets the number of days (without modifying any other components) in this date span.
        """

    def SetMonths(self, n: int) -> 'DateSpan':
        """ Sets the number of months (without modifying any other components) in this date span.
        """

    def SetWeeks(self, n: int) -> 'DateSpan':
        """ Sets the number of weeks (without modifying any other components) in this date span.
        """

    def SetYears(self, n: int) -> 'DateSpan':
        """ Sets the number of years (without modifying any other components) in this date span.
        """

    def Subtract(self, other: 'DateSpan') -> 'DateSpan':
        """ Subtracts the given   wx.DateSpan  to this   wx.DateSpan  and returns a reference to itself.
        """

    @staticmethod
    def Week() -> 'DateSpan':
        """ Returns a date span object corresponding to one week.
        """

    @staticmethod
    def Weeks(weeks: int) -> 'DateSpan':
        """ Returns a date span object corresponding to the given number of weeks.
        """

    @staticmethod
    def Year() -> 'DateSpan':
        """ Returns a date span object corresponding to one year.
        """

    @staticmethod
    def Years(years: int) -> 'DateSpan':
        """ Returns a date span object corresponding to the given number of years.
        """



class DateTime:
    """ DateTime class represents an absolute moment in time.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Add(self, *args, **kw) -> 'DateTime':
        """ Overloaded Implementations:
        """

    @staticmethod
    def ConvertYearToBC(year: int) -> int:
        """ Converts the year in absolute notation (i.e. a number which can be negative, positive or zero) to the year in BC/AD notation.
        """

    def DiffAsDateSpan(self, dt: 'DateTime') -> 'DateSpan':
        """ Returns the difference between this object and dt  as a   wx.DateSpan.
        """

    def Format(self, format=DefaultDateTimeFormat, tz=Local) -> str:
        """ This function does the same as the standard ANSI C  strftime(3)   function (http://www.cplusplus.com/reference/clibrary/ctime/strftime.html).
        """

    def FormatDate(self) -> str:
        """ Identical to calling Format   with  "%x"   argument (which means âpreferred date representation for the current localeâ).
        """

    def FormatISOCombined(self, sep: int='T') -> str:
        """ Returns the combined date-time representation in the ISO 8601 format  "YYYY-MM-DDTHH:MM:SS" .
        """

    def FormatISODate(self) -> str:
        """ This function returns the date representation in the ISO 8601 format  "YYYY-MM-DD" .
        """

    def FormatISOTime(self) -> str:
        """ This function returns the time representation in the ISO 8601 format  "HH:MM:SS" .
        """

    def FormatTime(self) -> str:
        """ Identical to calling Format   with  "%X"   argument (which means âpreferred time representation for the current localeâ).
        """

    @staticmethod
    def FromDMY(day, month, year=Inv_Year, hour=0, minute=0, second=0, millisecond=0) -> 'DateTime':
        """ Construct a DateTime using the supplied parameters.
        """

    @staticmethod
    def FromHMS(hour, minute=0, second=0, millisecond=0) -> 'DateTime':
        """ Construct a DateTime equal to Today () with the time set to the supplied parameters.
        """

    @staticmethod
    def FromJDN(jdn) -> 'DateTime':
        """ Construct a DateTime from a Julian Day Number.
        """

    @staticmethod
    def FromTimeT(timet) -> 'DateTime':
        """ Construct a DateTime from a C time_t value, the number of seconds since the epoch.
        """

    def FromTimezone(self, tz, noDST=False) -> 'DateTime':
        """ Transform the date from the given time zone to the local one.
        """

    @staticmethod
    def GetAmPmStrings() -> tuple:
        """ Returns the translations of the strings  AM   and   PM   used for time formatting for the current locale.
        """

    def GetAsDOS(self) -> int:
        """ Returns the date and time in DOS format.
        """

    @staticmethod
    def GetBeginDST(year=Inv_Year, country=Country_Default) -> 'DateTime':
        """ Get the beginning of DST for the given country in the given year (current one by default).
        """

    def GetCentury(self, tz: 'DateTime.TimeZone'=Local) -> int:
        """ Returns the century of this date.
        """

    @staticmethod
    def GetCountry() -> 'DateTime.Country':
        """ Returns the current default country.
        """

    @staticmethod
    def GetCurrentMonth(cal: Calendar=Gregorian) -> 'DateTime.Month':
        """ Get the current month in given calendar (only Gregorian is currently supported).
        """

    @staticmethod
    def GetCurrentYear(cal: Calendar=Gregorian) -> int:
        """ Get the current year in given calendar (only Gregorian is currently supported).
        """

    def GetDateOnly(self) -> 'DateTime':
        """ Returns the object having the same date component as this one but time of 00:00:00.
        """

    def GetDay(self, tz: 'DateTime.TimeZone'=Local) -> intshort:
        """ Returns the day in the given timezone (local one by default).
        """

    def GetDayOfYear(self, tz: 'DateTime.TimeZone'=Local) -> intshort:
        """ Returns the day of the year (in 1-366 range) in the given timezone (local one by default).
        """

    @staticmethod
    def GetEndDST(year=Inv_Year, country=Country_Default) -> 'DateTime':
        """ Returns the end of DST for the given country in the given year (current one by default).
        """

    @staticmethod
    def GetEnglishMonthName(month, flags=Name_Full) -> str:
        """ Return the standard English name of the given month.
        """

    @staticmethod
    def GetEnglishWeekDayName(weekday, flags=Name_Full) -> str:
        """ Return the standard English name of the given week day.
        """

    @staticmethod
    def GetFirstWeekDay(firstDay: WeekDay) -> bool:
        """ Acquires the first weekday of a week based on locale and/or OS settings.
        """

    def GetHour(self, tz: 'DateTime.TimeZone'=Local) -> intshort:
        """ Returns the hour in the given timezone (local one by default).
        """

    def GetJDN(self) -> float:
        """ Synonym for GetJulianDayNumber .
        """

    def GetJulianDayNumber(self) -> float:
        """ Returns the JDN corresponding to this date.
        """

    def GetLastMonthDay(self, month=Inv_Month, year=Inv_Year) -> 'DateTime':
        """ Returns the copy of this object to which SetToLastMonthDay   was applied.
        """

    def GetLastWeekDay(self, weekday, month=Inv_Month, year=Inv_Year) -> 'DateTime':
        """ Returns the copy of this object to which SetToLastWeekDay   was applied.
        """

    def GetMJD(self) -> float:
        """ Synonym for GetModifiedJulianDayNumber .
        """

    def GetMillisecond(self, tz: 'DateTime.TimeZone'=Local) -> intshort:
        """ Returns the milliseconds in the given timezone (local one by default).
        """

    def GetMinute(self, tz: 'DateTime.TimeZone'=Local) -> intshort:
        """ Returns the minute in the given timezone (local one by default).
        """

    def GetModifiedJulianDayNumber(self) -> float:
        """ Returns the âModified Julian Day Numberâ  (MJD) which is, by definition, is equal to JDN - 2400000.5.
        """

    def GetMonth(self, tz: 'DateTime.TimeZone'=Local) -> 'DateTime.Month':
        """ Returns the month in the given timezone (local one by default).
        """

    @staticmethod
    def GetMonthName(month, flags=Name_Full) -> str:
        """ Gets the full (default) or abbreviated name of the given month.
        """

    def GetNextWeekDay(self, weekday: DateTime.WeekDay) -> 'DateTime':
        """ Returns the copy of this object to which SetToNextWeekDay   was applied.
        """

    @staticmethod
    def GetNumberOfDays(month, year=Inv_Year, cal=Gregorian) -> intshort:
        """ Returns the number of days in the given month of the given year.
        """

    def GetPrevWeekDay(self, weekday: DateTime.WeekDay) -> 'DateTime':
        """ Returns the copy of this object to which SetToPrevWeekDay   was applied.
        """

    def GetRataDie(self) -> float:
        """ Return the Rata  Die number of this date.
        """

    def GetSecond(self, tz: 'DateTime.TimeZone'=Local) -> intshort:
        """ Returns the seconds in the given timezone (local one by default).
        """

    def GetTicks(self) -> int:
        """ Returns the number of seconds since Jan 1, 1970 UTC.
        """

    @staticmethod
    def GetTimeNow() -> int:
        """ Returns the current time.
        """

    def GetTm(self, tz: 'DateTime.TimeZone'=Local) -> 'DateTime.Tm':
        """ Returns broken down representation of the date and time.
        """

    def GetValue(self) -> int:
        """ Returns the number of milliseconds since Jan 1, 1970 UTC.
        """

    def GetWeekBasedYear(self, tz: 'DateTime.TimeZone') -> int:
        """ Returns the year to which the week containing this date belongs.
        """

    def GetWeekDay(self, *args, **kw) -> 'DateTime.WeekDay':
        """ Overloaded Implementations:
        """

    def GetWeekDayInSameWeek(self, weekday, flags=Monday_First) -> 'DateTime':
        """ Returns the copy of this object to which SetToWeekDayInSameWeek   was applied.
        """

    @staticmethod
    def GetWeekDayName(weekday, flags=Name_Full) -> str:
        """ Gets the full (default) or abbreviated name of the given week day.
        """

    def GetWeekOfMonth(self, flags=Monday_First, tz=Local) -> intshort:
        """ Returns the ordinal number of the week in the month (in 1-5 range).
        """

    def GetWeekOfYear(self, flags=Monday_First, tz=Local) -> intshort:
        """ Returns the number of the week of the year this date is in.
        """

    def GetYear(self, tz: 'DateTime.TimeZone'=Local) -> int:
        """ Returns the year in the given timezone (local one by default).
        """

    def GetYearDay(self, yday: int) -> 'DateTime':
        """ Returns the copy of this object to which SetToYearDay   was applied.
        """

    def IsBetween(self, t1, t2) -> bool:
        """ Returns True if IsStrictlyBetween   is True or if the date is equal to one of the limit values.
        """

    def IsDST(self, country: Country=Country_Default) -> int:
        """ Returns True if the DST is applied for this date in the given country.
        """

    @staticmethod
    def IsDSTApplicable(year=Inv_Year, country=Country_Default) -> bool:
        """ Returns True if DST was used in the given year (the current one by default) in the given country.
        """

    def IsEarlierThan(self, datetime: 'DateTime') -> bool:
        """ Returns True if this date precedes the given one.
        """

    def IsEqualTo(self, datetime: 'DateTime') -> bool:
        """ Returns True if the two dates are strictly identical.
        """

    def IsEqualUpTo(self, dt, ts) -> bool:
        """ Returns True if the date is equal to another one up to the given time interval, i.e. if the absolute difference between the two dates is less than this interval.
        """

    def IsLaterThan(self, datetime: 'DateTime') -> bool:
        """ Returns True if this date is later than the given one.
        """

    @staticmethod
    def IsLeapYear(year=Inv_Year, cal=Gregorian) -> bool:
        """ Returns True if the year  is a leap one in the specified calendar.
        """

    def IsSameDate(self, dt: 'DateTime') -> bool:
        """ Returns True if the date is the same without comparing the time parts.
        """

    def IsSameTime(self, dt: 'DateTime') -> bool:
        """ Returns True if the time is the same (although dates may differ).
        """

    def IsStrictlyBetween(self, t1, t2) -> bool:
        """ Returns True if this date lies strictly between the two given dates.
        """

    def IsValid(self) -> bool:
        """ Returns True if the object represents a valid time moment.
        """

    @staticmethod
    def IsWestEuropeanCountry(country: Country=Country_Default) -> bool:
        """ This function returns True if the specified (or default) country is one of Western European ones.
        """

    def IsWorkDay(self, country: Country=Country_Default) -> bool:
        """ Returns True is this day is not a holiday in the given country.
        """

    def MakeFromTimezone(self, tz, noDST=False) -> 'DateTime':
        """ Same as FromTimezone   but modifies the object in place.
        """

    def MakeTimezone(self, tz, noDST=False) -> 'DateTime':
        """ Modifies the object in place to represent the date in another time zone.
        """

    def MakeUTC(self, noDST: bool=False) -> 'DateTime':
        """ This is the same as calling MakeTimezone   with the argument  GMT0 .
        """

    @staticmethod
    def Now() -> 'DateTime':
        """ Returns the object corresponding to the current time in local time zone.
        """

    def ParseDate(self, date: str) -> int:
        """ This function is like ParseDateTime , but it only allows the date to be specified.
        """

    def ParseDateTime(self, datetime: str) -> int:
        """ Parses the string datetime  containing the date and time in free format.
        """

    def ParseFormat(self, *args, **kw) -> int:
        """ Overloaded Implementations:
        """

    def ParseISOCombined(self, date, sep='T') -> bool:
        """ This function parses the string containing the date and time in ISO 8601 combined format  "YYYY-MM-DDTHH:MM:SS" .
        """

    def ParseISODate(self, date: str) -> bool:
        """ This function parses the date in ISO 8601 format  "YYYY-MM-DD" .
        """

    def ParseISOTime(self, date: str) -> bool:
        """ This function parses the time in ISO 8601 format  "HH:MM:SS" .
        """

    def ParseRfc822Date(self, date: str) -> int:
        """ Parses the string date  looking for a date formatted according to the RFC 822 in it.
        """

    def ParseTime(self, time: str) -> int:
        """ This functions is like ParseDateTime , but only allows the time to be specified in the input string.
        """

    def ResetTime(self) -> 'DateTime':
        """ Reset time to midnight (00:00:00) without changing the date.
        """

    def Set(self, day, month, year=Inv_Year, hour=0, minute=0, second=0, millisec=0) -> 'DateTime':
        """ Sets the date and time from the parameters.
        """

    def SetHMS(self, hour, minute=0, second=0, millisec=0) -> 'DateTime':
        """ Sets the date to be equal to Today   and the time from supplied parameters.
        """

    def SetJDN(self, jdn: float) -> 'DateTime':
        """ Sets the date from the so-called Julian Day Number.
        """

    def SetTimeT(self, timet: int) -> 'DateTime':
        """ Constructs the object from timet  value holding the number of seconds since Jan 1, 1970 UTC.
        """

    def SetTm(self, tm: 'DateTime.Tm') -> 'DateTime':
        """ Sets the date and time from the broken down representation in the  ` wx.DateTime.Tm  `   structure.
        """

    @staticmethod
    def SetCountry(country: Country) -> None:
        """ Sets the country to use by default.
        """

    def SetDay(self, day: int) -> 'DateTime':
        """ Sets the day without changing other date components.
        """

    def SetFromDOS(self, ddt: int) -> 'DateTime':
        """ Sets the date from the date and time in DOS format.
        """

    def SetHour(self, hour: int) -> 'DateTime':
        """ Sets the hour without changing other date components.
        """

    def SetMillisecond(self, millisecond: int) -> 'DateTime':
        """ Sets the millisecond without changing other date components.
        """

    def SetMinute(self, minute: int) -> 'DateTime':
        """ Sets the minute without changing other date components.
        """

    def SetMonth(self, month: DateTime.Month) -> 'DateTime':
        """ Sets the month without changing other date components.
        """

    def SetSecond(self, second: int) -> 'DateTime':
        """ Sets the second without changing other date components.
        """

    def SetToCurrent(self) -> 'DateTime':
        """ Sets the date and time of to the current values.
        """

    def SetToLastMonthDay(self, month=Inv_Month, year=Inv_Year) -> 'DateTime':
        """ Sets the date to the last day in the specified month (the current one by default).
        """

    def SetToLastWeekDay(self, weekday, month=Inv_Month, year=Inv_Year) -> bool:
        """ The effect of calling this function is the same as of calling  SetToWeekDay (-1, weekday, month, year).
        """

    def SetToNextWeekDay(self, weekday: DateTime.WeekDay) -> 'DateTime':
        """ Sets the date so that it will be the first weekday  following the current date.
        """

    def SetToPrevWeekDay(self, weekday: DateTime.WeekDay) -> 'DateTime':
        """ Sets the date so that it will be the last weekday  before the current date.
        """

    def SetToWeekDay(self, weekday, n=1, month=Inv_Month, year=Inv_Year) -> bool:
        """ Sets the date to the n-th weekday  in the given month of the given year (the current month and year are used by default).
        """

    def SetToWeekDayInSameWeek(self, weekday, flags=Monday_First) -> 'DateTime':
        """ Adjusts the date so that it will still lie in the same week as before, but its week day will be the given one.
        """

    @staticmethod
    def SetToWeekOfYear(year, numWeek, weekday=Mon) -> 'DateTime':
        """ Set the date to the given weekday  in the week number numWeek  of the given year  .
        """

    def SetToYearDay(self, yday: int) -> 'DateTime':
        """ Sets the date to the day number yday  in the same year (i.e. unlike the other functions, this one does not use the current year).
        """

    def SetYear(self, year: int) -> 'DateTime':
        """ Sets the year without changing other date components.
        """

    def Subtract(self, *args, **kw) -> 'DateTime':
        """ Overloaded Implementations:
        """

    def ToTimezone(self, tz, noDST=False) -> 'DateTime':
        """ Transform the date to the given time zone.
        """

    def ToUTC(self, noDST: bool=False) -> 'DateTime':
        """ This is the same as calling ToTimezone   with the argument  GMT0 .
        """

    @staticmethod
    def Today() -> 'DateTime':
        """ Returns the object corresponding to the midnight of the current day (i.e. the same as wx.Now     , but the time part is set to 0).
        """

    @staticmethod
    def UNow() -> 'DateTime':
        """ Returns the object corresponding to the current time including the milliseconds.
        """

    def __repr__(self) -> None:
        """ 
        """

    def __str__(self) -> None:
        """ 
        """



class DCBrushChanger:
    """ DCBrushChanger is a small helper class for setting a brush on a DC
and unsetting it automatically in the destructor, restoring the
previous one.
    """
    def __init__(self, dc, brush) -> None:
        """ Sets brush  on the given dc, storing the old one.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class DCClipper:
    """ DCClipper is a helper class for setting a clipping region on a DC
during its lifetime.
    """
    def __init__(self, *args, **kw) -> None:
        """ Sets the clipping region to the specified region/coordinates.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class DCFontChanger:
    """ DCFontChanger is a small helper class for setting a font on a DC
and unsetting it automatically in the destructor, restoring the
previous one.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Set(self, font: 'Font') -> None:
        """ Set the font to use.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class DCOverlay:
    """ Connects an overlay with a drawing DC.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Clear(self) -> None:
        """ Clears the layer, restoring the state at the last init.
        """



class DCPenChanger:
    """ DCPenChanger is a small helper class for setting a pen on a DC and
unsetting it automatically in the destructor, restoring the previous
one.
    """
    def __init__(self, dc, pen) -> None:
        """ Sets pen  on the given dc, storing the old one.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class DCTextBgColourChanger:
    """ DCTextBgColourChanger is a small helper class for setting a
background text colour on a DC and unsetting it automatically in the
destructor, restoring the previous one.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Set(self, col: Union[int, str, 'Colour']) -> None:
        """ Set the background colour to use.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class DCTextBgModeChanger:
    """ DCTextBgModeChanger is a small helper class for setting a background
text mode on a DC and unsetting it automatically in the destructor,
restoring the previous one.
    """
    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class DCTextColourChanger:
    """ DCTextColourChanger is a small helper class for setting a foreground
text colour on a DC and unsetting it automatically in the
destructor, restoring the previous one.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Set(self, col: Union[int, str, 'Colour']) -> None:
        """ Set the colour to use.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class DelegateRendererNative(RendererNative):
    """ DelegateRendererNative allows reuse of renderers code by forwarding
all the RendererNative methods to the given object and thus allowing
you to only modify some of its methods  without having to reimplement
all of them.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawCheckBox(self, win, dc, rect, flags=0) -> None:
        """ Draw a check box.
        """

    def DrawCheckMark(self, win, dc, rect, flags=0) -> None:
        """ Draw a check mark.
        """

    def DrawComboBoxDropButton(self, win, dc, rect, flags=0) -> None:
        """ Draw a button like the one used by   wx.ComboBox  to show a drop down window.
        """

    def DrawDropArrow(self, win, dc, rect, flags=0) -> None:
        """ Draw a drop down arrow that is suitable for use outside a combo box.
        """

    def DrawFocusRect(self, win, dc, rect, flags=0) -> None:
        """ Draw a focus rectangle using the specified rectangle.
        """

    def DrawHeaderButton(self, win, dc, rect, flags=0, sortArrow=HDR_SORT_ICON_NONE, params=None) -> int:
        """ Draw the header control button (used, for example, by   wx.ListCtrl).
        """

    def DrawHeaderButtonContents(self, win, dc, rect, flags=0, sortArrow=HDR_SORT_ICON_NONE, params=None) -> int:
        """ Draw the contents of a header control button (label, sort arrows, etc.).
        """

    def DrawItemSelectionRect(self, win, dc, rect, flags=0) -> None:
        """ Draw a selection rectangle underneath the text as used e.g.
        """

    def DrawPushButton(self, win, dc, rect, flags=0) -> None:
        """ Draw a blank push button that looks very similar to   wx.Button.
        """

    def DrawSplitterBorder(self, win, dc, rect, flags=0) -> None:
        """ Draw the border for sash window: this border must be such that the sash drawn by DrawSplitterSash   blends into it well.
        """

    def DrawSplitterSash(self, win, dc, size, position, orient, flags=0) -> None:
        """ Draw a sash.
        """

    def DrawTitleBarBitmap(self, win, dc, rect, button, flags=0) -> None:
        """ Draw a title bar button in the given state.
        """

    def DrawTreeItemButton(self, win, dc, rect, flags=0) -> None:
        """ Draw the expanded/collapsed icon for a tree control item.
        """

    def GetCheckBoxSize(self, win, flags=0) -> 'Size':
        """ Returns the size of a check box.
        """

    def GetCheckMarkSize(self, win: 'Window') -> 'Size':
        """ Returns the size of a check mark.
        """

    def GetExpanderSize(self, win: 'Window') -> 'Size':
        """ Returns the size of the expander used in tree-like controls.
        """

    def GetHeaderButtonHeight(self, win: 'Window') -> int:
        """ Returns the height of a header button, either a fixed platform height if available, or a generic height based on the win  windowâs font.
        """

    def GetHeaderButtonMargin(self, win: 'Window') -> int:
        """ Returns the horizontal margin on the left and right sides of header buttonâs label.
        """

    def GetSplitterParams(self, win: 'Window') -> 'SplitterRenderParams':
        """ Get the splitter parameters, see   wx.SplitterRenderParams.
        """

    def GetVersion(self) -> 'RendererVersion':
        """ This function is used for version checking: Load   refuses to load any shared libraries implementing an older or incompatible version.
        """



class RendererNative:
    """ First, a brief introduction to RendererNative and why it is needed.
    """
    def DrawCheckBox(self, win, dc, rect, flags=0) -> None:
        """ Draw a check box.
        """

    def DrawCheckMark(self, win, dc, rect, flags=0) -> None:
        """ Draw a check mark.
        """

    def DrawChoice(self, win, dc, rect, flags=0) -> None:
        """ Draw a native   wx.Choice.
        """

    def DrawCollapseButton(self, win, dc, rect, flags=0) -> None:
        """ Draw a collapse button.
        """

    def DrawComboBox(self, win, dc, rect, flags=0) -> None:
        """ Draw a native   wx.ComboBox.
        """

    def DrawComboBoxDropButton(self, win, dc, rect, flags=0) -> None:
        """ Draw a button like the one used by   wx.ComboBox  to show a drop down window.
        """

    def DrawDropArrow(self, win, dc, rect, flags=0) -> None:
        """ Draw a drop down arrow that is suitable for use outside a combo box.
        """

    def DrawFocusRect(self, win, dc, rect, flags=0) -> None:
        """ Draw a focus rectangle using the specified rectangle.
        """

    def DrawGauge(self, win, dc, rect, value, max, flags=0) -> None:
        """ Draw a progress bar in the specified rectangle.
        """

    def DrawHeaderButton(self, win, dc, rect, flags=0, sortArrow=HDR_SORT_ICON_NONE, params=None) -> int:
        """ Draw the header control button (used, for example, by   wx.ListCtrl).
        """

    def DrawHeaderButtonContents(self, win, dc, rect, flags=0, sortArrow=HDR_SORT_ICON_NONE, params=None) -> int:
        """ Draw the contents of a header control button (label, sort arrows, etc.).
        """

    def DrawItemSelectionRect(self, win, dc, rect, flags=0) -> None:
        """ Draw a selection rectangle underneath the text as used e.g.
        """

    def DrawItemText(self, win, dc, text, rect, align=ALIGN_LEFT|ALIGN_TOP, flags=0, ellipsizeMode=ELLIPSIZE_END) -> None:
        """ Draw item text in the correct color based on selection status.
        """

    def DrawPushButton(self, win, dc, rect, flags=0) -> None:
        """ Draw a blank push button that looks very similar to   wx.Button.
        """

    def DrawRadioBitmap(self, win, dc, rect, flags=0) -> None:
        """ Draw a native   wx.RadioButton  bitmap.
        """

    def DrawSplitterBorder(self, win, dc, rect, flags=0) -> None:
        """ Draw the border for sash window: this border must be such that the sash drawn by DrawSplitterSash   blends into it well.
        """

    def DrawSplitterSash(self, win, dc, size, position, orient, flags=0) -> None:
        """ Draw a sash.
        """

    def DrawTextCtrl(self, win, dc, rect, flags=0) -> None:
        """ Draw a native   wx.TextCtrl  frame.
        """

    def DrawTitleBarBitmap(self, win, dc, rect, button, flags=0) -> None:
        """ Draw a title bar button in the given state.
        """

    def DrawTreeItemButton(self, win, dc, rect, flags=0) -> None:
        """ Draw the expanded/collapsed icon for a tree control item.
        """

    @staticmethod
    def Get() -> 'RendererNative':
        """ Return the currently used renderer.
        """

    def GetCheckBoxSize(self, win, flags=0) -> 'Size':
        """ Returns the size of a check box.
        """

    def GetCheckMarkSize(self, win: 'Window') -> 'Size':
        """ Returns the size of a check mark.
        """

    def GetCollapseButtonSize(self, win, dc) -> 'Size':
        """ Returns the size of a collapse button.
        """

    @staticmethod
    def GetDefault() -> 'RendererNative':
        """ Return the default (native) implementation for this platform â  this is also the one used by default but this may be changed by calling Set   in which case the return value of this method may be different from the return value of Get .
        """

    def GetExpanderSize(self, win: 'Window') -> 'Size':
        """ Returns the size of the expander used in tree-like controls.
        """

    @staticmethod
    def GetGeneric() -> 'RendererNative':
        """ Return the generic implementation of the renderer.
        """

    def GetHeaderButtonHeight(self, win: 'Window') -> int:
        """ Returns the height of a header button, either a fixed platform height if available, or a generic height based on the win  windowâs font.
        """

    def GetHeaderButtonMargin(self, win: 'Window') -> int:
        """ Returns the horizontal margin on the left and right sides of header buttonâs label.
        """

    def GetSplitterParams(self, win: 'Window') -> 'SplitterRenderParams':
        """ Get the splitter parameters, see   wx.SplitterRenderParams.
        """

    def GetVersion(self) -> 'RendererVersion':
        """ This function is used for version checking: Load   refuses to load any shared libraries implementing an older or incompatible version.
        """

    @staticmethod
    def Load(name: str) -> 'RendererNative':
        """ Load the renderer from the specified DLL, the returned pointer must be deleted by caller if not None when it is not used any more.
        """

    @staticmethod
    def Set(renderer: 'RendererNative') -> 'RendererNative':
        """ Set the renderer to use, passing None reverts to using the default renderer (the global renderer must always exist).
        """



class Dialog(TopLevelWindow):
    """ A dialog box is a window with a title bar and sometimes a system menu,
which can be moved around the screen.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddMainButtonId(self, id: int) -> None:
        """ Adds an identifier to be regarded as a main button for the non-scrolling area of a dialog.
        """

    def CanDoLayoutAdaptation(self) -> bool:
        """ Returns True if this dialog can and should perform layout adaptation using DoLayoutAdaptation , usually if the dialog is too large to fit on the display.
        """

    def Centre(self, direction: int=BOTH) -> None:
        """ Centres the dialog box on the display.
        """

    def Create(self, parent, id=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize, style=DEFAULT_DIALOG_STYLE, name=DialogNameStr) -> bool:
        """ Used for two-step dialog box construction.
        """

    def CreateButtonSizer(self, flags: int) -> 'Sizer':
        """ Creates a sizer with standard buttons.
        """

    def CreateSeparatedButtonSizer(self, flags: int) -> 'Sizer':
        """ Creates a sizer with standard buttons using CreateButtonSizer   separated from the rest of the dialog contents by a horizontal   wx.StaticLine.
        """

    def CreateSeparatedSizer(self, sizer: 'Sizer') -> 'Sizer':
        """ Returns the sizer containing the given one with a separating   wx.StaticLine  if necessarily.
        """

    def CreateStdDialogButtonSizer(self, flags: int) -> 'StdDialogButtonSizer':
        """ Creates a   wx.StdDialogButtonSizer  with standard buttons.
        """

    def CreateTextSizer(self, message, widthMax=-1) -> 'Sizer':
        """ Splits text up at newlines and places the lines into   wx.StaticText  objects with the specified maximum width in a vertical   wx.BoxSizer.
        """

    def DoLayoutAdaptation(self) -> bool:
        """ Performs layout adaptation, usually if the dialog is too large to fit on the display.
        """

    @staticmethod
    def EnableLayoutAdaptation(enable: bool) -> None:
        """ A static function enabling or disabling layout adaptation for all dialogs.
        """

    def EndModal(self, retCode: int) -> None:
        """ Ends a modal dialog, passing a value to be returned from the ShowModal   invocation.
        """

    def GetAffirmativeId(self) -> int:
        """ Gets the identifier of the button which works like standard wx.OK button in this dialog.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetContentWindow(self) -> 'Window':
        """ Override this to return a window containing the main content of the dialog.
        """

    def GetEscapeId(self) -> int:
        """ Gets the identifier of the button to map presses of  ESC   button to.
        """

    def GetLayoutAdaptationDone(self) -> bool:
        """ Returns True if the dialog has been adapted, usually by making it scrollable to work with a small display.
        """

    def GetLayoutAdaptationLevel(self) -> int:
        """ Gets a value representing the aggressiveness of search for buttons and sizers to be in the non-scrolling part of a layout-adapted dialog.
        """

    def GetLayoutAdaptationMode(self) -> 'DialogLayoutAdaptationMode':
        """ Gets the adaptation mode, overriding the global adaptation flag.
        """

    @staticmethod
    def GetLayoutAdapter() -> 'DialogLayoutAdapter':
        """ A static function getting the current layout adapter object.
        """

    def GetMainButtonIds(self) -> list[int]:
        """ Returns an array of identifiers to be regarded as the main buttons for the non-scrolling area of a dialog.
        """

    def GetReturnCode(self) -> int:
        """ Gets the return code for this window.
        """

    def Iconize(self, iconize: bool=True) -> None:
        """ Iconizes or restores the dialog.
        """

    def IsIconized(self) -> bool:
        """ Returns True if the dialog box is iconized.
        """

    @staticmethod
    def IsLayoutAdaptationEnabled() -> bool:
        """ A static function returning True if layout adaptation is enabled for all dialogs.
        """

    def IsMainButtonId(self, id: int) -> bool:
        """ Returns True if id  is in the array of identifiers to be regarded as the main buttons for the non-scrolling area of a dialog.
        """

    def IsModal(self) -> bool:
        """ Returns True if the dialog box is modal, False otherwise.
        """

    def SetAffirmativeId(self, id: int) -> None:
        """ Sets the identifier to be used as wx.OK button.
        """

    def SetEscapeId(self, id: int) -> None:
        """ Sets the identifier of the button which should work like the standard âCancelâ button in this dialog.
        """

    def SetIcon(self, icon: 'Icon') -> None:
        """ Sets the icon for this dialog.
        """

    def SetIcons(self, icons: 'IconBundle') -> None:
        """ Sets the icons for this dialog.
        """

    def SetLayoutAdaptationDone(self, done: bool) -> None:
        """ Marks the dialog as having been adapted, usually by making it scrollable to work with a small display.
        """

    def SetLayoutAdaptationLevel(self, level: int) -> None:
        """ Sets the aggressiveness of search for buttons and sizers to be in the non-scrolling part of a layout-adapted dialog.
        """

    def SetLayoutAdaptationMode(self, mode: DialogLayoutAdaptationMode) -> None:
        """ Sets the adaptation mode, overriding the global adaptation flag.
        """

    @staticmethod
    def SetLayoutAdapter(adapter: 'DialogLayoutAdapter') -> 'DialogLayoutAdapter':
        """ A static function for setting the current layout adapter object, returning the old adapter.
        """

    def SetReturnCode(self, retCode: int) -> None:
        """ Sets the return code for this window.
        """

    def Show(self, show: bool=True) -> bool:
        """ Hides or shows the dialog.
        """

    def ShowModal(self) -> int:
        """ Shows an application-modal dialog.
        """

    def ShowWindowModal(self) -> None:
        """ Shows a dialog modal to the parent top level window only.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """

CAPTION: int  #  Puts a caption on the dialog box.
DEFAULT_DIALOG_STYLE: int  #  Equivalent to a combination of wx.CAPTION, wx.CLOSE_BOX and wx.SYSTEM_MENU (the last one is not used under Unix).
RESIZE_BORDER: int  #  Display a resizable frame around the window.
SYSTEM_MENU: int  #  Display a system menu.
CLOSE_BOX: int  #  Displays a close box on the frame.
MAXIMIZE_BOX: int  #  Displays a maximize box on the dialog.
MINIMIZE_BOX: int  #  Displays a minimize box on the dialog.
THICK_FRAME: int  #  Display a thick frame around the window.
STAY_ON_TOP: int  #  The dialog stays on top of all other windows.
NO_3D: int  #  This style is obsolete and doesnât do anything any more, donât use it in any new code.
DIALOG_NO_PARENT: int  #  By default, a dialog created with a None parent window will be given the applicationâs top level window  as parent. Use this style to prevent this from happening and create an orphan dialog. This is not recommended for modal dialogs.
DIALOG_EX_CONTEXTHELP: int  #  Under Windows, puts a query button on the caption. When pressed, Windows will go into a context-sensitive help mode and wxWidgets will send a  wxEVT_HELP   event if the user clicked on an application window. Note that this is an extended style and must be set by calling  SetExtraStyle  before Create is called (two-step construction).
DIALOG_EX_METAL: int  #  On macOS, frames with this style will be shown with a metallic look. This is an extra style. ^^
EVT_CLOSE: int  #  The dialog is being closed by the user or programmatically (see wx.Window.Close ). The user may generate this event clicking the close button (typically the âXâ on the top-right of the title bar) if itâs present (see the  CLOSE_BOX   style).
EVT_INIT_DIALOG: int  #  Process a  wxEVT_INIT_DIALOG   event. See    wx.InitDialogEvent. ^^
ID_OK: int
ID_CANCEL: int
CAPTION: int
DEFAULT_DIALOG_STYLE: int
CAPTION: int
CLOSE_BOX: int
SYSTEM_MENU: int
RESIZE_BORDER: int
SYSTEM_MENU: int
CLOSE_BOX: int
MAXIMIZE_BOX: int
MINIMIZE_BOX: int
STAY_ON_TOP: int
DIALOG_NO_PARENT: int
DIALOG_EX_CONTEXTHELP: int
DIALOG_EX_METAL: int
OK: int
OK: int
HORIZONTAL: int
VERTICAL: int
BOTH: int
OK: int
CANCEL: int
YES: int
NO: int
APPLY: int
CLOSE: int
HELP: int
NO_DEFAULT: int
OK: int
CANCEL: int
YES: int
NO: int
APPLY: int
CLOSE: int
HELP: int
NO_DEFAULT: int
OK: int
OK: int
OK: int
OK: int
ID_OK: int
ID_ANY: int
ID_CANCEL: int
ID_NONE: int


class DialogLayoutAdapter:
    """ This abstract class is the base for classes that help wxWidgets
perform run-time layout adaptation of dialogs.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def CanDoLayoutAdaptation(self, dialog: 'Dialog') -> bool:
        """ Override this to returns True if adaptation can and should be done.
        """

    def DoLayoutAdaptation(self, dialog: 'Dialog') -> bool:
        """ Override this to perform layout adaptation, such as making parts of the dialog scroll and resizing the dialog to fit the display.
        """



class DirDialog(Dialog):
    """ This class represents the directory chooser dialog.
    """
    def __init__(self, parent, message=DirSelectorPromptStr, defaultPath="", style=DD_DEFAULT_STYLE, pos=DefaultPosition, size=DefaultSize, name=DirDialogNameStr) -> None:
        """ Constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetMessage(self) -> str:
        """ Returns the message that will be displayed on the dialog.
        """

    def GetPath(self) -> str:
        """ Returns the default or user-selected path.
        """

    def GetPaths(self, paths: list[str]) -> None:
        """ Fills the array paths  with the full paths of the chosen directories.
        """

    def SetMessage(self, message: str) -> None:
        """ Sets the message that will be displayed on the dialog.
        """

    def SetPath(self, path: str) -> None:
        """ Sets the default path.
        """

    def ShowModal(self) -> int:
        """ Shows the dialog, returning wx.ID_OK if the user pressed wx.OK, and wx.ID_CANCEL otherwise.
        """

DD_DEFAULT_STYLE: int  #  Equivalent to a combination of wx.DEFAULT_DIALOG_STYLE and wx.RESIZE_BORDER.
DD_DIR_MUST_EXIST: int  #  The dialog will allow the user to choose only an existing folder. When this style is not given, a âCreate new directoryâ button is added to the dialog (on Windows) or some other way is provided to the user to type the name of a new folder.
DD_CHANGE_DIR: int  #  Change the current working directory to the directory chosen by the user. This flag cannot be used with the  DD_MULTIPLE   style.
DD_MULTIPLE: int  #  Allow the user to select multiple directories. This flag is only available since wxWidgets 3.1.4
DD_SHOW_HIDDEN: int  #  Show hidden and system folders. This flag is only available since wxWidgets 3.1.4 ^^
DD_DEFAULT_STYLE: int
DEFAULT_DIALOG_STYLE: int
RESIZE_BORDER: int
DD_DIR_MUST_EXIST: int
DD_CHANGE_DIR: int
DD_MULTIPLE: int
DD_SHOW_HIDDEN: int
ID_OK: int
OK: int
ID_CANCEL: int
ID_OK: int
OK: int
ID_CANCEL: int


class DirFilterListCtrl(Choice):
    """  Overloaded Implementations:
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ parent (wx.GenericDirCtrl) â
        """

    def FillFilterList(self, filter, defaultFilter) -> None:
        """ filter (string) â
        """

    def Init(self) -> None:
        """ 
        """



class DirPickerCtrl(PickerBase):
    """ This control allows the user to select a directory.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, path="", message=DirSelectorPromptStr, pos=DefaultPosition, size=DefaultSize, style=DIRP_DEFAULT_STYLE, validator=DefaultValidator, name=DirPickerCtrlNameStr) -> bool:
        """ Creates the widgets with the given parameters.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetPath(self) -> str:
        """ Returns the absolute path of the currently selected directory.
        """

    def SetInitialDirectory(self, dir: str) -> None:
        """ Set the directory to show when starting to browse for directories.
        """

    def SetPath(self, dirname: str) -> None:
        """ Sets the absolute path of the currently selected directory.
        """

DIRP_DEFAULT_STYLE: int  #  The default style: int  #  includes wx.DIRP_DIR_MUST_EXIST and, under wxMSW only, wx.DIRP_USE_TEXTCTRL.
DIRP_USE_TEXTCTRL: int  #  Creates a text control to the left of the picker button which is completely managed by the   wx.DirPickerCtrl  and which can be used by the user to specify a path (see SetPath). The text control is automatically synchronized with buttonâs value. Use functions defined in   wx.PickerBase  to modify the text control.
DIRP_DIR_MUST_EXIST: int  #  Creates a picker which allows selecting only existing directories in the popup   wx.DirDialog. Notice that, as with  FLP_FILE_MUST_EXIST , it is still possible to enter a non-existent directory even when this file is specified if   DIRP_USE_TEXTCTRL   style is also used. Also note that if   DIRP_USE_TEXTCTRL   is not used, the native wxGTK implementation always uses this style as it doesnât support selecting non-existent directories.
DIRP_CHANGE_DIR: int  #  Change current working directory on each user directory selection change.
DIRP_SMALL: int  #  Use smaller version of the control with a small ââ¦â button instead of the normal âBrowseâ one. This flag is new since wxWidgets 2.9.3. ^^
EVT_DIRPICKER_CHANGED: int  #  The user changed the directory selected in the control either using the button or using text control (see wx.DIRP_USE_TEXTCTRL; note that in this case the event is fired only if the userâs input is valid, e.g. an existing directory path). ^^
DIRP_DEFAULT_STYLE: int
DIRP_DIR_MUST_EXIST: int
DIRP_USE_TEXTCTRL: int
DIRP_USE_TEXTCTRL: int
DIRP_DIR_MUST_EXIST: int
DIRP_CHANGE_DIR: int
DIRP_SMALL: int
DIRP_USE_TEXTCTRL: int


class Display:
    """ Determines the sizes and locations of displays connected to the
system.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def ChangeMode(self, mode: 'VideoMode'=DefaultVideoMode) -> bool:
        """ Changes the video mode of this display to the mode specified in the mode parameter.
        """

    def GetClientArea(self) -> 'Rect':
        """ Returns the client area of the display.
        """

    @staticmethod
    def GetCount() -> int:
        """ Returns the number of connected displays.
        """

    def GetCurrentMode(self) -> 'VideoMode':
        """ Returns the current video mode that this display is in.
        """

    @staticmethod
    def GetFromPoint(pt: 'Point') -> int:
        """ Returns the index of the display on which the given point lies, or  NOT_FOUND   if the point is not on any connected display.
        """

    @staticmethod
    def GetFromWindow(win: 'Window') -> int:
        """ Returns the index of the display on which the given window lies.
        """

    def GetGeometry(self) -> 'Rect':
        """ Returns the bounding rectangle of the display whose index was passed to the constructor.
        """

    def GetModes(self, mode: 'VideoMode'=DefaultVideoMode) -> ArrayVideoModes:
        """ Fills and returns an array with all the video modes that are supported by this display, or video modes that are supported by this display and match the mode parameter (if mode is not DefaultVideoMode).
        """

    def GetName(self) -> str:
        """ Returns the displayâs name.
        """

    def GetPPI(self) -> 'Size':
        """ Returns display resolution in pixels per inch.
        """

    def GetScaleFactor(self) -> float:
        """ Returns scaling factor used by this display.
        """

    @staticmethod
    def GetStdPPI() -> 'Size':
        """ Returns default display resolution for the current platform as   wx.Size.
        """

    @staticmethod
    def GetStdPPIValue() -> int:
        """ Returns default display resolution for the current platform in pixels per inch.
        """

    def IsPrimary(self) -> bool:
        """ Returns True if the display is the primary display.
        """



class DisplayChangedEvent(Event):
    """ A display changed event is sent to top-level windows when the display
resolution has changed.
    """
    def __init__(self) -> None:
        """ 
        """

EVT_DISPLAY_CHANGED: int  #  Process a  wxEVT_DISPLAY_CHANGED   event. ^^


class DPIChangedEvent(Event):
    """ Event sent when the display scale factor or pixel density (measured in
dots-per-inch, or DPI) of the monitor a window is on changes.
    """
    def GetNewDPI(self) -> 'Size':
        """ Returns the new DPI.
        """

    def GetOldDPI(self) -> 'Size':
        """ Returns the old DPI.
        """

    def Scale(self, sz: Union[tuple[int, int], 'Size']) -> 'Size':
        """ Rescale a value in pixels to match the new DPI.
        """

    def ScaleX(self, x: int) -> int:
        """ Rescale horizontal component to match the new DPI.
        """

    def ScaleY(self, y: int) -> int:
        """ Rescale vertical component to match the new DPI.
        """

EVT_DPI_CHANGED: int  #  Process a  wxEVT_DPI_CHANGED   event. ^^


class DragImage(Object):
    """ This class is used when you wish to drag an object on the screen, and
a simple cursor is not enough.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def BeginDrag(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def EndDrag(self) -> bool:
        """ Call this when the drag has finished.
        """

    def Hide(self) -> bool:
        """ Hides the image.
        """

    def Move(self, pt: 'Point') -> bool:
        """ Call this to move the image to a new position.
        """

    def Show(self) -> bool:
        """ Shows the image.
        """



class DropFilesEvent(Event):
    """ This class is used for drop files events, that is, when files have
been dropped onto the window.
    """
    def __init__(self, id=0, files=None) -> None:
        """ Constructor.
        """

    def GetFiles(self) -> Any:
        """ Returns an array of filenames.
        """

    def GetNumberOfFiles(self) -> int:
        """ Returns the number of files dropped.
        """

    def GetPosition(self) -> 'Point':
        """ Returns the position at which the files were dropped.
        """

EVT_DROP_FILES: int  #  Process a  wxEVT_DROP_FILES   event. ^^


class DropSource:
    """ This class represents a source for a drag and drop operation.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DoDragDrop(self, flags: int=Drag_CopyOnly) -> 'DragResult':
        """ Starts the drag-and-drop operation which will terminate when the user releases the mouse.
        """

    def GetDataObject(self) -> 'DataObject':
        """ Returns the   wx.DataObject  object that has been assigned previously.
        """

    def GiveFeedback(self, effect: DragResult) -> bool:
        """ You may give some custom UI feedback during the drag and drop operation by overriding this function.
        """

    def SetCursor(self, res, cursor) -> None:
        """ Set the icon to use for a certain drag result.
        """

    def SetData(self, data: 'DataObject') -> None:
        """ Sets the data   wx.DataObject  associated with the drop source.
        """

    def SetIcon(self, res, icon) -> None:
        """ Set the icon to use for a certain drag result.
        """



class DropTarget:
    """ This class represents a target for a drag and drop operation.
    """
    def __init__(self, data: Optional['DataObject']=None) -> None:
        """ Constructor.
        """

    def GetData(self) -> bool:
        """ This method may only be called from within OnData .
        """

    def GetDataObject(self) -> 'DataObject':
        """ Returns the data   wx.DataObject  associated with the drop target.
        """

    def GetDefaultAction(self) -> 'DragResult':
        """ Returns default action for drag and drop or DragNone if this not specified.
        """

    def OnData(self, x, y, defResult) -> 'DragResult':
        """ Called after OnDrop   returns True.
        """

    def OnDragOver(self, x, y, defResult) -> 'DragResult':
        """ Called when the mouse is being dragged over the drop target.
        """

    def OnDrop(self, x, y) -> bool:
        """ Called when the user drops a data object on the target.
        """

    def OnEnter(self, x, y, defResult) -> 'DragResult':
        """ Called when the mouse enters the drop target.
        """

    def OnLeave(self) -> None:
        """ Called when the mouse leaves the drop target.
        """

    def SetDataObject(self, data: 'DataObject') -> None:
        """ Sets the data   wx.DataObject  associated with the drop target and deletes any previously associated data object.
        """

    def SetDefaultAction(self, action: DragResult) -> None:
        """ Sets the default action for drag and drop.
        """



class EraseEvent(Event):
    """ An erase event is sent when a windowâs background needs to be
repainted.
    """
    def __init__(self, id=0, dc=None) -> None:
        """ Constructor.
        """

    def GetDC(self) -> 'DC':
        """ Returns the device context associated with the erase event to draw on.
        """

EVT_ERASE_BACKGROUND: int  #  Process a  wxEVT_ERASE_BACKGROUND   event. ^^


class Event(Object):
    """ An event is a structure holding information about an event passed to a
callback or member function.
    """
    def __init__(self, id=0, eventType=wxEVT_NULL) -> None:
        """ Constructor.
        """

    def Clone(self) -> 'Event':
        """ Returns a copy of the event.
        """

    def GetEventCategory(self) -> int:
        """ Returns a generic category for this event.
        """

    def GetEventObject(self) -> 'Window':
        """ Returns the object (usually a window) associated with the event, if any.
        """

    def GetEventType(self) -> int:
        """ Returns the identifier of the given event type, such as  wxEVT_BUTTON .
        """

    def GetId(self) -> int:
        """ Returns the identifier associated with this event, such as a button command id.
        """

    def GetSkipped(self) -> bool:
        """ Returns True if the event handler should be skipped, False otherwise.
        """

    def GetTimestamp(self) -> int:
        """ Gets the timestamp for the event.
        """

    def IsCommandEvent(self) -> bool:
        """ Returns True if the event is or is derived from   wx.CommandEvent  else it returns False.
        """

    def ResumePropagation(self, propagationLevel: int) -> None:
        """ Sets the propagation level to the given value (for example returned from an earlier call to wx.Event.StopPropagation ).
        """

    def SetEventObject(self, object: 'Object') -> None:
        """ Sets the originating object.
        """

    def SetEventType(self, type: int) -> None:
        """ Sets the event type.
        """

    def SetId(self, id: int) -> None:
        """ Sets the identifier associated with this event, such as a button command id.
        """

    def SetTimestamp(self, timeStamp: int=0) -> None:
        """ Sets the timestamp for the event.
        """

    def ShouldPropagate(self) -> bool:
        """ Test if this event should be propagated or not, i.e. if the propagation level is currently greater than 0.
        """

    def Skip(self, skip: bool=True) -> None:
        """ This method can be used inside an event handler to control whether further event handlers bound to this event will be called after the current one returns.
        """

    def StopPropagation(self) -> int:
        """ Stop the event from propagating to its parent window.
        """



class EventBlocker(EvtHandler):
    """ This class is a special event handler which allows discarding any
event (or a set of event types) directed to a specific window.
    """
    def __init__(self, win, type=-1) -> None:
        """ Constructs the blocker for the given window and for the given event type.
        """

    def Block(self, eventType: int) -> None:
        """ Adds to the list of event types which should be blocked the given eventType.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class EventFilter:
    """ A global event filter for pre-processing all the events generated in
the program.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def FilterEvent(self, event: 'Event') -> int:
        """ Override this method to implement event pre-processing.
        """



class EventLoopActivator:
    """ Makes an event loop temporarily active.
    """
    def __init__(self, loop: 'EventLoopBase') -> None:
        """ Makes the loop passed as the parameter currently active.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class EventLoopBase:
    """ Base class for all event loop implementations.
    """
    def Dispatch(self) -> bool:
        """ Dispatches the next event in the windowing system event queue.
        """

    def DispatchTimeout(self, timeout: int) -> int:
        """ Dispatch an event but not wait longer than the specified timeout for it.
        """

    def Exit(self, rc: int=0) -> None:
        """ Exit the currently running loop with the given exit code.
        """

    @staticmethod
    def GetActive() -> 'EventLoopBase':
        """ Return the currently active (running) event loop.
        """

    def IsEventAllowedInsideYield(self, cat: int) -> bool:
        """ Returns True if the given event category is allowed inside a YieldFor   call (i.e.
        """

    def IsMain(self) -> bool:
        """ Returns True if this is the main loop executed by wx.App.OnRun .
        """

    def IsOk(self) -> bool:
        """ Use this to check whether the event loop was successfully created before using it.
        """

    def IsRunning(self) -> bool:
        """ Return True if this event loop is currently running.
        """

    def IsYielding(self) -> bool:
        """ Returns True if called from inside wx.Yield       or from inside YieldFor .
        """

    def OnExit(self) -> None:
        """ This function is called before the event loop terminates, whether this happens normally (because of wx.Exit       call) or abnormally (because of an exception thrown from inside the loop).
        """

    def Pending(self) -> bool:
        """ Return True if any events are available.
        """

    def ProcessIdle(self) -> bool:
        """ This virtual function is called when the application becomes idle and normally just sends   wx.IdleEvent  to all interested parties.
        """

    def Run(self) -> int:
        """ Start the event loop, return the exit code when it is finished.
        """

    def ScheduleExit(self, rc: int=0) -> None:
        """ Schedule an exit from the loop with the given exit code.
        """

    @staticmethod
    def SetActive(loop: 'EventLoopBase') -> None:
        """ Set currently active (running) event loop.
        """

    def WakeUp(self) -> None:
        """ Called by wxWidgets to wake up the event loop even if it is currently blocked inside Dispatch .
        """

    def WakeUpIdle(self) -> None:
        """ Makes sure that idle events are sent again.
        """

    def Yield(self, onlyIfNeeded: bool=False) -> bool:
        """ Yields control to pending messages in the windowing system.
        """

    def YieldFor(self, eventsToProcess: int) -> bool:
        """ Works like wx.Yield       with onlyIfNeeded  == True, except that it allows the caller to specify a mask of the   wx.EventCategory  values which indicates which events should be processed and which should instead be âdelayedâ (i.e.
        """



class EvtHandler(Object, Trackable):
    """ A class that can handle events from the windowing system.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    @staticmethod
    def AddFilter(filter: 'EventFilter') -> None:
        """ Add an event filter whose FilterEvent() method will be called for each and every event processed by wxWidgets.
        """

    def AddPendingEvent(self, event: 'Event') -> None:
        """ Post an event to be processed later.
        """

    def Bind(self, event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY) -> None:
        """ Bind an event to an event handler.
        """

    def Connect(self, id, lastId, eventType, func) -> None:
        """ Make an entry in the dynamic event table for an event binding.
        """

    def DeletePendingEvents(self) -> None:
        """ Deletes all events queued on this event handler using wx.QueueEvent       or AddPendingEvent .
        """

    def Disconnect(self, id, lastId=-1, eventType=wxEVT_NULL, func=None) -> bool:
        """ Remove an event binding by removing its entry in the dynamic event table.
        """

    def GetEvtHandlerEnabled(self) -> bool:
        """ Returns True if the event handler is enabled, False otherwise.
        """

    def GetNextHandler(self) -> 'EvtHandler':
        """ Returns the pointer to the next handler in the chain.
        """

    def GetPreviousHandler(self) -> 'EvtHandler':
        """ Returns the pointer to the previous handler in the chain.
        """

    def IsUnlinked(self) -> bool:
        """ Returns True if the next and the previous handler pointers of this event handler instance are None.
        """

    def ProcessEvent(self, event: 'Event') -> bool:
        """ Processes an event, searching event tables and calling zero or more suitable event handler function(s).
        """

    def ProcessEventLocally(self, event: 'Event') -> bool:
        """ Try to process the event in this handler and all those chained to it.
        """

    def ProcessPendingEvents(self) -> None:
        """ Processes the pending events previously queued using wx.QueueEvent       or AddPendingEvent ; you must call this function only if you are sure there are pending events for this handler, otherwise a  CHECK   will fail.
        """

    def QueueEvent(self, event: 'Event') -> None:
        """ Queue event for a later processing.
        """

    @staticmethod
    def RemoveFilter(filter: 'EventFilter') -> None:
        """ Remove a filter previously installed with AddFilter .
        """

    def SafelyProcessEvent(self, event: 'Event') -> bool:
        """ Processes an event by calling   wx.ProcessEvent  and handles any exceptions that occur in the process.
        """

    def SetEvtHandlerEnabled(self, enabled: bool) -> None:
        """ Enables or disables the event handler.
        """

    def SetNextHandler(self, handler: 'EvtHandler') -> None:
        """ Sets the pointer to the next handler.
        """

    def SetPreviousHandler(self, handler: 'EvtHandler') -> None:
        """ Sets the pointer to the previous handler.
        """

    def TryAfter(self, event: 'Event') -> bool:
        """ Method called by   wx.ProcessEvent  as last resort.
        """

    def TryBefore(self, event: 'Event') -> bool:
        """ Method called by   wx.ProcessEvent  before examining this object event tables.
        """

    def Unbind(self, event, source=None, id=wx.ID_ANY, id2=wx.ID_ANY, handler=None) -> None:
        """ Disconnects the event handler binding for event from self.
Returns True if successful.
        """

    def Unlink(self) -> None:
        """ Unlinks this event handler from the chain itâs part of (if any); then links the âpreviousâ event handler to the ânextâ one (so that the chain wonât be interrupted).
        """



class FileConfig(ConfigBase):
    """ FileConfig implements ConfigBase interface for storing and
retrieving configuration information using plain text files.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DeleteAll(self) -> bool:
        """ Delete the whole underlying object (disk file, registry key, â¦).
        """

    def DeleteEntry(self, key, bDeleteGroupIfEmpty=True) -> bool:
        """ Deletes the specified entry and the group it belongs to if it was the last key in it and the second parameter is True.
        """

    def DeleteGroup(self, key: str) -> bool:
        """ Delete the group (with all subgroups).
        """

    def DisableAutoSave(self) -> None:
        """ Prevent this object from saving data to the disk file when it is destroyed.
        """

    def EnableAutoSave(self) -> None:
        """ Enables saving data to the disk file when this object is destroyed.
        """

    def Flush(self, bCurrentOnly: bool=False) -> bool:
        """ Permanently writes all changes (otherwise, theyâre only written from objectâs destructor).
        """

    @staticmethod
    def GetGlobalFileName(szFile: str) -> str:
        """ szFile (string) â
        """

    @staticmethod
    def GetLocalFileName(szFile, style=0) -> str:
        """ szFile (string) â
        """

    def GetNumberOfEntries(self, bRecursive: bool=False) -> int:
        """ Get number of entries in the current group.
        """

    def GetNumberOfGroups(self, bRecursive: bool=False) -> int:
        """ Get number of entries/subgroups in the current group, with or without its subgroups.
        """

    def GetPath(self) -> str:
        """ Retrieve the current path (always as absolute path).
        """

    def HasEntry(self, strName: str) -> bool:
        """ strName (string) â
        """

    def HasGroup(self, strName: str) -> bool:
        """ strName (string) â
        """

    def RenameEntry(self, oldName, newName) -> bool:
        """ Renames an entry in the current group.
        """

    def RenameGroup(self, oldName, newName) -> bool:
        """ Renames a subgroup of the current group.
        """

    def Save(self, os) -> bool:
        """ Saves all config data to the given stream, returns True if data was saved successfully or False on error.
        """

    def SetPath(self, strPath: str) -> None:
        """ Set current path: if the first character is â/â, it is the absolute path, otherwise it is a relative path.
        """

    def SetUmask(self, mode: int) -> None:
        """ Allows setting the mode to be used for the config file creation.
        """



class FileCtrl(Control):
    """ This control allows the user to select a file.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, defaultDirectory="", defaultFilename="", wildCard=FileSelectorDefaultWildcardStr, style=FC_DEFAULT_STYLE, pos=DefaultPosition, size=DefaultSize, name=FileCtrlNameStr) -> bool:
        """ Create function for two-step construction.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetDirectory(self) -> str:
        """ Returns the current directory of the file control (i.e. the directory shown by it).
        """

    def GetFilename(self) -> str:
        """ Returns the currently selected filename.
        """

    def GetFilenames(self) -> list[str]:
        """ Returns a list of filenames selected in the control.  This function
should only be used with controls which have the wx.``wx.FC_MULTIPLE`` style,
use GetFilename for the others.
        """

    def GetFilterIndex(self) -> int:
        """ Returns the zero-based index of the currently selected filter.
        """

    def GetPath(self) -> str:
        """ Returns the full path (directory and filename) of the currently selected file.
        """

    def GetPaths(self) -> list[str]:
        """ Returns a list of the full paths (directory and filename) of the files
chosen. This function should only be used with controlss which have
the wx.``wx.FC_MULTIPLE`` style, use GetPath for the others.
        """

    def GetWildcard(self) -> str:
        """ Returns the current wildcard.
        """

    def SetDirectory(self, directory: str) -> bool:
        """ Sets(changes) the current directory displayed in the control.
        """

    def SetFilename(self, filename: str) -> bool:
        """ Selects a certain file.
        """

    def SetFilterIndex(self, filterIndex: int) -> None:
        """ Sets the current filter index, starting from zero.
        """

    def SetPath(self, path: str) -> bool:
        """ Changes to a certain directory and selects a certain file.
        """

    def SetWildcard(self, wildCard: str) -> None:
        """ Sets the wildcard, which can contain multiple file types, for example: âBMP files (.bmp)|.bmp|GIF files (.gif)|.gifâ.
        """

    def ShowHidden(self, show: bool) -> None:
        """ Sets whether hidden files and folders are shown or not.
        """

FC_DEFAULT_STYLE: int  #  The default style: int  #  wx.FC_OPEN
FC_OPEN: int  #  Creates an file control suitable for opening files. Cannot be combined with wx.FC_SAVE.
FC_SAVE: int  #  Creates an file control suitable for saving files. Cannot be combined with wx.FC_OPEN.
FC_MULTIPLE: int  #  For open control only, Allows selecting multiple files. Cannot be combined with wx.FC_SAVE
FC_NOSHOWHIDDEN: int  #  Hides the âShow Hidden Filesâ checkbox (Generic only) ^^
EVT_FILECTRL_FILEACTIVATED: int  #  The user activated a file(by double-clicking or pressing Enter)
EVT_FILECTRL_SELECTIONCHANGED: int  #  The user changed the current selection(by selecting or deselecting a file)
EVT_FILECTRL_FOLDERCHANGED: int  #  The current folder of the file control has been changed
EVT_FILECTRL_FILTERCHANGED: int  #  The current file filter of the file control has been changed.
FC_DEFAULT_STYLE: int
FC_OPEN: int
FC_OPEN: int
FC_SAVE: int
FC_SAVE: int
FC_OPEN: int
FC_MULTIPLE: int
FC_SAVE: int
FC_NOSHOWHIDDEN: int


class FileCtrlEvent(CommandEvent):
    """ A file control event holds information about events associated with
FileCtrl objects.
    """
    def __init__(self, type, evtObject, id) -> None:
        """ Constructor.
        """

    def GetDirectory(self) -> str:
        """ Returns the current directory.
        """

    def GetFile(self) -> str:
        """ Returns the file selected (assuming it is only one file).
        """

    def GetFiles(self) -> list[str]:
        """ Returns the files selected.
        """

    def GetFilterIndex(self) -> int:
        """ Returns the current file filter index.
        """

    def SetDirectory(self, directory: str) -> None:
        """ Sets the directory of this event.
        """

    def SetFiles(self, files: list[str]) -> None:
        """ Sets the files changed by this event.
        """

    def SetFilterIndex(self, index: int) -> None:
        """ Sets the filter index changed by this event.
        """

EVT_FILECTRL_FILEACTIVATED: int  #  The user activated a file(by double-clicking or pressing Enter)
EVT_FILECTRL_SELECTIONCHANGED: int  #  The user changed the current selection(by selecting or deselecting a file)
EVT_FILECTRL_FOLDERCHANGED: int  #  The current folder of the file control has been changed
EVT_FILECTRL_FILTERCHANGED: int  #  The current file filter of the file control has been changed ^^


class FileDataObject(DataObjectSimple):
    """ FileDataObject is a specialization of DataObject for file names.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def AddFile(self, file: str) -> None:
        """ Adds a file to the file list represented by this data object (Windows only).
        """

    def GetAllFormats(self, dir=DataObject.Get) -> None:
        """ Returns a list of wx.DataFormat objects which this data object
supports transferring in the given direction.
        """

    def GetFilenames(self) -> list[str]:
        """ Returns the array of file names.
        """

    def SetData(self, format, buf) -> bool:
        """ bool
        """



class FileDialog(Dialog):
    """ This class represents the file chooser dialog.
    """
    def __init__(self, parent, message=FileSelectorPromptStr, defaultDir="", defaultFile="", wildcard=FileSelectorDefaultWildcardStr, style=FD_DEFAULT_STYLE, pos=DefaultPosition, size=DefaultSize, name=FileDialogNameStr) -> None:
        """ Constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetCurrentlySelectedFilename(self) -> str:
        """ Returns the path of the file currently selected in dialog.
        """

    def GetCurrentlySelectedFilterIndex(self) -> int:
        """ Returns the file type filter index currently selected in dialog.
        """

    def GetDirectory(self) -> str:
        """ Returns the default directory.
        """

    def GetExtraControl(self) -> 'Window':
        """ If functions SetExtraControlCreator   and ShowModal   were called, returns the extra window.
        """

    def GetFilename(self) -> str:
        """ Returns the default filename.
        """

    def GetFilenames(self) -> list[str]:
        """ Returns a list of filenames chosen in the dialog.  This function
should only be used with the dialogs which have wx.``MULTIPLE`` style,
use GetFilename for the others.
        """

    def GetFilterIndex(self) -> int:
        """ Returns the index into the list of filters supplied, optionally, in the wildcard parameter.
        """

    def GetMessage(self) -> str:
        """ Returns the message that will be displayed on the dialog.
        """

    def GetPath(self) -> str:
        """ Returns the full path (directory and filename) of the selected file.
        """

    def GetPaths(self) -> list[str]:
        """ Returns a list of the full paths of the files chosen. This function
should only be used with the dialogs which have wx.``MULTIPLE`` style, use
GetPath for the others.
        """

    def GetWildcard(self) -> str:
        """ Returns the file dialog wildcard.
        """

    def SetCustomizeHook(self, customizeHook: 'FileDialogCustomizeHook') -> bool:
        """ Set the hook to be used for customizing the dialog contents.
        """

    def SetDirectory(self, directory: str) -> None:
        """ Sets the default directory.
        """

    def SetFilename(self, setfilename: str) -> None:
        """ Sets the default filename.
        """

    def SetFilterIndex(self, filterIndex: int) -> None:
        """ Sets the default filter index, starting from zero.
        """

    def SetMessage(self, message: str) -> None:
        """ Sets the message that will be displayed on the dialog.
        """

    def SetPath(self, path: str) -> None:
        """ Sets the path (the combined directory and filename that will be returned when the dialog is dismissed).
        """

    def SetWildcard(self, wildCard: str) -> None:
        """ Sets the wildcard, which can contain multiple file types, for example: âBMP files (.bmp)|.bmp|GIF files (.gif)|.gifâ.
        """

    def ShowModal(self) -> int:
        """ Shows the dialog, returning  ID_OK   if the user pressed wx.OK, and   ID_CANCEL   otherwise.
        """

FD_DEFAULT_STYLE: int  #  Equivalent to  FD_OPEN .
FD_OPEN: int  #  This is an open dialog; usually this means that the default buttonâs label of the dialog is âOpenâ. Cannot be combined with  FD_SAVE .
FD_SAVE: int  #  This is a save dialog; usually this means that the default buttonâs label of the dialog is âSaveâ. Cannot be combined with  FD_OPEN .
FD_OVERWRITE_PROMPT: int  #  For save dialog only: int  #  prompt for a confirmation if a file will be overwritten. This style is always enabled on wxOSX and cannot be disabled.
FD_NO_FOLLOW: int  #  Directs the dialog to return the path and file name of the selected shortcut file, not its target as it does by default. Currently this flag is only implemented in wxMSW and wxOSX (where it prevents aliases from being resolved). The non-dereferenced link path is always returned, even without this flag, under Unix and so using it there doesnât do anything. This flag was added in wxWidgets 3.1.0.
FD_FILE_MUST_EXIST: int  #  For open dialog only: int  #  the user may only select files that actually exist. Notice that under macOS the file dialog with  FD_OPEN   style always behaves as if this style was specified, because it is impossible to choose a file that doesnât exist from a standard macOS file dialog.
FD_MULTIPLE: int  #  For open dialog only: int  #  allows selecting multiple files.
FD_CHANGE_DIR: int  #  Change the current working directory (when the dialog is dismissed) to the directory where the file(s) chosen by the user are.
FD_PREVIEW: int  #  Show the preview of the selected files (currently only supported by wxGTK).
FD_SHOW_HIDDEN: int  #  Show hidden files. This flag was added in wxWidgets 3.1.3 ^^
FD_DEFAULT_STYLE: int
FD_OPEN: int
FD_SAVE: int
FD_OVERWRITE_PROMPT: int
FD_NO_FOLLOW: int
FD_FILE_MUST_EXIST: int
FD_MULTIPLE: int
FD_CHANGE_DIR: int
FD_PREVIEW: int
FD_SHOW_HIDDEN: int
OK: int
NOT_FOUND: int
OK: int


class FileDialogButton(FileDialogCustomControl):
    """ Represents a custom button inside FileDialog.
    """


class FileDialogCheckBox(FileDialogCustomControl):
    """ Represents a custom checkbox inside FileDialog.
    """
    def GetValue(self) -> bool:
        """ Return True if the checkbox is checked.
        """

    def SetValue(self, value: bool) -> None:
        """ Check or uncheck the checkbox.
        """



class FileDialogChoice(FileDialogCustomControl):
    """ Represents a custom read-only combobox inside FileDialog.
    """
    def GetSelection(self) -> int:
        """ Return the index of the selected item, possibly wx.NOT_FOUND.
        """

    def SetSelection(self, n: int) -> None:
        """ Set the selection to the item with the given index.
        """

NOT_FOUND: int
NOT_FOUND: int


class FileDialogCustomControl(EvtHandler):
    """ The base class for all FileDialog custom controls.
    """
    def Disable(self) -> None:
        """ Disable this control.
        """

    def Enable(self, enable: bool=True) -> None:
        """ Enable or disable this control.
        """

    def Hide(self) -> None:
        """ Hide this control.
        """

    def Show(self, show: bool=True) -> None:
        """ Show or hide this control.
        """



class FileDialogCustomize:
    """ Used with FileDialogCustomizeHook to add custom controls to
FileDialog.
    """
    def AddButton(self, label: str) -> 'FileDialogButton':
        """ Add a button with the specified label.
        """

    def AddCheckBox(self, label: str) -> 'FileDialogCheckBox':
        """ Add a checkbox with the specified label.
        """

    def AddChoice(self, strings: list[str]) -> 'FileDialogChoice':
        """ Add a read-only combobox with the specified contents.
        """

    def AddRadioButton(self, label: str) -> 'FileDialogRadioButton':
        """ Add a radio button with the specified label.
        """

    def AddStaticText(self, label: str) -> 'FileDialogStaticText':
        """ Add a static text with the given contents.
        """

    def AddTextCtrl(self, label: str="") -> 'FileDialogTextCtrl':
        """ Add a text control with an optional label preceding it.
        """



class FileDialogCustomizeHook:
    """ Base class for customization hooks used with FileDialog.
    """
    def AddCustomControls(self, customizer: 'FileDialogCustomize') -> None:
        """ Must be overridden to add custom controls to the dialog using the provided customizer object.
        """

    def TransferDataFromCustomControls(self) -> None:
        """ Should typically be overridden to save the values of the custom controls when the dialog is accepted.
        """

    def UpdateCustomControls(self) -> None:
        """ May be overridden to update the custom controls whenever something changes in the dialog.
        """



class FileDialogRadioButton(FileDialogCustomControl):
    """ Represents a custom radio button inside FileDialog.
    """
    def GetValue(self) -> bool:
        """ Return True if the radio button is selected.
        """

    def SetValue(self, value: bool) -> None:
        """ Select the value of the radio button.
        """



class FileDialogStaticText(FileDialogCustomControl):
    """ Represents a custom static text inside FileDialog.
    """
    def SetLabelText(self, text: str) -> None:
        """ Set the text shown in the label.
        """



class FileDialogTextCtrl(FileDialogCustomControl):
    """ Represents a custom text control inside FileDialog.
    """
    def GetValue(self) -> str:
        """ Get the current value entered into the control.
        """

    def SetValue(self, text: str) -> None:
        """ Set the current control value.
        """



class FileDirPickerEvent(CommandEvent):
    """ This event class is used for the events generated by FilePickerCtrl
and by DirPickerCtrl.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetPath(self) -> str:
        """ Retrieve the absolute path of the file/directory the user has just selected.
        """

    def SetPath(self, path: str) -> None:
        """ Set the absolute path of the file/directory associated with the event.
        """

EVT_FILEPICKER_CHANGED: int  #  Generated whenever the selected file changes.
EVT_DIRPICKER_CHANGED: int  #  Generated whenever the selected directory changes. ^^


class FilePickerCtrl(PickerBase):
    """ This control allows the user to select a file.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, path="", message=FileSelectorPromptStr, wildcard=FileSelectorDefaultWildcardStr, pos=DefaultPosition, size=DefaultSize, style=FLP_DEFAULT_STYLE, validator=DefaultValidator, name=FilePickerCtrlNameStr) -> bool:
        """ Creates this widget with the given parameters.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetPath(self) -> str:
        """ Returns the absolute path of the currently selected file.
        """

    def SetInitialDirectory(self, dir: str) -> None:
        """ Set the directory to show when starting to browse for files.
        """

    def SetPath(self, filename: str) -> None:
        """ Sets the absolute path of the currently selected file.
        """

FLP_DEFAULT_STYLE: int  #  The default style: int  #  includes wx.FLP_OPEN | wx.FLP_FILE_MUST_EXIST and, under wxMSW and wxOSX, wx.FLP_USE_TEXTCTRL.
FLP_USE_TEXTCTRL: int  #  Creates a text control to the left of the picker button which is completely managed by the   wx.FilePickerCtrl  and which can be used by the user to specify a path (see SetPath). The text control is automatically synchronized with buttonâs value. Use functions defined in   wx.PickerBase  to modify the text control.
FLP_OPEN: int  #  Creates a picker which allows the user to select a file to open.
FLP_SAVE: int  #  Creates a picker which allows the user to select a file to save.
FLP_OVERWRITE_PROMPT: int  #  Can be combined with wx.FLP_SAVE only: int  #  ask confirmation to the user before selecting a file.
FLP_FILE_MUST_EXIST: int  #  Can be combined with wx.FLP_OPEN only: int  #  the file selected in the popup   wx.FileDialog  must be an existing file. Notice that it still remains possible for the user to enter a non-existent file name in the text control if  FLP_USE_TEXTCTRL   is also used, this flag is a hint for the user rather than a guarantee that the selected file does exist for the program.
FLP_CHANGE_DIR: int  #  Change current working directory on each user file selection change.
FLP_SMALL: int  #  Use smaller version of the control with a small ââ¦â button instead of the normal âBrowseâ one. This flag is new since wxWidgets 2.9.3. ^^
EVT_FILEPICKER_CHANGED: int  #  The user changed the file selected in the control either using the button or using text control (see wx.FLP_USE_TEXTCTRL; note that in this case the event is fired only if the userâs input is valid, e.g. an existing file path if wx.FLP_FILE_MUST_EXIST was given). ^^
FLP_DEFAULT_STYLE: int
FLP_OPEN: int
FLP_FILE_MUST_EXIST: int
FLP_USE_TEXTCTRL: int
FLP_USE_TEXTCTRL: int
FLP_OPEN: int
FLP_SAVE: int
FLP_OVERWRITE_PROMPT: int
FLP_SAVE: int
FLP_FILE_MUST_EXIST: int
FLP_OPEN: int
FLP_CHANGE_DIR: int
FLP_SMALL: int
FLP_USE_TEXTCTRL: int
FLP_FILE_MUST_EXIST: int


class FileDropTarget(DropTarget):
    """ This is a drop target which accepts files (dragged from File Manager
or Explorer).
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def OnDrop(self, x, y) -> bool:
        """ See wx.DropTarget.OnDrop .
        """

    def OnDropFiles(self, x, y, filenames) -> bool:
        """ Override this function to receive dropped files.
        """



class FileHistory(Object):
    """ The FileHistory encapsulates a user interface convenience, the list
of most recently visited files as shown on a menu (usually the File
menu).
    """
    def __init__(self, maxFiles=9, idBase=ID_FILE1) -> None:
        """ Constructor.
        """

    def AddFileToHistory(self, filename: str) -> None:
        """ Adds a file to the file history list, if the object has a pointer to an appropriate file menu.
        """

    def AddFilesToMenu(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetBaseId(self) -> int:
        """ Returns the base identifier for the range used for appending items.
        """

    def GetCount(self) -> int:
        """ Returns the number of files currently stored in the file history.
        """

    def GetHistoryFile(self, index: int) -> str:
        """ Returns the file at this index (zero-based).
        """

    def GetMaxFiles(self) -> int:
        """ Returns the maximum number of files that can be stored.
        """

    def GetMenuPathStyle(self) -> 'FileHistoryMenuPathStyle':
        """ Get the current style of the menu item labels.
        """

    def GetMenus(self) -> FileHistoryMenuList:
        """ Returns the list of menus that are managed by this file history object.
        """

    def Load(self, config: 'ConfigBase') -> None:
        """ Loads the file history from the given config object.
        """

    def RemoveFileFromHistory(self, i: int) -> None:
        """ Removes the specified file from the history.
        """

    def RemoveMenu(self, menu: 'Menu') -> None:
        """ Removes this menu from the list of those managed by this object.
        """

    def Save(self, config: 'ConfigBase') -> None:
        """ Saves the file history into the given config object.
        """

    def SetBaseId(self, baseId: int) -> None:
        """ Sets the base identifier for the range used for appending items.
        """

    def SetMenuPathStyle(self, style: FileHistoryMenuPathStyle) -> None:
        """ Set the style of the menu item labels.
        """

    def UseMenu(self, menu: 'Menu') -> None:
        """ Adds this menu to the list of those menus that are managed by this file history object.
        """

ID_FILE1: int


class FileSystem(Object):
    """ This class provides an interface for opening files on different file
systems.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    @staticmethod
    def AddHandler(handler: 'FileSystemHandler') -> None:
        """ This static function adds new handler into the list of handlers (see   wx.FileSystemHandler) which provide access to virtual FS.
        """

    def ChangePathTo(self, location, is_dir=False) -> None:
        """ Sets the current location.
        """

    @staticmethod
    def FileNameToURL(filename: str) -> str:
        """ Converts a FileName       into an URL.
        """

    def FindFileInPath(self, pStr, path, file) -> bool:
        """ Looks for the file with the given name file  in a colon or semi-colon (depending on the current platform) separated list of directories in path.
        """

    def FindFirst(self, wildcard, flags=0) -> str:
        """ Works like FindFirstFile .
        """

    def FindNext(self) -> str:
        """ Returns the next filename that matches the parameters passed to FindFirst .
        """

    def GetPath(self) -> str:
        """ Returns the actual path (set by wx.FileSystem.ChangePathTo ).
        """

    @staticmethod
    def HasHandlerForPath(location: str) -> bool:
        """ This static function returns True if there is a registered handler which can open the given location.
        """

    def OpenFile(self, location, flags=FS_READ) -> 'FSFile':
        """ Opens the file and returns a pointer to a   wx.FSFile  object or None if failed.
        """

    @staticmethod
    def RemoveHandler(handler: 'FileSystemHandler') -> 'FileSystemHandler':
        """ Remove a filesystem handler from the list of handlers.
        """

    @staticmethod
    def URLToFileName(url: str) -> str:
        """ Converts URL into a well-formed filename.
        """

FS_READ: int
FS_SEEKABLE: int


class FileSystemHandler(Object):
    """ Classes derived from FileSystemHandler are used to access virtual
file systems.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def CanOpen(self, location: str) -> bool:
        """ Returns True if the handler is able to open this file.
        """

    def FindFirst(self, wildcard, flags=0) -> str:
        """ Works like FindFirstFile .
        """

    def FindNext(self) -> str:
        """ Returns next filename that matches parameters passed to wx.FileSystem.FindFirst .
        """

    @staticmethod
    def GetAnchor(location: str) -> str:
        """ Returns the anchor if present in the location.
        """

    @staticmethod
    def GetLeftLocation(location: str) -> str:
        """ Returns the left location string extracted from location.
        """

    @staticmethod
    def GetMimeTypeFromExt(location: str) -> str:
        """ Returns the MIME type based on extension  of location.
        """

    @staticmethod
    def GetProtocol(location: str) -> str:
        """ Returns the protocol string extracted from location.
        """

    @staticmethod
    def GetRightLocation(location: str) -> str:
        """ Returns the right location string extracted from location.
        """

    def OpenFile(self, fs, location) -> 'FSFile':
        """ Opens the file and returns   wx.FSFile  pointer or None if failed.
        """



class FileSystemWatcher(EvtHandler):
    """ The FileSystemWatcher class allows receiving notifications of file
system changes.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def Add(self, path, events=FSW_EVENT_ALL) -> bool:
        """ Adds path  to currently watched files.
        """

    def AddTree(self, path, events=FSW_EVENT_ALL, filter="") -> bool:
        """ This is the same as Add , but also recursively adds every file/directory in the tree rooted at path.
        """

    def GetWatchedPaths(self, paths: list[str]) -> int:
        """ Retrieves all watched paths and places them in paths.
        """

    def GetWatchedPathsCount(self) -> int:
        """ Returns the number of currently watched paths.
        """

    def Remove(self, path: str) -> bool:
        """ Removes path  from the list of watched paths.
        """

    def RemoveAll(self) -> bool:
        """ Clears the list of currently watched paths.
        """

    def RemoveTree(self, path: str) -> bool:
        """ This is the same as Remove , but also removes every file/directory belonging to the tree rooted at path.
        """

    def SetOwner(self, handler: 'EvtHandler') -> None:
        """ Associates the file system watcher with the given handler  object.
        """



class FileSystemWatcherEvent(Event):
    """ A class of events sent when a file system event occurs.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Clone(self) -> 'Event':
        """ wx.Event
        """

    def GetChangeType(self) -> int:
        """ Returns the type of file system change that occurred.
        """

    def GetErrorDescription(self) -> str:
        """ Return a description of the warning or error if this is an error event.
        """

    def GetNewPath(self) -> str:
        """ Returns the new path of the renamed file/directory if this is a rename event.
        """

    def GetPath(self) -> str:
        """ Returns the path at which the event occurred.
        """

    def GetWarningType(self) -> 'FSWWarningType':
        """ Return the type of the warning if this event is a warning one.
        """

    def IsError(self) -> bool:
        """ Returns  true   if this error is an error event.
        """

    def ToString(self) -> str:
        """ Returns a String       describing an event, useful for logging, debugging or testing.
        """



class FileTranslationsLoader(TranslationsLoader):
    """ Standard TranslationsLoader implementation.
    """
    @staticmethod
    def AddCatalogLookupPathPrefix(prefix: str) -> None:
        """ Add a prefix to the catalog lookup path: the message catalog files will be looked up under prefix/lang/LC_MESSAGES and prefix/lang directories (in this order).
        """



class TranslationsLoader:
    """ Abstraction of translations discovery and loading.
    """
    def __init__(self) -> None:
        """ Trivial default constructor.
        """

    def GetAvailableTranslations(self, domain: str) -> list[str]:
        """ Implements wx.Translations.GetAvailableTranslations .
        """

    def LoadCatalog(self, domain, lang) -> MsgCatalog:
        """ Called to load requested catalog.
        """



class FileType:
    """ This class holds information about a given file type.
    """
    def __init__(self, ftInfo: 'FileTypeInfo') -> None:
        """ Copy constructor.
        """

    @staticmethod
    def ExpandCommand(command, params) -> str:
        """ This function is primarily intended for GetOpenCommand and GetPrintCommand usage but may be also used by the application directly if, for example, you want to use some non-default command to open the file.
        """

    def GetAllCommands(self, params: FileType.MessageParameters) -> tuple:
        """ Returns a tuple containing the verbs and commands arrays, corresponding for the registered information for this mime type.
        """

    def GetDescription(self) -> str:
        """ Returns a brief description for this file type: for example, âtext documentâ for
the âtext/plainâ MIME type.
        """

    def GetExpandedCommand(self, verb, params) -> str:
        """ The returned string is the command to be executed in order to open/print/edit the file of the given type.
        """

    def GetExtensions(self) -> list[str]:
        """ Returns all extensions associated with this file type: for
example, it may contain the following two elements for the MIME
type âtext/htmlâ (notice the absence of the leading dot): âhtmlâ
and âhtmâ.
        """

    def GetIcon(self) -> 'Icon':
        """ Return the icon associated with this mime type, if any.
        """

    def GetIconInfo(self) -> Any:
        """ Returns a tuple containing the Icon for this file type, the file where the
icon is found, and the index of the image in that file, if applicable.
        """

    def GetIconLocation(self) -> 'IconLocation':
        """ Returns a wx.IconLocation that can be used to fetch the icon for this mime type.
        """

    def GetMimeType(self) -> str:
        """ Returns full MIME type specification for this file type: for example, âtext/plainâ.
        """

    def GetMimeTypes(self) -> list[str]:
        """ Same as GetMimeType but returns a list of types.  This will usually contain
only one item, but sometimes, such as on Unix with KDE more than one type
if there are differences between KDE< mailcap and mime.types.
        """

    def GetOpenCommand(self, *args, **kw) -> str:
        """ Overloaded Implementations:
        """

    def GetPrintCommand(self, params) -> str:
        """ Returns the command which must be executed (see Execute()) in order to
print the file of the given type. The name of the file is retrieved from
the MessageParameters class.
        """



class FileTypeInfo:
    """ Container of information about FileType.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddExtension(self, ext: str) -> None:
        """ Add another extension associated with this file type.
        """

    def GetDescription(self) -> str:
        """ Get the long, user visible description.
        """

    def GetExtensions(self) -> list[str]:
        """ Get the array of all extensions.
        """

    def GetExtensionsCount(self) -> int:
        """ Get the number of extensions.
        """

    def GetIconFile(self) -> str:
        """ Get the icon filename.
        """

    def GetIconIndex(self) -> int:
        """ Get the index of the icon within the icon file.
        """

    def GetMimeType(self) -> str:
        """ Get the MIME type.
        """

    def GetOpenCommand(self) -> str:
        """ Get the open command.
        """

    def GetPrintCommand(self) -> str:
        """ Get the print command.
        """

    def GetShortDesc(self) -> str:
        """ Get the short description (only used under Win32 so far)
        """

    def SetDescription(self, description: str) -> None:
        """ Set the file type description.
        """

    def SetIcon(self, iconFile, iconIndex=0) -> None:
        """ Set the icon information.
        """

    def SetOpenCommand(self, command: str) -> None:
        """ Set the command to be used for opening files of this type.
        """

    def SetPrintCommand(self, command: str) -> None:
        """ Set the command to be used for printing files of this type.
        """

    def SetShortDesc(self, shortDesc: str) -> None:
        """ Set the short description for the files of this type.
        """



class FilterFSHandler(FileSystemHandler):
    """ Filter file system handler.
    """
    def __init__(self) -> None:
        """ 
        """



class FindDialogEvent(CommandEvent):
    """ FindReplaceDialog events.
    """
    def __init__(self, commandType=wxEVT_NULL, id=0) -> None:
        """ Constructor used by wxWidgets only.
        """

    def GetDialog(self) -> 'FindReplaceDialog':
        """ Return the pointer to the dialog which generated this event.
        """

    def GetFindString(self) -> str:
        """ Return the string to find (never empty).
        """

    def GetFlags(self) -> int:
        """ Get the currently selected flags: this is the combination of the   wx.FindReplaceFlags  enumeration values.
        """

    def GetReplaceString(self) -> str:
        """ Return the string to replace the search string with (only for replace and replace all events).
        """

EVT_FIND: int  #  Find button was pressed in the dialog.
EVT_FIND_NEXT: int  #  Find next button was pressed in the dialog.
EVT_FIND_REPLACE: int  #  Replace button was pressed in the dialog.
EVT_FIND_REPLACE_ALL: int  #  Replace all button was pressed in the dialog.
EVT_FIND_CLOSE: int  #  The dialog is being destroyed, any pointers to it cannot be used any longer. ^^


class FindReplaceDialog(Dialog):
    """ FindReplaceDialog is a standard modeless dialog which is used to
allow the user to search for some text (and possibly replace it with
something else).
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, data, title="", style=0) -> bool:
        """ Creates the dialog; use wx.Window.Show   to show it on screen.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetData(self) -> 'FindReplaceData':
        """ Get the   wx.FindReplaceData  object used by this dialog.
        """



class FindReplaceData(Object):
    """ FindReplaceData holds the data for FindReplaceDialog.
    """
    def __init__(self, flags: 'int'=0) -> None:
        """ Constructor initializes the flags to default value (0).
        """

    def GetFindString(self) -> str:
        """ Get the string to find.
        """

    def GetFlags(self) -> int:
        """ Get the combination of  FindReplaceFlags   values.
        """

    def GetReplaceString(self) -> str:
        """ Get the replacement string.
        """

    def SetFindString(self, str: str) -> None:
        """ Set the string to find (used as initial value by the dialog).
        """

    def SetFlags(self, flags: 'int') -> None:
        """ Set the flags to use to initialize the controls of the dialog.
        """

    def SetReplaceString(self, str: str) -> None:
        """ Set the replacement string (used as initial value by the dialog).
        """



class FlexGridSizer(GridSizer):
    """ A flex grid sizer is a sizer which lays out its children in a two-
dimensional table with all table fields in one row having the same
height and all fields in one column having the same width, but all
rows or all columns are not necessarily the same height or width as in
the GridSizer.
    """
    def __init__(self, *args, **kw) -> None:
        """ wx.FlexGridSizer  constructors.
        """

    def AddGrowableCol(self, idx, proportion=0) -> None:
        """ Specifies that column idx  (starting from zero) should be grown if there is extra space available to the sizer.
        """

    def AddGrowableRow(self, idx, proportion=0) -> None:
        """ Specifies that row idx (starting from zero) should be grown if there is extra space available to the sizer.
        """

    def CalcMin(self) -> 'Size':
        """ This method is abstract and has to be overwritten by any derived class.
        """

    def GetColWidths(self) -> list[int]:
        """ Returns a read-only array containing the widths of the columns in the sizer.
        """

    def GetFlexibleDirection(self) -> int:
        """ Returns a   wx.Orientation  value that specifies whether the sizer flexibly resizes its columns, rows, or both (default).
        """

    def GetNonFlexibleGrowMode(self) -> 'FlexSizerGrowMode':
        """ Returns the value that specifies how the sizer grows in the ânon-flexibleâ direction if there is one.
        """

    def GetRowHeights(self) -> list[int]:
        """ Returns a read-only array containing the heights of the rows in the sizer.
        """

    def IsColGrowable(self, idx: int) -> bool:
        """ Returns True if column idx  is growable.
        """

    def IsRowGrowable(self, idx: int) -> bool:
        """ Returns True if row idx  is growable.
        """

    def RemoveGrowableCol(self, idx: int) -> None:
        """ Specifies that the idx  column index is no longer growable.
        """

    def RemoveGrowableRow(self, idx: int) -> None:
        """ Specifies that the idx  row index is no longer growable.
        """

    def RepositionChildren(self, minSize: Union[tuple[int, int], 'Size']) -> None:
        """ Method which must be overridden in the derived sizer classes.
        """

    def SetFlexibleDirection(self, direction: int) -> None:
        """ Specifies whether the sizer should flexibly resize its columns, rows, or both.
        """

    def SetNonFlexibleGrowMode(self, mode: FlexSizerGrowMode) -> None:
        """ Specifies how the sizer should grow in the non-flexible direction if there is one (so SetFlexibleDirection   must have been called previously).
        """

VERTICAL: int
HORIZONTAL: int
BOTH: int
FLEX_GROWMODE_NONE: int
FLEX_GROWMODE_SPECIFIED: int
FLEX_GROWMODE_ALL: int


class GridSizer(Sizer):
    """ A grid sizer is a sizer which lays out its children in a two-
dimensional table with all table fields having the same size, i.e.
    """
    def __init__(self, *args, **kw) -> None:
        """ wx.GridSizer  constructors.
        """

    def CalcMin(self) -> 'Size':
        """ This method is abstract and has to be overwritten by any derived class.
        """

    def CalcRowsCols(self) -> None:
        """ Calculates how many rows and columns will be in the sizer based
on the current number of items and also the rows, cols specified
in the constructor.
        """

    def GetCols(self) -> int:
        """ Returns the number of columns that has been specified for the sizer.
        """

    def GetEffectiveColsCount(self) -> int:
        """ Returns the number of columns currently used by the sizer.
        """

    def GetEffectiveRowsCount(self) -> int:
        """ Returns the number of rows currently used by the sizer.
        """

    def GetHGap(self) -> int:
        """ Returns the horizontal gap (in pixels) between cells in the sizer.
        """

    def GetRows(self) -> int:
        """ Returns the number of rows that has been specified for the sizer.
        """

    def GetVGap(self) -> int:
        """ Returns the vertical gap (in pixels) between the cells in the sizer.
        """

    def RepositionChildren(self, minSize: Union[tuple[int, int], 'Size']) -> None:
        """ Method which must be overridden in the derived sizer classes.
        """

    def SetCols(self, cols: int) -> None:
        """ Sets the number of columns in the sizer.
        """

    def SetHGap(self, gap: int) -> None:
        """ Sets the horizontal gap (in pixels) between cells in the sizer.
        """

    def SetRows(self, rows: int) -> None:
        """ Sets the number of rows in the sizer.
        """

    def SetVGap(self, gap: int) -> None:
        """ Sets the vertical gap (in pixels) between the cells in the sizer.
        """



class FocusEvent(Event):
    """ A focus event is sent when a windowâs focus changes.
    """
    def __init__(self, eventType=wxEVT_NULL, id=0) -> None:
        """ Constructor.
        """

    def GetWindow(self) -> 'Window':
        """ Returns the window associated with this event, that is the window which had the focus before for the  wxEVT_SET_FOCUS   event and the window which is going to receive focus for the   wxEVT_KILL_FOCUS   one.
        """

    def SetWindow(self, win: 'Window') -> None:
        """ win (wx.Window) â
        """

EVT_SET_FOCUS: int  #  Process a  wxEVT_SET_FOCUS   event.
EVT_KILL_FOCUS: int  #  Process a  wxEVT_KILL_FOCUS   event. ^^


class Font(GDIObject):
    """ A font is an object which determines the appearance of text.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    @staticmethod
    def AddPrivateFont(filename: str) -> bool:
        """ Specify the name of a file containing a TrueType font to be made available to the current application.
        """

    def Bold(self) -> 'Font':
        """ Returns a bold version of this font.
        """

    @staticmethod
    def CanUsePrivateFont() -> bool:
        """ Returns True if this build of wxPython supports using AddPrivateFont.
        """

    def GetBaseFont(self) -> 'Font':
        """ Returns a font with the same face/size as the given one but with normal weight and style and not underlined nor stricken through.
        """

    @staticmethod
    def GetDefaultEncoding() -> int:
        """ Returns the current applicationâs default encoding.
        """

    def GetEncoding(self) -> int:
        """ Returns the encoding of this font.
        """

    def GetFaceName(self) -> str:
        """ Returns the face name associated with the font, or the empty string if there is no face information.
        """

    def GetFamily(self) -> int:
        """ Gets the font family if possible.
        """

    def GetFractionalPointSize(self) -> float:
        """ Gets the point size as a floating number.
        """

    def GetHFONT(self) -> None:
        """ Returns the fontâs native handle.
        """

    def GetNativeFontInfo(self) -> 'NativeFontInfo':
        """ Returns a font with the same face/size as the given one but with normal weight and style and not underlined nor stricken through.
        """

    def GetNativeFontInfoDesc(self) -> str:
        """ Returns the platform-dependent string completely describing this font.
        """

    def GetNativeFontInfoUserDesc(self) -> str:
        """ Returns a user-friendly string for this font object.
        """

    def GetNumericWeight(self) -> int:
        """ Gets the font weight as an integer value.
        """

    @staticmethod
    def GetNumericWeightOf(weight: int) -> int:
        """ Get the raw weight value corresponding to the given symbolic constant.
        """

    def GetPangoFontDescription(self) -> None:
        """ Returns the fontâs native handle.
        """

    def GetPixelSize(self) -> 'Size':
        """ Gets the pixel size.
        """

    def GetPointSize(self) -> int:
        """ Gets the point size as an integer number.
        """

    def GetStrikethrough(self) -> bool:
        """ Returns True if the font is stricken-through, False otherwise.
        """

    def GetStyle(self) -> int:
        """ Gets the font style.
        """

    def GetUnderlined(self) -> bool:
        """ Returns True if the font is underlined, False otherwise.
        """

    def GetWeight(self) -> int:
        """ Gets the font weight.
        """

    def IsFixedWidth(self) -> bool:
        """ Returns True if the font is a fixed width (or monospaced) font, False if it is a proportional one or font is invalid.
        """

    def IsOk(self) -> bool:
        """ Returns True if this object is a valid font, False otherwise.
        """

    def Italic(self) -> 'Font':
        """ Returns an italic version of this font.
        """

    def Larger(self) -> 'Font':
        """ Returns a larger version of this font.
        """

    def MakeBold(self) -> 'Font':
        """ Changes this font to be bold.
        """

    def MakeItalic(self) -> 'Font':
        """ Changes this font to be italic.
        """

    def MakeLarger(self) -> 'Font':
        """ Changes this font to be larger.
        """

    def MakeSmaller(self) -> 'Font':
        """ Changes this font to be smaller.
        """

    def MakeStrikethrough(self) -> 'Font':
        """ Changes this font to be stricken-through.
        """

    def MakeUnderlined(self) -> 'Font':
        """ Changes this font to be underlined.
        """

    @staticmethod
    def New(*args, **kw) -> 'Font':
        """ This function takes the same parameters as the relative Font constructor  and returns a new font object allocated on the heap.
        """

    def OSXGetCGFont(self) -> None:
        """ Returns the fontâs native handle.
        """

    def Scale(self, x: float) -> 'Font':
        """ Changes the size of this font.
        """

    def Scaled(self, x: float) -> 'Font':
        """ Returns a scaled version of this font.
        """

    @staticmethod
    def SetDefaultEncoding(encoding: int) -> None:
        """ Sets the default font encoding.
        """

    def SetEncoding(self, encoding: int) -> None:
        """ Sets the encoding for this font.
        """

    def SetFaceName(self, faceName: str) -> bool:
        """ Sets the facename for the font.
        """

    def SetFamily(self, family: int) -> None:
        """ Sets the font family.
        """

    def SetFractionalPointSize(self, pointSize: float) -> None:
        """ Sets the font size in points.
        """

    def SetNativeFontInfo(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def SetNativeFontInfoUserDesc(self, info: str) -> bool:
        """ Creates the font corresponding to the given native font description string and returns True if the creation was successful.
        """

    def SetNumericWeight(self, weight: int) -> None:
        """ Sets the font weight using an integer value.
        """

    def SetPixelSize(self, pixelSize: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the pixel size.
        """

    def SetPointSize(self, pointSize: int) -> None:
        """ Sets the font size in points to an integer value.
        """

    def SetStrikethrough(self, strikethrough: bool) -> None:
        """ Sets strike-through attribute of the font.
        """

    def SetStyle(self, style: int) -> None:
        """ Sets the font style.
        """

    def SetSymbolicSize(self, size: FontSymbolicSize) -> None:
        """ Sets the font size using a predefined symbolic size name.
        """

    def SetSymbolicSizeRelativeTo(self, size, base) -> None:
        """ Sets the font size compared to the base font size.
        """

    def SetUnderlined(self, underlined: bool) -> None:
        """ Sets underlining.
        """

    def SetWeight(self, weight: int) -> None:
        """ Sets the font weight.
        """

    def Smaller(self) -> 'Font':
        """ Returns a smaller version of this font.
        """

    def Strikethrough(self) -> 'Font':
        """ Returns stricken-through version of this font.
        """

    def Underlined(self) -> 'Font':
        """ Returns underlined version of this font.
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """

    def _copyFrom(self, other) -> None:
        """ For internal use only.
        """

    def __ne__(self, item: Any) -> bool:
        """ Inequality operator.
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.
        """



class FontData(Object):
    """ This class holds a variety of information related to font dialogs.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def EnableEffects(self, enable: bool) -> None:
        """ Enables or disables âeffectsâ under Windows or generic only.
        """

    def GetAllowSymbols(self) -> bool:
        """ Under Windows, returns a flag determining whether symbol fonts can be selected.
        """

    def GetChosenFont(self) -> 'Font':
        """ Gets the font chosen by the user if the user pressed wx.OK ( wx.FontDialog.ShowModal   returned wx.ID_OK).
        """

    def GetColour(self) -> 'Colour':
        """ Gets the colour associated with the font dialog.
        """

    def GetEnableEffects(self) -> bool:
        """ Determines whether âeffectsâ are enabled under Windows.
        """

    def GetInitialFont(self) -> 'Font':
        """ Gets the font that will be initially used by the font dialog.
        """

    def GetRestrictSelection(self) -> int:
        """ Returns the state of the flags restricting the selection.
        """

    def GetShowHelp(self) -> bool:
        """ Returns True if the Help button will be shown (Windows only).
        """

    def RestrictSelection(self, flags: int) -> None:
        """ Restricts the selection to a subset of the available fonts.
        """

    def SetAllowSymbols(self, allowSymbols: bool) -> None:
        """ Under Windows, determines whether symbol fonts can be selected.
        """

    def SetChosenFont(self, font: 'Font') -> None:
        """ Sets the font that will be returned to the user (for internal use only).
        """

    def SetColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the colour that will be used for the font foreground colour.
        """

    def SetInitialFont(self, font: 'Font') -> None:
        """ Sets the font that will be initially used by the font dialog.
        """

    def SetRange(self, min, max) -> None:
        """ Sets the valid range for the font point size (Windows only).
        """

    def SetShowHelp(self, showHelp: bool) -> None:
        """ Determines whether the Help button will be displayed in the font dialog (Windows only).
        """

OK: int
ID_OK: int
OK: int
ID_OK: int


class FontDialog(Dialog):
    """ This class represents the font chooser dialog.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, *args, **kw) -> None:
        """ Creates the dialog if the   wx.FontDialog  object had been initialized using the default constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetFontData(self) -> 'FontData':
        """ Returns the font data  associated with the font dialog.
        """

    def ShowModal(self) -> int:
        """ Shows the dialog, returning  ID_OK   if the user pressed Ok, and   ID_CANCEL   otherwise.
        """

OK: int


class FontEnumerator:
    """ FontEnumerator enumerates either all available fonts on the system
or only the ones with given attributes - either only fixed-width
(suited for use in programs such as terminal emulators and the like)
or the fonts available in the given encoding).
    """
    def __init__(self) -> None:
        """ 
        """

    def EnumerateEncodings(self, font: str="") -> bool:
        """ Call OnFontEncoding   for each encoding supported by the given font - or for each encoding supported by at least some font if font  is not specified.
        """

    def EnumerateFacenames(self, encoding=FONTENCODING_SYSTEM, fixedWidthOnly=False) -> bool:
        """ Call OnFacename   for each font which supports given encoding (only if it is not  FONTENCODING_SYSTEM ) and is of fixed width (if  fixedWidthOnly  is True).
        """

    @staticmethod
    def GetEncodings(facename: str="") -> list[str]:
        """ Return array of strings containing all encodings found by EnumerateEncodings .
        """

    @staticmethod
    def GetFacenames(encoding=FONTENCODING_SYSTEM, fixedWidthOnly=False) -> list[str]:
        """ Return array of strings containing all facenames found by EnumerateFacenames .
        """

    @staticmethod
    def InvalidateCache() -> None:
        """ Invalidate cache used by some of the methods of this class internally.
        """

    @staticmethod
    def IsValidFacename(facename: str) -> bool:
        """ Returns True if the given string is valid face name, i.e.
        """

    def OnFacename(self, font: str) -> bool:
        """ Called by EnumerateFacenames   for each match.
        """

    def OnFontEncoding(self, font, encoding) -> bool:
        """ Called by EnumerateEncodings   for each match.
        """



class FontInfo:
    """ This class is a helper used for Font creation using named parameter
idiom: it allows specifying various Font attributes using the
chained calls to its clearly named methods instead of passing them in
the fixed order to Font constructors.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AllFlags(self, flags: int) -> 'FontInfo':
        """ Set all the font attributes at once.
        """

    def AntiAliased(self, antiAliased: bool=True) -> 'FontInfo':
        """ Set anti-aliasing flag.
        """

    def Bold(self, bold: bool=True) -> 'FontInfo':
        """ Use a bold version of the font.
        """

    def Encoding(self, encoding: int) -> 'FontInfo':
        """ Set the font encoding to use.
        """

    def FaceName(self, faceName: str) -> 'FontInfo':
        """ Set the font face name to use.
        """

    def Family(self, family: int) -> 'FontInfo':
        """ Set the font family.
        """

    @staticmethod
    def GetWeightClosestToNumericValue(numWeight: int) -> int:
        """ Get the symbolic weight closest to the given raw weight value.
        """

    def Italic(self, italic: bool=True) -> 'FontInfo':
        """ Use an italic version of the font.
        """

    def Light(self, light: bool=True) -> 'FontInfo':
        """ Use a lighter version of the font.
        """

    def Slant(self, slant: bool=True) -> 'FontInfo':
        """ Use a slanted version of the font.
        """

    def Strikethrough(self, strikethrough: bool=True) -> 'FontInfo':
        """ Use a strike-through version of the font.
        """

    def Style(self, style: int) -> 'FontInfo':
        """ Specify the style of the font using one of FontStyle constants.
        """

    def Underlined(self, underlined: bool=True) -> 'FontInfo':
        """ Use an underlined version of the font.
        """

    def Weight(self, weight: int) -> 'FontInfo':
        """ Specify the weight of the font.
        """



class FontList:
    """ A font list is a list containing all fonts which have been created.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def FindOrCreateFont(self, *args, **kw) -> 'Font':
        """ Overloaded Implementations:
        """



class FontMapper:
    """ FontMapper manages user-definable correspondence between logical
font names and the fonts present on the machine.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def CharsetToEncoding(self, charset, interactive=True) -> int:
        """ Returns the encoding for the given charset (in the form of RFC 2046) or  FONTENCODING_SYSTEM   if couldnât decode it.
        """

    @staticmethod
    def Get() -> 'FontMapper':
        """ Get the current font mapper object.
        """

    @staticmethod
    def GetAllEncodingNames(encoding) -> list[str]:
        """ Returns the array of all possible names for the given encoding. If it
isnât empty, the first name in it is the canonical encoding name,
i.e. the same string as returned by GetEncodingName()
        """

    def GetAltForEncoding(self, encoding, facename="", interactive=True) -> tuple:
        """ Find an alternative for the given encoding (which is supposed to not be available on this system).
        """

    @staticmethod
    def GetEncoding(n: int) -> int:
        """ Returns the n-th  supported encoding.
        """

    @staticmethod
    def GetEncodingDescription(encoding: int) -> str:
        """ Return user-readable string describing the given encoding.
        """

    @staticmethod
    def GetEncodingFromName(encoding: str) -> int:
        """ Return the encoding corresponding to the given internal name.
        """

    @staticmethod
    def GetEncodingName(encoding: int) -> str:
        """ Return internal string identifier for the encoding (see also wx.FontMapper.GetEncodingDescription ).
        """

    @staticmethod
    def GetSupportedEncodingsCount() -> int:
        """ Returns the number of the font encodings supported by this class.
        """

    def IsEncodingAvailable(self, encoding, facename="") -> bool:
        """ Check whether given encoding is available in given face or not.
        """

    @staticmethod
    def Set(mapper: 'FontMapper') -> 'FontMapper':
        """ Set the current font mapper object and return previous one (may be None).
        """

    def SetConfigPath(self, prefix: str) -> None:
        """ Set the root config path to use (should be an absolute path).
        """

    def SetDialogParent(self, parent: 'Window') -> None:
        """ The parent window for modal dialogs.
        """

    def SetDialogTitle(self, title: str) -> None:
        """ The title for the dialogs (note that default is quite reasonable).
        """



class FontMetrics:
    """ Simple collection of various font metrics.
    """
    def __init__(self) -> None:
        """ Constructor initializes all fields to 0.
        """



class FontPickerCtrl(PickerBase):
    """ This control allows the user to select a font.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, font=NullFont, pos=DefaultPosition, size=DefaultSize, style=FNTP_DEFAULT_STYLE, validator=DefaultValidator, name=FontPickerCtrlNameStr) -> bool:
        """ Creates this widget with given parameters.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetMaxPointSize(self) -> int:
        """ Returns the maximum point size value allowed for the user-chosen font.
        """

    def GetMinPointSize(self) -> int:
        """ Returns the minimum point size value allowed for the user-chosen font.
        """

    def GetSelectedColour(self) -> 'Colour':
        """ Returns the currently selected colour.
        """

    def GetSelectedFont(self) -> 'Font':
        """ Returns the currently selected font.
        """

    def SetMaxPointSize(self, max: int) -> None:
        """ Sets the maximum point size value allowed for the user-chosen font.
        """

    def SetMinPointSize(self, min: int) -> None:
        """ Sets the minimum point size value allowed for the user-chosen font.
        """

    def SetSelectedColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the font colour.
        """

    def SetSelectedFont(self, font: 'Font') -> None:
        """ Sets the currently selected font.
        """

FNTP_DEFAULT_STYLE: int  #  The default style: int  #  wx.FNTP_FONTDESC_AS_LABEL | wx.FNTP_USEFONT_FOR_LABEL.
FNTP_USE_TEXTCTRL: int  #  Creates a text control to the left of the picker button which is completely managed by the   wx.FontPickerCtrl  and which can be used by the user to specify a font (see SetSelectedFont). The text control is automatically synchronized with buttonâs value. Use functions defined in   wx.PickerBase  to modify the text control.
FNTP_FONTDESC_AS_LABEL: int  #  Keeps the label of the button updated with the fontface name and the font size. E.g. choosing âTimes New Roman bold, italic withsize 10â from the fontdialog, will update the label (overwriting any previous label) with the âTimes New Roman, 10â text.
FNTP_USEFONT_FOR_LABEL: int  #  Uses the currently selected font to draw the label of the button. ^^
EVT_FONTPICKER_CHANGED: int  #  The user changed the font selected in the control either using the button or using text control (see wx.FNTP_USE_TEXTCTRL; note that in this case the event is fired only if the userâs input is valid, i.e. recognizable). ^^
FNTP_DEFAULT_STYLE: int
FNTP_FONTDESC_AS_LABEL: int
FNTP_USEFONT_FOR_LABEL: int
FNTP_USE_TEXTCTRL: int
FNTP_FONTDESC_AS_LABEL: int
FNTP_USEFONT_FOR_LABEL: int
FNTP_USE_TEXTCTRL: int
FNTP_USE_TEXTCTRL: int


class FontPickerEvent(CommandEvent):
    """ This event class is used for the events generated by FontPickerCtrl.
    """
    def __init__(self, generator, id, font) -> None:
        """ The constructor is not normally used by the user code.
        """

    def GetFont(self) -> 'Font':
        """ Retrieve the font the user has just selected.
        """

    def SetFont(self: 'Font', f) -> None:
        """ Set the font associated with the event.
        """

EVT_FONTPICKER_CHANGED: int  #  Generated whenever the selected font changes. ^^


class Frame(TopLevelWindow):
    """ A frame is a window whose size and position can (usually) be changed
by the user.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Centre(self, direction: int=BOTH) -> None:
        """ Centres the frame on the display.
        """

    def Create(self, parent, id=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE, name=FrameNameStr) -> bool:
        """ Used in two-step frame construction.
        """

    def CreateStatusBar(self, number=1, style=STB_DEFAULT_STYLE, id=0, name=StatusBarNameStr) -> 'StatusBar':
        """ Creates a status bar at the bottom of the frame.
        """

    def CreateToolBar(self, style=TB_DEFAULT_STYLE, id=ID_ANY, name=ToolBarNameStr) -> 'ToolBar':
        """ Creates a toolbar at the top or left of the frame.
        """

    def DoGiveHelp(self, text, show) -> None:
        """ Method used to show help string of the selected menu toolbar item.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetClientAreaOrigin(self) -> 'Point':
        """ Returns the origin of the frame client area (in client coordinates).
        """

    def GetMenuBar(self) -> 'MenuBar':
        """ Returns a pointer to the menubar currently associated with the frame (if any).
        """

    def GetStatusBar(self) -> 'StatusBar':
        """ Returns a pointer to the status bar currently associated with the frame (if any).
        """

    def GetStatusBarPane(self) -> int:
        """ Returns the status bar pane used to display menu and toolbar help.
        """

    def GetToolBar(self) -> 'ToolBar':
        """ Returns a pointer to the toolbar currently associated with the frame (if any).
        """

    def OnCreateStatusBar(self, number, style, id, name) -> 'StatusBar':
        """ Virtual function called when a status bar is requested by CreateStatusBar .
        """

    def OnCreateToolBar(self, style, id, name) -> 'ToolBar':
        """ Virtual function called when a toolbar is requested by CreateToolBar .
        """

    def PopStatusText(self, number: int=0) -> None:
        """ number (int) â
        """

    def ProcessCommand(self, id: int) -> bool:
        """ Simulate a menu command.
        """

    def PushStatusText(self, text, number=0) -> None:
        """ text (string) â
        """

    def SetMenuBar(self, menuBar: 'MenuBar') -> None:
        """ Tells the frame to show the given menu bar.
        """

    def SetStatusBar(self, statusBar: 'StatusBar') -> None:
        """ Associates a status bar with the frame.
        """

    def SetStatusBarPane(self, n: int) -> None:
        """ Set the status bar pane used to display menu and toolbar help.
        """

    def SetStatusText(self, text, number=0) -> None:
        """ Sets the status bar text and updates the status bar display.
        """

    def SetStatusWidths(self, widths: list[int]) -> None:
        """ Sets the widths of the fields in the status bar.
        """

    def SetToolBar(self, toolBar: 'ToolBar') -> None:
        """ Associates a toolbar with the frame.
        """

DEFAULT_FRAME_STYLE: int  #  Defined as wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN.
ICONIZE: int  #  Display the frame iconized (minimized). Windows only.
CAPTION: int  #  Puts a caption on the frame. Notice that this flag is required by wx.MINIMIZE_BOX, wx.MAXIMIZE_BOX and wx.CLOSE_BOX on most systems as the corresponding buttons cannot be shown if the window has no title bar at all. I.e. if wx.CAPTION is not specified those styles would be simply ignored.
MINIMIZE: int  #  Identical to wx.ICONIZE. Windows only.
MINIMIZE_BOX: int  #  Displays a minimize box on the frame.
MAXIMIZE: int  #  Displays the frame maximized. Windows and GTK+ only.
MAXIMIZE_BOX: int  #  Displays a maximize box on the frame. Notice that under wxGTK wx.RESIZE_BORDER must be used as well or this style is ignored.
CLOSE_BOX: int  #  Displays a close box on the frame.
STAY_ON_TOP: int  #  Stay on top of all other windows, see also wx.FRAME_FLOAT_ON_PARENT.
SYSTEM_MENU: int  #  Displays a system menu containing the list of various windows commands in the window title bar. Unlike wx.MINIMIZE_BOX, wx.MAXIMIZE_BOX and wx.CLOSE_BOX styles this style can be used without wx.CAPTION, at least under Windows, and makes the system menu available without showing it on screen in this case. However it is recommended to only use it together with wx.CAPTION for consistent behaviour under all platforms.
RESIZE_BORDER: int  #  Displays a resizable border around the window.
FRAME_TOOL_WINDOW: int  #  Causes a frame with a small title bar to be created; the frame does not appear in the taskbar under Windows or GTK+.
FRAME_NO_TASKBAR: int  #  Creates an otherwise normal frame but it does not appear in the taskbar under Windows or GTK+ (note that it will minimize to the desktop window under Windows which may seem strange to the users and thus it might be better to use this style only without wx.MINIMIZE_BOX style). In wxGTK, the flag is respected only if the window manager supports _NET_WM_STATE_SKIP_TASKBAR hint.
FRAME_FLOAT_ON_PARENT: int  #  The frame will always be on top of its parent (unlike wx.STAY_ON_TOP). A frame created with this style must have a not None parent.
FRAME_SHAPED: int  #  Windows with this style are allowed to have their shape changed with the SetShape  method. ^^
EVT_CLOSE: int  #  Process a  wxEVT_CLOSE_WINDOW   event when the frame is being closed by the user or programmatically (see  wx.Window.Close ). The user may generate this event clicking the close button (typically the âXâ on the top-right of the title bar) if itâs present (see the  CLOSE_BOX   style). See    wx.CloseEvent.
EVT_ICONIZE: int  #  Process a  wxEVT_ICONIZE   event. See    wx.IconizeEvent.
EVT_MENU_OPEN: int  #  A menu is about to be opened. See   wx.MenuEvent.
EVT_MENU_CLOSE: int  #  A menu has been just closed. See   wx.MenuEvent.
EVT_MENU_HIGHLIGHT: int  #  The menu item with the specified id has been highlighted: int  #  used to show help prompts in the status bar by   wx.Frame. See   wx.MenuEvent.
EVT_MENU_HIGHLIGHT_ALL: int  #  A menu item has been highlighted, i.e. the currently selected menu item has changed. See   wx.MenuEvent. ^^
DEFAULT_FRAME_STYLE: int
MINIMIZE_BOX: int
MAXIMIZE_BOX: int
RESIZE_BORDER: int
SYSTEM_MENU: int
CAPTION: int
CLOSE_BOX: int
CLIP_CHILDREN: int
ICONIZE: int
CAPTION: int
MINIMIZE_BOX: int
MAXIMIZE_BOX: int
CLOSE_BOX: int
CAPTION: int
MINIMIZE: int
ICONIZE: int
MINIMIZE_BOX: int
MAXIMIZE: int
MAXIMIZE_BOX: int
RESIZE_BORDER: int
CLOSE_BOX: int
STAY_ON_TOP: int
FRAME_FLOAT_ON_PARENT: int
SYSTEM_MENU: int
MINIMIZE_BOX: int
MAXIMIZE_BOX: int
CLOSE_BOX: int
CAPTION: int
CAPTION: int
RESIZE_BORDER: int
FRAME_TOOL_WINDOW: int
FRAME_NO_TASKBAR: int
MINIMIZE_BOX: int
FRAME_FLOAT_ON_PARENT: int
STAY_ON_TOP: int
FRAME_SHAPED: int
FRAME_EX_CONTEXTHELP: int
MAXIMIZE_BOX: int
MINIMIZE_BOX: int
DEFAULT_FRAME_STYLE: int
MAXIMIZE_BOX: int
FRAME_EX_METAL: int
HORIZONTAL: int
VERTICAL: int
BOTH: int


class FSFile(Object):
    """ This class represents a single file opened by FileSystem.
    """
    def __init__(self, stream, location, mimetype, anchor, modif) -> None:
        """ Constructor.
        """

    def DetachStream(self) -> 'InputStream':
        """ Detaches the stream from the   wx.FSFile  object.
        """

    def GetAnchor(self) -> str:
        """ Returns anchor (if present).
        """

    def GetLocation(self) -> str:
        """ Returns full location of the file, including path and protocol.
        """

    def GetMimeType(self) -> str:
        """ Returns the MIME type of the content of this file.
        """

    def GetModificationTime(self) -> 'DateTime':
        """ Returns time when this file was modified.
        """

    def GetStream(self) -> 'InputStream':
        """ Returns pointer to the stream.
        """



class FullScreenEvent(Event):
    """ An event being sent when the user enters or exits full screen mode.
    """
    def __init__(self, id=0, fullscreen=True) -> None:
        """ Constructor.
        """

    def IsFullScreen(self) -> bool:
        """ Returns True if the frame entered full screen, False if exited full screen.
        """

EVT_FULLSCREEN: int  #  Process a  wxEVT_FULLSCREEN   event. ^^


class Gauge(Control):
    """ A gauge is a horizontal or vertical bar which shows a quantity (often
time).
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, range=100, pos=DefaultPosition, size=DefaultSize, style=GA_HORIZONTAL, validator=DefaultValidator, name=GaugeNameStr) -> bool:
        """ Creates the gauge for two-step construction.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetRange(self) -> int:
        """ Returns the maximum position of the gauge.
        """

    def GetValue(self) -> int:
        """ Returns the current position of the gauge.
        """

    def IsVertical(self) -> bool:
        """ Returns True if the gauge is vertical (has  GA_VERTICAL   style) and False otherwise.
        """

    def Pulse(self) -> None:
        """ Switch the gauge to indeterminate mode (if required) and makes the gauge move a bit to indicate the user that some progress has been made.
        """

    def SetRange(self, range: int) -> None:
        """ Sets the range (maximum value) of the gauge.
        """

    def SetValue(self, pos: int) -> None:
        """ Sets the position of the gauge.
        """

GA_HORIZONTAL: int  #  Creates a horizontal gauge.
GA_VERTICAL: int  #  Creates a vertical gauge.
GA_SMOOTH: int  #  Creates smooth progress bar with one pixel wide update step (not supported by all platforms).
GA_TEXT: int  #  Display the current value in percents in the gauge itself. This style is only supported in Qt and ignored under the other platforms. This flag is only available in wxWidgets 3.1.0 and later.
GA_PROGRESS: int  #  Reflect the value of gauge in the application taskbar button under Windows 7 and later and the dock icon under macOS, ignored under the other platforms. This flag is only available in wxWidgets 3.1.0 and later. ^^
GA_HORIZONTAL: int
GA_VERTICAL: int
GA_SMOOTH: int
GA_TEXT: int
GA_PROGRESS: int


class GBPosition:
    """ This class represents the position of an item in a virtual grid of
rows and columns managed by a GridBagSizer.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Get(self) -> tuple:
        """ Return the row and col properties as a tuple.
        """

    def GetCol(self) -> int:
        """ Get the current column value.
        """

    def GetIM(self) -> None:
        """ Returns an immutable representation of the wx.GBPosition object, based on namedtuple.
        """

    def GetRow(self) -> int:
        """ Get the current row value.
        """

    def Set(self, row=0, col=0) -> None:
        """ Set both the row and column properties.
        """

    def SetCol(self, col: int) -> None:
        """ Set a new column value.
        """

    def SetRow(self, row: int) -> None:
        """ Set a new row value.
        """

    def __bool__(self) -> None:
        """ 
        """

    def __getitem__(self, idx) -> None:
        """ 
        """

    def __len__(self) -> None:
        """ 
        """

    def __nonzero__(self) -> None:
        """ 
        """

    def __reduce__(self) -> None:
        """ 
        """

    def __repr__(self) -> None:
        """ 
        """

    def __setitem__(self, idx, val) -> None:
        """ 
        """

    def __str__(self) -> None:
        """ 
        """

    def __ne__(self, item: Any) -> bool:
        """ Compare inequality of two GBPositions.
        """

    def __eq__(self, item: Any) -> bool:
        """ Compare equality of two GBPositions.
        """

GBPosition: int
GBPosition: int
GBPosition: int


class GridBagSizer(FlexGridSizer):
    """ A Sizer that can lay out items in a virtual grid like a
FlexGridSizer but in this case explicit positioning of the items is
allowed using GBPosition, and items can optionally span more than
one row and/or column using GBSpan.
    """
    def __init__(self, vgap=0, hgap=0) -> None:
        """ Constructor, with optional parameters to specify the gap between the rows and columns.
        """

    def Add(self, *args, **kw) -> 'SizerItem':
        """ Overloaded Implementations:
        """

    def CalcMin(self) -> 'Size':
        """ Called when the managed size of the sizer is needed or when layout needs done.
        """

    def CheckForIntersection(self, *args, **kw) -> bool:
        """ Look at all items and see if any intersect (or would overlap) the given item.
        """

    def FindItem(self, *args, **kw) -> 'GBSizerItem':
        """ Find the sizer item for the given window or subsizer, returns None if not found.
        """

    def FindItemAtPoint(self, pt: 'Point') -> 'GBSizerItem':
        """ Return the sizer item located at the point given in pt, or None if there is no item at that point.
        """

    def FindItemAtPosition(self, pos: 'GBPosition') -> 'GBSizerItem':
        """ Return the sizer item for the given grid cell, or None if there is no item at that position.
        """

    def FindItemWithData(self, userData: 'Object') -> 'GBSizerItem':
        """ Return the sizer item that has a matching user data (it only compares pointer values) or None if not found.
        """

    def GetCellSize(self, row, col) -> 'Size':
        """ Get the size of the specified cell, including hgap and vgap.
        """

    def GetEmptyCellSize(self) -> 'Size':
        """ Get the size used for cells in the grid with no item.
        """

    def GetItemPosition(self, *args, **kw) -> 'GBPosition':
        """ Get the grid position of the specified item.
        """

    def GetItemSpan(self, *args, **kw) -> 'GBSpan':
        """ Get the row/col spanning of the specified item.
        """

    def RepositionChildren(self, minSize: Union[tuple[int, int], 'Size']) -> None:
        """ Called when the managed size of the sizer is needed or when layout needs done.
        """

    def SetEmptyCellSize(self, sz: Union[tuple[int, int], 'Size']) -> None:
        """ Set the size used for cells in the grid with no item.
        """

    def SetItemPosition(self, *args, **kw) -> bool:
        """ Set the grid position of the specified item.
        """

    def SetItemSpan(self, *args, **kw) -> bool:
        """ Set the row/col spanning of the specified item.
        """



class GBSizerItem(SizerItem):
    """ The GBSizerItem class is used by the GridBagSizer for tracking the
items in the sizer.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetEndPos(self) -> tuple:
        """ Get the row and column of the endpoint of this item.
        """

    def GetGBSizer(self) -> 'GridBagSizer':
        """ wx.GridBagSizer
        """

    def GetPos(self) -> 'GBPosition':
        """ Get the grid position of the item.
        """

    def GetSpan(self) -> 'GBSpan':
        """ Get the row and column spanning of the item.
        """

    def Intersects(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def SetGBSizer(self, sizer: 'GridBagSizer') -> None:
        """ sizer (wx.GridBagSizer) â
        """

    def SetPos(self, pos: 'GBPosition') -> bool:
        """ If the item is already a member of a sizer then first ensure that there is no other item that would intersect with this one at the new position, then set the new position.
        """

    def SetSpan(self, span: 'GBSpan') -> bool:
        """ If the item is already a member of a sizer then first ensure that there is no other item that would intersect with this one with its new spanning size, then set the new spanning.
        """



class GBSpan:
    """ This class is used to hold the row and column spanning attributes of
items in a GridBagSizer.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Get(self) -> tuple:
        """ Return the rowspan and colspan properties as a tuple.
        """

    def GetColspan(self) -> int:
        """ Get the current colspan value.
        """

    def GetIM(self) -> None:
        """ Returns an immutable representation of the wx.GBSpan object, based on namedtuple.
        """

    def GetRowspan(self) -> int:
        """ Get the current rowspan value.
        """

    def Set(self, rowspan=0, colspan=0) -> None:
        """ Set both the rowspan and colspan properties.
        """

    def SetColspan(self, colspan: int) -> None:
        """ Set a new colspan value.
        """

    def SetRowspan(self, rowspan: int) -> None:
        """ Set a new rowspan value.
        """

    def __bool__(self) -> None:
        """ 
        """

    def __getitem__(self, idx) -> None:
        """ 
        """

    def __len__(self) -> None:
        """ 
        """

    def __nonzero__(self) -> None:
        """ 
        """

    def __reduce__(self) -> None:
        """ 
        """

    def __repr__(self) -> None:
        """ 
        """

    def __setitem__(self, idx, val) -> None:
        """ 
        """

    def __str__(self) -> None:
        """ 
        """

    def __ne__(self, item: Any) -> bool:
        """ Compare inequality of two GBSpans.
        """

    def __eq__(self, item: Any) -> bool:
        """ Compare equality of two GBSpans.
        """

GBSpan: int
GBSpan: int
GBSpan: int


class GCDC(DC):
    """ GCDC is a device context that draws on a GraphicsContext.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetGraphicsContext(self) -> 'GraphicsContext':
        """ Retrieves associated   wx.GraphicsContext.
        """

    def SetGraphicsContext(self, context: 'GraphicsContext') -> None:
        """ Set the graphics context to be used for this   wx.GCDC.
        """



class GraphicsContext(GraphicsObject):
    """ A GraphicsContext instance is the object that is drawn upon.
    """
    def BeginLayer(self, opacity: 'Double') -> None:
        """ All rendering will be done into a fully transparent temporary context.
        """

    def Clip(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def ConcatTransform(self, matrix: 'GraphicsMatrix') -> None:
        """ Concatenates the passed in transform with the current transform of this context.
        """

    @staticmethod
    def Create(*args, **kw) -> 'GraphicsContext':
        """ Overloaded Implementations:
        """

    def CreateBitmap(self, bitmap: 'Bitmap') -> 'GraphicsBitmap':
        """ Creates   wx.GraphicsBitmap  from an existing   wx.Bitmap.
        """

    def CreateBitmapFromImage(self, image: 'Image') -> 'GraphicsBitmap':
        """ Creates   wx.GraphicsBitmap  from an existing   wx.Image.
        """

    def CreateBrush(self, brush: 'Brush') -> 'GraphicsBrush':
        """ Creates a native brush from a   wx.Brush.
        """

    def CreateFont(self, *args, **kw) -> 'GraphicsFont':
        """ Overloaded Implementations:
        """

    @staticmethod
    def CreateFromNative(context: Any) -> 'GraphicsContext':
        """ Creates a   wx.GraphicsContext  from a native context.
        """

    @staticmethod
    def CreateFromNativeWindow(window: Any) -> 'GraphicsContext':
        """ Creates a   wx.GraphicsContext  from a native window.
        """

    @staticmethod
    def CreateFromUnknownDC(dc: 'DC') -> 'GraphicsContext':
        """ Creates a   wx.GraphicsContext  from a DC of unknown specific type.
        """

    def CreateLinearGradientBrush(self, *args, **kw) -> 'GraphicsBrush':
        """ Overloaded Implementations:
        """

    def CreateMatrix(self, *args, **kw) -> 'GraphicsMatrix':
        """ Overloaded Implementations:
        """

    def CreatePath(self) -> 'GraphicsPath':
        """ Creates a native graphics path which is initially empty.
        """

    def CreatePen(self, *args, **kw) -> 'GraphicsPen':
        """ Overloaded Implementations:
        """

    def CreateRadialGradientBrush(self, *args, **kw) -> 'GraphicsBrush':
        """ Overloaded Implementations:
        """

    def CreateSubBitmap(self, bitmap, x, y, w, h) -> 'GraphicsBitmap':
        """ Extracts a sub-bitmap from an existing bitmap.
        """

    def DisableOffset(self) -> None:
        """ Helper to determine if a 0.5 offset should be applied for the drawing operation.
        """

    def DrawBitmap(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DrawEllipse(self, x, y, w, h) -> None:
        """ Draws an ellipse.
        """

    def DrawIcon(self, icon, x, y, w, h) -> None:
        """ Draws the icon.
        """

    def DrawLines(self, point2Ds, fillStyle=ODDEVEN_RULE) -> None:
        """ Draws a polygon.
        """

    def DrawPath(self, path, fillStyle=ODDEVEN_RULE) -> None:
        """ Draws the path by first filling and then stroking.
        """

    def DrawRectangle(self, x, y, w, h) -> None:
        """ Draws a rectangle.
        """

    def DrawRoundedRectangle(self, x, y, w, h, radius) -> None:
        """ Draws a rounded rectangle.
        """

    def DrawText(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def EnableOffset(self, enable: bool=True) -> None:
        """ Indicates whether the context should try to offset for pixel boundaries.
        """

    def EndDoc(self) -> None:
        """ Done with that document (relevant only for printing / pdf etc.)
        """

    def EndLayer(self) -> None:
        """ Composites back the drawings into the context with the opacity given at the BeginLayer   call.
        """

    def EndPage(self) -> None:
        """ Ends the current page (relevant only for printing / pdf etc.)
        """

    def FillPath(self, path, fillStyle=ODDEVEN_RULE) -> None:
        """ Fills the path with the current brush.
        """

    def Flush(self) -> None:
        """ Make sure that the current content of this context is immediately visible.
        """

    def FromDIP(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:
        """

    def GetAntialiasMode(self) -> 'AntialiasMode':
        """ Returns the current shape antialiasing mode.
        """

    def GetClipBox(self, x, y, w, h) -> None:
        """ Returns bounding box of the current clipping region.
        """

    def GetCompositionMode(self) -> 'CompositionMode':
        """ Returns the current compositing operator.
        """

    def GetDPI(self) -> tuple:
        """ Returns the resolution of the graphics context in device points per inch.
        """

    def GetInterpolationQuality(self) -> 'InterpolationQuality':
        """ Returns the current interpolation quality.
        """

    def GetNativeContext(self) -> None:
        """ Returns the native context (CGContextRef for Core Graphics, Graphics pointer for GDIPlus and cairo_t pointer for cairo).
        """

    def GetPartialTextExtents(self, text: str) -> list[float]:
        """ Fills the widths  array with the widths from the beginning of text  to the corresponding character of text.
        """

    def GetSize(self) -> tuple:
        """ Returns the size of the graphics context in device coordinates.
        """

    def GetFullTextExtent(self, *args, **kw) -> tuple:
        """ Overloaded Implementations:
        """

    def GetTransform(self) -> 'GraphicsMatrix':
        """ Gets the current transformation matrix of this context.
        """

    def GetWindow(self) -> 'Window':
        """ Returns the associated window if any.
        """

    def OffsetEnabled(self) -> bool:
        """ Helper to determine if a 0.5 offset should be applied for the drawing operation.
        """

    def PopState(self) -> None:
        """ Sets current state of the context to the state saved by a preceding call to PushState   and removes that state from the stack of saved states.
        """

    def PushState(self) -> None:
        """ Push the current state (like transformations, clipping region and quality settings) of the context on a stack.
        """

    def ResetClip(self) -> None:
        """ Resets the clipping to original shape.
        """

    def Rotate(self, angle: 'Double') -> None:
        """ Rotates the current transformation matrix (in radians).
        """

    def Scale(self, xScale, yScale) -> None:
        """ Scales the current transformation matrix.
        """

    def SetAntialiasMode(self, antialias: AntialiasMode) -> bool:
        """ Sets the antialiasing mode, returns True if it supported.
        """

    def SetBrush(self, *args, **kw) -> None:
        """ Sets the brush for filling paths.
        """

    def SetCompositionMode(self, op: CompositionMode) -> bool:
        """ Sets the compositing operator, returns True if it supported.
        """

    def SetFont(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetInterpolationQuality(self, interpolation: InterpolationQuality) -> bool:
        """ Sets the interpolation quality, returns True if it is supported.
        """

    def SetPen(self, *args, **kw) -> None:
        """ Sets the pen used for stroking.
        """

    def SetTransform(self, matrix: 'GraphicsMatrix') -> None:
        """ Sets the current transformation matrix of this context.
        """

    def ShouldOffset(self) -> bool:
        """ Helper to determine if a 0.5 offset should be applied for the drawing operation.
        """

    def StartDoc(self, message: str) -> bool:
        """ Begin a new document (relevant only for printing / pdf etc.) If there is a progress dialog, message will be shown.
        """

    def StartPage(self, width=0, height=0) -> None:
        """ Opens a new page (relevant only for printing / pdf etc.) with the given size in points.
        """

    def StrokeLine(self, x1, y1, x2, y2) -> None:
        """ Strokes a single line.
        """

    def StrokeLineSegments(self, beginPoint2Ds, endPoint2Ds) -> None:
        """ Stroke disconnected lines from begin to end points.
        """

    def StrokeLines(self, point2Ds) -> None:
        """ Stroke lines connecting all the points.
        """

    def StrokePath(self, path: 'GraphicsPath') -> None:
        """ Strokes along a path with the current pen.
        """

    def ToDIP(self, *args, **kw) -> 'Size':
        """ Overloaded Implementations:
        """

    def Translate(self, dx, dy) -> None:
        """ Translates the current transformation matrix.
        """



class GDIObject(Object):
    """ This class allows platforms to implement functionality to optimise GDI
objects, such as Pen, Brush and Font.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """



class Pen(GDIObject):
    """ A pen is a drawing tool for drawing outlines.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetCap(self) -> 'PenCap':
        """ Returns the pen cap style, which may be one of  CAP_ROUND ,   CAP_PROJECTING   and   CAP_BUTT .
        """

    def GetColour(self) -> 'Colour':
        """ Returns a reference to the pen colour.
        """

    def GetDashes(self) -> list[int]:
        """ Gets an array of dashes (defined as  char   in X,   DWORD   under Windows).
        """

    def GetJoin(self) -> 'PenJoin':
        """ Returns the pen join style, which may be one of  JOIN_BEVEL ,   JOIN_ROUND   and   JOIN_MITER .
        """

    def GetQuality(self) -> 'PenQuality':
        """ Returns the pen quality.
        """

    def GetStipple(self) -> 'Bitmap':
        """ Gets a pointer to the stipple bitmap.
        """

    def GetStyle(self) -> 'PenStyle':
        """ Returns the pen style.
        """

    def GetWidth(self) -> int:
        """ Returns the pen width.
        """

    def IsNonTransparent(self) -> bool:
        """ Returns True if the pen is a valid non-transparent pen.
        """

    def IsOk(self) -> bool:
        """ Returns True if the pen is initialised.
        """

    def IsTransparent(self) -> bool:
        """ Returns True if the pen is transparent.
        """

    def SetCap(self, capStyle: PenCap) -> None:
        """ Sets the pen cap style, which may be one of  CAP_ROUND ,   CAP_PROJECTING   and   CAP_BUTT .
        """

    def SetColour(self, *args, **kw) -> None:
        """ The penâs colour is changed to the given colour.
        """

    def SetDashes(self, dashes: list[int]) -> None:
        """ Associates an array of dash values (defined as  char   in X,   DWORD   under Windows) with the pen.
        """

    def SetJoin(self, join_style: PenJoin) -> None:
        """ Sets the pen join style, which may be one of  JOIN_BEVEL ,   JOIN_ROUND   and   JOIN_MITER .
        """

    def SetQuality(self, quality: PenQuality) -> None:
        """ Sets the pen quality.
        """

    def SetStipple(self, stipple: 'Bitmap') -> None:
        """ Sets the bitmap for stippling.
        """

    def SetStyle(self, style: PenStyle) -> None:
        """ Set the pen style.
        """

    def SetWidth(self, width: int) -> None:
        """ Sets the pen width.
        """

    def _copyFrom(self, other) -> None:
        """ For internal use only.
        """

    def __ne__(self, item: Any) -> bool:
        """ Inequality operator.
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.
        """

PENSTYLE_TRANSPARENT: int
PENSTYLE_TRANSPARENT: int
PENSTYLE_TRANSPARENT: int


class GenericDirCtrl(Control):
    """ This control can be used to place a directory listing (with optional
files) on an arbitrary window.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def CollapsePath(self, path: str) -> bool:
        """ Collapse the given path.
        """

    def CollapseTree(self) -> None:
        """ Collapses the entire tree.
        """

    def Create(self, parent, id=ID_ANY, dir=DirDialogDefaultFolderStr, pos=DefaultPosition, size=DefaultSize, style=DIRCTRL_DEFAULT_STYLE, filter="", defaultFilter=0, name=TreeCtrlNameStr) -> bool:
        """ Create function for two-step construction.
        """

    def ExpandPath(self, path: str) -> bool:
        """ Tries to expand as much of the given path  as possible, so that the filename or directory is visible in the tree control.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetDefaultPath(self) -> str:
        """ Gets the default path.
        """

    def GetFilePath(self) -> str:
        """ Gets selected filename path only (else empty string).
        """

    def GetFilePaths(self, paths: list[str]) -> None:
        """ Fills the array paths  with the currently selected filepaths.
        """

    def GetFilter(self) -> str:
        """ Returns the filter string.
        """

    def GetFilterIndex(self) -> int:
        """ Returns the current filter index (zero-based).
        """

    def GetFilterListCtrl(self) -> 'DirFilterListCtrl':
        """ Returns a pointer to the filter list control (if present).
        """

    def GetPath(self, *args, **kw) -> str:
        """ Overloaded Implementations:
        """

    def GetPaths(self) -> list:
        """ Returns a list of the currently selected paths.
        """

    def GetRootId(self) -> 'TreeItemId':
        """ Returns the root id for the tree control.
        """

    def GetTreeCtrl(self) -> 'TreeCtrl':
        """ Returns a pointer to the tree control.
        """

    def Init(self) -> None:
        """ Initializes variables.
        """

    def ReCreateTree(self) -> None:
        """ Collapse and expand the tree, thus re-creating it from scratch.
        """

    def SelectPath(self, path, select=True) -> None:
        """ Selects the given item.
        """

    def SelectPaths(self, paths: list[str]) -> None:
        """ Selects only the specified paths, clearing any previous selection.
        """

    def SetDefaultPath(self, path: str) -> None:
        """ Sets the default path.
        """

    def SetFilter(self, filter: str) -> None:
        """ Sets the filter string.
        """

    def SetFilterIndex(self, n: int) -> None:
        """ Sets the current filter index (zero-based).
        """

    def SetPath(self, path: str) -> None:
        """ Sets the current path.
        """

    def ShowHidden(self, show: bool) -> None:
        """ show (bool) â If True, hidden folders and files will be displayed by the control. If False, they will not be displayed.
        """

    def UnselectAll(self) -> None:
        """ Removes the selection from all currently selected items.
        """

DIRCTRL_DIR_ONLY: int  #  Only show directories, and not files.
DIRCTRL_3D_INTERNAL: int  #  Use 3D borders for internal controls. This is the default.
DIRCTRL_SELECT_FIRST: int  #  When setting the default path, select the first file in the directory.
DIRCTRL_SHOW_FILTERS: int  #  Show the drop-down filter list.
DIRCTRL_EDIT_LABELS: int  #  Allow the folder and file labels to be editable.
DIRCTRL_MULTIPLE: int  #  Allows multiple files and folders to be selected. ^^
EVT_DIRCTRL_SELECTIONCHANGED: int  #  Selected directory has changed. Processes a  wxEVT_DIRCTRL_SELECTIONCHANGED   event type. Notice that this event is generated even for the changes done by the program itself and not only those done by the user. Available since wxWidgets 2.9.5.
EVT_DIRCTRL_FILEACTIVATED: int  #  The user activated a file by double-clicking or pressing Enter. Available since wxWidgets 2.9.5. ^^
DIRCTRL_DIR_ONLY: int
DIRCTRL_3D_INTERNAL: int
DIRCTRL_SELECT_FIRST: int
DIRCTRL_SHOW_FILTERS: int
DIRCTRL_EDIT_LABELS: int
DIRCTRL_MULTIPLE: int
DIRCTRL_MULTIPLE: int


class GenericDragImage(Object):
    """ This class is used when you wish to drag an object on the screen, and
a simple cursor is not enough.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def BeginDrag(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def DoDrawImage(self, dc, pos) -> bool:
        """ Draws the image on the device context with top-left corner at the given position.
        """

    def EndDrag(self) -> bool:
        """ Call this when the drag has finished.
        """

    def GetImageRect(self, pos: 'Point') -> 'Rect':
        """ Returns the rectangle enclosing the image, assuming that the image is drawn with its top-left corner at the given point.
        """

    def Hide(self) -> bool:
        """ Hides the image.
        """

    def Move(self, pt: 'Point') -> bool:
        """ Call this to move the image to a new position.
        """

    def Show(self) -> bool:
        """ Shows the image.
        """

    def UpdateBackingFromWindow(self, windowDC, destDC, sourceRect, destRect) -> bool:
        """ Override this if you wish to draw the window contents to the backing bitmap yourself.
        """



class GenericMessageDialog(Dialog):
    """ This class represents a dialog that shows a single or multi-line
message, with a choice of wx.OK, Yes, No and Cancel buttons.
    """
    def __init__(self, parent, message, caption=MessageBoxCaptionStr, style=OK|CENTRE, pos=DefaultPosition) -> None:
        """ Constructor specifying the message box properties.
        """

    def AddMessageDialogCheckBox(self, sizer: 'Sizer') -> None:
        """ Can be overridden to provide more contents for the dialog
        """

    def AddMessageDialogDetails(self, sizer: 'Sizer') -> None:
        """ Can be overridden to provide more contents for the dialog
        """

    def GetCancelLabel(self) -> str:
        """ string
        """

    def GetCaption(self) -> str:
        """ string
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetEffectiveIcon(self) -> int:
        """ long
        """

    def GetExtendedMessage(self) -> str:
        """ string
        """

    def GetHelpLabel(self) -> str:
        """ string
        """

    def GetMessage(self) -> str:
        """ string
        """

    def GetMessageDialogStyle(self) -> int:
        """ long
        """

    def GetNoLabel(self) -> str:
        """ string
        """

    def GetOKLabel(self) -> str:
        """ string
        """

    def GetYesLabel(self) -> str:
        """ string
        """

    def HasCustomLabels(self) -> bool:
        """ bool
        """

    def SetExtendedMessage(self, extendedMessage: str) -> None:
        """ Sets the extended message for the dialog: this message is usually an extension of the short message specified in the constructor or set with SetMessage .
        """

    def SetHelpLabel(self, help: MessageDialogButtonLabel) -> bool:
        """ Sets the label for the Help button.
        """

    def SetMessage(self, message: str) -> None:
        """ Sets the message shown by the dialog.
        """

    def SetOKCancelLabels(self, ok, cancel) -> bool:
        """ Overrides the default labels of the wx.OK and Cancel buttons.
        """

    def SetOKLabel(self, ok: MessageDialogButtonLabel) -> bool:
        """ Overrides the default label of the wx.OK button.
        """

    def SetYesNoCancelLabels(self, yes, no, cancel) -> bool:
        """ Overrides the default labels of the Yes, No and Cancel buttons.
        """

    def SetYesNoLabels(self, yes, no) -> bool:
        """ Overrides the default labels of the Yes and No buttons.
        """

    def ShowModal(self) -> int:
        """ Shows the dialog, returning one of wx.ID_OK, wx.ID_CANCEL, wx.ID_YES, wx.ID_NO or wx.ID_HELP.
        """

OK: int  #  Puts an Ok button in the message box. May be combined with  CANCEL .
CANCEL: int  #  Puts a Cancel button in the message box. Must be combined with either  OK   or   YES_NO .
YES_NO: int  #  Puts Yes and No buttons in the message box. It is recommended to always use  CANCEL   with this style as otherwise the message box wonât have a close button under wxMSW and the user will be forced to answer it.
HELP: int  #  Puts a Help button to the message box. This button can have special appearance or be specially positioned if its label is not changed from the default one. Notice that using this button is not supported when showing a message box from non-main thread in OSX/Cocoa. Available since wxWidgets 2.9.3.
NO_DEFAULT: int  #  Makes the âNoâ button default, can only be used with  YES_NO .
CANCEL_DEFAULT: int  #  Makes the âCancelâ button default, can only be used with  CANCEL . This style is currently not supported (and ignored) in wxOSX.
YES_DEFAULT: int  #  Makes the âYesâ button default, this is the default behaviour and this flag exists solely for symmetry with  NO_DEFAULT .
OK_DEFAULT: int  #  Makes the âwx.OKâ button default, this is the default behaviour and this flag exists solely for symmetry with  CANCEL_DEFAULT .
ICON_NONE: int  #  Displays no icon in the dialog if possible (an icon might still be displayed if the current platform mandates its use). This style may be used to prevent the dialog from using the default icon based on  YES_NO   presence as explained in   ICON_QUESTION   and   ICON_INFORMATION   documentation below.
ICON_ERROR: int  #  Displays an error icon in the dialog.
ICON_WARNING: int  #  Displays a warning icon in the dialog. This style should be used for informative warnings or, in combination with  YES_NO   or   CANCEL , for questions that have potentially serious consequences (caution icon is used on macOS in this case).
ICON_QUESTION: int  #  Displays a question mark symbol. This icon is automatically used with  YES_NO   so itâs usually unnecessary to specify it explicitly. This style is not supported for message dialogs under wxMSW when a task dialog is used to implement them (i.e. when running under Windows Vista or later) because  Microsoft guidelines  indicate that no icon should be used for routine confirmations. If it is specified, no icon will be displayed.
ICON_INFORMATION: int  #  Displays an information symbol. This icon is used by default if  YES_NO   is not given so it is usually unnecessary to specify it explicitly.
ICON_EXCLAMATION: int  #  Alias for  ICON_WARNING .
ICON_HAND: int  #  Alias for  ICON_ERROR .
ICON_AUTH_NEEDED: int  #  Displays an authentication needed symbol. This style is only supported for message dialogs under wxMSW when a task dialog is used to implement them (i.e. when running under Windows Vista or later). In other cases the default icon selection logic will be used. Note this can be combined with other styles to provide a fallback. For instance, using wx.ICON_AUTH_NEEDED | wx.ICON_QUESTION will show a shield symbol on Windows Vista or above and a question symbol on other platforms. Available since wxWidgets 2.9.5
STAY_ON_TOP: int  #  Makes the message box stay on top of all other windows and not only just its parent (currently implemented only under MSW and GTK).
CENTRE: int  #  Centre the message box on its parent or on the screen if parent is not specified. Setting this style under MSW makes no differences as the dialog is always centered on the parent. ^^
OK: int
OK: int
CANCEL: int
YES_NO: int
HELP: int
NO_DEFAULT: int
CANCEL_DEFAULT: int
YES_DEFAULT: int
OK_DEFAULT: int
OK: int
ICON_NONE: int
ICON_ERROR: int
ICON_WARNING: int
ICON_QUESTION: int
ICON_INFORMATION: int
ICON_EXCLAMATION: int
ICON_HAND: int
ICON_AUTH_NEEDED: int
ICON_AUTH_NEEDED: int
ICON_QUESTION: int
STAY_ON_TOP: int
CENTRE: int
OK: int
OK: int
ID_OK: int
ID_CANCEL: int
ID_YES: int
ID_NO: int
ID_HELP: int
OK: int
OK: int
OK: int
ID_OK: int
ID_CANCEL: int
ID_YES: int
ID_NO: int
ID_HELP: int


class GenericProgressDialog(Dialog):
    """ This class represents a dialog that shows a short message and a
progress bar.
    """
    def __init__(self, title, message, maximum=100, parent=None, style=PD_AUTO_HIDE|PD_APP_MODAL) -> None:
        """ Constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetMessage(self) -> str:
        """ Returns the last message passed to the Update   function; if you always passed ââ to Update   then the message set through the constructor is returned.
        """

    def GetRange(self) -> int:
        """ Returns the maximum value of the progress meter, as passed to the constructor or  NOT_FOUND   if the dialog has no progress bar.
        """

    def GetValue(self) -> int:
        """ Returns the last value passed to the Update   function or  NOT_FOUND   if the dialog has no progress bar.
        """

    def Pulse(self, newmsg: str="") -> tuple:
        """ Like Update   but makes the gauge control run in indeterminate mode.
        """

    def Resume(self) -> None:
        """ Can be used to continue with the dialog, after the user had clicked the âAbortâ button.
        """

    def SetRange(self, maximum: int) -> None:
        """ Changes the maximum value of the progress meter given in the constructor.
        """

    def Update(self, value, newmsg="") -> tuple:
        """ Updates the dialog, setting the progress bar to the new value and updating the message if new one is specified.
        """

    def WasCancelled(self) -> bool:
        """ Returns True if the âCancelâ button was pressed.
        """

    def WasSkipped(self) -> bool:
        """ Returns True if the âSkipâ button was pressed.
        """

PD_APP_MODAL: int  #  Make the progress dialog application-modal, i.e. disable all application windows while it is shown. If this flag is not given, it is only âlocallyâ modal â
PD_AUTO_HIDE: int  #  Causes the progress dialog to disappear from screen as soon as the maximum value of the progress meter has been reached. If this style is not present, the dialog will become a modal dialog (see wx.Dialog.ShowModal ) once the maximum value has been reached and wait for the user to dismiss it.
PD_SMOOTH: int  #  Causes smooth progress of the gauge control (uses a   wx.Gauge  with the  GA_SMOOTH   style).
PD_CAN_ABORT: int  #  This flag tells the dialog that it should have a âCancelâ button which the user may press. If this happens, the next call to Update  will return False.
PD_CAN_SKIP: int  #  This flag tells the dialog that it should have a âSkipâ button which the user may press. If this happens, the next call to Update  will return True in its skip parameter.
PD_ELAPSED_TIME: int  #  This flag tells the dialog that it should show elapsed time (since creating the dialog).
PD_ESTIMATED_TIME: int  #  This flag tells the dialog that it should show estimated time.
PD_REMAINING_TIME: int  #  This flag tells the dialog that it should show remaining time. ^^
PD_APP_MODAL: int
PD_AUTO_HIDE: int
PD_SMOOTH: int
PD_CAN_ABORT: int
PD_CAN_SKIP: int
PD_ELAPSED_TIME: int
PD_ESTIMATED_TIME: int
PD_REMAINING_TIME: int


class GestureEvent(Event):
    """ This is the base class for all supported gesture events.
    """
    def __init__(self, winid=0, type=wxEVT_NULL) -> None:
        """ Constructor.
        """

    def GetPosition(self) -> 'Point':
        """ Returns the position where the event took effect, in client coordinates: position of Pan event, center of zoom for Zoom event, center of rotation for Rotate event, center of box formed by 2 fingers for Two Finger Tap event and position of the pressed finger for Press and Tap Event.
        """

    def IsGestureEnd(self) -> bool:
        """ Returns True if the event was the last in a gesture sequence.
        """

    def IsGestureStart(self) -> bool:
        """ Returns True if the event was the first in a gesture sequence.
        """

    def SetGestureEnd(self, isEnd: bool=True) -> None:
        """ Sets the event to be the last in a gesture sequence.
        """

    def SetGestureStart(self, isStart: bool=True) -> None:
        """ Sets the event to be the first in a gesture sequence.
        """

    def SetPosition(self, pos: 'Point') -> None:
        """ Sets the position where the event took effect, in client coordinates: position of Pan event, center of zoom for Zoom event, center of rotation for Rotate event.
        """



class GIFHandler(ImageHandler):
    """ This is the image handler for the GIF format.
    """
    def __init__(self) -> None:
        """ Default constructor for   wx.GIFHandler.
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Called to test if this handler can read an image from the given stream.
        """

    def LoadFile(self, image, stream, verbose=True, index=-1) -> bool:
        """ Loads an image from a stream, putting the resulting data into image.
        """

    def SaveAnimation(self, images, stream, verbose=True, delayMilliSecs=1000) -> bool:
        """ Save the animated gif.
        """

    def SaveFile(self, image, stream, verbose=True) -> bool:
        """ Saves an image in the output stream.
        """



class GraphicsBitmap(GraphicsObject):
    """ Represents a bitmap.
    """
    def __init__(self) -> None:
        """ Default constructor creates an invalid bitmap.
        """

    def ConvertToImage(self) -> 'Image':
        """ Return the contents of this bitmap as   wx.Image.
        """

    def GetNativeBitmap(self) -> None:
        """ Return the pointer to the native bitmap data.
        """



class GraphicsBrush(GraphicsObject):
    """ A GraphicsBrush is a native representation of a brush.
    """


class GraphicsFont(GraphicsObject):
    """ A GraphicsFont is a native representation of a font.
    """


class GraphicsGradientStop:
    """ Represents a single gradient stop in a collection of gradient stops as
represented by GraphicsGradientStops.
    """
    def __init__(self, col=TransparentColour, pos=0.) -> None:
        """ Creates a stop with the given colour and position.
        """

    def GetColour(self) -> 'Colour':
        """ Return the stop colour.
        """

    def GetPosition(self) -> float:
        """ Return the stop position.
        """

    def SetColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Change the stop colour.
        """

    def SetPosition(self, pos: float) -> None:
        """ Change the stop position.
        """



class GraphicsGradientStops:
    """ Represents a collection of GraphicGradientStop values for use with
CreateLinearGradientBrush and CreateRadialGradientBrush.
    """
    def __init__(self, startCol=TransparentColour, endCol=TransparentColour) -> None:
        """ Initializes the gradient stops with the given boundary colours.
        """

    def Add(self, *args, **kw) -> None:
        """ Add a new stop.
        """

    def GetCount(self) -> int:
        """ Returns the number of stops.
        """

    def GetEndColour(self) -> 'Colour':
        """ Returns the end colour.
        """

    def GetStartColour(self) -> 'Colour':
        """ Returns the start colour.
        """

    def Item(self, n: Any) -> 'GraphicsGradientStop':
        """ Returns the stop at the given index.
        """

    def SetEndColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Set the end colour to col.
        """

    def SetStartColour(self, col: Union[int, str, 'Colour']) -> None:
        """ Set the start colour to col.
        """

    def __getitem__(self, n) -> None:
        """ 
        """

    def __len__(self) -> SIP_SSIZE_T:
        """ SIP_SSIZE_T
        """



class GraphicsMatrix(GraphicsObject):
    """ A GraphicsMatrix is a native representation of an affine matrix.
    """
    def Concat(self, t: 'GraphicsMatrix') -> None:
        """ Concatenates the matrix passed with the current matrix.
        """

    def Get(self) -> tuple:
        """ Returns the component values of the matrix via the argument pointers.
        """

    def GetNativeMatrix(self) -> None:
        """ Returns the native representation of the matrix.
        """

    def Invert(self) -> None:
        """ Inverts the matrix.
        """

    def IsEqual(self, t: 'GraphicsMatrix') -> bool:
        """ Returns True if the elements of the transformation matrix are equal.
        """

    def IsIdentity(self) -> bool:
        """ Return True if this is the identity matrix.
        """

    def Rotate(self, angle: 'Double') -> None:
        """ Rotates this matrix clockwise (in radians).
        """

    def Scale(self, xScale, yScale) -> None:
        """ Scales this matrix.
        """

    def Set(self, a=1.0, b=0.0, c=0.0, d=1.0, tx=0.0, ty=0.0) -> None:
        """ Sets the matrix to the respective values (default values are the identity matrix).
        """

    def TransformDistance(self, dx, dy) -> tuple:
        """ Applies this matrix to a distance (ie.
        """

    def TransformPoint(self, x, y) -> tuple:
        """ Applies this matrix to a point.
        """

    def Translate(self, dx, dy) -> None:
        """ Translates this matrix.
        """



class GraphicsObject(Object):
    """ This class is the superclass of native graphics objects like pens etc.
    """
    def GetRenderer(self) -> 'GraphicsRenderer':
        """ Returns the renderer that was used to create this instance, or None if it has not been initialized yet.
        """

    def IsNull(self) -> bool:
        """ bool
        """

    def IsOk(self) -> bool:
        """ bool
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """



class GraphicsPath(GraphicsObject):
    """ A GraphicsPath is a native representation of a geometric path.
    """
    def AddArc(self, *args, **kw) -> None:
        """ Adds an arc of a circle.
        """

    def AddArcToPoint(self, x1, y1, x2, y2, r) -> None:
        """ Adds an arc (of a circle with radius r) that is tangent to the line connecting current point and (x1, y1) and to the line connecting (x1, y1) and (x2, y2).
        """

    def AddCircle(self, x, y, r) -> None:
        """ Appends a circle around (x,`y`) with radius r  as a new closed subpath.
        """

    def AddCurveToPoint(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddEllipse(self, x, y, w, h) -> None:
        """ Appends an ellipse fitting into the passed in rectangle as a new closed subpath.
        """

    def AddLineToPoint(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddPath(self, path: 'GraphicsPath') -> None:
        """ Adds another path onto the current path.
        """

    def AddQuadCurveToPoint(self, cx, cy, x, y) -> None:
        """ Adds a quadratic bezier curve from the current point, using a control point and an end point.
        """

    def AddRectangle(self, x, y, w, h) -> None:
        """ Appends a rectangle as a new closed subpath.
        """

    def AddRoundedRectangle(self, x, y, w, h, radius) -> None:
        """ Appends a rounded rectangle as a new closed subpath.
        """

    def CloseSubpath(self) -> None:
        """ Closes the current sub-path.
        """

    def Contains(self, *args, **kw) -> None:
        """ True if the point is within the path.
        """

    def GetBox(self) -> 'Rect2D':
        """ Gets the bounding box enclosing all points (possibly including control points).
        """

    def GetCurrentPoint(self) -> 'Point2D':
        """ Gets the last point of the current path, (0,0) if not yet set.
        """

    def GetNativePath(self) -> None:
        """ Returns the native path (CGPathRef for Core Graphics, Path pointer for GDIPlus and a cairo_path_t pointer for cairo).
        """

    def MoveToPoint(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Transform(self, matrix: 'GraphicsMatrix') -> None:
        """ Transforms each point of this path by the matrix.
        """

    def UnGetNativePath(self, p: Any) -> None:
        """ Gives back the native path returned by GetNativePath   because there might be some deallocations necessary (e.g.
        """



class GraphicsPen(GraphicsObject):
    """ A GraphicsPen is a native representation of a pen.
    """


class GraphicsPenInfo:
    """ This class is a helper used for GraphicsPen creation using named
parameter idiom: it allows specifying various GraphicsPen attributes
using the chained calls to its clearly named methods instead of
passing them in the fixed order to GraphicsPen constructors.
    """


class GraphicsRenderer(Object):
    """ A GraphicsRenderer is the instance corresponding to the rendering
engine used.
    """
    def CreateBitmap(self, bitmap: 'Bitmap') -> 'GraphicsBitmap':
        """ Creates   wx.GraphicsBitmap  from an existing   wx.Bitmap.
        """

    def CreateBitmapFromImage(self, image: 'Image') -> 'GraphicsBitmap':
        """ Creates   wx.GraphicsBitmap  from an existing   wx.Image.
        """

    def CreateBitmapFromNativeBitmap(self, bitmap: Any) -> 'GraphicsBitmap':
        """ Creates   wx.GraphicsBitmap  from a native bitmap handle.
        """

    def CreateBrush(self, brush: 'Brush') -> 'GraphicsBrush':
        """ Creates a native brush from a   wx.Brush.
        """

    def CreateContext(self, *args, **kw) -> 'GraphicsContext':
        """ Overloaded Implementations:
        """

    def CreateContextFromImage(self, image: 'Image') -> 'GraphicsContext':
        """ Creates a   wx.GraphicsContext  associated with a   wx.Image.
        """

    def CreateContextFromNativeContext(self, context: Any) -> 'GraphicsContext':
        """ Creates a   wx.GraphicsContext  from a native context.
        """

    def CreateContextFromNativeWindow(self, window: Any) -> 'GraphicsContext':
        """ Creates a   wx.GraphicsContext  from a native window.
        """

    def CreateContextFromUnknownDC(self, dc: 'DC') -> 'GraphicsContext':
        """ Creates a   wx.GraphicsContext  from a DC of unknown specific type.
        """

    def CreateFont(self, *args, **kw) -> 'GraphicsFont':
        """ Overloaded Implementations:
        """

    def CreateFontAtDPI(self, font, dpi, col=BLACK) -> 'GraphicsFont':
        """ Creates a native graphics font from a   wx.Font  and a text colour.
        """

    def CreateImageFromBitmap(self, bmp: 'GraphicsBitmap') -> 'Image':
        """ Creates a   wx.Image  from a   wx.GraphicsBitmap.
        """

    def CreateLinearGradientBrush(self, x1, y1, x2, y2, stops, matrix=NullGraphicsMatrix) -> 'GraphicsBrush':
        """ Creates a native brush with a linear gradient.
        """

    def CreateMatrix(self, a=1.0, b=0.0, c=0.0, d=1.0, tx=0.0, ty=0.0) -> 'GraphicsMatrix':
        """ Creates a native affine transformation matrix from the passed in values.
        """

    def CreateMeasuringContext(self) -> 'GraphicsContext':
        """ Creates a   wx.GraphicsContext  that can be used for measuring texts only.
        """

    def CreatePath(self) -> 'GraphicsPath':
        """ Creates a native graphics path which is initially empty.
        """

    def CreatePen(self, info: 'GraphicsPenInfo') -> 'GraphicsPen':
        """ Creates a native pen from its description.
        """

    def CreateRadialGradientBrush(self, startX, startY, endX, endY, radius, stops, matrix=NullGraphicsMatrix) -> 'GraphicsBrush':
        """ Creates a native brush with a radial gradient.
        """

    def CreateSubBitmap(self, bitmap, x, y, w, h) -> 'GraphicsBitmap':
        """ Extracts a sub-bitmap from an existing bitmap.
        """

    @staticmethod
    def GetCairoRenderer() -> 'GraphicsRenderer':
        """ Returns Cairo renderer.
        """

    @staticmethod
    def GetDefaultRenderer() -> 'GraphicsRenderer':
        """ Returns the default renderer on this platform.
        """

    @staticmethod
    def GetDirect2DRenderer() -> 'GraphicsRenderer':
        """ Returns Direct2D renderer (MSW and Python3 only).
        """

    @staticmethod
    def GetGDIPlusRenderer() -> 'GraphicsRenderer':
        """ Returns GDI+ renderer (MSW only).
        """

    def GetName(self) -> str:
        """ Returns the name of the technology used by the renderer.
        """

    def GetType(self) -> None:
        """ Returns the name of the GraphicsRenderer class.
        """

    def GetVersion(self, major, minor=None, micro=None) -> None:
        """ Returns the version major, minor and micro/build of the technology used by the renderer.
        """



class Sizer(Object):
    """ Sizer is the abstract base class used for laying out subwindows in a
window.
    """
    def __init__(self) -> None:
        """ The constructor.
        """

    def Add(self, *args, **kw) -> 'SizerItem':
        """ Overloaded Implementations:
        """

    def AddMany(self, items) -> None:
        """ AddMany is a convenience method for adding several items to a sizer
at one time. Simply pass it a list of tuples, where each tuple
consists of the parameters that you would normally pass to the Add
method.
        """

    def AddSpacer(self, size: int) -> 'SizerItem':
        """ This base function adds non-stretchable space to both the horizontal and vertical orientation of the sizer.
        """

    def AddStretchSpacer(self, prop: int=1) -> 'SizerItem':
        """ Adds stretchable space to the sizer.
        """

    def CalcMin(self) -> 'Size':
        """ This method is abstract and has to be overwritten by any derived class.
        """

    def Clear(self, delete_windows: bool=False) -> None:
        """ Detaches all children from the sizer.
        """

    def ComputeFittingClientSize(self, window: 'Window') -> 'Size':
        """ Computes client area size for window  so that it matches the sizerâs minimal size.
        """

    def ComputeFittingWindowSize(self, window: 'Window') -> 'Size':
        """ Like ComputeFittingClientSize , but converts the result into window size.
        """

    def Detach(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def Fit(self, window: 'Window') -> 'Size':
        """ Tell the sizer to resize the window  so that its client area matches the sizerâs minimal size ( ComputeFittingClientSize   is called to determine it).
        """

    def FitInside(self, window: 'Window') -> None:
        """ Tell the sizer to resize the virtual size of the window  to match the sizerâs minimal size.
        """

    def GetChildren(self) -> SizerItemList:
        """ Returns the list of the items in this sizer.
        """

    def GetContainingWindow(self) -> 'Window':
        """ Returns the window this sizer is used in or None if none.
        """

    def GetItem(self, *args, **kw) -> 'SizerItem':
        """ Overloaded Implementations:
        """

    def GetItemById(self, id, recursive=False) -> 'SizerItem':
        """ Finds the item in the sizer which has the given id.
        """

    def GetItemCount(self) -> int:
        """ Returns the number of items in the sizer.
        """

    def GetMinSize(self) -> 'Size':
        """ Returns the minimal size of the sizer.
        """

    def GetPosition(self) -> 'Point':
        """ Returns the current position of the sizer.
        """

    def GetSize(self) -> 'Size':
        """ Returns the current size of the sizer.
        """

    def Hide(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def InformFirstDirection(self, direction, size, availableOtherDir) -> bool:
        """ Inform sizer about the first direction that has been decided (by parent item).
        """

    def Insert(self, *args, **kw) -> 'SizerItem':
        """ Overloaded Implementations:
        """

    def InsertSpacer(self, index, size) -> 'SizerItem':
        """ Inserts non-stretchable space to the sizer.
        """

    def InsertStretchSpacer(self, index, prop=1) -> 'SizerItem':
        """ Inserts stretchable space to the sizer.
        """

    def IsEmpty(self) -> bool:
        """ Return True if the sizer has no elements.
        """

    def IsShown(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def Layout(self) -> None:
        """ Call this to force layout of the children anew, e.g. after having added a child to or removed a child (window, other sizer or space) from the sizer while keeping the current dimension.
        """

    def Prepend(self, *args, **kw) -> 'SizerItem':
        """ Overloaded Implementations:
        """

    def PrependSpacer(self, size: int) -> 'SizerItem':
        """ Prepends non-stretchable space to the sizer.
        """

    def PrependStretchSpacer(self, prop: int=1) -> 'SizerItem':
        """ Prepends stretchable space to the sizer.
        """

    def RecalcSizes(self) -> None:
        """ This is a deprecated version of RepositionChildren()
        """

    def Remove(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def Replace(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def RepositionChildren(self, minSize: Union[tuple[int, int], 'Size']) -> None:
        """ Method which must be overridden in the derived sizer classes.
        """

    def SetContainingWindow(self, window: 'Window') -> None:
        """ Set the window this sizer is used in.
        """

    def SetDimension(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetItemMinSize(self, *args, **kw) -> None:
        """ Set an itemâs minimum size by window, sizer, or position.
        """

    def SetMinSize(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetSizeHints(self, window: 'Window') -> None:
        """ This method first calls Fit   and then wx.TopLevelWindow.SetSizeHints   on the window  passed to it.
        """

    def Show(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def ShowItems(self, show: bool) -> None:
        """ Show or hide all items managed by the sizer.
        """

    def __iter__(self) -> None:
        """ A Python convenience method that allows Sizers to act as iterables that will yield their wx.SizerItems.
        """

    def __nonzero__(self) -> None:
        """ Can be used to test if the C++ part of the sizer still exists, with
code like this:
        """

TOP: int
BOTTOM: int
LEFT: int
RIGHT: int
ALL: int
EXPAND: int
SHAPED: int
FIXED_MINSIZE: int
FIXED_MINSIZE: int
RESERVE_SPACE_EVEN_IF_HIDDEN: int
ALIGN_CENTER: int
ALIGN_CENTRE: int
ALIGN_LEFT: int
ALIGN_RIGHT: int
ALIGN_RIGHT: int
ALIGN_TOP: int
ALIGN_BOTTOM: int
ALIGN_CENTER_VERTICAL: int
ALIGN_CENTRE_VERTICAL: int
ALIGN_CENTER_HORIZONTAL: int
ALIGN_CENTRE_HORIZONTAL: int


class GUIEventLoop(EventLoopBase):
    """ A generic implementation of the GUI event loop.
    """
    def __init__(self) -> None:
        """ 
        """



class HeaderButtonParams:
    """ This struct can optionally be used with
RendererNative.DrawHeaderButton() to specify custom values used to
draw the text or bitmap label.
    """
    def __init__(self) -> None:
        """ 
        """



class HeaderColumn:
    """ Represents a column header in controls displaying tabular data such as
DataViewCtrl or Grid.
    """
    def GetAlignment(self) -> int:
        """ Returns the current column alignment.
        """

    def GetBitmap(self) -> 'Bitmap':
        """ This function exists only for backwards compatibility, itâs recommended to override GetBitmapBundle   in the new code and override this one to do nothing, as it will never be called if GetBitmapBundle   is overridden.
        """

    def GetBitmapBundle(self) -> 'BitmapBundle':
        """ Returns the bitmap in the header of the column, if any.
        """

    def GetFlags(self) -> int:
        """ Get the column flags.
        """

    def GetMinWidth(self) -> int:
        """ Return the minimal column width.
        """

    def GetTitle(self) -> str:
        """ Get the text shown in the column header.
        """

    def GetWidth(self) -> int:
        """ Returns the current width of the column.
        """

    def HasFlag(self, flag: int) -> bool:
        """ Return True if the specified flag is currently set for this column.
        """

    def IsHidden(self) -> bool:
        """ Returns True if the column is currently hidden.
        """

    def IsReorderable(self) -> bool:
        """ Returns True if the column can be dragged by user to change its order.
        """

    def IsResizeable(self) -> bool:
        """ Return True if the column can be resized by the user.
        """

    def IsShown(self) -> bool:
        """ Returns True if the column is currently shown.
        """

    def IsSortKey(self) -> bool:
        """ Returns True if the column is currently used for sorting.
        """

    def IsSortOrderAscending(self) -> bool:
        """ Returns True, if the sort order is ascending.
        """

    def IsSortable(self) -> bool:
        """ Returns True if the column can be clicked by user to sort the control contents by the field in this column.
        """

ALIGN_CENTRE: int
ALIGN_LEFT: int
ALIGN_RIGHT: int
COL_WIDTH_DEFAULT: int
COL_WIDTH_AUTOSIZE: int
COL_HIDDEN: int
COL_REORDERABLE: int
COL_HIDDEN: int
COL_SORTABLE: int


class HeaderColumnSimple(SettableHeaderColumn):
    """ Simple container for the information about the column.
    """
    def __init__(self, *args, **kw) -> None:
        """ Constructor for a column header.
        """

    def GetAlignment(self) -> int:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def GetBitmap(self) -> 'Bitmap':
        """ Trivial implementations of the base class pure virtual functions.
        """

    def GetBitmapBundle(self) -> 'BitmapBundle':
        """ Trivial implementations of the base class pure virtual functions.
        """

    def GetFlags(self) -> int:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def GetMinWidth(self) -> int:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def GetTitle(self) -> str:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def GetWidth(self) -> int:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def IsSortKey(self) -> bool:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def IsSortOrderAscending(self) -> bool:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def SetAlignment(self, align: int) -> None:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def SetBitmap(self, bitmap: 'BitmapBundle') -> None:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def SetFlags(self, flags: int) -> None:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def SetMinWidth(self, minWidth: int) -> None:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def SetSortOrder(self, ascending: bool) -> None:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def SetTitle(self, title: str) -> None:
        """ Trivial implementations of the base class pure virtual functions.
        """

    def SetWidth(self, width: int) -> None:
        """ Trivial implementations of the base class pure virtual functions.
        """



class HeaderCtrl(Control):
    """ HeaderCtrl is the control containing the column headings which is
usually used for display of tabular data.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddColumnsItems(self, menu, idColumnsBase=0) -> None:
        """ Helper function appending the checkable items corresponding to all the columns to the given menu.
        """

    def Create(self, parent, winid=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=HD_DEFAULT_STYLE, name=HeaderCtrlNameStr) -> bool:
        """ Create the header control window.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetColumn(self, idx: int) -> 'HeaderColumn':
        """ Method to be implemented by the derived classes to return the information for the given column.
        """

    def GetColumnAt(self, pos: int) -> int:
        """ Return the index of the column displayed at the given position.
        """

    def GetColumnCount(self) -> int:
        """ Return the number of columns in the control.
        """

    def GetColumnPos(self, idx: int) -> int:
        """ Get the position at which this column is currently displayed.
        """

    def GetColumnTitleWidth(self, *args, **kw) -> int:
        """ Overloaded Implementations:
        """

    def GetColumnsOrder(self) -> list[int]:
        """ Return the array describing the columns display order.
        """

    def IsEmpty(self) -> bool:
        """ Return whether the control has any columns.
        """

    @staticmethod
    def MoveColumnInOrderArray(order, idx, pos) -> None:
        """ Helper function to manipulate the array of column indices.
        """

    def OnColumnCountChanging(self, count: int) -> None:
        """ Can be overridden in the derived class to update internal data structures when the number of the columns in the control changes.
        """

    def ResetColumnsOrder(self) -> None:
        """ Reset the columns order to the natural one.
        """

    def SetColumnCount(self, count: int) -> None:
        """ Set the number of columns in the control.
        """

    def SetColumnsOrder(self, order: list[int]) -> None:
        """ Change the columns display order.
        """

    def ShowColumnsMenu(self, pt, title="") -> bool:
        """ Show the popup menu allowing the user to show or hide the columns.
        """

    def ShowCustomizeDialog(self) -> bool:
        """ Show the column customization dialog.
        """

    def UpdateColumn(self, idx: int) -> None:
        """ Update the column with the given index.
        """

    def UpdateColumnVisibility(self, idx, show) -> None:
        """ Method called when the column visibility is changed by the user.
        """

    def UpdateColumnWidthToFit(self, idx, widthTitle) -> bool:
        """ Method which may be implemented by the derived classes to allow double clicking the column separator to resize the column to fit its contents.
        """

    def UpdateColumnsOrder(self, order: list[int]) -> None:
        """ Method called when the columns order is changed in the customization dialog.
        """

HD_ALLOW_REORDER: int  #  If this style is specified (it is by default), the user can reorder the control columns by dragging them.
HD_ALLOW_HIDE: int  #  If this style is specified, the control shows a popup menu allowing the user to change the columns visibility on right mouse click. Notice that the program can always hide or show the columns, this style only affects the users capability to do it.
HD_BITMAP_ON_RIGHT: int  #  The column image, if any, will be shown on the right side if this style is used. Note that this style is only implemented in wxMSW currently and doesnât do anything under the other platforms. It is available since wxWidgets 3.1.1.
HD_DEFAULT_STYLE: int  #  Symbolic name for the default control style, currently equal to  HD_ALLOW_REORDER . ^^
EVT_HEADER_CLICK: int  #  A column heading was clicked.
EVT_HEADER_RIGHT_CLICK: int  #  A column heading was right clicked.
EVT_HEADER_MIDDLE_CLICK: int  #  A column heading was clicked with the middle mouse button.
EVT_HEADER_DCLICK: int  #  A column heading was double clicked.
EVT_HEADER_RIGHT_DCLICK: int  #  A column heading was right double clicked.
EVT_HEADER_MIDDLE_DCLICK: int  #  A column heading was double clicked with the middle mouse button.
EVT_HEADER_SEPARATOR_DCLICK: int  #  Separator to the right of the specified column was double clicked (this action is commonly used to resize the column to fit its contents width and the control provides UpdateColumnWidthToFit  method to make implementing this easier).
EVT_HEADER_BEGIN_RESIZE: int  #  The user started to drag the separator to the right of the column with the specified index (this can only happen for the columns for which wx.HeaderColumn.IsResizeable   returns True). The event can be vetoed to prevent the column from being resized. If it isnât, the resizing and end resize (or dragging cancelled) events will be generated later.
EVT_HEADER_RESIZING: int  #  The user is dragging the column with the specified index resizing it and its current width is wx.HeaderCtrlEvent.GetWidth . The event can be vetoed to stop the dragging operation completely at any time.
EVT_HEADER_END_RESIZE: int  #  The user stopped dragging the column by releasing the mouse. The column should normally be resized to the value of wx.HeaderCtrlEvent.GetWidth .
EVT_HEADER_BEGIN_REORDER: int  #  The user started to drag the column with the specified index (this can only happen for the controls with wx.HD_ALLOW_REORDER style). This event can be vetoed to prevent the column from being reordered, otherwise the end reorder message will be generated later.
EVT_HEADER_END_REORDER: int  #  The user dropped the column in its new location. The event can be vetoed to prevent the column from being placed at the new position or handled to update the display of the data in the associated control to match the new column location (available from wx.HeaderCtrlEvent.GetNewOrder ).
EVT_HEADER_DRAGGING_CANCELLED: int  #  The resizing or reordering operation currently in progress was cancelled. This can happen if the user pressed Esc key while dragging the mouse or the mouse capture was lost for some other reason. You only need to handle this event if your application entered into some modal mode when resizing or reordering began, in which case it should handle this event in addition to the matching end resizing or reordering ones. ^^
HD_ALLOW_REORDER: int
HD_ALLOW_HIDE: int
HD_BITMAP_ON_RIGHT: int
HD_DEFAULT_STYLE: int
HD_ALLOW_REORDER: int
HD_ALLOW_REORDER: int
HD_ALLOW_REORDER: int
HD_ALLOW_HIDE: int
HD_ALLOW_REORDER: int
HD_ALLOW_HIDE: int
HD_ALLOW_HIDE: int
HD_ALLOW_REORDER: int


class HeaderCtrlEvent(NotifyEvent):
    """ Event class representing the events generated by HeaderCtrl.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetColumn(self) -> int:
        """ Return the index of the column affected by this event.
        """

    def GetNewOrder(self) -> int:
        """ Return the new order of the column.
        """

    def GetWidth(self) -> int:
        """ Return the current width of the column.
        """

    def SetColumn(self, col: int) -> None:
        """ col (int) â
        """

    def SetNewOrder(self, order: int) -> None:
        """ order (int) â
        """

    def SetWidth(self, width: int) -> None:
        """ width (int) â
        """



class HeaderCtrlSimple(HeaderCtrl):
    """ HeaderCtrlSimple is a concrete header control which can be used
directly, without inheriting from it as you need to do when using
HeaderCtrl itself.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AppendColumn(self, col: 'HeaderColumnSimple') -> None:
        """ Append the column to the end of the control.
        """

    def DeleteColumn(self, idx: int) -> None:
        """ Delete the column at the given position.
        """

    def GetBestFittingWidth(self, idx: int) -> int:
        """ This function can be overridden in the classes deriving from this control instead of overriding UpdateColumnWidthToFit .
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def HideColumn(self, idx: int) -> None:
        """ Hide the column with the given index.
        """

    def InsertColumn(self, col, idx) -> None:
        """ Insert the column at the given position.
        """

    def RemoveSortIndicator(self) -> None:
        """ Remove the sort indicator from the column being used as sort key.
        """

    def ShowColumn(self, idx, show=True) -> None:
        """ Show or hide the column.
        """

    def ShowSortIndicator(self, idx, sortOrder=True) -> None:
        """ Update the column sort indicator.
        """

COL_HIDDEN: int


class HelpControllerBase(Object):
    """ This is the abstract base class a family of classes by which
applications may invoke a help viewer to provide on-line help.
    """
    def __init__(self, parentWindow: Optional['Window']=None) -> None:
        """ Constructs a help instance object, but does not invoke the help viewer.
        """

    def DisplayBlock(self, blockNo: int) -> bool:
        """ If the help viewer is not running, runs it and displays the file at the given block number.
        """

    def DisplayContents(self) -> bool:
        """ If the help viewer is not running, runs it and displays the contents.
        """

    def DisplayContextPopup(self, contextId: int) -> bool:
        """ Displays the section as a popup window using a context id.
        """

    def DisplaySection(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def DisplayTextPopup(self, text, pos) -> bool:
        """ Displays the text in a popup window, if possible.
        """

    def GetFrameParameters(self) -> tuple:
        """ For   wx.html.HtmlHelpController, returns the latest frame size and position settings and whether a new frame is drawn with each invocation.
        """

    def GetParentWindow(self) -> 'Window':
        """ Returns the window to be used as the parent for the help window.
        """

    def Initialize(self, file: str) -> bool:
        """ Initializes the help instance with a help filename.
        """

    def KeywordSearch(self, keyWord, mode=HELP_SEARCH_ALL) -> bool:
        """ If the help viewer is not running, runs it, and searches for sections matching the given keyword.
        """

    def LoadFile(self, file: str="") -> bool:
        """ If the help viewer is not running, runs it and loads the given file.
        """

    def OnQuit(self) -> None:
        """ Overridable member called when this applicationâs viewer is quit by the user.
        """

    def Quit(self) -> bool:
        """ If the viewer is running, quits it by disconnecting.
        """

    def SetFrameParameters(self, titleFormat, size, pos=DefaultPosition, newFrameEachTime=False) -> None:
        """ Set the parameters of the frame window.
        """

    def SetParentWindow(self, parentWindow: 'Window') -> None:
        """ Sets the window to be used as the parent for the help window.
        """

    def SetViewer(self, viewer, flags=HELP_NETSCAPE) -> None:
        """ Sets detailed viewer information.
        """

HELP_NETSCAPE: int


class HelpControllerHelpProvider(SimpleHelpProvider):
    """ HelpControllerHelpProvider is an implementation of HelpProvider
which supports both context identifiers and plain text help strings.
    """
    def __init__(self, hc: Optional['HelpControllerBase']=None) -> None:
        """ Note that the instance doesnât own the help controller.
        """

    def GetHelpController(self) -> 'HelpControllerBase':
        """ Returns the help controller associated with this help provider.
        """

    def SetHelpController(self, hc: 'HelpControllerBase') -> None:
        """ Sets the help controller associated with this help provider.
        """



class HelpProvider:
    """ HelpProvider is an abstract class used by a program implementing
context-sensitive help to show the help text for the given window.
    """
    def AddHelp(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    @staticmethod
    def Get() -> 'HelpProvider':
        """ Returns pointer to help provider instance.
        """

    def GetHelp(self, window: 'Window') -> str:
        """ This version associates the given text with all windows with this id.
        """

    def RemoveHelp(self, window: 'WindowBase') -> None:
        """ Removes the association between the window pointer and the help text.
        """

    @staticmethod
    def Set(helpProvider: 'HelpProvider') -> 'HelpProvider':
        """ Set the current, application-wide help provider.
        """

    def ShowHelp(self, window: 'WindowBase') -> bool:
        """ Shows help for the given window.
        """

    def ShowHelpAtPoint(self, window, point, origin) -> bool:
        """ This function may be overridden to show help for the window when it should depend on the position inside the window, By default this method forwards to ShowHelp , so it is enough to only implement the latter if the help doesnât depend on the position.
        """



class HelpEvent(CommandEvent):
    """ A help event is sent when the user has requested context-sensitive
help.
    """
    def __init__(self, type=wxEVT_NULL, winid=0, pt=DefaultPosition, origin=Origin_Unknown) -> None:
        """ Constructor.
        """

    def GetOrigin(self) -> 'HelpEvent.Origin':
        """ Returns the origin of the help event which is one of the   wx.HelpEvent.Origin   values.
        """

    def GetPosition(self) -> 'Point':
        """ Returns the left-click position of the mouse, in screen coordinates.
        """

    def SetOrigin(self, origin: HelpEvent.Origin) -> None:
        """ Set the help event origin, only used internally by wxWidgets normally.
        """

    def SetPosition(self, pt: 'Point') -> None:
        """ Sets the left-click position of the mouse, in screen coordinates.
        """

EVT_HELP: int  #  Process a  wxEVT_HELP   event.
EVT_HELP_RANGE: int  #  Process a  wxEVT_HELP   event for a range of ids. ^^


class HScrolledWindow(Panel, VarHScrollHelper):
    """ In the name of this class, âHâ stands for âhorizontalâ because it can
be used for scrolling columns of variable widths.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=PanelNameStr) -> bool:
        """ Same as the non-default constructor, but returns a status code: True if ok, False if the window couldnât be created.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

ID_ANY: int


class HTMLDataObject(DataObjectSimple):
    """ HTMLDataObject is used for working with HTML-formatted text.
    """
    def __init__(self, html: str="") -> None:
        """ Constructor.
        """

    def GetAllFormats(self, dir=DataObject.Get) -> None:
        """ Returns a list of wx.DataFormat objects which this data object
supports transferring in the given direction.
        """

    def GetHTML(self) -> str:
        """ Returns the HTML string.
        """

    def SetData(self, format, buf) -> bool:
        """ bool
        """

    def SetHTML(self, html: str) -> None:
        """ Sets the HTML string.
        """



class HVScrolledWindow(Panel, VarHVScrollHelper):
    """ This window inherits all functionality of both vertical and
horizontal, variable scrolled windows.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=PanelNameStr) -> bool:
        """ Same as the non-default constructor, but returns a status code: True if ok, False if the window couldnât be created.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

ID_ANY: int


class Icon(GDIObject):
    """ An icon is a small rectangular bitmap usually used for denoting a
minimized application.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def CopyFromBitmap(self, bmp: 'Bitmap') -> None:
        """ Copies bmp  bitmap to this icon.
        """

    def CreateFromHICON(self, hicon) -> bool:
        """ MSW-only method to create a wx.Icon from a native icon handle.
        """

    def GetDepth(self) -> int:
        """ Gets the colour depth of the icon.
        """

    def GetHandle(self) -> int:
        """ long
        """

    def GetHeight(self) -> int:
        """ Gets the height of the icon in physical pixels.
        """

    def GetLogicalHeight(self) -> float:
        """ Gets the height of the icon in logical pixels.
        """

    def GetLogicalSize(self) -> 'Size':
        """ Gets the size of the icon in logical pixels.
        """

    def GetLogicalWidth(self) -> float:
        """ Gets the width of the icon in logical pixels.
        """

    def GetScaleFactor(self) -> float:
        """ Gets the scale factor of this icon.
        """

    def GetSize(self) -> 'Size':
        """ Gets the size of the icon in physical pixels.
        """

    def GetWidth(self) -> int:
        """ Gets the width of the icon in physical pixels.
        """

    def IsOk(self) -> bool:
        """ Returns True if icon data is present.
        """

    def LoadFile(self, name, type=BITMAP_TYPE_ANY, desiredWidth=-1, desiredHeight=-1) -> bool:
        """ Loads an icon from a file or resource.
        """

    def SetDepth(self, depth: int) -> None:
        """ Sets the depth member (does not affect the icon data).
        """

    def SetHandle(self, handle) -> None:
        """ 
        """

    def SetHeight(self, height: int) -> None:
        """ Sets the height member (does not affect the icon data).
        """

    def SetWidth(self, width: int) -> None:
        """ Sets the width member (does not affect the icon data).
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """



class IconBundle(GDIObject):
    """ This class contains multiple copies of an icon in different sizes.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddIcon(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetIcon(self, *args, **kw) -> 'Icon':
        """ Overloaded Implementations:
        """

    def GetIconByIndex(self, n: int) -> 'Icon':
        """ return the icon at index (must be < GetIconCount )
        """

    def GetIconCount(self) -> int:
        """ return the number of available icons
        """

    def GetIconOfExactSize(self, size: Union[tuple[int, int], 'Size']) -> 'Icon':
        """ Returns the icon with exactly the given size or wx.NullIcon       if this size is not available.
        """

    def IsEmpty(self) -> bool:
        """ Returns True if the bundle doesnât contain any icons, False otherwise (in which case a call to GetIcon   with default parameter should return a valid icon).
        """



class IconizeEvent(Event):
    """ An event being sent when the frame is iconized (minimized) or
restored.
    """
    def __init__(self, id=0, iconized=True) -> None:
        """ Constructor.
        """

    def IsIconized(self) -> bool:
        """ Returns True if the frame has been iconized, False if it has been restored.
        """

EVT_ICONIZE: int  #  Process a  wxEVT_ICONIZE   event. ^^


class IconLocation:
    """ IconLocation is a tiny class describing the location of an
(external, i.e.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetFileName(self) -> str:
        """ string
        """

    def GetIndex(self) -> int:
        """ int
        """

    def IsOk(self) -> bool:
        """ Returns True if the object is valid, i.e. was properly initialized, and False otherwise.
        """

    def SetFileName(self, filename: str) -> None:
        """ filename (string) â
        """

    def SetIndex(self, num) -> None:
        """ 
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """



class IdleEvent(Event):
    """ This class is used for idle events, which are generated when the
system becomes idle.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    @staticmethod
    def GetMode() -> 'IdleMode':
        """ Static function returning a value specifying how wxWidgets will send idle events: to all windows, or only to those which specify that they will process the events.
        """

    def MoreRequested(self) -> bool:
        """ Returns True if the OnIdle function processing this event requested more processing time.
        """

    def RequestMore(self, needMore: bool=True) -> None:
        """ Tells wxWidgets that more processing is required.
        """

    @staticmethod
    def SetMode(mode: IdleMode) -> None:
        """ Static function for specifying how wxWidgets will send idle events: to all windows, or only to those which specify that they will process the events.
        """

EVT_IDLE: int  #  Process a  wxEVT_IDLE   event. ^^
IDLE_PROCESS_SPECIFIED: int
WS_EX_PROCESS_IDLE: int
IDLE_PROCESS_ALL: int


class IdManager:
    """ IdManager is responsible for allocating and releasing window IDs.
    """
    @staticmethod
    def ReserveId(count: int=1) -> int:
        """ Called directly by wx.Window.NewControlId , this function will create a new ID or range of IDs.
        """

    @staticmethod
    def UnreserveId(id, count=1) -> None:
        """ Called directly by wx.Window.UnreserveControlId , this function will unreserve an ID or range of IDs that is currently reserved.
        """

ID_NONE: int


class IFFHandler(ImageHandler):
    """ This is the image handler for the IFF format.
    """
    def __init__(self) -> None:
        """ Default constructor for   wx.IFFHandler.
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Called to test if this handler can read an image from the given stream.
        """

    def LoadFile(self, image, stream, verbose=True, index=-1) -> bool:
        """ Loads an image from a stream, putting the resulting data into image.
        """

    def SaveFile(self, image, stream, verbose=True) -> bool:
        """ Saves an image in the output stream.
        """



class Image(Object):
    """ This class encapsulates a platform-independent image.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    @staticmethod
    def AddHandler(handler: 'ImageHandler') -> None:
        """ Register an image handler.
        """

    def AdjustChannels(self, factor_red, factor_green, factor_blue, factor_alpha=1.0) -> 'Image':
        """ This function muliplies all 4 channels (red, green, blue, alpha) with
a factor (around 1.0). Useful for gamma correction, colour correction
and to add a certain amount of transparency to a image (fade in fade
out effects). If factor_alpha is given but the original image has no
alpha channel then a alpha channel will be added.
        """

    def Blur(self, blurRadius: int) -> 'Image':
        """ Blurs the image in both horizontal and vertical directions by the specified pixel blurRadius.
        """

    def BlurHorizontal(self, blurRadius: int) -> 'Image':
        """ Blurs the image in the horizontal direction only.
        """

    def BlurVertical(self, blurRadius: int) -> 'Image':
        """ Blurs the image in the vertical direction only.
        """

    @staticmethod
    def CanRead(*args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def ChangeBrightness(self, factor: float) -> None:
        """ Changes the brightness (value) of each pixel in the image.
        """

    def ChangeHSV(self, angleH, factorS, factorV) -> None:
        """ Changes the hue, the saturation and the brightness (value) of each pixel in the image.
        """

    def ChangeLightness(self, alpha: int) -> 'Image':
        """ Returns a changed version of the image based on the given lightness.
        """

    def ChangeSaturation(self, factor: float) -> None:
        """ Changes the saturation of each pixel in the image.
        """

    @staticmethod
    def CleanUpHandlers() -> None:
        """ Deletes all image handlers.
        """

    def Clear(self, value: int=0) -> None:
        """ Initialize the image data with zeroes (the default) or with the byte value given as value.
        """

    def ClearAlpha(self) -> None:
        """ Removes the alpha channel from the image.
        """

    def ComputeHistogram(self, histogram: 'ImageHistogram') -> int:
        """ Computes the histogram of the image.
        """

    def ConvertAlphaToMask(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def ConvertToBitmap(self, depth=-1) -> None:
        """ Convert the image to a wx.Bitmap.
        """

    def ConvertToDisabled(self, brightness: int=255) -> 'Image':
        """ Returns disabled (dimmed) version of the image.
        """

    def ConvertToGreyscale(self, *args, **kw) -> 'Image':
        """ Overloaded Implementations:
        """

    def ConvertToMono(self, r, g, b) -> 'Image':
        """ Returns monochromatic version of the image.
        """

    def ConvertToMonoBitmap(self, red, green, blue) -> None:
        """ Creates a monochrome version of the image and returns it as a wx.Bitmap.
        """

    def ConvertToRegion(self, R=-1, G=-1, B=-1, tolerance=0) -> 'Region':
        """ Create a wx.Region where the transparent areas match the given RGB values.
        """

    def Copy(self) -> 'Image':
        """ Returns an identical copy of this image.
        """

    def Create(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def Destroy(self) -> None:
        """ Destroys the image data.
        """

    def FindFirstUnusedColour(self, startR=1, startG=0, startB=0) -> tuple:
        """ Finds the first colour that is never used in the image.
        """

    @staticmethod
    def FindHandler(*args, **kw) -> 'ImageHandler':
        """ Overloaded Implementations:
        """

    @staticmethod
    def FindHandlerMime(mimetype: str) -> 'ImageHandler':
        """ Finds the handler associated with the given MIME type.
        """

    def GetAlpha(self, *args, **kw) -> int:
        """ Overloaded Implementations:
        """

    def GetAlphaBuffer(self) -> Any:
        """ Returns a writable Python buffer object that is pointing at the Alpha
data buffer inside the Image. You need to ensure that you do
not use this buffer object after the image has been destroyed.
        """

    def GetBlue(self, x, y) -> int:
        """ Returns the blue intensity at the given coordinate.
        """

    def GetData(self) -> Any:
        """ Returns a copy of the RGB bytes of the image.
        """

    def GetDataBuffer(self) -> Any:
        """ Returns a writable Python buffer object that is pointing at the RGB
image data buffer inside the Image. You need to ensure that you do
not use this buffer object after the image has been destroyed.
        """

    @staticmethod
    def GetDefaultLoadFlags() -> int:
        """ Returns the currently used default file load flags.
        """

    def GetGreen(self, x, y) -> int:
        """ Returns the green intensity at the given coordinate.
        """

    def GetHeight(self) -> int:
        """ Gets the height of the image in pixels.
        """

    @staticmethod
    def GetImageCount(*args, **kw) -> None:
        """ If the image file contains more than one image and the image handler is capable of retrieving these individually, this function will return the number of available images.
        """

    @staticmethod
    def GetImageExtWildcard() -> str:
        """ Iterates all registered   wx.ImageHandler  objects, and returns a string containing file extension masks suitable for passing to file open/save dialog boxes.
        """

    def GetLoadFlags(self) -> int:
        """ Returns the file load flags used for this object.
        """

    def GetMaskBlue(self) -> int:
        """ Gets the blue value of the mask colour.
        """

    def GetMaskGreen(self) -> int:
        """ Gets the green value of the mask colour.
        """

    def GetMaskRed(self) -> int:
        """ Gets the red value of the mask colour.
        """

    def GetOption(self, name: str) -> str:
        """ Gets a user-defined string-valued option.
        """

    def GetOptionInt(self, name: str) -> int:
        """ Gets a user-defined integer-valued option.
        """

    def GetOrFindMaskColour(self) -> tuple:
        """ Get the current mask colour or find a suitable unused colour that could be used as a mask colour.
        """

    def GetPalette(self) -> 'Palette':
        """ Returns the palette associated with the image.
        """

    def GetRed(self, x, y) -> int:
        """ Returns the red intensity at the given coordinate.
        """

    def GetSize(self) -> 'Size':
        """ Returns the size of the image in pixels.
        """

    def GetSubImage(self, rect: 'Rect') -> 'Image':
        """ Returns a sub image of the current one as long as the rect belongs entirely to the image.
        """

    def GetType(self) -> 'BitmapType':
        """ Gets the type of image found by LoadFile   or specified with SaveFile .
        """

    def GetWidth(self) -> int:
        """ Gets the width of the image in pixels.
        """

    @staticmethod
    def HSVtoRGB(hsv: HSVValue) -> RGBValue:
        """ Converts a color in HSV color space to RGB color space.
        """

    def HasAlpha(self) -> bool:
        """ Returns True if this image has alpha channel, False otherwise.
        """

    def HasMask(self) -> bool:
        """ Returns True if there is a mask active, False otherwise.
        """

    def HasOption(self, name: str) -> bool:
        """ Returns True if the given option is present.
        """

    def InitAlpha(self) -> None:
        """ Initializes the image alpha channel data.
        """

    @staticmethod
    def InitStandardHandlers() -> None:
        """ Internal use only.
        """

    @staticmethod
    def InsertHandler(handler: 'ImageHandler') -> None:
        """ Adds a handler at the start of the static list of format handlers.
        """

    def IsOk(self) -> bool:
        """ Returns True if image data is present.
        """

    def IsTransparent(self, x, y, threshold=IMAGE_ALPHA_THRESHOLD) -> bool:
        """ Returns True if the given pixel is transparent, i.e. either has the mask colour if this image has a mask or if this image has alpha channel and alpha value of this pixel is strictly less than threshold.
        """

    def LoadFile(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def Mirror(self, horizontally: bool=True) -> 'Image':
        """ Returns a mirrored copy of the image.
        """

    def Paste(self, image, x, y, alphaBlend=IMAGE_ALPHA_BLEND_OVER) -> None:
        """ Copy the data of the given image  to the specified position in this image.
        """

    @staticmethod
    def RGBtoHSV(rgb: RGBValue) -> HSVValue:
        """ Converts a color in RGB color space to HSV color space.
        """

    @staticmethod
    def RemoveHandler(name: str) -> bool:
        """ Finds the handler with the given name, and removes it.
        """

    def Replace(self, r1, g1, b1, r2, g2, b2) -> None:
        """ Replaces the colour specified by r1,g1,b1 by the colour r2,g2,b2.
        """

    def Rescale(self, width, height, quality=IMAGE_QUALITY_NORMAL) -> 'Image':
        """ Changes the size of the image in-place by scaling it: after a call to this function,the image will have the given width and height.
        """

    def Resize(self, size, pos, red=-1, green=-1, blue=-1) -> 'Image':
        """ Changes the size of the image in-place without scaling it by adding either a border with the given colour or cropping as necessary.
        """

    def Rotate(self, angle, rotationCentre, interpolating=True, offsetAfterRotation=None) -> 'Image':
        """ Rotates the image about the given point, by angle  radians.
        """

    def Rotate180(self) -> 'Image':
        """ Returns a copy of the image rotated by 180 degrees.
        """

    def Rotate90(self, clockwise: bool=True) -> 'Image':
        """ Returns a copy of the image rotated 90 degrees in the direction indicated by clockwise.
        """

    def RotateHue(self, angle: float) -> None:
        """ Rotates the hue of each pixel in the image by angle, which is a float in the range [-1.0..+1.0], where -1.0 corresponds to -360 degrees and +1.0 corresponds to +360 degrees.
        """

    def SaveFile(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def Scale(self, width, height, quality=IMAGE_QUALITY_NORMAL) -> 'Image':
        """ Returns a scaled version of the image.
        """

    def SetAlpha(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetAlphaBuffer(self, alpha) -> None:
        """ Sets the internal image alpha pointer to point at a Python buffer
object.  This can save making an extra copy of the data but you must
ensure that the buffer object lives lives at least as long as the
Image does.
        """

    def SetData(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetDataBuffer(self, *args, **kw) -> None:
        """ Sets the internal image data pointer to point at a Python buffer
object.  This can save making an extra copy of the data but you must
ensure that the buffer object lives lives at least as long as the
Image does.
        """

    @staticmethod
    def SetDefaultLoadFlags(flags: int) -> None:
        """ Sets the default value for the flags used for loading image files.
        """

    def SetLoadFlags(self, flags: int) -> None:
        """ Sets the flags used for loading image files by this object.
        """

    def SetMask(self, hasMask: bool=True) -> None:
        """ Specifies whether there is a mask or not.
        """

    def SetMaskColour(self, red, green, blue) -> None:
        """ Sets the mask colour for this image (and tells the image to use the mask).
        """

    def SetMaskFromImage(self, mask, mr, mg, mb) -> bool:
        """ Sets imageâs mask so that the pixels that have RGB value of mr,mg,mb in mask will be masked in the image.
        """

    def SetOption(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetPalette(self, palette: 'Palette') -> None:
        """ Associates a palette with the image.
        """

    def SetRGB(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetType(self, type: BitmapType) -> None:
        """ Set the type of image returned by GetType .
        """

    def Size(self, size, pos, red=-1, green=-1, blue=-1) -> 'Image':
        """ Returns a resized version of this image without scaling it by adding either a border with the given colour or cropping as necessary.
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """

BITMAP_TYPE_BMP: int
BITMAP_TYPE_GIF: int
BITMAP_TYPE_JPEG: int
BITMAP_TYPE_PNG: int
BITMAP_TYPE_PCX: int
BITMAP_TYPE_PNM: int
BITMAP_TYPE_TIFF: int
BITMAP_TYPE_TGA: int
BITMAP_TYPE_XPM: int
BITMAP_TYPE_ICO: int
BITMAP_TYPE_CUR: int
BITMAP_TYPE_ANI: int
BITMAP_TYPE_ANY: int
BITMAP_TYPE_BMP: int
BITMAP_TYPE_GIF: int
BITMAP_TYPE_JPEG: int
BITMAP_TYPE_PNG: int
BITMAP_TYPE_PCX: int
BITMAP_TYPE_PNM: int
BITMAP_TYPE_TIFF: int
BITMAP_TYPE_TGA: int
BITMAP_TYPE_XPM: int
BITMAP_TYPE_ICO: int
BITMAP_TYPE_CUR: int
BITMAP_TYPE_ANI: int
BITMAP_TYPE_ANY: int
BITMAP_TYPE_BMP: int
BITMAP_TYPE_GIF: int
BITMAP_TYPE_JPEG: int
BITMAP_TYPE_PNG: int
BITMAP_TYPE_PCX: int
BITMAP_TYPE_PNM: int
BITMAP_TYPE_TIFF: int
BITMAP_TYPE_TGA: int
BITMAP_TYPE_XPM: int
BITMAP_TYPE_ICO: int
BITMAP_TYPE_CUR: int
BITMAP_TYPE_ANI: int
BITMAP_TYPE_ANY: int
BITMAP_TYPE_BMP: int
BITMAP_TYPE_JPEG: int
BITMAP_TYPE_PNG: int
BITMAP_TYPE_PCX: int
BITMAP_TYPE_PNM: int
BITMAP_TYPE_TIFF: int
BITMAP_TYPE_XPM: int
BITMAP_TYPE_ICO: int
BITMAP_TYPE_CUR: int


class ImageDataObject(CustomDataObject):
    """ ImageDataObject is a specialization of DataObject for image data.
    """
    def __init__(self, image: 'Image'=NullImage) -> None:
        """ Constructor, optionally passing an image (otherwise use SetImage   later).
        """

    def GetAllFormats(self, dir=DataObject.Get) -> None:
        """ Returns a list of wx.DataFormat objects which this data object
supports transferring in the given direction.
        """

    def GetImage(self) -> 'Image':
        """ Returns the image associated with the data object.
        """

    def SetData(self, format, buf) -> bool:
        """ bool
        """

    def SetImage(self, image: 'Image') -> None:
        """ Sets the image stored by the data object.
        """



class ImageHandler(Object):
    """ This is the base class for implementing image file loading/saving, and
image creation from data.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def CanRead(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Called to test if this handler can read an image from the given stream.
        """

    def DoGetImageCount(self, stream: 'InputStream') -> int:
        """ Called to get the number of images available in a multi-image file type, if supported.
        """

    def GetAltExtensions(self) -> list[str]:
        """ Returns the other file extensions associated with this handler.
        """

    def GetExtension(self) -> str:
        """ Gets the preferred file extension associated with this handler.
        """

    def GetImageCount(self, stream: 'InputStream') -> int:
        """ If the image file contains more than one image and the image handler is capable of retrieving these individually, this function will return the number of available images.
        """

    def GetMimeType(self) -> str:
        """ Gets the MIME type associated with this handler.
        """

    def GetName(self) -> str:
        """ Gets the name of this handler.
        """

    def GetType(self) -> 'BitmapType':
        """ Gets the image type associated with this handler.
        """

    def LoadFile(self, image, stream, verbose=True, index=-1) -> bool:
        """ Loads an image from a stream, putting the resulting data into image.
        """

    def SaveFile(self, image, stream, verbose=True) -> bool:
        """ Saves an image in the output stream.
        """

    def SetAltExtensions(self, extensions: list[str]) -> None:
        """ Sets the alternative file extensions associated with this handler.
        """

    def SetExtension(self, extension: str) -> None:
        """ Sets the preferred file extension associated with this handler.
        """

    def SetMimeType(self, mimetype: str) -> None:
        """ Sets the handler MIME type.
        """

    def SetName(self, name: str) -> None:
        """ Sets the handler name.
        """

    def SetType(self, type: BitmapType) -> None:
        """ Sets the bitmap type for the handler.
        """



class ImageHistogram:
    """ startR (int) â 
    """
    def __init__(self) -> None:
        """ 
        """

    def FindFirstUnusedColour(self, startR=1, startG=0, startB=0) -> tuple:
        """ startR (int) â
        """

    @staticmethod
    def MakeKey(r, g, b) -> int:
        """ r (int) â
        """



class ImageList(Object):
    """ A ImageList contains a list of images, which are stored in an
unspecified form.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Add(self, *args, **kw) -> int:
        """ Overloaded Implementations:
        """

    def Create(self, width, height, mask=True, initialCount=1) -> bool:
        """ Initializes the list.
        """

    def Destroy(self) -> None:
        """ Destroys the current list.
        """

    def Draw(self, index, dc, x, y, flags=IMAGELIST_DRAW_NORMAL, solidBackground=False) -> bool:
        """ Draws a specified image onto a device context.
        """

    def GetBitmap(self, index: int) -> 'Bitmap':
        """ Returns the bitmap corresponding to the given index.
        """

    def GetIcon(self, index: int) -> 'Icon':
        """ Returns the icon corresponding to the given index.
        """

    def GetImageCount(self) -> int:
        """ Returns the number of images in the list.
        """

    def GetSize(self, *args, **kw) -> tuple:
        """ Overloaded Implementations:
        """

    def Remove(self, index: int) -> bool:
        """ Removes the image at the given position.
        """

    def RemoveAll(self) -> bool:
        """ Removes all the images in the list.
        """

    def Replace(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

IMAGELIST_DRAW_NORMAL: int
IMAGELIST_DRAW_TRANSPARENT: int
IMAGELIST_DRAW_SELECTED: int
IMAGELIST_DRAW_FOCUSED: int


class IndividualLayoutConstraint(Object):
    """ sibling (wx.Window) â 
    """
    def __init__(self) -> None:
        """ 
        """

    def Above(self, sibling, margin=LAYOUT_DEFAULT_MARGIN) -> None:
        """ sibling (wx.Window) â
        """

    def Absolute(self, val: int) -> None:
        """ val (int) â
        """

    def AsIs(self) -> None:
        """ 
        """

    def Below(self, sibling, margin=LAYOUT_DEFAULT_MARGIN) -> None:
        """ sibling (wx.Window) â
        """

    def GetDone(self) -> bool:
        """ bool
        """

    def GetEdge(self, which, thisWin, other) -> int:
        """ which (Edge) â
        """

    def GetMargin(self) -> int:
        """ int
        """

    def GetMyEdge(self) -> 'Edge':
        """ wx.Edge
        """

    def GetOtherEdge(self) -> int:
        """ int
        """

    def GetOtherWindow(self) -> 'Window':
        """ wx.Window
        """

    def GetPercent(self) -> int:
        """ int
        """

    def GetRelationship(self) -> 'Relationship':
        """ wx.Relationship
        """

    def GetValue(self) -> int:
        """ int
        """

    def LeftOf(self, sibling, margin=LAYOUT_DEFAULT_MARGIN) -> None:
        """ sibling (wx.Window) â
        """

    def PercentOf(self, otherW, wh, per) -> None:
        """ otherW (wx.Window) â
        """

    def ResetIfWin(self, otherW: 'Window') -> bool:
        """ otherW (wx.Window) â
        """

    def RightOf(self, sibling, margin=LAYOUT_DEFAULT_MARGIN) -> None:
        """ sibling (wx.Window) â
        """

    def SameAs(self, otherW, edge, margin=LAYOUT_DEFAULT_MARGIN) -> None:
        """ otherW (wx.Window) â
        """

    def SatisfyConstraint(self, constraints, win) -> bool:
        """ constraints (wx.LayoutConstraints) â
        """

    def Set(self, rel, otherW, otherE, val=0, margin=LAYOUT_DEFAULT_MARGIN) -> None:
        """ rel (Relationship) â
        """

    def SetDone(self, d: bool) -> None:
        """ d (bool) â
        """

    def SetEdge(self, which: Edge) -> None:
        """ which (Edge) â
        """

    def SetMargin(self, m: int) -> None:
        """ m (int) â
        """

    def SetRelationship(self, r: Relationship) -> None:
        """ r (Relationship) â
        """

    def SetValue(self, v: int) -> None:
        """ v (int) â
        """

    def Unconstrained(self) -> None:
        """ 
        """



class InfoBar(Control):
    """ An info bar is a transient window shown at top or bottom of its parent
window to display non-critical information to the user.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddButton(self, btnid, label="") -> None:
        """ Add a button to be shown in the info bar.
        """

    def Create(self, parent, winid=ID_ANY) -> bool:
        """ Create the info bar window.
        """

    def Dismiss(self) -> None:
        """ Hide the info bar window.
        """

    def GetButtonCount(self) -> int:
        """ Returns the number of currently shown buttons.
        """

    def GetButtonId(self, idx: int) -> int:
        """ Returns the ID of the button at the given position.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetEffectDuration(self) -> int:
        """ Return the effect animation duration currently used.
        """

    def GetHideEffect(self) -> 'ShowEffect':
        """ Return the effect currently used for hiding the bar.
        """

    def GetShowEffect(self) -> 'ShowEffect':
        """ Return the effect currently used for showing the bar.
        """

    def HasButtonId(self, btnid: int) -> bool:
        """ Returns whether a button with the given ID is currently shown.
        """

    def RemoveButton(self, btnid: int) -> None:
        """ Remove a button previously added by AddButton .
        """

    def SetEffectDuration(self, duration: int) -> None:
        """ Set the duration of the animation used when showing or hiding the bar.
        """

    def SetFont(self, font: 'Font') -> bool:
        """ Overridden base class methods changes the font of the text message.
        """

    def SetShowHideEffects(self, showEffect, hideEffect) -> None:
        """ Set the effects to use when showing and hiding the bar.
        """

    def ShowMessage(self, msg, flags=ICON_INFORMATION) -> None:
        """ Show a message in the bar.
        """

ID_NONE: int
SHOW_EFFECT_NONE: int
SHOW_EFFECT_SLIDE_TO_BOTTOM: int
SHOW_EFFECT_SLIDE_TO_TOP: int
ICON_NONE: int
ICON_INFORMATION: int
ICON_QUESTION: int
ICON_WARNING: int
ICON_ERROR: int
ICON_NONE: int


class InitDialogEvent(Event):
    """ A InitDialogEvent is sent as a dialog or panel is being initialised.
    """
    def __init__(self, id: int=0) -> None:
        """ Constructor.
        """

EVT_INIT_DIALOG: int  #  Process a  wxEVT_INIT_DIALOG   event. ^^


class InputStream(StreamBase):
    """ InputStream is an abstract base class which may not be used
directly.
    """
    def __init__(self) -> None:
        """ Creates a dummy input stream.
        """

    def CanRead(self) -> bool:
        """ Returns True if some data is available in the stream right now, so that calling Read   wouldnât block.
        """

    def Eof(self) -> bool:
        """ Returns True after an attempt has been made to read past the end of the stream.
        """

    def GetC(self) -> int:
        """ Returns the first character in the input queue and removes it, blocking until it appears if necessary.
        """

    def LastRead(self) -> int:
        """ Returns the last number of bytes read.
        """

    def Peek(self) -> int:
        """ Returns the first character in the input queue without removing it.
        """

    def Read(self, *args, **kw) -> 'InputStream':
        """ Overloaded Implementations:
        """

    def ReadAll(self, buffer, size) -> bool:
        """ Reads exactly the specified number of bytes into the buffer.
        """

    def SeekI(self, pos, mode=FromStart) -> 'FileOffset':
        """ Changes the stream current position.
        """

    def TellI(self) -> 'FileOffset':
        """ Returns the current stream position or InvalidOffset   if itâs not available (e.g.
        """

    def Ungetch(self, *args, **kw) -> int:
        """ Overloaded Implementations:
        """

    def close(self) -> None:
        """ 
        """

    def eof(self) -> bool:
        """ bool
        """

    def flush(self) -> None:
        """ 
        """

    def read(self, *args, **kw) -> Any:
        """ Overloaded Implementations:
        """

    def readline(self, *args, **kw) -> Any:
        """ Overloaded Implementations:
        """

    def readlines(self, *args, **kw) -> Any:
        """ Overloaded Implementations:
        """

    def seek(self, offset, whence=0) -> None:
        """ 
        """

    def tell(self) -> 'FileOffset':
        """ wx.FileOffset
        """



class InternetFSHandler(FileSystemHandler):
    """ A file system handler for accessing files from internet servers.
    """
    def __init__(self) -> None:
        """ 
        """



class ItemAttr:
    """ Represents the attributes (colour, font, â¦) of an item of a control
with multiple items such as e.g.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ Returns the currently set background colour.
        """

    def GetFont(self) -> 'Font':
        """ Returns the currently set font.
        """

    def GetTextColour(self) -> 'Colour':
        """ Returns the currently set text colour.
        """

    def HasBackgroundColour(self) -> bool:
        """ Returns True if the currently set background colour is valid.
        """

    def HasColours(self) -> bool:
        """ Returns True if either text or background colour is set.
        """

    def HasFont(self) -> bool:
        """ Returns True if the currently set font is valid.
        """

    def HasTextColour(self) -> bool:
        """ Returns True if the currently set text colour is valid.
        """

    def IsDefault(self) -> bool:
        """ Returns True if this object has no custom attributes set.
        """

    def SetBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets a new background colour.
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets a new font.
        """

    def SetTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets a new text colour.
        """

    def __ne__(self, item: Any) -> bool:
        """ Compare two item attributes for inequality.
        """

    def __eq__(self, item: Any) -> bool:
        """ Compare two item attributes for equality.
        """



class ItemContainerImmutable:
    """ ItemContainer defines an interface which is implemented by all
controls which have string subitems each of which may be selected.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def FindString(self, string, caseSensitive=False) -> int:
        """ Finds an item whose label matches the given string.
        """

    def GetCount(self) -> int:
        """ Returns the number of items in the control.
        """

    def GetSelection(self) -> int:
        """ Returns the index of the selected item or  NOT_FOUND   if no item is selected.
        """

    def GetString(self, n: int) -> str:
        """ Returns the label of the item with the given index.
        """

    def GetStringSelection(self) -> str:
        """ Returns the label of the selected item or an empty string if no item is selected.
        """

    def GetStrings(self) -> list[str]:
        """ Returns the array of the labels of all items in the control.
        """

    def IsEmpty(self) -> bool:
        """ Returns True if the control is empty or False if it has some items.
        """

    def Select(self, n: int) -> None:
        """ This is the same as SetSelection   and exists only because it is slightly more natural for controls which support multiple selection.
        """

    def SetSelection(self, n: int) -> None:
        """ Sets the selection to the given item n  or removes the selection entirely if n  ==  NOT_FOUND .
        """

    def SetString(self, n, string) -> None:
        """ Sets the label for the given item.
        """

    def SetStringSelection(self, string: str) -> bool:
        """ Selects the item with the specified string in the control.
        """

NOT_FOUND: int


class JoystickEvent(Event):
    """ This event class contains information about joystick events,
particularly events received by windows.
    """
    def __init__(self, eventType=wxEVT_NULL, state=0, joystick=JOYSTICK1, change=0) -> None:
        """ Constructor.
        """

    def ButtonDown(self, button: int=JOY_BUTTON_ANY) -> bool:
        """ Returns True if the event was a down event from the specified button (or any button).
        """

    def ButtonIsDown(self, button: int=JOY_BUTTON_ANY) -> bool:
        """ Returns True if the specified button (or any button) was in a down state.
        """

    def ButtonUp(self, button: int=JOY_BUTTON_ANY) -> bool:
        """ Returns True if the event was an up event from the specified button (or any button).
        """

    def GetButtonChange(self) -> int:
        """ Returns the identifier of the button changing state.
        """

    def GetButtonOrdinal(self) -> int:
        """ Returns the 0-indexed ordinal of the button changing state.
        """

    def GetButtonState(self) -> int:
        """ Returns the down state of the buttons.
        """

    def GetJoystick(self) -> int:
        """ Returns the identifier of the joystick generating the event - one of wx.JOYSTICK1 and wx.JOYSTICK2.
        """

    def GetPosition(self) -> 'Point':
        """ Returns the x, y position of the joystick event.
        """

    def GetZPosition(self) -> int:
        """ Returns the z position of the joystick event.
        """

    def IsButton(self) -> bool:
        """ Returns True if this was a button up or down event (not  âis any button down?â).
        """

    def IsMove(self) -> bool:
        """ Returns True if this was an x, y move event.
        """

    def IsZMove(self) -> bool:
        """ Returns True if this was a z move event.
        """

EVT_JOY_BUTTON_DOWN: int  #  Process a  wxEVT_JOY_BUTTON_DOWN   event.
EVT_JOY_BUTTON_UP: int  #  Process a  wxEVT_JOY_BUTTON_UP   event.
EVT_JOY_MOVE: int  #  Process a  wxEVT_JOY_MOVE   event.
EVT_JOY_ZMOVE: int  #  Process a  wxEVT_JOY_ZMOVE   event.
EVT_JOYSTICK_EVENTS: int  #  Processes all joystick events. ^^
JOYSTICK1: int
JOYSTICK2: int
JOYSTICK1: int
JOYSTICK2: int


class JPEGHandler(ImageHandler):
    """ This is the image handler for the JPEG format.
    """
    def __init__(self) -> None:
        """ Default constructor for   wx.JPEGHandler.
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Called to test if this handler can read an image from the given stream.
        """

    @staticmethod
    def GetLibraryVersionInfo() -> 'VersionInfo':
        """ Retrieve the version information about the JPEG library used by this handler.
        """

    def LoadFile(self, image, stream, verbose=True, index=-1) -> bool:
        """ Loads an image from a stream, putting the resulting data into image.
        """

    def SaveFile(self, image, stream, verbose=True) -> bool:
        """ Saves an image in the output stream.
        """



class KeyboardState:
    """ Provides methods for testing the state of the keyboard modifier keys.
    """
    def __init__(self, controlDown=False, shiftDown=False, altDown=False, metaDown=False) -> None:
        """ Constructor initializes the modifier key settings.
        """

    def AltDown(self) -> bool:
        """ Returns True if the Alt key is pressed.
        """

    def CmdDown(self) -> bool:
        """ Returns True if the key used for command accelerators is pressed.
        """

    def ControlDown(self) -> bool:
        """ Returns True if the Control key or Apple/Command key under macOS is pressed.
        """

    def GetModifiers(self) -> int:
        """ Return the bit mask of all pressed modifier keys.
        """

    def HasAnyModifiers(self) -> bool:
        """ Returns True if any modifiers at all are pressed.
        """

    def HasModifiers(self) -> bool:
        """ Returns True if Control or Alt are pressed.
        """

    def MetaDown(self) -> bool:
        """ Returns True if the Meta/Windows/Apple key is pressed.
        """

    def RawControlDown(self) -> bool:
        """ Returns True if the Control key (also under macOS).
        """

    def SetAltDown(self, down: bool) -> None:
        """ down (bool) â
        """

    def SetControlDown(self, down: bool) -> None:
        """ down (bool) â
        """

    def SetMetaDown(self, down: bool) -> None:
        """ down (bool) â
        """

    def SetRawControlDown(self, down: bool) -> None:
        """ down (bool) â
        """

    def SetShiftDown(self, down: bool) -> None:
        """ down (bool) â
        """

    def ShiftDown(self) -> bool:
        """ Returns True if the Shift key is pressed.
        """



class KeyEvent(Event, KeyboardState):
    """ This event class contains information about key press and release
events.
    """
    def __init__(self, keyEventType: int=wxEVT_NULL) -> None:
        """ Constructor.
        """

    def DoAllowNextEvent(self) -> None:
        """ Allow normal key events generation.
        """

    def GetKeyCode(self) -> int:
        """ Returns the key code of the key that generated this event.
        """

    def GetPosition(self) -> 'Point':
        """ Obtains the position (in client coordinates) at which the key was pressed.
        """

    def GetRawKeyCode(self) -> 'int':
        """ Returns the raw key code for this event.
        """

    def GetRawKeyFlags(self) -> 'int':
        """ Returns the low level key flags for this event.
        """

    def GetUnicodeKey(self) -> int:
        """ Returns the Unicode character corresponding to this key event.
        """

    def GetX(self) -> 'Coord':
        """ Returns the X position (in client coordinates) of the event.
        """

    def GetY(self) -> 'Coord':
        """ Returns the Y position (in client coordinates) of the event.
        """

    def IsAutoRepeat(self) -> bool:
        """ Returns True if this event is an auto-repeat of the key, False if this is the initial key press.
        """

    def IsKeyInCategory(self, category: int) -> bool:
        """ Returns True if the key is in the given key category.
        """

    def IsNextEventAllowed(self) -> bool:
        """ Returns True if DoAllowNextEvent   had been called, False by default.
        """

    def SetKeyCode(self, keyCode) -> None:
        """ 
        """

    def SetRawKeyCode(self, rawKeyCode) -> None:
        """ 
        """

    def SetRawKeyFlags(self, rawFlags) -> None:
        """ 
        """

    def SetUnicodeKey(self, uniChar) -> None:
        """ 
        """

EVT_KEY_DOWN: int  #  Process a  wxEVT_KEY_DOWN   event (any key has been pressed). If this event is handled and not skipped,   wxEVT_CHAR   will not be generated at all for this key press (but   wxEVT_KEY_UP   will be).
EVT_KEY_UP: int  #  Process a  wxEVT_KEY_UP   event (any key has been released).
EVT_CHAR: int  #  Process a  wxEVT_CHAR   event.
EVT_CHAR_HOOK: int  #  Process a  wxEVT_CHAR_HOOK   event. Unlike all the other key events, this event is propagated upwards the window hierarchy which allows intercepting it in the parent window of the focused window to which it is sent initially (if there is no focused window, this event is sent to the    wx.App  global object). It is also generated before any other key events and so gives the parent window an opportunity to modify the keyboard handling of its children, e.g. it is used internally by wxWidgets in some ports to intercept pressing Esc key in any child of a dialog to close the dialog itself when itâs pressed. By default, if this event is handled, i.e. the handler doesnât call wx.Event.Skip , neither  wxEVT_KEY_DOWN   nor   wxEVT_CHAR   events will be generated (although   wxEVT_KEY_UP   still will be), i.e. it replaces the normal key events. However by calling the special  DoAllowNextEvent  method you can handle  wxEVT_CHAR_HOOK   and still allow normal events generation. This is something that is rarely useful but can be required if you need to prevent a parent   wxEVT_CHAR_HOOK   handler from running without suppressing the normal key events. Finally notice that this event is not generated when the mouse is captured as it is considered that the window which has the capture should receive all the keyboard events too without allowing its parent    wx.TopLevelWindow  to interfere with their processing. ^^


class LanguageInfo:
    """ Encapsulates a Language identifier together with OS-specific
information related to that language.
    """
    def GetCanonicalWithRegion(self) -> str:
        """ Return the canonical locale name including the region, if known.
        """

    def GetLocaleName(self) -> str:
        """ Return the locale name corresponding to this language usable with  setlocale()   on the current system.
        """



LANGUAGE_DEFAULT: int
LANGUAGE_UNKNOWN: int
LANGUAGE_ABKHAZIAN: int
LANGUAGE_AFAR: int
LANGUAGE_AFAR_DJIBOUTI: int
LANGUAGE_AFAR_ERITREA: int
LANGUAGE_AFAR_ETHIOPIA: int
LANGUAGE_AFRIKAANS: int
LANGUAGE_AFRIKAANS_NAMIBIA: int
LANGUAGE_AFRIKAANS_SOUTH_AFRICA: int
LANGUAGE_AGHEM: int
LANGUAGE_AGHEM_CAMEROON: int
LANGUAGE_AKAN: int
LANGUAGE_AKAN_GHANA: int
LANGUAGE_ALBANIAN: int
LANGUAGE_ALBANIAN_ALBANIA: int
LANGUAGE_ALBANIAN_KOSOVO: int
LANGUAGE_ALBANIAN_NORTH_MACEDONIA: int
LANGUAGE_ALSATIAN_FRANCE: int
LANGUAGE_AMHARIC: int
LANGUAGE_AMHARIC_ETHIOPIA: int
LANGUAGE_ARABIC: int
LANGUAGE_ARABIC_ALGERIA: int
LANGUAGE_ARABIC_BAHRAIN: int
LANGUAGE_ARABIC_CHAD: int
LANGUAGE_ARABIC_COMOROS: int
LANGUAGE_ARABIC_DJIBOUTI: int
LANGUAGE_ARABIC_EGYPT: int
LANGUAGE_ARABIC_ERITREA: int
LANGUAGE_ARABIC_IRAQ: int
LANGUAGE_ARABIC_ISRAEL: int
LANGUAGE_ARABIC_JORDAN: int
LANGUAGE_ARABIC_KUWAIT: int
LANGUAGE_ARABIC_LEBANON: int
LANGUAGE_ARABIC_LIBYA: int
LANGUAGE_ARABIC_MAURITANIA: int
LANGUAGE_ARABIC_MOROCCO: int
LANGUAGE_ARABIC_OMAN: int
LANGUAGE_ARABIC_PALESTINIAN_AUTHORITY: int
LANGUAGE_ARABIC_QATAR: int
LANGUAGE_ARABIC_SAUDI_ARABIA: int
LANGUAGE_ARABIC_SOMALIA: int
LANGUAGE_ARABIC_SOUTH_SUDAN: int
LANGUAGE_ARABIC_SUDAN: int
LANGUAGE_ARABIC_SYRIA: int
LANGUAGE_ARABIC_TUNISIA: int
LANGUAGE_ARABIC_UAE: int
LANGUAGE_ARABIC_WORLD: int
LANGUAGE_ARABIC_YEMEN: int
LANGUAGE_ARMENIAN: int
LANGUAGE_ARMENIAN_ARMENIA: int
LANGUAGE_ASSAMESE: int
LANGUAGE_ASSAMESE_INDIA: int
LANGUAGE_ASTURIAN: int
LANGUAGE_ASTURIAN_SPAIN: int
LANGUAGE_ASU: int
LANGUAGE_ASU_TANZANIA: int
LANGUAGE_AYMARA: int
LANGUAGE_AZERBAIJANI: int
LANGUAGE_AZERBAIJANI_CYRILLIC: int
LANGUAGE_AZERBAIJANI_CYRILLIC_AZERBAIJAN: int
LANGUAGE_AZERBAIJANI_LATIN: int
LANGUAGE_AZERBAIJANI_LATIN_AZERBAIJAN: int
LANGUAGE_BAFIA: int
LANGUAGE_BAFIA_CAMEROON: int
LANGUAGE_BAMANANKAN: int
LANGUAGE_BAMANANKAN_LATIN: int
LANGUAGE_BAMANANKAN_LATIN_MALI: int
LANGUAGE_BANGLA: int
LANGUAGE_BANGLA_BANGLADESH: int
LANGUAGE_BANGLA_INDIA: int
LANGUAGE_BASAA: int
LANGUAGE_BASAA_CAMEROON: int
LANGUAGE_BASHKIR: int
LANGUAGE_BASHKIR_RUSSIA: int
LANGUAGE_BASQUE: int
LANGUAGE_BASQUE_SPAIN: int
LANGUAGE_BELARUSIAN: int
LANGUAGE_BELARUSIAN_BELARUS: int
LANGUAGE_BEMBA: int
LANGUAGE_BEMBA_ZAMBIA: int
LANGUAGE_BENA: int
LANGUAGE_BENA_TANZANIA: int
LANGUAGE_BIHARI: int
LANGUAGE_BISLAMA: int
LANGUAGE_BLIN: int
LANGUAGE_BLIN_ERITREA: int
LANGUAGE_BODO: int
LANGUAGE_BODO_INDIA: int
LANGUAGE_BOSNIAN: int
LANGUAGE_BOSNIAN_CYRILLIC: int
LANGUAGE_BOSNIAN_CYRILLIC_BOSNIA_AND_HERZEGOVINA: int
LANGUAGE_BOSNIAN_LATIN: int
LANGUAGE_BOSNIAN_LATIN_BOSNIA_AND_HERZEGOVINA: int
LANGUAGE_BRETON: int
LANGUAGE_BRETON_FRANCE: int
LANGUAGE_BULGARIAN: int
LANGUAGE_BULGARIAN_BULGARIA: int
LANGUAGE_BURMESE: int
LANGUAGE_BURMESE_MYANMAR: int
LANGUAGE_CATALAN: int
LANGUAGE_CATALAN_ANDORRA: int
LANGUAGE_CATALAN_FRANCE: int
LANGUAGE_CATALAN_ITALY: int
LANGUAGE_CATALAN_SPAIN: int
LANGUAGE_CEBUANO: int
LANGUAGE_CEBUANO_LATIN: int
LANGUAGE_CEBUANO_LATIN_PHILIPPINES: int
LANGUAGE_CENTRAL_ATLAS_TAMAZIGHT: int
LANGUAGE_CENTRAL_ATLAS_TAMAZIGHT_ARABIC: int
LANGUAGE_CENTRAL_ATLAS_TAMAZIGHT_ARABIC_MOROCCO: int
LANGUAGE_CENTRAL_ATLAS_TAMAZIGHT_LATIN: int
LANGUAGE_CENTRAL_ATLAS_TAMAZIGHT_LATIN_ALGERIA: int
LANGUAGE_CENTRAL_ATLAS_TAMAZIGHT_LATIN_MOROCCO: int
LANGUAGE_CENTRAL_ATLAS_TAMAZIGHT_TIFINAGH: int
LANGUAGE_CENTRAL_ATLAS_TAMAZIGHT_TIFINAGH_MOROCCO: int
LANGUAGE_CENTRAL_KURDISH: int
LANGUAGE_CENTRAL_KURDISH_IRAQ: int
LANGUAGE_CHAKMA: int
LANGUAGE_CHAKMA_CHAKMA: int
LANGUAGE_CHAKMA_CHAKMA_BANGLADESH: int
LANGUAGE_CHAKMA_CHAKMA_INDIA: int
LANGUAGE_CHECHEN: int
LANGUAGE_CHECHEN_RUSSIA: int
LANGUAGE_CHEROKEE: int
LANGUAGE_CHEROKEE_CHEROKEE: int
LANGUAGE_CHEROKEE_US: int
LANGUAGE_CHIGA: int
LANGUAGE_CHIGA_UGANDA: int
LANGUAGE_CHINESE: int
LANGUAGE_CHINESE_CHINA: int
LANGUAGE_CHINESE_HONGKONG: int
LANGUAGE_CHINESE_MACAO: int
LANGUAGE_CHINESE_SIMPLIFIED_EXPLICIT: int
LANGUAGE_CHINESE_SIMPLIFIED_HONGKONG: int
LANGUAGE_CHINESE_SIMPLIFIED_MACAO: int
LANGUAGE_CHINESE_SINGAPORE: int
LANGUAGE_CHINESE_TAIWAN: int
LANGUAGE_CHINESE_TRADITIONAL_EXPLICIT: int
LANGUAGE_CHURCH_SLAVIC: int
LANGUAGE_CHURCH_SLAVIC_RUSSIA: int
LANGUAGE_COLOGNIAN: int
LANGUAGE_COLOGNIAN_GERMANY: int
LANGUAGE_CORNISH: int
LANGUAGE_CORNISH_UK: int
LANGUAGE_CORSICAN: int
LANGUAGE_CORSICAN_FRANCE: int
LANGUAGE_CROATIAN: int
LANGUAGE_CROATIAN_BOSNIA_AND_HERZEGOVINA: int
LANGUAGE_CROATIAN_CROATIA: int
LANGUAGE_CZECH: int
LANGUAGE_CZECH_CZECHIA: int
LANGUAGE_DANISH: int
LANGUAGE_DANISH_DENMARK: int
LANGUAGE_DANISH_GREENLAND: int
LANGUAGE_DARI: int
LANGUAGE_DARI_AFGHANISTAN: int
LANGUAGE_DIVEHI: int
LANGUAGE_DIVEHI_MALDIVES: int
LANGUAGE_DUALA: int
LANGUAGE_DUALA_CAMEROON: int
LANGUAGE_DUTCH: int
LANGUAGE_DUTCH_ARUBA: int
LANGUAGE_DUTCH_BELGIAN: int
LANGUAGE_DUTCH_BONAIRE_SINT_EUSTATIUS_AND_SABA: int
LANGUAGE_DUTCH_CURACAO: int
LANGUAGE_DUTCH_NETHERLANDS: int
LANGUAGE_DUTCH_SINT_MAARTEN: int
LANGUAGE_DUTCH_SURINAME: int
LANGUAGE_DZONGKHA: int
LANGUAGE_DZONGKHA_BHUTAN: int
LANGUAGE_EDO: int
LANGUAGE_EDO_NIGERIA: int
LANGUAGE_EMBU: int
LANGUAGE_EMBU_KENYA: int
LANGUAGE_ENGLISH: int
LANGUAGE_ENGLISH_AMERICAN_SAMOA: int
LANGUAGE_ENGLISH_ANGUILLA: int
LANGUAGE_ENGLISH_ANTIGUA_AND_BARBUDA: int
LANGUAGE_ENGLISH_AUSTRALIA: int
LANGUAGE_ENGLISH_AUSTRIA: int
LANGUAGE_ENGLISH_BAHAMAS: int
LANGUAGE_ENGLISH_BARBADOS: int
LANGUAGE_ENGLISH_BELGIUM: int
LANGUAGE_ENGLISH_BELIZE: int
LANGUAGE_ENGLISH_BERMUDA: int
LANGUAGE_ENGLISH_BOTSWANA: int
LANGUAGE_ENGLISH_BRITISH_INDIAN_OCEAN_TERRITORY: int
LANGUAGE_ENGLISH_BRITISH_VIRGIN_ISLANDS: int
LANGUAGE_ENGLISH_BURUNDI: int
LANGUAGE_ENGLISH_CAMEROON: int
LANGUAGE_ENGLISH_CANADA: int
LANGUAGE_ENGLISH_CARIBBEAN: int
LANGUAGE_ENGLISH_CARIBBEAN_CB: int
LANGUAGE_ENGLISH_CAYMAN_ISLANDS: int
LANGUAGE_ENGLISH_CHRISTMAS_ISLAND: int
LANGUAGE_ENGLISH_COCOS_KEELING_ISLANDS: int
LANGUAGE_ENGLISH_COOK_ISLANDS: int
LANGUAGE_ENGLISH_CYPRUS: int
LANGUAGE_ENGLISH_DENMARK: int
LANGUAGE_ENGLISH_DOMINICA: int
LANGUAGE_ENGLISH_EIRE: int
LANGUAGE_ENGLISH_ERITREA: int
LANGUAGE_ENGLISH_ESWATINI: int
LANGUAGE_ENGLISH_EUROPE: int
LANGUAGE_ENGLISH_FALKLAND_ISLANDS: int
LANGUAGE_ENGLISH_FIJI: int
LANGUAGE_ENGLISH_FINLAND: int
LANGUAGE_ENGLISH_GAMBIA: int
LANGUAGE_ENGLISH_GERMANY: int
LANGUAGE_ENGLISH_GHANA: int
LANGUAGE_ENGLISH_GIBRALTAR: int
LANGUAGE_ENGLISH_GRENADA: int
LANGUAGE_ENGLISH_GUAM: int
LANGUAGE_ENGLISH_GUERNSEY: int
LANGUAGE_ENGLISH_GUYANA: int
LANGUAGE_ENGLISH_HONG_KONG_SAR: int
LANGUAGE_ENGLISH_INDIA: int
LANGUAGE_ENGLISH_INDONESIA: int
LANGUAGE_ENGLISH_ISLE_OF_MAN: int
LANGUAGE_ENGLISH_ISRAEL: int
LANGUAGE_ENGLISH_JAMAICA: int
LANGUAGE_ENGLISH_JERSEY: int
LANGUAGE_ENGLISH_KENYA: int
LANGUAGE_ENGLISH_KIRIBATI: int
LANGUAGE_ENGLISH_LESOTHO: int
LANGUAGE_ENGLISH_LIBERIA: int
LANGUAGE_ENGLISH_MACAO_SAR: int
LANGUAGE_ENGLISH_MADAGASCAR: int
LANGUAGE_ENGLISH_MALAWI: int
LANGUAGE_ENGLISH_MALAYSIA: int
LANGUAGE_ENGLISH_MALTA: int
LANGUAGE_ENGLISH_MARSHALL_ISLANDS: int
LANGUAGE_ENGLISH_MAURITIUS: int
LANGUAGE_ENGLISH_MICRONESIA: int
LANGUAGE_ENGLISH_MONTSERRAT: int
LANGUAGE_ENGLISH_NAMIBIA: int
LANGUAGE_ENGLISH_NAURU: int
LANGUAGE_ENGLISH_NETHERLANDS: int
LANGUAGE_ENGLISH_NEW_ZEALAND: int
LANGUAGE_ENGLISH_NIGERIA: int
LANGUAGE_ENGLISH_NIUE: int
LANGUAGE_ENGLISH_NORFOLK_ISLAND: int
LANGUAGE_ENGLISH_NORTHERN_MARIANA_ISLANDS: int
LANGUAGE_ENGLISH_PAKISTAN: int
LANGUAGE_ENGLISH_PALAU: int
LANGUAGE_ENGLISH_PAPUA_NEW_GUINEA: int
LANGUAGE_ENGLISH_PHILIPPINES: int
LANGUAGE_ENGLISH_PITCAIRN_ISLANDS: int
LANGUAGE_ENGLISH_PUERTO_RICO: int
LANGUAGE_ENGLISH_RWANDA: int
LANGUAGE_ENGLISH_SAMOA: int
LANGUAGE_ENGLISH_SEYCHELLES: int
LANGUAGE_ENGLISH_SIERRA_LEONE: int
LANGUAGE_ENGLISH_SINGAPORE: int
LANGUAGE_ENGLISH_SINT_MAARTEN: int
LANGUAGE_ENGLISH_SLOVENIA: int
LANGUAGE_ENGLISH_SOLOMON_ISLANDS: int
LANGUAGE_ENGLISH_SOUTH_AFRICA: int
LANGUAGE_ENGLISH_SOUTH_SUDAN: int
LANGUAGE_ENGLISH_ST_HELENA_ASCENSION_TRISTAN_DA_CUNHA: int
LANGUAGE_ENGLISH_ST_KITTS_AND_NEVIS: int
LANGUAGE_ENGLISH_ST_LUCIA: int
LANGUAGE_ENGLISH_ST_VINCENT_AND_GRENADINES: int
LANGUAGE_ENGLISH_SUDAN: int
LANGUAGE_ENGLISH_SWEDEN: int
LANGUAGE_ENGLISH_SWITZERLAND: int
LANGUAGE_ENGLISH_TANZANIA: int
LANGUAGE_ENGLISH_TOKELAU: int
LANGUAGE_ENGLISH_TONGA: int
LANGUAGE_ENGLISH_TRINIDAD: int
LANGUAGE_ENGLISH_TURKS_AND_CAICOS_ISLANDS: int
LANGUAGE_ENGLISH_TUVALU: int
LANGUAGE_ENGLISH_UGANDA: int
LANGUAGE_ENGLISH_UK: int
LANGUAGE_ENGLISH_UNITED_ARAB_EMIRATES: int
LANGUAGE_ENGLISH_US: int
LANGUAGE_ENGLISH_US_OUTLYING_ISLANDS: int
LANGUAGE_ENGLISH_US_VIRGIN_ISLANDS: int
LANGUAGE_ENGLISH_VANUATU: int
LANGUAGE_ENGLISH_WORLD: int
LANGUAGE_ENGLISH_ZAMBIA: int
LANGUAGE_ENGLISH_ZIMBABWE: int
LANGUAGE_ESPERANTO: int
LANGUAGE_ESPERANTO_WORLD: int
LANGUAGE_ESTONIAN: int
LANGUAGE_ESTONIAN_ESTONIA: int
LANGUAGE_EWE: int
LANGUAGE_EWE_GHANA: int
LANGUAGE_EWE_TOGO: int
LANGUAGE_EWONDO: int
LANGUAGE_EWONDO_CAMEROON: int
LANGUAGE_FAEROESE: int
LANGUAGE_FAEROESE_DENMARK: int
LANGUAGE_FAEROESE_FAROE_ISLANDS: int
LANGUAGE_FARSI: int
LANGUAGE_FIJI: int
LANGUAGE_FILIPINO: int
LANGUAGE_FILIPINO_PHILIPPINES: int
LANGUAGE_FINNISH: int
LANGUAGE_FINNISH_FINLAND: int
LANGUAGE_FRENCH: int
LANGUAGE_FRENCH_ALGERIA: int
LANGUAGE_FRENCH_BELGIAN: int
LANGUAGE_FRENCH_BENIN: int
LANGUAGE_FRENCH_BURKINA_FASO: int
LANGUAGE_FRENCH_BURUNDI: int
LANGUAGE_FRENCH_CAMEROON: int
LANGUAGE_FRENCH_CANADIAN: int
LANGUAGE_FRENCH_CARIBBEAN: int
LANGUAGE_FRENCH_CENTRAL_AFRICAN_REPUBLIC: int
LANGUAGE_FRENCH_CHAD: int
LANGUAGE_FRENCH_COMOROS: int
LANGUAGE_FRENCH_CONGO: int
LANGUAGE_FRENCH_CONGO_DRC: int
LANGUAGE_FRENCH_COTE_DIVOIRE: int
LANGUAGE_FRENCH_DJIBOUTI: int
LANGUAGE_FRENCH_EQUATORIAL_GUINEA: int
LANGUAGE_FRENCH_FRANCE: int
LANGUAGE_FRENCH_FRENCH_GUIANA: int
LANGUAGE_FRENCH_FRENCH_POLYNESIA: int
LANGUAGE_FRENCH_GABON: int
LANGUAGE_FRENCH_GUADELOUPE: int
LANGUAGE_FRENCH_GUINEA: int
LANGUAGE_FRENCH_HAITI: int
LANGUAGE_FRENCH_LUXEMBOURG: int
LANGUAGE_FRENCH_MADAGASCAR: int
LANGUAGE_FRENCH_MALI: int
LANGUAGE_FRENCH_MARTINIQUE: int
LANGUAGE_FRENCH_MAURITANIA: int
LANGUAGE_FRENCH_MAURITIUS: int
LANGUAGE_FRENCH_MAYOTTE: int
LANGUAGE_FRENCH_MONACO: int
LANGUAGE_FRENCH_MOROCCO: int
LANGUAGE_FRENCH_NEW_CALEDONIA: int
LANGUAGE_FRENCH_NIGER: int
LANGUAGE_FRENCH_REUNION: int
LANGUAGE_FRENCH_RWANDA: int
LANGUAGE_FRENCH_SENEGAL: int
LANGUAGE_FRENCH_SEYCHELLES: int
LANGUAGE_FRENCH_ST_BARTHELEMY: int
LANGUAGE_FRENCH_ST_MARTIN: int
LANGUAGE_FRENCH_ST_PIERRE_AND_MIQUELON: int
LANGUAGE_FRENCH_SWISS: int
LANGUAGE_FRENCH_SYRIA: int
LANGUAGE_FRENCH_TOGO: int
LANGUAGE_FRENCH_TUNISIA: int
LANGUAGE_FRENCH_VANUATU: int
LANGUAGE_FRENCH_WALLIS_AND_FUTUNA: int
LANGUAGE_FRISIAN: int
LANGUAGE_FRISIAN_NETHERLANDS: int
LANGUAGE_FRIULIAN: int
LANGUAGE_FRIULIAN_ITALY: int
LANGUAGE_FULAH: int
LANGUAGE_FULAH_LATIN: int
LANGUAGE_FULAH_LATIN_BURKINA_FASO: int
LANGUAGE_FULAH_LATIN_CAMEROON: int
LANGUAGE_FULAH_LATIN_GAMBIA: int
LANGUAGE_FULAH_LATIN_GHANA: int
LANGUAGE_FULAH_LATIN_GUINEA: int
LANGUAGE_FULAH_LATIN_GUINEA_BISSAU: int
LANGUAGE_FULAH_LATIN_LIBERIA: int
LANGUAGE_FULAH_LATIN_MAURITANIA: int
LANGUAGE_FULAH_LATIN_NIGER: int
LANGUAGE_FULAH_LATIN_NIGERIA: int
LANGUAGE_FULAH_LATIN_SENEGAL: int
LANGUAGE_FULAH_LATIN_SIERRA_LEONE: int
LANGUAGE_GALICIAN: int
LANGUAGE_GALICIAN_SPAIN: int
LANGUAGE_GANDA: int
LANGUAGE_GANDA_UGANDA: int
LANGUAGE_GEORGIAN: int
LANGUAGE_GEORGIAN_GEORGIA: int
LANGUAGE_GERMAN: int
LANGUAGE_GERMAN_AUSTRIAN: int
LANGUAGE_GERMAN_BELGIUM: int
LANGUAGE_GERMAN_GERMANY: int
LANGUAGE_GERMAN_ITALY: int
LANGUAGE_GERMAN_LIECHTENSTEIN: int
LANGUAGE_GERMAN_LUXEMBOURG: int
LANGUAGE_GERMAN_SWISS: int
LANGUAGE_GREEK: int
LANGUAGE_GREEK_CYPRUS: int
LANGUAGE_GREEK_GREECE: int
LANGUAGE_GREENLANDIC: int
LANGUAGE_GUARANI: int
LANGUAGE_GUARANI_PARAGUAY: int
LANGUAGE_GUJARATI: int
LANGUAGE_GUJARATI_INDIA: int
LANGUAGE_GUSII: int
LANGUAGE_GUSII_KENYA: int
LANGUAGE_HAUSA: int
LANGUAGE_HAUSA_LATIN: int
LANGUAGE_HAUSA_LATIN_GHANA: int
LANGUAGE_HAUSA_LATIN_NIGER: int
LANGUAGE_HAUSA_LATIN_NIGERIA: int
LANGUAGE_HAWAIIAN: int
LANGUAGE_HAWAIIAN_US: int
LANGUAGE_HEBREW: int
LANGUAGE_HEBREW_ISRAEL: int
LANGUAGE_HINDI: int
LANGUAGE_HINDI_INDIA: int
LANGUAGE_HUNGARIAN: int
LANGUAGE_HUNGARIAN_HUNGARY: int
LANGUAGE_IBIBIO: int
LANGUAGE_IBIBIO_NIGERIA: int
LANGUAGE_ICELANDIC: int
LANGUAGE_ICELANDIC_ICELAND: int
LANGUAGE_IGBO: int
LANGUAGE_IGBO_NIGERIA: int
LANGUAGE_INDONESIAN: int
LANGUAGE_INDONESIAN_INDONESIA: int
LANGUAGE_INTERLINGUA: int
LANGUAGE_INTERLINGUA_WORLD: int
LANGUAGE_INTERLINGUE: int
LANGUAGE_INUKTITUT: int
LANGUAGE_INUKTITUT_LATIN: int
LANGUAGE_INUKTITUT_LATIN_CANADA: int
LANGUAGE_INUKTITUT_SYLLABICS: int
LANGUAGE_INUKTITUT_SYLLABICS_CANADA: int
LANGUAGE_INUPIAK: int
LANGUAGE_IRISH: int
LANGUAGE_IRISH_IRELAND: int
LANGUAGE_ITALIAN: int
LANGUAGE_ITALIAN_ITALY: int
LANGUAGE_ITALIAN_SAN_MARINO: int
LANGUAGE_ITALIAN_SWISS: int
LANGUAGE_ITALIAN_VATICAN_CITY: int
LANGUAGE_JAPANESE: int
LANGUAGE_JAPANESE_JAPAN: int
LANGUAGE_JAVANESE: int
LANGUAGE_JAVANESE_INDONESIA: int
LANGUAGE_JAVANESE_JAVANESE: int
LANGUAGE_JAVANESE_JAVANESE_INDONESIA: int
LANGUAGE_JOLA_FONYI: int
LANGUAGE_JOLA_FONYI_SENEGAL: int
LANGUAGE_KABUVERDIANU: int
LANGUAGE_KABUVERDIANU_CABO_VERDE: int
LANGUAGE_KABYLE: int
LANGUAGE_KABYLE_ALGERIA: int
LANGUAGE_KAKO: int
LANGUAGE_KAKO_CAMEROON: int
LANGUAGE_KALAALLISUT: int
LANGUAGE_KALENJIN: int
LANGUAGE_KALENJIN_KENYA: int
LANGUAGE_KAMBA: int
LANGUAGE_KAMBA_KENYA: int
LANGUAGE_KANNADA: int
LANGUAGE_KANNADA_INDIA: int
LANGUAGE_KANURI: int
LANGUAGE_KANURI_LATIN: int
LANGUAGE_KANURI_NIGERIA: int
LANGUAGE_KASHMIRI: int
LANGUAGE_KASHMIRI_DEVANAGARI: int
LANGUAGE_KASHMIRI_DEVANAGARI_INDIA: int
LANGUAGE_KASHMIRI_INDIA: int
LANGUAGE_KASHMIRI_PERSO_ARABIC: int
LANGUAGE_KASHMIRI_PERSO_ARABIC_INDIA: int
LANGUAGE_KAZAKH: int
LANGUAGE_KAZAKH_KAZAKHSTAN: int
LANGUAGE_KHMER: int
LANGUAGE_KHMER_CAMBODIA: int
LANGUAGE_KICHE: int
LANGUAGE_KICHE_GUATEMALA: int
LANGUAGE_KICHE_LATIN: int
LANGUAGE_KIKUYU: int
LANGUAGE_KIKUYU_KENYA: int
LANGUAGE_KINYARWANDA: int
LANGUAGE_KINYARWANDA_RWANDA: int
LANGUAGE_KIRGHIZ: int
LANGUAGE_KIRGHIZ_KYRGYZSTAN: int
LANGUAGE_KIRUNDI: int
LANGUAGE_KIRUNDI_BURUNDI: int
LANGUAGE_KONKANI: int
LANGUAGE_KONKANI_INDIA: int
LANGUAGE_KOREAN: int
LANGUAGE_KOREAN_KOREA: int
LANGUAGE_KOREAN_NORTH_KOREA: int
LANGUAGE_KOYRABORO_SENNI: int
LANGUAGE_KOYRABORO_SENNI_MALI: int
LANGUAGE_KOYRA_CHIINI: int
LANGUAGE_KOYRA_CHIINI_MALI: int
LANGUAGE_KURDISH: int
LANGUAGE_KURDISH_PERSO_ARABIC_IRAN: int
LANGUAGE_KWASIO: int
LANGUAGE_KWASIO_CAMEROON: int
LANGUAGE_LAKOTA: int
LANGUAGE_LAKOTA_US: int
LANGUAGE_LANGI: int
LANGUAGE_LANGI_TANZANIA: int
LANGUAGE_LAOTHIAN: int
LANGUAGE_LAOTHIAN_LAOS: int
LANGUAGE_LATIN: int
LANGUAGE_LATIN_WORLD: int
LANGUAGE_LATVIAN: int
LANGUAGE_LATVIAN_LATVIA: int
LANGUAGE_LINGALA: int
LANGUAGE_LINGALA_ANGOLA: int
LANGUAGE_LINGALA_CENTRAL_AFRICAN_REPUBLIC: int
LANGUAGE_LINGALA_CONGO: int
LANGUAGE_LINGALA_CONGO_DRC: int
LANGUAGE_LITHUANIAN: int
LANGUAGE_LITHUANIAN_LITHUANIA: int
LANGUAGE_LOWER_SORBIAN: int
LANGUAGE_LOWER_SORBIAN_GERMANY: int
LANGUAGE_LOW_GERMAN: int
LANGUAGE_LOW_GERMAN_GERMANY: int
LANGUAGE_LOW_GERMAN_NETHERLANDS: int
LANGUAGE_LUBA_KATANGA: int
LANGUAGE_LUBA_KATANGA_CONGO_DRC: int
LANGUAGE_LUO: int
LANGUAGE_LUO_KENYA: int
LANGUAGE_LUXEMBOURGISH: int
LANGUAGE_LUXEMBOURGISH_LUXEMBOURG: int
LANGUAGE_LUYIA: int
LANGUAGE_LUYIA_KENYA: int
LANGUAGE_MACEDONIAN: int
LANGUAGE_MACEDONIAN_NORTH_MACEDONIA: int
LANGUAGE_MACHAME: int
LANGUAGE_MACHAME_TANZANIA: int
LANGUAGE_MAKHUWA_MEETTO: int
LANGUAGE_MAKHUWA_MEETTO_MOZAMBIQUE: int
LANGUAGE_MAKONDE: int
LANGUAGE_MAKONDE_TANZANIA: int
LANGUAGE_MALAGASY: int
LANGUAGE_MALAGASY_MADAGASCAR: int
LANGUAGE_MALAY: int
LANGUAGE_MALAYALAM: int
LANGUAGE_MALAYALAM_INDIA: int
LANGUAGE_MALAY_BRUNEI: int
LANGUAGE_MALAY_MALAYSIA: int
LANGUAGE_MALAY_SINGAPORE: int
LANGUAGE_MALTESE: int
LANGUAGE_MALTESE_MALTA: int
LANGUAGE_MANIPURI: int
LANGUAGE_MANIPURI_INDIA: int
LANGUAGE_MANX: int
LANGUAGE_MANX_ISLE_OF_MAN: int
LANGUAGE_MAORI: int
LANGUAGE_MAORI_NEW_ZEALAND: int
LANGUAGE_MAPUCHE: int
LANGUAGE_MAPUCHE_CHILE: int
LANGUAGE_MARATHI: int
LANGUAGE_MARATHI_INDIA: int
LANGUAGE_MASAI: int
LANGUAGE_MASAI_KENYA: int
LANGUAGE_MASAI_TANZANIA: int
LANGUAGE_MAZANDERANI: int
LANGUAGE_MAZANDERANI_IRAN: int
LANGUAGE_MERU: int
LANGUAGE_MERU_KENYA: int
LANGUAGE_META: int
LANGUAGE_META_CAMEROON: int
LANGUAGE_MOHAWK: int
LANGUAGE_MOHAWK_CANADA: int
LANGUAGE_MOLDAVIAN: int
LANGUAGE_MONGOLIAN: int
LANGUAGE_MONGOLIAN_CYRILLIC: int
LANGUAGE_MONGOLIAN_MONGOLIA: int
LANGUAGE_MONGOLIAN_TRADITIONAL: int
LANGUAGE_MONGOLIAN_TRADITIONAL_CHINA: int
LANGUAGE_MONGOLIAN_TRADITIONAL_MONGOLIA: int
LANGUAGE_MORISYEN: int
LANGUAGE_MORISYEN_MAURITIUS: int
LANGUAGE_MUNDANG: int
LANGUAGE_MUNDANG_CAMEROON: int
LANGUAGE_NAMA: int
LANGUAGE_NAMA_NAMIBIA: int
LANGUAGE_NAURU: int
LANGUAGE_NEPALI: int
LANGUAGE_NEPALI_INDIA: int
LANGUAGE_NEPALI_NEPAL: int
LANGUAGE_NGIEMBOON: int
LANGUAGE_NGIEMBOON_CAMEROON: int
LANGUAGE_NGOMBA: int
LANGUAGE_NGOMBA_CAMEROON: int
LANGUAGE_NKO: int
LANGUAGE_NKO_GUINEA: int
LANGUAGE_NORTHERN_LURI: int
LANGUAGE_NORTHERN_LURI_IRAN: int
LANGUAGE_NORTHERN_LURI_IRAQ: int
LANGUAGE_NORTH_NDEBELE: int
LANGUAGE_NORTH_NDEBELE_ZIMBABWE: int
LANGUAGE_NORWEGIAN: int
LANGUAGE_NORWEGIAN_BOKMAL: int
LANGUAGE_NORWEGIAN_BOKMAL_NORWAY: int
LANGUAGE_NORWEGIAN_BOKMAL_SVALBARD_AND_JAN_MAYEN: int
LANGUAGE_NORWEGIAN_NYNORSK: int
LANGUAGE_NORWEGIAN_NYNORSK_NORWAY: int
LANGUAGE_NUER: int
LANGUAGE_NUER_SOUTH_SUDAN: int
LANGUAGE_NYANKOLE: int
LANGUAGE_NYANKOLE_UGANDA: int
LANGUAGE_OCCITAN: int
LANGUAGE_OCCITAN_FRANCE: int
LANGUAGE_ODIA: int
LANGUAGE_ODIA_INDIA: int
LANGUAGE_OROMO: int
LANGUAGE_OROMO_ETHIOPIA: int
LANGUAGE_OROMO_KENYA: int
LANGUAGE_OSSETIC: int
LANGUAGE_OSSETIC_GEORGIA: int
LANGUAGE_OSSETIC_RUSSIA: int
LANGUAGE_PAPIAMENTO: int
LANGUAGE_PAPIAMENTO_CARIBBEAN: int
LANGUAGE_PASHTO: int
LANGUAGE_PASHTO_AFGHANISTAN: int
LANGUAGE_PASHTO_PAKISTAN: int
LANGUAGE_PERSIAN_IRAN: int
LANGUAGE_POLISH: int
LANGUAGE_POLISH_POLAND: int
LANGUAGE_PORTUGUESE: int
LANGUAGE_PORTUGUESE_ANGOLA: int
LANGUAGE_PORTUGUESE_BRAZILIAN: int
LANGUAGE_PORTUGUESE_CABO_VERDE: int
LANGUAGE_PORTUGUESE_EQUATORIAL_GUINEA: int
LANGUAGE_PORTUGUESE_GUINEA_BISSAU: int
LANGUAGE_PORTUGUESE_LUXEMBOURG: int
LANGUAGE_PORTUGUESE_MACAO_SAR: int
LANGUAGE_PORTUGUESE_MOZAMBIQUE: int
LANGUAGE_PORTUGUESE_PORTUGAL: int
LANGUAGE_PORTUGUESE_SAO_TOME_AND_PRINCIPE: int
LANGUAGE_PORTUGUESE_SWITZERLAND: int
LANGUAGE_PORTUGUESE_TIMOR_LESTE: int
LANGUAGE_PRUSSIAN: int
LANGUAGE_PRUSSIAN_WORLD: int
LANGUAGE_PUNJABI: int
LANGUAGE_PUNJABI_ARABIC: int
LANGUAGE_PUNJABI_GURMUKHI: int
LANGUAGE_PUNJABI_INDIA: int
LANGUAGE_PUNJABI_PAKISTAN: int
LANGUAGE_QUECHUA: int
LANGUAGE_QUECHUA_BOLIVIA: int
LANGUAGE_QUECHUA_ECUADOR: int
LANGUAGE_QUECHUA_MACRO: int
LANGUAGE_QUECHUA_PERU: int
LANGUAGE_RHAETO_ROMANCE: int
LANGUAGE_RHAETO_ROMANCE_SWITZERLAND: int
LANGUAGE_ROMANIAN: int
LANGUAGE_ROMANIAN_MOLDOVA: int
LANGUAGE_ROMANIAN_ROMANIA: int
LANGUAGE_ROMBO: int
LANGUAGE_ROMBO_TANZANIA: int
LANGUAGE_RUSSIAN: int
LANGUAGE_RUSSIAN_BELARUS: int
LANGUAGE_RUSSIAN_KAZAKHSTAN: int
LANGUAGE_RUSSIAN_KYRGYZSTAN: int
LANGUAGE_RUSSIAN_MOLDOVA: int
LANGUAGE_RUSSIAN_RUSSIA: int
LANGUAGE_RUSSIAN_UKRAINE: int
LANGUAGE_RWA: int
LANGUAGE_RWA_TANZANIA: int
LANGUAGE_SAHO: int
LANGUAGE_SAHO_ERITREA: int
LANGUAGE_SAKHA: int
LANGUAGE_SAKHA_RUSSIA: int
LANGUAGE_SAMBURU: int
LANGUAGE_SAMBURU_KENYA: int
LANGUAGE_SAMI: int
LANGUAGE_SAMI_FINLAND: int
LANGUAGE_SAMI_INARI: int
LANGUAGE_SAMI_INARI_FINLAND: int
LANGUAGE_SAMI_LULE: int
LANGUAGE_SAMI_LULE_NORWAY: int
LANGUAGE_SAMI_LULE_SWEDEN: int
LANGUAGE_SAMI_NORWAY: int
LANGUAGE_SAMI_SKOLT: int
LANGUAGE_SAMI_SKOLT_FINLAND: int
LANGUAGE_SAMI_SOUTHERN: int
LANGUAGE_SAMI_SOUTHERN_NORWAY: int
LANGUAGE_SAMI_SOUTHERN_SWEDEN: int
LANGUAGE_SAMI_SWEDEN: int
LANGUAGE_SAMOAN: int
LANGUAGE_SANGHO: int
LANGUAGE_SANGHO_CENTRAL_AFRICAN_REPUBLIC: int
LANGUAGE_SANGU: int
LANGUAGE_SANGU_TANZANIA: int
LANGUAGE_SANSKRIT: int
LANGUAGE_SANSKRIT_INDIA: int
LANGUAGE_SCOTS_GAELIC: int
LANGUAGE_SCOTS_GAELIC_UK: int
LANGUAGE_SENA: int
LANGUAGE_SENA_MOZAMBIQUE: int
LANGUAGE_SERBIAN: int
LANGUAGE_SERBIAN_CYRILLIC: int
LANGUAGE_SERBIAN_CYRILLIC_BOSNIA_AND_HERZEGOVINA: int
LANGUAGE_SERBIAN_CYRILLIC_KOSOVO: int
LANGUAGE_SERBIAN_CYRILLIC_MONTENEGRO: int
LANGUAGE_SERBIAN_CYRILLIC_SERBIA: int
LANGUAGE_SERBIAN_CYRILLIC_YU: int
LANGUAGE_SERBIAN_LATIN: int
LANGUAGE_SERBIAN_LATIN_BOSNIA_AND_HERZEGOVINA: int
LANGUAGE_SERBIAN_LATIN_KOSOVO: int
LANGUAGE_SERBIAN_LATIN_MONTENEGRO: int
LANGUAGE_SERBIAN_LATIN_SERBIA: int
LANGUAGE_SERBIAN_LATIN_YU: int
LANGUAGE_SERBIAN_SERBIA: int
LANGUAGE_SERBIAN_YU: int
LANGUAGE_SERBO_CROATIAN: int
LANGUAGE_SESOTHO: int
LANGUAGE_SESOTHO_LESOTHO: int
LANGUAGE_SESOTHO_SA_LEBOA: int
LANGUAGE_SESOTHO_SA_LEBOA_SOUTH_AFRICA: int
LANGUAGE_SESOTHO_SOUTH_AFRICA: int
LANGUAGE_SETSWANA: int
LANGUAGE_SETSWANA_BOTSWANA: int
LANGUAGE_SETSWANA_SOUTH_AFRICA: int
LANGUAGE_SHAMBALA: int
LANGUAGE_SHAMBALA_TANZANIA: int
LANGUAGE_SHONA: int
LANGUAGE_SHONA_LATIN: int
LANGUAGE_SHONA_LATIN_ZIMBABWE: int
LANGUAGE_SINDHI: int
LANGUAGE_SINDHI_ARABIC: int
LANGUAGE_SINDHI_DEVANAGARI: int
LANGUAGE_SINDHI_DEVANAGARI_INDIA: int
LANGUAGE_SINDHI_PAKISTAN: int
LANGUAGE_SINHALESE: int
LANGUAGE_SINHALESE_SRI_LANKA: int
LANGUAGE_SISWATI: int
LANGUAGE_SISWATI_ESWATINI: int
LANGUAGE_SISWATI_SOUTH_AFRICA: int
LANGUAGE_SLOVAK: int
LANGUAGE_SLOVAK_SLOVAKIA: int
LANGUAGE_SLOVENIAN: int
LANGUAGE_SLOVENIAN_SLOVENIA: int
LANGUAGE_SOGA: int
LANGUAGE_SOGA_UGANDA: int
LANGUAGE_SOMALI: int
LANGUAGE_SOMALI_DJIBOUTI: int
LANGUAGE_SOMALI_ETHIOPIA: int
LANGUAGE_SOMALI_KENYA: int
LANGUAGE_SOMALI_SOMALIA: int
LANGUAGE_SOUTH_NDEBELE: int
LANGUAGE_SOUTH_NDEBELE_SOUTH_AFRICA: int
LANGUAGE_SPANISH: int
LANGUAGE_SPANISH_ARGENTINA: int
LANGUAGE_SPANISH_BELIZE: int
LANGUAGE_SPANISH_BOLIVIA: int
LANGUAGE_SPANISH_BRAZIL: int
LANGUAGE_SPANISH_CHILE: int
LANGUAGE_SPANISH_COLOMBIA: int
LANGUAGE_SPANISH_COSTA_RICA: int
LANGUAGE_SPANISH_CUBA: int
LANGUAGE_SPANISH_DOMINICAN_REPUBLIC: int
LANGUAGE_SPANISH_ECUADOR: int
LANGUAGE_SPANISH_EL_SALVADOR: int
LANGUAGE_SPANISH_EQUATORIAL_GUINEA: int
LANGUAGE_SPANISH_GUATEMALA: int
LANGUAGE_SPANISH_HONDURAS: int
LANGUAGE_SPANISH_LATIN_AMERICA: int
LANGUAGE_SPANISH_MEXICAN: int
LANGUAGE_SPANISH_NICARAGUA: int
LANGUAGE_SPANISH_PANAMA: int
LANGUAGE_SPANISH_PARAGUAY: int
LANGUAGE_SPANISH_PERU: int
LANGUAGE_SPANISH_PHILIPPINES: int
LANGUAGE_SPANISH_PUERTO_RICO: int
LANGUAGE_SPANISH_SPAIN: int
LANGUAGE_SPANISH_URUGUAY: int
LANGUAGE_SPANISH_US: int
LANGUAGE_SPANISH_VENEZUELA: int
LANGUAGE_STANDARD_MOROCCAN_TAMAZIGHT: int
LANGUAGE_STANDARD_MOROCCAN_TAMAZIGHT_TIFINAGH: int
LANGUAGE_STANDARD_MOROCCAN_TAMAZIGHT_TIFINAGH_MOROCCO: int
LANGUAGE_SUNDANESE: int
LANGUAGE_SWAHILI: int
LANGUAGE_SWAHILI_CONGO_DRC: int
LANGUAGE_SWAHILI_KENYA: int
LANGUAGE_SWAHILI_TANZANIA: int
LANGUAGE_SWAHILI_UGANDA: int
LANGUAGE_SWEDISH: int
LANGUAGE_SWEDISH_ALAND_ISLANDS: int
LANGUAGE_SWEDISH_FINLAND: int
LANGUAGE_SWEDISH_SWEDEN: int
LANGUAGE_SWISS_GERMAN: int
LANGUAGE_SWISS_GERMAN_LIECHTENSTEIN: int
LANGUAGE_SWISS_GERMAN_SWITZERLAND: int
LANGUAGE_SYRIAC: int
LANGUAGE_SYRIAC_SYRIA: int
LANGUAGE_TACHELHIT: int
LANGUAGE_TACHELHIT_LATIN: int
LANGUAGE_TACHELHIT_LATIN_MOROCCO: int
LANGUAGE_TACHELHIT_TIFINAGH: int
LANGUAGE_TACHELHIT_TIFINAGH_MOROCCO: int
LANGUAGE_TAGALOG: int
LANGUAGE_TAITA: int
LANGUAGE_TAITA_KENYA: int
LANGUAGE_TAJIK: int
LANGUAGE_TAJIK_CYRILLIC: int
LANGUAGE_TAJIK_CYRILLIC_TAJIKISTAN: int
LANGUAGE_TAMIL: int
LANGUAGE_TAMIL_INDIA: int
LANGUAGE_TAMIL_MALAYSIA: int
LANGUAGE_TAMIL_SINGAPORE: int
LANGUAGE_TAMIL_SRI_LANKA: int
LANGUAGE_TASAWAQ: int
LANGUAGE_TASAWAQ_NIGER: int
LANGUAGE_TATAR: int
LANGUAGE_TATAR_RUSSIA: int
LANGUAGE_TELUGU: int
LANGUAGE_TELUGU_INDIA: int
LANGUAGE_TESO: int
LANGUAGE_TESO_KENYA: int
LANGUAGE_TESO_UGANDA: int
LANGUAGE_THAI: int
LANGUAGE_THAI_THAILAND: int
LANGUAGE_TIBETAN: int
LANGUAGE_TIBETAN_CHINA: int
LANGUAGE_TIBETAN_INDIA: int
LANGUAGE_TIGRE: int
LANGUAGE_TIGRE_ERITREA: int
LANGUAGE_TIGRINYA: int
LANGUAGE_TIGRINYA_ERITREA: int
LANGUAGE_TIGRINYA_ETHIOPIA: int
LANGUAGE_TONGA: int
LANGUAGE_TONGA_TONGA: int
LANGUAGE_TSONGA: int
LANGUAGE_TSONGA_SOUTH_AFRICA: int
LANGUAGE_TURKISH: int
LANGUAGE_TURKISH_CYPRUS: int
LANGUAGE_TURKISH_TURKEY: int
LANGUAGE_TURKMEN: int
LANGUAGE_TURKMEN_TURKMENISTAN: int
LANGUAGE_TWI: int
LANGUAGE_UIGHUR: int
LANGUAGE_UIGHUR_CHINA: int
LANGUAGE_UKRAINIAN: int
LANGUAGE_UKRAINIAN_UKRAINE: int
LANGUAGE_UPPER_SORBIAN: int
LANGUAGE_UPPER_SORBIAN_GERMANY: int
LANGUAGE_URDU: int
LANGUAGE_URDU_INDIA: int
LANGUAGE_URDU_PAKISTAN: int
LANGUAGE_UZBEK: int
LANGUAGE_UZBEK_CYRILLIC: int
LANGUAGE_UZBEK_CYRILLIC_UZBEKISTAN: int
LANGUAGE_UZBEK_LATIN: int
LANGUAGE_UZBEK_LATIN_UZBEKISTAN: int
LANGUAGE_UZBEK_PERSO_ARABIC: int
LANGUAGE_UZBEK_PERSO_ARABIC_AFGHANISTAN: int
LANGUAGE_VAI: int
LANGUAGE_VAI_LATIN: int
LANGUAGE_VAI_LATIN_LIBERIA: int
LANGUAGE_VAI_VAI: int
LANGUAGE_VAI_VAI_LIBERIA: int
LANGUAGE_VALENCIAN: int
LANGUAGE_VENDA: int
LANGUAGE_VENDA_SOUTH_AFRICA: int
LANGUAGE_VIETNAMESE: int
LANGUAGE_VIETNAMESE_VIETNAM: int
LANGUAGE_VOLAPUK: int
LANGUAGE_VOLAPUK_WORLD: int
LANGUAGE_VUNJO: int
LANGUAGE_VUNJO_TANZANIA: int
LANGUAGE_WALSER: int
LANGUAGE_WALSER_SWITZERLAND: int
LANGUAGE_WELSH: int
LANGUAGE_WELSH_UK: int
LANGUAGE_WOLAYTTA: int
LANGUAGE_WOLAYTTA_ETHIOPIA: int
LANGUAGE_WOLOF: int
LANGUAGE_WOLOF_SENEGAL: int
LANGUAGE_XHOSA: int
LANGUAGE_XHOSA_SOUTH_AFRICA: int
LANGUAGE_YANGBEN: int
LANGUAGE_YANGBEN_CAMEROON: int
LANGUAGE_YI: int
LANGUAGE_YIDDISH: int
LANGUAGE_YIDDISH_WORLD: int
LANGUAGE_YI_CHINA: int
LANGUAGE_YORUBA: int
LANGUAGE_YORUBA_BENIN: int
LANGUAGE_YORUBA_NIGERIA: int
LANGUAGE_ZARMA: int
LANGUAGE_ZARMA_NIGER: int
LANGUAGE_ZHUANG: int
LANGUAGE_ZULU: int
LANGUAGE_ZULU_SOUTH_AFRICA: int
LANGUAGE_USER_DEFINED: int
LANGUAGE_AZERI: int
LANGUAGE_AZERI_CYRILLIC: int
LANGUAGE_AZERI_LATIN: int
LANGUAGE_BENGALI: int
LANGUAGE_BENGALI_BANGLADESH: int
LANGUAGE_BENGALI_INDIA: int
LANGUAGE_BHUTANI: int
LANGUAGE_CHINESE_SIMPLIFIED: int
LANGUAGE_CHINESE_TRADITIONAL: int
LANGUAGE_CHINESE_MACAU: int
LANGUAGE_KERNEWEK: int
LANGUAGE_MALAY_BRUNEI_DARUSSALAM: int
LANGUAGE_ORIYA: int
LANGUAGE_ORIYA_INDIA: int
LANGUAGE_SPANISH_MODERN: int
LANGUAGE_CAMBODIAN: int


class LayoutConstraints(Object):
    """ bool
    """
    def __init__(self) -> None:
        """ 
        """

    def AreSatisfied(self) -> bool:
        """ bool
        """

    def SatisfyConstraints(self, win, noChanges) -> bool:
        """ win (wx.Window) â
        """



class LinuxDistributionInfo:
    """ A structure containing information about a Linux distribution as
returned by the lsb_release utility.
    """
    def __ne__(self, item: Any) -> bool:
        """ ldi (wx.LinuxDistributionInfo) â
        """

    def __eq__(self, item: Any) -> bool:
        """ ldi (wx.LinuxDistributionInfo) â
        """



class ListCtrl(Control):
    """ A list control presents lists in a number of formats: list view,
report view, icon view and small icon view.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Append(self, entry) -> None:
        """ Append an item to the list control.  The entry parameter should be a
sequence with an item for each column
        """

    def AppendColumn(self, heading, format=LIST_FORMAT_LEFT, width=-1) -> int:
        """ Adds a new column to the list control in report view mode.
        """

    def Arrange(self, flag: int=LIST_ALIGN_DEFAULT) -> bool:
        """ Arranges the items in icon or small icon view.
        """

    def AssignImageList(self, imageList, which) -> None:
        """ Sets the image list associated with the control and takes ownership of it.
        """

    def CheckItem(self, item, check=True) -> None:
        """ Check or uncheck a   wx.ListItem  in a control using checkboxes.
        """

    def ClearAll(self) -> None:
        """ Deletes all items and all columns.
        """

    def ClearColumnImage(self, col) -> None:
        """ 
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=LC_ICON, validator=DefaultValidator, name=ListCtrlNameStr) -> bool:
        """ Creates the list control.
        """

    def DeleteAllColumns(self) -> bool:
        """ Delete all columns in the list control.
        """

    def DeleteAllItems(self) -> bool:
        """ Deletes all items in the list control.
        """

    def DeleteColumn(self, col: int) -> bool:
        """ Deletes a column.
        """

    def DeleteItem(self, item: int) -> bool:
        """ Deletes the specified item.
        """

    def EditLabel(self, item: int) -> 'TextCtrl':
        """ Starts editing the label of the given item.
        """

    def EnableAlternateRowColours(self, enable: bool=True) -> None:
        """ Enable alternating row background colours (also called zebra striping).
        """

    def EnableBellOnNoMatch(self, on: bool=True) -> None:
        """ Enable or disable a beep if there is no match for the currently entered text when searching for the item from keyboard.
        """

    def EnableCheckBoxes(self, enable: bool=True) -> bool:
        """ Enable or disable checkboxes for list items.
        """

    def EnableSystemTheme(self, enable: bool=True) -> None:
        """ Can be used to disable the system theme of controls using it by default.
        """

    def EnsureVisible(self, item: int) -> bool:
        """ Ensures this item is visible.
        """

    def ExtendRulesAndAlternateColour(self, extend: bool=True) -> None:
        """ Extend rules and alternate rows background to the entire client area.
        """

    def FindItem(self, *args, **kw) -> int:
        """ Overloaded Implementations:
        """

    def Focus(self, idx) -> None:
        """ Focus and show the given item.
        """

    def GetAlternateRowColour(self) -> 'Colour':
        """ Get the alternative row background colour.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetColumn(self, col) -> 'ListItem':
        """ Gets information about this column. See SetItem() for more information.
        """

    def GetColumnCount(self) -> int:
        """ Returns the number of columns.
        """

    def GetColumnIndexFromOrder(self, pos: int) -> int:
        """ Gets the column index from its position in visual order.
        """

    def GetColumnOrder(self, col: int) -> int:
        """ Gets the column visual order position.
        """

    def GetColumnWidth(self, col: int) -> int:
        """ Gets the column width (report view only).
        """

    def GetColumnsOrder(self) -> list[int]:
        """ Returns the array containing the orders of all columns.
        """

    def GetCountPerPage(self) -> int:
        """ Gets the number of items that can fit vertically in the visible area of the list control (list or report view) or the total number of items in the list control (icon or small icon view).
        """

    def GetEditControl(self) -> 'TextCtrl':
        """ Returns the edit control being currently used to edit a label.
        """

    def GetFirstSelected(self, *args) -> None:
        """ Returns the first selected item, or -1 when none is selected.
        """

    def GetFocusedItem(self) -> None:
        """ Gets the currently focused item or -1 if none is focused.
        """

    def GetImageList(self, which: int) -> 'ImageList':
        """ Returns the specified image list.
        """

    def GetItem(self, itemIdx, col=0) -> 'ListItem':
        """ Gets information about the item. See SetItem() for more information.
        """

    def GetItemBackgroundColour(self, item: int) -> 'Colour':
        """ Returns the colour for this item.
        """

    def GetItemCount(self) -> int:
        """ Returns the number of items in the list control.
        """

    def GetItemData(self, item: int) -> int:
        """ Gets the application-defined data associated with this item.
        """

    def GetItemFont(self, item: int) -> 'Font':
        """ Returns the itemâs font.
        """

    def GetItemPosition(self, item) -> 'Point':
        """ Returns the position of the item, in icon or small icon view.
        """

    def GetItemRect(self, item, code=LIST_RECT_BOUNDS) -> 'Rect':
        """ Returns the rectangle representing the itemâs size and position, in physical coordinates.
code is one of wx.``wx.LIST_RECT_BOUNDS``, wx.``wx.LIST_RECT_ICON``, wx.``wx.LIST_RECT_LABEL``.
        """

    def GetItemSpacing(self) -> 'Size':
        """ Retrieves the spacing between icons in pixels: horizontal spacing is returned as  x   component of the    wx.Size  object and the vertical spacing as its  y   component.
        """

    def GetItemState(self, item, stateMask) -> int:
        """ Gets the item state.
        """

    def GetItemText(self, item, col=0) -> str:
        """ Gets the item text for this item.
        """

    def GetItemTextColour(self, item: int) -> 'Colour':
        """ Returns the colour for this item.
        """

    def GetMainWindow(self) -> 'Window':
        """ wx.Window
        """

    def GetNextItem(self, item, geometry=LIST_NEXT_ALL, state=LIST_STATE_DONTCARE) -> int:
        """ Searches for an item with the given geometry or state, starting from item  but excluding the item  itself.
        """

    def GetNextSelected(self, item) -> None:
        """ Returns subsequent selected items, or -1 when no more are selected.
        """

    def GetSelectedItemCount(self) -> int:
        """ Returns the number of selected items in the list control.
        """

    def GetSortIndicator(self) -> int:
        """ Returns the column that shows the sort indicator.
        """

    def GetSubItemRect(self, item, subItem, rect, code=LIST_RECT_BOUNDS) -> bool:
        """ Returns the rectangle representing the size and position, in physical coordinates, of the given subitem, i.e.
        """

    def GetTextColour(self) -> 'Colour':
        """ Gets the text colour of the list control.
        """

    def GetTopItem(self) -> int:
        """ Gets the index of the topmost visible item when in list or report view.
        """

    def GetUpdatedAscendingSortIndicator(self, col: int) -> bool:
        """ Returns the new value to use for sort indicator after clicking a column.
        """

    def GetViewRect(self) -> 'Rect':
        """ Returns the rectangle taken by all items in the control.
        """

    def HasCheckBoxes(self) -> bool:
        """ Returns True if checkboxes are enabled for list items.
        """

    def HasColumnOrderSupport(self) -> bool:
        """ bool
        """

    def HitTest(self, point) -> None:
        """ Determines which item (if any) is at the specified point, giving details in flags.
        """

LC_LIST: int  #  Multicolumn list view, with optional small icons. Columns are computed automatically, i.e. you donât set columns as in  LC_REPORT . In other words, the list wraps, unlike a    wx.ListBox.
LC_REPORT: int  #  Single or multicolumn report view, with optional header.
LC_VIRTUAL: int  #  The application provides items text on demand. May only be used with  LC_REPORT .
LC_ICON: int  #  Large icon view, with optional labels.
LC_SMALL_ICON: int  #  Small icon view, with optional labels.
LC_ALIGN_TOP: int  #  Icons align to the top. Win32 default, Win32 only.
LC_ALIGN_LEFT: int  #  Icons align to the left.
LC_AUTOARRANGE: int  #  Icons arrange themselves. Win32 only.
LC_EDIT_LABELS: int  #  Labels are editable: int  #  the application will be notified when editing starts.
LC_NO_HEADER: int  #  No header in report mode.
LC_SINGLE_SEL: int  #  Single selection (default is multiple).
LC_SORT_ASCENDING: int  #  Sort in ascending order. (You must still supply a comparison callback in wx.ListCtrl.SortItems .)
LC_SORT_DESCENDING: int  #  Sort in descending order. (You must still supply a comparison callback in wx.ListCtrl.SortItems .)
LC_HRULES: int  #  Draws light horizontal rules between rows in report mode.
LC_VRULES: int  #  Draws light vertical rules between columns in report mode. ^^
EVT_LIST_BEGIN_DRAG: int  #  Begin dragging with the left mouse button. Processes a  wxEVT_LIST_BEGIN_DRAG   event type.
EVT_LIST_BEGIN_RDRAG: int  #  Begin dragging with the right mouse button. Processes a  wxEVT_LIST_BEGIN_RDRAG   event type.
EVT_LIST_BEGIN_LABEL_EDIT: int  #  Begin editing a label. This can be prevented by calling Veto(). Processes a  wxEVT_LIST_BEGIN_LABEL_EDIT   event type.
EVT_LIST_END_LABEL_EDIT: int  #  Finish editing a label. This can be prevented by calling Veto(). Processes a  wxEVT_LIST_END_LABEL_EDIT   event type.
EVT_LIST_DELETE_ITEM: int  #  An item was deleted. Processes a  wxEVT_LIST_DELETE_ITEM   event type.
EVT_LIST_DELETE_ALL_ITEMS: int  #  All items were deleted. Processes a  wxEVT_LIST_DELETE_ALL_ITEMS   event type.
EVT_LIST_ITEM_SELECTED: int  #  The item has been selected. Notice that the mouse is captured by the control itself when this event is generated, see event handling overview. Processes a  wxEVT_LIST_ITEM_SELECTED   event type.
EVT_LIST_ITEM_DESELECTED: int  #  The item has been deselected. Processes a  wxEVT_LIST_ITEM_DESELECTED   event type.
EVT_LIST_ITEM_ACTIVATED: int  #  The item has been activated (ENTER or double click). Processes a  wxEVT_LIST_ITEM_ACTIVATED   event type.
EVT_LIST_ITEM_FOCUSED: int  #  The currently focused item has changed. Processes a  wxEVT_LIST_ITEM_FOCUSED   event type.
EVT_LIST_ITEM_MIDDLE_CLICK: int  #  The middle mouse button has been clicked on an item. This is only supported by the generic control. Processes a  wxEVT_LIST_ITEM_MIDDLE_CLICK   event type.
EVT_LIST_ITEM_RIGHT_CLICK: int  #  The right mouse button has been clicked on an item. Processes a  wxEVT_LIST_ITEM_RIGHT_CLICK   event type.
EVT_LIST_KEY_DOWN: int  #  A key has been pressed. Processes a  wxEVT_LIST_KEY_DOWN   event type.
EVT_LIST_INSERT_ITEM: int  #  An item has been inserted. Processes a  wxEVT_LIST_INSERT_ITEM   event type.
EVT_LIST_COL_CLICK: int  #  A column (m_col) has been left-clicked. Processes a  wxEVT_LIST_COL_CLICK   event type.
EVT_LIST_COL_RIGHT_CLICK: int  #  A column (m_col) has been right-clicked. Processes a  wxEVT_LIST_COL_RIGHT_CLICK   event type.
EVT_LIST_COL_BEGIN_DRAG: int  #  The user started resizing a column - can be vetoed. Processes a  wxEVT_LIST_COL_BEGIN_DRAG   event type.
EVT_LIST_COL_DRAGGING: int  #  The divider between columns is being dragged. Processes a  wxEVT_LIST_COL_DRAGGING   event type.
EVT_LIST_COL_END_DRAG: int  #  A column has been resized by the user. Processes a  wxEVT_LIST_COL_END_DRAG   event type.
EVT_LIST_CACHE_HINT: int  #  Prepare cache for a virtual list control. Processes a  wxEVT_LIST_CACHE_HINT   event type.
EVT_LIST_ITEM_CHECKED: int  #  The item has been checked. Processes a  wxEVT_LIST_ITEM_CHECKED   event type (new since wxWidgets 3.1.0).
EVT_LIST_ITEM_UNCHECKED: int  #  The item has been unchecked. Processes a  wxEVT_LIST_ITEM_UNCHECKED   event type (new since wxWidgets 3.1.0). ^^
LC_LIST: int
LC_REPORT: int
LC_VIRTUAL: int
LC_ICON: int
LC_SMALL_ICON: int
LC_ALIGN_TOP: int
LC_ALIGN_LEFT: int
LC_AUTOARRANGE: int
LC_EDIT_LABELS: int
LC_NO_HEADER: int
LC_SINGLE_SEL: int
LC_SORT_ASCENDING: int
LC_SORT_DESCENDING: int
LC_HRULES: int
LC_VRULES: int
ID_ANY: int
LIST_ALIGN_DEFAULT: int
LIST_ALIGN_LEFT: int
LIST_ALIGN_TOP: int
LIST_ALIGN_SNAP_TO_GRID: int
LC_VIRTUAL: int
LC_HRULES: int
LC_VRULES: int
LC_REPORT: int
LC_LIST: int
LC_SMALL_ICON: int
LC_ICON: int
IMAGE_LIST_NORMAL: int
IMAGE_LIST_SMALL: int
IMAGE_LIST_STATE: int
LIST_NEXT_ABOVE: int
LIST_NEXT_ALL: int
LIST_NEXT_BELOW: int
LIST_NEXT_LEFT: int
LIST_NEXT_RIGHT: int
LIST_STATE_DONTCARE: int
LIST_STATE_DROPHILITED: int
LIST_STATE_FOCUSED: int
LIST_STATE_SELECTED: int
LIST_STATE_CUT: int
LIST_HITTEST_ABOVE: int
LIST_HITTEST_BELOW: int
LIST_HITTEST_TOLEFT: int
LIST_HITTEST_TORIGHT: int
LIST_HITTEST_NOWHERE: int
LIST_HITTEST_ONITEMICON: int
LIST_HITTEST_ONITEMLABEL: int
LIST_HITTEST_ONITEMSTATEICON: int
LIST_HITTEST_ONITEM: int
LC_ICON: int
LC_SMALL_ICON: int
LC_REPORT: int
LC_ICON: int


class ListEvent(NotifyEvent):
    """ A list event holds information about events associated with ListCtrl
objects.
    """
    def __init__(self, commandType=wxEVT_NULL, id=0) -> None:
        """ Constructor.
        """

    def GetCacheFrom(self) -> int:
        """ For  EVT_LIST_CACHE_HINT   event only: return the first item which the list control advises us to cache.
        """

    def GetCacheTo(self) -> int:
        """ For  EVT_LIST_CACHE_HINT   event only: return the last item (inclusive) which the list control advises us to cache.
        """

    def GetColumn(self) -> int:
        """ The column position: it is only used with  COL   events.
        """

    def GetData(self) -> 'UIntPtr':
        """ The data.
        """

    def GetImage(self) -> int:
        """ The image.
        """

    def GetIndex(self) -> int:
        """ The item index.
        """

    def GetItem(self) -> 'ListItem':
        """ An item object, used by some events.
        """

    def GetKeyCode(self) -> int:
        """ Key code if the event is a keypress event.
        """

    def GetLabel(self) -> str:
        """ The (new) item label for  EVT_LIST_END_LABEL_EDIT   event.
        """

    def GetMask(self) -> int:
        """ The mask.
        """

    def GetPoint(self) -> 'Point':
        """ The position of the mouse pointer if the event is a drag event.
        """

    def GetText(self) -> str:
        """ The text.
        """

    def IsEditCancelled(self) -> bool:
        """ This method only makes sense for  EVT_LIST_END_LABEL_EDIT   message and returns True if it the label editing has been cancelled by the user ( GetLabel   returns an empty string in this case but it doesnât allow the application to distinguish between really cancelling the edit and the admittedly rare case when the user wants to rename it to an empty string).
        """

    def SetCacheFrom(self, cacheFrom: int) -> None:
        """ cacheFrom (long) â
        """

    def SetCacheTo(self, cacheTo: int) -> None:
        """ cacheTo (long) â
        """

    def SetColumn(self, col: int) -> None:
        """ col (int) â
        """

    def SetIndex(self, index: int) -> None:
        """ index (long) â
        """

    def SetItem(self, item: 'ListItem') -> None:
        """ item (wx.ListItem) â
        """

    def SetKeyCode(self, code: int) -> None:
        """ code (int) â
        """

    def SetPoint(self, point: 'Point') -> None:
        """ point (wx.Point) â
        """

EVT_LIST_BEGIN_DRAG: int  #  Begin dragging with the left mouse button.
EVT_LIST_BEGIN_RDRAG: int  #  Begin dragging with the right mouse button.
EVT_LIST_BEGIN_LABEL_EDIT: int  #  Begin editing a label. This can be prevented by calling Veto
EVT_LIST_END_LABEL_EDIT: int  #  Finish editing a label. This can be prevented by calling Veto
EVT_LIST_DELETE_ITEM: int  #  Delete an item.
EVT_LIST_DELETE_ALL_ITEMS: int  #  Delete all items.
EVT_LIST_ITEM_SELECTED: int  #  The item has been selected. Notice that the mouse is captured by the control itself when this event is generated, see event handling overview.
EVT_LIST_ITEM_DESELECTED: int  #  The item has been deselected. GetIndex  may be -1 with virtual lists.
EVT_LIST_ITEM_ACTIVATED: int  #  The item has been activated (ENTER or double click).
EVT_LIST_ITEM_FOCUSED: int  #  The currently focused item has changed.
EVT_LIST_ITEM_MIDDLE_CLICK: int  #  The middle mouse button has been clicked on an item.
EVT_LIST_ITEM_RIGHT_CLICK: int  #  The right mouse button has been clicked on an item.
EVT_LIST_KEY_DOWN: int  #  A key has been pressed. GetIndex  may be -1 if no item is selected.
EVT_LIST_INSERT_ITEM: int  #  An item has been inserted.
EVT_LIST_COL_CLICK: int  #  A column (m_col) has been left-clicked.
EVT_LIST_COL_RIGHT_CLICK: int  #  A column (m_col) (which can be -1 if the click occurred outside any column) has been right-clicked.
EVT_LIST_COL_BEGIN_DRAG: int  #  The user started resizing a column - can be vetoed.
EVT_LIST_COL_DRAGGING: int  #  The divider between columns is being dragged.
EVT_LIST_COL_END_DRAG: int  #  A column has been resized by the user.
EVT_LIST_CACHE_HINT: int  #  Prepare cache for a virtual list control
EVT_LIST_ITEM_CHECKED: int  #  The item has been checked (new since wxWidgets 3.1.0).
EVT_LIST_ITEM_UNCHECKED: int  #  The item has been unchecked (new since wxWidgets 3.1.0). ^^


class ListItem(Object):
    """ This class stores information about a ListCtrl item or column.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def Clear(self) -> None:
        """ Resets the item state to the default.
        """

    def GetAlign(self) -> 'ListColumnFormat':
        """ Returns the alignment for this item.
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ Returns the background colour for this item.
        """

    def GetColumn(self) -> int:
        """ Returns the zero-based column; meaningful only in report mode.
        """

    def GetData(self) -> int:
        """ Returns client data associated with the control.
        """

    def GetFont(self) -> 'Font':
        """ Returns the font used to display the item.
        """

    def GetId(self) -> int:
        """ Returns the zero-based item position.
        """

    def GetImage(self) -> int:
        """ Returns the zero-based index of the image associated with the item into the image list.
        """

    def GetMask(self) -> int:
        """ Returns a bit mask indicating which fields of the structure are valid.
        """

    def GetState(self) -> int:
        """ Returns a bit field representing the state of the item.
        """

    def GetText(self) -> str:
        """ Returns the label/header text.
        """

    def GetTextColour(self) -> 'Colour':
        """ Returns the text colour.
        """

    def GetWidth(self) -> int:
        """ Meaningful only for column headers in report mode.
        """

    def SetAlign(self, align: ListColumnFormat) -> None:
        """ Sets the alignment for the item.
        """

    def SetBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ Sets the background colour for the item.
        """

    def SetColumn(self, col: int) -> None:
        """ Sets the zero-based column.
        """

    def SetData(self, data: int) -> None:
        """ Sets client data for the item.
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the font for the item.
        """

    def SetId(self, id: int) -> None:
        """ Sets the zero-based item position.
        """

    def SetImage(self, image: int) -> None:
        """ Sets the zero-based index of the image associated with the item into the image list.
        """

    def SetMask(self, mask: int) -> None:
        """ Sets the mask of valid fields.
        """

    def SetState(self, state: int) -> None:
        """ Sets the item state flags (note that the valid state flags are influenced by the value of the state mask, see wx.ListItem.SetStateMask ).
        """

    def SetStateMask(self, stateMask: int) -> None:
        """ Sets the bitmask that is used to determine which of the state flags are to be set.
        """

    def SetText(self, text: str) -> None:
        """ Sets the text label for the item.
        """

    def SetTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ Sets the text colour for the item.
        """

    def SetWidth(self, width: int) -> None:
        """ Meaningful only for column headers in report mode.
        """

LIST_MASK_STATE: int
LIST_MASK_TEXT: int
LIST_MASK_IMAGE: int
LIST_MASK_DATA: int
LIST_MASK_WIDTH: int
LIST_MASK_FORMAT: int
LIST_STATE_DONTCARE: int
LIST_STATE_DROPHILITED: int
LIST_STATE_FOCUSED: int
LIST_STATE_SELECTED: int
LIST_STATE_CUT: int


class ListView(ListCtrl):
    """ This class currently simply presents a simpler to use interface for
the ListCtrl  it can be thought of as a faÃ§ade for that complicated
class.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def ClearColumnImage(self, col: int) -> None:
        """ Resets the column image â  after calling this function, no image will be shown.
        """

    def Focus(self, index: int) -> None:
        """ Sets focus to the item with the given index.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetFirstSelected(self) -> int:
        """ Returns the first selected item in a (presumably) multiple selection control.
        """

    def GetFocusedItem(self) -> int:
        """ Returns the currently focused item or -1 if none.
        """

    def GetNextSelected(self, item: int) -> int:
        """ Used together with GetFirstSelected   to iterate over all selected items in the control.
        """

    def IsSelected(self, index: int) -> bool:
        """ Returns True if the item with the given index  is selected, False otherwise.
        """

    def Select(self, n, on=True) -> None:
        """ Selects or unselects the given item.
        """

    def SetColumnImage(self, col, image) -> None:
        """ Sets the column image for the specified column.
        """

ID_ANY: int


class Locale:
    """ Locale class encapsulates all language-dependent settings and is a
generalization of the C locale concept.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddCatalog(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    @staticmethod
    def AddCatalogLookupPathPrefix(prefix: str) -> None:
        """ Calls wx.FileTranslationsLoader.AddCatalogLookupPathPrefix .
        """

    @staticmethod
    def AddLanguage(info: 'LanguageInfo') -> None:
        """ Adds custom, user-defined language to the database of known languages.
        """

    @staticmethod
    def FindLanguageInfo(locale: str) -> 'LanguageInfo':
        """ This function may be used to find the language description structure for the given locale, specified either as a two letter ISO language code (for example, âptâ), a language code followed by the country code (âpt_BRâ) or a full, human readable, language description (âPortuguese_Brazilâ).
        """

    def GetCanonicalName(self) -> str:
        """ Returns the canonical form of current locale name.
        """

    def GetHeaderValue(self, header, domain="") -> str:
        """ Calls wx.Translations.GetHeaderValue .
        """

    @staticmethod
    def GetInfo(index, cat=LOCALE_CAT_DEFAULT) -> str:
        """ Get the values of the given locale-dependent datum.
        """

    def GetLanguage(self) -> int:
        """ Returns the   wx.Language  constant of current language.
        """

    @staticmethod
    def GetLanguageCanonicalName(lang: int) -> str:
        """ Returns canonical name (see GetCanonicalName ) of the given language or empty string if this language is unknown.
        """

    @staticmethod
    def GetLanguageInfo(lang: int) -> 'LanguageInfo':
        """ Returns a pointer to   wx.LanguageInfo  structure containing information about the given language or None if this language is unknown.
        """

    @staticmethod
    def GetLanguageName(lang: int) -> str:
        """ Returns English name of the given language or empty string if this language is unknown.
        """

    def GetLocale(self) -> str:
        """ Returns the locale name as passed to the constructor or Init .
        """

    def GetName(self) -> str:
        """ Returns the current short name for the locale (as given to the constructor or the Init   function).
        """

    @staticmethod
    def GetOSInfo(index, cat=LOCALE_CAT_DEFAULT) -> str:
        """ Get the values of a locale datum in the OS locale.
        """

    def GetString(self, *args, **kw) -> str:
        """ Overloaded Implementations:
        """

    def GetSysName(self) -> str:
        """ Returns current platform-specific locale name as passed to setlocale().
        """

    @staticmethod
    def GetSystemEncoding() -> int:
        """ Tries to detect the userâs default font encoding.
        """

    @staticmethod
    def GetSystemEncodingName() -> str:
        """ Tries to detect the name of the userâs default font encoding.
        """

    @staticmethod
    def GetSystemLanguage() -> int:
        """ Tries to detect the userâs default locale setting.
        """

    def Init(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    @staticmethod
    def IsAvailable(lang: int) -> bool:
        """ Check whether the operating system and/or C run time environment supports this locale.
        """

    def IsLoaded(self, domain: str) -> bool:
        """ Calls wx.Translations.IsLoaded .
        """

    def IsOk(self) -> bool:
        """ Returns True if the locale could be set successfully.
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """

LOCALE_CAT_DEFAULT: int
LOCALE_LOAD_DEFAULT: int
LOCALE_DONT_LOAD_DEFAULT: int
LOCALE_LOAD_DEFAULT: int


class Log:
    """ Log class defines the interface for the log targets used by
wxWidgets logging functions as explained in the Logging Overview.
    """
    @staticmethod
    def AddTraceMask(mask: str) -> None:
        """ Add the mask  to the list of allowed masks for wx.LogTrace     .
        """

    @staticmethod
    def ClearTraceMasks() -> None:
        """ Removes all trace masks previously set with AddTraceMask .
        """

    @staticmethod
    def DisableTimestamp() -> None:
        """ Disables time stamping of the log messages.
        """

    def DoLogRecord(self, level, msg, info) -> None:
        """ Called to log a new record.
        """

    def DoLogText(self, msg: str) -> None:
        """ Called to log the specified string.
        """

    def DoLogTextAtLevel(self, level, msg) -> None:
        """ Called to log the specified string at given level.
        """

    @staticmethod
    def DontCreateOnDemand() -> None:
        """ Instructs   wx.Log  to not create new log targets on the fly if there is none currently (see GetActiveTarget ).
        """

    @staticmethod
    def EnableLogging(enable: bool=True) -> bool:
        """ Globally enable or disable logging.
        """

    def Flush(self) -> None:
        """ Show all pending output and clear the buffer.
        """

    @staticmethod
    def FlushActive() -> None:
        """ Flushes the current log target if any, does nothing if there is none.
        """

    @staticmethod
    def GetActiveTarget() -> 'Log':
        """ Returns the pointer to the active log target (may be None).
        """

    @staticmethod
    def GetLogLevel() -> 'LogLevel':
        """ Returns the current log level limit.
        """

    @staticmethod
    def GetRepetitionCounting() -> bool:
        """ Returns whether the repetition counting mode is enabled.
        """

    @staticmethod
    def GetTimestamp() -> str:
        """ Returns the current timestamp format string.
        """

    @staticmethod
    def GetTraceMasks() -> list[str]:
        """ Returns the currently allowed list of string trace masks.
        """

    @staticmethod
    def GetVerbose() -> bool:
        """ Returns whether the verbose mode is currently active.
        """

    @staticmethod
    def IsAllowedTraceMask(mask: str) -> bool:
        """ Returns True if the mask  is one of allowed masks for wx.LogTrace     .
        """

    @staticmethod
    def IsEnabled() -> bool:
        """ Returns True if logging is enabled at all now.
        """

    @staticmethod
    def IsLevelEnabled(level, component) -> bool:
        """ Returns True if logging at this level is enabled for the current thread.
        """

    def LogRecord(self, level, msg, info) -> None:
        """ Log the given record.
        """

    @staticmethod
    def RemoveTraceMask(mask: str) -> None:
        """ Remove the mask  from the list of allowed masks for wx.LogTrace     .
        """

    @staticmethod
    def Resume() -> None:
        """ Resumes logging previously suspended by a call to Suspend .
        """

    @staticmethod
    def SetActiveTarget(logtarget: 'Log') -> 'Log':
        """ Sets the specified log target as the active one.
        """

    @staticmethod
    def SetComponentLevel(component, level) -> None:
        """ Sets the log level for the given component.
        """

    def SetFormatter(self, formatter: 'LogFormatter') -> 'LogFormatter':
        """ Sets the specified formatter as the active one.
        """

    @staticmethod
    def SetLogLevel(logLevel: 'LogLevel') -> None:
        """ Specifies that log messages with level greater (numerically) than logLevel  should be ignored and not sent to the active log target.
        """

    @staticmethod
    def SetRepetitionCounting(repetCounting: bool=True) -> None:
        """ Enables logging mode in which a log message is logged once, and in case exactly the same message successively repeats one or more times, only the number of repetitions is logged.
        """

    @staticmethod
    def SetThreadActiveTarget(logger: 'Log') -> 'Log':
        """ Sets a thread-specific log target.
        """

    @staticmethod
    def SetTimestamp(format: str) -> None:
        """ Sets the timestamp format prepended by the default log targets to all messages.
        """

    @staticmethod
    def SetVerbose(verbose: bool=True) -> None:
        """ Activates or deactivates verbose mode in which the verbose messages are logged as the normal ones instead of being silently dropped.
        """

    @staticmethod
    def Suspend() -> None:
        """ Suspends the logging until Resume   is called.
        """



class LogBuffer(Log):
    """ LogBuffer is a very simple implementation of log sink which simply
collects all the logged messages in a string (except the debug
messages which are output in the usual way immediately as weâre
presumably not interested in collecting them for later).
    """
    def __init__(self) -> None:
        """ The default constructor does nothing.
        """

    def Flush(self) -> None:
        """ Shows all the messages collected so far to the user (using a message box in the GUI applications or by printing them out to the console in text mode) and clears the internal buffer.
        """

    def GetBuffer(self) -> str:
        """ Returns the current buffer contains.
        """



class LogChain(Log):
    """ This simple class allows you to chain log sinks, that is to install a
new sink but keep passing log messages to the old one instead of
replacing it completely as Log.SetActiveTarget does.
    """
    def __init__(self, logger: 'Log') -> None:
        """ Sets the specified  logger   (which may be None) as the default log target but the log messages are also passed to the previous log target if any.
        """

    def DetachOldLog(self) -> None:
        """ Detaches the old log target so it wonât be destroyed when the   wx.LogChain  object is destroyed.
        """

    def GetOldLog(self) -> 'Log':
        """ Returns the pointer to the previously active log target (which may be None).
        """

    def IsPassingMessages(self) -> bool:
        """ Returns True if the messages are passed to the previously active log target (default) or False if PassMessages   had been called.
        """

    def PassMessages(self, passMessages: bool) -> None:
        """ By default, the log messages are passed to the previously active log target.
        """

    def SetLog(self, logger: 'Log') -> None:
        """ Sets another log target to use (may be None).
        """



class LogFormatter:
    """ LogFormatter class is used to format the log messages.
    """
    def __init__(self) -> None:
        """ The default constructor does nothing.
        """

    def Format(self, level, msg, info) -> str:
        """ This function creates the full log message string.
        """

    def FormatTime(self, time: int) -> str:
        """ This function formats the time stamp part of the log message.
        """



class LogGui(Log):
    """ This is the default log target for the GUI wxWidgets applications.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def Flush(self) -> None:
        """ Presents the accumulated log messages, if any, to the user.
        """



class LogInterposer(LogChain):
    """ A special version of LogChain which uses itself as the new log
target.
    """
    def __init__(self) -> None:
        """ The default constructor installs this object as the current active log target.
        """



class LogInterposerTemp(LogChain):
    """ A special version of LogChain which uses itself as the new log
target.
    """
    def __init__(self) -> None:
        """ The default constructor installs this object as the current active log target.
        """



class LogNull:
    """ This class allows you to temporarily suspend logging.
    """
    def __init__(self) -> None:
        """ Suspends logging.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class LogRecordInfo:
    """ Information about a log record (unit of the log output).
    """


class LogStderr(Log):
    """ This class can be used to redirect the log messages to a C file stream
(not to be confused with C++ streams).
    """
    def __init__(self) -> None:
        """ Constructs a log target which sends all the log messages to the given  FILE .
        """



class LogTextCtrl(Log):
    """ Using these target all the log messages can be redirected to a text
control.
    """
    def __init__(self, pTextCtrl: 'TextCtrl') -> None:
        """ Constructs a log target which sends all the log messages to the given text control.
        """



class LogWindow(LogInterposer):
    """ This class represents a background log window: to be precise, it
collects all log messages in the log frame which it manages but also
passes them on to the log target which was active at the moment of its
creation.
    """
    def __init__(self, pParent, szTitle, show=True, passToOld=True) -> None:
        """ Creates the log frame window and starts collecting the messages in it.
        """

    def GetFrame(self) -> 'Frame':
        """ Returns the associated log frame window.
        """

    def OnFrameClose(self, frame: 'Frame') -> bool:
        """ Called if the user closes the window interactively, will not be called if it is destroyed for another reason (such as when program exits).
        """

    def OnFrameDelete(self, frame: 'Frame') -> None:
        """ Called right before the log frame is going to be deleted: will always be called unlike OnFrameClose .
        """

    def Show(self, show: bool=True) -> None:
        """ Shows or hides the frame.
        """



class LongPressEvent(GestureEvent):
    """ This event is generated when one finger touches the surface and
remains stationary.
    """
    def __init__(self, windid: int=0) -> None:
        """ Constructor.
        """

EVT_LONG_PRESS: int  #  Process a  wxEVT_LONG_PRESS . ^^


class Mask(Object):
    """ This class encapsulates a monochrome mask bitmap, where the masked
area is black and the unmasked area is white.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetBitmap(self) -> 'Bitmap':
        """ Returns the mask as a monochrome bitmap.
        """



class Matrix2D:
    """ A simple container for 2x2 matrix.
    """
    def __init__(self, v11=1, v12=0, v21=0, v22=1) -> None:
        """ Default constructor.
        """



class MaximizeEvent(Event):
    """ An event being sent when a top level window is maximized.
    """
    def __init__(self, id: int=0) -> None:
        """ Constructor.
        """

EVT_MAXIMIZE: int  #  Process a  wxEVT_MAXIMIZE   event. ^^


class MDIChildFrame(Frame):
    """ An MDI child frame is a frame that can only exist inside a
MDIClientWindow, which is itself a child of MDIParentFrame.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Activate(self) -> None:
        """ Activates this MDI child frame.
        """

    def Create(self, parent, id=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE, name=FrameNameStr) -> bool:
        """ Used in two-step frame construction.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetMDIParent(self) -> 'MDIParentFrame':
        """ Returns the MDI parent frame containing this child.
        """

    def IsAlwaysMaximized(self) -> bool:
        """ Returns True for MDI children in TDI implementations.
        """

    def Maximize(self, maximize: bool=True) -> None:
        """ Maximizes this MDI child frame.
        """

    def Restore(self) -> None:
        """ Restores this MDI child frame (unmaximizes).
        """



class MDIClientWindow(Window):
    """ An MDI client window is a child of MDIParentFrame, and manages zero
or more MDIChildFrame objects.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def CreateClient(self, parent, style=0) -> bool:
        """ Called by   wx.MDIParentFrame  immediately after creating the client window.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

HSCROLL: int
VSCROLL: int


class MDIParentFrame(Frame):
    """ An MDI (Multiple Document Interface) parent frame is a window which
can contain MDI child frames in its client area which emulates the
full desktop.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def ActivateNext(self) -> None:
        """ Activates the MDI child following the currently active one.
        """

    def ActivatePrevious(self) -> None:
        """ Activates the MDI child preceding the currently active one.
        """

    def ArrangeIcons(self) -> None:
        """ Arranges any iconized (minimized) MDI child windows.
        """

    def Cascade(self) -> None:
        """ Arranges the MDI child windows in a cascade.
        """

    def Create(self, parent, id=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE|VSCROLL|HSCROLL, name=FrameNameStr) -> bool:
        """ Used in two-step frame construction.
        """

    def GetActiveChild(self) -> 'MDIChildFrame':
        """ Returns a pointer to the active MDI child, if there is one.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetClientWindow(self) -> 'MDIClientWindow':
        """ Returns a pointer to the client window.
        """

    def GetWindowMenu(self) -> 'Menu':
        """ Returns the current MDI Window menu.
        """

    @staticmethod
    def IsTDI() -> bool:
        """ Returns whether the MDI implementation is tab-based.
        """

    def OnCreateClient(self) -> 'MDIClientWindow':
        """ Override this to return a different kind of client window.
        """

    def SetWindowMenu(self, menu: 'Menu') -> None:
        """ Replace the current MDI Window menu.
        """

    def Tile(self, orient: Orientation=HORIZONTAL) -> None:
        """ Tiles the MDI child windows either horizontally or vertically depending on whether orient  is  HORIZONTAL   or   VERTICAL .
        """

HSCROLL: int
VSCROLL: int
HSCROLL: int
VSCROLL: int
FRAME_NO_WINDOW_MENU: int
FRAME_NO_WINDOW_MENU: int


class MemoryDC(DC):
    """ A memory device context provides a means to draw graphics onto a
bitmap.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetSelectedBitmap(self) -> 'Bitmap':
        """ wx.Bitmap
        """

    def SelectObject(self, bitmap: 'Bitmap') -> None:
        """ Allow using this device context object to modify the given bitmap contents.
        """

    def SelectObjectAsSource(self, bitmap: 'Bitmap') -> None:
        """ Selects the given bitmap into the device context, to use as the memory bitmap.
        """



class MemoryFSHandler(FileSystemHandler):
    """ This FileSystem handler can store arbitrary data in memory stream
and make them accessible via an URL.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    @staticmethod
    def AddFile(*args, **kw) -> None:
        """ Overloaded Implementations:
        """

    @staticmethod
    def AddFileWithMimeType(*args, **kw) -> None:
        """ Overloaded Implementations:
        """

    @staticmethod
    def RemoveFile(filename: str) -> None:
        """ Removes a file from memory FS and frees the occupied memory.
        """



class Menu(EvtHandler):
    """ A menu is a popup (or pull down) list of items, one of which may be
selected before the menu goes away (clicking elsewhere dismisses the
menu).
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Append(self, *args, **kw) -> 'MenuItem':
        """ Overloaded Implementations:
        """

    def AppendCheckItem(self, id, item, help="") -> 'MenuItem':
        """ Adds a checkable item to the end of the menu.
        """

    def AppendRadioItem(self, id, item, help="") -> 'MenuItem':
        """ Adds a radio item to the end of the menu.
        """

    def AppendSeparator(self) -> 'MenuItem':
        """ Adds a separator to the end of the menu.
        """

    def AppendSubMenu(self, submenu, text, help="") -> 'MenuItem':
        """ Adds the given submenu  to this menu.
        """

    def Attach(self, menubar: 'MenuBar') -> None:
        """ menubar (wx.MenuBar) â
        """

    def Break(self) -> None:
        """ Inserts a break in a menu, causing the next appended item to appear in a new column.
        """

    def Check(self, id, check) -> None:
        """ Checks or unchecks the menu item.
        """

    def Delete(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def DestroyItem(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def Detach(self) -> None:
        """ 
        """

    def Enable(self, id, enable) -> None:
        """ Enables or disables (greys out) a menu item.
        """

    def FindChildItem(self, id: int) -> tuple:
        """ Finds the menu item object associated with the given menu item identifier and, optionally, the position of the item in the menu.
        """

    def FindItem(self, *args, **kw) -> int:
        """ Overloaded Implementations:
        """

    def FindItemById(self, id) -> 'MenuItem':
        """ FindItemById(id) . MenuItem
        """

    def FindItemByPosition(self, position: int) -> 'MenuItem':
        """ Returns the   wx.MenuItem  given a position in the menu.
        """

    def GetHelpString(self, id: int) -> str:
        """ Returns the help string associated with a menu item.
        """

    def GetInvokingWindow(self) -> 'Window':
        """ wx.Window
        """

    def GetLabel(self, id: int) -> str:
        """ Returns a menu item label.
        """

    def GetLabelText(self, id: int) -> str:
        """ Returns a menu item label, without any of the original mnemonics and accelerators.
        """

    def GetMenuItemCount(self) -> int:
        """ Returns the number of items in the menu.
        """

    def GetMenuItems(self) -> MenuItemList:
        """ Returns the list of items in the menu.
        """

    def GetParent(self) -> 'Menu':
        """ wx.Menu
        """

    def GetStyle(self) -> int:
        """ long
        """

    def GetTitle(self) -> str:
        """ Returns the title of the menu.
        """

    def GetWindow(self) -> 'Window':
        """ wx.Window
        """

    def Insert(self, *args, **kw) -> 'MenuItem':
        """ Overloaded Implementations:
        """

    def InsertCheckItem(self, pos, id, item, helpString="") -> 'MenuItem':
        """ Inserts a checkable item at the given position.
        """

    def InsertRadioItem(self, pos, id, item, helpString="") -> 'MenuItem':
        """ Inserts a radio item at the given position.
        """

    def InsertSeparator(self, pos: int) -> 'MenuItem':
        """ Inserts a separator at the given position.
        """

    def IsAttached(self) -> bool:
        """ bool
        """

    def IsChecked(self, id: int) -> bool:
        """ Determines whether a menu item is checked.
        """

    def IsEnabled(self, id: int) -> bool:
        """ Determines whether a menu item is enabled.
        """

    def Prepend(self, *args, **kw) -> 'MenuItem':
        """ Overloaded Implementations:
        """

    def PrependCheckItem(self, id, item, helpString="") -> 'MenuItem':
        """ Inserts a checkable item at position 0.
        """

    def PrependRadioItem(self, id, item, helpString="") -> 'MenuItem':
        """ Inserts a radio item at position 0.
        """

    def PrependSeparator(self) -> 'MenuItem':
        """ Inserts a separator at position 0.
        """

    def Remove(self, *args, **kw) -> 'MenuItem':
        """ Overloaded Implementations:
        """

    def SetHelpString(self, id, helpString) -> None:
        """ Sets an itemâs help string.
        """

    def SetInvokingWindow(self, win: 'Window') -> None:
        """ win (wx.Window) â
        """

    def SetLabel(self, id, label) -> None:
        """ Sets the label of a menu item.
        """

    def SetParent(self, parent: 'Menu') -> None:
        """ parent (wx.Menu) â
        """

    def SetTitle(self, title: str) -> None:
        """ Sets the title of the menu.
        """

    def UpdateUI(self, source: Optional['EvtHandler']=None) -> None:
        """ Update the state of all menu items, recursively, by generating  wxEVT_UPDATE_UI   events for them.
        """

ID_SEPARATOR: int
ID_ABOUT: int
ID_EXIT: int
MENU_TEAROFF: int
MENU_TEAROFF: int
NOT_FOUND: int


class MenuBar(Window):
    """ A menu bar is a series of menus accessible from the top of a frame.
    """
    def __init__(self, style: int=0) -> None:
        """ Construct an empty menu bar.
        """

    def Append(self, menu, title) -> bool:
        """ Adds the item to the end of the menu bar.
        """

    def Attach(self, frame: 'Frame') -> None:
        """ frame (wx.Frame) â
        """

    def Check(self, id, check) -> None:
        """ Checks or unchecks a menu item.
        """

    def Detach(self) -> None:
        """ 
        """

    def Enable(self, id, enable) -> None:
        """ Enables or disables (greys out) a menu item.
        """

    def EnableTop(self, pos, enable) -> None:
        """ Enables or disables a whole menu.
        """

    def FindItem(self, id: int) -> tuple:
        """ Finds the menu item object associated with the given menu item identifier.
        """

    def FindItemById(self, id) -> 'MenuItem':
        """ FindItemById(id) . MenuItem
        """

    def FindMenu(self, title: str) -> int:
        """ Returns the index of the menu with the given title  or  NOT_FOUND   if no such menu exists in this menubar.
        """

    def FindMenuItem(self, menuString, itemString) -> int:
        """ Finds the menu item id for a menu name/menu item string pair.
        """

    def GetFrame(self) -> 'Frame':
        """ wx.Frame
        """

    def GetHelpString(self, id: int) -> str:
        """ Gets the help string associated with the menu item identifier.
        """

    def GetLabel(self, id: int) -> str:
        """ Gets the label associated with a menu item.
        """

    def GetMenu(self, menuIndex: int) -> 'Menu':
        """ Returns the menu at menuIndex  (zero-based).
        """

    def GetMenuCount(self) -> int:
        """ Returns the number of menus in this menubar.
        """

    def GetMenuLabel(self, pos: int) -> str:
        """ Returns the label of a top-level menu.
        """

    def GetMenuLabelText(self, pos: int) -> str:
        """ Returns the label of a top-level menu.
        """

    def GetMenus(self) -> None:
        """ Return a list of (menu, label) items for the menus in the MenuBar.
        """

    def Insert(self, pos, menu, title) -> bool:
        """ Inserts the menu at the given position into the menu bar.
        """

    def IsAttached(self) -> bool:
        """ bool
        """

    def IsChecked(self, id: int) -> bool:
        """ Determines whether an item is checked.
        """

    def IsEnabled(self, id: int) -> bool:
        """ Determines whether an item is enabled.
        """

    def IsEnabledTop(self, pos: int) -> bool:
        """ Returns True if the menu with the given index is enabled.
        """

    @staticmethod
    def MacGetCommonMenuBar() -> 'MenuBar':
        """ Enables you to get the global menubar on Mac, that is, the menubar displayed when the app is running without any frames open.
        """

    @staticmethod
    def MacSetCommonMenuBar(menubar: 'MenuBar') -> None:
        """ Enables you to set the global menubar on Mac, that is, the menubar displayed when the app is running without any frames open.
        """

    def OSXGetAppleMenu(self) -> 'Menu':
        """ Returns the Apple menu.
        """

    def Refresh(self, eraseBackground=True, rect=None) -> None:
        """ Redraw the menu bar.
        """

    def Remove(self, pos: int) -> 'Menu':
        """ Removes the menu from the menu bar and returns the menu object - the caller is responsible for deleting it.
        """

    def Replace(self, pos, menu, title) -> 'Menu':
        """ Replaces the menu at the given position with another one.
        """

    def SetHelpString(self, id, helpString) -> None:
        """ Sets the help string associated with a menu item.
        """

    def SetLabel(self, id, label) -> None:
        """ Sets the label of a menu item.
        """

    def SetMenuLabel(self, pos, label) -> None:
        """ Sets the label of a top-level menu.
        """

    def SetMenus(self, items) -> None:
        """ SetMenus()
        """

MB_DOCKABLE: int
NOT_FOUND: int


class MenuEvent(Event):
    """ This class is used for a variety of menu-related events.
    """
    def __init__(self, type=wxEVT_NULL, id=0, menu=None) -> None:
        """ Constructor.
        """

    def GetMenu(self) -> 'Menu':
        """ Returns the menu which is being opened or closed, or the menu containing the highlighted item.
        """

    def GetMenuId(self) -> int:
        """ Returns the menu identifier associated with the event.
        """

    def IsPopup(self) -> bool:
        """ Returns True if the menu which is being opened or closed is a popup menu, False if it is a normal one.
        """

EVT_MENU_OPEN: int  #  A menu is about to be opened. On Windows, this is only sent once for each navigation of the menubar (up until all menus have closed).
EVT_MENU_CLOSE: int  #  A menu has been just closed. Notice that this event is currently being sent before the menu selection ( wxEVT_MENU ) event, if any.
EVT_MENU_HIGHLIGHT: int  #  The menu item with the specified id has been highlighted: int  #  used to show help prompts in the status bar by   wx.Frame
EVT_MENU_HIGHLIGHT_ALL: int  #  A menu item has been highlighted, i.e. the currently selected menu item has changed. ^^


class MenuItem(Object):
    """ A menu item represents an item in a menu.
    """
    def __init__(self, parentMenu=None, id=ID_SEPARATOR, text="", helpString="", kind=ITEM_NORMAL, subMenu=None) -> None:
        """ Constructs a   wx.MenuItem  object.
        """

    def AddExtraAccel(self, accel: AcceleratorEntry) -> None:
        """ Add an extra accelerator for this menu item.
        """

    def Check(self, check: bool=True) -> None:
        """ Checks or unchecks the menu item.
        """

    def ClearExtraAccels(self) -> None:
        """ Clear the extra accelerators list.
        """

    def Enable(self, enable: bool=True) -> None:
        """ Enables or disables the menu item.
        """

    def GetAccel(self) -> 'AcceleratorEntry':
        """ Get our accelerator or None (caller must delete the pointer)
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ Returns the background colour associated with the menu item.
        """

    def GetBitmap(self, *args, **kw) -> 'Bitmap':
        """ Overloaded Implementations:
        """

    def GetBitmapBundle(self) -> 'BitmapBundle':
        """ Returns the bitmap bundle containing the bitmap used for this item.
        """

    def GetDisabledBitmap(self) -> 'Bitmap':
        """ Returns the bitmap used for disabled items.
        """

    def GetFont(self) -> 'Font':
        """ Returns the font associated with the menu item.
        """

    def GetHelp(self) -> str:
        """ Returns the help string associated with the menu item.
        """

    def GetId(self) -> int:
        """ Returns the menu item identifier.
        """

    def GetItemLabel(self) -> str:
        """ Returns the text associated with the menu item including any accelerator characters that were passed to the constructor or SetItemLabel .
        """

    def GetItemLabelText(self) -> str:
        """ Returns the text associated with the menu item, without any accelerator characters.
        """

    def GetKind(self) -> 'ItemKind':
        """ Returns the item kind, one of  ITEM_SEPARATOR ,   ITEM_NORMAL ,   ITEM_CHECK   or   ITEM_RADIO .
        """

    @staticmethod
    def GetLabelText(text: str) -> str:
        """ Strips all accelerator characters and mnemonics from the given text.
        """

    def GetMarginWidth(self) -> int:
        """ Gets the width of the menu item checkmark bitmap.
        """

    def GetMenu(self) -> 'Menu':
        """ Returns the menu this menu item is in, or None if this menu item is not attached.
        """

    def GetSubMenu(self) -> 'Menu':
        """ Returns the submenu associated with the menu item, or None if there isnât one.
        """

    def GetTextColour(self) -> 'Colour':
        """ Returns the text colour associated with the menu item.
        """

    def IsCheck(self) -> bool:
        """ Returns True if the item is a check item.
        """

    def IsCheckable(self) -> bool:
        """ Returns True if the item is checkable.
        """

    def IsChecked(self) -> bool:
        """ Returns True if the item is checked.
        """

    def IsEnabled(self) -> bool:
        """ Returns True if the item is enabled.
        """

    def IsRadio(self) -> bool:
        """ Returns True if the item is a radio button.
        """

    def IsSeparator(self) -> bool:
        """ Returns True if the item is a separator.
        """

    def IsSubMenu(self) -> bool:
        """ Returns True if the item is a submenu.
        """

    def SetAccel(self, accel: 'AcceleratorEntry') -> None:
        """ Set the accel for this item - this may also be done indirectly with SetText
        """

    def SetBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the background colour associated with the menu item.
        """

    def SetBitmap(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetBitmaps(self, checked, unchecked=NullBitmap) -> None:
        """ Sets the checked/unchecked bitmaps for the menu item.
        """

    def SetDisabledBitmap(self, disabled: 'BitmapBundle') -> None:
        """ Sets the to be used for disabled menu items.
        """

    def SetFont(self, font: 'Font') -> None:
        """ Sets the font associated with the menu item.
        """

    def SetHelp(self, helpString: str) -> None:
        """ Sets the help string.
        """

    def SetItemLabel(self, label: str) -> None:
        """ Sets the label associated with the menu item.
        """

    def SetMarginWidth(self, width: int) -> None:
        """ Sets the width of the menu item checkmark bitmap.
        """

    def SetMenu(self, menu: 'Menu') -> None:
        """ Sets the parent menu which will contain this menu item.
        """

    def SetSubMenu(self, menu: 'Menu') -> None:
        """ Sets the submenu of this menu item.
        """

    def SetTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the text colour associated with the menu item.
        """

EVT_MENU: int  #  Process a  wxEVT_MENU   command, which is generated by a menu item. This type of event is sent as    wx.CommandEvent.
EVT_MENU_RANGE: int  #  Process a  wxEVT_MENU   command, which is generated by a range of menu items. This type of event is sent as    wx.CommandEvent.
EVT_MENU_OPEN: int  #  A menu is about to be opened. On Windows, this is only sent once for each navigation of the menubar (up until all menus have closed). This type of event is sent as   wx.MenuEvent.
EVT_MENU_CLOSE: int  #  A menu has been just closed. This type of event is sent as   wx.MenuEvent.
EVT_MENU_HIGHLIGHT: int  #  The menu item with the specified id has been highlighted. If the id is ID_NONE, highlighting has been removed from the previously highlighted menu item and there is no highlighted item any more. This is used by   wx.Frame  to show help prompts in the status bar. This type of event is sent as   wx.MenuEvent.
EVT_MENU_HIGHLIGHT_ALL: int  #  A menu item has been highlighted, i.e. the currently selected menu item has changed. This type of event is sent as   wx.MenuEvent. ^^
WXK_DELETE: int
WXK_BACK: int
WXK_INSERT: int
WXK_RETURN: int
WXK_PAGEUP: int
WXK_PAGEDOWN: int
WXK_LEFT: int
WXK_RIGHT: int
WXK_UP: int
WXK_DOWN: int
WXK_HOME: int
WXK_END: int
WXK_SPACE: int
WXK_TAB: int
WXK_ESCAPE: int
WXK_CANCEL: int
WXK_CLEAR: int
WXK_MENU: int
WXK_PAUSE: int
WXK_CAPITAL: int
WXK_SELECT: int
WXK_PRINT: int
WXK_EXECUTE: int
WXK_SNAPSHOT: int
WXK_HELP: int
WXK_ADD: int
WXK_SEPARATOR: int
WXK_SUBTRACT: int
WXK_DECIMAL: int
WXK_DIVIDE: int
WXK_NUMLOCK: int
WXK_SCROLL: int
WXK_NUMPAD_SPACE: int
WXK_NUMPAD_TAB: int
WXK_NUMPAD_ENTER: int
WXK_NUMPAD_HOME: int
WXK_NUMPAD_LEFT: int
WXK_NUMPAD_UP: int
WXK_NUMPAD_RIGHT: int
WXK_NUMPAD_DOWN: int
WXK_NUMPAD_PAGEUP: int
WXK_NUMPAD_PAGEDOWN: int
WXK_NUMPAD_PAGEUP: int
WXK_NUMPAD_PAGEDOWN: int
WXK_NUMPAD_END: int
WXK_NUMPAD_BEGIN: int
WXK_NUMPAD_INSERT: int
WXK_NUMPAD_DELETE: int
WXK_NUMPAD_EQUAL: int
WXK_NUMPAD_MULTIPLY: int
WXK_NUMPAD_ADD: int
WXK_NUMPAD_SEPARATOR: int
WXK_NUMPAD_SUBTRACT: int
WXK_NUMPAD_DECIMAL: int
WXK_NUMPAD_DIVIDE: int
WXK_WINDOWS_LEFT: int
WXK_WINDOWS_RIGHT: int
WXK_WINDOWS_MENU: int
WXK_COMMAND: int
WXK_SHIFT: int
WXK_ALT: int
WXK_SCROLL: int
WXK_CAPITAL: int
WXK_NUMLOCK: int
WXK_NUMPAD_TAB: int
WXK_TAB: int
WXK_WINDOWS_LEFT: int
WXK_WINDOWS_RIGHT: int
WXK_ADD: int
WXK_SEPARATOR: int
WXK_SUBTRACT: int
WXK_DECIMAL: int
WXK_DIVIDE: int
WXK_SNAPSHOT: int


class MessageDialog(Dialog):
    """ This class represents a dialog that shows a single or multi-line
message, with a choice of wx.OK, Yes, No and Cancel buttons.
    """
    def __init__(self, parent, message, caption=MessageBoxCaptionStr, style=OK|CENTRE, pos=DefaultPosition) -> None:
        """ Constructor specifying the message box properties.
        """

    def GetCancelLabel(self) -> str:
        """ string
        """

    def GetCaption(self) -> str:
        """ string
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetEffectiveIcon(self) -> int:
        """ long
        """

    def GetExtendedMessage(self) -> str:
        """ string
        """

    def GetHelpLabel(self) -> str:
        """ string
        """

    def GetMessage(self) -> str:
        """ string
        """

    def GetMessageDialogStyle(self) -> int:
        """ long
        """

    def GetNoLabel(self) -> str:
        """ string
        """

    def GetOKLabel(self) -> str:
        """ string
        """

    def GetYesLabel(self) -> str:
        """ string
        """

    def HasCustomLabels(self) -> bool:
        """ bool
        """

    def SetExtendedMessage(self, extendedMessage: str) -> None:
        """ Sets the extended message for the dialog: this message is usually an extension of the short message specified in the constructor or set with SetMessage .
        """

    def SetHelpLabel(self, help: MessageDialogButtonLabel) -> bool:
        """ Sets the label for the Help button.
        """

    def SetMessage(self, message: str) -> None:
        """ Sets the message shown by the dialog.
        """

    def SetOKCancelLabels(self, ok, cancel) -> bool:
        """ Overrides the default labels of the wx.OK and Cancel buttons.
        """

    def SetOKLabel(self, ok: MessageDialogButtonLabel) -> bool:
        """ Overrides the default label of the wx.OK button.
        """

    def SetYesNoCancelLabels(self, yes, no, cancel) -> bool:
        """ Overrides the default labels of the Yes, No and Cancel buttons.
        """

    def SetYesNoLabels(self, yes, no) -> bool:
        """ Overrides the default labels of the Yes and No buttons.
        """

    def ShowModal(self) -> int:
        """ Shows the dialog, returning one of wx.ID_OK, wx.ID_CANCEL, wx.ID_YES, wx.ID_NO or wx.ID_HELP.
        """

OK: int  #  Puts an Ok button in the message box. May be combined with  CANCEL .
CANCEL: int  #  Puts a Cancel button in the message box. Must be combined with either  OK   or   YES_NO .
YES_NO: int  #  Puts Yes and No buttons in the message box. It is recommended to always use  CANCEL   with this style as otherwise the message box wonât have a close button under wxMSW and the user will be forced to answer it.
HELP: int  #  Puts a Help button to the message box. This button can have special appearance or be specially positioned if its label is not changed from the default one. Notice that using this button is not supported when showing a message box from non-main thread in OSX/Cocoa. Available since wxWidgets 2.9.3.
NO_DEFAULT: int  #  Makes the âNoâ button default, can only be used with  YES_NO .
CANCEL_DEFAULT: int  #  Makes the âCancelâ button default, can only be used with  CANCEL . This style is currently not supported (and ignored) in wxOSX.
YES_DEFAULT: int  #  Makes the âYesâ button default, this is the default behaviour and this flag exists solely for symmetry with  NO_DEFAULT .
OK_DEFAULT: int  #  Makes the âwx.OKâ button default, this is the default behaviour and this flag exists solely for symmetry with  CANCEL_DEFAULT .
ICON_NONE: int  #  Displays no icon in the dialog if possible (an icon might still be displayed if the current platform mandates its use). This style may be used to prevent the dialog from using the default icon based on  YES_NO   presence as explained in   ICON_QUESTION   and   ICON_INFORMATION   documentation below.
ICON_ERROR: int  #  Displays an error icon in the dialog.
ICON_WARNING: int  #  Displays a warning icon in the dialog. This style should be used for informative warnings or, in combination with  YES_NO   or   CANCEL , for questions that have potentially serious consequences (caution icon is used on macOS in this case).
ICON_QUESTION: int  #  Displays a question mark symbol. This icon is automatically used with  YES_NO   so itâs usually unnecessary to specify it explicitly. This style is not supported for message dialogs under wxMSW when a task dialog is used to implement them (i.e. when running under Windows Vista or later) because  Microsoft guidelines  indicate that no icon should be used for routine confirmations. If it is specified, no icon will be displayed.
ICON_INFORMATION: int  #  Displays an information symbol. This icon is used by default if  YES_NO   is not given so it is usually unnecessary to specify it explicitly.
ICON_EXCLAMATION: int  #  Alias for  ICON_WARNING .
ICON_HAND: int  #  Alias for  ICON_ERROR .
ICON_AUTH_NEEDED: int  #  Displays an authentication needed symbol. This style is only supported for message dialogs under wxMSW when a task dialog is used to implement them (i.e. when running under Windows Vista or later). In other cases the default icon selection logic will be used. Note this can be combined with other styles to provide a fallback. For instance, using wx.ICON_AUTH_NEEDED | wx.ICON_QUESTION will show a shield symbol on Windows Vista or above and a question symbol on other platforms. Available since wxWidgets 2.9.5
STAY_ON_TOP: int  #  Makes the message box stay on top of all other windows and not only just its parent (currently implemented only under MSW and GTK).
CENTRE: int  #  Centre the message box on its parent or on the screen if parent is not specified. Setting this style under MSW makes no differences as the dialog is always centered on the parent. ^^
OK: int
OK: int
CANCEL: int
YES_NO: int
HELP: int
NO_DEFAULT: int
CANCEL_DEFAULT: int
YES_DEFAULT: int
OK_DEFAULT: int
OK: int
ICON_NONE: int
ICON_ERROR: int
ICON_WARNING: int
ICON_QUESTION: int
ICON_INFORMATION: int
ICON_EXCLAMATION: int
ICON_HAND: int
ICON_AUTH_NEEDED: int
ICON_AUTH_NEEDED: int
ICON_QUESTION: int
STAY_ON_TOP: int
CENTRE: int
OK: int
OK: int
ID_OK: int
ID_CANCEL: int
ID_YES: int
ID_NO: int
ID_HELP: int
OK: int
OK: int
OK: int
ID_OK: int
ID_CANCEL: int
ID_YES: int
ID_NO: int
ID_HELP: int


class Metafile(Object):
    """ A Metafile represents the MS Windows metafile object, so metafile
operations have no effect in X.
    """
    def __init__(self, filename: str="") -> None:
        """ Constructor.
        """

    def IsOk(self) -> bool:
        """ Returns True if the metafile is valid.
        """

    def Play(self, dc: 'DC') -> bool:
        """ Plays the metafile into the given device context, returning True if successful.
        """

    def SetClipboard(self, width=0, height=0) -> bool:
        """ Passes the metafile data to the clipboard.
        """



class MetafileDC(DC):
    """ This is a type of device context that allows a metafile object to be
created (Windows only), and has most of the characteristics of a
normal DC.
    """
    def __init__(self, filename: str="") -> None:
        """ Constructor.
        """

    def Close(self) -> 'Metafile':
        """ This must be called after the device context is finished with.
        """



class MimeTypesManager:
    """ This class allows the application to retrieve information about all
known MIME types from a system-specific location and the filename
extensions to the MIME types and vice versa.
    """
    def __init__(self) -> None:
        """ Constructor puts the object in the âworkingâ state.
        """

    def AddFallbacks(self, fallbacks: 'FileTypeInfo') -> None:
        """ This function may be used to provide hard-wired fallbacks for the MIME types and extensions that might not be present in the system MIME database.
        """

    def Associate(self, ftInfo: 'FileTypeInfo') -> 'FileType':
        """ Create a new association using the fields of   wx.FileTypeInfo  (at least the MIME type and the extension should be set).
        """

    def EnumAllFileTypes(self) -> list[str]:
        """ Returns a list of all known file types.
        """

    def GetFileTypeFromExtension(self, extension: str) -> 'FileType':
        """ Gather information about the files with given extension and return the corresponding   wx.FileType  object or None if the extension is unknown.
        """

    def GetFileTypeFromMimeType(self, mimeType: str) -> 'FileType':
        """ Gather information about the files with given MIME type and return the corresponding   wx.FileType  object or None if the MIME type is unknown.
        """

    @staticmethod
    def IsOfType(mimeType, wildcard) -> bool:
        """ This function returns True if either the given mimeType  is exactly the same as wildcard  or if it has the same category and the subtype of wildcard  is ââ.
        """

    def Unassociate(self, ft: 'FileType') -> bool:
        """ Undo Associate .
        """



class MiniFrame(Frame):
    """ A miniframe is a frame with a small title bar.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize, style=CAPTION|RESIZE_BORDER, name=FrameNameStr) -> bool:
        """ Used in two-step frame construction.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

ICONIZE: int  #  Display the frame iconized (minimized) (Windows only).
CAPTION: int  #  Puts a caption on the frame.
MINIMIZE: int  #  Identical to wx.ICONIZE.
MINIMIZE_BOX: int  #  Displays a minimize box on the frame (Windows and Motif only).
MAXIMIZE: int  #  Displays the frame maximized (Windows only).
MAXIMIZE_BOX: int  #  Displays a maximize box on the frame (Windows and Motif only).
CLOSE_BOX: int  #  Displays a close box on the frame.
STAY_ON_TOP: int  #  Stay on top of other windows (Windows only).
SYSTEM_MENU: int  #  Displays a system menu (Windows and Motif only).
RESIZE_BORDER: int  #  Displays a resizable border around the window. ^^
ICONIZE: int
CAPTION: int
MINIMIZE: int
ICONIZE: int
MINIMIZE_BOX: int
MAXIMIZE: int
MAXIMIZE_BOX: int
CLOSE_BOX: int
STAY_ON_TOP: int
SYSTEM_MENU: int
RESIZE_BORDER: int


class MirrorDC(DC):
    """ MirrorDC is a simple wrapper class which is always associated with a
real DC object and either forwards all of its operations to it
without changes (no mirroring takes place) or exchanges x and y
coordinates which makes it possible to reuse the same code to draw a
figure and its mirror  i.e.
    """
    def __init__(self, dc, mirror) -> None:
        """ Creates a (maybe) mirrored DC associated with the real dc.
        """



class ModalDialogHook:
    """ Allows intercepting all modal dialog calls.
    """
    def __init__(self) -> None:
        """ Default and trivial constructor.
        """

    def Enter(self, dialog: 'Dialog') -> int:
        """ Called by wxWidgets before showing any modal dialogs.
        """

    def Exit(self, dialog: 'Dialog') -> None:
        """ Called by wxWidgets after dismissing the modal dialog.
        """

    def Register(self) -> None:
        """ Register this hook as being active.
        """

    def Unregister(self) -> None:
        """ Unregister this hook.
        """

ID_NONE: int


class MouseCaptureChangedEvent(Event):
    """ A mouse capture changed event is sent to a window that loses its mouse
capture.
    """
    def __init__(self, windowId=0, gainedCapture=None) -> None:
        """ Constructor.
        """

    def GetCapturedWindow(self) -> 'Window':
        """ Returns the window that gained the capture, or None if it was a non-wxWidgets window.
        """

EVT_MOUSE_CAPTURE_CHANGED: int  #  Process a  wxEVT_MOUSE_CAPTURE_CHANGED   event. ^^


class MouseCaptureLostEvent(Event):
    """ A mouse capture lost event is sent to a window that had obtained mouse
capture, which was subsequently lost due to an âexternalâ event (for
example, when a dialog box is shown or if another application captures
the mouse).
    """
    def __init__(self, windowId: int=0) -> None:
        """ Constructor.
        """

EVT_MOUSE_CAPTURE_LOST: int  #  Process a  wxEVT_MOUSE_CAPTURE_LOST   event. ^^


class MouseEvent(Event, MouseState):
    """ This event class contains information about the events generated by
the mouse: they include mouse buttons press and release events and
mouse move events.
    """
    def __init__(self, mouseEventType: int=wxEVT_NULL) -> None:
        """ Constructor.
        """

    def Aux1DClick(self) -> bool:
        """ Returns True if the event was a first extra button double click.
        """

    def Aux1Down(self) -> bool:
        """ Returns True if the first extra button mouse button changed to down.
        """

    def Aux1Up(self) -> bool:
        """ Returns True if the first extra button mouse button changed to up.
        """

    def Aux2DClick(self) -> bool:
        """ Returns True if the event was a second extra button double click.
        """

    def Aux2Down(self) -> bool:
        """ Returns True if the second extra button mouse button changed to down.
        """

    def Aux2Up(self) -> bool:
        """ Returns True if the second extra button mouse button changed to up.
        """

    def Button(self, but: MouseButton) -> bool:
        """ Returns True if the event was generated by the specified button.
        """

    def ButtonDClick(self, but: MouseButton=MOUSE_BTN_ANY) -> bool:
        """ If the argument is omitted, this returns True if the event was a mouse double click event.
        """

    def ButtonDown(self, but: MouseButton=MOUSE_BTN_ANY) -> bool:
        """ If the argument is omitted, this returns True if the event was a mouse button down event.
        """

    def ButtonUp(self, but: MouseButton=MOUSE_BTN_ANY) -> bool:
        """ If the argument is omitted, this returns True if the event was a mouse button up event.
        """

    def Dragging(self) -> bool:
        """ Returns True if this was a dragging event (motion while a button is depressed).
        """

    def Entering(self) -> bool:
        """ Returns True if the mouse was entering the window.
        """

    def GetButton(self) -> int:
        """ Returns the mouse button which generated this event or  MOUSE_BTN_NONE   if no button is involved (for mouse move, enter or leave event, for example).
        """

    def GetClickCount(self) -> int:
        """ Returns the number of mouse clicks for this event: 1 for a simple click, 2 for a double-click, 3 for a triple-click and so on.
        """

    def GetColumnsPerAction(self) -> int:
        """ Returns the configured number of columns (or whatever) to be scrolled per wheel action.
        """

    def GetLinesPerAction(self) -> int:
        """ Returns the configured number of lines (or whatever) to be scrolled per wheel action.
        """

    def GetLogicalPosition(self, dc: 'DC') -> 'Point':
        """ Returns the logical mouse position in pixels (i.e. translated according to the translation set for the DC, which usually indicates that the window has been scrolled).
        """

    def GetMagnification(self) -> float:
        """ For magnify (pinch to zoom) events: returns the change in magnification.
        """

    def GetWheelAxis(self) -> 'MouseWheelAxis':
        """ Gets the axis the wheel operation concerns.
        """

    def GetWheelDelta(self) -> int:
        """ Get wheel delta, normally 120.
        """

    def GetWheelRotation(self) -> int:
        """ Get wheel rotation, positive or negative indicates direction of rotation.
        """

    def IsButton(self) -> bool:
        """ Returns True if the event was a mouse button event (not necessarily a button down event - that may be tested using ButtonDown ).
        """

    def IsPageScroll(self) -> bool:
        """ Returns True if the system has been setup to do page scrolling with the mouse wheel instead of line scrolling.
        """

    def IsWheelInverted(self) -> bool:
        """ On Mac, has the user selected âNaturalâ scrolling in their System Preferences? Currently False on all other OSâs.
        """

    def Leaving(self) -> bool:
        """ Returns True if the mouse was leaving the window.
        """

    def LeftDClick(self) -> bool:
        """ Returns True if the event was a left double click.
        """

    def LeftDown(self) -> bool:
        """ Returns True if the left mouse button changed to down.
        """

    def LeftUp(self) -> bool:
        """ Returns True if the left mouse button changed to up.
        """

    def Magnify(self) -> bool:
        """ Returns True if the event is a magnify (i.e. pinch to zoom) event.
        """

    def MetaDown(self) -> bool:
        """ Returns True if the Meta key was down at the time of the event.
        """

    def MiddleDClick(self) -> bool:
        """ Returns True if the event was a middle double click.
        """

    def MiddleDown(self) -> bool:
        """ Returns True if the middle mouse button changed to down.
        """

    def MiddleUp(self) -> bool:
        """ Returns True if the middle mouse button changed to up.
        """

    def Moving(self) -> bool:
        """ Returns True if this was a motion event and no mouse buttons were pressed.
        """

    def RightDClick(self) -> bool:
        """ Returns True if the event was a right double click.
        """

    def RightDown(self) -> bool:
        """ Returns True if the right mouse button changed to down.
        """

    def RightUp(self) -> bool:
        """ Returns True if the right mouse button changed to up.
        """

    def SetColumnsPerAction(self, columnsPerAction) -> None:
        """ 
        """

    def SetLinesPerAction(self, linesPerAction) -> None:
        """ 
        """

    def SetWheelAxis(self, wheelAxis) -> None:
        """ 
        """

    def SetWheelDelta(self, wheelDelta) -> None:
        """ 
        """

    def SetWheelRotation(self, wheelRotation) -> None:
        """ 
        """

EVT_LEFT_DOWN: int  #  Process a  wxEVT_LEFT_DOWN   event. The handler of this event should normally call event.Skip() to allow the default processing to take place as otherwise the window under mouse wouldnât get the focus.
EVT_LEFT_UP: int  #  Process a  wxEVT_LEFT_UP   event.
EVT_LEFT_DCLICK: int  #  Process a  wxEVT_LEFT_DCLICK   event.
EVT_MIDDLE_DOWN: int  #  Process a  wxEVT_MIDDLE_DOWN   event.
EVT_MIDDLE_UP: int  #  Process a  wxEVT_MIDDLE_UP   event.
EVT_MIDDLE_DCLICK: int  #  Process a  wxEVT_MIDDLE_DCLICK   event.
EVT_RIGHT_DOWN: int  #  Process a  wxEVT_RIGHT_DOWN   event.
EVT_RIGHT_UP: int  #  Process a  wxEVT_RIGHT_UP   event.
EVT_RIGHT_DCLICK: int  #  Process a  wxEVT_RIGHT_DCLICK   event.
EVT_MOUSE_AUX1_DOWN: int  #  Process a  wxEVT_AUX1_DOWN   event.
EVT_MOUSE_AUX1_UP: int  #  Process a  wxEVT_AUX1_UP   event.
EVT_MOUSE_AUX1_DCLICK: int  #  Process a  wxEVT_AUX1_DCLICK   event.
EVT_MOUSE_AUX2_DOWN: int  #  Process a  wxEVT_AUX2_DOWN   event.
EVT_MOUSE_AUX2_UP: int  #  Process a  wxEVT_AUX2_UP   event.
EVT_MOUSE_AUX2_DCLICK: int  #  Process a  wxEVT_AUX2_DCLICK   event.
EVT_MOTION: int  #  Process a  wxEVT_MOTION   event.
EVT_ENTER_WINDOW: int  #  Process a  wxEVT_ENTER_WINDOW   event.
EVT_LEAVE_WINDOW: int  #  Process a  wxEVT_LEAVE_WINDOW   event.
EVT_MOUSEWHEEL: int  #  Process a  wxEVT_MOUSEWHEEL   event.
EVT_MOUSE_EVENTS: int  #  Process all mouse events.
EVT_MAGNIFY: int  #  Process a  wxEVT_MAGNIFY   event (new since wxWidgets 3.1.0). ^^


class MouseEventsManager(EvtHandler):
    """ Helper for handling mouse input events in windows containing multiple
items.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, win: 'Window') -> bool:
        """ Finishes initialization of the object created using default constructor.
        """

    def MouseClickBegin(self, item: int) -> None:
        """ May be overridden to update the state of an item when it is pressed.
        """

    def MouseClickCancelled(self, item: int) -> None:
        """ Must be overridden to reset the item appearance changed by MouseClickBegin .
        """

    def MouseClicked(self, item: int) -> bool:
        """ Must be overridden to react to mouse clicks.
        """

    def MouseDragBegin(self, item, pos) -> bool:
        """ Must be overridden to allow or deny dragging of the item.
        """

    def MouseDragCancelled(self, item: int) -> None:
        """ Must be overridden to handle cancellation of mouse dragging.
        """

    def MouseDragEnd(self, item, pos) -> None:
        """ Must be overridden to handle item drop.
        """

    def MouseDragging(self, item, pos) -> None:
        """ Must be overridden to provide feed back while an item is being dragged.
        """

    def MouseHitTest(self, pos: 'Point') -> int:
        """ Must be overridden to return the item at the given position.
        """

NOT_FOUND: int


class MouseState(KeyboardState):
    """ Represents the mouse state.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def Aux1IsDown(self) -> bool:
        """ Returns True if the first extra button mouse button is currently down.
        """

    def Aux2IsDown(self) -> bool:
        """ Returns True if the second extra button mouse button is currently down.
        """

    def GetPosition(self) -> 'Point':
        """ Returns the physical mouse position.
        """

    def GetX(self) -> 'Coord':
        """ Returns X coordinate of the physical mouse event position.
        """

    def GetY(self) -> 'Coord':
        """ Returns Y coordinate of the physical mouse event position.
        """

    def LeftIsDown(self) -> bool:
        """ Returns True if the left mouse button is currently down.
        """

    def MiddleIsDown(self) -> bool:
        """ Returns True if the middle mouse button is currently down.
        """

    def RightIsDown(self) -> bool:
        """ Returns True if the right mouse button is currently down.
        """

    def SetAux1Down(self, down: bool) -> None:
        """ down (bool) â
        """

    def SetAux2Down(self, down: bool) -> None:
        """ down (bool) â
        """

    def SetLeftDown(self, down: bool) -> None:
        """ down (bool) â
        """

    def SetMiddleDown(self, down: bool) -> None:
        """ down (bool) â
        """

    def SetPosition(self, pos: 'Point') -> None:
        """ pos (wx.Point) â
        """

    def SetRightDown(self, down: bool) -> None:
        """ down (bool) â
        """

    def SetState(self, state: 'MouseState') -> None:
        """ state (wx.MouseState) â
        """

    def SetX(self, x: int) -> None:
        """ x (int) â
        """

    def SetY(self, y: int) -> None:
        """ y (int) â
        """



class MoveEvent(Event):
    """ A move event holds information about window position change.
    """
    def __init__(self, pt, id=0) -> None:
        """ Constructor.
        """

    def GetPosition(self) -> 'Point':
        """ Returns the position of the window generating the move change event.
        """

    def GetRect(self) -> 'Rect':
        """ wx.Rect
        """

    def SetPosition(self, pos: 'Point') -> None:
        """ pos (wx.Point) â
        """

    def SetRect(self, rect: 'Rect') -> None:
        """ rect (wx.Rect) â
        """

EVT_MOVE: int  #  Process a  wxEVT_MOVE   event, which is generated when a window is moved.
EVT_MOVE_START: int  #  Process a  wxEVT_MOVE_START   event, which is generated when the user starts to move or size a window. wxMSW only.
EVT_MOVING: int  #  Process a  wxEVT_MOVING   event, which is generated while the user is moving the window. wxMSW only.
EVT_MOVE_END: int  #  Process a  wxEVT_MOVE_END   event, which is generated when the user stops moving or sizing a window. wxMSW only. ^^


class MultiChoiceDialog(Dialog):
    """ This class represents a dialog that shows a list of strings, and
allows the user to select one or more.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetSelections(self) -> list[int]:
        """ Returns array with indexes of selected items.
        """

    def SetSelections(self, selections: list[int]) -> None:
        """ Sets selected items from the array of selected itemsâ indexes.
        """

    def ShowModal(self) -> int:
        """ Shows the dialog, returning either wx.ID_OK or wx.ID_CANCEL.
        """

OK: int  #  Show an wx.OK button.
CANCEL: int  #  Show a Cancel button.
CENTRE: int  #  Centre the message. ^^
OK: int
OK: int
CANCEL: int
CENTRE: int
ID_OK: int
ID_CANCEL: int
DEFAULT_DIALOG_STYLE: int
RESIZE_BORDER: int
OK: int
CANCEL: int
CENTRE: int
DEFAULT_DIALOG_STYLE: int
RESIZE_BORDER: int
OK: int
CANCEL: int
CENTRE: int
ID_OK: int
ID_CANCEL: int


class NativeFontInfo:
    """ NativeFontInfo is platform-specific font representation: this class
should be considered as an opaque font description only used by the
native functions, the user code can only get the objects of this type
from somewhere and pass it somewhere else (possibly save them
somewhere using ToString() and restore them using FromString())
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def FromString(self, s: str) -> bool:
        """ s (string) â
        """

    def FromUserString(self, s: str) -> bool:
        """ s (string) â
        """

    def GetEncoding(self) -> int:
        """ wx.FontEncoding
        """

    def GetFaceName(self) -> str:
        """ string
        """

    def GetFamily(self) -> int:
        """ wx.FontFamily
        """

    def GetFractionalPointSize(self) -> float:
        """ float
        """

    def GetNumericWeight(self) -> int:
        """ int
        """

    def GetPointSize(self) -> int:
        """ int
        """

    def GetStyle(self) -> int:
        """ wx.FontStyle
        """

    def GetUnderlined(self) -> bool:
        """ bool
        """

    def GetWeight(self) -> int:
        """ wx.FontWeight
        """

    def Init(self) -> None:
        """ 
        """

    def InitFromFont(self, font: 'Font') -> None:
        """ font (wx.Font) â
        """

    def SetEncoding(self, encoding: int) -> None:
        """ encoding (FontEncoding) â
        """

    def SetFaceName(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def SetFamily(self, family: int) -> None:
        """ family (FontFamily) â
        """

    def SetFractionalPointSize(self, pointsize: float) -> None:
        """ pointsize (float) â
        """

    def SetNumericWeight(self, weight: int) -> None:
        """ weight (int) â
        """

    def SetPointSize(self, pointsize: int) -> None:
        """ pointsize (int) â
        """

    def SetStyle(self, style: int) -> None:
        """ style (FontStyle) â
        """

    def SetUnderlined(self, underlined: bool) -> None:
        """ underlined (bool) â
        """

    def SetWeight(self, weight: int) -> None:
        """ weight (FontWeight) â
        """

    def ToString(self) -> str:
        """ string
        """

    def ToUserString(self) -> str:
        """ string
        """

    def __str__(self) -> str:
        """ string
        """



class NativePixelData:
    """ A class providing direct access to a wx.Bitmapâs
internal data without alpha channel (RGB).
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetPixels(self) -> 'NativePixelData_Accessor':
        """ wx.NativePixelData_Accessor
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """



class NativePixelData_Accessor:
    """  Overloaded Implementations:
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Get(self) -> Any:
        """ PyObject
        """

    def IsOk(self) -> bool:
        """ bool
        """

    def MoveTo(self, data, x, y) -> None:
        """ data (NativePixelData) â
        """

    def Offset(self, data, x, y) -> None:
        """ data (NativePixelData) â
        """

    def OffsetX(self, data, x) -> None:
        """ data (NativePixelData) â
        """

    def OffsetY(self, data, y) -> None:
        """ data (NativePixelData) â
        """

    def Reset(self, data: NativePixelData) -> None:
        """ data (NativePixelData) â
        """

    def Set(self, red, green, blue) -> None:
        """ 
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """

    def nextPixel(self) -> None:
        """ 
        """



class NavigationKeyEvent(Event):
    """ This event class contains information about navigation events,
generated by navigation keys such as tab and page down.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetCurrentFocus(self) -> 'Window':
        """ Returns the child that has the focus, or None.
        """

    def GetDirection(self) -> bool:
        """ Returns True if the navigation was in the forward direction.
        """

    def IsFromTab(self) -> bool:
        """ Returns True if the navigation event was from a tab key.
        """

    def IsWindowChange(self) -> bool:
        """ Returns True if the navigation event represents a window change (for example, from Ctrl-Page Down in a notebook).
        """

    def SetCurrentFocus(self, currentFocus: 'Window') -> None:
        """ Sets the current focus window member.
        """

    def SetDirection(self, direction: bool) -> None:
        """ Sets the direction to forward if direction  is True, or backward if False.
        """

    def SetFlags(self, flags: int) -> None:
        """ Sets the flags for this event.
        """

    def SetFromTab(self, fromTab: bool) -> None:
        """ Marks the navigation event as from a tab key.
        """

    def SetWindowChange(self, windowChange: bool) -> None:
        """ Marks the event as a window change event.
        """

EVT_NAVIGATION_KEY: int  #  Process a navigation key event. ^^


class NonOwnedWindow(Window):
    """ Common base class for all non-child windows.
    """
    def SetShape(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """



class NotifyEvent(CommandEvent):
    """ This class is not used by the event handlers by itself, but is a base
class for other event classes (such as BookCtrlEvent).
    """
    def __init__(self, eventType=wxEVT_NULL, id=0) -> None:
        """ Constructor (used internally by wxWidgets only).
        """

    def Allow(self) -> None:
        """ This is the opposite of Veto : it explicitly allows the event to be processed.
        """

    def IsAllowed(self) -> bool:
        """ Returns True if the change is allowed ( Veto   hasnât been called) or False otherwise (if it was).
        """

    def Veto(self) -> None:
        """ Prevents the change announced by this event from happening.
        """



class NumberEntryDialog(Dialog):
    """ This class represents a dialog that requests a numeric input from the
user.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, message, prompt, caption, value, min, max, pos=DefaultPosition) -> bool:
        """ parent (wx.Window) â Parent window.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetValue(self) -> int:
        """ Returns the value that the user has entered if the user has pressed wx.OK, or the original value if the user has pressed Cancel.
        """

OK: int
OK: int


class Object:
    """ This is the root class of many of the wxWidgets classes.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Destroy(self) -> None:
        """ Deletes the C++ object this Python object is a proxy for.
        """

    def GetClassInfo(self) -> 'ClassInfo':
        """ This virtual function is redefined for every class that requires run-time type information, when using the DECLARE_CLASS  macro (or similar).
        """

    def GetClassName(self) -> 'Char':
        """ Returns the class name of the C++ class using RTTI.
        """

    def GetRefData(self) -> 'ObjectRefData':
        """ Returns the Object.m_refData  pointer, i.e. the data referenced by this object.
        """

    def IsSameAs(self, obj: 'Object') -> bool:
        """ Returns True if this object has the same data pointer as obj.
        """

    def Ref(self, clone: 'Object') -> None:
        """ Makes this object refer to the data in clone.
        """

    def SetRefData(self, data: 'ObjectRefData') -> None:
        """ Sets the Object.m_refData  pointer.
        """

    def UnRef(self) -> None:
        """ Decrements the reference count in the associated data, and if it is zero, deletes the data.
        """

    def UnShare(self) -> None:
        """ This is the same of AllocExclusive   but this method is public.
        """



class OutputStream(StreamBase):
    """ OutputStream is an abstract base class which may not be used
directly.
    """
    def __init__(self) -> None:
        """ Creates a dummy   wx.OutputStream  object.
        """

    def Close(self) -> bool:
        """ Closes the stream, returning False if an error occurs.
        """

    def LastWrite(self) -> int:
        """ Returns the number of bytes written during the last Write .
        """

    def PutC(self, c: int) -> None:
        """ Puts the specified character in the output queue and increments the stream position.
        """

    def SeekO(self, pos, mode=FromStart) -> 'FileOffset':
        """ Changes the stream current position.
        """

    def TellO(self) -> 'FileOffset':
        """ Returns the current stream position.
        """

    def Write(self, *args, **kw) -> 'OutputStream':
        """ Overloaded Implementations:
        """

    def WriteAll(self, buffer, size) -> bool:
        """ Writes exactly the specified number of bytes from the buffer.
        """

    def close(self) -> None:
        """ 
        """

    def eof(self) -> bool:
        """ bool
        """

    def flush(self) -> None:
        """ 
        """

    def seek(self, offset, whence=0) -> None:
        """ 
        """

    def tell(self) -> 'FileOffset':
        """ wx.FileOffset
        """

    def write(self, data) -> Any:
        """ PyObject
        """



class Overlay:
    """ Creates an overlay over an existing window, allowing for manipulations
like rubberbanding, etc.
    """
    def __init__(self) -> None:
        """ 
        """

    def Reset(self) -> None:
        """ Clears the overlay without restoring the former state.
        """



class PageSetupDialog(Object):
    """ This class represents the page setup common dialog.
    """
    def __init__(self, parent, data=None) -> None:
        """ Constructor.
        """

    def GetPageSetupData(self) -> 'PageSetupDialogData':
        """ Returns the   wx.PageSetupDialogData  object associated with the dialog.
        """

    def ShowModal(self) -> int:
        """ Shows the dialog, returning  ID_OK   if the user pressed wx.OK, and   ID_CANCEL   otherwise.
        """

OK: int
OK: int
OK: int


class PageSetupDialogData(Object):
    """ This class holds a variety of information related to
PageSetupDialog.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def EnableHelp(self, flag: bool) -> None:
        """ Enables or disables the âHelpâ button (Windows only).
        """

    def EnableMargins(self, flag: bool) -> None:
        """ Enables or disables the margin controls (Windows only).
        """

    def EnableOrientation(self, flag: bool) -> None:
        """ Enables or disables the orientation control (Windows only).
        """

    def EnablePaper(self, flag: bool) -> None:
        """ Enables or disables the paper size control (Windows only).
        """

    def EnablePrinter(self, flag: bool) -> None:
        """ Enables or disables the âPrinterâ button, which invokes a printer setup dialog.
        """

    def GetDefaultInfo(self) -> bool:
        """ Returns True if the dialog will simply return default printer information (such as orientation) instead of showing a dialog (Windows only).
        """

    def GetDefaultMinMargins(self) -> bool:
        """ Returns True if the page setup dialog will take its minimum margin values from the currently selected printer properties (Windows only).
        """

    def GetEnableHelp(self) -> bool:
        """ Returns True if the printer setup button is enabled.
        """

    def GetEnableMargins(self) -> bool:
        """ Returns True if the margin controls are enabled (Windows only).
        """

    def GetEnableOrientation(self) -> bool:
        """ Returns True if the orientation control is enabled (Windows only).
        """

    def GetEnablePaper(self) -> bool:
        """ Returns True if the paper size control is enabled (Windows only).
        """

    def GetEnablePrinter(self) -> bool:
        """ Returns True if the printer setup button is enabled.
        """

    def GetMarginBottomRight(self) -> 'Point':
        """ Returns the right (x) and bottom (y) margins in millimetres.
        """

    def GetMarginTopLeft(self) -> 'Point':
        """ Returns the left (x) and top (y) margins in millimetres.
        """

    def GetMinMarginBottomRight(self) -> 'Point':
        """ Returns the right (x) and bottom (y) minimum margins the user can enter (Windows only).
        """

    def GetMinMarginTopLeft(self) -> 'Point':
        """ Returns the left (x) and top (y) minimum margins the user can enter (Windows only).
        """

    def GetPaperId(self) -> 'PaperSize':
        """ Returns the paper id (stored in the internal   wx.PrintData  object).
        """

    def GetPaperSize(self) -> 'Size':
        """ Returns the paper size in millimetres.
        """

    def GetPrintData(self) -> 'PrintData':
        """ Returns a reference to the print data associated with this object.
        """

    def IsOk(self) -> bool:
        """ Returns True if the print data associated with the dialog data is valid.
        """

    def SetDefaultInfo(self, flag: bool) -> None:
        """ Pass True if the dialog will simply return default printer information (such as orientation) instead of showing a dialog (Windows only).
        """

    def SetDefaultMinMargins(self, flag: bool) -> None:
        """ Pass True if the page setup dialog will take its minimum margin values from the currently selected printer properties (Windows only).
        """

    def SetMarginBottomRight(self, pt: 'Point') -> None:
        """ Sets the right (x) and bottom (y) margins in millimetres.
        """

    def SetMarginTopLeft(self, pt: 'Point') -> None:
        """ Sets the left (x) and top (y) margins in millimetres.
        """

    def SetMinMarginBottomRight(self, pt: 'Point') -> None:
        """ Sets the right (x) and bottom (y) minimum margins the user can enter (Windows only).
        """

    def SetMinMarginTopLeft(self, pt: 'Point') -> None:
        """ Sets the left (x) and top (y) minimum margins the user can enter (Windows only).
        """

    def SetPaperId(self, id: PaperSize) -> None:
        """ Sets the paper size id.
        """

    def SetPaperSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the paper size in millimetres.
        """

    def SetPrintData(self, printData: 'PrintData') -> None:
        """ Sets the print data associated with this object.
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """



class PaintDC(ClientDC):
    """ A PaintDC must be constructed if an application wishes to paint on
the client area of a window from within an EVT_PAINT() event handler.
    """
    def __init__(self, window: 'Window') -> None:
        """ Constructor.
        """



class PaintEvent(Event):
    """ A paint event is sent when a windowâs contents needs to be repainted.
    """
    def __init__(self, window: 'Window') -> None:
        """ Constructor for exclusive use of wxWidgets itself.
        """

EVT_PAINT: int  #  Process a  wxEVT_PAINT   event. ^^


class Palette(GDIObject):
    """ A palette is a table that maps pixel values to RGB colours.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, red, green, blue) -> None:
        """ Creates a palette from 3 sequences of integers, one for each red, blue or green component.
        """

    def GetColoursCount(self) -> int:
        """ Returns number of entries in palette.
        """

    def GetPixel(self, red, green, blue) -> int:
        """ Returns a pixel value (index into the palette) for the given RGB values.
        """

    def GetRGB(self, pixel) -> tuple:
        """ Returns RGB values for a given palette index.
        """

    def IsOk(self) -> bool:
        """ Returns True if palette data is present.
        """



class PaletteChangedEvent(Event):
    """ winid (wx.WindowID) â 
    """
    def __init__(self, winid: int=0) -> None:
        """ winid (wx.WindowID) â
        """

    def GetChangedWindow(self) -> 'Window':
        """ wx.Window
        """

    def SetChangedWindow(self, win: 'Window') -> None:
        """ win (wx.Window) â
        """



class Panel(Window):
    """ A panel is a window on which controls are placed.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AcceptsFocus(self) -> bool:
        """ This method is overridden from wx.Window.AcceptsFocus   and returns True only if there is no child window in the panel which can accept the focus.
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=TAB_TRAVERSAL, name=PanelNameStr) -> bool:
        """ Used for two-step panel construction.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def InitDialog(self) -> None:
        """ Sends a   wx.InitDialogEvent, which in turn transfers data to the dialog via validators.
        """

    def Layout(self) -> bool:
        """ See wx.Window.SetAutoLayout : when auto layout is on, this function gets called automatically when the window is resized.
        """

    def SetFocus(self) -> None:
        """ Overrides wx.Window.SetFocus .
        """

    def SetFocusIgnoringChildren(self) -> None:
        """ In contrast to SetFocus   (see above) this will set the focus to the panel even if there are child windows in the panel.
        """

EVT_NAVIGATION_KEY: int  #  Process a navigation key event. ^^


class PanGestureEvent(GestureEvent):
    """ This event is generated when the user moves a finger on the surface.
    """
    def __init__(self, winid: int=0) -> None:
        """ Constructor.
        """

    def GetDelta(self) -> 'Point':
        """ Returns the distance covered since the previous panning event.
        """

    def SetDelta(self, delta: 'Point') -> None:
        """ Sets the distance covered since the previous panning event.
        """

EVT_GESTURE_PAN: int  #  Process a  wxEVT_GESTURE_PAN . ^^


class PasswordEntryDialog(TextEntryDialog):
    """ This class represents a dialog that requests a one-line password
string from the user.
    """
    def __init__(self, parent, message, caption=GetPasswordFromUserPromptStr, defaultValue="", style=TextEntryDialogStyle, pos=DefaultPosition) -> None:
        """ Constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

CANCEL: int
CENTRE: int
TE_PASSWORD: int


class PCXHandler(ImageHandler):
    """ This is the image handler for the PCX format.
    """
    def __init__(self) -> None:
        """ Default constructor for   wx.PCXHandler.
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Called to test if this handler can read an image from the given stream.
        """

    def LoadFile(self, image, stream, verbose=True, index=-1) -> bool:
        """ Loads an image from a stream, putting the resulting data into image.
        """

    def SaveFile(self, image, stream, verbose=True) -> bool:
        """ Saves an image in the output stream.
        """



class PenInfo:
    """ This class is a helper used for Pen creation using named parameter
idiom: it allows specifying various Pen attributes using the chained
calls to its clearly named methods instead of passing them in the
fixed order to Pen constructors.
    """


class PenList:
    """ There is only one instance of this class: ThePenList.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def FindOrCreatePen(self, colour, width=1, style=PENSTYLE_SOLID) -> 'Pen':
        """ Finds a pen with the specified attributes and returns it, else creates a new pen, adds it to the pen list, and returns it.
        """



class PickerBase(Control):
    """ Base abstract class for all pickers which support an auxiliary text
control.
    """
    def __init__(self) -> None:
        """ 
        """

    def CreateBase(self, parent, id=ID_ANY, text="", pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=ButtonNameStr) -> bool:
        """ parent (wx.Window) â
        """

    def GetInternalMargin(self) -> int:
        """ Returns the margin (in pixel) between the picker and the text control.
        """

    def GetPickerCtrl(self) -> 'Control':
        """ Returns the native implementation of the real picker control.
        """

    def GetPickerCtrlProportion(self) -> int:
        """ Returns the proportion value of the picker.
        """

    def GetPickerStyle(self, style: int) -> int:
        """ style (long) â
        """

    def GetTextCtrl(self) -> 'TextCtrl':
        """ Returns a pointer to the text control handled by this window or None if the  PB_USE_TEXTCTRL   style was not specified when this control was created.
        """

    def GetTextCtrlProportion(self) -> int:
        """ Returns the proportion value of the text control.
        """

    def GetTextCtrlStyle(self, style: int) -> int:
        """ style (long) â
        """

    def HasTextCtrl(self) -> bool:
        """ Returns True if this window has a valid text control (i.e. if the  PB_USE_TEXTCTRL   style was given when creating this control).
        """

    def IsPickerCtrlGrowable(self) -> bool:
        """ Returns True if the picker control is growable.
        """

    def IsTextCtrlGrowable(self) -> bool:
        """ Returns True if the text control is growable.
        """

    def PostCreation(self) -> None:
        """ 
        """

    def SetInternalMargin(self, margin: int) -> None:
        """ Sets the margin (in pixel) between the picker and the text control.
        """

    def SetPickerCtrl(self, picker: 'Control') -> None:
        """ picker (wx.Control) â
        """

    def SetPickerCtrlGrowable(self, grow: bool=True) -> None:
        """ Sets the picker control as growable when  grow   is True.
        """

    def SetPickerCtrlProportion(self, prop: int) -> None:
        """ Sets the proportion value of the picker.
        """

    def SetTextCtrl(self, text: 'TextCtrl') -> None:
        """ text (wx.TextCtrl) â
        """

    def SetTextCtrlGrowable(self, grow: bool=True) -> None:
        """ Sets the text control as growable when  grow   is True.
        """

    def SetTextCtrlProportion(self, prop: int) -> None:
        """ Sets the proportion value of the text control.
        """

    def UpdatePickerFromTextCtrl(self) -> None:
        """ 
        """

    def UpdateTextCtrlFromPicker(self) -> None:
        """ 
        """

PB_USE_TEXTCTRL: int  #  Creates a text control to the left of the picker which is completely managed by this   wx.PickerBase  class. ^^
PB_USE_TEXTCTRL: int


class PixelDataBase:
    """ Return the height of the area this pixel data represents.
    """
    def GetHeight(self) -> int:
        """ Return the height of the area this pixel data represents.
        """

    def GetOrigin(self) -> 'Point':
        """ Return the origin of the area this pixel data represents.
        """

    def GetRowStride(self) -> int:
        """ Returns the distance between the start of one row to the start of the next row.
        """

    def GetSize(self) -> 'Size':
        """ Return the size of the area this pixel data represents.
        """

    def GetWidth(self) -> int:
        """ Return the width of the area this pixel data represents.
        """

    def __iter__(self) -> None:
        """ Create and return an iterator/generator object for traversing
this pixel data object.
        """

    def __init__(self) -> None:
        """ 
        """



class PlatformId:
    """ Defines a very broad platform categorization.
    """


class PlatformInformation:
    """ PlatformInfo()
PlatformInfo(pid, tkMajor=-1, tkMinor=-1, id=OS_UNKNOWN, osMajor=-1, osMinor=-1, bitness=BITNESS_INVALID, endian=ENDIAN_INVALID)
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def CheckOSVersion(self, major, minor, micro=0) -> bool:
        """ Returns True if the OS version is at least  major.minor.micro .
        """

    def CheckToolkitVersion(self, major, minor, micro=0) -> bool:
        """ Returns True if the toolkit version is at least  major.minor.micro .
        """

    @staticmethod
    def Get() -> PlatformInfo:
        """ Returns the global PlatformInfo       object, initialized with the values for the currently running platform.
        """

    @staticmethod
    def GetArch(arch: str) -> 'Architecture':
        """ arch (string) â
        """

    def GetArchName(self) -> str:
        """ string
        """

    def GetArchitecture(self) -> 'Architecture':
        """ wx.Architecture
        """

    def GetBitness(self) -> 'Bitness':
        """ Returns the architecture bitness ID of this PlatformInfo       instance.
        """

    @staticmethod
    def GetBitnessName(*args, **kw) -> str:
        """ Overloaded Implementations:
        """

    def GetCpuArchitectureName(self) -> str:
        """ Returns the CPU architecture name, if available.
        """

    def GetDesktopEnvironment(self) -> str:
        """ Returns the desktop environment associated with this PlatformInfo       instance.
        """

    def GetEndianness(self) -> 'Endianness':
        """ Returns the endianness ID of this PlatformInfo       instance.
        """

    def GetEndiannessName(self) -> str:
        """ Returns the name for the endianness of this PlatformInfo       instance.
        """

    def GetLinuxDistributionInfo(self) -> 'LinuxDistributionInfo':
        """ Returns the Linux distribution info associated with this PlatformInfo       instance.
        """

    def GetNativeCpuArchitectureName(self) -> str:
        """ Returns the native CPU architecture name, if available.
        """

    def GetOSMajorVersion(self) -> int:
        """ Returns the run-time major version of the OS associated with this PlatformInfo       instance.
        """

    def GetOSMicroVersion(self) -> int:
        """ Returns the run-time micro version of the OS associated with this PlatformInfo       instance.
        """

    def GetOSMinorVersion(self) -> int:
        """ Returns the run-time minor version of the OS associated with this PlatformInfo       instance.
        """

    def GetOperatingSystemDescription(self) -> str:
        """ Returns the description of the operating system of this PlatformInfo       instance.
        """

    @staticmethod
    def GetOperatingSystemDirectory() -> str:
        """ Returns the operating system directory.
        """

    def GetOperatingSystemFamilyName(self) -> str:
        """ Returns the operating system family name of the OS associated with this PlatformInfo       instance.
        """

    def GetOperatingSystemId(self) -> 'OperatingSystemId':
        """ Returns the operating system ID of this PlatformInfo       instance.
        """

    def GetOperatingSystemIdName(self) -> str:
        """ Returns the operating system name of the OS associated with this PlatformInfo       instance.
        """

    def GetPortId(self) -> 'PortId':
        """ Returns the wxWidgets port ID associated with this PlatformInfo       instance.
        """

    def GetPortIdName(self) -> str:
        """ Returns the name of the wxWidgets port ID associated with this PlatformInfo       instance.
        """

    def GetPortIdShortName(self) -> str:
        """ Returns the short name of the wxWidgets port ID associated with this PlatformInfo       instance.
        """

    def GetToolkitMajorVersion(self) -> int:
        """ Returns the run-time major version of the toolkit associated with this PlatformInfo       instance.
        """

    def GetToolkitMicroVersion(self) -> int:
        """ Returns the run-time micro version of the toolkit associated with this PlatformInfo       instance.
        """

    def GetToolkitMinorVersion(self) -> int:
        """ Returns the run-time minor version of the toolkit associated with this PlatformInfo       instance.
        """

    def IsOk(self) -> bool:
        """ Returns True if this instance is fully initialized with valid values.
        """

    def IsUsingUniversalWidgets(self) -> bool:
        """ Returns True if this PlatformInfo       describes wxUniversal build.
        """

    def SetArchitecture(self, n: Architecture) -> None:
        """ n (Architecture) â
        """

    def SetBitness(self, n: Bitness) -> None:
        """ Sets the architecture bitness enum value associated with this PlatformInfo       instance.
        """

    def SetDesktopEnvironment(self, de: str) -> None:
        """ Sets the desktop environment associated with this PlatformInfo       instance.
        """

    def SetEndianness(self, n: Endianness) -> None:
        """ Sets the endianness enum value associated with this PlatformInfo       instance.
        """

    def SetLinuxDistributionInfo(self, di: 'LinuxDistributionInfo') -> None:
        """ Sets the linux distribution info associated with this PlatformInfo       instance.
        """

    def SetOSVersion(self, major, minor, micro=0) -> None:
        """ Sets the version of the operating system associated with this PlatformInfo       instance.
        """

    def SetOperatingSystemDescription(self, desc: str) -> None:
        """ Sets the operating system description associated with this PlatformInfo       instance.
        """

    def SetOperatingSystemId(self, n: OperatingSystemId) -> None:
        """ Sets the operating system associated with this PlatformInfo       instance.
        """

    def SetPortId(self, n: PortId) -> None:
        """ Sets the wxWidgets port ID associated with this PlatformInfo       instance.
        """

    def SetToolkitVersion(self, major, minor, micro=0) -> None:
        """ Sets the version of the toolkit associated with this PlatformInfo       instance.
        """

    def __ne__(self, item: Any) -> bool:
        """ Inequality operator.
        """

    def __eq__(self, item: Any) -> bool:
        """ Equality operator.
        """



class PNGHandler(ImageHandler):
    """ This is the image handler for the PNG format.
    """
    def __init__(self) -> None:
        """ Default constructor for   wx.PNGHandler.
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Called to test if this handler can read an image from the given stream.
        """

    def LoadFile(self, image, stream, verbose=True, index=-1) -> bool:
        """ Loads an image from a stream, putting the resulting data into image.
        """

    def SaveFile(self, image, stream, verbose=True) -> bool:
        """ Saves an image in the output stream.
        """



class PNMHandler(ImageHandler):
    """ This is the image handler for the PNM format.
    """
    def __init__(self) -> None:
        """ Default constructor for   wx.PNMHandler.
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Called to test if this handler can read an image from the given stream.
        """

    def LoadFile(self, image, stream, verbose=True, index=-1) -> bool:
        """ Loads an image from a stream, putting the resulting data into image.
        """

    def SaveFile(self, image, stream, verbose=True) -> bool:
        """ Saves an image in the output stream.
        """



class Point:
    """ A Point is a useful data structure for graphics operations.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Get(self) -> tuple:
        """ Return the x and y properties as a tuple.
        """

    def GetIM(self) -> None:
        """ Returns an immutable representation of the wx.Point object, based on namedtuple.
        """

    def IsFullySpecified(self) -> bool:
        """ Returns True if neither of the point components is equal to DefaultCoord.
        """

    def SetDefaults(self, pt: 'Point') -> None:
        """ Combine this object with another one replacing the uninitialized values.
        """

    def __eq__(self, item: Any) -> bool:
        """ bool
        """

    def __getitem__(self, idx) -> None:
        """ 
        """

    def __len__(self) -> None:
        """ 
        """

    def __ne__(self, item: Any) -> bool:
        """ bool
        """

    def __reduce__(self) -> None:
        """ 
        """

    def __repr__(self) -> None:
        """ 
        """

    def __setitem__(self, idx, val) -> None:
        """ 
        """

    def __str__(self) -> None:
        """ 
        """

    def __iadd__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def __isub__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

Point: int
Point: int
Point: int


class Point2D:
    """  Overloaded Implementations:
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Get(self) -> Any:
        """ Get() . (x,y)
        """

    def GetCrossProduct(self, vec: Point2DDouble) -> 'Double':
        """ vec (Point2DDouble) â
        """

    def GetDistance(self, pt: Point2DDouble) -> 'Double':
        """ pt (Point2DDouble) â
        """

    def GetDistanceSquare(self, pt: Point2DDouble) -> 'Double':
        """ pt (Point2DDouble) â
        """

    def GetDotProduct(self, vec: Point2DDouble) -> 'Double':
        """ vec (Point2DDouble) â
        """

    def GetFloor(self) -> tuple:
        """ tuple
        """

    def GetIM(self) -> None:
        """ Returns an immutable representation of the wx.Point2D object, based on namedtuple.
        """

    def GetRounded(self) -> tuple:
        """ tuple
        """

    def GetVectorAngle(self) -> 'Double':
        """ wx.Double
        """

    def GetVectorLength(self) -> 'Double':
        """ wx.Double
        """

    def Normalize(self) -> None:
        """ 
        """

    def SetVectorAngle(self, degrees: 'Double') -> None:
        """ degrees (wx.Double) â
        """

    def SetVectorLength(self, length: 'Double') -> None:
        """ length (wx.Double) â
        """

    def __bool__(self) -> None:
        """ 
        """

    def __getitem__(self, idx) -> None:
        """ 
        """

    def __len__(self) -> None:
        """ 
        """

    def __nonzero__(self) -> None:
        """ 
        """

    def __reduce__(self) -> None:
        """ 
        """

    def __repr__(self) -> None:
        """ 
        """

    def __setitem__(self, idx, val) -> None:
        """ 
        """

    def __str__(self) -> None:
        """ 
        """

    def __ne__(self, item: Any) -> bool:
        """ pt (Point2DDouble) â
        """

    def __imul__(self) -> None:
        """ pt (Point2DDouble) â
        """

    def __iadd__(self) -> None:
        """ pt (Point2DDouble) â
        """

    def __sub__(self) -> None:
        """ 
        """

    def __isub__(self) -> None:
        """ pt (Point2DDouble) â
        """

    def __idiv__(self) -> None:
        """ pt (Point2DDouble) â
        """

    def __eq__(self, item: Any) -> bool:
        """ pt (Point2DDouble) â
        """

Point2D: int
Point2D: int
Point2D: int


class PopupTransientWindow(PopupWindow):
    """ A PopupWindow which disappears automatically when the user clicks
mouse outside it or if it loses focus in any other way.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Dismiss(self) -> None:
        """ Hide the window.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def OnDismiss(self) -> None:
        """ This is called when the popup is disappeared because of anything else but direct call to Dismiss .
        """

    def Popup(self, focus: Optional['Window']=None) -> None:
        """ Popup the window (this will show it too).
        """

    def ProcessLeftDown(self, event: 'MouseEvent') -> bool:
        """ Called when a mouse is pressed while the popup is shown.
        """



class PopupWindow(NonOwnedWindow):
    """ A special kind of top level window used for popup menus, combobox
popups and such.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, flags=BORDER_NONE) -> bool:
        """ Create method for two-step creation.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def Position(self, ptOrigin, sizePopup) -> None:
        """ Move the popup window to the right position, i.e. such that it is entirely visible.
        """

PU_CONTAINS_CONTROLS: int  #  By default in wxMSW, a popup window will not take focus from its parent window. However many standard controls, including common ones such as   wx.TextCtrl, need focus to function correctly and will not work when placed on a default popup. This flag can be used to make the popup take focus and let all controls work but at the price of not allowing the parent window to keep focus while the popup is shown, which can also be sometimes desirable. This style is currently only implemented in MSW and simply does nothing under the other platforms (itâs new since wxWidgets 3.1.3). ^^
PU_CONTAINS_CONTROLS: int


class Position:
    """ This class represents the position of an item in any kind of grid of
rows and columns such as GridBagSizer, or HVScrolledWindow.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Get(self) -> tuple:
        """ Return the row and col properties as a tuple.
        """

    def GetCol(self) -> int:
        """ A synonym for GetColumn .
        """

    def GetColumn(self) -> int:
        """ Get the current row value.
        """

    def GetIM(self) -> None:
        """ Returns an immutable representation of the wx.Position object, based on namedtuple.
        """

    def GetRow(self) -> int:
        """ Get the current row value.
        """

    def SetCol(self, column: int) -> None:
        """ A synonym for SetColumn .
        """

    def SetColumn(self, column: int) -> None:
        """ Set a new column value.
        """

    def SetRow(self, row: int) -> None:
        """ Set a new row value.
        """

    def __bool__(self) -> None:
        """ 
        """

    def __getitem__(self, idx) -> None:
        """ 
        """

    def __len__(self) -> None:
        """ 
        """

    def __nonzero__(self) -> None:
        """ 
        """

    def __reduce__(self) -> None:
        """ 
        """

    def __repr__(self) -> None:
        """ 
        """

    def __setitem__(self, idx, val) -> None:
        """ 
        """

    def __str__(self) -> None:
        """ 
        """

    def __ne__(self, item: Any) -> bool:
        """ pos (wx.Position) â
        """

    def __add__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def __iadd__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def __sub__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def __isub__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def __eq__(self, item: Any) -> bool:
        """ pos (wx.Position) â
        """

Position: int
Position: int
Position: int


class PostScriptDC(DC):
    """ This defines the wxWidgets Encapsulated PostScript device context,
which can write PostScript files on any platform.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """



class PowerEvent(Event):
    """ The power events are generated when the system power state changes,
e.g.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def IsVetoed(self) -> bool:
        """ Returns whether Veto has been called.
        """

    def Veto(self) -> None:
        """ Call this to prevent suspend from taking place in  wxEVT_POWER_SUSPENDING   handler (it is ignored for all the others).
        """

EVT_POWER_SUSPENDING: int  # 
EVT_POWER_SUSPENDED: int  #  System is about to suspend: int  #  normally the application should quickly (i.e. without user intervention) close all the open files and network connections here, possibly remembering them to reopen them later when the system is resumed.
EVT_POWER_SUSPEND_CANCEL: int  #  System suspension was cancelled because some application vetoed it.
EVT_POWER_RESUME: int  #  System resumed from suspend: int  #  normally the application should restore the state in which it had been before the suspension. ^^


class PowerResource:
    """ Helper functions for acquiring and releasing the given power resource.
    """
    @staticmethod
    def Acquire(kind, reason="") -> bool:
        """ Acquire a power resource for the application.
        """

    @staticmethod
    def Release(kind: PowerResourceKind) -> None:
        """ Release a previously acquired power resource.
        """



class PowerResourceBlocker:
    """ Helper RAII class ensuring that power resources are released.
    """
    def __init__(self, kind, reason="") -> None:
        """ Acquires the power resource.
        """

    def IsInEffect(self) -> bool:
        """ Returns whether the power resource could be acquired.
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class PreferencesEditor:
    """ Manage preferences dialog.
    """
    def __init__(self, title: str="") -> None:
        """ Constructor.
        """

    def AddPage(self, page: 'PreferencesPage') -> None:
        """ Add a new page to the editor.
        """

    def Dismiss(self) -> None:
        """ Hide the currently shown dialog, if any.
        """

    @staticmethod
    def ShouldApplyChangesImmediately() -> bool:
        """ Returns whether changes to values in preferences pages should be applied immediately or only when the user clicks the wx.OK button.
        """

    def Show(self, parent: 'Window') -> None:
        """ Show the preferences dialog or bring it to the top if itâs already shown.
        """

    @staticmethod
    def ShownModally() -> bool:
        """ Returns whether the preferences dialog is shown modally.
        """

OK: int
OK: int


class PreferencesPage:
    """ One page of preferences dialog.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def CreateWindow(self, parent: 'Window') -> 'Window':
        """ Create a window for this page.
        """

    def GetIcon(self) -> 'BitmapBundle':
        """ Return the icon to be used for the page on some platforms.
        """

    def GetLargeIcon(self) -> 'Bitmap':
        """ wx.Bitmap
        """

    def GetName(self) -> str:
        """ Return name of the page.
        """



class PressAndTapEvent(GestureEvent):
    """ This event is generated when the user press the surface with one
finger and taps with another.
    """
    def __init__(self, windid: int=0) -> None:
        """ Constructor.
        """

EVT_PRESS_AND_TAP: int  #  Process a  wxEVT_PRESS_AND_TAP . ^^


class PreviewCanvas(Scrolled):
    """ A preview canvas is the default canvas used by the print preview
system to display the preview.
    """
    def __init__(self, preview, parent, pos=DefaultPosition, size=DefaultSize, style=0, name="canvas") -> None:
        """ Constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def OnPaint(self, event: 'PaintEvent') -> None:
        """ Calls wx.PrintPreview.PaintPage   to refresh the canvas.
        """



class PreviewControlBar(Panel):
    """ This is the default implementation of the preview control bar, a panel
with buttons and a zoom control.
    """
    def __init__(self, preview, buttons, parent, pos=DefaultPosition, size=DefaultSize, style=0, name="panel") -> None:
        """ Constructor.
        """

    def CreateButtons(self) -> None:
        """ Creates buttons, according to value of the button style flags.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetPrintPreview(self) -> 'PrintPreview':
        """ Gets the print preview object associated with the control bar.
        """

    def GetZoomControl(self) -> int:
        """ Gets the current zoom setting in percent.
        """

    def SetZoomControl(self, percent: int) -> None:
        """ Sets the zoom control.
        """

PREVIEW_PRINT: int
PREVIEW_NEXT: int
PREVIEW_PREVIOUS: int
PREVIEW_ZOOM: int
PREVIEW_DEFAULT: int


class PreviewFrame(Frame):
    """ This class provides the default method of managing the print preview
interface.
    """
    def __init__(self, preview, parent, title="PrintPreview", pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE, name=FrameNameStr) -> None:
        """ Constructor.
        """

    def CreateCanvas(self) -> None:
        """ Creates a   wx.PreviewCanvas.
        """

    def CreateControlBar(self) -> None:
        """ Creates a   wx.PreviewControlBar.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def Initialize(self) -> None:
        """ Initializes the frame elements and prepares for showing it.
        """

    def InitializeWithModality(self, kind: PreviewFrameModalityKind) -> None:
        """ Initializes the frame elements and prepares for showing it with the given modality kind.
        """

    def OnCloseWindow(self, event: 'CloseEvent') -> None:
        """ Enables any disabled frames in the application, and deletes the print preview object, implicitly deleting any printout objects associated with the print preview object.
        """



class PrintAbortDialog(Dialog):
    """ The dialog created by default by the print framework that enables
aborting the printing process.
    """
    def __init__(self, parent, documentTitle, pos=DefaultPosition, size=DefaultSize, style=DEFAULT_DIALOG_STYLE, name="dialog") -> None:
        """ parent (wx.Window) â
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def SetProgress(self, currentPage, totalPages, currentCopy, totalCopies) -> None:
        """ currentPage (int) â
        """



class PrintData(Object):
    """ This class holds a variety of information related to printers and
printer device contexts.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetBin(self) -> 'PrintBin':
        """ Returns the current bin (papersource).
        """

    def GetCollate(self) -> bool:
        """ Returns True if collation is on.
        """

    def GetColour(self) -> bool:
        """ Returns True if colour printing is on.
        """

    def GetDuplex(self) -> 'DuplexMode':
        """ Returns the duplex mode.
        """

    def GetFilename(self) -> str:
        """ string
        """

    def GetNoCopies(self) -> int:
        """ Returns the number of copies requested by the user.
        """

    def GetOrientation(self) -> 'PrintOrientation':
        """ Gets the orientation.
        """

    def GetPaperId(self) -> 'PaperSize':
        """ Returns the paper size id.
        """

    def GetPaperSize(self) -> 'Size':
        """ wx.Size
        """

    def GetPrintMode(self) -> 'PrintMode':
        """ wx.PrintMode
        """

    def GetPrinterName(self) -> str:
        """ Returns the printer name.
        """

    def GetPrivData(self) -> Any:
        """ PyObject
        """

    def GetQuality(self) -> 'PrintQuality':
        """ Returns the current print quality.
        """

    def IsOk(self) -> bool:
        """ Returns True if the print data is valid for using in print dialogs.
        """

    def SetBin(self, flag: PrintBin) -> None:
        """ Sets the current bin.
        """

    def SetCollate(self, flag: bool) -> None:
        """ Sets collation to on or off.
        """

    def SetColour(self, flag: bool) -> None:
        """ Sets colour printing on or off.
        """

    def SetDuplex(self, mode: DuplexMode) -> None:
        """ Returns the duplex mode.
        """

    def SetFilename(self, filename: str) -> None:
        """ filename (string) â
        """

    def SetNoCopies(self, n: int) -> None:
        """ Sets the default number of copies to be printed out.
        """

    def SetOrientation(self, orientation: PrintOrientation) -> None:
        """ Sets the orientation.
        """

    def SetPaperId(self, paperId: PaperSize) -> None:
        """ Sets the paper id.
        """

    def SetPaperSize(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetPrintMode(self, printMode: PrintMode) -> None:
        """ printMode (PrintMode) â
        """

    def SetPrinterName(self, printerName: str) -> None:
        """ Sets the printer name.
        """

    def SetPrivData(self, data) -> None:
        """ 
        """

    def SetQuality(self, quality: 'PrintQuality') -> None:
        """ Sets the desired print quality.
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """

DUPLEX_SIMPLEX: int
DUPLEX_HORIZONTAL: int
DUPLEX_VERTICAL: int
LANDSCAPE: int
PORTRAIT: int
PRINT_QUALITY_HIGH: int
PRINT_QUALITY_MEDIUM: int
PRINT_QUALITY_LOW: int
PRINT_QUALITY_DRAFT: int
DUPLEX_SIMPLEX: int
DUPLEX_HORIZONTAL: int
DUPLEX_VERTICAL: int
LANDSCAPE: int
PORTRAIT: int
PRINT_QUALITY_HIGH: int
PRINT_QUALITY_MEDIUM: int
PRINT_QUALITY_LOW: int
PRINT_QUALITY_DRAFT: int


class PrintDialog(Object):
    """ This class represents the print and print setup common dialogs.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetPrintDC(self) -> 'DC':
        """ Returns the device context created by the print dialog, if any.
        """

    def GetPrintData(self) -> 'PrintData':
        """ Returns the print data  associated with the print dialog.
        """

    def GetPrintDialogData(self) -> 'PrintDialogData':
        """ Returns the print dialog data  associated with the print dialog.
        """

    def ShowModal(self) -> int:
        """ Shows the dialog, returning  ID_OK   if the user pressed wx.OK, and   ID_CANCEL   otherwise.
        """

OK: int
OK: int


class PrintDialogData(Object):
    """ This class holds information related to the visual characteristics of
PrintDialog.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def EnableHelp(self, flag: bool) -> None:
        """ Enables or disables the âHelpâ button.
        """

    def EnablePageNumbers(self, flag: bool) -> None:
        """ Enables or disables the âPage numbersâ controls.
        """

    def EnablePrintToFile(self, flag: bool) -> None:
        """ Enables or disables the âPrint to fileâ checkbox.
        """

    def EnableSelection(self, flag: bool) -> None:
        """ Enables or disables the âSelectionâ radio button.
        """

    def GetAllPages(self) -> bool:
        """ Returns True if the user requested that all pages be printed.
        """

    def GetCollate(self) -> bool:
        """ Returns True if the user requested that the document(s) be collated.
        """

    def GetFromPage(self) -> int:
        """ Returns the from  page number, as entered by the user.
        """

    def GetMaxPage(self) -> int:
        """ Returns the maximum  page number.
        """

    def GetMinPage(self) -> int:
        """ Returns the minimum  page number.
        """

    def GetNoCopies(self) -> int:
        """ Returns the number of copies requested by the user.
        """

    def GetPrintData(self) -> 'PrintData':
        """ Returns a reference to the internal   wx.PrintData  object.
        """

    def GetPrintToFile(self) -> bool:
        """ Returns True if the user has selected printing to a file.
        """

    def GetSelection(self) -> bool:
        """ Returns True if the user requested that the selection be printed (where âselectionâ is a concept specific to the application).
        """

    def GetToPage(self) -> int:
        """ Returns the âprint toâ  page number, as entered by the user.
        """

    def IsOk(self) -> bool:
        """ Returns True if the print data is valid for using in print dialogs.
        """

    def SetCollate(self, flag: bool) -> None:
        """ Sets the âCollateâ checkbox to True or False.
        """

    def SetFromPage(self, page: int) -> None:
        """ Sets the from  page number.
        """

    def SetMaxPage(self, page: int) -> None:
        """ Sets the maximum  page number.
        """

    def SetMinPage(self, page: int) -> None:
        """ Sets the minimum  page number.
        """

    def SetNoCopies(self, n: int) -> None:
        """ Sets the default number of copies the user has requested to be printed out.
        """

    def SetPrintData(self, printData: 'PrintData') -> None:
        """ Sets the internal   wx.PrintData.
        """

    def SetPrintToFile(self, flag: bool) -> None:
        """ Sets the âPrint to fileâ checkbox to True or False.
        """

    def SetSelection(self, flag: bool) -> None:
        """ Selects the âSelectionâ radio button.
        """

    def SetToPage(self, page: int) -> None:
        """ Sets the âprint toâ  page number.
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """



class Printer(Object):
    """ This class represents the Windows or PostScript printer, and is the
vehicle through which printing may be launched by an application.
    """
    def __init__(self, data: Optional['PrintDialogData']=None) -> None:
        """ Constructor.
        """

    def CreateAbortWindow(self, parent, printout) -> 'PrintAbortDialog':
        """ Creates the default printing abort window, with a cancel button.
        """

    def GetAbort(self) -> bool:
        """ Returns True if the user has aborted the print job.
        """

    @staticmethod
    def GetLastError() -> 'PrinterError':
        """ Return last error.
        """

    def GetPrintDialogData(self) -> 'PrintDialogData':
        """ Returns the print data  associated with the printer object.
        """

    def Print(self, parent, printout, prompt=True) -> bool:
        """ Starts the printing process.
        """

    def PrintDialog(self, parent: 'Window') -> 'DC':
        """ Invokes the print dialog.
        """

    def ReportError(self, parent, printout, message) -> None:
        """ Default error-reporting function.
        """

    def Setup(self, parent: 'Window') -> bool:
        """ Invokes the print setup dialog.
        """

PRINTER_NO_ERROR: int
PRINTER_CANCELLED: int
PRINTER_ERROR: int


class PrinterDC(DC):
    """ A printer device context is specific to MSW and Mac, and allows access
to any printer with a Windows or Macintosh driver.
    """
    def __init__(self, printData: 'PrintData') -> None:
        """ Constructor.
        """

    def GetPaperRect(self) -> 'Rect':
        """ Return the rectangle in device coordinates that corresponds to the full paper area, including the nonprinting regions of the paper.
        """



class Printout(Object):
    """ This class encapsulates the functionality of printing out an
application document.
    """
    def __init__(self, title: str="Printout") -> None:
        """ Constructor.
        """

    def FitThisSizeToPage(self, imageSize: Union[tuple[int, int], 'Size']) -> None:
        """ Set the user scale and device origin of the   wx.DC  associated with this   wx.Printout  so that the given image size fits entirely within the page rectangle and the origin is at the top left corner of the page rectangle.
        """

    def FitThisSizeToPageMargins(self, imageSize, pageSetupData) -> None:
        """ Set the user scale and device origin of the   wx.DC  associated with this   wx.Printout  so that the given image size fits entirely within the page margins set in the given   wx.PageSetupDialogData  object.
        """

    def FitThisSizeToPaper(self, imageSize: Union[tuple[int, int], 'Size']) -> None:
        """ Set the user scale and device origin of the   wx.DC  associated with this   wx.Printout  so that the given image size fits entirely within the paper and the origin is at the top left corner of the paper.
        """

    def GetDC(self) -> 'DC':
        """ Returns the device context associated with the printout (given to the printout at start of printing or previewing).
        """

    def GetLogicalPageMarginsRect(self, pageSetupData: 'PageSetupDialogData') -> 'Rect':
        """ Return the rectangle corresponding to the page margins specified by the given   wx.PageSetupDialogData  object in the associated   wx.DCâs logical coordinates for the current user scale and device origin.
        """

    def GetLogicalPageRect(self) -> 'Rect':
        """ Return the rectangle corresponding to the page in the associated   wx.DC  âs logical coordinates for the current user scale and device origin.
        """

    def GetLogicalPaperRect(self) -> 'Rect':
        """ Return the rectangle corresponding to the paper in the associated   wx.DC  âs logical coordinates for the current user scale and device origin.
        """

    def GetPPIPrinter(self) -> None:
        """ Returns the number of pixels per logical inch of the printer device context.
        """

    def GetPPIScreen(self) -> None:
        """ Returns the number of pixels per logical inch of the screen device context.
        """

    def GetPageInfo(self) -> tuple:
        """ Called by the framework to obtain information from the application about minimum and maximum page values that the user can select, and the required page range to be printed.
        """

    def GetPageSizeMM(self) -> None:
        """ Returns the size of the printer page in millimetres.
        """

    def GetPageSizePixels(self) -> tuple:
        """ Returns the size of the printer page in pixels, called the page rectangle.
        """

    def GetPaperRectPixels(self) -> 'Rect':
        """ Returns the rectangle that corresponds to the entire paper in pixels, called the paper rectangle.
        """

    def GetPreview(self) -> 'PrintPreview':
        """ Returns the associated preview object if any.
        """

    def GetTitle(self) -> str:
        """ Returns the title of the printout.
        """

    def HasPage(self, pageNum: int) -> bool:
        """ Should be overridden to return True if the document has this page, or False if not.
        """

    def IsPreview(self) -> bool:
        """ Returns True if the printout is currently being used for previewing.
        """

    def MapScreenSizeToDevice(self) -> None:
        """ Set the user scale and device origin of the   wx.DC  associated with this   wx.Printout  so that one screen pixel maps to one device pixel on the DC.
        """

    def MapScreenSizeToPage(self) -> None:
        """ This sets the user scale of the   wx.DC  associated with this   wx.Printout  to the same scale as MapScreenSizeToPaper   but sets the logical origin to the top left corner of the page rectangle.
        """

    def MapScreenSizeToPageMargins(self, pageSetupData: 'PageSetupDialogData') -> None:
        """ This sets the user scale of the   wx.DC  associated with this   wx.Printout  to the same scale as MapScreenSizeToPageMargins   but sets the logical origin to the top left corner of the page margins specified by the given   wx.PageSetupDialogData  object.
        """

    def MapScreenSizeToPaper(self) -> None:
        """ Set the user scale and device origin of the   wx.DC  associated with this   wx.Printout  so that the printed page matches the screen size as closely as possible and the logical origin is in the top left corner of the paper rectangle.
        """

    def OffsetLogicalOrigin(self, xoff, yoff) -> None:
        """ Shift the device origin by an amount specified in logical coordinates.
        """

    def OnBeginDocument(self, startPage, endPage) -> bool:
        """ Called by the framework at the start of document printing.
        """

    def OnBeginPrinting(self) -> None:
        """ Called by the framework at the start of printing.
        """

    def OnEndDocument(self) -> None:
        """ Called by the framework at the end of document printing.
        """

    def OnEndPrinting(self) -> None:
        """ Called by the framework at the end of printing.
        """

    def OnPreparePrinting(self) -> None:
        """ Called once by the framework before any other demands are made of the   wx.Printout  object.
        """

    def OnPrintPage(self, pageNum: int) -> bool:
        """ Called by the framework when a page should be printed.
        """

    def SetLogicalOrigin(self, x, y) -> None:
        """ Set the device origin of the associated   wx.DC  so that the current logical point becomes the new logical origin.
        """



class PrintPreview(Object):
    """ Objects of this class manage the print preview process.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetCanvas(self) -> 'PreviewCanvas':
        """ Gets the preview window used for displaying the print preview image.
        """

    def GetCurrentPage(self) -> int:
        """ Gets the page currently being previewed.
        """

    def GetFrame(self) -> 'Frame':
        """ Gets the frame used for displaying the print preview canvas and control bar.
        """

    def GetMaxPage(self) -> int:
        """ Returns the maximum page number.
        """

    def GetMinPage(self) -> int:
        """ Returns the minimum page number.
        """

    def GetPrintout(self) -> 'Printout':
        """ Gets the preview printout object associated with the   wx.PrintPreview  object.
        """

    def GetPrintoutForPrinting(self) -> 'Printout':
        """ Gets the printout object to be used for printing from within the preview interface, or None if none exists.
        """

    def IsOk(self) -> bool:
        """ Returns True if the   wx.PrintPreview  is valid, False otherwise.
        """

    def PaintPage(self, canvas, dc) -> bool:
        """ This refreshes the preview window with the preview image.
        """

    def Print(self, prompt: bool) -> bool:
        """ Invokes the print process using the second   wx.Printout  object supplied in the   wx.PrintPreview  constructor.
        """

    def RenderPage(self, pageNum: int) -> bool:
        """ Renders a page into a   wx.MemoryDC.
        """

    def SetCanvas(self, window: 'PreviewCanvas') -> None:
        """ Sets the window to be used for displaying the print preview image.
        """

    def SetCurrentPage(self, pageNum: int) -> bool:
        """ Sets the current page to be previewed.
        """

    def SetFrame(self, frame: 'Frame') -> None:
        """ Sets the frame to be used for displaying the print preview canvas and control bar.
        """

    def SetPrintout(self, printout: 'Printout') -> None:
        """ Associates a printout object with the   wx.PrintPreview  object.
        """

    def SetZoom(self, percent: int) -> None:
        """ Sets the percentage preview zoom, and refreshes the preview canvas accordingly.
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """



class Process(EvtHandler):
    """ The objects of this class are used in conjunction with the Execute()
function.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Activate(self) -> bool:
        """ Activates a GUI process by bringing up its main window to the front.
        """

    def CloseOutput(self) -> None:
        """ Closes the output stream (the one connected to the stdin of the child process).
        """

    def Detach(self) -> None:
        """ Detaches this event handler from the parent specified in the constructor (see wx.EvtHandler.Unlink   for a similar but not identical function).
        """

    @staticmethod
    def Exists(pid: int) -> bool:
        """ Returns True if the given process exists in the system.
        """

    def GetErrorStream(self) -> 'InputStream':
        """ Returns an input stream which corresponds to the standard error output (stderr) of the child process.
        """

    def GetInputStream(self) -> 'InputStream':
        """ It returns an input stream corresponding to the standard output stream of the subprocess.
        """

    def GetOutputStream(self) -> 'OutputStream':
        """ It returns an output stream corresponding to the input stream of the subprocess.
        """

    def GetPid(self) -> int:
        """ Returns the process ID of the process launched by Open   or set by wx.Execute       (if you passed this   wx.Process  as argument).
        """

    def IsErrorAvailable(self) -> bool:
        """ Returns True if there is data to be read on the child process standard error stream.
        """

    def IsInputAvailable(self) -> bool:
        """ Returns True if there is data to be read on the child process standard output stream.
        """

    def IsInputOpened(self) -> bool:
        """ Returns True if the child process standard output stream is opened.
        """

    @staticmethod
    def Kill(pid, sig=SIGTERM, flags=KILL_NOCHILDREN) -> 'KillError':
        """ Send the specified signal to the given process.
        """

    def OnTerminate(self, pid, status) -> None:
        """ It is called when the process with the pid pid  finishes.
        """

    @staticmethod
    def Open(cmd, flags=EXEC_ASYNC) -> 'Process':
        """ This static method replaces the standard  popen()   function: it launches the process specified by the  cmd  parameter and returns the   wx.Process  object which can be used to retrieve the streams connected to the standard input, output and error output of the child process.
        """

    def Redirect(self) -> None:
        """ Turns on redirection.
        """

    def SetPriority(self, priority: Any) -> None:
        """ Sets the priority of the process, between 0 (lowest) and 100 (highest).
        """

EVT_END_PROCESS: int  #  Process a  wxEVT_END_PROCESS   event, sent by  wx.Process.OnTerminate   upon the external process termination. ^^


class ProcessEvent(Event):
    """ A process event is sent to the EvtHandler specified to Process
when a process is terminated.
    """
    def __init__(self, id=0, pid=0, exitcode=0) -> None:
        """ Constructor.
        """

    def GetExitCode(self) -> int:
        """ Returns the exist status.
        """

    def GetPid(self) -> int:
        """ Returns the process id.
        """

EVT_END_PROCESS: int  #  Process a  wxEVT_END_PROCESS   event.  id  is the identifier of the process object (the id passed to the   wx.Process  constructor) or a window to receive the event. ^^


class ProgressDialog(GenericProgressDialog):
    """ If supported by the platform this class will provide the platformâs
native progress dialog, else it will simply be the
GenericProgressDialog.
    """
    def __init__(self, title, message, maximum=100, parent=None, style=PD_APP_MODAL|PD_AUTO_HIDE) -> None:
        """ title (string) â
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetMessage(self) -> str:
        """ Returns the last message passed to the Update   function; if you always passed ââ to Update   then the message set through the constructor is returned.
        """

    def GetRange(self) -> int:
        """ Returns the maximum value of the progress meter, as passed to the constructor or  NOT_FOUND   if the dialog has no progress bar.
        """

    def GetValue(self) -> int:
        """ Returns the last value passed to the Update   function or  NOT_FOUND   if the dialog has no progress bar.
        """

    def Pulse(self, newmsg: str="") -> tuple:
        """ Like Update   but makes the gauge control run in indeterminate mode.
        """

    def Resume(self) -> None:
        """ Can be used to continue with the dialog, after the user had clicked the âAbortâ button.
        """

    def SetRange(self, maximum: int) -> None:
        """ Changes the maximum value of the progress meter given in the constructor.
        """

    def Update(self, value, newmsg="") -> tuple:
        """ Updates the dialog, setting the progress bar to the new value and updating the message if new one is specified.
        """

    def WasCancelled(self) -> bool:
        """ Returns True if the âCancelâ button was pressed.
        """

    def WasSkipped(self) -> bool:
        """ Returns True if the âSkipâ button was pressed.
        """



class PropagateOnce:
    """ Helper class to temporarily lower propagation level.
    """
    def __init__(self, event: 'Event') -> None:
        """ event (wx.Event) â
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class PropagationDisabler:
    """ Helper class to temporarily change an event to not propagate.
    """
    def __init__(self, event: 'Event') -> None:
        """ event (wx.Event) â
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """



class PyApp(AppConsole):
    """ The App class represents the application itself when USE_GUI=1.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    @staticmethod
    def GTKSuppressDiagnostics(flags: int=-1) -> None:
        """ Disables the printing of various GTK messages.
        """

    def GetAssertMode(self) -> 'AppAssertMode':
        """ Returns the current mode for how the application responds to  asserts.
        """

    @staticmethod
    def GetComCtl32Version() -> int:
        """ Returns 400, 470, 471, etc. for comctl32.dll 4.00, 4.70, 4.71 or 0 if
it wasnât found at all.  Raises an exception on non-Windows platforms.
        """

    def GetDisplayMode(self) -> 'VideoMode':
        """ Get display mode that is used use.
        """

    def GetExitOnFrameDelete(self) -> bool:
        """ Returns True if the application will exit when the top-level frame is deleted.
        """

    def GetLayoutDirection(self) -> int:
        """ Return the layout direction for the current locale or  Layout_Default   if itâs unknown.
        """

    @staticmethod
    def GetMainTopWindow() -> 'Window':
        """ Returns a pointer to the top application window if any.
        """

    def GetTopWindow(self) -> 'Window':
        """ Returns a pointer to the top window.
        """

    def GetUseBestVisual(self) -> bool:
        """ Returns True if the application will use the best visual on systems that support different visuals, False otherwise.
        """

    def IsActive(self) -> bool:
        """ Returns True if the application is active, i.e. if one of its windows is currently in the foreground.
        """

    @staticmethod
    def IsDisplayAvailable() -> bool:
        """ Returns True if the application is able to connect to the systemâs
display, or whatever the equivallent is for the platform.
        """

    def MacHideApp(self) -> None:
        """ Hide all application windows just as the user can do with the
system Hide command.  Mac only.
        """

    def MacNewFile(self) -> None:
        """ Called in response of an âopen-applicationâ Apple event.
        """

    def MacOpenFile(self, fileName: str) -> None:
        """ Called in response of an âopen-documentâ Apple event.
        """

    def MacOpenFiles(self, fileNames: list[str]) -> None:
        """ Called in response of an openFiles message.
        """

    def MacOpenURL(self, url: str) -> None:
        """ Called in response of a âget-urlâ Apple event.
        """

    def MacPrintFile(self, fileName: str) -> None:
        """ Called in response of a âprint-documentâ Apple event.
        """

    def MacReopenApp(self) -> None:
        """ Called in response of a âreopen-applicationâ Apple event.
        """

    def OSXEnableAutomaticTabbing(self, enable: bool) -> None:
        """ Enable the automatic tabbing features of macOS.
        """

    def OSXIsGUIApplication(self) -> bool:
        """ May be overridden to indicate that the application is not a foreground GUI application under macOS.
        """

    def SafeYield(self, win, onlyIfNeeded) -> bool:
        """ This function is similar to wx.Yield     , except that it disables the user input to all program windows before calling wx.AppConsole.Yield   and re-enables it again afterwards.
        """

    def SafeYieldFor(self, win, eventsToProcess) -> bool:
        """ Works like wx.SafeYield       with onlyIfNeeded  == True except that it allows the caller to specify a mask of events to be processed.
        """

    def SetAssertMode(self, wxAppAssertMode: AppAssertMode) -> None:
        """ Set the mode indicating how the application responds to  assertion
statements. Valid settings are a combination of these flags:
        """

    def SetDisplayMode(self, info: 'VideoMode') -> bool:
        """ Set display mode to use.
        """

    def SetExitOnFrameDelete(self, flag: bool) -> None:
        """ Allows the programmer to specify whether the application will exit when the top-level frame is deleted.
        """

    def SetNativeTheme(self, theme: str) -> bool:
        """ Allows runtime switching of the UI environment theme.
        """

    def SetTopWindow(self, window: 'Window') -> None:
        """ Sets the âtopâ window.
        """

    def SetUseBestVisual(self, flag, forceTrueColour=False) -> None:
        """ Allows the programmer to specify whether the application will use the best visual on systems that support several visual on the same display.
        """

EVT_QUERY_END_SESSION: int  #  Process a query end session event, supplying the member function. See   wx.CloseEvent.
EVT_END_SESSION: int  #  Process an end session event, supplying the member function. See   wx.CloseEvent.
EVT_ACTIVATE_APP: int  #  Process a  wxEVT_ACTIVATE_APP   event. See    wx.ActivateEvent.
EVT_HIBERNATE: int  #  Process a hibernate event. See   wx.ActivateEvent.
EVT_DIALUP_CONNECTED: int  #  A connection with the network was established. See DialUpEvent     .
EVT_DIALUP_DISCONNECTED: int  #  The connection with the network was lost. See DialUpEvent     .
EVT_IDLE: int  #  Process a  wxEVT_IDLE   event. See    wx.IdleEvent. ^^


class PyCommandEvent:
    """ PyCommandEvent can be used as a base class for implementing
custom event types in Python. You should derive from this class
instead of CommandEvent because this class is Python-aware
and is able to transport its Python bits safely through the
wxWidgets event system and have them still be there when the
event handler is invoked. Note that since PyCommandEvent is
taking care of preserving the extra attributes that have been set
then you do not need to override the Clone method in your
derived classes.
    """
    def __init__(self, eventType=wxEVT_NULL, id=0) -> None:
        """ eventType (wx.EventType) â
        """

    def Clone(self) -> None:
        """ Make a new instance of the event that is a copy of self.
        """

    def __delattr__(self, name: Any) -> None:
        """ name (PyObject) â
        """

    def __getattr__(self, name: Any) -> Any:
        """ name (PyObject) â
        """

    def __setattr__(self, name, value) -> None:
        """ name (PyObject) â
        """

    def _getAttrDict(self) -> Any:
        """ Gives access to the internal object that is tracking the eventâs python attributes.
        """



class PyEvent:
    """ PyEvent can be used as a base class for implementing custom
event types in Python. You should derive from this class instead
of Event because this class is Python-aware and is able to
transport its Python bits safely through the wxWidgets event
system and have them still be there when the event handler is
invoked. Note that since PyEvent is taking care of preserving
the extra attributes that have been set then you do not need to
override the Clone method in your derived classes.
    """
    def __init__(self, id=0, eventType=wxEVT_NULL) -> None:
        """ id (int) â
        """

    def Clone(self) -> None:
        """ Make a new instance of the event that is a copy of self.
        """

    def __delattr__(self, name: Any) -> None:
        """ name (PyObject) â
        """

    def __getattr__(self, name: Any) -> Any:
        """ name (PyObject) â
        """

    def __setattr__(self, name, value) -> None:
        """ name (PyObject) â
        """

    def _getAttrDict(self) -> Any:
        """ Gives access to the internal object that is tracking the eventâs python attributes.
        """



class PyEventBinder:
    """ Instances of this class are used to bind specific events to event handlers.
    """
    def __init__(self, evtType, expectedIDs=0) -> None:
        """ 
        """

    def Bind(self, target, id1, id2, function) -> None:
        """ Bind this set of event types to target using its Connect() method.
        """

    def Unbind(self, target, id1, id2, handler=None) -> None:
        """ Remove an event binding.
        """

    def __call__(self, *args) -> None:
        """ For backwards compatibility with the old EVT_* functions.
Should be called with either (window, func), (window, ID,
func) or (window, ID1, ID2, func) parameters depending on the
type of the event.
        """

    def _getEvtType(self) -> None:
        """ Make it easy to get to the default wxEventType typeID for this
event binder.
        """



class PyOnDemandOutputWindow:
    """ A class that can be used for redirecting Pythonâs stdout and
stderr streams.  It will do nothing until something is wrriten to
the stream at which point it will create a Frame with a text area
and write the text there.
    """
    def __init__(self, title="wxPython: stdout/stderr") -> None:
        """ 
        """

    def CreateOutputWindow(self, txt) -> None:
        """ 
        """

    def OnCloseWindow(self, event) -> None:
        """ 
        """

    def SetParent(self, parent) -> None:
        """ Set the window to be used as the popup Frameâs parent.
        """

    def close(self) -> None:
        """ 
        """

    def flush(self) -> None:
        """ 
        """

    def write(self, text) -> None:
        """ Create the output window if needed and write the string to it.
If not called in the context of the gui thread then CallAfter is
used to do the work there.
        """



class PySimpleApp(App):
    """ This class is deprecated.  Please use App instead.
    """
    def __init__(self, *args, **kw) -> None:
        """ 
        """



class QueryNewPaletteEvent(Event):
    """ winid (wx.WindowID) â 
    """
    def __init__(self, winid: int=0) -> None:
        """ winid (wx.WindowID) â
        """

    def GetPaletteRealized(self) -> bool:
        """ bool
        """

    def SetPaletteRealized(self, realized: bool) -> None:
        """ realized (bool) â
        """



class RadioBox(Control, ItemContainerImmutable):
    """ A radio box item is used to select one of number of mutually exclusive
choices.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, label="", pos=DefaultPosition, size=DefaultSize, choices=[], majorDimension=0, style=RA_SPECIFY_COLS, validator=DefaultValidator, name=RadioBoxNameStr) -> bool:
        """ Creates the radiobox for two-step construction.
        """

    def EnableItem(self, n, enable=True) -> bool:
        """ Enables or disables an individual button in the radiobox.
        """

    def FindString(self, string, bCase=False) -> int:
        """ Finds a button matching the given string, returning the position if found, or  NOT_FOUND   if not found.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetColumnCount(self) -> int:
        """ Returns the number of columns in the radiobox.
        """

    def GetCount(self) -> int:
        """ Returns the number of items in the control.
        """

    def GetItemFromPoint(self, pt: 'Point') -> int:
        """ Returns a radio box item under the point, a zero-based item index, or  NOT_FOUND   if no item is under the point.
        """

    def GetItemHelpText(self, item: int) -> str:
        """ Returns the helptext associated with the specified item  if any or  "" .
        """

    def GetItemLabel(self, n) -> None:
        """ Return the text of the nâth item in the radio box.
        """

    def GetItemToolTip(self, item: int) -> 'ToolTip':
        """ Returns the tooltip associated with the specified item  if any or None.
        """

    def GetRowCount(self) -> int:
        """ Returns the number of rows in the radiobox.
        """

    def GetSelection(self) -> int:
        """ Returns the index of the selected item.
        """

    def GetString(self, n: int) -> str:
        """ Returns the label of the item with the given index.
        """

    def IsItemEnabled(self, n: int) -> bool:
        """ Returns True if the item is enabled or False if it was disabled using Enable .
        """

    def IsItemShown(self, n: int) -> bool:
        """ Returns True if the item is currently shown or False if it was hidden using Show .
        """

    def SetItemHelpText(self, item, helptext) -> None:
        """ Sets the helptext for an item.
        """

    def SetItemLabel(self, n, text) -> None:
        """ SetItemLabel(self, n, text)
        """

    def SetItemToolTip(self, item, text) -> None:
        """ Sets the tooltip text for the specified item in the radio group.
        """

    def SetSelection(self, n: int) -> None:
        """ Sets the selection to the given item.
        """

    def SetString(self, n, string) -> None:
        """ Sets the label for the given item.
        """

    def ShowItem(self, item, show=True) -> bool:
        """ Shows or hides individual buttons.
        """

RA_SPECIFY_ROWS: int  #  The major dimension parameter refers to the maximum number of rows.
RA_SPECIFY_COLS: int  #  The major dimension parameter refers to the maximum number of columns. ^^
EVT_RADIOBOX: int  #  Process a  wxEVT_RADIOBOX   event, when a radiobutton is clicked. ^^
RA_SPECIFY_ROWS: int
RA_SPECIFY_COLS: int


class RadioButton(Control):
    """ A radio button item is a button which usually denotes one of several
mutually exclusive options.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, label="", pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=RadioButtonNameStr) -> bool:
        """ Creates the choice for two-step construction.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetFirstInGroup(self) -> 'RadioButton':
        """ Returns the first button of the radio button group this button belongs to.
        """

    def GetLastInGroup(self) -> 'RadioButton':
        """ Returns the last button of the radio button group this button belongs to.
        """

    def GetNextInGroup(self) -> 'RadioButton':
        """ Returns the next radio button in the same group.
        """

    def GetPreviousInGroup(self) -> 'RadioButton':
        """ Returns the previous radio button in the same group.
        """

    def GetValue(self) -> bool:
        """ Returns True if the radio button is checked, False otherwise.
        """

    def SetValue(self, value: bool) -> None:
        """ Sets the radio button to checked or unchecked status.
        """

RB_GROUP: int  #  Marks the beginning of a new group of radio buttons.
RB_SINGLE: int  #  Creates a radio button which is not part of any radio button group. When this style is used, no other radio buttons will be turned off automatically when this button is turned on and such behaviour will need to be implemented manually, in the event handler for this button. ^^
EVT_RADIOBUTTON: int  #  Process a  wxEVT_RADIOBUTTON   event, when the radiobutton is clicked. ^^
RB_GROUP: int
RB_SINGLE: int


class RealPoint:
    """ A RealPoint is a useful data structure for graphics operations.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Get(self) -> tuple:
        """ Return the pointâs properties as a tuple.
        """

    def GetIM(self) -> None:
        """ Returns an immutable representation of the wx.RealPoint object, based on namedtuple.
        """

    def __bool__(self) -> None:
        """ 
        """

    def __eq__(self, item: Any) -> bool:
        """ bool
        """

    def __getitem__(self, idx) -> None:
        """ 
        """

    def __len__(self) -> None:
        """ 
        """

    def __mul__(self, d) -> 'RealPoint':
        """ wx.RealPoint
        """

    def __ne__(self, item: Any) -> bool:
        """ bool
        """

    def __nonzero__(self) -> None:
        """ 
        """

    def __reduce__(self) -> None:
        """ 
        """

    def __repr__(self) -> None:
        """ 
        """

    def __setitem__(self, idx, val) -> None:
        """ 
        """

    def __str__(self) -> None:
        """ 
        """

    def __iadd__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def __isub__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

RealPoint: int
RealPoint: int
RealPoint: int


class RearrangeCtrl(Panel):
    """ A composite control containing a RearrangeList and the buttons
allowing to move the items in it.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, order=[], items=[], style=0, validator=DefaultValidator, name=RearrangeListNameStr) -> bool:
        """ Effectively creates the window for an object created using the default constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetList(self) -> 'RearrangeList':
        """ Return the listbox which is the main part of this control.
        """



class RearrangeList(CheckListBox):
    """ A listbox-like control allowing the user to rearrange the items and to
enable or disable them.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def CanMoveCurrentDown(self) -> bool:
        """ Return True if the currently selected item can be moved down.
        """

    def CanMoveCurrentUp(self) -> bool:
        """ Return True if the currently selected item can be moved up.
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, order=[], items=[], style=0, validator=DefaultValidator, name=RearrangeListNameStr) -> bool:
        """ Effectively creates the window for an object created using the default constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetCurrentOrder(self) -> list[int]:
        """ Return the current order of the items.
        """

    def MoveCurrentDown(self) -> bool:
        """ Move the currently selected item one position below.
        """

    def MoveCurrentUp(self) -> bool:
        """ Move the currently selected item one position above.
        """



class RearrangeDialog(Dialog):
    """ A dialog allowing the user to rearrange the specified items.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddExtraControls(self, win: 'Window') -> None:
        """ Customize the dialog by adding extra controls to it.
        """

    def Create(self, parent, message, title="", order=[], items=[], pos=DefaultPosition, name=RearrangeDialogNameStr) -> bool:
        """ Effectively creates the dialog for an object created using the default constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetList(self) -> 'RearrangeList':
        """ Return the list control used by the dialog.
        """

    def GetOrder(self) -> list[int]:
        """ Return the array describing the order of items after it was modified by the user.
        """



class Rect:
    """ Represents a rectangle with integer coordinates.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def CenterIn(self, r, dir=BOTH) -> 'Rect':
        """ Returns the rectangle having the same size as this one but centered relatively to the given rectangle r.
        """

    def CentreIn(self, r, dir=BOTH) -> 'Rect':
        """ Returns the rectangle having the same size as this one but centered relatively to the given rectangle r.
        """

    def Contains(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def Deflate(self, *args, **kw) -> 'Rect':
        """ Decrease the rectangle size.
        """

    def Get(self) -> tuple:
        """ Return the rectangleâs properties as a tuple.
        """

    def GetBottom(self) -> int:
        """ Gets the bottom point of the rectangle.
        """

    def GetBottomLeft(self) -> 'Point':
        """ Gets the position of the bottom left corner.
        """

    def GetBottomRight(self) -> 'Point':
        """ Gets the position of the bottom right corner.
        """

    def GetHeight(self) -> int:
        """ Gets the height member.
        """

    def GetIM(self) -> None:
        """ Returns an immutable representation of the wx.Rect object, based on namedtuple.
        """

    def GetLeft(self) -> int:
        """ Gets the left point of the rectangle (the same as GetX ).
        """

    def GetPosition(self) -> 'Point':
        """ Gets the position.
        """

    def GetRight(self) -> int:
        """ Gets the right point of the rectangle.
        """

    def GetSize(self) -> 'Size':
        """ Gets the size.
        """

    def GetTop(self) -> int:
        """ Gets the top point of the rectangle (the same as GetY ).
        """

    def GetTopLeft(self) -> 'Point':
        """ Gets the position of the top left corner of the rectangle, same as GetPosition .
        """

    def GetTopRight(self) -> 'Point':
        """ Gets the position of the top right corner.
        """

    def GetWidth(self) -> int:
        """ Gets the width member.
        """

    def GetX(self) -> int:
        """ Gets the x member.
        """

    def GetY(self) -> int:
        """ Gets the y member.
        """

    def Inflate(self, *args, **kw) -> 'Rect':
        """ Increases the size of the rectangle.
        """

    def Intersect(self, rect: 'Rect') -> 'Rect':
        """ Modifies this rectangle to contain the overlapping portion of this rectangle and the one passed in as parameter.
        """

    def Intersects(self, rect: 'Rect') -> bool:
        """ Returns True if this rectangle has a non-empty intersection with the rectangle rect  and False otherwise.
        """

    def IsEmpty(self) -> bool:
        """ Returns True if this rectangle has a width or height less than or equal to 0 and False otherwise.
        """

    def Offset(self, *args, **kw) -> None:
        """ Moves the rectangle by the specified offset.
        """

    def SetBottom(self, bottom: int) -> None:
        """ Set the bottom edge of the rectangle.
        """

    def SetBottomLeft(self, p: 'Point') -> None:
        """ Set the bottom-left point of the rectangle.
        """

    def SetBottomRight(self, p: 'Point') -> None:
        """ Set the bottom-right point of the rectangle.
        """

    def SetHeight(self, height: int) -> None:
        """ Sets the height.
        """

    def SetLeft(self, left: int) -> None:
        """ Set the left side of the rectangle.
        """

    def SetPosition(self, pos: 'Point') -> None:
        """ Sets the position.
        """

    def SetRight(self, right: int) -> None:
        """ Set the right side of the rectangle.
        """

    def SetSize(self, s: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the size.
        """

    def SetTop(self, top: int) -> None:
        """ Set the top edge of the rectangle.
        """

    def SetTopLeft(self, p: 'Point') -> None:
        """ Set the top-left point of the rectangle.
        """

    def SetTopRight(self, p: 'Point') -> None:
        """ Set the top-right point of the rectangle.
        """

    def SetWidth(self, width: int) -> None:
        """ Sets the width.
        """

    def SetX(self, x: int) -> None:
        """ Sets the x position.
        """

    def SetY(self, y: int) -> None:
        """ Sets the y position.
        """

    def Union(self, rect: 'Rect') -> 'Rect':
        """ Modifies the rectangle to contain the bounding box of this rectangle and the one passed in as parameter.
        """

    def __bool__(self) -> None:
        """ 
        """

    def __eq__(self, item: Any) -> bool:
        """ bool
        """

    def __getitem__(self, idx) -> None:
        """ 
        """

    def __len__(self) -> None:
        """ 
        """

    def __ne__(self, item: Any) -> bool:
        """ bool
        """

    def __nonzero__(self) -> None:
        """ 
        """

    def __reduce__(self) -> None:
        """ 
        """

    def __repr__(self) -> None:
        """ 
        """

    def __setitem__(self, idx, val) -> None:
        """ 
        """

    def __str__(self) -> None:
        """ 
        """

    def __imul__(self) -> None:
        """ Returns the intersection of two rectangles (which may be empty).
        """

    def __iadd__(self) -> None:
        """ Like Union , but doesnât treat empty rectangles specially.
        """

Rect: int
Rect: int
Rect: int


class Rect2D:
    """  Overloaded Implementations:
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def ConstrainTo(self, rect: Rect2DDouble) -> None:
        """ rect (Rect2DDouble) â
        """

    def Contains(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def CreateIntersection(self, otherRect: Rect2DDouble) -> Rect2DDouble:
        """ otherRect (Rect2DDouble) â
        """

    def CreateUnion(self, otherRect: Rect2DDouble) -> Rect2DDouble:
        """ otherRect (Rect2DDouble) â
        """

    def Get(self) -> Any:
        """ Get() . (x, y, width, height)
        """

    def GetBottom(self) -> 'Double':
        """ wx.Double
        """

    def GetCentre(self) -> Point2DDouble:
        """ Point2DDouble
        """

    def GetIM(self) -> None:
        """ Returns an immutable representation of the wx.Rect2D object, based on namedtuple.
        """

    def GetLeft(self) -> 'Double':
        """ wx.Double
        """

    def GetLeftBottom(self) -> Point2DDouble:
        """ Point2DDouble
        """

    def GetLeftTop(self) -> Point2DDouble:
        """ Point2DDouble
        """

    def GetOutCode(self, pt: Point2DDouble) -> 'OutCode':
        """ pt (Point2DDouble) â
        """

    def GetOutcode(self, pt: Point2DDouble) -> 'OutCode':
        """ pt (Point2DDouble) â
        """

    def GetPosition(self) -> Point2DDouble:
        """ Point2DDouble
        """

    def GetRight(self) -> 'Double':
        """ wx.Double
        """

    def GetRightBottom(self) -> Point2DDouble:
        """ Point2DDouble
        """

    def GetRightTop(self) -> Point2DDouble:
        """ Point2DDouble
        """

    def GetSize(self) -> 'Size':
        """ wx.Size
        """

    def GetTop(self) -> 'Double':
        """ wx.Double
        """

    def HaveEqualSize(self, rect: Rect2DDouble) -> bool:
        """ rect (Rect2DDouble) â
        """

    def Inset(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Interpolate(self, widthfactor, heightfactor) -> Point2DDouble:
        """ widthfactor (wx.int) â
        """

    def Intersect(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Intersects(self, rect: Rect2DDouble) -> bool:
        """ rect (Rect2DDouble) â
        """

    def IsEmpty(self) -> bool:
        """ bool
        """

    def MoveBottomTo(self, n: 'Double') -> None:
        """ n (wx.Double) â
        """

    def MoveCentreTo(self, pt: Point2DDouble) -> None:
        """ pt (Point2DDouble) â
        """

    def MoveLeftBottomTo(self, pt: Point2DDouble) -> None:
        """ pt (Point2DDouble) â
        """

    def MoveLeftTo(self, n: 'Double') -> None:
        """ n (wx.Double) â
        """

    def MoveLeftTopTo(self, pt: Point2DDouble) -> None:
        """ pt (Point2DDouble) â
        """

    def MoveRightBottomTo(self, pt: Point2DDouble) -> None:
        """ pt (Point2DDouble) â
        """

    def MoveRightTo(self, n: 'Double') -> None:
        """ n (wx.Double) â
        """

    def MoveRightTopTo(self, pt: Point2DDouble) -> None:
        """ pt (Point2DDouble) â
        """

    def MoveTopTo(self, n: 'Double') -> None:
        """ n (wx.Double) â
        """

    def Offset(self, pt: Point2DDouble) -> None:
        """ pt (Point2DDouble) â
        """

    def Scale(self: 'Double', *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetBottom(self, n: 'Double') -> None:
        """ n (wx.Double) â
        """

    def SetCentre(self, pt: Point2DDouble) -> None:
        """ pt (Point2DDouble) â
        """

    def SetLeft(self, n: 'Double') -> None:
        """ n (wx.Double) â
        """

    def SetLeftBottom(self, pt: Point2DDouble) -> None:
        """ pt (Point2DDouble) â
        """

    def SetLeftTop(self, pt: Point2DDouble) -> None:
        """ pt (Point2DDouble) â
        """

    def SetRight(self, n: 'Double') -> None:
        """ n (wx.Double) â
        """

    def SetRightBottom(self, pt: Point2DDouble) -> None:
        """ pt (Point2DDouble) â
        """

    def SetRightTop(self, pt: Point2DDouble) -> None:
        """ pt (Point2DDouble) â
        """

    def SetTop(self, n: 'Double') -> None:
        """ n (wx.Double) â
        """

    def Union(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def __bool__(self) -> None:
        """ 
        """

    def __getitem__(self, idx) -> None:
        """ 
        """

    def __len__(self) -> None:
        """ 
        """

    def __nonzero__(self) -> None:
        """ 
        """

    def __reduce__(self) -> None:
        """ 
        """

    def __repr__(self) -> None:
        """ 
        """

    def __setitem__(self, idx, val) -> None:
        """ 
        """

    def __str__(self) -> None:
        """ 
        """

    def __ne__(self, item: Any) -> bool:
        """ rect (Rect2DDouble) â
        """

    def __eq__(self, item: Any) -> bool:
        """ rect (Rect2DDouble) â
        """

Rect2D: int
Rect2D: int
Rect2D: int


class RefCounter:
    """ This class is used to manage reference-counting providing a simple
interface and a counter.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def DecRef(self) -> None:
        """ Decrements the reference count associated with this shared data and, if it reaches zero, destroys this instance of   wx.RefCounter  releasing its memory.
        """

    def GetRefCount(self) -> int:
        """ Returns the reference count associated with this shared data.
        """

    def IncRef(self) -> None:
        """ Increments the reference count associated with this shared data.
        """



class Region(GDIObject):
    """ A Region represents a simple or complex region on a device context
or window.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Clear(self) -> None:
        """ Clears the current region.
        """

    def Contains(self, *args, **kw) -> 'RegionContain':
        """ Overloaded Implementations:
        """

    def ConvertToBitmap(self) -> 'Bitmap':
        """ Convert the region to a black and white bitmap with the white pixels being inside the region.
        """

    def GetBox(self) -> 'Rect':
        """ Returns the outer bounds of the region.
        """

    def Intersect(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def IsEmpty(self) -> bool:
        """ Returns True if the region is empty, False otherwise.
        """

    def IsEqual(self, region: 'Region') -> bool:
        """ Returns True if the region is equal to, i.e. covers the same area as, another one.
        """

    def Offset(self, *args, **kw) -> None:
        """ Moves the region by the specified offsets in horizontal and vertical directions.
        """

    def Subtract(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def Union(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def Xor(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def __iter__(self) -> None:
        """ Returns a rectangle iterator conforming to the Python iterator
protocol.
        """



class RegionIterator(Object):
    """ This class is used to iterate through the rectangles in a region,
typically when examining the damaged regions of a window within an
OnPaint call.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetH(self) -> 'Coord':
        """ An alias for GetHeight .
        """

    def GetHeight(self) -> 'Coord':
        """ Returns the height value for the current region.
        """

    def GetRect(self) -> 'Rect':
        """ Returns the current rectangle.
        """

    def GetW(self) -> 'Coord':
        """ An alias for GetWidth .
        """

    def GetWidth(self) -> 'Coord':
        """ Returns the width value for the current region.
        """

    def GetX(self) -> 'Coord':
        """ Returns the x value for the current region.
        """

    def GetY(self) -> 'Coord':
        """ Returns the y value for the current region.
        """

    def HaveRects(self) -> bool:
        """ Returns True if there are still some rectangles; otherwise returns False.
        """

    def Next(self) -> None:
        """ Move the iterator to the next rectangle in the region.
        """

    def Reset(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def __bool__(self) -> int:
        """ Returns True while there are still rectangles available in the iteration.
        """

    def __nonzero__(self) -> int:
        """ Returns True while there are still rectangles available in the iteration.
        """



class RendererVersion:
    """ This simple struct represents the RendererNative interface version
and is only used as the return value of
RendererNative.GetVersion().
    """
    def __init__(self, version_, age_) -> None:
        """ version_ (int) â
        """

    @staticmethod
    def IsCompatible(ver: 'RendererVersion') -> bool:
        """ Checks if the main program is compatible with the renderer having the version ver, returns True if it is and False otherwise.
        """



class RichMessageDialog:
    """ Extension of MessageDialog with additional functionality.
    """
    def __init__(self, parent, message, caption=MessageBoxCaptionStr, style=OK|CENTRE) -> None:
        """ Constructor specifying the rich message dialog properties.
        """

    def GetCheckBoxText(self) -> str:
        """ Retrieves the label for the checkbox.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetDetailedText(self) -> str:
        """ Retrieves the detailed text.
        """

    def GetFooterIcon(self) -> int:
        """ Retrieves the footer icon.
        """

    def GetFooterText(self) -> str:
        """ Retrieves the footer text.
        """

    def IsCheckBoxChecked(self) -> bool:
        """ Retrieves the state of the checkbox.
        """

    def SetFooterIcon(self, icon: int) -> None:
        """ Specify the footer icon set together with the footer text.
        """

    def SetFooterText(self, footerText: str) -> None:
        """ Shows or hides a footer text that is used at the bottom of the dialog together with an optional icon.
        """

    def ShowCheckBox(self, checkBoxText, checked=False) -> None:
        """ Shows a checkbox with a given label or hides it.
        """

    def ShowDetailedText(self, detailedText: str) -> None:
        """ Shows or hides a detailed text and an expander that is used to show or hide the detailed text.
        """

    def ShowModal(self) -> int:
        """ Shows the dialog, returning one of wx.ID_OK, wx.ID_CANCEL, wx.ID_YES, wx.ID_NO.
        """

ID_OK: int
ID_CANCEL: int
ID_YES: int
ID_NO: int
ID_OK: int
ID_CANCEL: int
ID_YES: int
ID_NO: int


class RotateGestureEvent(GestureEvent):
    """ This event is generated when two fingers move in opposite directions
on the surface.
    """
    def __init__(self, windid: int=0) -> None:
        """ Constructor.
        """

    def GetRotationAngle(self) -> float:
        """ Returns the total angle of rotation in radians in clockwise direction since the gesture was first started i.e.
        """

    def SetRotationAngle(self, rotationAngle: float) -> None:
        """ Sets the total angle of rotation in radians in clockwise direction since the gesture was first started i.e.
        """

EVT_GESTURE_ROTATE: int  #  Process a  wxEVT_GESTURE_ROTATE . ^^


class ScreenDC(DC):
    """ A ScreenDC can be used to paint on the screen.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    @staticmethod
    def EndDrawingOnTop() -> bool:
        """ Use this in conjunction with StartDrawingOnTop .
        """

    @staticmethod
    def StartDrawingOnTop(*args, **kw) -> bool:
        """ Overloaded Implementations:
        """



class ScrollBar(Control):
    """ A ScrollBar is a control that represents a horizontal or vertical
scrollbar.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=SB_HORIZONTAL, validator=DefaultValidator, name=ScrollBarNameStr) -> bool:
        """ Scrollbar creation function called by the scrollbar constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetPageSize(self) -> int:
        """ Returns the page size of the scrollbar.
        """

    def GetRange(self) -> int:
        """ Returns the length of the scrollbar.
        """

    def GetThumbPosition(self) -> int:
        """ Returns the current position of the scrollbar thumb.
        """

    def GetThumbSize(self) -> int:
        """ Returns the thumb or âviewâ size.
        """

    def IsVertical(self) -> bool:
        """ Returns True for scrollbars that have the vertical style set.
        """

    def SetScrollbar(self, position, thumbSize, range, pageSize, refresh=True) -> None:
        """ Sets the scrollbar properties.
        """

    def SetThumbPosition(self, viewStart: int) -> None:
        """ Sets the position of the scrollbar.
        """

SB_HORIZONTAL: int  #  Specifies a horizontal scrollbar.
SB_VERTICAL: int  #  Specifies a vertical scrollbar. ^^
EVT_SCROLL: int  #  Process all scroll events.
EVT_SCROLL_TOP: int  #  Process  wxEVT_SCROLL_TOP   scroll to top or leftmost (minimum) position events.
EVT_SCROLL_BOTTOM: int  #  Process  wxEVT_SCROLL_BOTTOM   scroll to bottom or rightmost (maximum) position events.
EVT_SCROLL_LINEUP: int  #  Process  wxEVT_SCROLL_LINEUP   line up or left events.
EVT_SCROLL_LINEDOWN: int  #  Process  wxEVT_SCROLL_LINEDOWN   line down or right events.
EVT_SCROLL_PAGEUP: int  #  Process  wxEVT_SCROLL_PAGEUP   page up or left events.
EVT_SCROLL_PAGEDOWN: int  #  Process  wxEVT_SCROLL_PAGEDOWN   page down or right events.
EVT_SCROLL_THUMBTRACK: int  #  Process  wxEVT_SCROLL_THUMBTRACK   thumbtrack events (frequent events sent as the user drags the thumbtrack).
EVT_SCROLL_THUMBRELEASE: int  #  Process  wxEVT_SCROLL_THUMBRELEASE   thumb release events.
EVT_SCROLL_CHANGED: int  #  Process  wxEVT_SCROLL_CHANGED   end of scrolling events (MSW only).
EVT_COMMAND_SCROLL: int  #  Process all scroll events.
EVT_COMMAND_SCROLL_TOP: int  #  Process  wxEVT_SCROLL_TOP   scroll to top or leftmost (minimum) position events.
EVT_COMMAND_SCROLL_BOTTOM: int  #  Process  wxEVT_SCROLL_BOTTOM   scroll to bottom or rightmost (maximum) position events.
EVT_COMMAND_SCROLL_LINEUP: int  #  Process  wxEVT_SCROLL_LINEUP   line up or left events.
EVT_COMMAND_SCROLL_LINEDOWN: int  #  Process  wxEVT_SCROLL_LINEDOWN   line down or right events.
EVT_COMMAND_SCROLL_PAGEUP: int  #  Process  wxEVT_SCROLL_PAGEUP   page up or left events.
EVT_COMMAND_SCROLL_PAGEDOWN: int  #  Process  wxEVT_SCROLL_PAGEDOWN   page down or right events.
EVT_COMMAND_SCROLL_THUMBTRACK: int  #  Process  wxEVT_SCROLL_THUMBTRACK   thumbtrack events (frequent events sent as the user drags the thumbtrack).
EVT_COMMAND_SCROLL_THUMBRELEASE: int  #  Process  wxEVT_SCROLL_THUMBRELEASE   thumb release events.
EVT_COMMAND_SCROLL_CHANGED: int  #  Process  wxEVT_SCROLL_CHANGED   end of scrolling events (MSW only). ^^
SB_HORIZONTAL: int
SB_VERTICAL: int
ID_ANY: int


class Scrolled:
    """ The Scrolled class manages scrolling for its client area,
transforming the coordinates according to the scrollbar positions, and
setting the scroll positions, thumb sizes and ranges according to the
area in view.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AdjustScrollbars(self) -> None:
        """ 
        """

    def CalcScrolledPosition(self, *args, **kw) -> 'Point':
        """ Overloaded Implementations:
        """

    def CalcUnscrolledPosition(self, *args, **kw) -> 'Point':
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=-1, pos=DefaultPosition, size=DefaultSize, style=HSCROLL|VSCROLL, name="scrolledWindow") -> bool:
        """ Creates the window for two-step construction.
        """

    def DisableKeyboardScrolling(self) -> None:
        """ Disable use of keyboard keys for scrolling.
        """

    def DoPrepareDC(self, dc: 'DC') -> None:
        """ Call this function to prepare the device context for drawing a scrolled image.
        """

    def EnableScrolling(self, xScrolling, yScrolling) -> None:
        """ Enable or disable use of wx.Window.ScrollWindow   for scrolling.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetScaleX(self) -> float:
        """ float
        """

    def GetScaleY(self) -> float:
        """ float
        """

    def GetScrollLines(self, orient: int) -> int:
        """ orient (int) â
        """

    def GetScrollPageSize(self, orient: int) -> int:
        """ orient (int) â
        """

    def GetScrollPixelsPerUnit(self) -> tuple:
        """ Get the number of pixels per scroll unit (line), in each direction, as set by SetScrollbars .
        """

    def GetSizeAvailableForScrollTarget(self, size: Union[tuple[int, int], 'Size']) -> 'Size':
        """ Function which must be overridden to implement the size available for the scroll target for the given size of the main window.
        """

    def GetTargetRect(self) -> 'Rect':
        """ wx.Rect
        """

    def GetTargetWindow(self) -> 'Window':
        """ wx.Window
        """

    def GetViewStart(self) -> tuple:
        """ Get the position at which the visible portion of the window starts.
        """

    def IsAutoScrolling(self) -> bool:
        """ Are we generating the autoscroll events?
        """

    def IsRetained(self) -> bool:
        """ Motif only: True if the window has a backing bitmap.
        """

    def OnDraw(self, dc: 'DC') -> None:
        """ Called by the default paint event handler to allow the application to define painting behaviour without having to worry about calling DoPrepareDC .
        """

    def PrepareDC(self, dc: 'DC') -> None:
        """ This function is for backwards compatibility only and simply calls DoPrepareDC   now.
        """

    def Scroll(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SendAutoScrollEvents(self, event: 'ScrollWinEvent') -> bool:
        """ This method can be overridden in a derived class to forbid sending the auto scroll events - note that unlike StopAutoScrolling   it doesnât stop the timer, so it will be called repeatedly and will typically return different values depending on the current mouse position.
        """

    def SetScale(self, xs, ys) -> None:
        """ xs (float) â
        """

    def SetScrollPageSize(self, orient, pageSize) -> None:
        """ orient (int) â
        """

    def SetScrollRate(self, xstep, ystep) -> None:
        """ Set the horizontal and vertical scrolling increment only.
        """

    def SetScrollbars(self, pixelsPerUnitX, pixelsPerUnitY, noUnitsX, noUnitsY, xPos=0, yPos=0, noRefresh=False) -> None:
        """ Sets up vertical and/or horizontal scrollbars.
        """

    def SetTargetRect(self, rect: 'Rect') -> None:
        """ rect (wx.Rect) â
        """

    def SetTargetWindow(self, window: 'Window') -> None:
        """ Call this function to tell   wx.Scrolled  to perform the actual scrolling on a different window (and not on itself).
        """

    def ShouldScrollToChildOnFocus(self, child: 'Window') -> bool:
        """ This method can be overridden in a derived class to prevent scrolling the child window into view automatically when it gets focus.
        """

    def ShowScrollbars(self, horz, vert) -> None:
        """ Set the scrollbar visibility.
        """

    def StopAutoScrolling(self) -> None:
        """ Stop generating the scroll events when mouse is held outside the window.
        """

HSCROLL: int  #  If this style is specified and VSCROLL  isnât, the window will be scrollable only in horizontal direction (by default, i.e. if neither this style nor VSCROLL  is specified, it scrolls in both directions).
VSCROLL: int  #  If this style is specified and HSCROLL  isnât, the window will be scrollable only in vertical direction (by default, i.e. if neither this style nor HSCROLL  is specified, it scrolls in both directions).
ALWAYS_SHOW_SB: int  #  Since wxWidgets 2.9.5, specifying this style makes the window always show its scrollbars, even if they are not used. See ShowScrollbars.
RETAINED: int  #  Uses a backing pixmap to speed refreshes. Motif only. ^^
EVT_SCROLLWIN: int  #  Process all scroll events.
EVT_SCROLLWIN_TOP: int  #  Process  wxEVT_SCROLLWIN_TOP   scroll-to-top events.
EVT_SCROLLWIN_BOTTOM: int  #  Process  wxEVT_SCROLLWIN_BOTTOM   scroll-to-bottom events.
EVT_SCROLLWIN_LINEUP: int  #  Process  wxEVT_SCROLLWIN_LINEUP   line up events.
EVT_SCROLLWIN_LINEDOWN: int  #  Process  wxEVT_SCROLLWIN_LINEDOWN   line down events.
EVT_SCROLLWIN_PAGEUP: int  #  Process  wxEVT_SCROLLWIN_PAGEUP   page up events.
EVT_SCROLLWIN_PAGEDOWN: int  #  Process  wxEVT_SCROLLWIN_PAGEDOWN   page down events.
EVT_SCROLLWIN_THUMBTRACK: int  #  Process  wxEVT_SCROLLWIN_THUMBTRACK   thumbtrack events (frequent events sent as the user drags the thumbtrack).
EVT_SCROLLWIN_THUMBRELEASE: int  #  Process  wxEVT_SCROLLWIN_THUMBRELEASE   thumb release events. ^^
HSCROLL: int
VSCROLL: int
ALWAYS_SHOW_SB: int
RETAINED: int
SHOW_SB_ALWAYS: int
SHOW_SB_NEVER: int
SHOW_SB_DEFAULT: int


class ScrolledCanvas(Window, Scrolled):
    """ The ScrolledCanvas      class is a combination of the Window      and
Scrolled      classes, and manages scrolling for its client area,
transforming the coordinates according to the scrollbar positions,
and setting the scroll positions, thumb sizes and ranges according to
the area in view.
    """


class ScrolledWindow:
    """ Scrolled window derived from Panel.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def SetFocusIgnoringChildren(self) -> None:
        """ In contrast to SetFocus() this will set the focus to the panel even if
there are child windows in the panel. This is only rarely needed.
        """



class ScrollEvent(CommandEvent):
    """ A scroll event holds information about events sent from stand-alone
scrollbars (see ScrollBar) and sliders (see Slider).
    """
    def __init__(self, commandType=wxEVT_NULL, id=0, pos=0, orientation=0) -> None:
        """ Constructor.
        """

    def GetOrientation(self) -> int:
        """ Returns wx.HORIZONTAL or wx.VERTICAL, depending on the orientation of the scrollbar.
        """

    def GetPosition(self) -> int:
        """ Returns the position of the scrollbar.
        """

    def SetOrientation(self, orient: int) -> None:
        """ orient (int) â
        """

    def SetPosition(self, pos: int) -> None:
        """ pos (int) â
        """

EVT_SCROLL: int  #  Process all scroll events.
EVT_SCROLL_TOP: int  #  Process  wxEVT_SCROLL_TOP   scroll-to-top events (minimum position).
EVT_SCROLL_BOTTOM: int  #  Process  wxEVT_SCROLL_BOTTOM   scroll-to-bottom events (maximum position).
EVT_SCROLL_LINEUP: int  #  Process  wxEVT_SCROLL_LINEUP   line up events.
EVT_SCROLL_LINEDOWN: int  #  Process  wxEVT_SCROLL_LINEDOWN   line down events.
EVT_SCROLL_PAGEUP: int  #  Process  wxEVT_SCROLL_PAGEUP   page up events.
EVT_SCROLL_PAGEDOWN: int  #  Process  wxEVT_SCROLL_PAGEDOWN   page down events.
EVT_SCROLL_THUMBTRACK: int  #  Process  wxEVT_SCROLL_THUMBTRACK   thumbtrack events (frequent events sent as the user drags the thumbtrack).
EVT_SCROLL_THUMBRELEASE: int  #  Process  wxEVT_SCROLL_THUMBRELEASE   thumb release events.
EVT_SCROLL_CHANGED: int  #  Process  wxEVT_SCROLL_CHANGED   end of scrolling events (MSW only).
EVT_COMMAND_SCROLL: int  #  Process all scroll events.
EVT_COMMAND_SCROLL_TOP: int  #  Process  wxEVT_SCROLL_TOP   scroll-to-top events (minimum position).
EVT_COMMAND_SCROLL_BOTTOM: int  #  Process  wxEVT_SCROLL_BOTTOM   scroll-to-bottom events (maximum position).
EVT_COMMAND_SCROLL_LINEUP: int  #  Process  wxEVT_SCROLL_LINEUP   line up events.
EVT_COMMAND_SCROLL_LINEDOWN: int  #  Process  wxEVT_SCROLL_LINEDOWN   line down events.
EVT_COMMAND_SCROLL_PAGEUP: int  #  Process  wxEVT_SCROLL_PAGEUP   page up events.
EVT_COMMAND_SCROLL_PAGEDOWN: int  #  Process  wxEVT_SCROLL_PAGEDOWN   page down events.
EVT_COMMAND_SCROLL_THUMBTRACK: int  #  Process  wxEVT_SCROLL_THUMBTRACK   thumbtrack events (frequent events sent as the user drags the thumbtrack).
EVT_COMMAND_SCROLL_THUMBRELEASE: int  #  Process  wxEVT_SCROLL_THUMBRELEASE   thumb release events.
EVT_COMMAND_SCROLL_CHANGED: int  #  Process  wxEVT_SCROLL_CHANGED   end of scrolling events (MSW only). ^^
HORIZONTAL: int
VERTICAL: int
HORIZONTAL: int
VERTICAL: int


class Slider(Control):
    """ A slider is a control with a handle which can be pulled back and forth
to change the value.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def ClearSel(self) -> None:
        """ Clears the selection, for a slider with the wx.SL_SELRANGE  style.
        """

    def ClearTicks(self) -> None:
        """ Clears the ticks.
        """

    def Create(self, parent, id=ID_ANY, value=0, minValue=0, maxValue=100, point=DefaultPosition, size=DefaultSize, style=SL_HORIZONTAL, validator=DefaultValidator, name=SliderNameStr) -> bool:
        """ Used for two-step slider construction.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetLineSize(self) -> int:
        """ Returns the line size.
        """

    def GetMax(self) -> int:
        """ Gets the maximum slider value.
        """

    def GetMin(self) -> int:
        """ Gets the minimum slider value.
        """

    def GetPageSize(self) -> int:
        """ Returns the page size.
        """

    def GetRange(self) -> None:
        """ 
        """

    def GetSelEnd(self) -> int:
        """ Returns the selection end point.
        """

    def GetSelStart(self) -> int:
        """ Returns the selection start point.
        """

    def GetThumbLength(self) -> int:
        """ Returns the thumb length.
        """

    def GetTickFreq(self) -> int:
        """ Returns the tick frequency.
        """

    def GetValue(self) -> int:
        """ Gets the current slider value.
        """

    def SetLineSize(self, lineSize: int) -> None:
        """ Sets the line size for the slider.
        """

    def SetMax(self, maxValue: int) -> None:
        """ Sets the maximum slider value.
        """

    def SetMin(self, minValue: int) -> None:
        """ Sets the minimum slider value.
        """

    def SetPageSize(self, pageSize: int) -> None:
        """ Sets the page size for the slider.
        """

    def SetRange(self, minValue, maxValue) -> None:
        """ Sets the minimum and maximum slider values.
        """

    def SetSelection(self, startPos, endPos) -> None:
        """ Sets the selection.
        """

    def SetThumbLength(self, len: int) -> None:
        """ Sets the slider thumb length.
        """

    def SetTick(self, tickPos: int) -> None:
        """ Sets a tick position.
        """

    def SetTickFreq(self, freq: int) -> None:
        """ Sets the tick mark frequency and position.
        """

    def SetValue(self, value: int) -> None:
        """ Sets the slider position.
        """

SL_HORIZONTAL: int  #  Displays the slider horizontally (this is the default).
SL_VERTICAL: int  #  Displays the slider vertically.
SL_AUTOTICKS: int  #  Displays tick marks (Windows, GTK+ 2.16 and later).
SL_MIN_MAX_LABELS: int  #  Displays minimum, maximum labels (new since wxWidgets 2.9.1).
SL_VALUE_LABEL: int  #  Displays value label (new since wxWidgets 2.9.1).
SL_LABELS: int  #  Displays minimum, maximum and value labels (same as wx.SL_VALUE_LABEL and wx.SL_MIN_MAX_LABELS together).
SL_LEFT: int  #  Displays ticks on the left and forces the slider to be vertical (Windows and GTK+ 3 only).
SL_RIGHT: int  #  Displays ticks on the right and forces the slider to be vertical.
SL_TOP: int  #  Displays ticks on the top (Windows and GTK+ 3 only).
SL_BOTTOM: int  #  Displays ticks on the bottom (this is the default).
SL_BOTH: int  #  Displays ticks on both sides of the slider. Windows only.
SL_SELRANGE: int  #  Displays a highlighted selection range. Windows only.
SL_INVERSE: int  #  Inverses the minimum and maximum endpoints on the slider. Not compatible with wx.SL_SELRANGE. ^^
EVT_SCROLL: int  #  Process all scroll events.
EVT_SCROLL_TOP: int  #  Process  wxEVT_SCROLL_TOP   scroll-to-top events (minimum position).
EVT_SCROLL_BOTTOM: int  #  Process  wxEVT_SCROLL_BOTTOM   scroll-to-bottom events (maximum position).
EVT_SCROLL_LINEUP: int  #  Process  wxEVT_SCROLL_LINEUP   line up events.
EVT_SCROLL_LINEDOWN: int  #  Process  wxEVT_SCROLL_LINEDOWN   line down events.
EVT_SCROLL_PAGEUP: int  #  Process  wxEVT_SCROLL_PAGEUP   page up events.
EVT_SCROLL_PAGEDOWN: int  #  Process  wxEVT_SCROLL_PAGEDOWN   page down events.
EVT_SCROLL_THUMBTRACK: int  #  Process  wxEVT_SCROLL_THUMBTRACK   thumbtrack events (frequent events sent as the user drags the thumbtrack).
EVT_SCROLL_THUMBRELEASE: int  #  Process  wxEVT_SCROLL_THUMBRELEASE   thumb release events.
EVT_SCROLL_CHANGED: int  #  Process  wxEVT_SCROLL_CHANGED   end of scrolling events (MSW only).
EVT_COMMAND_SCROLL: int  #  Process all scroll events.
EVT_COMMAND_SCROLL_TOP: int  #  Process  wxEVT_SCROLL_TOP   scroll-to-top events (minimum position).
EVT_COMMAND_SCROLL_BOTTOM: int  #  Process  wxEVT_SCROLL_BOTTOM   scroll-to-bottom events (maximum position).
EVT_COMMAND_SCROLL_LINEUP: int  #  Process  wxEVT_SCROLL_LINEUP   line up events.
EVT_COMMAND_SCROLL_LINEDOWN: int  #  Process  wxEVT_SCROLL_LINEDOWN   line down events.
EVT_COMMAND_SCROLL_PAGEUP: int  #  Process  wxEVT_SCROLL_PAGEUP   page up events.
EVT_COMMAND_SCROLL_PAGEDOWN: int  #  Process  wxEVT_SCROLL_PAGEDOWN   page down events.
EVT_COMMAND_SCROLL_THUMBTRACK: int  #  Process  wxEVT_SCROLL_THUMBTRACK   thumbtrack events (frequent events sent as the user drags the thumbtrack).
EVT_COMMAND_SCROLL_THUMBRELEASE: int  #  Process  wxEVT_SCROLL_THUMBRELEASE   thumb release events.
EVT_COMMAND_SCROLL_CHANGED: int  #  Process  wxEVT_SCROLL_CHANGED   end of scrolling events (MSW only).
EVT_SLIDER: int  #  Process  wxEVT_SLIDER   which is generated after any change of    wx.Slider  position in addition to one of the events above. Notice that the handler of this event receives a   wx.CommandEvent  as argument and not   wx.ScrollEvent, as all the other handlers. ^^
SL_HORIZONTAL: int
SL_VERTICAL: int
SL_AUTOTICKS: int
SL_MIN_MAX_LABELS: int
SL_VALUE_LABEL: int
SL_LABELS: int
SL_VALUE_LABEL: int
SL_MIN_MAX_LABELS: int
SL_LEFT: int
SL_RIGHT: int
SL_TOP: int
SL_BOTTOM: int
SL_BOTH: int
SL_SELRANGE: int
SL_INVERSE: int
SL_SELRANGE: int
SL_RIGHT: int
SL_SELRANGE: int
ID_ANY: int
SL_SELRANGE: int


class ScrollWinEvent(Event):
    """ A scroll event holds information about events sent from scrolling
windows.
    """
    def __init__(self, commandType=wxEVT_NULL, pos=0, orientation=0) -> None:
        """ Constructor.
        """

    def GetOrientation(self) -> int:
        """ Returns wx.HORIZONTAL or wx.VERTICAL, depending on the orientation of the scrollbar.
        """

    def GetPosition(self) -> int:
        """ Returns the position of the scrollbar for the thumb track and release events.
        """

    def SetOrientation(self, orient: int) -> None:
        """ orient (int) â
        """

    def SetPosition(self, pos: int) -> None:
        """ pos (int) â
        """

EVT_SCROLLWIN: int  #  Process all scroll events.
EVT_SCROLLWIN_TOP: int  #  Process  wxEVT_SCROLLWIN_TOP   scroll-to-top events.
EVT_SCROLLWIN_BOTTOM: int  #  Process  wxEVT_SCROLLWIN_BOTTOM   scroll-to-bottom events.
EVT_SCROLLWIN_LINEUP: int  #  Process  wxEVT_SCROLLWIN_LINEUP   line up events.
EVT_SCROLLWIN_LINEDOWN: int  #  Process  wxEVT_SCROLLWIN_LINEDOWN   line down events.
EVT_SCROLLWIN_PAGEUP: int  #  Process  wxEVT_SCROLLWIN_PAGEUP   page up events.
EVT_SCROLLWIN_PAGEDOWN: int  #  Process  wxEVT_SCROLLWIN_PAGEDOWN   page down events.
EVT_SCROLLWIN_THUMBTRACK: int  #  Process  wxEVT_SCROLLWIN_THUMBTRACK   thumbtrack events (frequent events sent as the user drags the thumbtrack).
EVT_SCROLLWIN_THUMBRELEASE: int  #  Process  wxEVT_SCROLLWIN_THUMBRELEASE   thumb release events. ^^
HORIZONTAL: int
VERTICAL: int
HORIZONTAL: int
VERTICAL: int
HORIZONTAL: int
VERTICAL: int


class SearchCtrl(TextCtrl):
    """ A search control is a composite control with a search button, a text
control, and a cancel button.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AppendText(self, text: str) -> None:
        """ Appends the text to the end of the text control.
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

    def CanCopy(self) -> bool:
        """ Returns True if the selection can be copied to the clipboard.
        """

    def CanCut(self) -> bool:
        """ Returns True if the selection can be cut to the clipboard.
        """

    def CanPaste(self) -> bool:
        """ Returns True if the contents of the clipboard can be pasted into the text control.
        """

    def CanRedo(self) -> bool:
        """ Returns True if there is a redo facility available and the last operation can be redone.
        """

    def CanUndo(self) -> bool:
        """ Returns True if there is an undo facility available and the last operation can be undone.
        """

    def ChangeValue(self, value: str) -> None:
        """ Sets the new text control value.
        """

    def Clear(self) -> None:
        """ Clears the text in the control.
        """

    def Copy(self) -> None:
        """ Copies the selected text to the clipboard.
        """

    def Create(self, parent, id=ID_ANY, value="", pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=SearchCtrlNameStr) -> bool:
        """ parent (wx.Window) â
        """

    def Cut(self) -> None:
        """ Copies the selected text to the clipboard and removes it from the control.
        """

    def ForceUpper(self) -> None:
        """ Convert all text entered into the control to upper case.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetDescriptiveText(self) -> str:
        """ Return the text displayed when there is not yet any user input.
        """

    def GetHint(self) -> str:
        """ Returns the current hint string.
        """

    def GetInsertionPoint(self) -> int:
        """ Returns the insertion point, or cursor, position.
        """

    def GetLastPosition(self) -> 'TextPos':
        """ Returns the zero based index of the last position in the text control, which is equal to the number of characters in the control.
        """

    def GetMargins(self) -> 'Point':
        """ Returns the margins used by the control.
        """

    def GetMenu(self) -> 'Menu':
        """ Returns a pointer to the search controlâs menu object or None if there is no menu attached.
        """

    def GetRange(self, from_, to_) -> str:
        """ Returns the string containing the text starting in the positions from  and up to to  in the control.
        """

    def GetSelection(self) -> tuple:
        """ Gets the current selection span.
        """

    def GetStringSelection(self) -> str:
        """ Gets the text currently selected in the control.
        """

    def GetValue(self) -> str:
        """ Gets the contents of the control.
        """

    def IsCancelButtonVisible(self) -> bool:
        """ Returns the cancel buttonâs visibility state.
        """

    def IsEditable(self) -> bool:
        """ Returns True if the controls contents may be edited by user (note that it always can be changed by the program).
        """

    def IsEmpty(self) -> bool:
        """ Returns True if the control is currently empty.
        """

    def IsSearchButtonVisible(self) -> bool:
        """ Returns the search button visibility value.
        """

    def Paste(self) -> None:
        """ Pastes text from the clipboard to the text item.
        """

    def Redo(self) -> None:
        """ If there is a redo facility and the last operation can be redone, redoes the last operation.
        """

    def Remove(self, from_, to_) -> None:
        """ Removes the text starting at the first given position up to (but not including) the character at the last position.
        """

    def Replace(self, from_, to_, value) -> None:
        """ Replaces the text starting at the first position up to (but not including) the character at the last position with the given text.
        """

    def SelectAll(self) -> None:
        """ Selects all text in the control.
        """

    def SelectNone(self) -> None:
        """ Deselects selected text in the control.
        """

    def SetCancelBitmap(self, bmp) -> None:
        """ 
        """

    def SetDescriptiveText(self, text: str) -> None:
        """ Set the text to be displayed in the search control when the user has not yet typed anything in it.
        """

    def SetEditable(self, editable: bool) -> None:
        """ Makes the text item editable or read-only, overriding the wx.TE_READONLY  flag.
        """

    def SetHint(self, hint: str) -> bool:
        """ Sets a hint shown in an empty unfocused text control.
        """

    def SetInsertionPoint(self, pos: int) -> None:
        """ Sets the insertion point at the given position.
        """

    def SetInsertionPointEnd(self) -> None:
        """ Sets the insertion point at the end of the text control.
        """

    def SetMargins(self, *args, **kw) -> None:
        """ Attempts to set the control margins.
        """

    def SetMaxLength(self, len: int) -> None:
        """ This function sets the maximum number of characters the user can enter into the control.
        """

    def SetMenu(self, menu: 'Menu') -> None:
        """ Sets the search controlâs menu object.
        """

    def SetSearchBitmap(self, bmp) -> None:
        """ 
        """

    def SetSearchMenuBitmap(self, bmp) -> None:
        """ 
        """

    def SetSelection(self, from_, to_) -> None:
        """ Selects the text starting at the first position up to (but not including) the character at the last position.
        """

    def SetValue(self, value: str) -> None:
        """ Sets the new text control value.
        """

    def ShowCancelButton(self, show: bool) -> None:
        """ Shows or hides the cancel button.
        """

    def ShowSearchButton(self, show: bool) -> None:
        """ Sets the search button visibility value on the search control.
        """

    def Undo(self) -> None:
        """ If there is an undo facility and the last operation can be undone, undoes the last operation.
        """

    def WriteText(self, text: str) -> None:
        """ Writes the text into the text control at the current insertion position.
        """

TE_PROCESS_TAB: int  #  The control will receive  wxEVT_CHAR   events for TAB pressed - normally, TAB is used for passing to the next control in a dialog instead. For the control created with this style, you can still use Ctrl-Enter to pass to the next control from the keyboard.
TE_NOHIDESEL: int  #  By default, the Windows text control doesnât show the selection when it doesnât have focus - use this style to force it to always show it. It doesnât do anything under other platforms.
TE_LEFT: int  #  The text in the control will be left-justified (default).
TE_CENTRE: int  #  The text in the control will be centered (currently wxMSW and wxGTK2 only).
TE_RIGHT: int  #  The text in the control will be right-justified (currently wxMSW and wxGTK2 only).
TE_CAPITALIZE: int  #  On PocketPC and Smartphone, causes the first letter to be capitalized. ^^
EVT_SEARCH: int  #  Respond to a  wxEVT_SEARCH   event, generated when the search button is clicked. Note that this does not initiate a search on its own, you need to perform the appropriate action in your event handler. You may use: int  # 
EVT_SEARCH_CANCEL: int  #  Respond to a  wxEVT_SEARCH_CANCEL   event, generated when the cancel button is clicked. ^^
TE_PROCESS_TAB: int
TE_NOHIDESEL: int
TE_LEFT: int
TE_CENTRE: int
TE_RIGHT: int
TE_READONLY: int
TE_READONLY: int


class SetCursorEvent(Event):
    """ A SetCursorEvent is generated from Window when the mouse cursor is
about to be set as a result of mouse motion.
    """
    def __init__(self, x=0, y=0) -> None:
        """ Constructor, used by the library itself internally to initialize the event object.
        """

    def GetCursor(self) -> 'Cursor':
        """ Returns a reference to the cursor specified by this event.
        """

    def GetX(self) -> 'Coord':
        """ Returns the X coordinate of the mouse in client coordinates.
        """

    def GetY(self) -> 'Coord':
        """ Returns the Y coordinate of the mouse in client coordinates.
        """

    def HasCursor(self) -> bool:
        """ Returns True if the cursor specified by this event is a valid cursor.
        """

    def SetCursor(self, cursor: 'Cursor') -> None:
        """ Sets the cursor associated with this event.
        """

EVT_SET_CURSOR: int  #  Process a  wxEVT_SET_CURSOR   event. ^^


class SettableHeaderColumn(HeaderColumn):
    """ Adds methods to set the column attributes to HeaderColumn.
    """
    def ChangeFlag(self, flag, set) -> None:
        """ Set or clear the given flag.
        """

    def ClearFlag(self, flag: int) -> None:
        """ Clear the specified flag for the column.
        """

    def SetAlignment(self, align: int) -> None:
        """ Set the alignment of the column header.
        """

    def SetBitmap(self, bitmap: 'BitmapBundle') -> None:
        """ Set the bitmap to be displayed in the column header.
        """

    def SetFlag(self, flag: int) -> None:
        """ Set the specified flag for the column.
        """

    def SetFlags(self, flags: int) -> None:
        """ Set the column flags.
        """

    def SetHidden(self, hidden: bool) -> None:
        """ Hide or show the column.
        """

    def SetMinWidth(self, minWidth: int) -> None:
        """ Set the minimal column width.
        """

    def SetReorderable(self, reorderable: bool) -> None:
        """ Allow changing the column order by dragging it.
        """

    def SetResizeable(self, resizable: bool) -> None:
        """ Call this to enable or disable interactive resizing of the column by the user.
        """

    def SetSortOrder(self, ascending: bool) -> None:
        """ Sets this column as the sort key for the associated control.
        """

    def SetSortable(self, sortable: bool) -> None:
        """ Allow clicking the column to sort the control contents by the field in this column.
        """

    def SetTitle(self, title: str) -> None:
        """ Set the text to display in the column header.
        """

    def SetWidth(self, width: int) -> None:
        """ Set the column width.
        """

    def ToggleFlag(self, flag: int) -> None:
        """ Toggle the specified flag for the column.
        """

    def ToggleSortOrder(self) -> None:
        """ Inverses the sort order.
        """

    def UnsetAsSortKey(self) -> None:
        """ Donât use this column for sorting.
        """

ALIGN_NOT: int
ALIGN_CENTRE: int
ALIGN_LEFT: int
ALIGN_RIGHT: int
ALIGN_CENTRE_HORIZONTAL: int
ALIGN_CENTRE: int
COL_RESIZABLE: int
COL_SORTABLE: int
COL_REORDERABLE: int
COL_HIDDEN: int
COL_RESIZABLE: int
COL_WIDTH_DEFAULT: int
COL_WIDTH_AUTOSIZE: int


class SharedClientDataContainer:
    """ This class is a replacement for ClientDataContainer, and unlike
ClientDataContainer the SharedClientDataContainer client data is
copiable, so it can be copied when objects containing it are cloned.
    """
    def GetClientData(self) -> None:
        """ Get the untyped client data.
        """

    def GetClientObject(self) -> ClientData:
        """ Get a pointer to the client data object.
        """

    def SetClientData(self, data: Any) -> None:
        """ Set the untyped client data.
        """

    def SetClientObject(self, data: ClientData) -> None:
        """ Set the client data object.
        """



class ShowEvent(Event):
    """ An event being sent when the window is shown or hidden.
    """
    def __init__(self, winid=0, show=False) -> None:
        """ Constructor.
        """

    def IsShown(self) -> bool:
        """ Return True if the window has been shown, False if it has been hidden.
        """

    def SetShow(self, show: bool) -> None:
        """ Set whether the windows was shown or hidden.
        """

EVT_SHOW: int  #  Process a  wxEVT_SHOW   event. ^^


class Simplebook(BookCtrlBase):
    """ Simplebook is a control showing exactly one of its several pages.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name="") -> bool:
        """ Really create the window of an object created using default constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def SetEffect(self, effect: ShowEffect) -> None:
        """ Set the same effect to use for both showing and hiding the pages.
        """

    def SetEffectTimeout(self, timeout: Any) -> None:
        """ Set the same effect timeout to use for both showing and hiding the pages.
        """

    def SetEffects(self, showEffect, hideEffect) -> None:
        """ Set the effects to use for showing and hiding the pages.
        """

    def SetEffectsTimeouts(self, showTimeout, hideTimeout) -> None:
        """ Set the effect timeout to use for showing and hiding the pages.
        """

    def ShowNewPage(self, page: 'Window') -> bool:
        """ Add a new page and show it immediately.
        """



class SimpleHelpProvider(HelpProvider):
    """ SimpleHelpProvider is an implementation of HelpProvider which
supports only plain text help strings, and shows the string associated
with the control (if any) in a tooltip.
    """


class SingleChoiceDialog(Dialog):
    """ PySingleChoiceDialog(parent, message, caption, choices, style=CHOICEDLG_STYLE, pos=DefaultPosition)
    """
    def __init__(self, parent, message, caption, choices, style=CHOICEDLG_STYLE, pos=DefaultPosition) -> None:
        """ Constructor, taking an array of String       choices and optional client data.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetSelection(self) -> int:
        """ Returns the index of selected item.
        """

    def GetStringSelection(self) -> str:
        """ Returns the selected string.
        """

    def SetSelection(self, selection: int) -> None:
        """ Sets the index of the initially selected item.
        """

    def ShowModal(self) -> int:
        """ Shows the dialog, returning either wx.ID_OK or wx.ID_CANCEL.
        """

OK: int  #  Show an wx.OK button.
CANCEL: int  #  Show a Cancel button.
CENTRE: int  #  Centre the message. ^^
OK: int
OK: int
OK: int
CANCEL: int
CENTRE: int
ID_OK: int
ID_CANCEL: int
DEFAULT_DIALOG_STYLE: int
RESIZE_BORDER: int
OK: int
CANCEL: int
CENTRE: int
ID_OK: int
ID_CANCEL: int


class SingleInstanceChecker:
    """ SingleInstanceChecker class allows checking that only a single
instance of a program is running.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, name, path="") -> bool:
        """ Initialize the object if it had been created using the default constructor.
        """

    def CreateDefault(self) -> bool:
        """ Calls Create   with default name.
        """

    def IsAnotherRunning(self) -> bool:
        """ Returns True if another copy of this program is already running and False otherwise.
        """



class Size:
    """ A Size is a useful data structure for graphics operations.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def DecBy(self, *args, **kw) -> None:
        """ Decreases the size in both x and y directions.
        """

    def DecTo(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Decrements this object so that both of its dimensions are not greater than the corresponding dimensions of the size.
        """

    def DecToIfSpecified(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Decrements this object to be not bigger than the given size ignoring non-specified components.
        """

    def Get(self) -> tuple:
        """ Return the width and height properties as a tuple.
        """

    def GetHeight(self) -> int:
        """ Gets the height member.
        """

    def GetIM(self) -> None:
        """ Returns an immutable representation of the wx.Size object, based on namedtuple.
        """

    def GetWidth(self) -> int:
        """ Gets the width member.
        """

    def IncBy(self, *args, **kw) -> None:
        """ Increases the size in both x and y directions.
        """

    def IncTo(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Increments this object so that both of its dimensions are not less than the corresponding dimensions of the size.
        """

    def IsFullySpecified(self) -> bool:
        """ Returns True if neither of the size object components is equal to -1, which is used as default for the size values in wxWidgets (hence the predefined wx.DefaultSize       has both of its components equal to -1).
        """

    def Scale(self, xscale, yscale) -> 'Size':
        """ Scales the dimensions of this object by the given factors.
        """

    def Set(self, width, height) -> None:
        """ Sets the width and height members.
        """

    def SetDefaults(self, sizeDefault: Union[tuple[int, int], 'Size']) -> None:
        """ Combine this size object with another one replacing the default (i.e. equal to -1) components of this object with those of the other.
        """

    def SetHeight(self, height: int) -> None:
        """ Sets the height.
        """

    def SetWidth(self, width: int) -> None:
        """ Sets the width.
        """

    def __bool__(self) -> None:
        """ 
        """

    def __eq__(self, item: Any) -> bool:
        """ bool
        """

    def __getitem__(self, idx) -> None:
        """ 
        """

    def __len__(self) -> None:
        """ 
        """

    def __ne__(self, item: Any) -> bool:
        """ bool
        """

    def __nonzero__(self) -> None:
        """ 
        """

    def __reduce__(self) -> None:
        """ 
        """

    def __repr__(self) -> None:
        """ 
        """

    def __setitem__(self, idx, val) -> None:
        """ 
        """

    def __str__(self) -> None:
        """ 
        """

    def __imul__(self) -> None:
        """ factor (int) â
        """

    def __iadd__(self) -> None:
        """ sz (wx.Size) â
        """

    def __isub__(self) -> None:
        """ sz (wx.Size) â
        """

    def __idiv__(self) -> None:
        """ factor (int) â
        """

Size: int
Size: int
Size: int


class SizeEvent(Event):
    """ A size event holds information about size change events of Window.
    """
    def __init__(self, sz, id=0) -> None:
        """ Constructor.
        """

    def GetRect(self) -> 'Rect':
        """ wx.Rect
        """

    def GetSize(self) -> 'Size':
        """ Returns the entire size of the window generating the size change event.
        """

    def SetRect(self, rect: 'Rect') -> None:
        """ rect (wx.Rect) â
        """

    def SetSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ size (wx.Size) â
        """

EVT_SIZE: int  #  Process a  wxEVT_SIZE   event. ^^


class SizerFlags:
    """ Container for sizer items flags providing readable names for them.
    """
    def __init__(self, proportion: int=0) -> None:
        """ Creates the   wx.Sizer  with the proportion specified by proportion.
        """

    def Align(self, alignment: int) -> 'SizerFlags':
        """ Sets the alignment of this   wx.SizerFlags  to align.
        """

    def Border(self, *args, **kw) -> 'SizerFlags':
        """ Overloaded Implementations:
        """

    def Bottom(self) -> 'SizerFlags':
        """ Aligns the object to the bottom, similar for  Align(wxALIGN_BOTTOM) .
        """

    def Center(self) -> 'SizerFlags':
        """ Sets the object of the   wx.SizerFlags  to center itself in the area it is given.
        """

    def CenterHorizontal(self) -> 'SizerFlags':
        """ Same as CentreHorizontal .
        """

    def CenterVertical(self) -> 'SizerFlags':
        """ Same as CentreVertical .
        """

    def Centre(self) -> 'SizerFlags':
        """ wx.Center       for people with the other dialect of English.
        """

    def CentreHorizontal(self) -> 'SizerFlags':
        """ Center an item only in horizontal direction.
        """

    def CentreVertical(self) -> 'SizerFlags':
        """ Center an item only in vertical direction.
        """

    @staticmethod
    def DisableConsistencyChecks() -> None:
        """ Globally disable checks for sizer flag consistency in debug builds.
        """

    def DoubleBorder(self, direction: int=ALL) -> 'SizerFlags':
        """ Sets the border in the given direction  having twice the default border size.
        """

    def DoubleHorzBorder(self) -> 'SizerFlags':
        """ Sets the border in left and right directions having twice the default border size.
        """

    def Expand(self) -> 'SizerFlags':
        """ Sets the object of the   wx.SizerFlags  to expand to fill as much area as it can.
        """

    def FixedMinSize(self) -> 'SizerFlags':
        """ Set the  FIXED_MINSIZE   flag which indicates that the initial size of the window should be also set as its minimal size.
        """

    @staticmethod
    def GetDefaultBorder() -> int:
        """ Returns the border used by default in   wx.Border  method.
        """

    @staticmethod
    def GetDefaultBorderFractional() -> float:
        """ Returns the border used by default, with fractional precision.
        """

    def Left(self) -> 'SizerFlags':
        """ Aligns the object to the left, similar for  Align(wxALIGN_LEFT) .
        """

    def Proportion(self, proportion: int) -> 'SizerFlags':
        """ Sets the proportion of this   wx.SizerFlags  to proportion.
        """

    def ReserveSpaceEvenIfHidden(self) -> 'SizerFlags':
        """ Set the  RESERVE_SPACE_EVEN_IF_HIDDEN   flag.
        """

    def Right(self) -> 'SizerFlags':
        """ Aligns the object to the right, similar for  Align(wxALIGN_RIGHT) .
        """

    def Shaped(self) -> 'SizerFlags':
        """ Set the  _SHAPED   flag which indicates that the elements should always keep the fixed width to height ratio equal to its original value.
        """

    def Top(self) -> 'SizerFlags':
        """ Aligns the object to the top, similar for  Align(wxALIGN_TOP) .
        """

    def TripleBorder(self, direction: int=ALL) -> 'SizerFlags':
        """ Sets the border in the given direction  having thrice the default border size.
        """



class SizerItem(Object):
    """ The SizerItem class is used to track the position, size and other
attributes of each item managed by a Sizer.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AssignSizer(self, sizer: 'Sizer') -> None:
        """ Set the sizer tracked by this item.
        """

    def AssignSpacer(self, *args, **kw) -> None:
        """ Set the size of the spacer tracked by this item.
        """

    def AssignWindow(self, window: 'Window') -> None:
        """ Set the window to be tracked by this item.
        """

    def CalcMin(self) -> 'Size':
        """ Calculates the minimum desired size for the item, including any space needed by borders.
        """

    def DeleteWindows(self) -> None:
        """ Destroy the window or the windows in a subsizer, depending on the type of item.
        """

    def DetachSizer(self) -> None:
        """ Enable deleting the SizerItem without destroying the contained sizer.
        """

    def GetBorder(self) -> int:
        """ Return the border attribute.
        """

    def GetFlag(self) -> int:
        """ Return the flags attribute.
        """

    def GetId(self) -> int:
        """ Return the numeric id of   wx.SizerItem, or  ID_NONE   if the id has not been set.
        """

    def GetMinSize(self) -> 'Size':
        """ Get the minimum size needed for the item.
        """

    def GetPosition(self) -> 'Point':
        """ What is the current position of the item, as set in the last Layout.
        """

    def GetProportion(self) -> int:
        """ Get the proportion item attribute.
        """

    def GetRatio(self) -> float:
        """ Get the ratio item attribute.
        """

    def GetRect(self) -> 'Rect':
        """ Get the rectangle of the item on the parent window, excluding borders.
        """

    def GetSize(self) -> 'Size':
        """ Get the current size of the item, as set in the last Layout.
        """

    def GetSizer(self) -> 'Sizer':
        """ If this item is tracking a sizer, return it.
        """

    def GetSpacer(self) -> 'Size':
        """ If this item is tracking a spacer, return its size.
        """

    def GetUserData(self) -> PyUserData:
        """ Get the userData item attribute.
        """

    def GetWindow(self) -> 'Window':
        """ If this item is tracking a window then return it.
        """

    def IsShown(self) -> bool:
        """ Returns True if this item is a window or a spacer and it is shown or if this item is a sizer and not all of its elements are hidden.
        """

    def IsSizer(self) -> bool:
        """ Is this item a sizer?
        """

    def IsSpacer(self) -> bool:
        """ Is this item a spacer?
        """

    def IsWindow(self) -> bool:
        """ Is this item a window?
        """

    def SetBorder(self, border: int) -> None:
        """ Set the border item attribute.
        """

    def SetDimension(self, pos, size) -> None:
        """ Set the position and size of the space allocated to the sizer, and adjust the position and size of the item to be within that space taking alignment and borders into account.
        """

    def SetFlag(self, flag: int) -> None:
        """ Set the flag item attribute.
        """

    def SetId(self, id: int) -> None:
        """ Sets the numeric id of the   wx.SizerItem  to id.
        """

    def SetInitSize(self, x, y) -> None:
        """ Sets the minimum size to be allocated for this item.
        """

    def SetMinSize(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetProportion(self, proportion: int) -> None:
        """ Set the proportion item attribute.
        """

    def SetRatio(self, *args, **kw) -> None:
        """ Set the ratio item attribute.
        """

    def SetUserData(self, userData: PyUserData) -> None:
        """ userData (PyUserData) â
        """

    def Show(self, show: bool) -> None:
        """ Set the show item attribute, which sizers use to determine if the item is to be made part of the layout or not.
        """



class SpinButton(Control):
    """ A SpinButton has two small up and down (or left and right) arrow
buttons.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=-1, pos=DefaultPosition, size=DefaultSize, style=SP_VERTICAL, name="wxSpinButton") -> bool:
        """ Scrollbar creation function called by the spin button constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetIncrement(self) -> int:
        """ Get the value for increment for a spin control.
        """

    def GetMax(self) -> int:
        """ Returns the maximum permissible value.
        """

    def GetMin(self) -> int:
        """ Returns the minimum permissible value.
        """

    def GetRange(self) -> None:
        """ 
        """

    def GetValue(self) -> int:
        """ Returns the current spin button value.
        """

    def SetIncrement(self, value: int) -> None:
        """ Sets the increment for the control.
        """

    def SetMax(self, maxVal) -> None:
        """ 
        """

    def SetMin(self, minVal) -> None:
        """ 
        """

    def SetRange(self, min, max) -> None:
        """ Sets the range of the spin button.
        """

    def SetValue(self, value: int) -> None:
        """ Sets the value of the spin button.
        """

SP_HORIZONTAL: int  #  Specifies a horizontal spin button (note that this style is not supported in wxGTK).
SP_VERTICAL: int  #  Specifies a vertical spin button.
SP_ARROW_KEYS: int  #  The user can use arrow keys to change the value.
SP_WRAP: int  #  The value wraps at the minimum and maximum. ^^
EVT_SPIN: int  #  Generated whenever pressing an arrow changed the spin button value.
EVT_SPIN_UP: int  #  Generated whenever pressing left/up arrow changed the spin button value.
EVT_SPIN_DOWN: int  #  Generated whenever pressing right/down arrow changed the spin button value. ^^
SP_HORIZONTAL: int
SP_VERTICAL: int
SP_ARROW_KEYS: int
SP_WRAP: int
UP: int
DOWN: int
ID_ANY: int


class SpinCtrl(Control):
    """ SpinCtrl combines TextCtrl and SpinButton in one control.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, value="", pos=DefaultPosition, size=DefaultSize, style=SP_ARROW_KEYS, min=0, max=100, initial=0, name="wxSpinCtrl") -> bool:
        """ Creation function called by the spin control constructor.
        """

    def GetBase(self) -> int:
        """ Returns the numerical base being currently used, 10 by default.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetIncrement(self) -> int:
        """ Get the value for increment for a spin control.
        """

    def GetMax(self) -> int:
        """ Gets maximal allowable value.
        """

    def GetMin(self) -> int:
        """ Gets minimal allowable value.
        """

    def GetRange(self) -> None:
        """ 
        """

    def GetTextValue(self) -> str:
        """ Returns the text in the text entry part of the control.
        """

    def GetValue(self) -> int:
        """ Gets the value of the spin control.
        """

    def SetBase(self, base: int) -> bool:
        """ Sets the base to use for the numbers in this control.
        """

    def SetIncrement(self, value: int) -> None:
        """ Sets the increment for the control.
        """

    def SetMax(self, maxVal) -> None:
        """ 
        """

    def SetMin(self, minVal) -> None:
        """ 
        """

    def SetRange(self, minVal, maxVal) -> None:
        """ Sets range of allowable values.
        """

    def SetSelection(self, from_, to_) -> None:
        """ Select the text in the text part of the control between positions from  (inclusive) and to  (exclusive).
        """

    def SetValue(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

SP_ARROW_KEYS: int  #  The user can use arrow keys to change the value.
SP_WRAP: int  #  The value wraps at the minimum and maximum.
TE_PROCESS_ENTER: int  #  Indicates that the control should generate  wxEVT_TEXT_ENTER   events. Using this style will prevent the user from using the Enter key for dialog navigation (e.g. activating the default button in the dialog) under MSW.
ALIGN_LEFT: int  #  Same as wx.TE_LEFT for   wx.TextCtrl: int  #  the text is left aligned (this is the default).
ALIGN_CENTRE_HORIZONTAL: int  #  Same as wx.TE_CENTRE for   wx.TextCtrl: int  #  the text is centered.
ALIGN_RIGHT: int  #  Same as wx.TE_RIGHT for   wx.TextCtrl: int  #  the text is right aligned. ^^
EVT_SPINCTRL: int  #  Process a wxEVT_SPINCTRL event, which is generated whenever the numeric value of the spin control is updated. ^^
SP_ARROW_KEYS: int
SP_WRAP: int
TE_PROCESS_ENTER: int
ALIGN_LEFT: int
TE_LEFT: int
ALIGN_CENTRE_HORIZONTAL: int
TE_CENTRE: int
ALIGN_RIGHT: int
TE_RIGHT: int
ID_ANY: int


class SpinCtrlDouble(Control):
    """ SpinCtrlDouble combines TextCtrl and SpinButton in one control
and displays a real number.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, value="", pos=DefaultPosition, size=DefaultSize, style=SP_ARROW_KEYS, min=0, max=100, initial=0, inc=1, name="wxSpinCtrlDouble") -> bool:
        """ Creation function called by the spin control constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetDigits(self) -> int:
        """ Gets precision of the value of the spin control.
        """

    def GetIncrement(self) -> float:
        """ Gets the increment value.
        """

    def GetMax(self) -> float:
        """ Gets maximal allowable value.
        """

    def GetMin(self) -> float:
        """ Gets minimal allowable value.
        """

    def GetRange(self) -> None:
        """ 
        """

    def GetTextValue(self) -> str:
        """ Returns the text in the text entry part of the control.
        """

    def GetValue(self) -> float:
        """ Gets the value of the spin control.
        """

    def SetDigits(self, digits: int) -> None:
        """ Sets precision of the value of the spin control.
        """

    def SetIncrement(self, inc: float) -> None:
        """ Sets the increment value.
        """

    def SetMax(self, maxVal) -> None:
        """ 
        """

    def SetMin(self, minVal) -> None:
        """ 
        """

    def SetRange(self, minVal, maxVal) -> None:
        """ Sets range of allowable values.
        """

    def SetValue(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

SP_ARROW_KEYS: int  #  The user can use arrow keys to change the value.
SP_WRAP: int  #  The value wraps at the minimum and maximum. ^^
EVT_SPINCTRLDOUBLE: int  #  Generated whenever the numeric value of the spin control is changed, that is, when the up/down spin button is clicked, when ENTER is pressed, or the control loses focus and the new value is different from the last. See   wx.SpinDoubleEvent. ^^
SP_ARROW_KEYS: int
SP_WRAP: int
ID_ANY: int


class SpinDoubleEvent(NotifyEvent):
    """ This event class is used for the events generated by SpinCtrlDouble.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetValue(self) -> float:
        """ Returns the value associated with this spin control event.
        """

    def SetValue(self, value: float) -> None:
        """ Set the value associated with the event.
        """

EVT_SPINCTRLDOUBLE: int  #  Generated whenever the numeric value of the spin control is changed, that is, when the up/down spin button is clicked or when the control loses focus and the new value is different from the last one. See   wx.SpinDoubleEvent. ^^


class SpinEvent(NotifyEvent):
    """ This event class is used for the events generated by SpinButton and
SpinCtrl.
    """
    def __init__(self, commandType=wxEVT_NULL, id=0) -> None:
        """ The constructor is not normally used by the user code.
        """

    def GetPosition(self) -> int:
        """ Retrieve the current spin button or control value.
        """

    def SetPosition(self, pos: int) -> None:
        """ Set the value associated with the event.
        """

EVT_SPIN: int  #  Generated whenever an arrow is pressed.
EVT_SPIN_UP: int  #  Generated when left/up arrow is pressed.
EVT_SPIN_DOWN: int  #  Generated when right/down arrow is pressed. ^^
UP: int
DOWN: int


class SplitterEvent(NotifyEvent):
    """ This class represents the events generated by a splitter control.
    """
    def __init__(self, eventType=wxEVT_NULL, splitter=None) -> None:
        """ Constructor.
        """

    def GetOldSize(self) -> int:
        """ Returns the old size before the update.
        """

    def GetSashPosition(self) -> int:
        """ Returns the new sash position.
        """

    def GetWindowBeingRemoved(self) -> 'Window':
        """ Returns a pointer to the window being removed when a splitter window is unsplit.
        """

    def GetX(self) -> int:
        """ Returns the x coordinate of the double-click point.
        """

    def GetY(self) -> int:
        """ Returns the y coordinate of the double-click point.
        """

    def SetSashPosition(self, pos: int) -> None:
        """ In the case of  wxEVT_SPLITTER_SASH_POS_CHANGED   events, sets the new sash position.
        """

    def SetSize(self, oldSize, newSize) -> None:
        """ Sets the size values of the window size.
        """

EVT_SPLITTER_SASH_POS_CHANGING: int  #  The sash position is in the process of being changed. May be used to modify the position of the tracking bar to properly reflect the position that would be set if the drag were to be completed at this point. Processes a  wxEVT_SPLITTER_SASH_POS_CHANGING   event.
EVT_SPLITTER_SASH_POS_CHANGED: int  #  The sash position was changed. May be used to modify the sash position before it is set, or to prevent the change from taking place. Processes a  wxEVT_SPLITTER_SASH_POS_CHANGED   event.
EVT_SPLITTER_UNSPLIT: int  #  The splitter has been just unsplit. Processes a  wxEVT_SPLITTER_UNSPLIT   event.
EVT_SPLITTER_DCLICK: int  #  The sash was double clicked. The default behaviour is to unsplit the window when this happens (unless the minimum pane size has been set to a value greater than zero). Processes a  wxEVT_SPLITTER_DOUBLECLICKED   event. ^^


class SplitterRenderParams:
    """ This is just a simple struct used as a return value of
RendererNative.GetSplitterParams().
    """
    def __init__(self, widthSash_, border_, isSens_) -> None:
        """ The only way to initialize this struct is by using this constructor.
        """



class SplitterWindow(Window):
    """ This class manages up to two subwindows.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, point=DefaultPosition, size=DefaultSize, style=SP_3D, name="splitter") -> bool:
        """ Creation function, for two-step construction.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetDefaultSashSize(self) -> int:
        """ Returns the default sash size in pixels.
        """

    def GetMinimumPaneSize(self) -> int:
        """ Returns the current minimum pane size (defaults to zero).
        """

    def GetSashGravity(self) -> float:
        """ Returns the current sash gravity.
        """

    def GetSashPosition(self) -> int:
        """ Returns the current sash position.
        """

    def GetSashSize(self) -> int:
        """ Returns the default sash size in pixels or 0 if it is invisible.
        """

    def GetSplitMode(self) -> 'SplitMode':
        """ Gets the split mode.
        """

    def GetWindow1(self) -> 'Window':
        """ Returns the left/top or only pane.
        """

    def GetWindow2(self) -> 'Window':
        """ Returns the right/bottom pane.
        """

    def Initialize(self, window: 'Window') -> None:
        """ Initializes the splitter window to have one pane.
        """

    def IsSashInvisible(self) -> bool:
        """ Returns True if the sash is invisible even when the window is split, False otherwise.
        """

    def IsSplit(self) -> bool:
        """ Returns True if the window is split, False otherwise.
        """

    def ReplaceWindow(self, winOld, winNew) -> bool:
        """ This function replaces one of the windows managed by the   wx.SplitterWindow  with another one.
        """

    def SetMinimumPaneSize(self, paneSize: int) -> None:
        """ Sets the minimum pane size.
        """

    def SetSashGravity(self, gravity: float) -> None:
        """ Sets the sash gravity.
        """

    def SetSashInvisible(self, invisible: bool=True) -> None:
        """ Sets whether the sash should be invisible, even when the window is split.
        """

    def SetSashPosition(self, position, redraw=True) -> None:
        """ Sets the sash position.
        """

    def SetSplitMode(self, mode: int) -> None:
        """ Sets the split mode.
        """

    def SplitHorizontally(self, window1, window2, sashPosition=0) -> bool:
        """ Initializes the top and bottom panes of the splitter window.
        """

    def SplitVertically(self, window1, window2, sashPosition=0) -> bool:
        """ Initializes the left and right panes of the splitter window.
        """

    def Unsplit(self, toRemove: Optional['Window']=None) -> bool:
        """ Unsplits the window.
        """

    def UpdateSize(self) -> None:
        """ Causes any pending sizing of the sash and child panes to take place immediately.
        """

SP_3D: int  #  Draws a 3D effect border and sash.
SP_THIN_SASH: int  #  Draws a thin sash.
SP_3DSASH: int  #  Draws a 3D effect sash (part of default style).
SP_3DBORDER: int  #  Synonym for wx.SP_BORDER.
SP_BORDER: int  #  Draws a standard border.
SP_NOBORDER: int  #  No border (default).
SP_NO_XP_THEME: int  #  Under Windows, switches off the attempt to draw the splitter using Windows theming, so the borders and sash will take on the pre-XP look.
SP_PERMIT_UNSPLIT: int  #  Always allow to unsplit, even with the minimum pane size other than zero.
SP_LIVE_UPDATE: int  #  Donât draw wx.XOR line but resize the child windows immediately. ^^
EVT_SPLITTER_SASH_POS_CHANGING: int  #  The sash position is in the process of being changed. May be used to modify the position of the tracking bar to properly reflect the position that would be set if the drag were to be completed at this point. Processes a  wxEVT_SPLITTER_SASH_POS_CHANGING   event.
EVT_SPLITTER_SASH_POS_RESIZE: int  #  The sash position is in the process of being updated. May be used to modify the position of the tracking bar to properly reflect the position that would be set if the update were to be completed. This can happen e.g. when the window is resized and the sash is moved according to the gravity setting. This event is sent when the window is resized and allows the application to select the desired new sash position. If it doesnât process the event, the position is determined by the gravity setting. Processes a  wxEVT_SPLITTER_SASH_POS_RESIZE   event and is only available in wxWidgets 3.1.6 or newer.
EVT_SPLITTER_SASH_POS_CHANGED: int  #  The sash position was changed. May be used to modify the sash position before it is set, or to prevent the change from taking place. Processes a  wxEVT_SPLITTER_SASH_POS_CHANGED   event.
EVT_SPLITTER_UNSPLIT: int  #  The splitter has been just unsplit. Processes a  wxEVT_SPLITTER_UNSPLIT   event.
EVT_SPLITTER_DCLICK: int  #  The sash was double clicked. The default behaviour is to unsplit the window when this happens (unless the minimum pane size has been set to a value greater than zero). Processes a  wxEVT_SPLITTER_DOUBLECLICKED   event. ^^
SP_3D: int
SP_THIN_SASH: int
SP_3DSASH: int
SP_3DBORDER: int
SP_BORDER: int
SP_BORDER: int
SP_NOBORDER: int
SP_NO_XP_THEME: int
SP_PERMIT_UNSPLIT: int
SP_LIVE_UPDATE: int
XOR: int
SP_PERMIT_UNSPLIT: int
SPLIT_VERTICAL: int
SPLIT_HORIZONTAL: int


class StandardPaths:
    """ StandardPaths returns the standard locations in the file system and
should be used by applications to find their data files in a portable
way.
    """
    @staticmethod
    def Get() -> 'StandardPaths':
        """ Returns reference to the unique global standard paths object.
        """

    def GetAppDocumentsDir(self) -> str:
        """ Return the directory for the document files used by this application.
        """

    def GetConfigDir(self) -> str:
        """ Return the directory containing the system config files.
        """

    def GetDataDir(self) -> str:
        """ Return the location of the applications global, i.e. not user-specific, data files.
        """

    def GetDocumentsDir(self) -> str:
        """ Same as calling GetUserDir   with Dir_Documents parameter.
        """

    def GetExecutablePath(self) -> str:
        """ Return the directory and the filename for the current executable.
        """

    def GetFileLayout(self) -> 'StandardPaths.FileLayout':
        """ Returns the current file layout.
        """

    def GetInstallPrefix(self) -> str:
        """ Return the program installation prefix, e.g.  /usr ,   /opt   or   /home/zeitlin .
        """

    def GetLocalDataDir(self) -> str:
        """ Return the location for application data files which are host-specific and canât, or shouldnât, be shared with the other machines.
        """

    def GetLocalizedResourcesDir(self, lang, category=ResourceCat_None) -> str:
        """ Return the localized resources directory containing the resource files of the specified category for the given language.
        """

    def GetPluginsDir(self) -> str:
        """ Return the directory where the loadable modules (plugins) live.
        """

    def GetResourcesDir(self) -> str:
        """ Return the directory where the application resource files are located.
        """

    def GetTempDir(self) -> str:
        """ Return the directory for storing temporary files, for the current user.
        """

    def GetUserConfigDir(self) -> str:
        """ Return the directory for the user config files.
        """

    def GetUserDataDir(self) -> str:
        """ Return the directory for the user-dependent application data files:
        """

    def GetUserDir(self, userDir: Dir) -> str:
        """ Return the path of the specified user data directory.
        """

    def GetUserLocalDataDir(self) -> str:
        """ Return the directory for user data files which shouldnât be shared with the other machines.
        """

    @staticmethod
    def MSWGetShellDir(csidl: int) -> str:
        """ Returns location of Windows shell special folder.
        """

    def MakeConfigFileName(self, basename, conv=ConfigFileConv_Ext) -> str:
        """ Return the file name which would be used by   wx.FileConfig  if it were constructed with basename.
        """

    def SetFileLayout(self, layout: FileLayout) -> None:
        """ Sets the current file layout.
        """

    def SetInstallPrefix(self, prefix: str) -> None:
        """ Lets   wx.StandardPaths  know about the real program installation prefix on a Unix system.
        """

    def UseAppInfo(self, info: int) -> None:
        """ Controls what application information is used when constructing paths that should be unique to this program, such as the application data directory, the plugins directory on Unix, etc.
        """

    def __init__(self) -> None:
        """ Protected default constructor.
        """



class StaticBitmap(Control):
    """ A static bitmap control displays a bitmap.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, bitmap=NullBitmap, pos=DefaultPosition, size=DefaultSize, style=0, name=StaticBitmapNameStr) -> bool:
        """ Creation function, for two-step construction.
        """

    def GetBitmap(self) -> 'Bitmap':
        """ Returns the bitmap currently used in the control.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetIcon(self) -> 'Icon':
        """ Returns the icon currently used in the control.
        """

    def GetScaleMode(self) -> 'StaticBitmap.ScaleMode':
        """ Returns the scale mode currently used in the control.
        """

    def SetBitmap(self, label: 'BitmapBundle') -> None:
        """ Sets the bitmap label.
        """

    def SetIcon(self, label: 'Icon') -> None:
        """ Sets the label to the given icon.
        """

    def SetScaleMode(self, scaleMode: ScaleMode) -> None:
        """ Sets the scale mode.
        """



class StaticBox(Control):
    """ A static box is a rectangle drawn around other windows to denote a
logical grouping of items.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, label="", pos=DefaultPosition, size=DefaultSize, style=0, name=StaticBoxNameStr) -> bool:
        """ Creates the static box for two-step construction.
        """

    def Enable(self, enable: bool=True) -> bool:
        """ Enables or disables the box without affecting its label window, if any.
        """

    def GetBordersForSizer(self) -> tuple:
        """ Returns extra space that may be needed for borders within a StaticBox.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

ID_ANY: int


class StaticBoxSizer(BoxSizer):
    """ StaticBoxSizer is a sizer derived from BoxSizer but adds a static
box around the sizer.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def CalcMin(self) -> 'Size':
        """ Implements the calculation of a box sizerâs minimal.
        """

    def GetStaticBox(self) -> 'StaticBox':
        """ Returns the static box associated with the sizer.
        """

    def RepositionChildren(self, minSize: Union[tuple[int, int], 'Size']) -> None:
        """ Method which must be overridden in the derived sizer classes.
        """



class StaticLine(Control):
    """ A static line is just a line which may be used in a dialog to separate
the groups of controls.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=LI_HORIZONTAL, name=StaticLineNameStr) -> bool:
        """ Creates the static line for two-step construction.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    @staticmethod
    def GetDefaultSize() -> int:
        """ This static function returns the size which will be given to the smaller dimension of the static line, i.e.
        """

    def IsVertical(self) -> bool:
        """ Returns True if the line is vertical, False if horizontal.
        """

LI_HORIZONTAL: int  #  Creates a horizontal line.
LI_VERTICAL: int  #  Creates a vertical line. ^^
LI_HORIZONTAL: int
LI_VERTICAL: int
ID_ANY: int
LI_HORIZONTAL: int
LI_VERTICAL: int


class StaticText(Control):
    """ A static text control displays one or more lines of read-only text.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, label="", pos=DefaultPosition, size=DefaultSize, style=0, name=StaticTextNameStr) -> bool:
        """ Creation function, for two-step construction.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def IsEllipsized(self) -> bool:
        """ Returns True if the window styles for this control contains one of the  ST_ELLIPSIZE_START ,   ST_ELLIPSIZE_MIDDLE   or   ST_ELLIPSIZE_END   styles.
        """

    def SetLabel(self, label: str) -> None:
        """ Change the label shown in the control.
        """

    def Wrap(self, width: int) -> None:
        """ This functions wraps the controls label so that each of its lines becomes at most width  pixels wide if possible (the lines are broken at words boundaries so it might not be the case if words are too long).
        """

ALIGN_LEFT: int  #  Align the text to the left.
ALIGN_RIGHT: int  #  Align the text to the right.
ALIGN_CENTRE_HORIZONTAL: int  #  Center the text (horizontally).
ST_NO_AUTORESIZE: int  #  By default, the control will adjust its size to exactly fit to the size of the text when SetLabel  is called. If this style flag is given, the control will not change its size (this style is especially useful with controls which also have the  ALIGN_RIGHT   or the   ALIGN_CENTRE_HORIZONTAL   style because otherwise they wonât make sense any longer after a call to  SetLabel).
ST_ELLIPSIZE_START: int  #  If the labeltext width exceeds the control width, replace the beginning of the label with an ellipsis; uses wx.Control.Ellipsize .
ST_ELLIPSIZE_MIDDLE: int  #  If the label text width exceeds the control width, replace the middle of the label with an ellipsis; uses wx.Control.Ellipsize .
ST_ELLIPSIZE_END: int  #  If the label text width exceeds the control width, replace the end of the label with an ellipsis; uses wx.Control.Ellipsize . ^^
ALIGN_LEFT: int
ALIGN_RIGHT: int
ALIGN_CENTRE_HORIZONTAL: int
ST_NO_AUTORESIZE: int
ST_ELLIPSIZE_START: int
ST_ELLIPSIZE_MIDDLE: int
ST_ELLIPSIZE_END: int


class StatusBar(Control):
    """ A status bar is a narrow window that can be placed along the bottom of
a frame to give small amounts of status information.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, style=STB_DEFAULT_STYLE, name=StatusBarNameStr) -> bool:
        """ Creates the window, for two-step construction.
        """

    def GetBorders(self) -> 'Size':
        """ Returns the horizontal and vertical borders used when rendering the field text inside the field area.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetField(self, n: int) -> 'StatusBarPane':
        """ Returns the   wx.StatusBarPane  representing the n-th  field.
        """

    def GetFieldRect(self, i) -> 'Rect':
        """ Returns the size and position of a fieldâs internal bounding rectangle.
        """

    def GetFieldsCount(self) -> int:
        """ Returns the number of fields in the status bar.
        """

    def GetStatusStyle(self, n: int) -> int:
        """ Returns the style of the n-th  field.
        """

    def GetStatusText(self, i: int=0) -> str:
        """ Returns the string associated with a status bar field.
        """

    def GetStatusWidth(self, n: int) -> int:
        """ Returns the width of the n-th  field.
        """

    def PopStatusText(self, field: int=0) -> None:
        """ Restores the text to the value it had before the last call to PushStatusText .
        """

    def PushStatusText(self, string, field=0) -> None:
        """ Saves the current field text in a per-field stack, and sets the field text to the string passed as argument.
        """

    def SetFieldsCount(self, number=1, widths=None) -> None:
        """ Sets the number of fields, and optionally the field widths.
        """

    def SetMinHeight(self, height: int) -> None:
        """ Sets the minimal possible height for the status bar.
        """

    def SetStatusStyles(self, styles) -> None:
        """ Sets the styles of the fields in the status line which can make fields appear flat or raised instead of the standard sunken 3D border.
        """

    def SetStatusText(self, text, i=0) -> None:
        """ Sets the status text for the i-th  field.
        """

    def SetStatusWidths(self, widths: list[int]) -> None:
        """ Sets the widths of the fields in the status line.
        """

STB_SIZEGRIP: int  #  Displays a gripper at the right-hand side of the status bar which can be used to resize the parent window.
STB_SHOW_TIPS: int  #  Displays tooltips for those panes whose status text has been ellipsized/truncated because the status text doesnât fit the pane width. Note that this style has effect only on wxGTK (with GTK+ >= 2.12) currently.
STB_ELLIPSIZE_START: int  #  Replace the beginning of the status texts with an ellipsis when the status text widths exceed the status bar paneâs widths (uses wx.Control.Ellipsize ).
STB_ELLIPSIZE_MIDDLE: int  #  Replace the middle of the status texts with an ellipsis when the status text widths exceed the status bar paneâs widths (uses wx.Control.Ellipsize ).
STB_ELLIPSIZE_END: int  #  Replace the end of the status texts with an ellipsis when the status text widths exceed the status bar paneâs widths (uses wx.Control.Ellipsize ).
STB_DEFAULT_STYLE: int  #  The default style: int  #  includes  STB_SIZEGRIP|wxSTB_SHOW_TIPS|wxSTB_ELLIPSIZE_END|wxFULL_REPAINT_ON_RESIZE . ^^
STB_SIZEGRIP: int
STB_SHOW_TIPS: int
STB_ELLIPSIZE_START: int
STB_ELLIPSIZE_MIDDLE: int
STB_ELLIPSIZE_END: int
STB_DEFAULT_STYLE: int


class StatusBarPane:
    """ A status bar pane data container used by StatusBar.
    """
    def __init__(self, style=SB_NORMAL, width=0) -> None:
        """ Constructs the pane with the given style  and width.
        """

    def GetStyle(self) -> int:
        """ Returns the pane style.
        """

    def GetText(self) -> str:
        """ Returns the text currently shown in this pane.
        """

    def GetWidth(self) -> int:
        """ Returns the pane width; it maybe negative, indicating a variable-width field.
        """



class StdDialogButtonSizer(BoxSizer):
    """ This class creates button layouts which conform to the standard button
spacing and ordering defined by the platform or toolkitâs user
interface guidelines (if such things exist).
    """
    def __init__(self) -> None:
        """ Constructor for a   wx.StdDialogButtonSizer.
        """

    def AddButton(self, button: 'Button') -> None:
        """ Adds a button to the   wx.StdDialogButtonSizer.
        """

    def CalcMin(self) -> 'Size':
        """ Implements the calculation of a box sizerâs minimal.
        """

    def Realize(self) -> None:
        """ Rearranges the buttons and applies proper spacing between buttons to make them match the platform or toolkitâs interface guidelines.
        """

    def RepositionChildren(self, minSize: Union[tuple[int, int], 'Size']) -> None:
        """ Method which must be overridden in the derived sizer classes.
        """

    def SetAffirmativeButton(self, button: 'Button') -> None:
        """ Sets the affirmative button for the sizer.
        """

    def SetCancelButton(self, button: 'Button') -> None:
        """ Sets the cancel button for the sizer.
        """

    def SetNegativeButton(self, button: 'Button') -> None:
        """ Sets the negative button for the sizer.
        """

ID_SAVE: int
ID_NO: int
ID_OK: int
ID_YES: int
ID_SAVE: int
ID_APPLY: int
ID_CLOSE: int
ID_NO: int
ID_CANCEL: int
ID_HELP: int
ID_CONTEXT_HELP: int


class StockPreferencesPage(PreferencesPage):
    """ Specialization of PreferencesPage useful for certain commonly used
preferences page.
    """
    def __init__(self, kind: Kind) -> None:
        """ Constructor.
        """

    def GetIcon(self) -> 'BitmapBundle':
        """ Reimplemented to return stock icon on macOS.
        """

    def GetKind(self) -> 'StockPreferencesPage.Kind':
        """ Returns the pageâs kind.
        """

    def GetName(self) -> str:
        """ Reimplemented to return suitable name for the pageâs kind.
        """



class StopWatch:
    """ The StopWatch class allow you to measure time intervals.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def Pause(self) -> None:
        """ Pauses the stop watch.
        """

    def Resume(self) -> None:
        """ Resumes the stop watch which had been paused with Pause .
        """

    def Start(self, milliseconds: int=0) -> None:
        """ (Re)starts the stop watch with a given initial value.
        """

    def Time(self) -> int:
        """ Returns the time in milliseconds since the start (or restart) or the last call of Pause .
        """

    def TimeInMicro(self) -> int:
        """ Returns elapsed time in microseconds.
        """



class StreamBase:
    """ This class is the base class of most stream related classes in
wxWidgets.
    """
    def __init__(self) -> None:
        """ Creates a dummy stream object.
        """

    def GetLastError(self) -> 'StreamError':
        """ This function returns the last error.
        """

    def GetLength(self) -> 'FileOffset':
        """ Returns the length of the stream in bytes.
        """

    def GetSize(self) -> int:
        """ This function returns the size of the stream.
        """

    def IsOk(self) -> bool:
        """ Returns True if no error occurred on the stream.
        """

    def IsSeekable(self) -> bool:
        """ Returns True if the stream supports seeking to arbitrary offsets.
        """

    def Reset(self, error: StreamError=STREAM_NO_ERROR) -> None:
        """ Resets the stream state.
        """



class SVGBitmapEmbedHandler(SVGBitmapHandler):
    """ Handler embedding bitmaps as base64-encoded PNGs into the SVG.
    """
    def ProcessBitmap(self, bitmap, x, y, stream) -> bool:
        """ Writes the bitmap representation as SVG to the given stream.
        """



class SVGBitmapFileHandler(SVGBitmapHandler):
    """ Handler saving bitmaps to external PNG files and linking to it from
the SVG.
    """
    def __init__(self, path: str) -> None:
        """ Create a   wx.SVGBitmapFileHandler  and specify the location where the file will be saved.
        """

    def ProcessBitmap(self, bitmap, x, y, stream) -> bool:
        """ Writes the bitmap representation as SVG to the given stream.
        """



class SVGBitmapHandler:
    """ Abstract base class for handling bitmaps inside a SVGFileDC.
    """
    def ProcessBitmap(self, bitmap, x, y, stream) -> bool:
        """ Writes the bitmap representation as SVG to the given stream.
        """



class SVGFileDC(DC):
    """ A SVGFileDC is a device context onto which graphics and text can be
drawn, and the output produced as a vector file, in SVG format.
    """
    def __init__(self, filename, width=320, height=240, dpi=72, title="") -> None:
        """ Initializes a   wx.SVGFileDC  with the given filename, width  and height  at dpi  resolution, and an optional title.
        """

    def Clear(self) -> None:
        """ Draws a rectangle the size of the SVG using the wx.DC.SetBackground   brush.
        """

    def CrossHair(self, x, y) -> None:
        """ Function not implemented in this DC class.
        """

    def DestroyClippingRegion(self) -> None:
        """ Destroys the current clipping region so that none of the DC is clipped.
        """

    def EndDoc(self) -> None:
        """ Function not implemented in this DC class.
        """

    def EndPage(self) -> None:
        """ Function not implemented in this DC class.
        """

    def FloodFill(self, x, y, colour, style=FLOOD_SURFACE) -> bool:
        """ Function not implemented in this DC class.
        """

    def GetDepth(self) -> int:
        """ Function not implemented in this DC class.
        """

    def GetLogicalFunction(self) -> 'RasterOperationMode':
        """ Function not implemented in this DC class.
        """

    def GetPixel(self, x, y, colour) -> bool:
        """ Function not implemented in this DC class.
        """

    def SetBitmapHandler(self, handler: 'SVGBitmapHandler') -> None:
        """ Replaces the default bitmap handler with handler.
        """

    def SetLogicalFunction(self, function: RasterOperationMode) -> None:
        """ Function not implemented in this DC class.
        """

    def SetPalette(self, palette: 'Palette') -> None:
        """ Function not implemented in this DC class.
        """

    def SetShapeRenderingMode(self, renderingMode: SVGShapeRenderingMode) -> None:
        """ Set the shape rendering mode of the generated SVG.
        """

    def StartDoc(self, message: str) -> bool:
        """ Function not implemented in this DC class.
        """

    def StartPage(self) -> None:
        """ Function not implemented in this DC class.
        """

SVG_SHAPE_RENDERING_AUTO: int


class SysColourChangedEvent(Event):
    """ This class is used for system colour change events, which are
generated when the user changes the colour settings or when the system
theme changes (e.g.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

EVT_SYS_COLOUR_CHANGED: int  #  Process a  wxEVT_SYS_COLOUR_CHANGED   event. ^^


class SystemAppearance:
    """ Provides information about the current system appearance.
    """
    def GetName(self) -> str:
        """ Return the name if available or empty string otherwise.
        """

    def IsDark(self) -> bool:
        """ Return True if the current system there is explicitly recognized as being a dark theme or if the default window background is dark.
        """

    def IsUsingDarkBackground(self) -> bool:
        """ Return True if the default window background is significantly darker than foreground.
        """



class SystemOptions(Object):
    """ SystemOptions stores option/value pairs that wxWidgets itself or
applications can use to alter behaviour at run-time.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    @staticmethod
    def GetOption(name: str) -> str:
        """ Gets an option.
        """

    @staticmethod
    def GetOptionInt(name: str) -> int:
        """ Gets an option as an integer.
        """

    @staticmethod
    def HasOption(name: str) -> bool:
        """ Returns True if the given option is present.
        """

    @staticmethod
    def IsFalse(name: str) -> bool:
        """ Returns True if the option with the given name  had been set to 0 value.
        """

    @staticmethod
    def SetOption(*args, **kw) -> None:
        """ Sets an option.
        """

CLIP_CHILDREN: int
BG_STYLE_COLOUR: int
FD_OPEN: int


class SystemSettings:
    """ SystemSettings allows the application to ask for details about the
system.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    @staticmethod
    def GetAppearance() -> 'SystemAppearance':
        """ Returns the object describing the current system appearance.
        """

    @staticmethod
    def GetColour(index: SystemColour) -> 'Colour':
        """ Returns a system colour.
        """

    @staticmethod
    def GetFont(index: SystemFont) -> 'Font':
        """ Returns a system font.
        """

    @staticmethod
    def GetMetric(index, win=None) -> int:
        """ Returns the value of a system metric, or -1 if the metric is not supported on the current system.
        """

    @staticmethod
    def GetScreenType() -> 'SystemScreenType':
        """ Returns the screen type.
        """

    @staticmethod
    def HasFeature(index: SystemFeature) -> bool:
        """ Returns True if the port has certain feature.
        """

SYS_CAPTION_Y: int
SYS_CURSOR_X: int


class TextAttr:
    """ TextAttr represents the character and paragraph attributes, or
style, for a range of text in a TextCtrl or RichTextCtrl.
    """
    def __init__(self, *args, **kw) -> None:
        """ Constructors.
        """

    def Apply(self, style, compareWith=None) -> bool:
        """ Applies the attributes in style  to the original object, but not those attributes from style  that are the same as those in compareWith  (if passed).
        """

    def EqPartial(self, attr, weakTest=True) -> bool:
        """ Partial equality test.
        """

    def GetAlignment(self) -> int:
        """ Returns the alignment flags.
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ Returns the background colour.
        """

    def GetBulletFont(self) -> str:
        """ Returns a string containing the name of the font associated with the bullet symbol.
        """

    def GetBulletName(self) -> str:
        """ Returns the standard bullet name, applicable if the bullet style is wx.TEXT_ATTR_BULLET_STYLE_STANDARD.
        """

    def GetBulletNumber(self) -> int:
        """ Returns the bullet number.
        """

    def GetBulletStyle(self) -> int:
        """ Returns the bullet style.
        """

    def GetBulletText(self) -> str:
        """ Returns the bullet text, which could be a symbol, or (for example) cached outline text.
        """

    def GetCharacterStyleName(self) -> str:
        """ Returns the name of the character style.
        """

    def GetFlags(self) -> int:
        """ Returns flags indicating which attributes are applicable.
        """

    def GetFont(self) -> 'Font':
        """ Creates and returns a font specified by the font attributes in the   wx.TextAttr  object.
        """

    def GetFontAttributes(self, font, flags=TEXT_ATTR_FONT) -> bool:
        """ Gets the font attributes from the given font, using only the attributes specified by flags.
        """

    def GetFontEncoding(self) -> int:
        """ Returns the font encoding.
        """

    def GetFontFaceName(self) -> str:
        """ Returns the font face name.
        """

    def GetFontFamily(self) -> int:
        """ Returns the font family.
        """

    def GetFontSize(self) -> int:
        """ Returns the font size in points.
        """

    def GetFontStyle(self) -> int:
        """ Returns the font style.
        """

    def GetFontUnderlined(self) -> bool:
        """ Returns True if the font is underlined.
        """

    def GetFontWeight(self) -> int:
        """ Returns the font weight.
        """

    def GetLeftIndent(self) -> int:
        """ Returns the left indent in tenths of a millimetre.
        """

    def GetLeftSubIndent(self) -> int:
        """ Returns the left sub-indent in tenths of a millimetre.
        """

    def GetLineSpacing(self) -> int:
        """ Returns the line spacing value, one of   wx.TextAttrLineSpacing  values.
        """

    def GetListStyleName(self) -> str:
        """ Returns the name of the list style.
        """

    def GetOutlineLevel(self) -> int:
        """ Returns the outline level.
        """

    def GetParagraphSpacingAfter(self) -> int:
        """ Returns the space in tenths of a millimeter after the paragraph.
        """

    def GetParagraphSpacingBefore(self) -> int:
        """ Returns the space in tenths of a millimeter before the paragraph.
        """

    def GetParagraphStyleName(self) -> str:
        """ Returns the name of the paragraph style.
        """

    def GetRightIndent(self) -> int:
        """ Returns the right indent in tenths of a millimeter.
        """

    def GetTabs(self) -> list[int]:
        """ Returns an array of tab stops, each expressed in tenths of a millimeter.
        """

    def GetTextColour(self) -> 'Colour':
        """ Returns the text foreground colour.
        """

    def GetTextEffectFlags(self) -> int:
        """ Returns the text effect bits of interest.
        """

    def GetTextEffects(self) -> int:
        """ Returns the text effects, a bit list of styles.
        """

    def GetURL(self) -> str:
        """ Returns the URL for the content.
        """

    def GetUnderlineColour(self) -> 'Colour':
        """ Returns the underline color used.
        """

    def GetUnderlineType(self) -> 'TextAttrUnderlineType':
        """ Returns the underline type, which is one of the TextAttrUnderlineType values.
        """

    def HasAlignment(self) -> bool:
        """ Returns True if the attribute object specifies alignment.
        """

    def HasBackgroundColour(self) -> bool:
        """ Returns True if the attribute object specifies a background colour.
        """

    def HasBulletName(self) -> bool:
        """ Returns True if the attribute object specifies a standard bullet name.
        """

    def HasBulletNumber(self) -> bool:
        """ Returns True if the attribute object specifies a bullet number.
        """

    def HasBulletStyle(self) -> bool:
        """ Returns True if the attribute object specifies a bullet style.
        """

    def HasBulletText(self) -> bool:
        """ Returns True if the attribute object specifies bullet text (usually specifying a symbol).
        """

    def HasCharacterStyleName(self) -> bool:
        """ Returns True if the attribute object specifies a character style name.
        """

    def HasFlag(self, flag: int) -> bool:
        """ Returns True if the flag  is present in the attribute objectâs flag bitlist.
        """

    def HasFont(self) -> bool:
        """ Returns True if the attribute object specifies any font attributes.
        """

    def HasFontEncoding(self) -> bool:
        """ Returns True if the attribute object specifies an encoding.
        """

    def HasFontFaceName(self) -> bool:
        """ Returns True if the attribute object specifies a font face name.
        """

    def HasFontFamily(self) -> bool:
        """ Returns True if the attribute object specifies a font family.
        """

    def HasFontItalic(self) -> bool:
        """ Returns True if the attribute object specifies italic style.
        """

    def HasFontPixelSize(self) -> bool:
        """ Returns True if the attribute object specifies a font pixel size.
        """

    def HasFontPointSize(self) -> bool:
        """ Returns True if the attribute object specifies a font point size.
        """

    def HasFontSize(self) -> bool:
        """ Returns True if the attribute object specifies a font point or pixel size.
        """

    def HasFontUnderlined(self) -> bool:
        """ Returns True if the attribute object specifies either underlining or no underlining.
        """

    def HasFontWeight(self) -> bool:
        """ Returns True if the attribute object specifies font weight (bold, light or normal).
        """

    def HasLeftIndent(self) -> bool:
        """ Returns True if the attribute object specifies a left indent.
        """

    def HasLineSpacing(self) -> bool:
        """ Returns True if the attribute object specifies line spacing.
        """

    def HasListStyleName(self) -> bool:
        """ Returns True if the attribute object specifies a list style name.
        """

    def HasOutlineLevel(self) -> bool:
        """ Returns True if the attribute object specifies an outline level.
        """

    def HasPageBreak(self) -> bool:
        """ Returns True if the attribute object specifies a page break before this paragraph.
        """

    def HasParagraphSpacingAfter(self) -> bool:
        """ Returns True if the attribute object specifies spacing after a paragraph.
        """

    def HasParagraphSpacingBefore(self) -> bool:
        """ Returns True if the attribute object specifies spacing before a paragraph.
        """

    def HasParagraphStyleName(self) -> bool:
        """ Returns True if the attribute object specifies a paragraph style name.
        """

    def HasRightIndent(self) -> bool:
        """ Returns True if the attribute object specifies a right indent.
        """

    def HasTabs(self) -> bool:
        """ Returns True if the attribute object specifies tab stops.
        """

    def HasTextColour(self) -> bool:
        """ Returns True if the attribute object specifies a text foreground colour.
        """

    def HasTextEffects(self) -> bool:
        """ Returns True if the attribute object specifies text effects.
        """

    def HasURL(self) -> bool:
        """ Returns True if the attribute object specifies a URL.
        """

    def IsCharacterStyle(self) -> bool:
        """ Returns True if the object represents a character style, that is, the flags specify a font or a text background or foreground colour.
        """

    def IsDefault(self) -> bool:
        """ Returns False if we have any attributes set, True otherwise.
        """

    def IsParagraphStyle(self) -> bool:
        """ Returns True if the object represents a paragraph style, that is, the flags specify alignment, indentation, tabs, paragraph spacing, or bullet style.
        """

    def Merge(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetAlignment(self, alignment: int) -> None:
        """ Sets the paragraph alignment.
        """

    def SetBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ Sets the background colour.
        """

    def SetBulletFont(self, font: str) -> None:
        """ Sets the name of the font associated with the bullet symbol.
        """

    def SetBulletName(self, name: str) -> None:
        """ Sets the standard bullet name, applicable if the bullet style is wx.TEXT_ATTR_BULLET_STYLE_STANDARD.
        """

    def SetBulletNumber(self, n: int) -> None:
        """ Sets the bullet number.
        """

    def SetBulletStyle(self, style: int) -> None:
        """ Sets the bullet style.
        """

    def SetBulletText(self, text: str) -> None:
        """ Sets the bullet text, which could be a symbol, or (for example) cached outline text.
        """

    def SetCharacterStyleName(self, name: str) -> None:
        """ Sets the character style name.
        """

    def SetFlags(self, flags: int) -> None:
        """ Sets the flags determining which styles are being specified.
        """

    def SetFont(self, font, flags=TEXT_ATTR_FONT & ~TEXT_ATTR_FONT_PIXEL_SIZE) -> None:
        """ Sets the attributes for the given font.
        """

    def SetFontEncoding(self, encoding: int) -> None:
        """ Sets the font encoding.
        """

    def SetFontFaceName(self, faceName: str) -> None:
        """ Sets the font face name.
        """

    def SetFontFamily(self, family: int) -> None:
        """ Sets the font family.
        """

    def SetFontPixelSize(self, pixelSize: int) -> None:
        """ Sets the font size in pixels.
        """

    def SetFontPointSize(self, pointSize: int) -> None:
        """ Sets the font size in points.
        """

    def SetFontSize(self, pointSize: int) -> None:
        """ Sets the font size in points.
        """

    def SetFontStyle(self, fontStyle: int) -> None:
        """ Sets the font style (normal, italic or slanted).
        """

    def SetFontUnderlined(self, underlined: bool) -> None:
        """ Sets the font underlining (solid line, text colour).
        """

    def SetFontUnderlineType(self, type, colour=NullColour) -> None:
        """ Sets the font underlining.
        """

    def SetFontWeight(self, fontWeight: int) -> None:
        """ Sets the font weight.
        """

    def SetLeftIndent(self, indent, subIndent=0) -> None:
        """ Sets the left indent and left subindent in tenths of a millimetre.
        """

    def SetLineSpacing(self, spacing: int) -> None:
        """ Sets the line spacing.
        """

    def SetListStyleName(self, name: str) -> None:
        """ Sets the list style name.
        """

    def SetOutlineLevel(self, level: int) -> None:
        """ Specifies the outline level.
        """

    def SetPageBreak(self, pageBreak: bool=True) -> None:
        """ Specifies a page break before this paragraph.
        """

    def SetParagraphSpacingAfter(self, spacing: int) -> None:
        """ Sets the spacing after a paragraph, in tenths of a millimetre.
        """

    def SetParagraphSpacingBefore(self, spacing: int) -> None:
        """ Sets the spacing before a paragraph, in tenths of a millimetre.
        """

    def SetParagraphStyleName(self, name: str) -> None:
        """ Sets the name of the paragraph style.
        """

    def SetRightIndent(self, indent: int) -> None:
        """ Sets the right indent in tenths of a millimetre.
        """

    def SetTabs(self, tabs: list[int]) -> None:
        """ Sets the tab stops, expressed in tenths of a millimetre.
        """

    def SetTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ Sets the text foreground colour.
        """

    def SetTextEffectFlags(self, flags: int) -> None:
        """ Sets the text effect bits of interest.
        """

    def SetTextEffects(self, effects: int) -> None:
        """ Sets the text effects, a bit list of styles.
        """

    def SetURL(self, url: str) -> None:
        """ Sets the URL for the content.
        """

TEXT_ATTR_BULLET_STYLE_STANDARD: int
TEXT_ATTR_BULLET_STYLE_STANDARD: int
TEXT_ATTR_BULLET_STYLE_STANDARD: int
TEXT_ATTR_URL: int
TEXT_ALIGNMENT_JUSTIFIED: int
TEXT_ATTR_BULLET_STYLE_STANDARD: int
TEXT_ATTR_BULLET_STYLE_BITMAP: int
TEXT_ATTR_UNDERLINE_DOUBLE: int
TEXT_ATTR_UNDERLINE_SOLID: int
TEXT_ATTR_UNDERLINE_SPECIAL: int
TEXT_ATTR_UNDERLINE_SPECIAL: int
TEXT_ATTR_UNDERLINE_SPECIAL: int
TEXT_ATTR_UNDERLINE_SPECIAL: int
TEXT_ATTR_EFFECTS: int
TEXT_ATTR_EFFECT_CAPITALS: int
TEXT_ATTR_EFFECT_STRIKETHROUGH: int
TEXT_ATTR_EFFECT_SUPERSCRIPT: int
TEXT_ATTR_EFFECT_SUBSCRIPT: int
TEXT_ATTR_EFFECT_CAPITALS: int
TEXT_ATTR_EFFECT_STRIKETHROUGH: int
TEXT_ATTR_EFFECTS: int
TEXT_ATTR_URL: int


class TextCompleter:
    """ Base class for custom text completer objects.
    """
    def GetNext(self) -> str:
        """ Called to retrieve the next completion.
        """

    def Start(self, prefix: str) -> bool:
        """ Function called to start iteration over the completions for the given prefix.
        """



class TextCompleterSimple(TextCompleter):
    """ A simpler base class for custom completer objects.
    """
    def GetCompletions(self, prefix: str) -> res:
        """ Pure virtual method returning all possible completions for the given prefix.
        """

    def GetNext(self) -> str:
        """ Called to retrieve the next completion.
        """

    def Start(self, prefix: str) -> bool:
        """ Function called to start iteration over the completions for the given prefix.
        """



class TextDataObject(DataObjectSimple):
    """ TextDataObject is a specialization of DataObjectSimple for text
data.
    """
    def __init__(self, text: str="") -> None:
        """ Constructor, may be used to initialise the text (otherwise SetText   should be used later).
        """

    def GetAllFormats(self, dir=DataObject.Get) -> None:
        """ Returns a list of wx.DataFormat objects which this data object
supports transferring in the given direction.
        """

    def GetFormat(self) -> 'DataFormat':
        """ Returns the preferred format supported by this object.
        """

    def GetFormatCount(self, dir: int=DataObject.Get) -> int:
        """ Returns 2 under Mac and wxGTK, where text data coming from the clipboard may be provided as ANSI ( DF_TEXT ) or as Unicode text ( DF_UNICODETEXT , but only when   USE_UNICODE==1 ).
        """

    def GetText(self) -> str:
        """ Returns the text associated with the data object.
        """

    def GetTextLength(self) -> int:
        """ Returns the data size.
        """

    def SetData(self, format, buf) -> bool:
        """ bool
        """

    def SetText(self, strText: str) -> None:
        """ Sets the text associated with the data object.
        """



class TextDropTarget(DropTarget):
    """ A predefined drop target for dealing with text data.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def OnDrop(self, x, y) -> bool:
        """ See wx.DropTarget.OnDrop .
        """

    def OnDropText(self, x, y, data) -> bool:
        """ Override this function to receive dropped text.
        """



class TextEntry:
    """ Common base class for single line text entry fields.
    """
    def AppendText(self, text: str) -> None:
        """ Appends the text to the end of the text control.
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

    def CanCopy(self) -> bool:
        """ Returns True if the selection can be copied to the clipboard.
        """

    def CanCut(self) -> bool:
        """ Returns True if the selection can be cut to the clipboard.
        """

    def CanPaste(self) -> bool:
        """ Returns True if the contents of the clipboard can be pasted into the text control.
        """

    def CanRedo(self) -> bool:
        """ Returns True if there is a redo facility available and the last operation can be redone.
        """

    def CanUndo(self) -> bool:
        """ Returns True if there is an undo facility available and the last operation can be undone.
        """

    def ChangeValue(self, value: str) -> None:
        """ Sets the new text control value.
        """

    def Clear(self) -> None:
        """ Clears the text in the control.
        """

    def Copy(self) -> None:
        """ Copies the selected text to the clipboard.
        """

    def Cut(self) -> None:
        """ Copies the selected text to the clipboard and removes it from the control.
        """

    def ForceUpper(self) -> None:
        """ Convert all text entered into the control to upper case.
        """

    def GetHint(self) -> str:
        """ Returns the current hint string.
        """

    def GetInsertionPoint(self) -> int:
        """ Returns the insertion point, or cursor, position.
        """

    def GetLastPosition(self) -> 'TextPos':
        """ Returns the zero based index of the last position in the text control, which is equal to the number of characters in the control.
        """

    def GetMargins(self) -> 'Point':
        """ Returns the margins used by the control.
        """

    def GetRange(self, from_, to_) -> str:
        """ Returns the string containing the text starting in the positions from  and up to to  in the control.
        """

    def GetSelection(self) -> tuple:
        """ Gets the current selection span.
        """

    def GetStringSelection(self) -> str:
        """ Gets the text currently selected in the control.
        """

    def GetValue(self) -> str:
        """ Gets the contents of the control.
        """

    def IsEditable(self) -> bool:
        """ Returns True if the controls contents may be edited by user (note that it always can be changed by the program).
        """

    def IsEmpty(self) -> bool:
        """ Returns True if the control is currently empty.
        """

    def Paste(self) -> None:
        """ Pastes text from the clipboard to the text item.
        """

    def Redo(self) -> None:
        """ If there is a redo facility and the last operation can be redone, redoes the last operation.
        """

    def Remove(self, from_, to_) -> None:
        """ Removes the text starting at the first given position up to (but not including) the character at the last position.
        """

    def Replace(self, from_, to_, value) -> None:
        """ Replaces the text starting at the first position up to (but not including) the character at the last position with the given text.
        """

    def SelectAll(self) -> None:
        """ Selects all text in the control.
        """

    def SelectNone(self) -> None:
        """ Deselects selected text in the control.
        """

    def SetEditable(self, editable: bool) -> None:
        """ Makes the text item editable or read-only, overriding the wx.TE_READONLY  flag.
        """

    def SetHint(self, hint: str) -> bool:
        """ Sets a hint shown in an empty unfocused text control.
        """

    def SetInsertionPoint(self, pos: int) -> None:
        """ Sets the insertion point at the given position.
        """

    def SetInsertionPointEnd(self) -> None:
        """ Sets the insertion point at the end of the text control.
        """

    def SetMargins(self, *args, **kw) -> None:
        """ Attempts to set the control margins.
        """

    def SetMaxLength(self, len: int) -> None:
        """ This function sets the maximum number of characters the user can enter into the control.
        """

    def SetSelection(self, from_, to_) -> None:
        """ Selects the text starting at the first position up to (but not including) the character at the last position.
        """

    def SetValue(self, value: str) -> None:
        """ Sets the new text control value.
        """

    def Undo(self) -> None:
        """ If there is an undo facility and the last operation can be undone, undoes the last operation.
        """

    def WriteText(self, text: str) -> None:
        """ Writes the text into the text control at the current insertion position.
        """

TE_READONLY: int
TE_READONLY: int


class TextEntryDialog(Dialog):
    """ This class represents a dialog that requests a one-line text string
from the user.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, message, caption=GetTextFromUserPromptStr, value="", style=TextEntryDialogStyle, pos=DefaultPosition) -> bool:
        """ parent (wx.Window) â Parent window.
        """

    def ForceUpper(self) -> None:
        """ Convert all text entered into the text control used by the dialog to upper case.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetValue(self) -> str:
        """ Returns the text that the user has entered if the user has pressed wx.OK, or the original value if the user has pressed Cancel.
        """

    def SetMaxLength(self, len: int) -> None:
        """ This function sets the maximum number of characters the user can enter into this dialog.
        """

    def SetValue(self, value: str) -> None:
        """ Sets the default text value.
        """

    def ShowModal(self) -> int:
        """ Shows the dialog, returning wx.ID_OK if the user pressed wx.OK, and wx.ID_CANCEL otherwise.
        """

OK: int
ID_OK: int
OK: int
ID_CANCEL: int
CANCEL: int
CENTRE: int
OK: int
ID_OK: int
OK: int
ID_CANCEL: int


class TextUrlEvent(CommandEvent):
    """  Overloaded Implementations:
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Clone(self) -> 'Event':
        """ Returns a copy of the event.
        """

    def GetMouseEvent(self) -> 'MouseEvent':
        """ wx.MouseEvent
        """

    def GetURLEnd(self) -> int:
        """ long
        """

    def GetURLStart(self) -> int:
        """ long
        """



class TGAHandler(ImageHandler):
    """ This is the image handler for the TGA format.
    """
    def __init__(self) -> None:
        """ Default constructor for   wx.TGAHandler.
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Called to test if this handler can read an image from the given stream.
        """

    def LoadFile(self, image, stream, verbose=True, index=-1) -> bool:
        """ Loads an image from a stream, putting the resulting data into image.
        """

    def SaveFile(self, image, stream, verbose=True) -> bool:
        """ Saves an image in the output stream.
        """



class TIFFHandler(ImageHandler):
    """ This is the image handler for the TIFF format.
    """
    def __init__(self) -> None:
        """ Default constructor for   wx.TIFFHandler.
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Called to test if this handler can read an image from the given stream.
        """

    def LoadFile(self, image, stream, verbose=True, index=-1) -> bool:
        """ Loads an image from a stream, putting the resulting data into image.
        """



class TimerEvent(Event):
    """ TimerEvent object is passed to the event handler of timer events
(see Timer.SetOwner).
    """
    def __init__(self, timer: 'Timer') -> None:
        """ timer (wx.Timer) â
        """

    def GetInterval(self) -> int:
        """ Returns the interval of the timer which generated this event.
        """

    def GetTimer(self) -> 'Timer':
        """ Returns the timer object which generated this event.
        """



class TimerRunner:
    """ Starts the timer in its constructor, stops in the dtor.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Start(self, milli, oneShot=False) -> None:
        """ milli (int) â
        """



class TimeSpan:
    """ TimeSpan class represents a time interval.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Abs(self) -> 'TimeSpan':
        """ Returns the absolute value of the timespan: does not modify the object.
        """

    def Add(self, diff: 'TimeSpan') -> 'TimeSpan':
        """ Adds the given   wx.TimeSpan  to this   wx.TimeSpan  and returns a reference to itself.
        """

    @staticmethod
    def Day() -> 'TimeSpan':
        """ Returns the timespan for one day.
        """

    @staticmethod
    def Days(days: int) -> 'TimeSpan':
        """ Returns the timespan for the given number of days.
        """

    def Format(self, format: str=DefaultTimeSpanFormat) -> str:
        """ Returns the string containing the formatted representation of the time span.
        """

    def GetDays(self) -> int:
        """ Returns the difference in number of days.
        """

    def GetHours(self) -> int:
        """ Returns the difference in number of hours.
        """

    def GetMilliseconds(self) -> int:
        """ Returns the difference in number of milliseconds.
        """

    def GetMinutes(self) -> int:
        """ Returns the difference in number of minutes.
        """

    def GetSeconds(self) -> int:
        """ Returns the difference in number of seconds.
        """

    def GetValue(self) -> int:
        """ Returns the internal representation of timespan.
        """

    def GetWeeks(self) -> int:
        """ Returns the difference in number of weeks.
        """

    @staticmethod
    def Hour() -> 'TimeSpan':
        """ Returns the timespan for one hour.
        """

    @staticmethod
    def Hours(hours: int) -> 'TimeSpan':
        """ Returns the timespan for the given number of hours.
        """

    def IsEqualTo(self, ts: 'TimeSpan') -> bool:
        """ Returns True if two timespans are equal.
        """

    def IsLongerThan(self, ts: 'TimeSpan') -> bool:
        """ Compares two timespans: works with the absolute values, i.e. -2 hours is longer than 1 hour.
        """

    def IsNegative(self) -> bool:
        """ Returns True if the timespan is negative.
        """

    def IsNull(self) -> bool:
        """ Returns True if the timespan is empty.
        """

    def IsPositive(self) -> bool:
        """ Returns True if the timespan is positive.
        """

    def IsShorterThan(self, ts: 'TimeSpan') -> bool:
        """ Compares two timespans: works with the absolute values, i.e. 1 hour is shorter than -2 hours.
        """

    @staticmethod
    def Millisecond() -> 'TimeSpan':
        """ Returns the timespan for one millisecond.
        """

    @staticmethod
    def Milliseconds(ms: int) -> 'TimeSpan':
        """ Returns the timespan for the given number of milliseconds.
        """

    @staticmethod
    def Minute() -> 'TimeSpan':
        """ Returns the timespan for one minute.
        """

    @staticmethod
    def Minutes(min: int) -> 'TimeSpan':
        """ Returns the timespan for the given number of minutes.
        """

    def Multiply(self, n: int) -> 'TimeSpan':
        """ Multiplies this time span by n.
        """

    def Neg(self) -> 'TimeSpan':
        """ Negate the value of the timespan.
        """

    def Negate(self) -> 'TimeSpan':
        """ Returns timespan with inverted sign.
        """

    @staticmethod
    def Second() -> 'TimeSpan':
        """ Returns the timespan for one second.
        """

    @staticmethod
    def Seconds(sec: int) -> 'TimeSpan':
        """ Returns the timespan for the given number of seconds.
        """

    def Subtract(self, diff: 'TimeSpan') -> 'TimeSpan':
        """ Subtracts the given   wx.TimeSpan  to this   wx.TimeSpan  and returns a reference to itself.
        """

    @staticmethod
    def Week() -> 'TimeSpan':
        """ Returns the timespan for one week.
        """

    @staticmethod
    def Weeks(weeks: int) -> 'TimeSpan':
        """ Returns the timespan for the given number of weeks.
        """



class TipWindow(Window):
    """ Shows simple text in a popup tip window on creation.
    """
    def __init__(self, parent, text, maxLength=100) -> None:
        """ Constructor.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def SetBoundingRect(self, rectBound: 'Rect') -> None:
        """ By default, the tip window disappears when the user clicks the mouse or presses a keyboard key or if it loses focus in any other way - for example because the user switched to another application window.
        """



class ToolBar(Control):
    """ A toolbar is a bar of buttons and/or other controls usually placed
below the menu bar in a Frame.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddCheckTool(self, toolId, label, bitmap1, bmpDisabled=NullBitmap, shortHelp="", longHelp="", clientData=None) -> 'ToolBarToolBase':
        """ Adds a new check (or toggle) tool to the toolbar.
        """

    def AddControl(self, control, label="") -> 'ToolBarToolBase':
        """ Adds any control to the toolbar, typically e.g. a   wx.ComboBox.
        """

    def AddLabelTool(self, id, label, bitmap, bmpDisabled=wx.NullBitmap, kind=wx.ITEM_NORMAL, shortHelp="", longHelp="", clientData=None) -> None:
        """ Old style method to add a tool in the toolbar.
        """

    def AddRadioTool(self, toolId, label, bitmap1, bmpDisabled=NullBitmap, shortHelp="", longHelp="", clientData=None) -> 'ToolBarToolBase':
        """ Adds a new radio tool to the toolbar.
        """

    def AddSeparator(self) -> 'ToolBarToolBase':
        """ Adds a separator for spacing groups of tools.
        """

    def AddSimpleTool(self, toolId, bitmap, shortHelpString="", longHelpString="", isToggle=0) -> None:
        """ Old style method to add a tool to the toolbar.
        """

    def AddStretchableSpace(self) -> 'ToolBarToolBase':
        """ Adds a stretchable space to the toolbar.
        """

    def AddTool(self, *args, **kw) -> 'ToolBarToolBase':
        """ Overloaded Implementations:
        """

    def ClearTools(self) -> None:
        """ Deletes all the tools in the toolbar.
        """

    def CreateSeparator(self) -> 'ToolBarToolBase':
        """ Factory function to create a new separator toolbar tool.
        """

    def CreateTool(self, *args, **kw) -> 'ToolBarToolBase':
        """ Overloaded Implementations:
        """

    def DeleteTool(self, toolId: int) -> bool:
        """ Removes the specified tool from the toolbar and deletes it.
        """

    def DeleteToolByPos(self, pos: int) -> bool:
        """ This function behaves like DeleteTool   but it deletes the tool at the specified position and not the one with the given id.
        """

    def EnableTool(self, toolId, enable) -> None:
        """ Enables or disables the tool.
        """

    def FindById(self, id: int) -> 'ToolBarToolBase':
        """ Returns a pointer to the tool identified by id  or None if no corresponding tool is found.
        """

    def FindControl(self, id: int) -> 'Control':
        """ Returns a pointer to the control identified by id  or None if no corresponding control is found.
        """

    def FindToolForPosition(self, x, y) -> 'ToolBarToolBase':
        """ Finds a tool for the given mouse position.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetMargins(self) -> 'Size':
        """ Returns the left/right and top/bottom margins, which are also used for inter-toolspacing.
        """

    def GetToolBitmapSize(self) -> 'Size':
        """ Returns the size of bitmap that the toolbar expects to have.
        """

    def GetToolByPos(self, pos: int) -> 'ToolBarToolBase':
        """ Returns a pointer to the tool at ordinal position pos.
        """

    def GetToolClientData(self, toolId: int) -> PyUserData:
        """ Get any client data associated with the tool.
        """

    def GetToolEnabled(self, toolId: int) -> bool:
        """ Called to determine whether a tool is enabled (responds to user input).
        """

    def GetToolLongHelp(self, toolId: int) -> str:
        """ Returns the long help for the given tool.
        """

    def GetToolPacking(self) -> int:
        """ Returns the value used for packing tools.
        """

    def GetToolPos(self, toolId: int) -> int:
        """ Returns the tool position in the toolbar, or  NOT_FOUND   if the tool is not found.
        """

    def GetToolSeparation(self) -> int:
        """ Returns the default separator size.
        """

    def GetToolShortHelp(self, toolId: int) -> str:
        """ Returns the short help for the given tool.
        """

    def GetToolSize(self) -> 'Size':
        """ Returns the size of a whole button, which is usually larger than a tool bitmap because of added 3D effects.
        """

    def GetToolState(self, toolId: int) -> bool:
        """ Gets the on/off state of a toggle tool.
        """

    def GetToolsCount(self) -> int:
        """ Returns the number of tools in the toolbar.
        """

    def InsertControl(self, pos, control, label="") -> 'ToolBarToolBase':
        """ Inserts the control into the toolbar at the given position.
        """

    def InsertLabelTool(self, pos, id, label, bitmap, bmpDisabled=wx.NullBitmap, kind=wx.ITEM_NORMAL, shortHelp="", longHelp="", clientData=None) -> None:
        """ Old style method to insert a tool in the toolbar.
        """

    def InsertSeparator(self, pos: int) -> 'ToolBarToolBase':
        """ Inserts the separator into the toolbar at the given position.
        """

    def InsertSimpleTool(self, pos, toolId, bitmap, shortHelpString="", longHelpString="", isToggle=0) -> None:
        """ Old style method to insert a tool in the toolbar.
        """

    def InsertStretchableSpace(self, pos: int) -> 'ToolBarToolBase':
        """ Inserts a stretchable space at the given position.
        """

    def InsertTool(self, *args, **kw) -> None:
        """ Inserts the tool with the specified attributes into the toolbar at the given position.
        """

    def Realize(self) -> bool:
        """ This function should be called after you have added tools.
        """

    def RemoveTool(self, id: int) -> 'ToolBarToolBase':
        """ Removes the given tool from the toolbar but doesnât delete it.
        """

    def SetDropdownMenu(self, id, menu) -> bool:
        """ Sets the dropdown menu for the tool given by its id.
        """

    def SetMargins(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetToolBitmapSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ Sets the default size of each tool bitmap.
        """

    def SetToolClientData(self, id, clientData) -> None:
        """ Sets the client data associated with the tool.
        """

    def SetToolDisabledBitmap(self, id, bitmap) -> None:
        """ Sets the bitmap to be used by the tool with the given ID when the tool is in a disabled state.
        """

    def SetToolLongHelp(self, toolId, helpString) -> None:
        """ Sets the long help for the given tool.
        """

    def SetToolNormalBitmap(self, id, bitmap) -> None:
        """ Sets the bitmap to be used by the tool with the given ID.
        """

    def SetToolPacking(self, packing: int) -> None:
        """ Sets the value used for spacing tools.
        """

    def SetToolSeparation(self, separation: int) -> None:
        """ Sets the default separator size.
        """

    def SetToolShortHelp(self, toolId, helpString) -> None:
        """ Sets the short help for the given tool.
        """

    def ToggleTool(self, toolId, toggle) -> None:
        """ Toggles a tool on or off.
        """

TB_FLAT: int  #  Gives the toolbar a flat look (Windows and GTK only).
TB_DOCKABLE: int  #  Makes the toolbar floatable and dockable (GTK only).
TB_HORIZONTAL: int  #  Specifies horizontal layout (default).
TB_VERTICAL: int  #  Specifies vertical layout.
TB_TEXT: int  #  Shows the text in the toolbar buttons; by default only icons are shown.
TB_NOICONS: int  #  Specifies no icons in the toolbar buttons; by default they are shown.
TB_NODIVIDER: int  #  Specifies no divider (border) above the toolbar (Windows only)
TB_NOALIGN: int  #  Specifies no alignment with the parent window (Windows only, not very useful).
TB_HORZ_LAYOUT: int  #  Shows the text and the icons alongside, not vertically stacked (Windows and GTK 2 only). This style must be used with  TB_TEXT .
TB_HORZ_TEXT: int  #  Combination of  TB_HORZ_LAYOUT   and   TB_TEXT .
TB_NO_TOOLTIPS: int  #  Donât show the short help tooltips for the tools when the mouse hovers over them.
TB_BOTTOM: int  #  Align the toolbar at the bottom of parent window.
TB_RIGHT: int  #  Align the toolbar at the right side of parent window.
TB_DEFAULT_STYLE: int  #  The  TB_HORIZONTAL   style. This style is new since wxWidgets 2.9.5. ^^
EVT_TOOL: int  #  Process a  wxEVT_TOOL   event (a synonym for   wxEVT_MENU ). Pass the id of the tool.
EVT_MENU: int  #  The same as EVT_TOOL().
EVT_TOOL_RANGE: int  #  Process a  wxEVT_TOOL   event for a range of identifiers. Pass the ids of the tools.
EVT_MENU_RANGE: int  #  The same as EVT_TOOL_RANGE().
EVT_TOOL_RCLICKED: int  #  Process a  wxEVT_TOOL_RCLICKED   event. Pass the id of the tool. (Not available on wxOSX.)
EVT_TOOL_RCLICKED_RANGE: int  #  Process a  wxEVT_TOOL_RCLICKED   event for a range of ids. Pass the ids of the tools. (Not available on wxOSX.)
EVT_TOOL_ENTER: int  #  Process a  wxEVT_TOOL_ENTER   event. Pass the id of the toolbar itself. The value of  wx.CommandEvent.GetSelection   is the tool id, or -1 if the mouse cursor has moved off a tool. (Not available on wxOSX.)
EVT_TOOL_DROPDOWN: int  #  Process a  wxEVT_TOOL_DROPDOWN   event. If unhandled, displays the default dropdown menu set using  wx.ToolBar.SetDropdownMenu . ^^
TB_FLAT: int
TB_DOCKABLE: int
TB_HORIZONTAL: int
TB_VERTICAL: int
TB_TEXT: int
TB_NOICONS: int
TB_NODIVIDER: int
TB_NOALIGN: int
TB_HORZ_LAYOUT: int
TB_HORZ_TEXT: int
TB_NO_TOOLTIPS: int
TB_BOTTOM: int
TB_RIGHT: int
TB_DEFAULT_STYLE: int


class ToolBarToolBase(Object):
    """ A toolbar tool represents one item on the toolbar.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Attach(self, tbar: 'ToolBar') -> None:
        """ tbar (wx.ToolBar) â
        """

    def CanBeToggled(self) -> bool:
        """ bool
        """

    def Detach(self) -> None:
        """ 
        """

    def Enable(self, enable: bool) -> bool:
        """ enable (bool) â
        """

    def GetBitmap(self) -> 'Bitmap':
        """ wx.Bitmap
        """

    def GetClientData(self) -> PyUserData:
        """ PyUserData
        """

    def GetControl(self) -> 'Control':
        """ wx.Control
        """

    def GetDisabledBitmap(self) -> 'Bitmap':
        """ wx.Bitmap
        """

    def GetDisabledBitmapBundle(self) -> 'BitmapBundle':
        """ Return the bundle containing disabled tool bitmaps.
        """

    def GetDropdownMenu(self) -> 'Menu':
        """ wx.Menu
        """

    def GetId(self) -> int:
        """ int
        """

    def GetKind(self) -> 'ItemKind':
        """ wx.ItemKind
        """

    def GetLabel(self) -> str:
        """ string
        """

    def GetLongHelp(self) -> str:
        """ string
        """

    def GetNormalBitmap(self) -> 'Bitmap':
        """ wx.Bitmap
        """

    def GetNormalBitmapBundle(self) -> 'BitmapBundle':
        """ Return the bundle containing normal tool bitmaps.
        """

    def GetShortHelp(self) -> str:
        """ string
        """

    def GetStyle(self) -> int:
        """ int
        """

    def GetToolBar(self) -> 'ToolBar':
        """ Return the toolbar this tool is a member of.
        """

    def IsButton(self) -> bool:
        """ bool
        """

    def IsControl(self) -> bool:
        """ bool
        """

    def IsEnabled(self) -> bool:
        """ bool
        """

    def IsSeparator(self) -> bool:
        """ bool
        """

    def IsStretchable(self) -> bool:
        """ bool
        """

    def IsStretchableSpace(self) -> bool:
        """ bool
        """

    def IsToggled(self) -> bool:
        """ bool
        """

    def MakeStretchable(self) -> None:
        """ 
        """

    def SetClientData(self, clientData: PyUserData) -> None:
        """ clientData (PyUserData) â
        """

    def SetDisabledBitmap(self, bmp: 'BitmapBundle') -> None:
        """ bmp (wx.BitmapBundle) â
        """

    def SetDropdownMenu(self, menu: 'Menu') -> None:
        """ menu (wx.Menu) â
        """

    def SetLabel(self, label: str) -> None:
        """ label (string) â
        """

    def SetLongHelp(self, help: str) -> bool:
        """ help (string) â
        """

    def SetNormalBitmap(self, bmp: 'BitmapBundle') -> None:
        """ bmp (wx.BitmapBundle) â
        """

    def SetShortHelp(self, help: str) -> bool:
        """ help (string) â
        """

    def SetToggle(self, toggle: bool) -> bool:
        """ toggle (bool) â
        """

    def Toggle(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """



class Toolbook(BookCtrlBase):
    """ Toolbook is a class similar to Notebook but which uses a ToolBar
to show the labels instead of the tabs.
    """
    def __init__(self, *args, **kw) -> None:
        """ Constructs a choicebook control.
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name="") -> bool:
        """ Create the tool book control that has already been constructed with the default constructor.
        """

    def EnablePage(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetToolBar(self) -> 'ToolBar':
        """ Return the toolbar used for page selection.
        """

TBK_BUTTONBAR: int  #  Use ButtonToolBar-based implementation under macOS (ignored under other platforms).
TBK_HORZ_LAYOUT: int  #  Shows the text and the icons alongside, not vertically stacked (only implement under Windows and GTK 2 platforms as it relies on  TB_HORZ_LAYOUT   flag support). ^^
EVT_TOOLBOOK_PAGE_CHANGED: int  #  The page selection was changed. Processes a  wxEVT_TOOLBOOK_PAGE_CHANGED   event.
EVT_TOOLBOOK_PAGE_CHANGING: int  #  The page selection is about to be changed. Processes a  wxEVT_TOOLBOOK_PAGE_CHANGING   event. This event can be vetoed (using  wx.NotifyEvent.Veto ). ^^
TBK_BUTTONBAR: int
TBK_HORZ_LAYOUT: int


class ToolTip(Object):
    """ This class holds information about a tooltip associated with a window
(see Window.SetToolTip()).
    """
    def __init__(self, tip: str) -> None:
        """ Constructor.
        """

    @staticmethod
    def Enable(flag: bool) -> None:
        """ Enable or disable tooltips globally.
        """

    def GetTip(self) -> str:
        """ Get the tooltip text.
        """

    def GetWindow(self) -> 'Window':
        """ Get the associated window.
        """

    @staticmethod
    def SetAutoPop(msecs: int) -> None:
        """ Set the delay after which the tooltip disappears or how long a tooltip remains visible.
        """

    @staticmethod
    def SetDelay(msecs: int) -> None:
        """ Set the delay after which the tooltip appears.
        """

    @staticmethod
    def SetMaxWidth(width: int) -> None:
        """ Set tooltip maximal width in pixels.
        """

    @staticmethod
    def SetReshow(msecs: int) -> None:
        """ Set the delay between subsequent tooltips to appear.
        """

    def SetTip(self, tip: str) -> None:
        """ Set the tooltip text.
        """



class TopLevelWindow(NonOwnedWindow):
    """ TopLevelWindow is a common base class for Dialog and Frame.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def CanSetTransparent(self) -> bool:
        """ Returns True if the platform supports making the window translucent.
        """

    def CenterOnScreen(self, direction: int=BOTH) -> None:
        """ A synonym for CentreOnScreen .
        """

    def CentreOnScreen(self, direction: int=BOTH) -> None:
        """ Centres the window on screen.
        """

    def Create(self, parent, id=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE, name=FrameNameStr) -> bool:
        """ Creates the top level window.
        """

    def EnableCloseButton(self, enable: bool=True) -> bool:
        """ Enables or disables the Close button (most often in the right upper corner of a dialog) and the Close entry of the system menu (most often in the left upper corner of the dialog).
        """

    def EnableFullScreenView(self, enable=True, style=FULLSCREEN_ALL) -> bool:
        """ Enables the zoom button to toggle full screen mode.
        """

    def EnableMaximizeButton(self, enable: bool=True) -> bool:
        """ Enables or disables the Maximize button (in the right or left upper corner of a frame or dialog).
        """

    def EnableMinimizeButton(self, enable: bool=True) -> bool:
        """ Enables or disables the Minimize button (in the right or left upper corner of a frame or dialog).
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetContentProtection(self) -> 'ContentProtection':
        """ Get the current content protection of the window.
        """

    def GetDefaultItem(self) -> 'Window':
        """ Returns a pointer to the button which is the default for this window, or
        """

    @staticmethod
    def GetDefaultSize() -> 'Size':
        """ Get the default size for a new top level window.
        """

    def GetIcon(self) -> 'Icon':
        """ Returns the standard icon of the window.
        """

    def GetIcons(self) -> 'IconBundle':
        """ Returns all icons associated with the window, there will be none of them if neither SetIcon   nor SetIcons   had been called before.
        """

    def GetTitle(self) -> str:
        """ Gets a string containing the window title.
        """

    def GetTmpDefaultItem(self) -> 'Window':
        """ wx.Window
        """

    def Iconize(self, iconize: bool=True) -> None:
        """ Iconizes or restores the window.
        """

    def IsActive(self) -> bool:
        """ Returns True if this window is currently active, i.e. if the user is currently working with it.
        """

    def IsAlwaysMaximized(self) -> bool:
        """ Returns True if this window is expected to be always maximized, either due to platform policy or due to local policy regarding particular class.
        """

    def IsFullScreen(self) -> bool:
        """ Returns True if the window is in fullscreen mode.
        """

    def IsIconized(self) -> bool:
        """ Returns True if the window is iconized.
        """

    def IsMaximized(self) -> bool:
        """ Returns True if the window is maximized.
        """

    def Layout(self) -> bool:
        """ Lays out the children using the window sizer or resizes the only child of the window to cover its entire area.
        """

    def MacGetMetalAppearance(self) -> bool:
        """ bool
        """

    def MacGetTopLevelWindowRef(self) -> None:
        """ 
        """

    def MacGetUnifiedAppearance(self) -> bool:
        """ bool
        """

    def MacSetMetalAppearance(self, on) -> None:
        """ 
        """

    def Maximize(self, maximize: bool=True) -> None:
        """ Maximizes or restores the window.
        """

    def OSXIsModified(self) -> bool:
        """ Returns the current modified state of the   wx.TopLevelWindow  on macOS.
        """

    def OSXSetModified(self, modified: bool) -> None:
        """ This function sets the   wx.TopLevelWindowâs modified state on macOS, which currently draws a black dot in the   wx.TopLevelWindowâs close button.
        """

    def RequestUserAttention(self, flags: int=USER_ATTENTION_INFO) -> None:
        """ Use a system-dependent way to attract users attention to the window when it is in background.
        """

    def Restore(self) -> None:
        """ Restore a previously iconized or maximized window to its normal state.
        """

    def RestoreToGeometry(self, ser: 'TopLevelWindow.GeometrySerializer') -> bool:
        """ Restores the window to the previously saved geometry.
        """

    def SaveGeometry(self, ser: 'TopLevelWindow.GeometrySerializer') -> bool:
        """ Save the current window geometry to allow restoring it later.
        """

    def SetContentProtection(self, contentProtection: ContentProtection) -> bool:
        """ Set content protection for the window.
        """

    def SetDefaultItem(self, win: 'Window') -> 'Window':
        """ Changes the default item for the panel, usually win  is a button.
        """

    def SetIcon(self, icon: 'Icon') -> None:
        """ Sets the icon for this window.
        """

    def SetIcons(self, icons: 'IconBundle') -> None:
        """ Sets several icons of different sizes for this window: this allows using different icons for different situations (e.g.
        """

    def SetMaxSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ A simpler interface for setting the size hints than SetSizeHints .
        """

    def SetMinSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ A simpler interface for setting the size hints than SetSizeHints .
        """

    def SetRepresentedFilename(self, filename: str) -> None:
        """ Sets the file name represented by this   wx.TopLevelWindow.
        """

    def SetSizeHints(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetTitle(self, title: str) -> None:
        """ Sets the window title.
        """

    def SetTmpDefaultItem(self, win: 'Window') -> 'Window':
        """ win (wx.Window) â
        """

    def SetTransparent(self, alpha: 'Byte') -> bool:
        """ If the platform supports it will set the window to be translucent.
        """

    def ShouldPreventAppExit(self) -> bool:
        """ This virtual function is not meant to be called directly but can be overridden to return False (it returns True by default) to allow the application to close even if this, presumably not very important, window is still opened.
        """

    def ShowFullScreen(self, show, style=FULLSCREEN_ALL) -> bool:
        """ Depending on the value of show  parameter the window is either shown full screen or restored to its normal state.
        """

    def ShowWithoutActivating(self) -> None:
        """ Show the   wx.TopLevelWindow, but do not give it keyboard focus.
        """

EVT_MAXIMIZE: int  #  Process a  wxEVT_MAXIMIZE   event. See    wx.MaximizeEvent.
EVT_MOVE: int  #  Process a  wxEVT_MOVE   event, which is generated when a window is moved. See    wx.MoveEvent.
EVT_MOVE_START: int  #  Process a  wxEVT_MOVE_START   event, which is generated when the user starts to move or size a window. wxMSW only. See    wx.MoveEvent.
EVT_MOVE_END: int  #  Process a  wxEVT_MOVE_END   event, which is generated when the user stops moving or sizing a window. wxMSW only. See    wx.MoveEvent.
EVT_SHOW: int  #  Process a  wxEVT_SHOW   event. See    wx.ShowEvent.
EVT_FULLSCREEN: int  #  Process a  wxEVT_FULLSCREEN   event. See    wx.FullScreenEvent. ^^
MAXIMIZE_BOX: int
MINIMIZE_BOX: int


class Trackable:
    """ Add-on base class for a trackable object.
    """


class Translations:
    """ This class allows getting translations for strings.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def AddCatalog(self, domain, msgIdLanguage=LANGUAGE_ENGLISH_US) -> bool:
        """ Add a catalog for use with the current locale.
        """

    def AddStdCatalog(self) -> bool:
        """ Add standard wxWidgets catalogs (âwxstdâ and possible port-specific catalogs).
        """

    @staticmethod
    def Get() -> 'Translations':
        """ Returns current translations object, may return None.
        """

    def GetAvailableTranslations(self, domain: str) -> list[str]:
        """ Returns list of all translations of domain  that were found.
        """

    def GetBestTranslation(self, *args, **kw) -> None:
        """ Returns the best UI language for the domain.
        """

    def GetHeaderValue(self, header, domain="") -> str:
        """ Returns the header value for header header.
        """

    def GetTranslatedString(self, *args, **kw) -> str:
        """ Overloaded Implementations:
        """

    def IsLoaded(self, domain: str) -> bool:
        """ Check if the given catalog is loaded, and returns True if it is.
        """

    @staticmethod
    def Set(t: 'Translations') -> None:
        """ Sets current translations object.
        """

    def SetLanguage(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def SetLoader(self, loader: 'TranslationsLoader') -> None:
        """ Changes loader use to read catalogs to a non-default one.
        """

LANGUAGE_DEFAULT: int
LANGUAGE_DEFAULT: int


class TreeCtrl(Control, WithImages):
    """ A tree control presents information as a hierarchy, with items that
may be expanded to show further items.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def AddRoot(self, text, image=-1, selImage=-1, data=None) -> 'TreeItemId':
        """ Adds the root node to the tree, returning the new item.
        """

    def AppendItem(self, parent, text, image=-1, selImage=-1, data=None) -> 'TreeItemId':
        """ Appends an item to the end of the branch identified by parent, return a new item id.
        """

    def AssignStateImageList(self, imageList: 'ImageList') -> None:
        """ Sets the state image list.
        """

    def ClearFocusedItem(self) -> None:
        """ Clears the currently focused item.
        """

    def Collapse(self, item: 'TreeItemId') -> None:
        """ Collapses the given item.
        """

    def CollapseAll(self) -> None:
        """ Collapses the root item.
        """

    def CollapseAllChildren(self, item: 'TreeItemId') -> None:
        """ Collapses this item and all of its children, recursively.
        """

    def CollapseAndReset(self, item: 'TreeItemId') -> None:
        """ Collapses the given item and removes all children.
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=TR_DEFAULT_STYLE, validator=DefaultValidator, name=TreeCtrlNameStr) -> bool:
        """ Creates the tree control.
        """

    def Delete(self, item: 'TreeItemId') -> None:
        """ Deletes the specified item.
        """

    def DeleteAllItems(self) -> None:
        """ Deletes all items in the control.
        """

    def DeleteChildren(self, item: 'TreeItemId') -> None:
        """ Deletes all children of the given item (but not the item itself).
        """

    def EditLabel(self, item: 'TreeItemId') -> 'TextCtrl':
        """ Starts editing the label of the given item.
        """

    def EnableBellOnNoMatch(self, on: bool=True) -> None:
        """ Enable or disable a beep if there is no match for the currently entered text when searching for the item from keyboard.
        """

    def EnableSystemTheme(self, enable: bool=True) -> None:
        """ Can be used to disable the system theme of controls using it by default.
        """

    def EndEditLabel(self, item, discardChanges=False) -> None:
        """ Ends label editing.
        """

    def EnsureVisible(self, item: 'TreeItemId') -> None:
        """ Scrolls and/or expands items to ensure that the given item is visible.
        """

    def Expand(self, item: 'TreeItemId') -> None:
        """ Expands the given item.
        """

    def ExpandAll(self) -> None:
        """ Expands all items in the tree.
        """

    def ExpandAllChildren(self, item: 'TreeItemId') -> None:
        """ Expands the given item and all its children recursively.
        """

    def GetBoundingRect(self, item, textOnly=False) -> Any:
        """ Returns the rectangle bounding the item. If textOnly is True,
only the rectangle around the itemâs label will be returned, otherwise
the itemâs image is also taken into account. The return value may be None
if the rectangle was not successfully retrieved, such as if the item is
currently not visible.
        """

    def GetChildrenCount(self, item, recursively=True) -> int:
        """ Returns the number of items in the branch.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetCount(self) -> int:
        """ Returns the number of items in the control.
        """

    def GetEditControl(self) -> 'TextCtrl':
        """ Returns the edit control being currently used to edit a label.
        """

    def GetFirstChild(self, item) -> None:
        """ Returns the first child; call GetNextChild   for the next child.
        """

    def GetFirstVisibleItem(self) -> 'TreeItemId':
        """ Returns the first visible item.
        """

    def GetFocusedItem(self) -> 'TreeItemId':
        """ Returns the item last clicked or otherwise selected.
        """

    def GetIndent(self) -> int:
        """ Returns the current tree control indentation.
        """

    def GetItemBackgroundColour(self, item: 'TreeItemId') -> 'Colour':
        """ Returns the background colour of the item.
        """

    def GetItemData(self, item) -> None:
        """ Returns the tree item data associated with the item.
        """

    def GetItemFont(self, item: 'TreeItemId') -> 'Font':
        """ Returns the font of the item label.
        """

    def GetItemImage(self, item, which=TreeItemIcon_Normal) -> int:
        """ Gets the specified item image.
        """

    def GetItemParent(self, item: 'TreeItemId') -> 'TreeItemId':
        """ Returns the itemâs parent.
        """

    def GetItemState(self, item: 'TreeItemId') -> int:
        """ Gets the specified item state.
        """

    def GetItemText(self, item: 'TreeItemId') -> str:
        """ Returns the item label.
        """

    def GetItemTextColour(self, item: 'TreeItemId') -> 'Colour':
        """ Returns the colour of the item label.
        """

    def GetLastChild(self, item: 'TreeItemId') -> 'TreeItemId':
        """ Returns the last child of the item (or an invalid tree item if this item has no children).
        """

    def GetNextChild(self, item, cookie) -> None:
        """ Returns the next child; call GetFirstChild   for the first child.
        """

    def GetNextSibling(self, item: 'TreeItemId') -> 'TreeItemId':
        """ Returns the next sibling of the specified item; call GetPrevSibling   for the previous sibling.
        """

    def GetNextVisible(self, item: 'TreeItemId') -> 'TreeItemId':
        """ Returns the next visible item or an invalid item if this item is the last visible one.
        """

    def GetPrevSibling(self, item: 'TreeItemId') -> 'TreeItemId':
        """ Returns the previous sibling of the specified item; call GetNextSibling   for the next sibling.
        """

    def GetPrevVisible(self, item: 'TreeItemId') -> 'TreeItemId':
        """ Returns the previous visible item or an invalid item if this item is the first visible one.
        """

    def GetQuickBestSize(self) -> bool:
        """ Returns True if the control will use a quick calculation for the best size, looking only at the first and last items.
        """

    def GetRootItem(self) -> 'TreeItemId':
        """ Returns the root item for the tree control.
        """

    def GetSelection(self) -> 'TreeItemId':
        """ Returns the selection, or an invalid item if there is no selection.
        """

    def GetSelections(self) -> Any:
        """ Returns a list of currently selected items in the tree.  This function can be called only if the control has the wx.``wx.TR_MULTIPLE`` style.
        """

    def GetSpacing(self) -> int:
        """ Returns the current tree control spacing.
        """

    def GetStateImageList(self) -> 'ImageList':
        """ Returns the state image list (from which application-defined state images are taken).
        """

    def HitTest(self, point, flags) -> None:
        """ Calculates which (if any) item is under the given point, returning the tree item id at this point plus extra information flags.
        """

    def InsertItem(self, *args, **kw) -> 'TreeItemId':
        """ Overloaded Implementations:
        """

    def IsBold(self, item: 'TreeItemId') -> bool:
        """ Returns True if the given item is in bold state.
        """

    def IsEmpty(self) -> bool:
        """ Returns True if the control is empty (i.e. has no items, even no root one).
        """

    def IsExpanded(self, item: 'TreeItemId') -> bool:
        """ Returns True if the item is expanded (only makes sense if it has children).
        """

    def IsSelected(self, item: 'TreeItemId') -> bool:
        """ Returns True if the item is selected.
        """

    def IsVisible(self, item: 'TreeItemId') -> bool:
        """ Returns True if the item is visible on the screen.
        """

    def ItemHasChildren(self, item: 'TreeItemId') -> bool:
        """ Returns True if the item has children.
        """

    def OnCompareItems(self, item1, item2) -> int:
        """ Override this function in the derived class to change the sort order of the items in the tree control.
        """

    def PrependItem(self, parent, text, image=-1, selImage=-1, data=None) -> 'TreeItemId':
        """ Appends an item as the first child of parent, return a new item id.
        """

    def ScrollTo(self, item: 'TreeItemId') -> None:
        """ Scrolls the specified item into view.
        """

    def SelectChildren(self, parent: 'TreeItemId') -> None:
        """ Select all the immediate children of the given parent.
        """

    def SelectItem(self, item, select=True) -> None:
        """ Selects the given item.
        """

    def SetFocusedItem(self, item: 'TreeItemId') -> None:
        """ Sets the currently focused item.
        """

    def SetIndent(self, indent: int) -> None:
        """ Sets the indentation for the tree control.
        """

    def SetItemBackgroundColour(self, item, col) -> None:
        """ Sets the colour of the itemâs background.
        """

    def SetItemBold(self, item, bold=True) -> None:
        """ Makes item appear in bold font if bold  parameter is True or resets it to the normal state.
        """

    def SetItemData(self, item, data) -> None:
        """ Sets the item client data.
        """

    def SetItemDropHighlight(self, item, highlight=True) -> None:
        """ Gives the item the visual feedback for DragânâDrop actions, which is useful if something is dragged from the outside onto the tree control (as opposed to a DnD operation within the tree control, which already is implemented internally).
        """

    def SetItemFont(self, item, font) -> None:
        """ Sets the itemâs font.
        """

    def SetItemHasChildren(self, item, hasChildren=True) -> None:
        """ Force appearance of the button next to the item.
        """

    def SetItemImage(self, item, image, which=TreeItemIcon_Normal) -> None:
        """ Sets the specified itemâs image.
        """

    def SetItemState(self, item, state) -> None:
        """ Sets the specified item state.
        """

    def SetItemText(self, item, text) -> None:
        """ Sets the item label.
        """

    def SetItemTextColour(self, item, col) -> None:
        """ Sets the colour of the itemâs text.
        """

    def SetQuickBestSize(self, quickBestSize: bool) -> None:
        """ If True is passed, specifies that the control will use a quick calculation for the best size, looking only at the first and last items.
        """

    def SetSpacing(self, spacing: int) -> None:
        """ Sets the spacing for the tree control.
        """

    def SetStateImageList(self, imageList: 'ImageList') -> None:
        """ Sets the state image list (from which application-defined state images are taken).
        """

    def SetWindowStyle(self, styles: int) -> None:
        """ Sets the mode flags associated with the display of the tree control.
        """

    def SortChildren(self, item: 'TreeItemId') -> None:
        """ Sorts the children of the given item using OnCompareItems .
        """

    def Toggle(self, item: 'TreeItemId') -> None:
        """ Toggles the given item between collapsed and expanded states.
        """

    def ToggleItemSelection(self, item: 'TreeItemId') -> None:
        """ Toggles the given item between selected and unselected states.
        """

    def Unselect(self) -> None:
        """ Removes the selection from the currently selected item (if any).
        """

    def UnselectAll(self) -> None:
        """ This function either behaves the same as Unselect   if the control doesnât have  TR_MULTIPLE   style, or removes the selection from all items if it does have this style.
        """

    def UnselectItem(self, item: 'TreeItemId') -> None:
        """ Unselects the given item.
        """

TR_EDIT_LABELS: int  #  Use this style if you wish the user to be able to edit labels in the tree control.
TR_NO_BUTTONS: int  #  For convenience to document that no buttons are to be drawn.
TR_HAS_BUTTONS: int  #  Use this style to show + and - buttons to the left of parent items.
TR_TWIST_BUTTONS: int  #  Selects alternative style of  +/ -   buttons  and shows rotating (âtwistingâ) arrows instead. Currently this style is only implemented under Microsoft Windows Vista and later Windows versions and is ignored under the other platforms as enabling it is equivalent to using  SystemThemedControl.EnableSystemTheme .
TR_NO_LINES: int  #  Use this style to hide vertical level connectors.
TR_FULL_ROW_HIGHLIGHT: int  #  Use this style to have the background colour and the selection highlight extend over the entire horizontal row of the tree control window. (This flag is ignored under Windows unless you specify  TR_NO_LINES   as well.)
TR_LINES_AT_ROOT: int  #  Use this style to show lines leading to the root nodes (unless no  TR_NO_LINES   is also used, in which case no lines are shown). Note that in the MSW version, if this style is omitted, not only the lines, but also the button used for expanding the root item is not shown, which can be unexpected, so it is recommended to always use it.
TR_HIDE_ROOT: int  #  Use this style to suppress the display of the root node, effectively causing the first-level nodes to appear as a series of root nodes.
TR_ROW_LINES: int  #  Use this style to draw a contrasting border between displayed rows.
TR_HAS_VARIABLE_ROW_HEIGHT: int  #  Use this style to cause row heights to be just big enough to fit the content. If not set, all rows use the largest row height. The default is that this flag is unset. Generic only.
TR_SINGLE: int  #  For convenience to document that only one item may be selected at a time. Selecting another item causes the current selection, if any, to be deselected. This is the default.
TR_MULTIPLE: int  #  Use this style to allow a range of items to be selected. If a second range is selected, the current range, if any, is deselected.
TR_DEFAULT_STYLE: int  #  The set of flags that are closest to the defaults for the native control for a particular toolkit. ^^
EVT_TREE_BEGIN_DRAG: int  #  Begin dragging with the left mouse button. If you want to enable left-dragging you need to intercept this event and explicitly call wx.TreeEvent.Allow , as itâs vetoed by default. Processes a  wxEVT_TREE_BEGIN_DRAG   event type.
EVT_TREE_BEGIN_RDRAG: int  #  Begin dragging with the right mouse button. If you want to enable right-dragging you need to intercept this event and explicitly call wx.TreeEvent.Allow , as itâs vetoed by default. Processes a  wxEVT_TREE_BEGIN_RDRAG   event type.
EVT_TREE_END_DRAG: int  #  End dragging with the left or right mouse button. Processes a  wxEVT_TREE_END_DRAG   event type.
EVT_TREE_BEGIN_LABEL_EDIT: int  #  Begin editing a label. This can be prevented by calling Veto(). Processes a  wxEVT_TREE_BEGIN_LABEL_EDIT   event type.
EVT_TREE_END_LABEL_EDIT: int  #  Finish editing a label. This can be prevented by calling Veto(). Processes a  wxEVT_TREE_END_LABEL_EDIT   event type.
EVT_TREE_DELETE_ITEM: int  #  An item was deleted. Processes a  wxEVT_TREE_DELETE_ITEM   event type.
EVT_TREE_GET_INFO: int  #  Request information from the application. Processes a  wxEVT_TREE_GET_INFO   event type.
EVT_TREE_SET_INFO: int  #  Information is being supplied. Processes a  wxEVT_TREE_SET_INFO   event type.
EVT_TREE_ITEM_ACTIVATED: int  #  The item has been activated, i.e. chosen by double clicking it with mouse or from keyboard. Processes a  wxEVT_TREE_ITEM_ACTIVATED   event type.
EVT_TREE_ITEM_COLLAPSED: int  #  The item has been collapsed. Processes a  wxEVT_TREE_ITEM_COLLAPSED   event type.
EVT_TREE_ITEM_COLLAPSING: int  #  The item is being collapsed. This can be prevented by calling Veto(). Processes a  wxEVT_TREE_ITEM_COLLAPSING   event type.
EVT_TREE_ITEM_EXPANDED: int  #  The item has been expanded. Processes a  wxEVT_TREE_ITEM_EXPANDED   event type.
EVT_TREE_ITEM_EXPANDING: int  #  The item is being expanded. This can be prevented by calling Veto(). Processes a  wxEVT_TREE_ITEM_EXPANDING   event type.
EVT_TREE_ITEM_RIGHT_CLICK: int  #  The user has clicked the item with the right mouse button. Processes a  wxEVT_TREE_ITEM_RIGHT_CLICK   event type.
EVT_TREE_ITEM_MIDDLE_CLICK: int  #  The user has clicked the item with the middle mouse button. This is only supported by the generic control. Processes a  wxEVT_TREE_ITEM_MIDDLE_CLICK   event type.
EVT_TREE_SEL_CHANGED: int  #  Selection has changed. Processes a  wxEVT_TREE_SEL_CHANGED   event type.
EVT_TREE_SEL_CHANGING: int  #  Selection is changing. This can be prevented by calling Veto(). Processes a  wxEVT_TREE_SEL_CHANGING   event type.
EVT_TREE_KEY_DOWN: int  #  A key has been pressed. Processes a  wxEVT_TREE_KEY_DOWN   event type.
EVT_TREE_ITEM_GETTOOLTIP: int  #  The opportunity to set the item tooltip is being given to the application (call wx.TreeEvent.SetToolTip ). Windows only. Processes a  wxEVT_TREE_ITEM_GETTOOLTIP   event type.
EVT_TREE_ITEM_MENU: int  #  The context menu for the selected item has been requested, either by a right click or by using the menu key. Notice that these events always carry a valid tree item and so are not generated when (right) clicking outside of the items area. If you need to handle such events, consider using  wxEVT_CONTEXT_MENU   instead. Processes a   wxEVT_TREE_ITEM_MENU   event type.
EVT_TREE_STATE_IMAGE_CLICK: int  #  The state image has been clicked. Processes a  wxEVT_TREE_STATE_IMAGE_CLICK   event type. ^^
TR_EDIT_LABELS: int
TR_NO_BUTTONS: int
TR_HAS_BUTTONS: int
TR_TWIST_BUTTONS: int
TR_NO_LINES: int
TR_FULL_ROW_HIGHLIGHT: int
TR_LINES_AT_ROOT: int
TR_HIDE_ROOT: int
TR_ROW_LINES: int
TR_HAS_VARIABLE_ROW_HEIGHT: int
TR_SINGLE: int
TR_MULTIPLE: int
TR_DEFAULT_STYLE: int
TR_HIDE_ROOT: int


class TreeEvent(NotifyEvent):
    """ A tree event holds information about events associated with TreeCtrl
objects.
    """
EVT_TREE_BEGIN_DRAG: int  #  Begin dragging with the left mouse button. If you want to enable left-dragging you need to intercept this event and explicitly call wx.TreeEvent.Allow , as itâs vetoed by default. Also notice that the control must have an associated image list (see SetImageList()) to drag its items under MSW.
EVT_TREE_BEGIN_RDRAG: int  #  Begin dragging with the right mouse button. If you want to enable right-dragging you need to intercept this event and explicitly call wx.TreeEvent.Allow , as itâs vetoed by default.
EVT_TREE_END_DRAG: int  #  End dragging with the left or right mouse button.
EVT_TREE_BEGIN_LABEL_EDIT: int  #  Begin editing a label. This can be prevented by calling Veto
EVT_TREE_END_LABEL_EDIT: int  #  Finish editing a label. This can be prevented by calling Veto
EVT_TREE_DELETE_ITEM: int  #  Delete an item.
EVT_TREE_GET_INFO: int  #  Request information from the application.
EVT_TREE_SET_INFO: int  #  Information is being supplied.
EVT_TREE_ITEM_ACTIVATED: int  #  The item has been activated, i.e. chosen by double clicking it with mouse or from keyboard.
EVT_TREE_ITEM_COLLAPSED: int  #  The item has been collapsed.
EVT_TREE_ITEM_COLLAPSING: int  #  The item is being collapsed. This can be prevented by calling Veto
EVT_TREE_ITEM_EXPANDED: int  #  The item has been expanded.
EVT_TREE_ITEM_EXPANDING: int  #  The item is being expanded. This can be prevented by calling Veto
EVT_TREE_ITEM_RIGHT_CLICK: int  #  The user has clicked the item with the right mouse button.
EVT_TREE_ITEM_MIDDLE_CLICK: int  #  The user has clicked the item with the middle mouse button.
EVT_TREE_SEL_CHANGED: int  #  Selection has changed.
EVT_TREE_SEL_CHANGING: int  #  Selection is changing. This can be prevented by calling Veto
EVT_TREE_KEY_DOWN: int  #  A key has been pressed.
EVT_TREE_ITEM_GETTOOLTIP: int  #  The opportunity to set the item tooltip is being given to the application (call SetToolTip). Windows only.
EVT_TREE_ITEM_MENU: int  #  The context menu for the selected item has been requested, either by a right click or by using the menu key.
EVT_TREE_STATE_IMAGE_CLICK: int  #  The state image has been clicked. ^^


class TreeItemId:
    """ An opaque reference to a tree item.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetID(self) -> None:
        """ 
        """

    def IsOk(self) -> bool:
        """ Returns True if this instance is referencing a valid tree item.
        """

    def Unset(self) -> None:
        """ 
        """

    def __bool__(self) -> int:
        """ int
        """

    def __eq__(self, item: Any) -> bool:
        """ bool
        """

    def __hash__(self) -> None:
        """ 
        """

    def __ne__(self, item: Any) -> bool:
        """ bool
        """

    def __nonzero__(self) -> int:
        """ int
        """



class TwoFingerTapEvent(GestureEvent):
    """ This event is generated when two fingers touch the surface at the same
time.
    """
    def __init__(self, windid: int=0) -> None:
        """ Constructor.
        """

EVT_TWO_FINGER_TAP: int  #  Process a  wxEVT_TWO_FINGER_TAP . ^^


class UIActionSimulator:
    """ UIActionSimulator is a class used to simulate user interface actions
such as a mouse click or a key press.
    """
    def __init__(self) -> None:
        """ Default constructor.
        """

    def Char(self, keycode, modifiers=MOD_NONE) -> bool:
        """ Press and release a key.
        """

    def KeyDown(self, keycode, modifiers=MOD_NONE) -> bool:
        """ Press a key.
        """

    def KeyUp(self, keycode, modifiers=MOD_NONE) -> bool:
        """ Release a key.
        """

    def MouseClick(self, button: int=MOUSE_BTN_LEFT) -> bool:
        """ Click a mouse button.
        """

    def MouseDblClick(self, button: int=MOUSE_BTN_LEFT) -> bool:
        """ Double-click a mouse button.
        """

    def MouseDown(self, button: int=MOUSE_BTN_LEFT) -> bool:
        """ Press a mouse button.
        """

    def MouseDragDrop(self, x1, y1, x2, y2, button=MOUSE_BTN_LEFT) -> bool:
        """ Perform a drag and drop operation.
        """

    def MouseMove(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def MouseUp(self, button: int=MOUSE_BTN_LEFT) -> bool:
        """ Release a mouse button.
        """

    def Select(self, text: str) -> bool:
        """ Simulate selection of an item with the given text.
        """

    def Text(self, text: int) -> bool:
        """ Emulate typing in the keys representing the given string.
        """



class UniChar:
    """ This class represents a single Unicode character.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetAsChar(self, c: int) -> bool:
        """ Returns True if the character is representable as a single byte in the current locale encoding.
        """

    def GetValue(self) -> value_type:
        """ Returns Unicode code point value of the character.
        """

    def HighSurrogate(self, *args, **kw) -> 'Uint16':
        """ Overloaded Implementations:
        """

    def IsAscii(self) -> bool:
        """ Returns True if the character is an ASCII character (i.e. if its value is less than 128).
        """

    def IsBMP(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def IsSupplementary(self, *args, **kw) -> bool:
        """ Overloaded Implementations:
        """

    def LowSurrogate(self, *args, **kw) -> 'Uint16':
        """ Overloaded Implementations:
        """



class UpdateUIEvent(CommandEvent):
    """ This class is used for pseudo-events which are called by wxWidgets to
give an application the chance to update various user interface
elements.
    """
    def __init__(self, commandId: int=0) -> None:
        """ Constructor.
        """

    @staticmethod
    def CanUpdate(window: 'Window') -> bool:
        """ Returns True if it is appropriate to update (send UI update events to) this window.
        """

    def Check(self, check: bool) -> None:
        """ Check or uncheck the UI element.
        """

    def Enable(self, enable: bool) -> None:
        """ Enable or disable the UI element.
        """

    def GetChecked(self) -> bool:
        """ Returns True if the UI element should be checked.
        """

    def GetEnabled(self) -> bool:
        """ Returns True if the UI element should be enabled.
        """

    @staticmethod
    def GetMode() -> 'UpdateUIMode':
        """ Static function returning a value specifying how wxWidgets will send update events: to all windows, or only to those which specify that they will process the events.
        """

    def GetSetChecked(self) -> bool:
        """ Returns True if the application has called Check .
        """

    def GetSetEnabled(self) -> bool:
        """ Returns True if the application has called Enable .
        """

    def GetSetShown(self) -> bool:
        """ Returns True if the application has called Show .
        """

    def GetSetText(self) -> bool:
        """ Returns True if the application has called SetText .
        """

    def GetShown(self) -> bool:
        """ Returns True if the UI element should be shown.
        """

    def GetText(self) -> str:
        """ Returns the text that should be set for the UI element.
        """

    @staticmethod
    def GetUpdateInterval() -> int:
        """ Returns the current interval between updates in milliseconds.
        """

    def IsCheckable(self) -> bool:
        """ Returns True if the UI element can be checked.
        """

    @staticmethod
    def ResetUpdateTime() -> None:
        """ Used internally to reset the last-updated time to the current time.
        """

    @staticmethod
    def SetMode(mode: UpdateUIMode) -> None:
        """ Specify how wxWidgets will send update events: to all windows, or only to those which specify that they will process the events.
        """

    def SetText(self, text: str) -> None:
        """ Sets the text for this UI element.
        """

    @staticmethod
    def SetUpdateInterval(updateInterval: int) -> None:
        """ Sets the interval between updates in milliseconds.
        """

    def Show(self, show: bool) -> None:
        """ Show or hide the UI element.
        """

EVT_UPDATE_UI: int  #  Process a  wxEVT_UPDATE_UI   event for the command with the given id.
EVT_UPDATE_UI_RANGE: int  #  Process a  wxEVT_UPDATE_UI   event for any command with id included in the given range. ^^
UPDATE_UI_PROCESS_SPECIFIED: int
WS_EX_PROCESS_UI_UPDATES: int
WS_EX_PROCESS_UI_UPDATES: int
UPDATE_UI_PROCESS_ALL: int
UPDATE_UI_PROCESS_ALL: int


class URLDataObject(DataObject):
    """ URLDataObject is a DataObject containing an URL and can be used
e.g.
    """
    def __init__(self, url: str="") -> None:
        """ Constructor, may be used to initialize the URL.
        """

    def GetAllFormats(self, dir=DataObject.Get) -> None:
        """ Returns a list of wx.DataFormat objects which this data object
supports transferring in the given direction.
        """

    def GetURL(self) -> str:
        """ Returns the URL stored by this object, as a string.
        """

    def SetData(self, format, buf) -> bool:
        """ bool
        """

    def SetURL(self, url: str) -> None:
        """ Sets the URL stored by this object.
        """



class Validator(EvtHandler):
    """ Validator is the base class for a family of validator classes that
mediate between a class of control, and application data.
    """
    def __init__(self) -> None:
        """ Constructor.
        """

    def Clone(self) -> 'Window':
        """ All validator classes must implement the Clone   function, which returns an identical copy of itself.
        """

    def GetWindow(self) -> 'Window':
        """ Returns the window associated with the validator.
        """

    @staticmethod
    def IsSilent() -> bool:
        """ Returns if the error sound is currently disabled.
        """

    def SetWindow(self, window: 'Window') -> None:
        """ Associates a window with the validator.
        """

    @staticmethod
    def SuppressBellOnError(suppress: bool=True) -> None:
        """ This functions switches on or turns off the error sound produced by the validators if an invalid key is pressed.
        """

    def TransferFromWindow(self) -> bool:
        """ This overridable function is called when the value in the window must be transferred to the validator.
        """

    def TransferToWindow(self) -> bool:
        """ This overridable function is called when the value associated with the validator must be transferred to the window.
        """

    def Validate(self, parent: 'Window') -> bool:
        """ This overridable function is called when the value in the associated window must be validated.
        """



class VarHScrollHelper(VarScrollHelperBase):
    """ This class provides functions wrapping the VarScrollHelperBase
class, targeted for horizontal-specific scrolling.
    """
    def __init__(self, winToScroll: 'Window') -> None:
        """ Constructor taking the target window to be scrolled by this helper class.
        """

    def EstimateTotalWidth(self) -> 'Coord':
        """ This class forwards calls from EstimateTotalSize   to this function so derived classes can override either just the height or the width estimation, or just estimate both differently if desired in any   wx.HVScrolledWindow  derived class.
        """

    def GetColumnCount(self) -> int:
        """ Returns the number of columns the target window contains.
        """

    def GetVisibleColumnsBegin(self) -> int:
        """ Returns the index of the first visible column based on the scroll position.
        """

    def GetVisibleColumnsEnd(self) -> int:
        """ Returns the index of the last visible column based on the scroll position.
        """

    def IsColumnVisible(self, column: int) -> bool:
        """ Returns True if the given column is currently visible (even if only partially visible) or False otherwise.
        """

    def OnGetColumnWidth(self, column: int) -> 'Coord':
        """ This function must be overridden in the derived class, and should return the width of the given column in pixels.
        """

    def OnGetColumnsWidthHint(self, columnMin, columnMax) -> None:
        """ This function doesnât have to be overridden but it may be useful to do so if calculating the columnsâ sizes is a relatively expensive operation as it gives your code a chance to calculate several of them at once and cache the result if necessary.
        """

    def RefreshColumn(self, column: int) -> None:
        """ Triggers a refresh for just the given columnâs area of the window if itâs visible.
        """

    def RefreshColumns(self, from_, to_) -> None:
        """ Triggers a refresh for the area between the specified range of columns given (inclusively).
        """

    def ScrollColumnPages(self, pages: int) -> bool:
        """ Scroll by the specified number of pages which may be positive (to scroll right) or negative (to scroll left).
        """

    def ScrollColumns(self, columns: int) -> bool:
        """ Scroll by the specified number of columns which may be positive (to scroll right) or negative (to scroll left).
        """

    def ScrollToColumn(self, column: int) -> bool:
        """ Scroll to the specified column.
        """

    def SetColumnCount(self, columnCount: int) -> None:
        """ Set the number of columns the window contains.
        """



class VarScrollHelperBase:
    """ This class provides all common base functionality for scroll
calculations shared among all variable scrolled window implementations
as well as automatic scrollbar functionality, saved scroll positions,
controlling target windows to be scrolled, as well as defining all
required virtual functions that need to be implemented for any
orientation specific work.
    """
    def __init__(self, winToScroll: 'Window') -> None:
        """ Constructor taking the target window to be scrolled by this helper class.
        """

    def CalcScrolledPosition(self, coord: int) -> int:
        """ Translates the logical coordinate given to the current device coordinate.
        """

    def CalcUnscrolledPosition(self, coord: int) -> int:
        """ Translates the device coordinate given to the corresponding logical coordinate.
        """

    def EnablePhysicalScrolling(self, scrolling: bool=True) -> None:
        """ With physical scrolling on (when this is True), the device origin is changed properly when a   wx.PaintDC  is prepared, children are actually moved and laid out properly, and the contents of the window (pixels) are actually moved.
        """

    def EstimateTotalSize(self) -> 'Coord':
        """ When the number of scroll units change, we try to estimate the total size of all units when the full window size is needed (i.e.
        """

    def GetNonOrientationTargetSize(self) -> int:
        """ This function needs to be overridden in the in the derived class to return the window size with respect to the opposing orientation.
        """

    def GetOrientation(self) -> 'Orientation':
        """ This function need to be overridden to return the orientation that this helper is working with, either  HORIZONTAL   or   VERTICAL .
        """

    def GetOrientationTargetSize(self) -> int:
        """ This function needs to be overridden in the in the derived class to return the window size with respect to the orientation this helper is working with.
        """

    def GetTargetWindow(self) -> 'Window':
        """ This function will return the target window this helper class is currently scrolling.
        """

    def GetVisibleBegin(self) -> int:
        """ Returns the index of the first visible unit based on the scroll position.
        """

    def GetVisibleEnd(self) -> int:
        """ Returns the index of the last visible unit based on the scroll position.
        """

    def IsVisible(self, unit: int) -> bool:
        """ Returns True if the given scroll unit is currently visible (even if only partially visible) or False otherwise.
        """

    def OnGetUnitSize(self, unit: int) -> 'Coord':
        """ This function must be overridden in the derived class, and should return the size of the given unit in pixels.
        """

    def OnGetUnitsSizeHint(self, unitMin, unitMax) -> None:
        """ This function doesnât have to be overridden but it may be useful to do so if calculating the unitsâ sizes is a relatively expensive operation as it gives your code a chance to calculate several of them at once and cache the result if necessary.
        """

    def RefreshAll(self) -> None:
        """ Recalculate all parameters and repaint all units.
        """

    def SetTargetWindow(self, target: 'Window') -> None:
        """ Normally the window will scroll itself, but in some rare occasions you might want it to scroll (part of) another window (e.g.
        """

    def UpdateScrollbar(self) -> None:
        """ Update the thumb size shown by the scrollbar.
        """

    def VirtualHitTest(self, coord: int) -> int:
        """ Returns the virtual scroll unit under the device unit given accounting for scroll position or  NOT_FOUND   if none (i.e.
        """



class VarHVScrollHelper(VarVScrollHelper, VarHScrollHelper):
    """ This class provides functions wrapping the VarHScrollHelper and
VarVScrollHelper classes, targeted for scrolling a window in both
axis.
    """
    def __init__(self, winToScroll: 'Window') -> None:
        """ Constructor taking the target window to be scrolled by this helper class.
        """

    def EnablePhysicalScrolling(self, vscrolling=True, hscrolling=True) -> None:
        """ With physical scrolling on (when this is True), the device origin is changed properly when a   wx.PaintDC  is prepared, children are actually moved and laid out properly, and the contents of the window (pixels) are actually moved.
        """

    def GetRowColumnCount(self) -> 'Size':
        """ Returns the number of columns and rows the target window contains.
        """

    def GetVisibleBegin(self) -> 'Position':
        """ Returns the index of the first visible column and row based on the current scroll position.
        """

    def GetVisibleEnd(self) -> 'Position':
        """ Returns the index of the last visible column and row based on the scroll position.
        """

    def IsVisible(self, *args, **kw) -> bool:
        """ Returns True if both the given row and column are currently visible (even if only partially visible) or False otherwise.
        """

    def RefreshRowColumn(self, *args, **kw) -> None:
        """ Triggers a refresh for just the area shared between the given row and column of the window if it is visible.
        """

    def RefreshRowsColumns(self, *args, **kw) -> None:
        """ Triggers a refresh for the visible area shared between all given rows and columns (inclusive) of the window.
        """

    def ScrollToRowColumn(self, *args, **kw) -> bool:
        """ Scroll to the specified row and column.
        """

    def SetRowColumnCount(self, rowCount, columnCount) -> None:
        """ Set the number of rows and columns the target window will contain.
        """

    def VirtualHitTest(self, *args, **kw) -> 'Position':
        """ Returns the virtual scroll unit under the device unit given accounting for scroll position or  NOT_FOUND   (for the row, column, or possibly both values) if none.
        """



class VarVScrollHelper(VarScrollHelperBase):
    """ This class provides functions wrapping the VarScrollHelperBase
class, targeted for vertical-specific scrolling.
    """
    def __init__(self, winToScroll: 'Window') -> None:
        """ Constructor taking the target window to be scrolled by this helper class.
        """

    def EstimateTotalHeight(self) -> 'Coord':
        """ This class forwards calls from EstimateTotalSize   to this function so derived classes can override either just the height or the width estimation, or just estimate both differently if desired in any   wx.HVScrolledWindow  derived class.
        """

    def GetRowCount(self) -> int:
        """ Returns the number of rows the target window contains.
        """

    def GetVisibleRowsBegin(self) -> int:
        """ Returns the index of the first visible row based on the scroll position.
        """

    def GetVisibleRowsEnd(self) -> int:
        """ Returns the index of the last visible row based on the scroll position.
        """

    def IsRowVisible(self, row: int) -> bool:
        """ Returns True if the given row is currently visible (even if only partially visible) or False otherwise.
        """

    def OnGetRowHeight(self, row: int) -> 'Coord':
        """ This function must be overridden in the derived class, and should return the height of the given row in pixels.
        """

    def OnGetRowsHeightHint(self, rowMin, rowMax) -> None:
        """ This function doesnât have to be overridden but it may be useful to do so if calculating the rowsâ sizes is a relatively expensive operation as it gives your code a chance to calculate several of them at once and cache the result if necessary.
        """

    def RefreshRow(self, row: int) -> None:
        """ Triggers a refresh for just the given rowâs area of the window if itâs visible.
        """

    def RefreshRows(self, from_, to_) -> None:
        """ Triggers a refresh for the area between the specified range of rows given (inclusively).
        """

    def ScrollRowPages(self, pages: int) -> bool:
        """ Scroll by the specified number of pages which may be positive (to scroll down) or negative (to scroll up).
        """

    def ScrollRows(self, rows: int) -> bool:
        """ Scroll by the specified number of rows which may be positive (to scroll down) or negative (to scroll up).
        """

    def ScrollToRow(self, row: int) -> bool:
        """ Scroll to the specified row.
        """

    def SetRowCount(self, rowCount: int) -> None:
        """ Set the number of rows the window contains.
        """



class VersionInfo:
    """ VersionInfo contains version information.
    """
    def __init__(self, name="", major=0, minor=0, micro=0, revision=0, description="", copyright="") -> None:
        """ Constructor.
        """

    def GetCopyright(self) -> str:
        """ Get the copyright string.
        """

    def GetDescription(self) -> str:
        """ Get the description string.
        """

    def GetMajor(self) -> int:
        """ Get the major version number.
        """

    def GetMicro(self) -> int:
        """ Get the micro version, or release number.
        """

    def GetMinor(self) -> int:
        """ Get the minor version number.
        """

    def GetName(self) -> str:
        """ Get the name of the object (library).
        """

    def GetRevision(self) -> int:
        """ Get the revision version, or build number.
        """

    def GetVersionString(self) -> str:
        """ Get the string representation.
        """

    def HasCopyright(self) -> bool:
        """ Returns True if a copyright string has been specified.
        """

    def HasDescription(self) -> bool:
        """ Return True if a description string has been specified.
        """

    def ToString(self) -> str:
        """ Get the string representation of this version object.
        """



class VideoMode:
    """ Determines the sizes and locations of displays connected to the
system.
    """
    def __init__(self, width=0, height=0, depth=0, freq=0) -> None:
        """ Constructs this class using the given parameters.
        """

    def GetDepth(self) -> int:
        """ Returns bits per pixel (e.g. 32), 1 is monochrome and 0 means unspecified/known.
        """

    def GetHeight(self) -> int:
        """ Returns the screen height in pixels (e.g. 480), 0 means unspecified.
        """

    def GetWidth(self) -> int:
        """ Returns the screen width in pixels (e.g. 640), 0 means unspecified.
        """

    def IsOk(self) -> bool:
        """ Returns True if the object has been initialized.
        """

    def Matches(self, other: 'VideoMode') -> bool:
        """ Returns True if this mode matches the other one in the sense that all non zero fields of the other mode have the same value in this one (except for refresh which is allowed to have a greater value).
        """

    def __bool__(self) -> int:
        """ int
        """

    def __nonzero__(self) -> int:
        """ int
        """

    def __ne__(self, item: Any) -> bool:
        """ mode (wx.VideoMode) â
        """

    def __eq__(self, item: Any) -> bool:
        """ m (wx.VideoMode) â
        """



class VisualAttributes:
    """ Struct containing all the visual attributes of a control.
    """


class VListBox(VScrolledWindow):
    """ VListBox is a ListBox-like control with the following two main
differences from a regular ListBox: it can have an arbitrarily huge
number of items because it doesnât store them itself but uses the
OnDrawItem() callback to draw them (so it is a virtual listbox) and
its items can have variable height as determined by OnMeasureItem()
(so it is also a listbox with the lines of variable height).
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Clear(self) -> None:
        """ Deletes all items from the control.
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=VListBoxNameStr) -> bool:
        """ Creates the control.
        """

    def DeselectAll(self) -> bool:
        """ Deselects all the items in the listbox.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetFirstSelected(self) -> tuple:
        """ Returns the index of the first selected item in the listbox or  NOT_FOUND   if no items are currently selected.
        """

    def GetItemCount(self) -> int:
        """ Get the number of items in the control.
        """

    def GetItemRect(self, item: int) -> 'Rect':
        """ Returns the rectangle occupied by this item in physical coordinates.
        """

    def GetMargins(self) -> 'Point':
        """ Returns the margins used by the control.
        """

    def GetNextSelected(self, cookie: int) -> tuple:
        """ Returns the index of the next selected item or  NOT_FOUND   if there are no more.
        """

    def GetSelectedCount(self) -> int:
        """ Returns the number of the items currently selected.
        """

    def GetSelection(self) -> int:
        """ Get the currently selected item or  NOT_FOUND   if there is no selection.
        """

    def GetSelectionBackground(self) -> 'Colour':
        """ Returns the background colour used for the selected cells.
        """

    def HasMultipleSelection(self) -> bool:
        """ Returns True if the listbox was created with  LB_MULTIPLE   style and so supports multiple selection or False if it is a single selection listbox.
        """

    def IsCurrent(self, item: int) -> bool:
        """ Returns True if this item is the current one, False otherwise.
        """

    def IsSelected(self, item: int) -> bool:
        """ Returns True if this item is selected, False otherwise.
        """

    def OnDrawBackground(self, dc, rect, n) -> None:
        """ This method is used to draw the itemâs background and, maybe, a border around it.
        """

    def OnDrawItem(self, dc, rect, n) -> None:
        """ The derived class must implement this function to actually draw the item with the given index on the provided DC.
        """

    def OnDrawSeparator(self, dc, rect, n) -> None:
        """ This method may be used to draw separators between the lines.
        """

    def OnMeasureItem(self, n: int) -> 'Coord':
        """ The derived class must implement this method to return the height of the specified item (in pixels).
        """

    def Select(self, item, select=True) -> bool:
        """ Selects or deselects the specified item which must be valid (i.e. not equal to  NOT_FOUND ).
        """

    def SelectAll(self) -> bool:
        """ Selects all the items in the listbox.
        """

    def SelectRange(self, from_, to_) -> bool:
        """ Selects all items in the specified range which may be given in any order.
        """

    def SetItemCount(self, count: int) -> None:
        """ Set the number of items to be shown in the control.
        """

    def SetMargins(self, *args, **kw) -> None:
        """ Set the margins: horizontal margin is the distance between the window border and the item contents while vertical margin is half of the distance between items.
        """

    def SetSelection(self, selection: int) -> None:
        """ Set the selection to the specified item, if it is -1 the selection is unset.
        """

    def SetSelectionBackground(self, col: Union[int, str, 'Colour']) -> None:
        """ Sets the colour to be used for the selected cells background.
        """

    def Toggle(self, item: int) -> None:
        """ Toggles the state of the specified item, i.e. selects it if it was unselected and deselects it if it was selected.
        """



class VScrolledWindow(Panel, VarVScrollHelper):
    """ In the name of this class, âVâ may stand for âvariableâ because it can
be used for scrolling rows of variable heights; âvirtualâ, because it
is not necessary to know the heights of all rows in advance  only
those which are shown on the screen need to be measured; or even
âverticalâ, because this class only supports scrolling vertically.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=PanelNameStr) -> bool:
        """ Same as the non-default constructor, but returns a status code: True if ok, False if the window couldnât be created.
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â
        """

    def GetFirstVisibleLine(self) -> int:
        """ Deprecated compatibility helper.
        """

    def GetLastVisibleLine(self) -> int:
        """ Deprecated compatibility helper.
        """

    def GetLineCount(self) -> int:
        """ Deprecated compatibility helper.
        """

    def HitTest(self, *args) -> None:
        """ Deprecated compatibility helper.
        """

    def RefreshLine(self, line) -> None:
        """ Deprecated compatibility helper.
        """

    def RefreshLines(self, from_, to_) -> None:
        """ Deprecated compatibility helper.
        """

    def ScrollLines(self, lines) -> bool:
        """ Deprecated compatibility helper.
        """

    def ScrollPages(self, pages) -> bool:
        """ Deprecated compatibility helper.
        """

    def ScrollToLine(self, line) -> bool:
        """ Deprecated compatibility helper.
        """

    def SetLineCount(self, count) -> None:
        """ Deprecated compatibility helper.
        """

ID_ANY: int


class WindowBase:
    """ child (wx.WindowBase) â 
    """
    def AddChild(self, child: 'WindowBase') -> None:
        """ child (wx.WindowBase) â
        """

    def RemoveChild(self, child: 'WindowBase') -> None:
        """ child (wx.WindowBase) â
        """



class WindowCreateEvent(CommandEvent):
    """ This event is sent just after the actual window associated with a
Window object has been created.
    """
    def __init__(self, win: Optional['Window']=None) -> None:
        """ Constructor.
        """

    def GetWindow(self) -> 'Window':
        """ Return the window being created.
        """

EVT_WINDOW_CREATE: int  #  Process a  wxEVT_CREATE   event. ^^


class WindowDC(DC):
    """ A WindowDC must be constructed if an application wishes to paint on
the whole area of a window (client and decorations).
    """
    def __init__(self, window: 'Window') -> None:
        """ Constructor.
        """



class WindowDestroyEvent(CommandEvent):
    """ This event is sent as early as possible during the window destruction
process.
    """
    def __init__(self, win: Optional['Window']=None) -> None:
        """ Constructor.
        """

    def GetWindow(self) -> 'Window':
        """ Return the window being destroyed.
        """



class WindowDisabler:
    """ This class disables all top level windows of the application (maybe
with the exception of one of them) in its constructor and enables them
back in its destructor.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def __enter__(self) -> None:
        """ 
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 
        """

FRAME_TOOL_WINDOW: int
FRAME_NO_TASKBAR: int


class WindowIDRef:
    """ A WindowIDRef object wraps an ID value and marks it as being in-use
until all references to that ID are gone.
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:
        """

    def GetId(self) -> int:
        """ Alias for GetValue allowing the IDRef to be passed as the source parameter to wx.EvtHandler.Bind.
        """

    def GetValue(self) -> int:
        """ Get the ID value
        """

    def __eq__(self, item: Any) -> bool:
        """ bool
        """

    def __ge__(self, id) -> bool:
        """ bool
        """

    def __gt__(self, id) -> bool:
        """ bool
        """

    def __hash__(self) -> None:
        """ 
        """

    def __index__(self) -> int:
        """ See __int__
        """

    def __int__(self) -> int:
        """ Alias for GetValue allowing the IDRef to be passed as the WindowID parameter when creating widgets or other places an integer type is needed.
        """

    def __le__(self, id) -> bool:
        """ bool
        """

    def __lt__(self, id) -> bool:
        """ bool
        """

    def __ne__(self, item: Any) -> bool:
        """ bool
        """

    def __repr__(self) -> None:
        """ 
        """



class WindowModalDialogEvent(CommandEvent):
    """ Event sent by Dialog.ShowWindowModal() when the dialog closes.
    """
    def __init__(self, commandType=wxEVT_NULL, id=0) -> None:
        """ Constructor.
        """

    def Clone(self) -> 'Event':
        """ Clone the event.
        """

    def GetDialog(self) -> 'Dialog':
        """ Return the corresponding dialog.
        """

    def GetReturnCode(self) -> int:
        """ Return the dialogâs return code.
        """



class WithImages:
    """ A mixin class to be used with other classes that use a ImageList.
    """
    def __init__(self) -> None:
        """ 
        """

    def AssignImageList(self, imageList: 'ImageList') -> None:
        """ Sets the image list for the page control and takes ownership of the list.
        """

    def GetImageCount(self) -> int:
        """ Return the number of images in this control.
        """

    def GetImageList(self) -> 'ImageList':
        """ Returns the associated image list, may be None.
        """

    def GetUpdatedImageListFor(self, win: 'Window') -> 'ImageList':
        """ Returns the image list updated to reflect the DPI scaling used for the given window if possible.
        """

    def HasImages(self) -> bool:
        """ Return True if the control has any images associated with it.
        """

    def SetImageList(self, imageList: 'ImageList') -> None:
        """ Sets the image list to use.
        """

    def SetImages(self, images: Vector) -> None:
        """ Set the images to use for the items in the control.
        """

NO_IMAGE: int


class WrapSizer(BoxSizer):
    """ A wrap sizer lays out its items in a single line, like a box sizer  as
long as there is space available in that direction.
    """
    def __init__(self, orient=HORIZONTAL, flags=WRAPSIZER_DEFAULT_FLAGS) -> None:
        """ Constructor for a   wx.WrapSizer.
        """

    def CalcMin(self) -> 'Size':
        """ Implements the calculation of a box sizerâs minimal.
        """

    def InformFirstDirection(self, direction, size, availableOtherDir) -> bool:
        """ Not used by an application.
        """

    def IsSpaceItem(self, item: 'SizerItem') -> bool:
        """ Can be overridden in the derived classes to treat some normal items as spacers.
        """

    def RepositionChildren(self, minSize: Union[tuple[int, int], 'Size']) -> None:
        """ Method which must be overridden in the derived sizer classes.
        """



class XPMHandler(ImageHandler):
    """ This is the image handler for the XPM format.
    """
    def __init__(self) -> None:
        """ Default constructor for   wx.XPMHandler.
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ Called to test if this handler can read an image from the given stream.
        """

    def LoadFile(self, image, stream, verbose=True, index=-1) -> bool:
        """ Loads an image from a stream, putting the resulting data into image.
        """

    def SaveFile(self, image, stream, verbose=True) -> bool:
        """ Saves an image in the output stream.
        """



class ZoomGestureEvent(GestureEvent):
    """ This event is generated when two fingers pinch the surface to zoom in
or out.
    """
    def __init__(self, windid: int=0) -> None:
        """ Constructor.
        """

    def GetZoomFactor(self) -> float:
        """ Returns the zoom Factor since the gesture started.
        """

    def SetZoomFactor(self, zoomFactor: float) -> None:
        """ Sets the zoom Factor.
        """

EVT_GESTURE_ZOOM: int  #  Process a  wxEVT_GESTURE_ZOOM . ^^


