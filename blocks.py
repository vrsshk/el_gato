import pygame
from os.path import join

from images import sprite_separator

block_size = 32

class Block(pygame.sprite.Sprite):
    """Класс для создания квадратного блока в игре.

    Block получен наследованием класса pygame.sprite.Sprite,
    базового класс для создания видимых игровых объектов.
    """
    
    def __init__(self, x, y, size):
        """Инициализация блока.

        Args:
            x (int): Расположение блока по оси x.
            y (int): Расположение блока по оси y.
            size (int): Размер блока.
        
        Attributes:
            image (Surface): Квадратная область для изображения блока.
            rect (Rect): Объект для хранения прямоугольных координат блока.
        """
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(top = y, left = x)
    def update(self, x_offset):
        """Двигает блок при движении "камеры".

        Args:
            x_offset (int): Изменение расположения блоков при движении камеры.
        """
        self.rect.x += x_offset


class StaticBlock(Block):
    """Блок со статичным изображением.

    Получен наследованием класса Block.
    """
    def __init__(self, x, y, size, surface):
        """Инициализация блока.

        Args:
            x (int): Расположение блока по оси x.
            y (int): Расположение блока по оси y.
            size (int): Размер блока.
            surface (Surface): Изображение(спрайт) блока.
        """
        super().__init__(x, y, size)
        self.image = surface

class AnimatedBlock(Block):
    """Блок с динамичным изображением (анимацией).

    Получен наследованием класса Block.
    """
    def __init__(self, x, y, size, file_name):
        """Инициализация блока.

        Args:
            x (int): Расположение блока по оси x.
            y (int): Расположение блока по оси y.
            size (int): Размер блока.
            file_name (_type_): Название файла, содержащего нужные спрайты.

        Attributes:
            sprites (list): Список спрайтов.
            animation_index (int): Индекс анимации.
        """
        super().__init__(x, y, size)
        path =  join("assets", "surrounding", file_name)
        sprite_sheet = pygame.image.load(path).convert_alpha()
        self.sprites = sprite_separator(sprite_sheet, size, size)
        self.animation_index = 0
    def animate(self):
        """Метод анимации персонажа.
        """
        self.animation_index += 0.15
        if self.animation_index > len(self.sprites):
            self.animation_index = 0
        self.image = self.sprites[int(self.animation_index)]
    def update(self, x_offset):
        """Двигает блок при движении "камеры", вызывает метод анимации.

        Args:
            x_offset (int): Изменение расположения блоков при движении камеры.
        """
        self.animate()
        self.rect.x += x_offset