from .generator import DocumentationGenerator

dg = DocumentationGenerator()
dg.generate()


# Test mode
# testUrls: list[str] = [
#     "wx.functions.html",
#     "wx.Window.html",
# ]
# for testUrl in testUrls:
#     print("")
#     print("Testing: " + testUrl)
#     typingList = dg.parser.processClassApi(testUrl)
#     print(typingList)
