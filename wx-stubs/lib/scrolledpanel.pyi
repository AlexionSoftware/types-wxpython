from .. import Panel

class ScrolledPanel(Panel):
	""" Interface voor wx.lib.scrolledPanel.ScrolledPanel
	"""
	def SetupScrolling(self, scroll_x: bool=True, scroll_y: bool=True, rate_x: int=20, rate_y: int=20, scrollToTop: bool=True, scrollIntoView: bool=True) -> None:
		""" This function sets up the event handling necessary to handle scrolling properly. It should be called within the __init__ function of any class that is derived from ScrolledPanel, once the controls on the panel have been constructed and thus the size of the scrolling area can be determined.
		"""
