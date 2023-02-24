# -*- coding: utf-8 -*-
from typing import Any, Optional, Union

class ChildrenRepositioningGuard:
    """ Helper for ensuring EndRepositioningChildren() is called correctly.
    """
    def __init__(self, win: 'Window') -> None:
        """ Constructor calls wx.Window.BeginRepositioningChildren .
        """



