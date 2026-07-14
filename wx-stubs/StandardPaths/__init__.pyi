# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

FileLayout: TypeAlias = int  # Enumeration

Dir: TypeAlias = int  # Enumeration

class ResourceCat(int):  # Enum
    pass

ResourceCat_None: ResourceCat
ResourceCat_Messages: ResourceCat

class ConfigFileConv(int):  # Enum
    pass

ConfigFileConv_Dot: ConfigFileConv
ConfigFileConv_Ext: ConfigFileConv
