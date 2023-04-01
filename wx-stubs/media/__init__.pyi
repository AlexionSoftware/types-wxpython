# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class MediaCtrl(Control):
    """ MediaCtrl is a class for displaying various types of media, such as
videos, audio files, natively through native codecs.

        Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Create(self, parent, id=-1, fileName="", pos=DefaultPosition, size=DefaultSize, style=0, szBackend="", validator=DefaultValidator, name="mediaCtrl") -> bool:
        """ Creates this control.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def GetBestSize(self) -> 'Size':
        """ Obtains the best size relative to the original/natural size of the video, if there is any.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def GetPlaybackRate(self) -> float:
        """ Obtains the playback rate, or speed of the media.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def GetState(self) -> 'media.MediaState':
        """ Obtains the state the playback of the media is in.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def GetVolume(self) -> float:
        """ Gets the volume of the media from a 0.0 to 1.0 range.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Length(self) -> 'FileOffset':
        """ Obtains the length - the total amount of time the media has in milliseconds.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Load(self, fileName: str) -> bool:
        """ Loads the file that fileName refers to.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def LoadURI(self, uri: str) -> bool:
        """ Loads the location that uri refers to.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def LoadURIWithProxy(self, uri, proxy) -> bool:
        """ Loads the location that  uri   refers to with the proxy   proxy .

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Pause(self) -> bool:
        """ Pauses playback of the media.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Play(self) -> bool:
        """ Resumes playback of the media.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Seek(self, where, mode=FromStart) -> 'FileOffset':
        """ Seeks to a position within the media.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def SetPlaybackRate(self, dRate: float) -> bool:
        """ Sets the playback rate, or speed of the media, to that referred by dRate.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def SetVolume(self, dVolume: float) -> bool:
        """ Sets the volume of the media from a 0.0 to 1.0 range to that referred by  dVolume .

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def ShowPlayerControls(self, flags: MediaCtrlPlayerControls=MEDIACTRLPLAYERCONTROLS_DEFAULT) -> bool:
        """ A special feature to   wx.media.MediaCtrl.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Stop(self) -> bool:
        """ Stops the media.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Tell(self) -> 'FileOffset':
        """ Obtains the current position in time within the media in milliseconds.

            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    BestSize: 'Size'  # See GetBestSize
    PlaybackRate: float  # See GetPlaybackRate and SetPlaybackRate
    State: 'media.MediaState'  # See GetState
    Volume: float  # See GetVolume and SetVolume



MC_NO_AUTORESIZE: int  # By default, the control will automatically adjust its size to exactly fit the size of a loaded video as soon as a video is loaded. If this flag is given, the control will not change its size automatically and it must be done manually (if desired) using Layout. It is strongly recommended to use this flag and handle control resizing manually (note that this style is only available in wxWidgets 3.1.6, so it is only possible to do it when using this or later version). ^^

MEDIASTATE_STOPPED: int

MEDIASTATE_PAUSED: int

MEDIASTATE_PLAYING: int

class MediaEvent(NotifyEvent):
    """ Event MediaCtrl uses.

        Source: https://docs.wxpython.org/wx.media.MediaEvent.html
    """
    def __init__(self, commandType=wxEVT_NULL, winid=0) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.media.MediaEvent.html
        """



EVT_MEDIA_LOADED: int  # Sent when a media has loaded enough data that it can start playing. Processes a  wxEVT_MEDIA_LOADED   event type.

EVT_MEDIA_STOP: int  # Sent when a media has switched to the  MEDIASTATE_STOPPED   state. You may be able to Veto this event to prevent it from stopping, causing it to continue playing - even if it has reached that end of the media (note that this may not have the desired effect - if you want to loop the media, for example, catch the   EVT_MEDIA_FINISHED   and play there instead). Processes a   wxEVT_MEDIA_STOP   event type.

EVT_MEDIA_FINISHED: int  # Sent when a media has finished playing in a   wx.media.MediaCtrl. Processes a  wxEVT_MEDIA_FINISHED   event type.

EVT_MEDIA_STATECHANGED: int  # Sent when a media has switched its state (from any media state). Processes a  wxEVT_MEDIA_STATECHANGED   event type.

EVT_MEDIA_PLAY: int  # Sent when a media has switched to the  MEDIASTATE_PLAYING   state. Processes a   wxEVT_MEDIA_PLAY   event type.

EVT_MEDIA_PAUSE: int  # Sent when a media has switched to the  MEDIASTATE_PAUSED   state. Processes a   wxEVT_MEDIA_PAUSE   event type. ^^

MediaState: TypeAlias = int  # Enumeration

MediaCtrlPlayerControls: TypeAlias = int  # Enumeration

MEDIACTRLPLAYERCONTROLS_NONE: int

MEDIACTRLPLAYERCONTROLS_STEP: int

MEDIACTRLPLAYERCONTROLS_VOLUME: int

MEDIACTRLPLAYERCONTROLS_DEFAULT: int

