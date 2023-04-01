# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class HSVValue:
    """ A simple class which stores hue, saturation and value as doubles in
the range 0.0-1.0.

        Source: https://docs.wxpython.org/wx.Image.HSVValue.html
    """
    def __init__(self, h=0.0, s=0.0, v=0.0) -> None:
        """ Constructor for   wx.Image.HSVValue, an object that contains values for hue, saturation and value which represent the value of a color.

            Source: https://docs.wxpython.org/wx.Image.HSVValue.html
        """

    hue: Any  # A public C++ attribute of type float.
    saturation: Any  # A public C++ attribute of type float.
    value: Any  # A public C++ attribute of type float.



class RGBValue:
    """ integers in the range of 0-255.

        Source: https://docs.wxpython.org/wx.Image.RGBValue.html
    """
    def __init__(self, r=0, g=0, b=0) -> None:
        """ Constructor for   wx.Image.RGBValue, an object that contains values for red, green and blue which represent the value of a color.

            Source: https://docs.wxpython.org/wx.Image.RGBValue.html
        """

    blue: Any  # A public C++ attribute of type int.
    green: Any  # A public C++ attribute of type int.
    red: Any  # A public C++ attribute of type int.



