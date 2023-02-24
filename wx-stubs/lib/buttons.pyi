from typing import Optional

from .. import Bitmap, Button, Window

class GenBitmapTextButton(Button):
	""" Interface voor wx.lib.GenBitmapTextButton
	"""

	def __init__(self, parent: Window, id: int = None, pos: tuple[int, int] = None, size: tuple[int, int] = None, style: int = None, name: str = None, label: str = None, bitmap: Optional[Bitmap] = None) -> None:
		pass
