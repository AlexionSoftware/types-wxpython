# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class MultiMessageDialog(Dialog):
    """ A dialog like wx.MessageDialog, but with an optional 2nd message string
that is shown in a scrolled window, and also allows passing in the icon to
be shown instead of the stock error, question, etc. icons. The btnLabels
can be used if youâd like to change the stock labels on the buttons, itâs
a dictionary mapping stock IDs to label strings.

        Source: https://docs.wxpython.org/wx.lib.dialogs.MultiMessageDialog.html
    """
    def __init__(self, parent, message, caption = "Message Box", msg2="", style = wx.OK | wx.CANCEL, pos = wx.DefaultPosition, icon=None, btnLabels=None) -> None:
        """ Initialize self.  See help(type(self)) for accurate signature.

            Source: https://docs.wxpython.org/wx.lib.dialogs.MultiMessageDialog.html
        """

    def OnButton(self, evt) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.dialogs.MultiMessageDialog.html
        """



class MultipleChoiceDialog(Dialog):
    """ Dialog()
Dialog(parent, id=ID_ANY, title=ââ, pos=DefaultPosition, size=DefaultSize, style=DEFAULT_DIALOG_STYLE, name=DialogNameStr)

        Source: https://docs.wxpython.org/wx.lib.dialogs.MultipleChoiceDialog.html
    """
    def __init__(*args, **kwargs) -> None:
        """ Initialize self.  See help(type(self)) for accurate signature.

            Source: https://docs.wxpython.org/wx.lib.dialogs.MultipleChoiceDialog.html
        """

    def GetValue(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.dialogs.MultipleChoiceDialog.html
        """

    def GetValueString(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.lib.dialogs.MultipleChoiceDialog.html
        """



class ScrolledMessageDialog(Dialog):
    """ Dialog()
Dialog(parent, id=ID_ANY, title=ââ, pos=DefaultPosition, size=DefaultSize, style=DEFAULT_DIALOG_STYLE, name=DialogNameStr)

        Source: https://docs.wxpython.org/wx.lib.dialogs.ScrolledMessageDialog.html
    """
    def __init__(*args, **kwargs) -> None:
        """ Initialize self.  See help(type(self)) for accurate signature.

            Source: https://docs.wxpython.org/wx.lib.dialogs.ScrolledMessageDialog.html
        """



