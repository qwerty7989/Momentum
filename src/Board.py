import pygame as py
import sys
from src import Globe # ? Import globe for manage global objects
from src.Piece import *
from src.constant import *

class Board(object):
    def __init__(self) -> None:

        # ? Initiate default board
        # ? 0 is Free Block
        # ? 1 is Occupied Block
        self.board = []
        self.board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]


        # ? Load Block and Shape
        self.block = Globe.Game.ResourceManager.block
        self.shape = Globe.Game.ResourceManager.shape

        # ? Main game clock
        self.Frame = TICK_PER_FRAME

        # ? Game Tick time
        self.lastTicks = py.time.get_ticks()
        self.gameTicks = GAME_FRAME * self.Frame

        # ? Move Tick time
        self.lastPressed = py.time.get_ticks()
        self.moveTicks = MOVE_FRAME * self.Frame

        # ? New piece yet
        self.IsNowPiece = False 

    def newPiece(self):
        self.piece = Piece(START_GRID_X, START_GRID_Y)

    def positionConverter(self, u, v):
        # Start counting the 1st top-left block as (1, 1)
        # And the bottom-right block as (10, 20)
        x = u * BLOCK_SIZE # 32 is offset to border of the grid (1 Block = 32 pixels)
        y = v * BLOCK_SIZE  
        return (x, y)

    def update(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:
                print(py.key.name(event.key))
        
        if not self.IsNowPiece:
            self.newPiece()
            self.IsNowPiece = True

        # ? Key pressed
        keys = py.key.get_pressed()

        nowTicks = py.time.get_ticks()
        if not keys[py.K_DOWN] and nowTicks - self.lastTicks >= self.gameTicks:
            self.lastTicks = nowTicks

            # ? Natural fall
            self.piece.naturalFall()
            
        if keys[py.K_RIGHT] or keys[py.K_LEFT] or keys[py.K_DOWN]:
            nowTicks = py.time.get_ticks()
            if nowTicks - self.lastPressed >= self.moveTicks:
                self.lastPressed = nowTicks
                self.piece.movePiece(keys[py.K_RIGHT] - keys[py.K_LEFT], 0)
                self.piece.movePiece(0, keys[py.K_DOWN])


    def draw(self, screen):
        if self.IsNowPiece:
            self.piece.draw(screen)

        


