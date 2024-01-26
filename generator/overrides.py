# -*- coding: utf-8 -*-
from typing import Any

OVERRIDES: dict[str, dict[str, Any]] = {
    "wx.ListCtrl.GetFirstSelected": {
        "returnType": "int",
    },
    "wx.ListCtrl.GetNextSelected": {
        "returnType": "int",
    },
    "wx.ListCtrl.GetFocusedItem": {
        "returnType": "int",
    },
    "wx.NewIdRef": {
        "returnType": "int",
    },
    "wx.ListCtrl.OnGetItemAttr": {
        "returnType": "Optional['ItemAttr']",
    },
    "wx.TreeCtrl.GetItemData": {
        "returnType": "Any",
    },
    "wx.TreeCtrl.GetFirstChild": {
        "returnType": "tuple['TreeItemId', str]",
    },
    "wx.TreeCtrl.GetNextChild": {
        "returnType": "tuple['TreeItemId', str]",
    },
    "wx.GetApp": {
        "returnType": "'App'",
    },
    "wx.App": {
        "superClass": ["PyApp", "AppConsole"],
    },
    "wx.App.Get": {
        "returnType": "'App'",
    },
    "wx.Object.Destroy": {
        "returnType": "bool",  # Destroy should always returns True; https://docs.wxpython.org/wx.Window.html#wx.Window.Destroy
    },
    "wx.Window.Destroy": {
        "returnType": "bool",  # Destroy should always returns True; https://docs.wxpython.org/wx.Window.html#wx.Window.Destroy
    },
    "wx.dataview.DataViewListCtrl.GetValue": {
        "returnType": "Any",
    },
    "wx.dataview.DataViewModel.GetValue": {
        "returnType": "Any",
    },
    "wx.dataview.DataViewRenderer.GetValue": {
        "returnType": "Any",
    },
    "wx.dataview.DataViewRenderer.GetValueFromEditorCtrl": {
        "returnType": "Any",
    },
    "wx.dataview.DataViewCustomRenderer.GetValueFromEditorCtrl": {
        "returnType": "Any",
    },
    "wx.grid.GridCellAttr.GetEditorPtr": {
        "returnType": "'grid.GridCellEditor'",
    },
    "wx.adv.Animation.GetHandlers": {
        "returnType": "list['adv.AnimationHandler']",
    },
    "wx.richtext.RichTextObject.CalculateRange": {
        "returnType": "None",
    },
    "wx.richtext.RichTextProperties.FindOrCreateProperty": {
        "returnType": "Any",
    },
    "wx.richtext.RichTextProperties.GetProperty": {
        "returnType": "Any",
    },
    "wx.richtext.RichTextProperties.SetProperty": {
        "params": {
            "props": "Any"
        },
        "paramStr": "self, props: Any"
    },
    "wx.richtext.RichTextProperties.SetProperties": {
        "params": {
            "props": "Any"
        }
    },
    "wx.richtext.RichTextBuffer.GetDrawingHandlers": {
        "returnType": "list['richtext.RichTextDrawingHandler']",
    },
    "wx.richtext.RichTextBuffer.GetHandlers": {
        "returnType": "list['richtext.RichTextFileHandler']",
    },
    "wx.richtext.RichTextTable.CalculateRange": {
        "returnType": "None",
    },
    "wx.richtext.RichTextField.CalculateRange": {
        "returnType": "None",
    },
    "wx.propgrid.PropertyGridInterface.GetPropertyValueAsULongLong": {
        "returnType": "int",
    },
    "wx.dataview.DataViewListStore.GetValueByRow": {
        "returnType": "Any",
    },
    "wx.dataview.DataViewListModel.GetValueByRow": {
        "returnType": "Any",
    },
    "wx.richtext.RichTextPlainText.CalculateRange": {
        "returnType": "None",
    },
    "wx.richtext.RichTextCompositeObject.CalculateRange": {
        "returnType": "None",
    },
    "wx.richtext.RichTextParagraph.CalculateRange": {
        "returnType": "None",
    },
    "wx.richtext.RichTextParagraph.MoveFromList": {
        "params": {
            "list": "list['richtext.RichTextList']"
        },
        "paramStr": "self, list: list['richtext.RichTextList']"
    },
    "wx.lib.buttons.GenButton.GetBezelWidth": {
        "returnType": "int",
    },
    "wx.lib.buttons.GenButton.SetBezelWidth": {
        "params": {
            "width": "int"
        },
        "paramStr": "self, width: int"
    },
    "wx.lib.calendar.Calendar.GetColor": {
        "params": {
            "color": "str"
        },
        "paramStr": "self, color: str"
    },
    "wx.DC.GetCGContext": {
        "returnType": "int",
    },
    "wx.DC.GetGdkDrawable": {
        "returnType": "int",
    },
    "wx.DC.GetHandle": {
        "returnType": "int",
    },
    "wx.DC.CGContext": {
        "returnType": "int",
    },
    "wx.DC.GdkDrawable": {
        "returnType": "int",
    },
    "wx.DC.Handle": {
        "returnType": "int",
    },
    "wx.ListEvent.GetData": {
        "returnType": "int",
    },
    "wx.ListEvent.Data": {
        "returnType": "int",
    },
    "wx.dataview.DataViewListCtrl.GetItemData":{
        "returnType": "int",
    },
    "wx.dataview.DataViewListStore.GetItemData": {
        "returnType": "int",
    },
    "wx.propgrid.PGChoices.GetId": {
        "returnType": "int",
    },
    "wx.propgrid.PGChoices.Id": {
        "returnType": "int",
    },
    "wx.Colour.GetPixel": {
        "returnType": "int",
    },
    "wx.Colour.Pixel": {
        "returnType": "int",
    },
    "wx.stc.StyledTextCtrl.SendMsg": {
        "returnType": "int",
    },
    "wx.StaticBitmap.SetBitmap": {
        "params": {
            "label": "Union['Bitmap', 'BitmapBundle']"
        },
        "paramStr": "self, label: Union['Bitmap', 'BitmapBundle']",
    },
    "wx.dataview.TreeListCtrl.DeleteColumn": {
        "params": {
            "col": "int"
        },
        "returnType": "bool",
        "paramStr": "self, col: int"
    },
    "wx.version": {
        "returnType": "str",
    },
    "wx.CallLater.IsRunning": {
        "returnType": "bool",
    },
    "wx.DateTime.IsDST": {
        "params": {
            "country": "'DateTime.Country'"
        }
    },
    "wx.DateTime.IsWestEuropeanCountry": {
        "params": {
            "country": "'DateTime.Country'"
        }
    },
    "wx.DateTime.IsWorkDay": {
        "params": {
            "country": "'DateTime.Country'"
        }
    },
    "wx.DateTime.SetCountry": {
        "params": {
            "country": "'DateTime.Country'"
        }
    },
    "wx.StandardPaths.SetFileLayout": {
        "params": {
            "layout": "'StandardPaths.FileLayout'"
        }
    },
    "wx.StockPreferencesPage.__init__": {
        "params": {
            "kind": "'StockPreferencesPage.Kind'"
        }
    },
    "wx.Scrolled": {
        "superClass": ["wx.Window"],
    },
    "wx.grid.Grid": {
        "superClass": ["wx.Scrolled"],
    },
    "wx.Window.GetHandle": {
        "returnType": "Any"
    },
    "wx.Window.GetClientSize": {
        "returnType": "'Rect'"
    },
    "wx.TreeCtrl.HitTest": {
        "params": {
            "point": "Union['Point', tuple[int, int]]",
            "flags": "Optional[int]"
        },
        "paramStr": "self, point: Union['Point', tuple[int, int]], flags: Optional[int] = None",
        "returnType": "tuple['TreeItemId', int]",
    },
    "wx.ScrolledWindow": {
        "superClass": ["wx.Scrolled"],
    },
    "wx.ListCtrl.IsSelected": {
        "returnType": "bool"
    },
    "wx.DC.GetTextExtent": {
        "returnType": "'Size'"
    },
    "wx.ColourDatabase.FindColour": {
        "returnType": "'Colour'"
    },
    "wx.Image.ConvertToBitmap": {
        "returnType": "'Bitmap'"
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetNextExpanded": {
        "params": {
            "item": "'GenericTreeItem'"
        },
        "paramStr": "self, item: 'GenericTreeItem'",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetPrevExpanded": {
        "params": {
            "item": "'GenericTreeItem'"
        },
        "paramStr": "self, item: 'GenericTreeItem'",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.HasAGWFlag": {
        "params": {
            "flag": "int"
        },
        "paramStr": "self, flag: int",
        "returnType": "bool"
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.RefreshItemWithWindows": {
        "params": {
            "item": "'GenericTreeItem'"
        },
        "paramStr": "self, item: 'GenericTreeItem'",
    },
    "wx.lib.agw.customtreectrl.GenericTreeItem.SetData": {
        "params": {
            "data": "Any"
        },
        "paramStr": "self, data: Any",
    },
    "wx.lib.agw.aui.auibook.AuiNotebook.ReDockPage": {
        "params": {
            "pane": "Any"
        },
        "paramStr": "self, pane: Any",
    },
    "wx.lib.agw.aui.auibook.AuiTabCtrl.GetPointedToTab": {
        "returnType": "Any"
    },
    "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.ClientToScreen": {
        "params": {
            "x": "int",
            "y": "int"
        },
        "paramStr": "self, x: int, y: int",
    },
    "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.HitTest": {
        "params": {
            "pointOrTuple": "Any",
        },
        "paramStr": "self, pointOrTuple: Any",
    },
    "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.ScreenToClient": {
        "params": {
            "x": "int",
            "y": "int"
        },
        "paramStr": "self, x: int, y: int",
    },
    "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetAGWWindowStyleFlag": {
        "params": {
            "style": "int",
        },
        "paramStr": "self, style: int",
    },
    "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetCursor": {
        "params": {
            "cursor": "Any",
        },
        "paramStr": "self, cursor: Any",
    },
    "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SortItems": {
        "params": {
            "func": "Any",
        },
        "paramStr": "self, func: Any = None",
    },
    "wx.lib.agw.aui.framemanager.AuiManager.OnTabBeginDrag": {
        "params": {
            "event": "Any",
        },
        "paramStr": "self, event: Any",
    },
    "wx.lib.agw.aui.framemanager.AuiManager.OnTabEndDrag": {
        "params": {
            "event": "Any",
        },
        "paramStr": "self, event: Any",
    },
    "wx.lib.agw.aui.framemanager.AuiManager.OnTabPageClose": {
        "params": {
            "event": "Any",
        },
        "paramStr": "self, event: Any",
    },
    "wx.lib.agw.aui.framemanager.AuiManager.OnTabSelected": {
        "params": {
            "event": "Any",
        },
        "paramStr": "self, event: Any",
    },
    "wx.lib.agw.aui.framemanager.AuiManager.PaneFromTabEvent": {
        "params": {
            "event": "Any",
        },
        "paramStr": "self, event: Any",
    },
    "wx.lib.agw.aui.framemanager.AuiManager.StartPreviewTimer": {
        "params": {
            "toolbar": "Any",
        },
        "paramStr": "self, toolbar: Any",
    },
    "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SortItems": {
        "params": {
            "func": "Any",
        },
        "paramStr": "self, func: Any = None",
    },
    "wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetX": {
        "params": {
            "x": "int",
        },
        "paramStr": "self, x: int",
    },
    "wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetY": {
        "params": {
            "y": "int",
        },
        "paramStr": "self, y: int",
    },
    "wx.lib.agw.flatnotebook.FlatNotebook.SetAGWWindowStyleFlag": {
        "params": {
            "agwStyle": "int",
        },
        "paramStr": "self, agwStyle: int",
    },
    "wx.lib.agw.customtreectrl.GenericTreeItem.GetParent": {
        "returnType": "Optional['GenericTreeItem']",
    },
    "wx.lib.agw.customtreectrl.GenericTreeItem.GetData": {
        "returnType": "Any",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetSelection": {
        "returnType": "Optional['GenericTreeItem']",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetSelections": {
        "returnType": "list['GenericTreeItem']",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemParent": {
        "returnType": "Optional['GenericTreeItem']",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemText": {
        "returnType": "str",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetRootItem": {
        "returnType": "Optional['GenericTreeItem']",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.AddRoot": {
        "returnType": "'GenericTreeItem'",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.AppendItem": {
        "returnType": "'GenericTreeItem'",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.HitTest": {
        "returnType": "tuple['GenericTreeItem', int]",
    },
    "wx.Frame.SetStatusWidths": {
        "params": {
            "widths": "list[int]",
        },
        "paramStr": "self, widths: list[int]",
    },
    "wx.StatusBar.SetStatusWidths": {
        "params": {
            "widths": "list[int]",
        },
        "paramStr": "self, widths: list[int]",
    },
    "wx.MultiChoiceDialog.SetSelections": {
        "params": {
            "selections": "list[int]",
        },
        "paramStr": "self, selections: list[int]",
    },
    "wx.MultiChoiceDialog.GetSelections": {
        "returnType": "list[int]",
    },
    "wx.ListBox.GetSelections": {
        "returnType": "list[int]",
    },
    "wx.lib.intctrl.IntCtrl.GetValue": {
        "returnType": "Optional[int]",
    },
    "wx.lib.intctrl.IntCtrl.SetValue": {
        "params": {
            "value": "Optional[int]",
        },
        "paramStr": "self, value: Optional[int]",
    },
    "wx.lib.masked.timectrl.TimeCtrl.GetValue": {
        "returnType": "Optional[Any]",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetChildrenCount": {
        "returnType": "int",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetChildren": {
        "returnType": "list['GenericTreeItem']",
    },
    "wx.lib.agw.customtreectrl.GenericTreeItem.GetChildren": {
        "returnType": "list['GenericTreeItem']",
    },
    "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetText": {
        "returnType": "str",
    },
    "wx.lib.agw.customtreectrl.GenericTreeItem.GetText": {
        "returnType": "str",
    },
}
