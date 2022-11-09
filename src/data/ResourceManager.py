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
            self.title[i] = py.transform.scale(self.title[i], (360, 72))

        # ? Load Block
        self.block_name = [
            "LightBlue.png", # I
            "Blue.png",      # J
            "Orange.png",    # L
            "Yellow.png",    # O
            "Green.png",     # S
            "Purple.png",    # T
            "Red.png",       # Z
        ]
        self.block = {}
        for i in self.block_name:
            self.block[i] = py.image.load("src\\data\\SingleBlocks\\" + i).convert_alpha()


        # ? Load Shape
        self.shape_name = [
            "I.png", # Light Blue
            "J.png", # Blue
            "L.png", # Orange
            "O.png", # Yellow
            "S.png", # Green
            "T.png", # Purple
            "Z.png"  # Red
        ]
        self.shape = {}
        for i in self.shape_name:
            self.shape[i] = py.image.load("src\\data\\ShapeBlocks\\" + i).convert_alpha()
