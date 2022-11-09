"""
Thank you for GD50! For most of the concepts and ideas around the game development. 
Most of these codes and assets are referenced from the "Match 3" class from the "CS50's Introduction to Game Development" course.
Link: https://cs50.harvard.edu/games/2018/weeks/2/
"""

import pygame as py

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 600

class main(object):
    def __init__(self):
        
        # set the application's display size
        self.screen = py.display.set_mode(
            [WINDOW_WIDTH , WINDOW_HEIGHT],
            vsync = 1)

        # set the application title bar
        py.display.set_caption("Momentum")
        
        # variable
        self.RUNNING = True
        self.run()

    def update(self, dt):
        pass

    def run(self):
        while self.RUNNING == True:
            self.screen.fill((255, 255, 255))
            py.draw.circle(self.screen, (0, 0, 255), (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 75)

            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    quit()

            py.display.update()

if __name__ == "__main__":
    py.init()

    main()

    py.quit()
