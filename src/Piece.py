import pygame as py
import random
from src import Globe # ? Import globe for manage global objects
from src.constant import *

class Piece(object):
    """
    Matrix
        0  1  2  3
        4  5  6  7
        8  9 10 11
       12 13 14 15

    I-piece
        1
        5        4 5 6 7      
        9
        13
    """
    # ? Reference from SRS spin
    # https://tetris.fandom.com/wiki/SRS
    pieces = [
            # I-piece
            [[4, 5, 6, 7], [2, 6, 10, 14], [9, 8, 10, 11],[13, 9, 5, 1]],
            # J-piece
            [[0, 4, 5, 6], [2, 1, 5, 9], [10, 6, 5, 4], [8, 9, 5, 1]],
            # L-piece
            [[3, 7, 6, 5], [11, 10, 6, 2], [9, 5, 6, 7], [1, 2, 6, 10]],
            # O-piece (O-Spin, Let's Goooo!!!)
            [[1, 2, 5, 6], [2, 6, 5, 1], [6, 5, 1, 2], [5, 1, 2, 6]],
            # S-piece
            [[7, 6, 10, 9], [15, 11, 10, 6], [13, 14, 10, 11], [5, 9, 10, 14]],
            # T-piece
            [[1, 4, 5, 6], [6, 1, 5, 9], [9, 6, 5, 4], [4, 9, 5, 1]],
            # Z-piece
            [[4, 5, 9, 10], [6, 10, 9, 13], [14, 13, 9, 8],[12, 8, 9, 5]],
        ]
        
    def __init__(self, x, y):
        # ? Load Block and Shape
        self.block = Globe.Game.ResourceManager.block
        self.block_name = Globe.Game.ResourceManager.block_name

        # ? Data about each piece
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.pieces) - 1)
        self.rotation = 0

    def blockList(self):
        return self.pieces[self.type][self.rotation]

    def positionConverter(self, u, v):
        # Start counting the 1st top-left block as (1, 1)
        # And the bottom-right block as (10, 20)
        x = (u + 1) * BLOCK_SIZE # 32 is offset to border of the grid (1 Block = 32 pixels)
        y = (v + 1) * BLOCK_SIZE  
        return (x, y)


    def rotatePiece(self):
        self.rotation = (self.rotation + 1) % len(self.pieces[self.type])

    def naturalFall(self):
        self.y += 1

    def movePiece(self, x):
        self.x += x


    def update(self):
        pass


    def draw(self, screen):
        # ? Block
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.blockList():
                    screen.blit(self.block[self.block_name[self.type]], self.positionConverter(j + self.x, i + self.y))
