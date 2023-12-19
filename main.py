import pygame, sys
import os
from level import Level
from map import csv_to_list

pygame.init() 
window_width= 960
window_height = 640
FPS = 60


window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
im = pygame.image.load(os.path.join("pictures", "im1.png"))

level_map = csv_to_list('0')
level = Level(level_map, window)    
window.blit(im,[0,0])

while True:
    window.blit(im,[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    level.run()
    
    pygame.display.update()
    clock.tick(FPS)