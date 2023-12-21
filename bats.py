import pygame
from blocks import AnimatedBlock
from random import randint


class Bat(AnimatedBlock):
    def __init__(self, x, y, size, file_name):
        super().__init__(x, y, size, file_name)
        self.speed = randint(1, 2)

    def flip_image(self):
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image, True, False)
    
    def reverse(self):
        self.speed *= -1
        self.flip_image()
    
    def move(self):
        self.rect.x += self.speed
    
    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
