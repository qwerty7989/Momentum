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
        self.myFontBig = py.font.Font("fonts\\font.ttf" , 60)
        self.myFontMedium = py.font.Font("fonts\\font.ttf" , 48)
        self.myFontSmall = py.font.Font("fonts\\font.ttf" , 36)

        self.myFont = {
            "Big": self.myFontBig,
            "Medium": self.myFontMedium,
            "Small": self.myFontSmall
        }

        self.sound_path = {
            "Clearline" : "src\\data\\Sound\\clearline.wav",
            "Gameover" : "src\\data\\Sound\\gameover.wav",
            "Rotate" : "src\\data\\Sound\\rotate.wav",
            "Move" : "src\\data\\Sound\\move.wav",
            "Select" : "src\\data\\Sound\\select.wav",
            "Confirm" : "src\\data\\Sound\\confirm.wav",
            "Gameover" : "src\\data\\Sound\\gameover.wav",
            "Victory" : "src\\data\\Sound\\victory.wav",
            "Back" : "src\\data\\Sound\\back.wav",
            "Drop" : "src\\data\\Sound\\drop.wav"
        }