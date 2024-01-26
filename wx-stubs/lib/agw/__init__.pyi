# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

def ChopText(dc, text, max_size) -> None:
    """ Chops the input text if its size does not fit in max_size, by cutting the
text and adding ellipsis at the end.

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.html
    """


def DrawTreeItemButton(win, dc, rect, flags) -> None:
    """ Draw the expanded/collapsed icon for a tree control item.

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.html
    """


def EventFlagsToSelType(style, shiftDown=False, ctrlDown=False) -> None:
    """ Translate the key or mouse event flag to the type of selection we
are dealing with.

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.html
    """


def MakeDisabledBitmap(original: 'Bitmap') -> None:
    """ Creates a disabled-looking bitmap starting from the input one.

        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.html
    """


DragImage: int

WANTS_CHARS: int

TR_NO_BUTTONS: int

TR_SINGLE: int

TR_HAS_BUTTONS: int

TR_NO_LINES: int

TR_LINES_AT_ROOT: int

TR_TWIST_BUTTONS: int

TR_MULTIPLE: int

TR_HAS_VARIABLE_ROW_HEIGHT: int

TR_EDIT_LABELS: int

TR_ROW_LINES: int

TR_HIDE_ROOT: int

TR_FULL_ROW_HIGHLIGHT: int

TR_HAS_VARIABLE_LINE_HEIGHT: int

CONTROL_EXPANDED: int

