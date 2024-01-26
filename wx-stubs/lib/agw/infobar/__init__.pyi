# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class AutoWrapStaticText(GenStaticText):
    """ A simple class derived from lib.stattext that implements auto-wrapping
behaviour depending on the parent size.

        Source: https://docs.wxpython.org/wx.lib.agw.infobar.AutoWrapStaticText.html
    """
    def __init__(self, parent, label) -> None:
        """ Defsult class constructor.

            Source: https://docs.wxpython.org/wx.lib.agw.infobar.AutoWrapStaticText.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ Handles the wx.EVT_SIZE event for AutoWrapStaticText.

            Source: https://docs.wxpython.org/wx.lib.agw.infobar.AutoWrapStaticText.html
        """

    def SetLabel(self, label, wrapped=False) -> None:
        """ Sets the AutoWrapStaticText label.

            Source: https://docs.wxpython.org/wx.lib.agw.infobar.AutoWrapStaticText.html
        """

    def Wrap(self, width: int) -> None:
        """ This functions wraps the controls label so that each of its lines becomes at
most width pixels wide if possible (the lines are broken at words boundaries
so it might not be the case if words are too long).

            Source: https://docs.wxpython.org/wx.lib.agw.infobar.AutoWrapStaticText.html
        """



EVT_SIZE: int

