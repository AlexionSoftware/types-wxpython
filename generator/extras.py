# -*- coding: utf-8 -*-
from .interfaces import ITyping, TypingType, ITypingClass, ITypingLiteral, ITypingFunction


EXTRA_KNOWN_ITEMS: list[ITyping] = []
lObj: ITypingLiteral = {
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
	"returnType": "int",
	"docstring": "",
	"source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
	"type": TypingType.LITERAL,
	"name": "YELLOW",
	"moduleName": "wx",
	"returnType": "int",
	"docstring": "",
	"source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
	"type": TypingType.LITERAL,
	"name": "BLACK",
	"moduleName": "wx",
	"returnType": "int",
	"docstring": "",
	"source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
	"type": TypingType.LITERAL,
	"name": "WHITE",
	"moduleName": "wx",
	"returnType": "int",
	"docstring": "",
	"source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
	"type": TypingType.LITERAL,
	"name": "BLUE",
	"moduleName": "wx",
	"returnType": "int",
	"docstring": "",
	"source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
	"type": TypingType.LITERAL,
	"name": "GREEN",
	"moduleName": "wx",
	"returnType": "int",
	"docstring": "",
	"source": "",
}
EXTRA_KNOWN_ITEMS.append(lObj)
lObj = {
	"type": TypingType.LITERAL,
	"name": "CYAN",
	"moduleName": "wx",
	"returnType": "int",
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