import pygame
import os
from os import listdir
from os.path import isfile, join

window_width = 960
HEIGHT = 720
FPS = 60

window = pygame.display.set_mode((window_width, HEIGHT))

#this func gets list of sprites and returns list of flipped(x-axis) sprites
def flip (images):
    flipped_sprites = []
    for image in images:
        flipped_sprites.append(pygame.transform.flip(image, True, False))
    return flipped_sprites

def load_sprite_sheets(dir, width, height, direction = False):
    """Summary line.

    The function loads images with several sprites from the directory.  
    Each image is divided into separate sprites, which are collected in lists. 
    Additional sprite lists are created for sprites with a direction. 
    After that, the lists are collected into a dictionary by their name.


    Args:
        dir (str): The name of the folder in the pictures directory.
        window_width (int): The window_width of one sprite.
        height (int): The height of one sprite.
        direction (bool): Shows if the images have a direction

    Returns:
        dict: The dictionary provides a list of proper sprites by their name.


    Examples:
        Suppose there is a "sprites" folder with two images "1.png" and "2.png" 
        in the "pictures" folder.
        "1.png" is 20x10 pixel image is made up of 2 sprites.
        "2.png" is 30x10 pixel image is made up of 3 sprites.
        The direction is irrelevant.
        Then the output will be the dictionary all_sprites{}
        all_sprites["1"] will return a list with two 10X10 sprites,
        all_sprites["3"] will return a list with two 10X10 sprites.

        >>> dir = "sprites"
        >>> window_width = 10
        >>> height = 10
        >>> direction = False
        all_sprites{}

    """
    path = join("pictures", dir) #str with the path to the directory
    files = [f for f in listdir(path) if isfile(join(path, f))] #list of titles

    all_sprites = {}#dict compares spritesheet names to the sprite lists

    for file in files:
        #loading big image(with all the sprites)
        sprite_sheet = pygame.image.load(join(path, file)).convert_alpha()

        sprites = [] #list of the sprites
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA)
            rect = pygame.Rect(i * width, 0, width, height)#going by window_width
            surface.blit(sprite_sheet, (0, 0), rect)#drawing a rectangle surf
            sprites.append(surface)

        if direction:
            #str "run.png" turning into "run_right" or "run_left"
            all_sprites[file.replace(".png", "") + "_right"] = sprites
            all_sprites[file.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[file.replace(".png", "")] = sprites
    return all_sprites