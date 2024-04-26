# -*- coding: utf-8 -*-
from .interfaces import ITyping, TypingType, ITypingClass, ITypingLiteral, ITypingFunction


EXTRA_KNOWN_ITEMS: list[ITyping] = []
aObj: ITypingLiteral = {
    "type": TypingType.ALIAS,
    "name": "Coord",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Char",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Double",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "CommandList",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.CommandProcessor.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "WindowList",
    "moduleName": "wx",
    "returnType": "list['Window']",
    "docstring": "WindowList is a type-safe List-like class whose elements are of type Window* .",
    "source": "https://docs.wxpython.org/wx.Window.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "intshort",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.DateTime.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "FileHistoryMenuList",
    "moduleName": "wx",
    "returnType": "'Menu'",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.FileHistory.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "MessageDialogButtonLabel",
    "moduleName": "wx",
    "returnType": "str",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.GenericMessageDialog.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "SizerItemList",
    "moduleName": "wx",
    "returnType": "list['SizerItem']",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Sizer.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "DataViewItemArray",
    "moduleName": "wx.dataview",
    "returnType": "list['DataViewItem']",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.dataview.DataViewCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "GridCellCoordsArray",
    "moduleName": "wx.grid",
    "returnType": "list['GridCellCoords']",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.grid.Grid.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "GridSelectionModes",
    "moduleName": "wx.grid",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.grid.Grid.GridSelectionModes.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Edge",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Edge.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "MenuItemList",
    "moduleName": "wx",
    "returnType": "list['MenuItem']",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Menu.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "ObjectRefData",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Object.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "PrintQuality",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.PrintData.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Point2DDouble",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Rect2D.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "TextPos",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.SearchCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "ClientData",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.SharedClientDataContainer.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "PyUserData",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.SizerItem.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "FileOffset",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.StreamBase.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "WeekDay",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.DateTime.WeekDay.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "value_type",
    "moduleName": "wx",
    "returnType": "bytes",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Unichar.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RichTextActionList",
    "moduleName": "wx.richtext",
    "returnType": "list['RichTextAction']",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.richtext.RichTextCommand.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "PGVariant",
    "moduleName": "wx.propgrid",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "byte",
    "moduleName": "wx.propgrid",
    "returnType": "bytes",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Byte",
    "moduleName": "wx",
    "returnType": "bytes",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.BusyInfoFlags.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RibbonButtonBarButtonBase",
    "moduleName": "wx.ribbon",
    "returnType": "Any",  # This should point to wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RibbonToolBarToolBase",
    "moduleName": "wx.ribbon",
    "returnType": "Any",  # This should point to wx.lib.agw.ribbon.toolbar.RibbonToolBarToolBase
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RibbonGalleryItem",
    "moduleName": "wx.ribbon",
    "returnType": "Any",  # This should point to wx.lib.agw.ribbon.gallery.RibbonGalleryItem
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "wxRichTextStyleType",
    "moduleName": "wx.richtext",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "CharBuffer",
    "moduleName": "wx.stc",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.stc.StyledTextCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "AuiPaneInfoArray",
    "moduleName": "wx.aui",
    "returnType": "list['AuiPaneInfo']",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.aui.AuiManager.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "DVCVariant",
    "moduleName": "wx.dataview",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.dataview.DataViewEvent.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "AttrKind",
    "moduleName": "wx.grid",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.grid.GridCellAttr.AttrKind.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "HtmlBookRecArray",
    "moduleName": "wx.html",
    "returnType": "list[Any]",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.html.HtmlHelpData.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "HtmlHelpDataItems",
    "moduleName": "wx.html",
    "returnType": "list[Any]",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.html.HtmlHelpData.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RichTextVariantArray",
    "moduleName": "wx.richtext",
    "returnType": "list[Any]",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.richtext.RichTextProperties.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Animation",
    "moduleName": "wx.xrc",
    "returnType": "Any",  # This should be wx.adv.Animation
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "XmlNode",
    "moduleName": "wx.xrc",
    "returnType": "Any",  # This should be wx.xml.XmlNode
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RichTextFloatCollector",
    "moduleName": "wx.richtext",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RichTextObjectPtrArrayArray",
    "moduleName": "wx.richtext",
    "returnType": "list[Any]",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.richtext.RichTextTable.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RichTextObjectPtrArray",
    "moduleName": "wx.richtext",
    "returnType": "list[Any]",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RichTextObjectPtrArray",
    "moduleName": "wx.richtext",
    "returnType": "list[Any]",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.richtext.RichTextTable.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RichTextRangeArray",
    "moduleName": "wx.richtext",
    "returnType": "list['RichTextRange']",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.richtext.RichTextSelection.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "ArrayPGProperty",
    "moduleName": "wx.propgrid",
    "returnType": "list['PGProperty']",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.propgrid.PropertyGrid.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RichTextObjectList",
    "moduleName": "wx.richtext",
    "returnType": "list['RichTextObject']",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "TextAttrDimensionFlags",
    "moduleName": "wx.richtext",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.richtext.TextAttrDimension.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Reason",
    "moduleName": "wx.ActivateEvent",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.ActivateEvent.Reason.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "ArtClient",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.ArtProvider.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Vector",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.BitmapBundle.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "EntryType",
    "moduleName": "wx.ConfigBase",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.ConfigBase.EntryType.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "LongLong_t",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.ConfigBase.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Month",
    "moduleName": "wx.DateTime",
    "returnType": "Any",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.DateTime.Month.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "ArrayVideoModes",
    "moduleName": "wx",
    "returnType": "list['VideoMode']",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Display.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "MsgCatalog",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.TranslationsLoader.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "SIP_SSIZE_T",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.GraphicsGradientStops.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "GridWindow",
    "moduleName": "wx.grid",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.grid.Grid.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "CellSpan",
    "moduleName": "wx.grid.Grid",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.grid.Grid.CellSpan.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "GridCellAttrPtr",
    "moduleName": "wx.grid",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.grid.Grid.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "TabBehaviour",
    "moduleName": "wx.grid",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.grid.Grid.TabBehaviour.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RGBValue",
    "moduleName": "wx",
    "returnType": "'Image.RGBValue'",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Image.RGBValue.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "HSVValue",
    "moduleName": "wx",
    "returnType": "'Image.HSVValue'",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Image.HSVValue.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Relationship",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.Relationship.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "LogLevel",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.Log.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.LITERAL,
    "name": "PlatformInfo",
    "moduleName": "wx",
    "returnType": "tuple[str, str, str, str, str, str, str, str, str, str]",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.PlatformInformation.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "PreviewFrameModalityKind",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.PreviewFrameModalityKind.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Rect2DDouble",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Rect2D.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "OutCode",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.OutCode.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "RegionContain",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.RegionContain.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "FileLayout",
    "moduleName": "wx.StandardPaths",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.StandardPaths.FileLayout.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Dir",
    "moduleName": "wx.StandardPaths",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.StandardPaths.Dir.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Dir",
    "moduleName": "wx",
    "returnType": "'StandardPaths.Dir'",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.StandardPaths.Dir.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "ScaleMode",
    "moduleName": "wx.StaticBitmap",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.StaticBitmap.ScaleMode.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "ScaleMode",
    "moduleName": "wx",
    "returnType": "'StaticBitmap.ScaleMode'",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.StaticBitmap.ScaleMode.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Kind",
    "moduleName": "wx.StockPreferencesPage",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.StockPreferencesPage.Kind.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "res",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.TextCompleterSimple.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "TZ",
    "moduleName": "wx.DateTime",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.DateTime.TimeZone.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "void",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.TreeItemId.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Uint16",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.UniChar.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "MemoryBuffer",
    "moduleName": "wx",
    "returnType": "Any",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.stc.StyledTextCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "WebViewIE_EmulationLevel",
    "moduleName": "wx.html2",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.html2.WebViewIE_EmulationLevel.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "PromptMode",
    "moduleName": "wx.html",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.html.HtmlEasyPrinting.PromptMode.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "FlagType",
    "moduleName": "wx.propgrid",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.propgrid.PGProperty.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "HTMLCursor",
    "moduleName": "wx.html",
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.html.HtmlWindowInterface.HTMLCursor.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
aObj = {
    "type": TypingType.ALIAS,
    "name": "Calendar",
    "moduleName": "wx",  # This should be wx.DateTime.Calendar
    "returnType": "int",
    "docstring": "Enumeration",
    "source": "https://docs.wxpython.org/wx.DateTime.Calendar.enumeration.html",
}
EXTRA_KNOWN_ITEMS.append(aObj)
lObj: ITypingLiteral = {
    "type": TypingType.LITERAL,
    "name": "PRINT_QUALITY_HIGH",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.PrintData.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "PRINT_QUALITY_MEDIUM",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.PrintData.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "PRINT_QUALITY_LOW",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.PrintData.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "PRINT_QUALITY_DRAFT",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.PrintData.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GROW",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "Synonym of wx.EXPAND",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "RA_HORIZONTAL",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "Synonym of wx.HORIZONTAL",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "RA_VERTICAL",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "Synonym of wx.VERTICAL",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "NORMAL",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "DEFAULT",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "wxEVT_COMMAND_BUTTON_CLICKED",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "RED",
    "moduleName": "wx",
    "returnType": "Colour",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "YELLOW",
    "moduleName": "wx",
    "returnType": "Colour",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "BLACK",
    "moduleName": "wx",
    "returnType": "Colour",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "WHITE",
    "moduleName": "wx",
    "returnType": "Colour",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "BLUE",
    "moduleName": "wx",
    "returnType": "Colour",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GREEN",
    "moduleName": "wx",
    "returnType": "Colour",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "CYAN",
    "moduleName": "wx",
    "returnType": "Colour",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "OPEN",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "NullBitmap",
    "moduleName": "wx",
    "returnType": "Bitmap",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "EVT_TIMER",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
cObj: ITypingClass = {
    "type": TypingType.CLASS,
    "name": "FrozenWindow",
    "moduleName": "wx",
    "source": "",
    "superClass": ["ContextManager"],
    "docstring": "Freeze the window and all its children.",
    "properties": [],
    "functions": [
        {
            "type": TypingType.FUNCTION,
            "name": "__init__",
            "moduleName": "wx.FrozenWindow",
            "returnType": "None",
            "methodType": "normal",
            "source": "",
            "docstring": "Constructor",
            "params": {
                "window": "'Window'",
            },
            "paramStr": "self, window: 'Window'",
        }, {
            "type": TypingType.FUNCTION,
            "name": "__enter__",
            "moduleName": "wx.FrozenWindow",
            "returnType": "None",
            "methodType": "normal",
            "source": "",
            "docstring": "Enter the context manager.",
            "params": {},
            "paramStr": "self",
        }, {
            "type": TypingType.FUNCTION,
            "name": "__exit__",
            "moduleName": "wx.FrozenWindow",
            "returnType": "None",
            "methodType": "normal",
            "source": "",
            "docstring": "Exit the context manager.",
            "params": {},
            "paramStr": "self, *args, **kwargs",
        }
    ],
}
EXTRA_KNOWN_ITEMS.append(cObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "NullCursor",
    "moduleName": "wx",
    "returnType": "'Cursor'",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "LIST_AUTOSIZE",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GRID_VALUE_STRING",
    "moduleName": "wx.grid",
    "returnType": "str",
    "docstring": "",
    "source": "https://github.com/wxWidgets/Phoenix/blob/master/etg/grid.py#L90",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GRID_VALUE_BOOL",
    "moduleName": "wx.grid",
    "returnType": "str",
    "docstring": "",
    "source": "https://github.com/wxWidgets/Phoenix/blob/master/etg/grid.py#L90",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GRID_VALUE_NUMBER",
    "moduleName": "wx.grid",
    "returnType": "str",
    "docstring": "",
    "source": "https://github.com/wxWidgets/Phoenix/blob/master/etg/grid.py#L90",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GRID_VALUE_FLOAT",
    "moduleName": "wx.grid",
    "returnType": "str",
    "docstring": "",
    "source": "https://github.com/wxWidgets/Phoenix/blob/master/etg/grid.py#L90",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GRID_VALUE_CHOICE",
    "moduleName": "wx.grid",
    "returnType": "str",
    "docstring": "",
    "source": "https://github.com/wxWidgets/Phoenix/blob/master/etg/grid.py#L90",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GRID_VALUE_DATE",
    "moduleName": "wx.grid",
    "returnType": "str",
    "docstring": "",
    "source": "https://github.com/wxWidgets/Phoenix/blob/master/etg/grid.py#L90",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GRID_VALUE_TEXT",
    "moduleName": "wx.grid",
    "returnType": "str",
    "docstring": "",
    "source": "https://github.com/wxWidgets/Phoenix/blob/master/etg/grid.py#L90",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GRID_VALUE_LONG",
    "moduleName": "wx.grid",
    "returnType": "str",
    "docstring": "",
    "source": "https://github.com/wxWidgets/Phoenix/blob/master/etg/grid.py#L90",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GRID_VALUE_CHOICEINT",
    "moduleName": "wx.grid",
    "returnType": "str",
    "docstring": "",
    "source": "https://github.com/wxWidgets/Phoenix/blob/master/etg/grid.py#L90",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GRID_VALUE_DATETIME",
    "moduleName": "wx.grid",
    "returnType": "str",
    "docstring": "",
    "source": "https://github.com/wxWidgets/Phoenix/blob/master/etg/grid.py#L90",
}
EXTRA_KNOWN_ITEMS.append(lObj)
fObj: ITypingFunction = {
    "type": TypingType.FUNCTION,
    "name": "NewCommandEvent",
    "methodType": "normal",
    "moduleName": "wx.lib.newevent",
    "returnType": "tuple[type['Event'], 'PyEventBinder']",
    "params": {},
    "paramStr": "",
    "docstring": "Generates a new (command_event, binder) tuple.",
    "source": "https://docs.wxpython.org/wx.lib.newevent.html",
}
EXTRA_KNOWN_ITEMS.append(fObj)
fObj = {
    "type": TypingType.FUNCTION,
    "name": "NewEvent",
    "methodType": "normal",
    "moduleName": "wx.lib.newevent",
    "returnType": "tuple[type['Event'], 'PyEventBinder']",
    "params": {},
    "paramStr": "",
    "docstring": "Generates a new (event, binder) tuple.",
    "source": "https://docs.wxpython.org/wx.lib.newevent.html",
}
EXTRA_KNOWN_ITEMS.append(fObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "DefaultValidator",
    "moduleName": "wx",
    "returnType": "Validator",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Validator.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "DefaultPosition",
    "moduleName": "wx",
    "returnType": "Position",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Point.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ABOVE",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "Above the client area.",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html#wx.TreeCtrl.HitTest",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_BELOW",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "Below the client area.",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html#wx.TreeCtrl.HitTest",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_NOWHERE",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "In the client area but below the last item.",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html#wx.TreeCtrl.HitTest",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMBUTTON",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "On the button associated with an item.",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html#wx.TreeCtrl.HitTest",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMICON",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "On the bitmap associated with an item.",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html#wx.TreeCtrl.HitTest",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMINDENT",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "In the indentation associated with an item.",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html#wx.TreeCtrl.HitTest",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMLABEL",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "On the label (string) associated with an item.",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html#wx.TreeCtrl.HitTest",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMRIGHT",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "In the area to the right of an item.",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html#wx.TreeCtrl.HitTest",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMSTATEICON",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "On the state icon for a tree view item that is in a user-defined state.",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html#wx.TreeCtrl.HitTest",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_TOLEFT",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "To the right of the client area.",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html#wx.TreeCtrl.HitTest",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_TORIGHT",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "To the left of the client area.",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html#wx.TreeCtrl.HitTest",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "wxEVT_COMMAND_TREE_END_DRAG",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TheColourDatabase",
    "moduleName": "wx",
    "returnType": "ColourDatabase",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.ColourDatabase.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TheClipboard",
    "moduleName": "wx",
    "returnType": "Clipboard",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.Clipboard.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "DD_NEW_DIR_BUTTON",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "SOLID",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.DC.html#wx.DC.DrawTextList",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "GREY",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
fObj = {
    "type": TypingType.FUNCTION,
    "name": "DrawSavedLines",
    "methodType": "normal",
    "moduleName": "wx.Panel",
    "className": "wx.Panel",
    "returnType": "None",
    "params": {"dc": "'DC'"},
    "paramStr": "self, dc: 'DC'",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(fObj)
fObj = {
    "type": TypingType.FUNCTION,
    "name": "EndDrawing",
    "methodType": "normal",
    "moduleName": "wx.DC",
    "className": "wx.DC",
    "returnType": "None",
    "params": {},
    "paramStr": "self",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(fObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "CHOICEDLG_STYLE",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.SingleChoiceDialog.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
fObj = {
    "type": TypingType.FUNCTION,
    "name": "SetClippingRect",
    "methodType": "normal",
    "moduleName": "wx.ClientDC",
    "className": "wx.ClientDC",
    "returnType": "None",
    "params": {"rect": "'Rect'"},
    "paramStr": "self, rect: 'Rect'",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(fObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TRANSPARENT",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "LOG_FatalError",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/log_classes_overview.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "LOG_Error",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/log_classes_overview.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "EVT_CALENDAR_DAY",
    "moduleName": "wx",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.adv.CalendarCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
fObj = {
    "type": TypingType.FUNCTION,
    "name": "SetUpperDateLimit",
    "methodType": "normal",
    "moduleName": "wx.adv.CalendarCtrl",
    "className": "wx.adv.CalendarCtrl",
    "returnType": "None",
    "params": {
        "date": "'DateTime'",
    },
    "paramStr": "self, date: 'DateTime'",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(fObj)
fObj = {
    "type": TypingType.FUNCTION,
    "name": "SetLowerDateLimit",
    "methodType": "normal",
    "moduleName": "wx.adv.CalendarCtrl",
    "className": "wx.adv.CalendarCtrl",
    "returnType": "None",
    "params": {
        "date": "'DateTime'",
    },
    "paramStr": "self, date: 'DateTime'",
    "docstring": "",
    "source": "",
}
EXTRA_KNOWN_ITEMS.append(fObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_ALIGN_DEFAULT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_ALIGN_SNAP_TO_GRID",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_VRULES",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_HRULES",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_ICON",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_SMALL_ICON",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_LIST",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_REPORT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_ALIGN_TOP",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_ALIGN_LEFT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_AUTOARRANGE",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_VIRTUAL",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_EDIT_LABELS",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_NO_HEADER",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_NO_SORT_HEADER",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_SINGLE_SEL",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_SORT_ASCENDING",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_SORT_DESCENDING",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_TILE",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_NO_HIGHLIGHT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_STICKY_HIGHLIGHT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_STICKY_NOSELEVENT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_SEND_LEFTCLICK",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_HAS_VARIABLE_ROW_HEIGHT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_AUTO_CHECK_CHILD",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_AUTO_TOGGLE_CHILD",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_AUTO_CHECK_PARENT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_SHOW_TOOLTIPS",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_HOT_TRACKING",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_BORDER_SELECT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_TRACK_SELECT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_HEADER_IN_ALL_VIEWS",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_NO_FULL_ROW_SELECT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_FOOTER",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_USER_ROW_HEIGHT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_FORMAT_LEFT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_FORMAT_RIGHT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_FORMAT_CENTRE",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_FORMAT_CENTER",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_STATE",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_TEXT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_IMAGE",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_DATA",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_WIDTH",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_FORMAT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_FONTCOLOUR",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_FONT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_BACKCOLOUR",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_KIND",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_ENABLE",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_CHECK",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_HYPERTEXT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_WINDOW",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_PYDATA",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_SHOWN",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_RENDERER",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_OVERFLOW",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_FOOTER_TEXT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_FOOTER_IMAGE",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_FOOTER_FORMAT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_FOOTER_FONT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_FOOTER_CHECK",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_MASK_FOOTER_KIND",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_STATE_DONTCARE",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_STATE_DROPHILITED",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_STATE_FOCUSED",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_STATE_SELECTED",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_STATE_CUT",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_STATE_DISABLED",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_STATE_FILTERED",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_STATE_INUSE",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_STATE_PICKED",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "ULC_STATE_SOURCE",
    "moduleName": "wx.lib.agw.ultimatelistctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_VC71",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_FANCY_TABS",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_TABS_BORDER_SIMPLE",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_NO_X_BUTTON",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_NO_NAV_BUTTONS",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_MOUSE_MIDDLE_CLOSES_TABS",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_BOTTOM",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_NODRAG",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_VC8",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_X_ON_TAB",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_BACKGROUND_GRADIENT",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_COLOURFUL_TABS",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_DCLICK_CLOSES_TABS",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_SMART_TABS",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_DROPDOWN_TABS_LIST",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_ALLOW_FOREIGN_DND",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_HIDE_ON_SINGLE_TAB",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_DEFAULT_STYLE",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_FF2",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_NO_TAB_FOCUS",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_RIBBON_TABS",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_HIDE_TABS",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "FNB_NAV_BUTTONS_WHEN_NEEDED",
    "moduleName": "wx.lib.agw.flatnotebook",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "AUI_BUTTON_STATE_NORMAL",
    "moduleName": "wx.lib.agw.aui.auibar",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "AUI_BUTTON_STATE_HOVER",
    "moduleName": "wx.lib.agw.aui.auibar",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "AUI_BUTTON_STATE_PRESSED",
    "moduleName": "wx.lib.agw.aui.auibar",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "AUI_BUTTON_STATE_DISABLED",
    "moduleName": "wx.lib.agw.aui.auibar",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "AUI_BUTTON_STATE_HIDDEN",
    "moduleName": "wx.lib.agw.aui.auibar",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "AUI_BUTTON_STATE_CHECKED",
    "moduleName": "wx.lib.agw.aui.auibar",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TreeItemIcon_Normal",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TreeItemIcon_Selected",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TreeItemIcon_Expanded",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TreeItemIcon_SelectedExpanded",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.TreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ABOVE",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_BELOW",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_NOWHERE",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMBUTTON",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMICON",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMINDENT",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMLABEL",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEM",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMRIGHT",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_TOLEFT",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_TORIGHT",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMUPPERPART",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMLOWERPART",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "TREE_HITTEST_ONITEMCHECKICON",
    "moduleName": "wx.lib.agw.customtreectrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "EVT_INT",
    "moduleName": "wx.lib.intctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "WXK_CTRL_V",
    "moduleName": "wx.lib.intctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "WXK_CTRL_X",
    "moduleName": "wx.lib.intctrl",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
    "type": TypingType.LITERAL,
    "name": "EVT_CALENDAR_DAY",
    "moduleName": "wx.adv",
    "returnType": "int",
    "docstring": "",
    "source": "https://docs.wxpython.org/wx.adv.CalendarCtrl.html",
}
EXTRA_KNOWN_ITEMS.append(lObj)
