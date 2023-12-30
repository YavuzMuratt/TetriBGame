from settings import *
import random


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + POS_OFFSET
        self.alive = True

        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        pg.draw.rect(self.image, 'red', (1, 1, TILE_SIZE - 2 , TILE_SIZE - 2))
        self.rect = self.image.get_rect()

    def is_alive(self):
        if not self.alive:
            self.kill()

    def rotate(self, pivot_position):
        translated = self.pos - pivot_position
        rotated = translated.rotate(90)
        return rotated + pivot_position

    def set_rect_position(self):
        self.rect.topleft = self.pos * TILE_SIZE

    def update(self):
        self.is_alive()
        self.set_rect_position()

    def is_collided(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_WIDTH and y <  FIELD_HEIGHT and (
                y < 0 or not self.tetromino.tetris.field_arr[y][x]):
            return False
        return True



class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOS.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOS[self.shape]]
        self.landing = False

    def rotate(self):
        pivot_pos = self.blocks[0].pos
        new_pos = [block.rotate(pivot_pos) for block in self.blocks]

        if not self.is_collided(new_pos):
            for i, block in enumerate(self.blocks):
                block.pos = new_pos[i]
                block.pos = new_pos[i]
                block.set_rect_position()

    def is_collided(self, block_pos):
        return any(map(Block.is_collided, self.blocks, block_pos))

    def move(self, direction):
        move_direction = MOVE_DIRS[direction]
        new_block_pos = [block.pos + move_direction for block in self.blocks]
        is_collided = self.is_collided(new_block_pos)

        if not is_collided:
            for block in self.blocks:
                block.pos += move_direction
        elif direction == 'down':
            self.landing = True

    def update(self):
        self.move(direction='down')
