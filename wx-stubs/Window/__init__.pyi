# -*- coding: utf-8 -*-
from typing import Optional, Any


class ChildrenRepositioningGuard:
	""" Helper for ensuring EndRepositioningChildren() is called correctly.
	"""
	def __init__(self, win: 'Window') -> None:
		""" Constructor calls wx.Window.BeginRepositioningChildren .
		"""



