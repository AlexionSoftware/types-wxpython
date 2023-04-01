# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class XmlResource(Object):
    """ This is the main class for interacting with the XML-based resource
system.

        Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def AddHandler(self, handler: 'xrc.XmlResourceHandler') -> None:
        """ Initializes only a specific handler (or custom handler).

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def AddSubclassFactory(factory: 'xrc.XmlSubclassFactory') -> None:
        """ Registers subclasses factory for use in XRC.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def AttachUnknownControl(self, name, control, parent=None) -> bool:
        """ Attaches an unknown control to the given panel/window/dialog.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def ClearHandlers(self) -> None:
        """ Removes all handlers and deletes them (this means that any handlers added using AddHandler   must be allocated on the heap).

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def CompareVersion(self, major, minor, release, revision) -> int:
        """ Compares the XRC version to the argument.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def FindXRCIDById(numId: int) -> str:
        """ Returns a string ID corresponding to the given numeric ID.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def Get() -> 'xrc.XmlResource':
        """ Gets the global resources object or creates one if none exists.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def GetDomain(self) -> str:
        """ Returns the domain (message catalog) that will be used to load translatable strings in the XRC.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def GetFlags(self) -> int:
        """ Returns flags, which may be a bitlist of   wx.xrc.XmlResourceFlags  enumeration values.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def GetResourceNode(self, name: str) -> 'xrc.XmlNode':
        """ Returns the   wx.xml.XmlNode  containing the definition of the object with the given name or None.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def GetVersion(self) -> int:
        """ Returns version information (a.b.c.d = d + 256c + 2562b + 2563a).

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def GetXRCID(str_id, value_if_not_found=ID_NONE) -> int:
        """ Returns a numeric ID that is equivalent to the string ID used in an XML resource.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def InitAllHandlers(self) -> None:
        """ Initializes handlers for all supported controls/windows.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def InsertHandler(self, handler: 'xrc.XmlResourceHandler') -> None:
        """ Add a new handler at the beginning of the handler list.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def Load(self, filemask: str) -> bool:
        """ Loads resources from XML files that match given filemask.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadAllFiles(self, dirname: str) -> bool:
        """ Loads all .xrc files from directory dirname.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadBitmap(self, name: str) -> 'Bitmap':
        """ Loads a bitmap resource from a file.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadDialog(self, *args, **kw) -> 'Dialog':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadDocument(self, doc, name="") -> bool:
        """ Load resources from the XML document containing them.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadFile(self, file: str) -> bool:
        """ Simpler form of Load   for loading a single XRC file.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadFrame(self, *args, **kw) -> 'Frame':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadFromBuffer(self, data) -> bool:
        """ Load the resource from a bytes string or other data buffer compatible object.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadIcon(self, name: str) -> 'Icon':
        """ Loads an icon resource from a file.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadMenu(self, name: str) -> 'Menu':
        """ Loads menu from resource.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadMenuBar(self, *args, **kw) -> 'MenuBar':
        """ Loads a menubar from resource.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadObject(self, *args, **kw) -> 'Window':
        """ Load an object from the resource specifying both the resource name and the class name.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadObjectRecursively(self, *args, **kw) -> 'Window':
        """ Load an object from anywhere in the resource tree.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadPanel(self, *args, **kw) -> 'Panel':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadToolBar(self, parent, name) -> 'ToolBar':
        """ Loads a toolbar.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def Set(res: 'xrc.XmlResource') -> 'xrc.XmlResource':
        """ Sets the global resources object and returns a pointer to the previous one (may be None).

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def SetDomain(self, domain: str) -> None:
        """ Sets the domain (message catalog) that will be used to load translatable strings in the XRC.

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def SetFlags(self, flags: int) -> None:
        """ Sets flags (bitlist of   wx.xrc.XmlResourceFlags  enumeration values).

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def Unload(self, filename: str) -> bool:
        """ This function unloads a resource previously loaded by Load .

            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    Domain: str  # See GetDomain and SetDomain
    Flags: int  # See GetFlags and SetFlags
    Version: int  # See GetVersion



class XmlResourceHandler(Object):
    """ SizerXmlHandler is a class for resource handlers capable of creating
a Sizer object from an XML node.

        Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
    """
    def __init__(self) -> None:
        """ Default constructor.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def AddStyle(self, name, value) -> None:
        """ Add a style flag (e.g.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def AddWindowStyles(self) -> None:
        """ Add styles common to all Window-derived classes.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CanHandle(self, node: 'xml.XmlNode') -> bool:
        """ Returns True if it understands this node and can create a resource from it, False otherwise.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CreateChildren(self, parent, this_hnd_only=False) -> None:
        """ Creates children.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CreateChildrenPrivately(self, parent, rootnode=None) -> None:
        """ Helper function.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CreateResFromNode(self, node, parent, instance=None) -> 'Window':
        """ Creates a resource from a node.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CreateResource(self, node, parent, instance) -> 'Window':
        """ Creates an object (menu, dialog, control, â¦) from an XML node.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def DoCreateResource(self) -> 'Window':
        """ Called from CreateResource after variables were filled.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetAnimation(self, param="animation", ctrl=None) -> 'xrc.Animation':
        """ Creates an animation (see   wx.adv.Animation) from the filename specified in param.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetBitmap(self, *args, **kw) -> 'Bitmap':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetBitmapBundle(self, *args, **kw) -> 'BitmapBundle':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetBool(self, param, defaultv=False) -> bool:
        """ Gets a bool flag (1, t, yes, on, True are True, everything else is False).

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetClass(self) -> str:
        """ After CreateResource has been called this will return the class name of the XML resource node being processed.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetColour(self, param, defaultColour=NullColour) -> 'Colour':
        """ Gets colour in HTML syntax (#``RRGGBB``).

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetCurFileSystem(self) -> 'FileSystem':
        """ Returns the current file system.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetDimension(self, param, defaultv=0, windowToUse=0) -> 'Coord':
        """ Gets a dimension (may be in dialog units).

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetDirection(self, param, dirDefault=LEFT) -> int:
        """ Gets a direction.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetFloat(self, param, defaultv=0) -> float:
        """ Gets a float value from the parameter.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetFont(self, param: str="font") -> 'Font':
        """ Gets a font.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetID(self) -> int:
        """ Returns the wx.xrc.XRCID.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetIcon(self, *args, **kw) -> 'Icon':
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetIconBundle(self, param, defaultArtClient=ART_OTHER) -> 'IconBundle':
        """ Returns an icon bundle.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetImageList(self, param: str="imagelist") -> 'ImageList':
        """ Creates an image list from the param  markup data.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetInstance(self) -> 'Window':
        """ After CreateResource has been called this will return the instance that the XML resource content should be created upon, if it has already been created.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetLong(self, param, defaultv=0) -> int:
        """ Gets the integer value from the parameter.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetName(self) -> str:
        """ Returns the resource name.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNode(self) -> 'xrc.XmlNode':
        """ After CreateResource has been called this will return the XML node being processed.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNodeChildren(self, node: 'xml.XmlNode') -> 'xrc.XmlNode':
        """ Gets the first child of the given node or None.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNodeContent(self, node: 'xml.XmlNode') -> str:
        """ Gets node content from wx.xml.XML_ENTITY_NODE.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNodeNext(self, node: 'xml.XmlNode') -> 'xrc.XmlNode':
        """ Gets the next sibling node related to the given node, possibly None.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNodeParent(self, node: 'xml.XmlNode') -> 'xrc.XmlNode':
        """ Gets the parent of the node given.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetParamNode(self, param: str) -> 'xrc.XmlNode':
        """ Finds the node or returns None.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetParamValue(self, *args, **kw) -> str:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetParent(self) -> 'Window':
        """ After CreateResource has been called this will return the current itemâs parent, if any.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetParentAsWindow(self) -> 'Window':
        """ After CreateResource has been called this will return the itemâs parent as a   wx.Window.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetPosition(self, param: str="pos") -> 'Point':
        """ Gets the position (may be in dialog units).

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetResource(self) -> 'xrc.XmlResource':
        """ After CreateResource has been called this will return the current   wx.xrc.XmlResource  object.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetSize(self, param="size", windowToUse=0) -> 'Size':
        """ Gets the size (may be in dialog units).

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetStyle(self, param="style", defaults=0) -> int:
        """ Gets style flags from text in form âflag | flag2| flag3 |â¦â Only understands flags added with AddStyle .

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetText(self, param, translate=True) -> str:
        """ Gets text from param and does some conversions:

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def HasParam(self, param: str) -> bool:
        """ Check to see if a parameter exists.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def IsObjectNode(self, node: 'xml.XmlNode') -> bool:
        """ Checks if the given node is an object node.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def IsOfClass(self, node, classname) -> bool:
        """ Convenience function.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def ReportError(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def ReportParamError(self, param, message) -> None:
        """ Like ReportError , but uses the node of parameter param  of the currently processed object as the context.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def SetParentResource(self, res: 'xrc.XmlResource') -> None:
        """ Sets the parent resource.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def SetupWindow(self, wnd: 'Window') -> None:
        """ Sets common window options.

            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    Animation: 'xrc.Animation'  # See GetAnimation
    Bitmap: '_Bitmap'  # See GetBitmap
    BitmapBundle: '_BitmapBundle'  # See GetBitmapBundle
    Class: str  # See GetClass
    CurFileSystem: 'FileSystem'  # See GetCurFileSystem
    Font: '_Font'  # See GetFont
    ID: int  # See GetID
    Icon: '_Icon'  # See GetIcon
    ImageList: '_ImageList'  # See GetImageList
    Instance: 'Window'  # See GetInstance
    Name: str  # See GetName
    Node: 'xrc.XmlNode'  # See GetNode
    Parent: 'Window'  # See GetParent
    ParentAsWindow: 'Window'  # See GetParentAsWindow
    Position: 'Point'  # See GetPosition
    Resource: 'xrc.XmlResource'  # See GetResource
    Size: '_Size'  # See GetSize
    Style: int  # See GetStyle



XRCID: int

XML_ENTITY_NODE: int

XmlResourceFlags: TypeAlias = int  # Enumeration

XRC_USE_LOCALE: int

XRC_NO_SUBCLASSING: int

XRC_NO_RELOADING: int

XRC_USE_ENVVARS: int

class XmlSubclassFactory:
    """ className (String) â 

        Source: https://docs.wxpython.org/wx.xrc.XmlSubclassFactory.html
    """
    def __init__(self) -> None:
        """ 

            Source: https://docs.wxpython.org/wx.xrc.XmlSubclassFactory.html
        """

    def Create(self, className: str) -> 'Window':
        """ className (String) â

            Source: https://docs.wxpython.org/wx.xrc.XmlSubclassFactory.html
        """



Animation: TypeAlias = Any

XmlNode: TypeAlias = Any

