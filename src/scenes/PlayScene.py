import pygame as py
import sys
from src import Globe # ? Import globe for manage global objects
from src.Board import *
from src.Hud import *

class PlayScene(object):
    def __init__(self):
        
        self.Board = Board()
        self.Hud = Hud()

        
        

    def update(self):
        self.Hud.update()
        self.Board.update()
            
           

    def draw(self, screen):
        self.Hud.draw(screen)
        self.Board.draw(screen)
