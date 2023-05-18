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
	"name": "Reason",
	"moduleName": "wx",  # This should be wx.ActivateEvent.Reason
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
	"name": "EntryType",
	"moduleName": "wx",  # This should be wx.ConfigBase.EntryType
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
	"name": "Country",
	"moduleName": "wx",
	"returnType": "wx.DateTime.Country",
	"docstring": "Enumeration",
	"source": "https://docs.wxpython.org/wx.DateTime.Country.enumeration.html",
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
	"type": TypingType.ALIAS,
	"name": "PlatformInfo",
	"moduleName": "wx",
	"returnType": "PlatformInformation",
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
	"name": "FileLayout",
	"moduleName": "wx",
	"returnType": "'StandardPaths.FileLayout'",
	"docstring": "Enumeration",
	"source": "https://docs.wxpython.org/wx.StandardPaths.FileLayout.enumeration.html",
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
	"name": "Kind",
	"moduleName": "wx",
	"returnType": "'StockPreferencesPage.Kind'",
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
