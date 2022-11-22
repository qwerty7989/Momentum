"""
Thank you for GD50! For most of the concepts and ideas around the game development. 
Most of these codes and assets are referenced from the "Match 3" class from the "CS50's Introduction to Game Development" course.
Link: https://cs50.harvard.edu/games/2018/weeks/2/
"""

# Import Pygame
import pygame as py

# ? Import Dependencies for class object usage 
from src.Dependencies import *

class main(object):
    def __init__(self):
        # ? Application's display resolution
        self.screen = py.display.set_mode(
            [WINDOW_WIDTH , WINDOW_HEIGHT],
            vsync = 1)

        # ? System Clock
        self.clock = py.time.Clock()

        # ? Application title bar
        py.display.set_caption("Momentum")
        
        # ? Resource Manager
        self.ResourceManager = ResourceManager()

        # ? Is game running?
        self.isRunning = True

        Globe.Game = self

        # ? Initiate the first scene with SceneManager
        self.sceneList = {
            "Start" : StartScene,
            "Play" : PlayScene,
            "Scoreboard" : ScoreboardScene,
            "Gameover" : GameoverScene
        }
        self.SceneManager = SceneManager(self.sceneList, "Start")

        # ? Start the application
        self.run()

    def run(self):
        while self.isRunning == True:
            
            # ? Update screen
            self.SceneManager.scene.update()
            self.SceneManager.scene.draw(self.screen)
        
            py.display.update()
            self.clock.tick(TICK_PER_FRAME)

if __name__ == "__main__":
    py.init()

    main()

    py.quit()
    sys.exit()
