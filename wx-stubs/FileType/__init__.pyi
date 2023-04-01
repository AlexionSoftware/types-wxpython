# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class MessageParameters:
    """ Class representing message parameters.

        Source: https://docs.wxpython.org/wx.FileType.MessageParameters.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.FileType.MessageParameters.html
        """

    def GetFileName(self) -> str:
        """ Return the filename.

            Source: https://docs.wxpython.org/wx.FileType.MessageParameters.html
        """

    def GetMimeType(self) -> str:
        """ Return the MIME type.

            Source: https://docs.wxpython.org/wx.FileType.MessageParameters.html
        """

    def GetParamValue(self, name: str) -> str:
        """ Overridable method for derived classes. Returns empty string by default.

            Source: https://docs.wxpython.org/wx.FileType.MessageParameters.html
        """

    FileName: str  # See GetFileName
    MimeType: str  # See GetMimeType



