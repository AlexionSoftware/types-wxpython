# -*- coding: utf-8 -*-
import enum
from typing import Any, ContextManager, Optional, TypeAlias, Union

FileLayout: TypeAlias = int  # Enumeration

Dir: TypeAlias = int  # Enumeration

class ResourceCat(enum.IntEnum):
    ResourceCat_None = ...
    ResourceCat_Messages = ...

class ConfigFileConv(enum.IntEnum):
    ConfigFileConv_Dot = ...
    ConfigFileConv_Ext = ...
