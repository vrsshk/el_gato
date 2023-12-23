import pygame
from os import listdir
from os.path import join, basename
from csv import reader

from blocks import block_size

def surrounding(level_number):
    """Функция, преобразующая csv файлы для необходимого игрового уровня.

    В зависимости от номера уровня открывается необходимая папка с csv файлами
    (картами). Каждая карта преобразуется в набор (list) построчных наборов
    (list) координат (str). Т.е. каждая карта представляет "таблицу" с координатами
    нужных объектов. Все преобразованные карты собираются в словарь, 
    который сопоставляет их с названиями файлов (названия объектов сопоставлены
    таблицам с их координатами).

    Args:
        level_number (int): Номер уровня.

    Returns:
        dict: Сопоставляет названия csv файлов с их содержанием. 
    """
    path = join("map",str(level_number))
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
    """Разбивает изображение на отдельные области, возвращает их списком.

    На вход подается название изображения из папки assets/surrounding.
    Изображение нарезается сеткой с ячейками размера 32*32.
    Формируется список новых изображений (Surface). Изображаения 
    добавляются в порядке слева направо, сверух вниз.

    Args:
        file_name (str): Название необходимого изображения.

    Returns:
        list: Набор новых изображений.
    """

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