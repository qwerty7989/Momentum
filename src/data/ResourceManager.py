import pygame as py

class ResourceManager(object):
    def __init__(self):
        # ? Contain all files we need. (Image, Audio, etc.)
        # ? Load Background
        self.background_name = [
            "Board.png",
        ]
        self.background = {}
        for i in self.background_name:
            self.background[i] = py.image.load("src\\data\\Board\\" + i).convert_alpha()
            self.background[i] = py.transform.scale(self.background[i], (384, 704))

        # ? Load Title Logo
        self.title_name = [
            "Title.png"
        ]
        self.title = {}
        for i in self.title_name:
            self.title[i] = py.image.load("src\\data\\Title\\" + i).convert_alpha()
            self.title[i] = py.transform.scale(self.title[i], (720, 144))

        # ? Load Shawdow
        self.shadow_name = [
            "Single.png" # Single shadow block
        ]
        self.shadow = {}
        for i in self.shadow_name:
            self.shadow[i] = py.image.load("src\\data\\Ghost\\" + i).convert_alpha()
            self.shadow[i] = py.transform.scale(self.shadow[i], (32, 32))

        # ? Load Block
        self.block_name = [
            "LightBlue.png", # I
            "Blue.png",      # J
            "Orange.png",    # L
            "Green.png",     # S
            "Purple.png",    # T
            "Red.png",       # Z
            "Yellow.png"     # O
        ]
        self.block = {}
        for i in self.block_name:
            self.block[i] = py.image.load("src\\data\\SingleBlocks\\" + i).convert_alpha()
            self.block[i] = py.transform.scale(self.block[i], (32, 32))


        # ? Load Shape
        self.shape_name = [
            "I.png", # Light Blue
            "J.png", # Blue
            "L.png", # Orange
            "S.png", # Green
            "T.png", # Purple
            "Z.png", # Red
            "O.png"  # Yellow
        ]
        self.shape = {}
        for i in self.shape_name:
            self.shape[i] = py.image.load("src\\data\\ShapeBlocks\\" + i).convert_alpha()
            width, height = self.shape[i].get_size()
            self.shape[i] = py.transform.scale(self.shape[i], (width / 2, height / 2))


        self.hud_name = [
            "sidebarLeft.png",
            "sidebarRight.png",
            "holdingHud.png",
            "queueHud.png"
        ]
        self.hud = {}
        for i in self.hud_name:
            self.hud[i] = py.image.load("src\\data\\Hud\\" + i).convert_alpha()
            
        # ? System Font 
        self.myFont = py.font.Font("fonts\\font.ttf" , 60)