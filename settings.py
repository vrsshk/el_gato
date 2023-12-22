import pygame
from os import listdir
from os.path import join, basename
from csv import reader

from blocks import block_size

def surrounding(level_number):
    path = join("map",level_number)
    files = []
    for f in listdir(path):
        files.append(join(path, f))

    surrounding = {}

    for file in files:
        layer = []
        with open(file) as f:
            read_file = reader(f, delimiter=',')
            for row in read_file:
                layer.append(list(row))
        surrounding[basename(file).replace(".csv", "")] = layer
    return surrounding

def layer_images(file_name):

    path = join ("assets", "surrounding", file_name)
    big_image = pygame.image.load(path).convert_alpha()
    x_number = int(big_image.get_size()[0] / block_size)
    y_number = int(big_image.get_size()[1] / block_size)

    images = []
    for row in range(y_number):
        for col in range(x_number):
            x = col*block_size
            y = row*block_size
            surface = pygame.Surface((block_size, block_size), pygame.SRCALPHA)
            surface.blit(big_image, (0, 0), pygame.Rect(x,y, block_size, block_size))
            images.append(surface)

    return images
