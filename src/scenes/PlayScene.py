import pygame as py
import sys
from src import Globe # ? Import globe for manage global objects

class PlayScene(object):
    def __init__(self):
        # ? Load background
        self.background = Globe.Game.ResourceManager.background



    def update(self):
        pass


    def draw(self, screen):
        # ? Background 
        screen.blit(self.background["Board.png"], (0, 0))

        # ? HUD


        # ? 