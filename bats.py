import pygame
from random import randint

from images import load_sprite_sheets

class Bat(pygame.sprite.Sprite):
    """Класс Bats используется для создания летучих мышей в игре.
    """
    def __init__(self, x, y):
        """Инициализация летучей мыши.

        Args:
            x (int): Расположение мыши по оси x.
            y (int): Расположение мыши по оси y.

        Atributes:
            image (Surface): Область для изображения мыши.
            rect (Rect): Объект для хранения прямоугольных координат мыши.
            direction_name (str): Название направления мыши по оси x.
            animations (dict): Словарь, который сопоставляет название анимации с набором нужных картинок.
            animation_index (int): Индекс анимации.
            status (str): Текущий статус мыши.
            speed (int): Скорость мыши по оси x.
        """
        super().__init__()
        self.image = pygame.Surface((48, 48), pygame.SRCALPHA)
        self.rect = self.image.get_rect(top = y, left = x)
        self.direction = "right"

        #animation
        self.animations = load_sprite_sheets("bat", 48, 48, True)
        self.animation_index = 0

        #status
        self.dead = False
        self.status = "idle"

        #movement
        self.speed = randint(1, 2)

    def animate(self): 
        """Метод анимации мыши.
        """
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
        """Метод, поворачивающий мышь.
        """
        self.speed *= -1
    
    def move(self):
        """Метод движения мыши.
        """
        self.rect.x += self.speed
    
    def update(self, shift):
        """Вызывает основные методы класса и сдвигает мышь при движении "камеры".

        Args:
            shift (int): Изменение расположения блоков при движении камеры.
        """
        self.rect.x += shift
        self.animate()
        self.move()
