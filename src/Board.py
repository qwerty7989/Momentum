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
        self.board = [[-1 for x in range(self.width)] for y in range(self.height)]

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

        # ? Hold Piece
        self.holdPiece = None
        self.IsUsePieceYet = False
        self.IsHoldPiece = False

        # ? Natural Fall
        self.naturalFall = True

        # ? Line clear counter
        self.lineClearedCounter = 0

        # ? Debug zone
        self.lastAntiFallPressed = py.time.get_ticks() 
        self.showDebug = True

    def newPiece(self):
        self.piece = Piece(START_GRID_X, START_GRID_Y, False)
        self.shadow = Piece(START_GRID_X, START_GRID_Y, True)
        self.shadow.type = self.piece.type

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
                    if i + self.piece.y > self.height - 1 or j + self.piece.x > self.width - 1 or j + self.piece.x < 0 or self.board[i + self.piece.y][j + self.piece.x] > -1:
                        intersection = True
        return intersection

    def intersectsShadow(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.shadow.blockList():
                    if i + self.shadow.y > self.height - 1 or j + self.shadow.x > self.width - 1 or j + self.shadow.x < 0 or self.board[i + self.shadow.y][j + self.shadow.x] > -1:
                        intersection = True
        return intersection

    def freeze(self):
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.piece.blockList():
                    self.board[i + self.piece.y][j + self.piece.x] = self.piece.type
        self.lineClearedCounter += self.clearLines()
        self.newPiece()
        if self.intersects():
            self.state = "gameover"

    def clearLines(self):
        lineCleared = 0
        for y in range(self.height - 1, -1, -1):
            isFilled = True
            for x in range(self.width):
                if self.board[y][x] == -1:
                    isFilled = False                    
            if isFilled:
                self.board = [[-1 for x in range(self.width)]] + self.board[:y] + self.board[y+1:] 
                lineCleared += 1

        return lineCleared

    def update(self):
        # ? Exit game
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if self.showDebug and event.type == py.KEYDOWN:
                print(py.key.name(event.key))
        
        # ? If there's no piece, create new.
        if not self.IsNowPiece:
            self.newPiece()
            self.IsNowPiece = True

        # ? Key pressed
        keys = py.key.get_pressed()

        # ! Natural fall [DONE]
        # ? Piece will naturally "fall" 
        if self.naturalFall:
            nowTicks = py.time.get_ticks()
            if nowTicks - self.lastTicks >= self.gameTicks:
                self.lastTicks = nowTicks
                
                prevY = self.piece.y
                self.piece.moveDown()
                if self.intersects():
                    self.piece.y = prevY
                    if self.IsHoldPiece: 
                        self.IsUsePieceYet = True
                    self.freeze()
            
        # ! Move [DONE]
        # ? Piece will "move" left or right or down
        if keys[KEY_LEFT] or keys[KEY_RIGHT] or keys[KEY_DOWN] or keys[KEY_HARD_DROP]:
            nowTicks = py.time.get_ticks()
            if nowTicks - self.lastMove >= self.moveTicks:
                self.lastMove = nowTicks

                # ! Left
                if keys[KEY_LEFT]:
                    prevX = self.piece.x
                    self.piece.movePiece(-1)
                    if self.intersects():
                        self.piece.x = prevX

                # ! Right
                if keys[KEY_RIGHT]:
                    prevX = self.piece.x
                    self.piece.movePiece(1)
                    if self.intersects():
                        self.piece.x = prevX

                # ! Down
                if keys[KEY_DOWN]:
                    prevY = self.piece.y
                    self.piece.moveDown()
                    if self.intersects():
                        self.piece.y = prevY
                        if self.IsHoldPiece: 
                            self.IsUsePieceYet = True
                        self.freeze()

                # ! Hard Drop
                if keys[KEY_HARD_DROP]:
                    while not self.intersects():
                        self.piece.y += 1
                    self.piece.y -= 1
                    if self.IsHoldPiece: 
                        self.IsUsePieceYet = True
                    self.freeze()
     
        # ! Rotate [DONE] [Had to go simpler moveset rather than SRS in order to make it by deadline]
        # ? Piece will "rotate" on different tick from "move"
        if (keys[KEY_UP] or keys[KEY_ROTATE_CW] or keys[KEY_ROTATE_CCW] or keys[KEY_ROTATE_180]) and not self.rotatePressed:
            nowTicks = py.time.get_ticks()
            if nowTicks - self.lastRotate >= self.rotateTicks:
                # ! Rotate Clockwise
                if keys[KEY_UP] or keys[KEY_ROTATE_CW]:
                    self.lastRotate = nowTicks
                    self.rotatePressed = True
                    self.piece.rotatePiece(1)
                    if self.intersects():
                        self.piece.rotatePiece(-1)
                        self.rotatePressed = False

                # ! Rotate Counter Clockwise
                elif keys[KEY_ROTATE_CCW]:
                    self.lastRotate = nowTicks
                    self.rotatePressed = True
                    self.piece.rotatePiece(-1)
                    if self.intersects():
                        self.piece.rotatePiece(1)
                        self.rotatePressed = False

                # ! Rotate 180 Degree
                elif keys[KEY_ROTATE_180]:
                    self.lastRotate = nowTicks
                    self.rotatePressed = True
                    self.piece.rotatePiece(1)
                    self.piece.rotatePiece(1)
                    if self.intersects():
                        self.piece.rotatePiece(-1)
                        self.piece.rotatePiece(-1)
                        self.rotatePressed = False

        elif not (keys[KEY_UP] or keys[KEY_ROTATE_CW] or keys[KEY_ROTATE_CCW] or keys[KEY_ROTATE_180]):
            self.rotatePressed = False

        # ! Hold [DONE]
        if keys[KEY_HOLD]:
            if not self.IsHoldPiece:       
                self.piece.resetPosition()       
                self.holdPiece = self.piece
                self.newPiece()
                self.IsHoldPiece = True

            elif self.IsHoldPiece and self.IsUsePieceYet: 
                self.piece.resetPosition()
                self.tempPiece = self.piece
                self.piece = self.holdPiece
                self.holdPiece = self.tempPiece
                self.IsUsePieceYet = False

        # ? Debug zone
        if self.showDebug:
            if keys[py.K_f]:
                nowTicks = py.time.get_ticks()
                if nowTicks - self.lastAntiFallPressed >= self.gameTicks:
                    self.lastAntiFallPressed = nowTicks
                    self.naturalFall = not self.naturalFall
            if keys[py.K_s]:
                print(self.lineClearedCounter)

    def draw(self, screen):
        # ? If there's a piece, draw it
        if self.IsNowPiece:
            self.piece.draw(screen)
            self.shadow.rotation = self.piece.rotation
            self.shadow.x = self.piece.x
            self.shadow.y = self.piece.y
            self.shadow.type = self.piece.type
            while not self.intersectsShadow():
                self.shadow.y += 1
            self.shadow.y -= 1
            self.shadow.draw(screen)

        # ? Draw Block placed on the board
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != -1:
                    screen.blit(self.block[self.block_name[self.board[y][x]]], self.positionConverter(x, y))

        
