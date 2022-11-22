import pygame as py
import sys
from src import Globe # ? Import globe for manage global objects
from src.constant import *

class ScoreboardScene(object):
    def __init__(self):
        # ? Select function
        self.selectIndex = 0

        # ? Load title
        self.title = Globe.Game.ResourceManager.title
        self.myFont = Globe.Game.ResourceManager.myFont
        self.clearedTime = Globe.Game.clearedTime
        self.soundPath = Globe.Game.ResourceManager.sound_path
        self.soundManager = Globe.Game.soundManager

        # ? Click or not?
        self.confirm = False

        # ? Continue
        self.isContinue = False

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
                        self.soundManager.load(self.soundPath["Select"])
                        self.soundManager.play(0)
                        self.selectIndex -= 1
                        if self.selectIndex < 0: self.selectIndex = 3
                    elif event.key == KEY_DOWN:
                        self.soundManager.load(self.soundPath["Select"])
                        self.soundManager.play(0)
                        self.selectIndex += 1
                        if self.selectIndex > 3: self.selectIndex = 0
                    
                    if event.key == KEY_EXIT and self.isContinue:
                        Globe.Game.SceneManager.gotoScene("Start")

                    if event.key == py.K_f: # 
                        self.soundManager.load(self.soundPath["Confirm"])
                        self.soundManager.play(0)
                        self.isContinue = True
                    
                    if event.key == KEY_EXIT and self.isContinue:
                        self.soundManager.load(self.soundPath["Back"])
                        self.soundManager.play(0)
                        Globe.Game.SceneManager.gotoScene("Start")

                    if event.key == py.K_z and self.isContinue: # 
                        self.soundManager.load(self.soundPath["Confirm"])
                        self.soundManager.play(0)
                        self.confirm = True
        
        else : # ? Confirm
            if self.selectIndex == 0: # ? Start
                Globe.Game.SceneManager.gotoScene("Play")

            if self.selectIndex == 1: # ? Back
                Globe.Game.SceneManager.gotoScene("Start")

    def draw(self, screen):
        if self.isContinue:
            screen.fill((24, 24, 24))

            # ? Clear time
            # ! Didn't finish it in time, should save scoreboard to .csv file
            self.writeText((str)(int(self.clearedTime / 60))+ ":" + (str)(int((self.clearedTime / 10) % 10)) + (str)(int(self.clearedTime % 10)), (255, 255, 255), "Big")
            screen.blit(self.text, ((832 / 2) - 50, (600 / 2) - 150))

            # ? Cursor
            self.writeText(">", (255, 255, 255), "Medium")
            screen.blit(self.text, ((832 / 2) - 176, (600 / 2) + 240 + (60 * self.selectIndex)))

            # ? PLAY AGAIN GAME
            if self.selectIndex == 0:
                self.writeText("PLAY AGAIN", (255, 255, 255), "Medium")
            else:
                self.writeText("PLAY AGAIN", (200, 200, 200), "Medium")
            screen.blit(self.text, ((832 / 2) - 128, (600 / 2) + 240))
            
            # ? BACK
            if self.selectIndex == 1:
                self.writeText("BACK", (255, 255, 255), "Medium")
            else:
                self.writeText("BACK", (200, 200, 200), "Medium")
            screen.blit(self.text, ((832 / 2) - 128, (600 / 2) + 300))

        else:
            # ? Victory Text
            self.writeText("Victory!", (0, 128, 0), "Big")
            screen.blit(self.text, ((832 / 2) - 116, (600 / 2)))

            # ? CONTINUE
            self.writeText("PRESS F", (0, 0, 0), "Small")
            screen.blit(self.text, ((832 / 2) - 88, (600 / 2) + 80))

            # ? Press Z to continue
            self.writeText("TO CONTINUE", (0, 0, 0), "Small")
            screen.blit(self.text, ((832 / 2) - 118, (600 / 2) + 120))
