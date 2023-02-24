# -*- coding: utf-8 -*-
class ScrolledMessageDialog(wx.Dialog):
	""" Dialog waarop een bericht gescrolled kan worden weergegeven
	"""

	def __init__(self, parent: wx.Window, messageString: str, title: str) -> None:
		""" Constructor
		"""
