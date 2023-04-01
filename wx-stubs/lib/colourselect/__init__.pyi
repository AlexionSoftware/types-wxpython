# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class ColourSelect(GenBitmapButton):
    """ A subclass of wx.lib.buttons.GenBitmapButton that,
when clicked, will display a colour selection dialog.

        Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
    """
    def __init__(self, parent, id=wx.ID_ANY, label="", colour=wx.BLACK, pos=wx.DefaultPosition, size=wx.DefaultSize, callback=None, style=0) -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def GetColour(self) -> 'Colour':
        """ Returns the current colour set for the ColourSelect.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def GetCustomColours(self) -> 'lib.colourselect.CustomColourData':
        """ Returns the current set of custom colour values to be shown in the
colour dialog, if supported.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def GetLabel(self) -> str:
        """ Returns the current text label for the ColourSelect.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def GetValue(self) -> 'Colour':
        """ Returns the current colour set for the ColourSelect.
Same as GetColour.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def MakeBitmap(self) -> None:
        """ Creates a bitmap representation of the current selected colour.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def OnChange(self) -> None:
        """ Fires the EVT_COLOURSELECT event, as the user has changed the current colour.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def OnClick(self, event: 'CommandEvent') -> None:
        """ Handles the wx.EVT_BUTTON event for ColourSelect.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def SetBitmap(self, bmp: 'Bitmap') -> None:
        """ Sets the bitmap representation of the current selected colour to the button.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def SetColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the current colour for ColourSelect.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def SetCustomColours(self, colours: CustomColourData) -> None:
        """ Sets the list of custom colour values to be shown in colour dialog, if
supported.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def SetLabel(self, label: str) -> None:
        """ Sets the new text label for wx.ColourSelect.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def SetValue(self, colour: Union[int, str, 'Colour']) -> None:
        """ Sets the current colour for ColourSelect.  Same as
SetColour.

            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    Colour: Any  # Returns the current colour set for the ColourSelect.
    CustomColours: Any  # Returns the current set of custom colour values to be shown in the
colour dialog, if supported.
    Label: Any  # Returns the current text label for the ColourSelect.
    Value: Any  # Returns the current colour set for the ColourSelect.
Same as GetColour.



EVT_BUTTON: int

class CustomColourData:
    """ A simple container for tracking custom colours to be shown in the colour
dialog, and which facilitates reuse of this collection across multiple
instances or multiple invocations of the ColourSelect button.

        Source: https://docs.wxpython.org/wx.lib.colourselect.CustomColourData.html
    """
    def __init__(self) -> None:
        """ Initialize self.  See help(type(self)) for accurate signature.

            Source: https://docs.wxpython.org/wx.lib.colourselect.CustomColourData.html
        """

    Colours: Any  # See Colours , Colours



