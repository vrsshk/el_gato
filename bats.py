import pygame
from blocks import AnimatedBlock
from random import randint

from images import load_sprite_sheets

class Bat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((39, 48), pygame.SRCALPHA)
        self.rect = self.image.get_rect(top = y, left = x)
        self.direction = "right"

        #animation
        self.animations = load_sprite_sheets("bat", 48, 48, True)
        self.animation_index = 0
        self.animation_count = 0

        #status
        self.dead = False
        self.status = "idle"

        #movement
        self.speed = randint(1, 2)

    def get_status(self):
        pass

    def animate(self): 
        if self.speed > 0:
            self.direction = "right"
        elif self.speed <0:
            self.direction = "left"
        animation = self.animations[self.status + "_" + self.direction]

        self.animation_index += 0.15
        if self.animation_index > len(animation):
            if self.status == 'angry':
                self.dead = True
            self.animation_index = 0
        self.image = animation[int(self.animation_index)]

    def reverse(self):
        self.speed *= -1
    
    def move(self):
        self.rect.x += self.speed
    
    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
