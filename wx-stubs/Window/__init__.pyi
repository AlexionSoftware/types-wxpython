# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class ChildrenRepositioningGuard:
    """ Helper for ensuring EndRepositioningChildren() is called correctly.

        Source: https://docs.wxpython.org/wx.Window.ChildrenRepositioningGuard.html
    """
    def __init__(self, win: 'Window') -> None:
        """ Constructor calls wx.Window.BeginRepositioningChildren .

            Source: https://docs.wxpython.org/wx.Window.ChildrenRepositioningGuard.html
        """



