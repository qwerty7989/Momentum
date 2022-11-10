import pygame as py
import sys
from src import Globe # ? Import globe for manage global objects

class Board(object):
    def __init__(self) -> None:
        # ? Load Block and Shape
        self.block = Globe.Game.ResourceManager.block
        self.shape = Globe.Game.ResourceManager.shape


        # ? Game Tick time
        self.lastTicks = py.time.get_ticks()
        self.gameTicks = 800

        # ? Move Tick time
        self.lastPressed = py.time.get_ticks()
        self.moveTicks = 200

        # ? Start position coordinates
        self.shapeStartX = 32
        self.shapeStartY = 32

        # ? Start position on the grid
        self.gridPosX = 4
        self.gridPosY = -1

    def positionConverter(self, u, v):
        # Start counting the 1st top-left block as (1, 1)
        # And the bottom-right block as (10, 20)
        x = u * 32 # 32 is offset to border of the grid
        y = v * 32  
        return (x, y)

    def update(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:
                print(py.key.name(event.key))
        
        

        # ? Key pressed
        keys = py.key.get_pressed()

        nowTicks = py.time.get_ticks()
        if not keys[py.K_DOWN] and nowTicks - self.lastTicks >= self.gameTicks:
            self.lastTicks = nowTicks

            # ? Natural fall
            self.gridPosY += 1

            
        if keys[py.K_RIGHT] or keys[py.K_LEFT] or keys[py.K_DOWN]:
            nowTicks = py.time.get_ticks()
            if nowTicks - self.lastPressed >= self.moveTicks:
                self.lastPressed = nowTicks
                self.gridPosX += keys[py.K_RIGHT] - keys[py.K_LEFT]
                self.gridPosY += keys[py.K_DOWN]


    def draw(self, screen):
        # ? Block
        screen.blit(self.shape["I.png"], self.positionConverter(self.gridPosX, self.gridPosY))

        # screen.blit(self.block["Blue.png"], (self.shapeStartX, self.shapeStartY))


