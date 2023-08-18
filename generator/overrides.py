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
		"returnType": "Optional[bool]",
	},
	"wx.Window.Destroy": {
		"returnType": "Optional[bool]",
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
    "wx.grid.Grid": {
        "superClass": ["wx.Scrolled"],
	}
}
