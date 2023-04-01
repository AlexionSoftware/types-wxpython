# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class __ThemedMixin:
    """ Uses the native renderer to draw the bezel, also handle mouse-overs.

        Source: https://docs.wxpython.org/wx.lib.buttons.__ThemedMixin.html
    """
    def DrawBezel(self, dc, x1, y1, x2, y2) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.buttons.__ThemedMixin.html
        """

    def InitOtherEvents(self) -> None:
        """ Initializes other events needed for themed buttons.

            Source: https://docs.wxpython.org/wx.lib.buttons.__ThemedMixin.html
        """

    def OnMouse(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_ENTER_WINDOW and wx.EVT_LEAVE_WINDOW events for
GenButton when used as a themed button.

            Source: https://docs.wxpython.org/wx.lib.buttons.__ThemedMixin.html
        """



EVT_ENTER_WINDOW: int

EVT_LEAVE_WINDOW: int

class __ToggleMixin:
    """ A mixin that allows to transform GenButton in the corresponding
toggle button.

        Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
    """
    def GetToggle(self) -> None:
        """ Returns the toggled state of a button.

            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """

    def OnKeyDown(self, event: 'KeyEvent') -> None:
        """ Handles the wx.EVT_KEY_DOWN event for GenButton when used as toggle button.

            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """

    def OnKeyUp(self, event: 'KeyEvent') -> None:
        """ Handles the wx.EVT_KEY_UP event for GenButton when used as toggle button.

            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """

    def OnLeftDown(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_LEFT_DOWN event for GenButton when used as toggle button.

            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """

    def OnLeftUp(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_LEFT_UP event for GenButton when used as toggle button.

            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """

    def OnMotion(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_MOTION event for GenButton when used as toggle button.

            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """

    def SetToggle(self, flag: bool) -> None:
        """ Sets the button as toggled/not toggled.

            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """



EVT_KEY_DOWN: int

EVT_KEY_UP: int

EVT_LEFT_DOWN: int

EVT_LEFT_UP: int

EVT_MOTION: int

class GenButton(Control):
    """ A generic button, and base class for the other generic buttons.

        Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
    """
    def __init__(self, parent, id=-1, label='', pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, validator = wx.DefaultValidator, name = "genbutton") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def AcceptsFocus(self) -> None:
        """ Can this window be given focus by mouse click?

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def DoGetBestSize(self) -> None:
        """ Overridden base class virtual. Determines the best size of the
button based on the label and bezel size.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def DrawBezel(self, dc, x1, y1, x2, y2) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def DrawFocusIndicator(self, dc, w, h) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def DrawLabel(self, dc, width, height, dx=0, dy=0) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ Enables/disables the button.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def GetBackgroundBrush(self, dc: 'DC') -> None:
        """ Returns the current wx.Brush to be used to draw the button background.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def GetBezelWidth(self) -> int:
        """ Returns the width of the 3D effect, in pixels.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def GetDefaultAttributes(self) -> None:
        """ Overridden base class virtual. By default we should use
the same font/colour attributes as the native wx.Button.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def GetUseFocusIndicator(self) -> bool:
        """ Returns the focus indicator flag, specifying if a focus indicator
(dotted line) is being used.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def InitColours(self) -> None:
        """ Calculate a new set of highlight and shadow colours based on
the background colour. Works okay if the colour is darkâ¦

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def InitOtherEvents(self) -> None:
        """ Override this method in a subclass to initialize any other events that
need to be bound.  Added so __init__ doesnât need to be
overridden, which is complicated with multiple inheritance.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def Notify(self) -> None:
        """ Actually sends a wx.EVT_BUTTON event to the listener (if any).

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnGainFocus(self, event: 'FocusEvent') -> None:
        """ Handles the wx.EVT_SET_FOCUS event for GenButton.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnKeyDown(self, event: 'KeyEvent') -> None:
        """ Handles the wx.EVT_KEY_DOWN event for GenButton.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnKeyUp(self, event: 'KeyEvent') -> None:
        """ Handles the wx.EVT_KEY_UP event for GenButton.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnLeftDown(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_LEFT_DOWN event for GenButton.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnLeftUp(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_LEFT_UP event for GenButton.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnLoseCapture(self, event: 'MouseCaptureLostEvent') -> None:
        """ Handles the wx.EVT_MOUSE_CAPTURE_LOST event for GenButton.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnLoseFocus(self, event: 'FocusEvent') -> None:
        """ Handles the wx.EVT_KILL_FOCUS event for GenButton.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnMotion(self, event: 'MouseEvent') -> None:
        """ Handles the wx.EVT_MOTION event for GenButton.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnPaint(self, event: 'PaintEvent') -> None:
        """ Handles the wx.EVT_PAINT event for GenButton.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ Handles the wx.EVT_SIZE event for GenButton.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def SetBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the GenButton background colour.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def SetBezelWidth(self, width: int) -> None:
        """ Sets the width of the 3D effect.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def SetDefault(self) -> None:
        """ This sets the GenButton to be the default item for
the panel or dialog box.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def SetForegroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the wx.GenButton foreground colour.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def SetInitialSize(self, size: Optional[Union[tuple[int, int], 'Size']]=None) -> None:
        """ Given the current font and bezel width settings, calculate
and set a good size.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def SetUseFocusIndicator(self, flag: bool) -> None:
        """ Specifies if a focus indicator (dotted line) should be used.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def ShouldInheritColours(self) -> None:
        """ Overridden base class virtual. Buttons usually donât inherit
the parentâs colours.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """



EVT_BUTTON: int

EVT_SET_FOCUS: int

EVT_MOUSE_CAPTURE_LOST: int

EVT_KILL_FOCUS: int

EVT_PAINT: int

EVT_SIZE: int

DefaultSize: int

class GenBitmapButton(GenButton):
    """ A generic bitmap button.

        Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
    """
    def __init__(self, parent, id=-1, bitmap=wx.NullBitmap, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, validator = wx.DefaultValidator, name = "genbutton") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def DrawLabel(self, dc, width, height, dx=0, dy=0) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def GetBitmapDisabled(self) -> 'Bitmap':
        """ Returns the bitmap for the buttonâs disabled state, which may be invalid.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def GetBitmapFocus(self) -> 'Bitmap':
        """ Returns the bitmap for the buttonâs focused state, which may be invalid.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def GetBitmapLabel(self) -> 'Bitmap':
        """ Returns the bitmap for the buttonâs normal state.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def GetBitmapSelected(self) -> 'Bitmap':
        """ Returns the bitmap for the buttonâs pressed state, which may be invalid.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def SetBitmapDisabled(self, bitmap: 'Bitmap') -> None:
        """ Sets the bitmap for the disabled button appearance.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def SetBitmapFocus(self, bitmap: 'Bitmap') -> None:
        """ Sets the bitmap for the focused button appearance.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def SetBitmapLabel(self, bitmap: 'Bitmap', createOthers=True) -> None:
        """ Set the bitmap to display normally.
This is the only one that is required.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def SetBitmapSelected(self, bitmap: 'Bitmap') -> None:
        """ Sets the bitmap for the selected (depressed) button appearance.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """



class GenBitmapTextButton(GenBitmapButton):
    """ A generic bitmapped button with text label.

        Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapTextButton.html
    """
    def __init__(self, parent, id=-1, bitmap=wx.NullBitmap, label='', pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, validator = wx.DefaultValidator, name = "genbutton") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapTextButton.html
        """

    def DrawLabel(self, dc, width, height, dx=0, dy=0) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapTextButton.html
        """



class GenBitmapTextToggleButton(__ToggleMixin,GenBitmapTextButton):
    """ A generic toggle bitmap button with text label.

        Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapTextToggleButton.html
    """


class GenBitmapToggleButton(__ToggleMixin,GenBitmapButton):
    """ A generic toggle bitmap button.

        Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapToggleButton.html
    """


class GenButtonEvent(CommandEvent):
    """ Event sent from the generic buttons when the button is activated.

        Source: https://docs.wxpython.org/wx.lib.buttons.GenButtonEvent.html
    """
    def __init__(self, eventType, id) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButtonEvent.html
        """

    def GetButtonObj(self) -> None:
        """ Returns the object associated with this event.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButtonEvent.html
        """

    def GetIsDown(self) -> bool:
        """ Returns the button toggle status as True if the button is down, False
otherwise.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButtonEvent.html
        """

    def SetButtonObj(self, btn: GenButton) -> None:
        """ Sets the event object for the event.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButtonEvent.html
        """

    def SetIsDown(self, isDown: bool) -> None:
        """ Set the button toggle status as âdownâ or âupâ.

            Source: https://docs.wxpython.org/wx.lib.buttons.GenButtonEvent.html
        """



class GenToggleButton(__ToggleMixin,GenButton):
    """ A generic toggle button.

        Source: https://docs.wxpython.org/wx.lib.buttons.GenToggleButton.html
    """


class ThemedGenBitmapButton(__ThemedMixin,GenBitmapButton):
    """ A themed generic bitmap button.

        Source: https://docs.wxpython.org/wx.lib.buttons.ThemedGenBitmapButton.html
    """


class ThemedGenBitmapTextButton(__ThemedMixin,GenBitmapTextButton):
    """ A themed generic bitmapped button with text label.

        Source: https://docs.wxpython.org/wx.lib.buttons.ThemedGenBitmapTextButton.html
    """


class ThemedGenBitmapTextToggleButton(__ThemedMixin,GenBitmapTextToggleButton):
    """ A themed generic toggle bitmap button with text label.

        Source: https://docs.wxpython.org/wx.lib.buttons.ThemedGenBitmapTextToggleButton.html
    """


class ThemedGenBitmapToggleButton(__ThemedMixin,GenBitmapToggleButton):
    """ A themed generic toggle bitmap button.

        Source: https://docs.wxpython.org/wx.lib.buttons.ThemedGenBitmapToggleButton.html
    """


class ThemedGenButton(__ThemedMixin,GenButton):
    """ A themed generic button.

        Source: https://docs.wxpython.org/wx.lib.buttons.ThemedGenButton.html
    """


class ThemedGenToggleButton(__ThemedMixin,GenToggleButton):
    """ A themed generic toggle button.

        Source: https://docs.wxpython.org/wx.lib.buttons.ThemedGenToggleButton.html
    """


