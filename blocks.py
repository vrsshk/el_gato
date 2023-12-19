import pygame

block_size = 32

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.image.fill('black')
        self.rect = self.image.get_rect(top = y, left = x)
    def update(self, x_offset):
        self.rect.x += x_offset