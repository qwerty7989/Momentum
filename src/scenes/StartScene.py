import pygame as py
import sys
from src import Globe # ? Import globe for manage global objects
from src.constant import *

class StartScene(object):
    def __init__(self):
        # ? Select function
        self.selectIndex = 0

        # ? Load title
        self.title = Globe.Game.ResourceManager.title
        self.myFont = Globe.Game.ResourceManager.myFont

        # ? Click or not?
        self.confirm = False

    def writeText(self, text, color):
        self.text = self.myFont.render(text, False, color)

    def update(self):
        if self.confirm == False:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

                if event.type == py.KEYDOWN: # ? Any key pressed
                    if event.key == KEY_UP:
                        self.selectIndex -= 1
                        if self.selectIndex < 0: self.selectIndex = 3
                    elif event.key == KEY_DOWN:
                        self.selectIndex += 1
                        if self.selectIndex > 3: self.selectIndex = 0
                    

                    if event.key == py.K_z: # 
                        self.confirm = True



        else: # ? Confirm
            if self.selectIndex == 0: # ? Start
                Globe.Game.SceneManager.gotoScene("Play")



            if self.selectIndex == 3: # ? Exit
                py.quit()
                sys.exit()

    def draw(self, screen):
        screen.fill((24, 24, 24))
        screen.blit(self.title["Title.png"], (56, 80))

        # ? Cursor
        self.writeText(">", (255, 255, 255))
        screen.blit(self.text, ((832 / 2) - 176, (600 / 2) + (60 * self.selectIndex)))

        # ? START GAME
        if self.selectIndex == 0:
            self.writeText("START", (255, 255, 255))
        else:
            self.writeText("START", (200, 200, 200))
        screen.blit(self.text, ((832 / 2) - 128, (600 / 2)))
        
        # ? SETTING
        if self.selectIndex == 1:
            self.writeText("SETTING", (255, 255, 255))
        else:
            self.writeText("SETTING", (200, 200, 200))
        screen.blit(self.text, ((832 / 2) - 128, (600 / 2) + 60))

        # ? CREDITS
        if self.selectIndex == 2:
            self.writeText("CREDITS", (255, 255, 255))
        else:
            self.writeText("CREDITS", (200, 200, 200))
        screen.blit(self.text, ((832 / 2) - 128, (600 / 2) + 120))

        # ? EXIT
        if self.selectIndex == 3:
            self.writeText("EXIT", (255, 255, 255))
        else:
            self.writeText("EXIT", (200, 200, 200))
        screen.blit(self.text, ((832 / 2) - 128, (600 / 2) + 180))