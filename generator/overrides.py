# -*- coding: utf-8 -*-
from typing import Any

OVERRIDES: dict[str, dict[str, Any]] = {
	"wx.ListCtrl.GetFirstSelected": {
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
}
