import pygame as py

# ? Resolution
WINDOW_WIDTH = 832
WINDOW_HEIGHT = 704

# ? Board size
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

# ? Board Margin (Blocks)
MARGIN_WIDTH_BLOCK = 8
MARGIN_HEIGHT_BLOCK = 1

# ? Board Margin (Pixels)
MARGIN_WIDTH = 224
MARGIN_HEIGHT = 0

# ? Tick in each Frame
TICK_PER_FRAME = 100/6

GAME_FRAME = 25
MOVE_FRAME = 7
ROTATE_FRAME = 7

# ? Start position 
START_GRID_X = 3
START_GRID_Y = 0

# ? Size of each Block
BLOCK_SIZE = 32

# ? Config
KEY_UP = py.K_UP
KEY_DOWN = py.K_DOWN
KEY_LEFT = py.K_LEFT
KEY_RIGHT = py.K_RIGHT
KEY_HARD_DROP = py.K_SPACE
KEY_ROTATE_CW = py.K_x
KEY_ROTATE_CCW = py.K_z
KEY_ROTATE_180 = py.K_a
KEY_HOLD = py.K_c
KEY_EXIT = py.K_q





# ! TODO
# ? Concept
# Normal Tetris with gimmick, goal is to complete 40-line as fast
# as possible 

# ? PlayScene
# hard-drop shadow[DONE] -> complete line detector[DONE] -> 7-bags system[DONE], "holding" display[DONE], "queue piece" display[DONE] -> 40 line counter -> game sound with bfxr -> some gimmick to the game. i.e. Skill, well just something. 
# Add some timer to track the time to complete 40-line

# ? StartScene
# Start game -> Option -> Scoreboard -> Credit 
# Option would copied from Tetr.io if the DAS ARS etc. were implemented
# Scoreboard save in csv format

"""Add main game logic and gameplay"""
"""Add SRS rotation"""
"""Add SRS spawn"""
"""Add wall kick"""

"""Add Queue/Next (7-bag system)"""
"""Add ARE"""
"""Add DAS"""
"""Add Shadow"""


# ! Done
"""Add Piece"""
"""Add Drop"""
"""Add Board.py for manage the Tetris tile"""
"""Game Tick in each Frame: 100 millisecond / 6"""