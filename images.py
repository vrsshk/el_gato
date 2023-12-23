import pygame
from os import listdir
from os.path import isfile, join

window_width= 1120
window_height = 704
window = pygame.display.set_mode((window_width, window_height))


def flip (images):
    """Отзеркаливает спрайты из списка по оси х.

    Args:
        images (list): Набор изображений (Surface).

    Returns:
        list: Набор отзеркаленных изображений (Surface).
    """
    flipped_sprites = []
    for image in images:
        flipped_sprites.append(pygame.transform.flip(image, True, False))
    return flipped_sprites

#Следующие функции заимствованы из видеоролика с канала freeCodeCamp.org

def sprite_separator(sprite_sheet, width, height):
    """Нарезка большого изображения на спрайты.

    Спрайты должны расставлены в большом изображении горизонтально, 
    т.к. нарезка просиходит проходом по ширине изображения. 

    Args:
        sprite_sheet (Surface): Изображение с несколькими спрайтами.
        width (int): Ширина одного спрайта.
        height (int): Высота одного спрайта.

    Returns:
        list: Набор спрайтов.
    """
    sprites = [] #list of the sprites
    for i in range(sprite_sheet.get_width() // width):
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        rect = pygame.Rect(i * width, 0, width, height)#going by window_width
        surface.blit(sprite_sheet, (0, 0), rect)#drawing a rectangle surf
        sprites.append(surface)
    return sprites


def load_sprite_sheets(dir, width, height, direction = False):
    """Загрузка изображений для анимации.

    Функция загружает изображения с несколькими спрайтами из указанной 
    папки (dir).  Каждое изображение разделяется на отдельные спрайты с помощью 
    функции sprite_separator, которые далее собираются в наборы (list).
    Полученные наборы собираются в словарь по их имени.
    Для изображений, в которых нужно учитывать направление создается 2 набора
    для каждого направления.


    Args:
        dir (str): Название необходимой директории в папке assets.
        width (int): Ширина одного спрайта.
        height (int): Высота одного спрайта.
        direction (bool): Показывает имеет ли изображение направление.

    Returns:
        dict: Словарь, сопоставляет названия(str) с наборами спрайтов (list of surfaces).


    Examples:
        Пусть в папке assets/sprites находятся 2 изображения "1.png" и "2.png".
        Изображение "1.png" размера 20x10 пикселя состоит из 2 спрайтов.
        Изображение "2.png" размера 30x10 пикселя состоит из 3 спрайтов.
        Направление не учитывается. Вызовем функцию с подходящими параметрами.
        all_sprites = load_sprite_sheets("sprites", 10, 10, False)
        Словарь all_sprites будет содержать 2 списка изображений.
        all_sprites["1"] возвращает список с двумя спрайтами 10Х10,
        all_sprites["3"]  возвращает список с тремя спрайтами 10Х10.

        >>> dir = "sprites"
        >>> window_width = 10
        >>> height = 10
        >>> direction = False
        all_sprites{}
    """
    path = join("assets", dir) #str with the path to the directory
    files = [f for f in listdir(path) if isfile(join(path, f))] #list of titles

    all_sprites = {}#dict compares spritesheet names to the sprite lists

    for file in files:
        #loading big image(with all the sprites)
        sprite_sheet = pygame.image.load(join(path, file)).convert_alpha()
        sprites = sprite_separator(sprite_sheet, width, height)

        if direction:
            #str "run.png" turning into "run_right" or "run_left"
            all_sprites[file.replace(".png", "") + "_right"] = sprites
            all_sprites[file.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[file.replace(".png", "")] = sprites
    return all_sprites

