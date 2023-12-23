import pygame
from images import load_sprite_sheets

class Player(pygame.sprite.Sprite):
    """Класс Player используется для создания героя в игре.


    Player получен наследованием класса pygame.sprite.Sprite,
    базового класс для создания видимых игровых объектов.
    """    
    
    def __init__(self, x, y, change_hb):
        """Инициализация героя.

        Args:
            x (int): Расположение героя по оси x.
            y (int): Расположение героя по оси y.
            change_hb (func): Функция, изменяющая количество здоровья.

        Atributes:
            image (Surface): Область для изображения героя.
            rect (Rect): Объект для хранения прямоугольных координат героя.
            direction (Vector2): Двумерный вектор, показывающий направление движения героя.
            direction_name (str): Название направления героя по оси x.
            change_hb (method): Метод класса Game, изменяющий количество здоровья.
            invincible (bool): Переменная, показывающающая неуязвим ли герой.
            invincibility_delay (int): Длительность периода неуязвимости героя.
            hurt_time (int): Время, в которе герой получил урон.
            animations (dict): Словарь, который сопоставляет название анимации с набором нужных картинок.
            animation_index (int): Индекс анимации.
            animation_speed (float): Скорость анимации.
            status (str): Текущий статус героя.
            landed (bool): Переменная, показывающающая находится ли герой на земле.
            x_vel (int): Скорость героя по оси x.
            y_vel (int): Начальная скорость героя при прыжке по оси y.
            gravity (float): Гравитационное изменение скорости по оси y.
        """
        super().__init__()
        
        #
        self.image = pygame.Surface((39, 48), pygame.SRCALPHA)
        self.rect = self.image.get_rect(top = y, left = x)
        self.direction = pygame.math.Vector2(0, 0)
        self.direction_name = "right"

        #health
        self.change_hb = change_hb
        self.invincible = False
        self.invincibility_delay = 2000
        self.hurt_time = 0
 
        #animation
        self.animations = load_sprite_sheets("hero", 39, 48, True)
        self.animation_index = 0
        self.animation_speed = 0.2

        #status
        self.status = "idle"
        self.landed = False

        #movement
        self.x_vel = 5
        self.y_vel = -14
        self.gravity = 0.5
    
    def get_status(self):
        """Метод для определения статуса героя.
        """
        if self.invincible:
            self.status = 'damage'
        elif self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 0:
            self.status = "fall"
        elif self.direction.y == 0:
            if self.direction.x ==0:
                self.status = "idle"
            else:
                self.status = "run"


    def animate(self):
        """Метод для анимации героя.

        В зависимости от статуса героя и его направления по оси x
        формируется набор изображений animation. Индекс анимации меняется
        с учетом скорости смены анимации. В зависмости от индекса анимации меняется
        изображение героя.
        Индекс обнуляется, есди превосходит количество изображений в наборе.
        """
        
        if self.direction.x > 0: 
            self.direction_name = "right"
        elif self.direction.x < 0: 
            self.direction_name = "left"
        
        animation = self.animations[self.status + "_" + self.direction_name]

        self.animation_index += self.animation_speed
        if self.animation_index > len(animation):
            self.animation_index = 0
        self.image = animation[int(self.animation_index)]

    def handle_move(self):
        """Метод для управления героем с помощью клавиатуры.

        При нажатии на левую стрелку, вектор направления героя по оси x
        меняется на -1. При нажатии на правую стрелку, вектор направления 
        героя по оси x меняется на 1. При нажатии пробела вызывается метод
        прыжка.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.landed:
            self.jump()

    def gravity_on(self):
        """Метод для учета гравитации.
        """
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        """Метод для прыжка.
        """
        self.direction.y = self.y_vel

    def get_damage(self, damage):
        """Метод для нанесения урона герою.

        Не срабатывает, если герой находится в периоде неуязвимости после получения предыдущего урона.

        Args:
            damage (int): Количество урона, которое вычтется из шкалы здоровья.
        """
        if not self.invincible:
            self.change_hb(damage)
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()
    
    def invincibility_timer(self):
        """Счетчик периода неуязвимости после получения урона.
        """
        if self.invincible:
            current_time = pygame.time.get_ticks() 
            if current_time - self.hurt_time >= self.invincibility_delay:
                self.invincible = False

    def update(self):
        """Метод обновления.

        Вызывает основные методы класса.
        """
        self.handle_move()
        self.get_status()
        self.animate()
        self.invincibility_timer()
