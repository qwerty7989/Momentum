import pygame as py
import sys
from src import Globe # ? Import globe for manage global objects

class PlayScene(object):
    def __init__(self):
        # ? Load background
        self.background = Globe.Game.ResourceManager.background
        
        self.Lorem = False

    def update(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:
                self.Lorem = True

    def draw(self, screen):
        # ? Background 
        screen.blit(self.background["Board.png"], (0, 0))

        # ? HUD


        # ? 