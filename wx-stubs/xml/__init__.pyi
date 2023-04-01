# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, TypeAlias, Union

class XmlDocument(Object):
    """ This class holds XML data/document as parsed by XML parser in the root
node.

        Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def AppendToProlog(self, node: 'xml.XmlNode') -> None:
        """ Appends a Process Instruction or Comment node to the document prologue.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def DetachDocumentNode(self) -> 'xml.XmlNode':
        """ Detaches the document node and returns it.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def DetachRoot(self) -> 'xml.XmlNode':
        """ Detaches the root entity node and returns it.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetDoctype(self) -> 'xml.XmlDoctype':
        """ Returns the DOCTYPE declaration data for the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetDocumentNode(self) -> 'xml.XmlNode':
        """ Returns the document node of the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetEOL(self) -> str:
        """ Returns the output line ending string used for documents.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetFileEncoding(self) -> str:
        """ Returns encoding of document (may be empty).

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetFileType(self) -> 'TextFileType':
        """ Returns the output line ending format used for documents.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    @staticmethod
    def GetLibraryVersionInfo() -> 'VersionInfo':
        """ Get expat library version information.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetRoot(self) -> 'xml.XmlNode':
        """ Returns the root element node of the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetVersion(self) -> str:
        """ Returns the version of document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def IsOk(self) -> bool:
        """ Returns True if the document has been loaded successfully.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def Load(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def Save(self, *args, **kw) -> bool:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetDoctype(self, doctype: 'xml.XmlDoctype') -> None:
        """ Sets the data which will appear in the DOCTYPE declaration when the document is saved.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetDocumentNode(self, node: 'xml.XmlNode') -> None:
        """ Sets the document node of this document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetFileEncoding(self, encoding: str) -> None:
        """ Sets the encoding of the file which will be used to save the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetFileType(self, fileType: TextFileType) -> None:
        """ Sets the output line ending formats when the document is saved.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetRoot(self, node: 'xml.XmlNode') -> None:
        """ Sets the root element node of this document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetVersion(self, version: str) -> None:
        """ Sets the version of the XML file which will be used to save the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    Doctype: 'xml.XmlDoctype'  # See GetDoctype and SetDoctype
    DocumentNode: 'xml.XmlNode'  # See GetDocumentNode and SetDocumentNode
    EOL: str  # See GetEOL
    FileEncoding: str  # See GetFileEncoding and SetFileEncoding
    FileType: 'TextFileType'  # See GetFileType and SetFileType
    Root: 'xml.XmlNode'  # See GetRoot and SetRoot
    Version: str  # See GetVersion and SetVersion



XMLDOC_KEEP_WHITESPACE_NODES: int

class XmlNode:
    """ Represents a node in an XML document.

        Source: https://docs.wxpython.org/wx.xml.XmlNode.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def AddAttribute(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def AddChild(self, child: 'xml.XmlNode') -> None:
        """ Adds node child  as the last child of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def DeleteAttribute(self, name: str) -> bool:
        """ Removes the first attributes which has the given name  from the list of attributes for this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetAttribute(self, attrName, defaultVal="") -> str:
        """ Returns the value of the attribute named attrName  if it does exist.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetAttributes(self) -> 'xml.XmlAttribute':
        """ Return a pointer to the first attribute of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetChildren(self) -> 'xml.XmlNode':
        """ Returns the first child of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetContent(self) -> str:
        """ Returns the content of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetDepth(self, grandparent: Optional['xml.XmlNode']=None) -> int:
        """ Returns the number of nodes which separate this node from  grandparent .

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetLineNumber(self) -> int:
        """ Returns line number of the node in the input XML file or  -1   if it is unknown.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetName(self) -> str:
        """ Returns the name of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetNext(self) -> 'xml.XmlNode':
        """ Returns a pointer to the sibling of this node or None if there are no siblings.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetNoConversion(self) -> bool:
        """ Returns a flag indicating whether encoding conversion is necessary when saving.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetNodeContent(self) -> str:
        """ Returns the content of the first child node of type  XML_TEXT_NODE   or   XML_CDATA_SECTION_NODE .

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetParent(self) -> 'xml.XmlNode':
        """ Returns a pointer to the parent of this node or None if this node has no parent.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetType(self) -> 'xml.XmlNodeType':
        """ Returns the type of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def HasAttribute(self, attrName: str) -> bool:
        """ Returns True if this node has a attribute named attrName.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def InsertChild(self, child, followingNode) -> bool:
        """ Inserts the child  node immediately before followingNode  in the children list.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def InsertChildAfter(self, child, precedingNode) -> bool:
        """ Inserts the child  node immediately after precedingNode  in the children list.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def IsWhitespaceOnly(self) -> bool:
        """ Returns True if the content of this node is a string containing only whitespaces (spaces, tabs, new lines, etc).

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def RemoveChild(self, child: 'xml.XmlNode') -> bool:
        """ Removes the given node from the children list.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetContent(self, con: str) -> None:
        """ Sets the content of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetName(self, name: str) -> None:
        """ Sets the name of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetNext(self, next: 'xml.XmlNode') -> None:
        """ Sets as sibling the given node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetNoConversion(self, noconversion: bool) -> None:
        """ Sets a flag to indicate whether encoding conversion is necessary when saving.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetParent(self, parent: 'xml.XmlNode') -> None:
        """ Sets as parent the given node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetType(self, type: XmlNodeType) -> None:
        """ Sets the type of this node.

            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    Attributes: 'xml.XmlAttribute'  # See GetAttributes
    Children: 'xml.XmlNode'  # See GetChildren
    Content: str  # See GetContent and SetContent
    Depth: int  # See GetDepth
    LineNumber: int  # See GetLineNumber
    Name: str  # See GetName and SetName
    Next: 'xml.XmlNode'  # See GetNext and SetNext
    NoConversion: bool  # See GetNoConversion and SetNoConversion
    NodeContent: str  # See GetNodeContent
    Parent: 'xml.XmlNode'  # See GetParent and SetParent
    Type: 'xml.XmlNodeType'  # See GetType and SetType



class XmlAttribute:
    """ Represents a node attribute.

        Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
    """
    def __init__(self, *args, **kw) -> None:
        """ Overloaded Implementations:

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def GetName(self) -> str:
        """ Returns the name of this attribute.

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def GetNext(self) -> 'xml.XmlAttribute':
        """ Returns the sibling of this attribute or None if there are no siblings.

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def GetValue(self) -> str:
        """ Returns the value of this attribute.

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def SetName(self, name: str) -> None:
        """ Sets the name of this attribute.

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def SetNext(self, next: 'xml.XmlAttribute') -> None:
        """ Sets the sibling of this attribute.

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def SetValue(self, value: str) -> None:
        """ Sets the value of this attribute.

            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    Name: str  # See GetName and SetName
    Next: 'xml.XmlAttribute'  # See GetNext and SetNext
    Value: str  # See GetValue and SetValue



class XmlDoctype:
    """ Represents a DOCTYPE Declaration.

        Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
    """
    def __init__(self, rootName="", systemId="", publicId="") -> None:
        """ Creates and possible initializes the DOCTYPE.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def Clear(self) -> None:
        """ Removes all the DOCTYPE values.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def GetFullString(self) -> str:
        """ Returns the formatted DOCTYPE contents.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def GetPublicId(self) -> str:
        """ Returns the public id of the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def GetRootName(self) -> str:
        """ Returns the root name of the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def GetSystemId(self) -> str:
        """ Returns the system id of the document.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def IsValid(self) -> bool:
        """ Returns True if the contents can produce a valid DOCTYPE string.

            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    FullString: str  # See GetFullString
    PublicId: str  # See GetPublicId
    RootName: str  # See GetRootName
    SystemId: str  # See GetSystemId



XmlNodeType: TypeAlias = int  # Enumeration

XML_ELEMENT_NODE: int

XML_ATTRIBUTE_NODE: int

XML_TEXT_NODE: int

XML_CDATA_SECTION_NODE: int

XML_ENTITY_REF_NODE: int

XML_ENTITY_NODE: int

XML_PI_NODE: int

XML_COMMENT_NODE: int

XML_DOCUMENT_NODE: int

XML_DOCUMENT_TYPE_NODE: int

XML_DOCUMENT_FRAG_NODE: int

XML_NOTATION_NODE: int

XML_HTML_DOCUMENT_NODE: int

