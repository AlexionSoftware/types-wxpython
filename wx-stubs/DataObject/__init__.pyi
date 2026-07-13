# -*- coding: utf-8 -*-

import enum
from typing import Any, ContextManager, Optional, TypeAlias, Union

class Direction(enum.IntEnum):
    Get = ...
    Set = ...
    Both = ...

