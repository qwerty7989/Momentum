import pygame as py
import sys
from src import Globe # ? Import globe for manage global objects
from src.constant import *

class Hud(object):
    def __init__(self) -> None:
        # ? Load background
        self.background = Globe.Game.ResourceManager.background
        
        # ? Load HUD
        self.hud = Globe.Game.ResourceManager.hud

    def update(self):
        pass

    def draw(self, screen):
        # ? HUD - Left side
        screen.blit(self.hud["sidebarLeft.png"], (0, 0))

        # ? Holding piece
        screen.blit(self.hud["holdingHud.png"], (24, 104))


        # ? HUD - Right side
        screen.blit(self.hud["sidebarRight.png"], (608, 0))
        
        # ? Queue piece
        screen.blit(self.hud["queueHud.png"], (632, 104))



        # ? Background - Board
        screen.blit(self.background["Board.png"], (MARGIN_WIDTH, MARGIN_HEIGHT))


