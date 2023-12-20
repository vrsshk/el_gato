import pygame, sys
import os
from level import Level

pygame.init() 
window_width= 960
window_height = 640
FPS = 60


window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
im = pygame.image.load(os.path.join("pictures", "bg", "bg3.png"))

level = Level(0, window)    
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