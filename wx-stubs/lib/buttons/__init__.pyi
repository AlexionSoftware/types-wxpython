# -*- coding: utf-8 -*-
from typing import Any, Optional, Union

class __ThemedMixin:
    """ Uses the native renderer to draw the bezel, also handle mouse-overs.
    """
    def DrawBezel(self, dc, x1, y1, x2, y2) -> None:
        """ 
        """

    def InitOtherEvents(self) -> None:
        """ Initializes other events needed for themed buttons.
        """

    def OnMouse(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_ENTER_WINDOW and wx.EVT_LEAVE_WINDOW events for
GenButton when used as a themed button.
        """

EVT_ENTER_WINDOW: int
EVT_LEAVE_WINDOW: int
EVT_ENTER_WINDOW: int
EVT_LEAVE_WINDOW: int


class __ToggleMixin:
    """ A mixin that allows to transform GenButton in the corresponding
toggle button.
    """
    def GetToggle(self) -> None:
        """ Returns the toggled state of a button.
        """

    def OnKeyDown(self, event: 'KeyEvent') -> None:
        """ Handles the wx.EVT_KEY_DOWN event for GenButton when used as toggle button.
        """

    def OnKeyUp(self, event: 'KeyEvent') -> None:
        """ Handles the wx.EVT_KEY_UP event for GenButton when used as toggle button.
        """

    def OnLeftDown(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_LEFT_DOWN event for GenButton when used as toggle button.
        """

    def OnLeftUp(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_LEFT_UP event for GenButton when used as toggle button.
        """

    def OnMotion(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_MOTION event for GenButton when used as toggle button.
        """

    def SetToggle(self, flag: bool) -> None:
        """ Sets the button as toggled/not toggled.
        """

EVT_KEY_DOWN: int
EVT_KEY_UP: int
EVT_LEFT_DOWN: int
EVT_LEFT_UP: int
EVT_MOTION: int
EVT_KEY_DOWN: int
EVT_KEY_UP: int
EVT_LEFT_DOWN: int
EVT_LEFT_UP: int
EVT_MOTION: int


class GenButton(Control):
    """ A generic button, and base class for the other generic buttons.
    """
    def __init__(self, parent, id=-1, label='', pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, validator = wx.DefaultValidator, name = "genbutton") -> None:
        """ Default class constructor.
        """

    def AcceptsFocus(self) -> None:
        """ Can this window be given focus by mouse click?
        """

    def DoGetBestSize(self) -> None:
        """ Overridden base class virtual. Determines the best size of the
button based on the label and bezel size.
        """

    def DrawBezel(self, dc, x1, y1, x2, y2) -> None:
        """ 
        """

    def DrawFocusIndicator(self, dc, w, h) -> None:
        """ 
        """

    def DrawLabel(self, dc, width, height, dx=0, dy=0) -> None:
        """ 
        """

    def Enable(self, enable: bool=True) -> None:
        """ Enables/disables the button.
        """

    def GetBackgroundBrush(self, dc: 'DC') -> None:
        """ Returns the current wx.Brush to be used to draw the button background.
        """

    def GetBezelWidth(self) -> integer:
        """ Returns the width of the 3D effect, in pixels.
        """

    def GetDefaultAttributes(self) -> None:
        """ Overridden base class virtual. By default we should use
the same font/colour attributes as the native wx.Button.
        """

    def GetUseFocusIndicator(self) -> bool:
        """ Returns the focus indicator flag, specifying if a focus indicator
(dotted line) is being used.
        """

    def InitColours(self) -> None:
        """ Calculate a new set of highlight and shadow colours based on
the background colour. Works okay if the colour is darkâ¦
        """

    def InitOtherEvents(self) -> None:
        """ Override this method in a subclass to initialize any other events that
need to be bound.  Added so __init__ doesnât need to be
overridden, which is complicated with multiple inheritance.
        """

    def Notify(self) -> None:
        """ Actually sends a wx.EVT_BUTTON event to the listener (if any).
        """

    def OnGainFocus(self, event: 'FocusEvent') -> None:
        """ Handles the wx.EVT_SET_FOCUS event for GenButton.
        """

    def OnKeyDown(self, event: 'KeyEvent') -> None:
        """ Handles the wx.EVT_KEY_DOWN event for GenButton.
        """

    def OnKeyUp(self, event: 'KeyEvent') -> None:
        """ Handles the wx.EVT_KEY_UP event for GenButton.
        """

    def OnLeftDown(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_LEFT_DOWN event for GenButton.
        """

    def OnLeftUp(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_LEFT_UP event for GenButton.
        """

    def OnLoseCapture(self, event: 'MouseCaptureLostEvent') -> None:
        """ Handles the wx.EVT_MOUSE_CAPTURE_LOST event for GenButton.
        """

    def OnLoseFocus(self, event: 'FocusEvent') -> None:
        """ Handles the wx.EVT_KILL_FOCUS event for GenButton.
        """

    def OnMotion(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_MOTION event for GenButton.
        """

    def OnPaint(self, event: 'PaintEvent') -> None:
        """ Handles the wx.EVT_PAINT event for GenButton.
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ Handles the wx.EVT_SIZE event for GenButton.
        """

    def SetBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the GenButton background colour.
        """

    def SetBezelWidth(self, width: integer) -> None:
        """ Sets the width of the 3D effect.
        """

    def SetDefault(self) -> None:
        """ This sets the GenButton to be the default item for
the panel or dialog box.
        """

    def SetForegroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the wx.GenButton foreground colour.
        """

    def SetInitialSize(self, size: Optional[Union[tuple[int, int], 'Size']]=None) -> None:
        """ Given the current font and bezel width settings, calculate
and set a good size.
        """

    def SetUseFocusIndicator(self, flag: bool) -> None:
        """ Specifies if a focus indicator (dotted line) should be used.
        """

    def ShouldInheritColours(self) -> None:
        """ Overridden base class virtual. Buttons usually donât inherit
the parentâs colours.
        """

EVT_BUTTON: int
EVT_SET_FOCUS: int
EVT_KEY_DOWN: int
EVT_KEY_UP: int
EVT_LEFT_DOWN: int
EVT_LEFT_UP: int
EVT_MOUSE_CAPTURE_LOST: int
EVT_KILL_FOCUS: int
EVT_MOTION: int
EVT_PAINT: int
EVT_SIZE: int
EVT_BUTTON: int
EVT_SET_FOCUS: int
EVT_KEY_DOWN: int
EVT_KEY_UP: int
EVT_LEFT_DOWN: int
EVT_LEFT_UP: int
EVT_MOUSE_CAPTURE_LOST: int
EVT_KILL_FOCUS: int
EVT_MOTION: int
EVT_PAINT: int
EVT_SIZE: int
DefaultSize: int


class GenBitmapButton(lib.buttons.GenButton):
    """ A generic bitmap button.
    """
    def __init__(self, parent, id=-1, bitmap=wx.NullBitmap, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, validator = wx.DefaultValidator, name = "genbutton") -> None:
        """ Default class constructor.
        """

    def DrawLabel(self, dc, width, height, dx=0, dy=0) -> None:
        """ 
        """

    def GetBitmapDisabled(self) -> 'Bitmap':
        """ Returns the bitmap for the buttonâs disabled state, which may be invalid.
        """

    def GetBitmapFocus(self) -> 'Bitmap':
        """ Returns the bitmap for the buttonâs focused state, which may be invalid.
        """

    def GetBitmapLabel(self) -> 'Bitmap':
        """ Returns the bitmap for the buttonâs normal state.
        """

    def GetBitmapSelected(self) -> 'Bitmap':
        """ Returns the bitmap for the buttonâs pressed state, which may be invalid.
        """

    def SetBitmapDisabled(self, bitmap: 'Bitmap') -> None:
        """ Sets the bitmap for the disabled button appearance.
        """

    def SetBitmapFocus(self, bitmap: 'Bitmap') -> None:
        """ Sets the bitmap for the focused button appearance.
        """

    def SetBitmapLabel(self, bitmap: 'Bitmap', createOthers=True) -> None:
        """ Set the bitmap to display normally.
This is the only one that is required.
        """

    def SetBitmapSelected(self, bitmap: 'Bitmap') -> None:
        """ Sets the bitmap for the selected (depressed) button appearance.
        """



class GenBitmapTextButton(lib.buttons.GenBitmapButton):
    """ A generic bitmapped button with text label.
    """
    def __init__(self, parent, id=-1, bitmap=wx.NullBitmap, label='', pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, validator = wx.DefaultValidator, name = "genbutton") -> None:
        """ Default class constructor.
        """

    def DrawLabel(self, dc, width, height, dx=0, dy=0) -> None:
        """ 
        """



class GenBitmapTextToggleButton(lib.buttons.__ToggleMixin, lib.buttons.GenBitmapTextButton):
    """ A generic toggle bitmap button with text label.
    """


class GenBitmapToggleButton(lib.buttons.__ToggleMixin, lib.buttons.GenBitmapButton):
    """ A generic toggle bitmap button.
    """


class GenButtonEvent(CommandEvent):
    """ Event sent from the generic buttons when the button is activated.
    """
    def __init__(self, eventType, id) -> None:
        """ Default class constructor.
        """

    def GetButtonObj(self) -> None:
        """ Returns the object associated with this event.
        """

    def GetIsDown(self) -> bool:
        """ Returns the button toggle status as True if the button is down, False
otherwise.
        """

    def SetButtonObj(self, btn: GenButton) -> None:
        """ Sets the event object for the event.
        """

    def SetIsDown(self, isDown: bool) -> None:
        """ Set the button toggle status as âdownâ or âupâ.
        """



class GenToggleButton(lib.buttons.__ToggleMixin, lib.buttons.GenButton):
    """ A generic toggle button.
    """


class ThemedGenBitmapButton(lib.buttons.__ThemedMixin, lib.buttons.GenBitmapButton):
    """ A themed generic bitmap button.
    """


class ThemedGenBitmapTextButton(lib.buttons.__ThemedMixin, lib.buttons.GenBitmapTextButton):
    """ A themed generic bitmapped button with text label.
    """


class ThemedGenBitmapTextToggleButton(lib.buttons.__ThemedMixin, lib.buttons.GenBitmapTextToggleButton):
    """ A themed generic toggle bitmap button with text label.
    """


class ThemedGenBitmapToggleButton(lib.buttons.__ThemedMixin, lib.buttons.GenBitmapToggleButton):
    """ A themed generic toggle bitmap button.
    """


class ThemedGenButton(lib.buttons.__ThemedMixin, lib.buttons.GenButton):
    """ A themed generic button.
    """


class ThemedGenToggleButton(lib.buttons.__ThemedMixin, lib.buttons.GenToggleButton):
    """ A themed generic toggle button.
    """


