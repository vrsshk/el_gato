import pygame
from os.path import join

from images import sprite_separator

block_size = 32

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(top = y, left = x)
    def update(self, x_offset):
        self.rect.x += x_offset


class StaticBlock(Block):
    def __init__(self, x, y, size, surface):
        super().__init__(x, y, size)
        self.image = surface

class AnimatedBlock(Block):
    def __init__(self, x, y, size, file_name):
        super().__init__(x, y, size)
        path =  join("assets", "surrounding", file_name)
        sprite_sheet = pygame.image.load(path).convert_alpha()
        self.sprites = sprite_separator(sprite_sheet, size, size)
        self.animation_index = 0
    def animate(self): 
        self.animation_index += 0.15
        if self.animation_index > len(self.sprites):
            self.animation_index = 0
        self.image = self.sprites[int(self.animation_index)]
    def update(self, x_offset):
        self.animate()
        self.rect.x += x_offset