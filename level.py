import pygame
from blocks import Block, StaticBlock, block_size
from player import Player
from stuff import level_map, window_height, window_width
from settings import surrounding, layer_images



class Level:
    def __init__(self, level_number, surface):
        self.surrounding = surrounding(str(level_number))

        self.scroll_vel = 0
        self.display_surface = surface
        self.setup_level()
        self.offset = 0

    def setup_level(self):
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(100, 100))

        self.blocks = self.create_layer('blocks')
        self.grass = self.create_layer('grass')

    def create_layer(self, type):
        layer = self.surrounding[type]
        sprite_group = pygame.sprite.Group()
        for i, row in enumerate(layer):
            for j, symbol in enumerate(row):
                x = j * block_size
                y = i * block_size
                if symbol != "-1":
                    if type == 'blocks':
                        images = layer_images('blocks.png')
                        image = images[int(symbol)]
                        sprite = StaticBlock(x, y, block_size, image)
                        sprite_group.add(sprite)
                    if type == 'grass':
                        images = layer_images('grass.png')
                        image = images[int(symbol)]
                        sprite = StaticBlock(x, y, block_size, image)
                        sprite_group.add(sprite)                     
        return sprite_group      

    def scroll_x(self):
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

    def horizontal_collision_movement(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.x_vel

        for block in self.blocks.sprites():
            if block.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = block.rect.right
                elif player.direction.x > 0:
                    player.rect.right = block.rect.left       

    def vertical_collision_movement(self):
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

    def run(self):
        self.scroll_x()

        #for blocks
        self.blocks.update(self.scroll_vel)
        self.blocks.draw(self.display_surface)

        #for hero
        self.player.update()
        self.horizontal_collision_movement()
        self.vertical_collision_movement()
        self.player.draw(self.display_surface)

        #for grass
        self.grass.update(self.scroll_vel)
        self.grass.draw(self.display_surface)
    


