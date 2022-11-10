import pygame as py
import sys
from src import Globe # ? Import globe for manage global objects

class Hud(object):
    def __init__(self) -> None:
        # ? Load background
        self.background = Globe.Game.ResourceManager.background
        
        # ? Load HUD
        self.hud = Globe.Game.ResourceManager.hud

    def update(self):
        pass

    def draw(self, screen):
        # ? Background 
        screen.blit(self.background["Board.png"], (0, 0))
        
        # ? HUD
        screen.blit(self.hud["sidebar.png"], (384, 0))


