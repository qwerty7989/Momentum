import pygame as py
import sys
from src import Globe # ? Import globe for manage global objects
from src.constant import *

class GameoverScene(object):
    def __init__(self):
        # ? Select function
        self.selectIndex = 0

        # ? Load title
        self.title = Globe.Game.ResourceManager.title
        self.myFont = Globe.Game.ResourceManager.myFont

        # ? Click or not?
        self.confirm = False

    def writeText(self, text, color, size):
        self.text = self.myFont[size].render(text, False, color)

    def update(self):
        if self.confirm == False:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

                if event.type == py.KEYDOWN: # ? Any key pressed
                    if event.key == KEY_UP:
                        self.selectIndex -= 1
                        if self.selectIndex < 0: self.selectIndex = 1
                    elif event.key == KEY_DOWN:
                        self.selectIndex += 1
                        if self.selectIndex > 1: self.selectIndex = 0
                    
                    if event.key == KEY_EXIT:
                        Globe.Game.SceneManager.gotoScene("Start")

                    if event.key == py.K_z: # 
                        self.confirm = True



        else: # ? Confirm
            if self.selectIndex == 0: # ? Retry
                Globe.Game.SceneManager.gotoScene("Play")

            if self.selectIndex == 1: # ? Back
                Globe.Game.SceneManager.gotoScene("Start")



    def draw(self, screen):
        screen.fill((255, 255, 255), (((832 / 2) - 108), (600 / 2) + 60 + (60 * ((self.selectIndex + 1) % 2)), 100, 100))

        # ? Gameover Text
        self.writeText("Game Over!", (128, 0, 0), "Medium")
        screen.blit(self.text, ((832 / 2) - 136, (600 / 2)))

        # ? Cursor
        self.writeText(">", (0, 0, 0), "Medium")
        screen.blit(self.text, ((832 / 2) - 108, (600 / 2) + 60 + (60 * self.selectIndex)))

        # ? RETRY
        if self.selectIndex == 0:
            self.writeText("RETRY", (0, 0, 0), "Medium")
        else:
            self.writeText("RETRY", (128, 128, 128), "Medium")
        screen.blit(self.text, ((832 / 2) - 64, (600 / 2) + 60))

        # ? BACK to menu
        if self.selectIndex == 1:
            self.writeText("BACK", (0, 0, 0), "Medium")
        else:
            self.writeText("BACK", (128, 128, 128), "Medium")
        screen.blit(self.text, ((832 / 2) - 64, (600 / 2) + 120))