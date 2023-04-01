# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class ScrolledPanel(ScrolledWindow):
    """ ScrolledPanel fills a âholeâ in the implementation of
ScrolledWindow, providing automatic scrollbar and scrolling
behavior and the tab traversal management that ScrolledWindow lacks.

        Source: https://docs.wxpython.org/wx.lib.scrolledpanel.ScrolledPanel.html
    """
    def __init__(self, parent, id=-1, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name="scrolledpanel") -> None:
        """ Default class constructor.

            Source: https://docs.wxpython.org/wx.lib.scrolledpanel.ScrolledPanel.html
        """

    def OnChildFocus(self, evt: ChildFocusEvent) -> None:
        """ If the child window that gets the focus is not fully visible,
this handler will try to scroll enough to see it.

            Source: https://docs.wxpython.org/wx.lib.scrolledpanel.ScrolledPanel.html
        """

    def ScrollChildIntoView(self, child: 'Window') -> None:
        """ Scroll the panel so that the specified child window is in view.

            Source: https://docs.wxpython.org/wx.lib.scrolledpanel.ScrolledPanel.html
        """

    def SetupScrolling(self, scroll_x=True, scroll_y=True, rate_x=20, rate_y=20, scrollToTop=True, scrollIntoView=True) -> None:
        """ This function sets up the event handling necessary to handle
scrolling properly. It should be called within the __init__
function of any class that is derived from ScrolledPanel,
once the controls on the panel have been constructed and
thus the size of the scrolling area can be determined.

            Source: https://docs.wxpython.org/wx.lib.scrolledpanel.ScrolledPanel.html
        """



