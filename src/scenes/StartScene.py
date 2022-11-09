import pygame as py
import sys
from src.Globe import * # ? Import globe for manage global objects

class StartScene(object):
    def __init__(self):
        # ? Select function
        self.selectIndex = 0

        # ? Load title
        self.title = Globe.Game.ResourceManager.title

        # ? Click or not?
        self.confirm = False

    def update(self):
        if self.confirm == False:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

                if event.type == py.KEYDOWN: # ? Any key pressed
                    
                    

                    if event.key == py.K_z: # 
                        self.confirm = True



        else: # ? Confirm
            if self.selectIndex == 0: # ? Start
                Globe.Game.SceneManager.gotoScene("Play")

    def draw(self, screen):
        screen.blit(self.title["Title.png"], (136, 80))