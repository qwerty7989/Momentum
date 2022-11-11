import pygame as py
import sys
from src import Globe # ? Import globe for manage global objects
from src.Piece import *
from src.constant import *

class Board(object):
    def __init__(self) -> None:

        # ? Initiate default board
        # ? -1 is Free Block
        # ? 0-6 is Occupied Block
        # ? Board (x,y) start from 0
        # ? Grid (x,y) start from 0
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT
        self.board = []
        for i in range(self.height):
            new_line = []
            for j in range(self.width):
                new_line.append(-1)
            self.board.append(new_line)


        # ? Load Block and Shape
        self.block = Globe.Game.ResourceManager.block
        self.shape = Globe.Game.ResourceManager.shape
        self.block_name = Globe.Game.ResourceManager.block_name

        # ? Main game clock
        self.Frame = TICK_PER_FRAME

        # ? Game Tick time
        self.lastTicks = py.time.get_ticks()
        self.gameFrame = GAME_FRAME
        self.gameTicks = self.gameFrame * self.Frame

        # ? Move Tick time
        self.lastMove = py.time.get_ticks()
        self.moveFrame = MOVE_FRAME
        self.moveTicks = self.moveFrame * self.Frame

        # ? Rotate Tick time
        self.lastRotate = py.time.get_ticks()
        self.rotateFrame = ROTATE_FRAME
        self.rotateTicks = self.rotateFrame * self.Frame
        self.rotatePressed = False

        # ? New piece yet
        self.IsNowPiece = False 


        # ? Debug zone
        self.lastAntiFallPressed = py.time.get_ticks() 
        self.naturalFall = False


    def newPiece(self):
        self.piece = Piece(START_GRID_X, START_GRID_Y)

    def positionConverter(self, u, v):
        # Start counting the 1st top-left block as (0, 0)
        # And the bottom-right block as (10, 20)
        x = (u + 1) * BLOCK_SIZE # 32 is offset to border of the grid (1 Block = 32 pixels)
        y = (v + 1) * BLOCK_SIZE  
        return (x, y)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.piece.blockList():
                    if i + self.piece.y > self.height - 1 or j + self.piece.x > self.width -1 or j + self.piece.x < 1 or self.board[i + self.piece.y][j + self.piece.x] > 1:
                        intersection = True
        return intersection

    def freeze(self):
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.piece.blockList():
                    self.board[i + self.piece.y][j + self.piece.x] = self.piece.type
        # self.break_lines()
        self.newPiece()
        if self.intersects():
            self.state = "gameover"

    def update(self):
        # ? Exit game
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:
                print(py.key.name(event.key))
        
        # ? If there's no piece, create new.
        if not self.IsNowPiece:
            self.newPiece()
            self.IsNowPiece = True

        # ? Key pressed
        keys = py.key.get_pressed()

        # ? Piece will naturally "fall" 
        nowTicks = py.time.get_ticks()
        if keys[py.K_DOWN] or nowTicks - self.lastTicks >= self.gameTicks:
            self.lastTicks = nowTicks

            # ? Natural fall
            if self.naturalFall:
                prevY = self.piece.y
                self.piece.naturalFall()
                if self.intersects():
                    self.piece.y = prevY
                    self.freeze()
            
        # ? Piece will "move" left or right or down
        if keys[py.K_RIGHT] or keys[py.K_LEFT]:
            nowTicks = py.time.get_ticks()
            if nowTicks - self.lastMove >= self.moveTicks:
                self.lastMove = nowTicks

                if keys[py.K_RIGHT] or keys[py.K_LEFT]:
                    prevX = self.piece.x
                    self.piece.movePiece(keys[py.K_RIGHT] - keys[py.K_LEFT])
                    if self.intersects():
                        self.piece.x = prevX
        
        # ? Piece will "rotate" on different tick from "move"
        if keys[py.K_UP] and not self.rotatePressed:
            nowTicks = py.time.get_ticks()
            if nowTicks - self.lastRotate >= self.rotateTicks:
                self.lastRotate = nowTicks
                self.rotatePressed = True
                self.piece.rotatePiece()
        elif not keys[py.K_UP]:
            self.rotatePressed = False

        # ? Debug zone
        if keys[py.K_f]:
            nowTicks = py.time.get_ticks()
            if nowTicks - self.lastAntiFallPressed >= self.gameTicks:
                self.lastAntiFallPressed = nowTicks
                self.naturalFall = not self.naturalFall

    def draw(self, screen):
        if self.IsNowPiece:
            self.piece.draw(screen)

        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != -1:
                    screen.blit(self.block[self.block_name[self.board[y][x]]], self.positionConverter(x, y))

        


