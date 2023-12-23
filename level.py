import pygame
import os
from blocks import Block, AnimatedBlock, StaticBlock, block_size
from player import Player
from settings import surrounding, layer_images
from bats import Bat
from data import window_height, window_width

class Level:
    """Класс Level используется для создания игрового уровня.
    """

    def __init__(self, level_number, surface, create_overworld, change_coins, change_hb):
        """Инициализация уровня.

        Args:
            level_number (int): Номер уровня.
            surface (Surface): Область для изображения уровня, игровое окно.
            create_overworld (method): Метод класса Game, возвращающий окно с выбором уровней.
            change_coins (method): Метод класса Game, изменяющий количество монет.
            change_hb (method): Метод класса Game, изменяющий количество здоровья.

        Attributes:
            surrounding (dict): Словарь, сопоставляющий названия объектов с таблицами их координат.
            scroll_vel (int): Скорость перемещения "камеры".
            display_surface (Surface): Область для изображения уровня, игровое окно.
            change_coins (method): Метод, изменяющий количество монет.
            change_hb (method): Метод, изменяющий количество здоровья.
            create_overworld (method): Метод, возвращающий окно с выбором уровней.
            defeat_bg (Surface): Изображение для игрового окна в случае поражения.
            victory_bg (Surface): Изображение для игрового окна в случае победы.
            exit (bool): Переменная, показывающая начат ли возврат в меню.
            exit_delay (int): Длительность возврата в меню.
            exit_time (int): Время начала возврата в меню.
            player (GroupSingle): Группа, содержащая героя класса Player.
        """
        #level setup
        self.surrounding = surrounding(level_number)
        self.scroll_vel = 0
        self.display_surface = surface
        self.setup_level()

        #ui setup
        self.change_coins = change_coins
        self.change_hb = change_hb
        
        #overworld
        self.create_overworld = create_overworld

        self.defeat_bg = pygame.image.load(os.path.join("assets", "bg", "bg_defeat.png"))
        self.victory_bg = pygame.image.load(os.path.join("assets", "bg", "bg_victory.png"))        
        #timer
        self.exit = False
        self.exit_delay = 4000
        self.exit_time = 0

        #player
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(32, 320, self.change_hb))

    def handle_input(self):
        """Метод для выхода в меню с помощью клавиатуры.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.create_overworld()

    def setup_level(self):
        """Метод, задающий группы объектов для игрового уровня.
        """
        self.blocks = self.create_layer('blocks')
        self.grass = self.create_layer('grass')
        self.coins = self.create_layer('coins')
        self.bats = self.create_layer('bats')
        self.barrier = self.create_layer('barrier')

    def create_layer(self, object):
        """Метод, собирающий объекты в группы в зависимости от их карт.

        С помощью функции surrounding формируется "таблица" с координатами 
        для нужноых объектов.
        Пробегая по строкам таблицы, проверяется наличие объекта 
        на текущей позиции. При наличии объекта, он добавляется в группу,
        с учетом своего класса.

        Args:
            object (str): Название объекта (blocks, grass, etc.)

        Returns:
            Group: Группа объектов с необходимыми координатами.
        """
        layer = self.surrounding[object]
        sprite_group = pygame.sprite.Group()
        for i, row in enumerate(layer):
            for j, symbol in enumerate(row):
                x = j * block_size
                y = i * block_size
                if symbol != "-1":
                    if object == 'blocks':
                        images = layer_images('blocks.png')
                        image = images[int(symbol)]
                        sprite = StaticBlock(x, y, block_size, image)
                        sprite_group.add(sprite)
                    if object == 'grass':
                        images = layer_images('grass.png')
                        image = images[int(symbol)]
                        sprite = StaticBlock(x, y, block_size, image)
                        sprite_group.add(sprite)
                    if object == 'coins':
                        x_1 = x + 8
                        y_1 = y + 8
                        sprite = AnimatedBlock(x_1, y_1, 16, 'coins.png')
                        sprite_group.add(sprite)
                    if object == 'bats':
                        x_1 = x - 16
                        y_1 = y - 16
                        sprite = Bat(x_1, y_1)
                        sprite_group.add(sprite)
                    if object == 'barrier':
                        x_1 = x
                        y_1 = y
                        sprite = Block(x_1, y_1, block_size)
                        sprite_group.add(sprite)
         
        return sprite_group
    
    def bats_reverse(self):
        """Метод, разворачивающий летучих мышей.
        """
        for bat in self.bats.sprites():
            if pygame.sprite.spritecollide(bat, self.barrier, False):
                bat.reverse()

    def scroll_x(self):
        """Метод, задающий камеру.
        
        Нужен для сдвига объектов при подходе героя к краю игровой области.
        """
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if (player_x < window_width / 4) and (direction_x < 0):
            player.x_vel = 0
            self.scroll_vel = 5
        elif (player_x > 3 * window_width / 4) and (direction_x > 0):
            player.x_vel = 0
            self.scroll_vel = -5

        else:
            self.scroll_vel = 0
            player.x_vel = 5
    
    def check_fall(self):
        """Метод для проверки героя на падение из игровой области.
        """
        player = self.player.sprite
        player_y = player.rect.centery
        if player_y > 1000:
            self.player.sprite.get_damage(100)

    def horizontal_collision_movement(self):
        """Метод для горизонатального взаимодействия героя с блоками.
        """
        player = self.player.sprite
        player.rect.x += player.direction.x * player.x_vel

        for block in self.blocks.sprites():
            if block.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = block.rect.right
                elif player.direction.x > 0:
                    player.rect.right = block.rect.left       

    def vertical_collision_movement(self):
        """Метод для вертикального взаимодействия героя с блоками.
        """
        player = self.player.sprite
        player.gravity_on()

        for block in self.blocks.sprites():
            if block.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = block.rect.top
                    player.direction.y = 0
                    player.landed = True
                elif player.direction.y < 0:
                    player.rect.top = block.rect.bottom
                    player.direction.y = 0
        if player.landed and player.direction.y < 0:
            player.landed = False

    def bat_collision(self):
        """Метод для взаимодействия героя с летучими мышами.
        """
        bat_collisions = pygame.sprite.spritecollide(self.player.sprite, self.bats, False)

        if bat_collisions:
            for bat in bat_collisions:
                bat_center = bat.rect.centery
                bat_top = bat.rect.top
                player_bottom = self.player.sprite.rect.bottom
                if (bat_top < player_bottom < bat_center) and self.player.sprite.direction.y >= 0:
                    self.player.sprite.direction.y = -10
                    bat.status = 'angry'
                    if bat.dead: 
                        bat.kill()
                else:
                    if bat.status == 'angry':
                        self.player.sprite.get_damage(15)
                    else:
                        self.player.sprite.get_damage(5)

    def coin_collision(self):
        """Метод для взаимодействия героя с монетками.
        """
        player = self.player.sprite
        for coin in self.coins.sprites():
            if coin.rect.colliderect(player.rect):
                self.change_coins()
                self.coins.remove(coin)
                if len(self.coins.sprites()) == 0:
                    self.exit = True
                    self.exit_time = pygame.time.get_ticks()

    def exit_timer(self):
        """Счетчик периода выхода после начала возврата в меню.
        """
        if self.exit == True:
            im = pygame.image.load(os.path.join("assets", "bg", "bg_victory.png"))
            self.display_surface.blit(im,[0,0])
            current_time = pygame.time.get_ticks()
            if current_time - self.exit_time >= self.exit_delay:
                self.create_overworld()

    def run(self):
        """Метод, вызывающий основные методы класса.
        """

        self.handle_input()
        self.scroll_x()

        #for blocks
        self.blocks.update(self.scroll_vel)
        self.blocks.draw(self.display_surface)

        #for hero
        self.player.update()
        self.horizontal_collision_movement()
        self.vertical_collision_movement()
        self.player.draw(self.display_surface)

        #for coins
        self.coins.update(self.scroll_vel)
        self.coin_collision()
        self.coins.draw(self.display_surface)

        #for bats
        self.barrier.update(self.scroll_vel)
        self.bats_reverse()
        self.bats.update(self.scroll_vel)
        self.bats.draw(self.display_surface)

        #for grass
        self.grass.update(self.scroll_vel)
        self.grass.draw(self.display_surface)

        #check damage
        self.bat_collision()
        self.check_fall()
        self.exit_timer()
    


