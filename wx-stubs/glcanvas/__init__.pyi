# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class GLCanvas(Window):
    """ GLCanvas is a class for displaying OpenGL graphics.

        Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ variant (WindowVariant) â

            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """

    @staticmethod
    def IsDisplaySupported(*args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """

    @staticmethod
    def IsExtensionSupported(extension: int) -> bool:
        """ Returns True if the extension with given name is supported.

            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """

    def SetColour(self, colour: str) -> bool:
        """ Sets the current colour for this window (using  glcolor3f() ), using the wxWidgets colour database to find a named colour.

            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """

    def SetCurrent(self, context: 'glcanvas.GLContext') -> bool:
        """ Makes the OpenGL state that is represented by the OpenGL rendering context context  current, i.e.

            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """

    def SwapBuffers(self) -> bool:
        """ Swaps the double-buffer of this window, making the back-buffer the front-buffer and vice versa, so that the output of the previous OpenGL commands is displayed on the window.

            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """



WX_GL_RGBA: int

class GLContext(Object):
    """ An instance of a GLContext represents the state of an OpenGL state
machine and the connection between OpenGL and the system.

        Source: https://docs.wxpython.org/wx.glcanvas.GLContext.html
    """
    def __init__(self, win, other=None, ctxAttrs=None) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContext.html
        """

    def IsOK(self) -> bool:
        """ Checks if the underlying OpenGL rendering context was correctly created by the system with the requested attributes.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContext.html
        """

    def SetCurrent(self, win: 'glcanvas.GLCanvas') -> bool:
        """ Makes the OpenGL state that is represented by this rendering context current with the   wx.glcanvas.GLCanvas win.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContext.html
        """



class GLAttributes(GLAttribsBase):
    """ This class is used for setting display attributes when drawing through
OpenGL (âPixel formatâ in MSW and OSX parlance, âConfigsâ in X11).

        Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
    """
    def AuxBuffers(self, val: int) -> 'glcanvas.GLAttributes':
        """ Specifies the number of auxiliary buffers.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def BufferSize(self, val: int) -> 'glcanvas.GLAttributes':
        """ Specifies the number of bits for colour buffer.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def Defaults(self) -> 'glcanvas.GLAttributes':
        """ wxWidgets defaults: RGBA, Z-depth 16 bits, double buffering, 1 sample buffer, 4 samplers.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def Depth(self, val: int) -> 'glcanvas.GLAttributes':
        """ Specifies number of bits for Z-buffer.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def DoubleBuffer(self) -> 'glcanvas.GLAttributes':
        """ Requests using double buffering.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def EndList(self) -> None:
        """ The set of attributes must end with this one; otherwise, the GPU may display nothing at all.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def FrameBuffersRGB(self) -> 'glcanvas.GLAttributes':
        """ Used to request a frame buffer sRGB capable.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def Level(self, val: int) -> 'glcanvas.GLAttributes':
        """ Specifies the framebuffer level.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def MinAcumRGBA(self, mRed, mGreen, mBlue, mAlpha) -> 'glcanvas.GLAttributes':
        """ Specifies the minimal number of bits for each accumulator channel.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def MinRGBA(self, mRed, mGreen, mBlue, mAlpha) -> 'glcanvas.GLAttributes':
        """ Specifies the minimal number of bits for each colour and alpha.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def PlatformDefaults(self) -> 'glcanvas.GLAttributes':
        """ Set some typically needed attributes.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def RGBA(self) -> 'glcanvas.GLAttributes':
        """ Use True colour instead of colour index rendering for each pixel.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def SampleBuffers(self, val: int) -> 'glcanvas.GLAttributes':
        """ Use multi-sampling support (antialiasing).

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def Samplers(self, val: int) -> 'glcanvas.GLAttributes':
        """ Specifies the number of samplers per pixel.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def Stencil(self, val: int) -> 'glcanvas.GLAttributes':
        """ Specifies number of bits for stencil buffer.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def Stereo(self) -> 'glcanvas.GLAttributes':
        """ Use stereoscopic display.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """



class GLContextAttrs(GLAttribsBase):
    """ This class is used for setting context attributes.

        Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
    """
    def CompatibilityProfile(self) -> 'glcanvas.GLContextAttrs':
        """ Request a type of context with all OpenGL features from version 1.0 to the newest available by the GPU driver.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def CoreProfile(self) -> 'glcanvas.GLContextAttrs':
        """ Request an OpenGL core profile for the context.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def DebugCtx(self) -> 'glcanvas.GLContextAttrs':
        """ Request debugging functionality.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def ES2(self) -> 'glcanvas.GLContextAttrs':
        """ Request an ES or ES2 (âEmbedded Subsystemâ) context.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def EndList(self) -> None:
        """ The set of attributes must end with this one; otherwise, the GPU may display nothing at all.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def ForwardCompatible(self) -> 'glcanvas.GLContextAttrs':
        """ Request a forward-compatible context.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def LoseOnReset(self) -> 'glcanvas.GLContextAttrs':
        """ With robustness enabled, if graphics reset happens, all context state is lost.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def MajorVersion(self, val: int) -> 'glcanvas.GLContextAttrs':
        """ Request specific OpenGL core major version number (>= 3).

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def MinorVersion(self, val: int) -> 'glcanvas.GLContextAttrs':
        """ Request specific OpenGL core minor version number.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def NoResetNotify(self) -> 'glcanvas.GLContextAttrs':
        """ With robustness enabled, never deliver notification of reset events.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def OGLVersion(self, vmayor, vminor) -> 'glcanvas.GLContextAttrs':
        """ An easy way of requesting an OpenGL version.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def PlatformDefaults(self) -> 'glcanvas.GLContextAttrs':
        """ Set platform specific defaults.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def ReleaseFlush(self, val: int=1) -> 'glcanvas.GLContextAttrs':
        """ Request OpenGL to avoid or not flushing pending commands when the context is made no longer current (released).

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def ResetIsolation(self) -> 'glcanvas.GLContextAttrs':
        """ Request OpenGL to protect other applications or shared contexts from reset side-effects.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def Robust(self) -> 'glcanvas.GLContextAttrs':
        """ Request robustness, or how OpenGL handles out-of-bounds buffer object accesses and graphics reset notification behaviours.

            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """



class GLAttribsBase:
    """ This is the base class for GLAttributes and GLContextAttrs.

        Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
    """
    def __init__(self) -> None:
        """ Constructor.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    def AddAttribBits(self, searchVal, combineVal) -> None:
        """ Combine (bitwise wx.OR) a given value with the existing one, if any.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    def AddAttribute(self, attribute: int) -> None:
        """ Adds an integer value to the list of attributes.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    def GetSize(self) -> int:
        """ Returns the size of the internal list of attributes.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    def NeedsARB(self) -> bool:
        """ Returns the current value of the ARB-flag.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    def Reset(self) -> None:
        """ Delete contents and sets ARB-flag to False.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    def SetNeedsARB(self, needsARB: bool=True) -> None:
        """ Sets the necessity of using special ARB-functions (e.g.

            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    Size: int  # See GetSize



OR: int

