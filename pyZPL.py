class ZPLElement:
    def __init__(self):
        self.children = []
    width = 0
    height = 0
    x = 0
    y = 0
    type = ""
    ZPL = ""
    row = 0
    
    top = None
    bottom = None
    left = None
    right = None

class ZPLCustomItem:
    fixed = ""
    data = ""
    ID = ""
    type = ""
    visible = False

class ZPLImage:
    width = 0
    height = 0
    downloadCmd = ""

class ZPLRow:
    def __init__(self):
        self.rowElements = []
    width = 0
    height = 0
