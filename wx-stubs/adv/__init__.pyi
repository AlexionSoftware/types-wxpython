from typing import Optional
from .. import Window, Icon, ICON_INFORMATION, EvtHandler


EVT_TASKBAR_LEFT_DCLICK: int
EVT_TASKBAR_RIGHT_UP: int


class HyperlinkCtrl(Window):
	""" Interface voor wx.adv.HyperLinkCtrl
	"""


class TaskBarIcon(EvtHandler):

	def SetIcon(self, icon: Icon, tooltip: str = "") -> bool:
		""" Sets the icon, and optional tooltip text.
		"""


class NotificationMessage:
	""" Interface voor wwx.adv.NotificationMessage
	"""

	def __init__(self, title: str, message: str = "", parent: Optional[Window] = None, flags: int = ICON_INFORMATION) -> None:
		""" Default constructor, use SetParent , SetTitle and SetMessage to initialize the object before showing it.
		"""

	def AddAction(self, actionId: str, label: str = "") -> bool:
		""" Add an action to the notification.
		"""

	def Close(self) -> None:
		""" Hides the notification.
		"""

	@classmethod
	def MSWUseToasts(cls, shortcutPath: str = "", appId: str = "") -> bool:
		""" Enables toast notifications available since Windows 8 and suppresses the additional icon in the notification area on Windows 10.
		"""

	def SetFlags(self, flags: int) -> None:
		""" This parameter can be currently used to specify the icon to show in the notification.
		"""

	def SetIcon(self, icon: Icon) -> None:
		""" Specify a custom icon to be displayed in the notification.
		"""

	def SetMessage(self, message: str) -> None:
		""" Set the main text of the notification.
		"""

	def SetParent(self, parent: Window) -> None:
		""" Set the parent for this notification: the notification will be associated with the top level parent of this window or, if this method is not called, with the main application window by default.
		"""

	def SetTitle(self, title: str) -> None:
		""" Set the title, it must be a concise string (not more than 64 characters), use SetMessage to give the user more details.
		"""

	def Show(self, timeout: int = 0) -> bool:
		""" Show the notification to the user and hides it after timeout seconds are elapsed.
		"""

	@classmethod
	def UseTaskBarIcon(cls, icon: TaskBarIcon) -> TaskBarIcon:
		""" If the application already uses a wx.adv.TaskBarIcon, it should be connected to notifications by using this method.
			This has no effect if toast notifications are used.
		"""
