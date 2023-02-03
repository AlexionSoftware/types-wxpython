from typing import Any, Optional
from .. import Window, Icon, ICON_INFORMATION, EvtHandler


EVT_TASKBAR_LEFT_DCLICK: int
EVT_TASKBAR_RIGHT_UP: int
SOUND_SYNC: int
SOUND_ASYNC: int
SOUND_LOOP: int


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


class Sound:
	""" This class represents a short sound (loaded from Windows WAV file), that can be stored in memory and played.

		Currently this class is implemented on Windows and Unix and can use either Open Sound System (OSS) or Simple DirectMedia Layer (SDL) under the latter. Notice that OSS is not provided any more by most, and maybe even all, Linux systems in 2017 and osspd (OSS Proxy Daemon) package typically needs to be installed to make it work."""

	def __init__(self, fileName: Optional[str] = None) -> None:
		""" Constructs a wave object from a file or, under Windows, from a Windows resource.
		"""

	def Create(self, fileName: str) -> bool:
		""" Constructs a wave object from a file or resource.
		"""

	def CreateFromData(self, data: Any) -> bool:
		""" Create a sound object from data in a memory buffer in WAV format.
		"""

	def IsOk(self) -> bool:
		""" Returns True if the object contains a successfully loaded file or resource, False otherwise.
		"""

	def Play(self, flags: int = -1) -> bool:
		""" Plays the sound file.

			If another sound is playing, it will be interrupted.

			Returns True on success, False otherwise. Note that in general it is possible to delete the object which is being asynchronously played any time after calling this function and the sound would continue playing, however this currently doesn’t work under Windows for sound objects loaded from memory data.

			The possible values for flags are:
 				- wx.adv.SOUND_SYNC: Play will block and wait until the sound is replayed.
  				- wx.adv.SOUND_ASYNC: Sound is played asynchronously, Play returns immediately.
				- SOUND_ASYNC|wxSOUND_LOOP: Sound is played asynchronously and loops until another sound is played, Stop is called or the program terminates.
		"""

	@staticmethod
	def PlaySound(filename: str, flags: int = -1) -> bool:
		""" Plays the sound file.

			If another sound is playing, it will be interrupted.

			Returns True on success, False otherwise. Note that in general it is possible to delete the object which is being asynchronously played any time after calling this function and the sound would continue playing, however this currently doesn’t work under Windows for sound objects loaded from memory data.

			The possible values for flags are:
 				- wx.adv.SOUND_SYNC: Play will block and wait until the sound is replayed.
  				- wx.adv.SOUND_ASYNC: Sound is played asynchronously, Play returns immediately.
				- SOUND_ASYNC|wxSOUND_LOOP: Sound is played asynchronously and loops until another sound is played, Stop is called or the program terminates.
		"""

	@staticmethod
	def Stop() -> None:
		""" If a sound is played, this function stops it.
		"""
