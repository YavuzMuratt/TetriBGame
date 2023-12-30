import pygame as pg

vec = pg.math.Vector2

FPS = 60
COLOR = (20, 20 ,20)

TILE_SIZE = 50
FIELD_SIZE = FIELD_WIDTH, FIELD_HEIGHT = 10, 20
FIELD_RES = FIELD_WIDTH * TILE_SIZE, FIELD_HEIGHT * TILE_SIZE

ANIMATON_TIME_INTERVAL = 150

POS_OFFSET = vec(FIELD_WIDTH // 2 - 1, 0)

MOVE_DIRS = {
    'left': vec(-1, 0),
    'right': vec(1, 0),
    'down': vec(0, 1)
}

TETROMINOS = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}