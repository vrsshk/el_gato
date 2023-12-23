from typing import Any
import pygame
from data import levels, icon_picture


#Код в этом файле частично заимствован код из видеоролика с канала Clear Code
#https://youtu.be/IUe2pdTWroc?si=hnEfNgZaZEhbbKQm

class Node(pygame.sprite.Sprite):
    """Класс Node используется для создания таблички с названием уровня в меню.
    """
    def __init__(self, pos):
        """Инициализация

        Args:
            pos (tuple): Координаты таблички.

        Attributes:
            image (Surface): Область для изображения таблички.
            rect (Rect): Объект для хранения прямоугольных координат героя.
        """
        super().__init__()
        self.image = pygame.Surface((222, 124))
        self.rect = self.image.get_rect(center = pos)

class Icon(pygame.sprite.Sprite):
    """Класс для изображения выбора таблички.
    """
    def __init__(self, pos):
        """Инициализация

        Args:
            pos (tuple): Координаты таблички.

        Attributes:
            image (Surface): Область для изображения таблички.
            rect (Rect): Объект для хранения прямоугольных координат героя.
        """
        super().__init__()
        self.image = pygame.Surface((222, 124))
        self.image = icon_picture
        self.rect = self.image.get_rect(center = pos)
    

class Overworld:
    """Класс для создания меню с выбором уровней.
    """
    def __init__(self, start_level, max_level, surface, create_level):
        """Инициализация меню.

        Args:
            start_level (int): Уровень, выбранный при запуске.
            max_level (int): Максимальный возможный уровень
            surface (Surface): Область для изображения меню, игровое окно.
            create_level (method): Метод класса Game, запускающий режим уровня.
        """

        #setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level
        self.create_level = create_level

        #timer
        self.pressed = False
        self.pressed_delay = 150
        self.press_time = 0

        #sprites
        self.setup_nodes()
        self.setup_icon()

    def setup_nodes(self):
        """Метод, задающий группу табличек.
        """
        self.nodes = pygame.sprite.Group()
        for data in levels.values():
            node_sprite = Node(data['node_pos'])
            node_sprite.image = data['node_picture']
            self.nodes.add(node_sprite)

    def setup_icon(self):
        """Метод, задающий иконку выбора нужной текущей таблицы.
        """
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center) 
        self.icon.add(icon_sprite)

    def handle_input(self):
        """Метод для управления меню с помощью клавиатуры.
        """
        keys = pygame.key.get_pressed()
        if not self.pressed:
            if keys[pygame.K_RIGHT] and self.current_level < 2:
                self.current_level += 1
                self.pressed = True
                self.press_time = pygame.time.get_ticks() 
            elif keys[pygame.K_LEFT] and self.current_level > 0:
                self.current_level -= 1
                self.pressed = True
                self.press_time = pygame.time.get_ticks() 
            elif keys[pygame.K_SPACE] or keys[pygame.K_KP_ENTER]:
                self.create_level(self.current_level)
                self.pressed = True
                self.press_time = pygame.time.get_ticks() 
    
    def press_timer(self):
        """Счетчик времени, прошедего после нажатия на кнопку.
        """
        if self.pressed:
            current_time = pygame.time.get_ticks() 
            if current_time - self.press_time >= self.pressed_delay:
                self.pressed = False

    def update_icon_position(self):
        """Обновление расположения иконки "выбора".
        """
        self.icon.sprite.rect.center = self.nodes.sprites()[self.current_level].rect.center

    def run(self):
        """Метод обновления.

        Вызывает основные методы класса, отрисовывает таблички уровней и иконку выбора.
        """
        self.handle_input()

        self.update_icon_position()
        
        self.icon.draw(self.display_surface)
        self.nodes.draw(self.display_surface)
        self.press_timer()
