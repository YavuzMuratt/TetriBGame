from settings import *
from tetromino import Tetromino
import math


class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_arr = self.get_field_arr()
        self.tetromino = Tetromino(self)

    def check_lines(self):
        row = FIELD_HEIGHT - 1
        for y in range(FIELD_HEIGHT - 1,  -1, -1):
            for x in range(FIELD_WIDTH):
                self.field_arr[row][x] = self.field_arr[y][x]

                if self.field_arr[y][x]:
                    self.field_arr[row][x].pos = vec(x, y)

            if sum(map(bool, self.field_arr[row])) < FIELD_WIDTH:
                row -= 1
            else:
                for x in range(FIELD_WIDTH):
                    self.field_arr[row][x].alive = False
                    self.field_arr[row][x] = 0

    def put_blocks_in_arr(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_arr[y][x] = block

    def get_field_arr(self):
        return [[0 for x in range(FIELD_WIDTH)] for y in range(FIELD_HEIGHT)]

    def check_landing(self):
        if self.tetromino.landing:
            self.put_blocks_in_arr()
            self.tetromino = Tetromino(self)

    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetromino.move(direction= 'left')
        elif pressed_key == pg.K_RIGHT:
            self.tetromino.move(direction= 'right')
        elif pressed_key == pg.K_UP:
            self.tetromino.rotate()

    def draw_grid(self):
        for x in range(FIELD_WIDTH):
            for y in range(FIELD_HEIGHT):
                pg.draw.rect(self.app.screen, "gray", (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        if self.app.anim_trigger:
            self.check_lines()
            self.tetromino.update()
            self.check_landing()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)
