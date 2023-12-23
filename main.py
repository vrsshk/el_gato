import pygame, sys
import os
from level import Level
from overworld import Overworld
from ui import UI
from data import window_height, window_width, fps
pygame.init() 

class Game:
    """Основной класс игры.
    """
    def __init__(self):
        """Инициализация игры.

        Attributes:
            ui (UI): Пользовательский интерфейс (шкала здоровья и количество монет)
            full_health (int): Полное количество здоровья героя.
            current_health (int): Текущее количество здоровья героя.
            coins (int): Количество монет,собранных героем
            exit (bool): Переменная, показывающая начат ли возврат в меню.
            exit_delay (int): Длительность возврата в меню.
            exit_time (int): Время начала возврата в меню.
            overworld (Overworld): Меню с выбором уровня.
            status (str): Текущий статус игры (меню или уровень)
        """
        #game atributes
        self.ui = UI(window)
        self.ful_health = 90
        self.current_health = 90
        self.coins = 0
        
        #timer
        self.exit = False
        self.exit_delay = 1500
        self.exit_time = 0

        #create overworld
        self.overworld = Overworld(0, 2, window, self.create_level)
        self.status = 'overworld'
    
    def create_level(self, current_level):
        """Метод создания класса в зависимости от выбранного уровня.

        Args:
            current_level (int): Текущий уровень.
        """
        self.level = Level(current_level, window, self.create_overworld, self.change_coins, self.change_hb)
        self.status = 'level'

    def create_overworld(self):
        """Метод создания (выхода в) меню.
        """
        self.status = 'overworld'

    def change_hb(self, damage):
        """Метод для получения урона героем.

        Args:
            damage (int): Количество нанесенного урона.
        """
        self.current_health -= damage
        if self.current_health <= 0:
            self.exit = True
            self.exit_time = pygame.time.get_ticks()


    def exit_timer(self):
        """Счетчик периода выхода после начала возврата в меню.
        """
        if self.exit == True:
            im = pygame.image.load(os.path.join("assets", "bg", "bg_defeat.png"))
            window.blit(im,[0,0])
            current_time = pygame.time.get_ticks()
            if current_time - self.exit_time >= self.exit_delay:
                self.create_overworld()
        
    def change_coins(self):
        """Метод, меняющий количество монет.
        """
        self.coins += 1

    def run(self):
        """Метод обновления игры.

        Загружает фоновое изображение, проверяет статус игры и 
        в зависимости от него вызывает необходимые методы.
        """
        im = pygame.image.load(os.path.join("assets", "bg", "bg.png"))
        window.blit(im,[0,0])

        if self.status == 'overworld':
            self.overworld.run()
        elif self.status == 'level':
            self.level.run()
            self.ui.show_health(self.current_health, self.ful_health)
            self.ui.show_coins(self.coins)
            self.exit_timer()

window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.run()
    
    pygame.display.update()
    clock.tick(fps)