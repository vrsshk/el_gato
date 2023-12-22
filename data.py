import pygame
from os.path import join
from images import sprite_separator
window_width= 1120
window_height = 704

fps = 60

icon_picture = pygame.image.load(join('assets', 'surrounding', 'levels_icon.png')).convert_alpha()

sprite_sheet = pygame.image.load(join('assets', 'surrounding', 'levels.png')).convert_alpha()
level_pictures = sprite_separator(sprite_sheet, 222, 124)

level_0 = {'node_pos': (250,200), 'node_picture': level_pictures[0]}
level_1 = {'node_pos': (560,350), 'node_picture': level_pictures[1]}
level_2 = {'node_pos': (870,500),'node_picture': level_pictures[2]}

levels = {
    0: level_0,
    1: level_1,
    2: level_2}
