import pygame, sys
import os
from level import Level
from overworld import Overworld
from data import window_height, window_width, fps
pygame.init() 

class Game:
    def __init__(self):
        self.max_level = 1
        self.overworld = Overworld(0, 2, window, self.create_level)
        self.status = 'overworld'
    
    def create_level(self, current_level):
        self.level = Level(current_level, window, self.create_overworld)
        self.status = 'level'

    def create_overworld(self):
        self.status = 'overworld'

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        elif self.status == 'level':
            self.level.run()

window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
im = pygame.image.load(os.path.join("pictures", "bg", "bg.png"))
  
window.blit(im,[0,0])

game = Game()

while True:
    window.blit(im,[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.run()
    
    pygame.display.update()
    clock.tick(fps)