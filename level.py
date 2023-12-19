import pygame
from blocks import Block, block_size
from player import Player
from stuff import level_map, window_height, window_width
from map import csv_to_list



class Level:
    def __init__(self, level_map, surface):
        self.map_dict = level_map
        self.scroll_vel = 0
        self.display_surface = surface
        self.setup_level()
        self.offset = 0

    def setup_level(self):

        
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(200, 200))
        table = self.map_dict['blocks']
        self.blocks = self.create_blocks(table,'blocks')

    def create_blocks(self, table, type):
        sprite_group = pygame.sprite.Group()
        for i, row in enumerate(table):
            for j, symbol in enumerate(row):
                x = j * block_size
                y = i * block_size
                if symbol != "-1":
                    if type == 'blocks':
                        sprite = Block(x, y, block_size)
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
        #for blocks
        self.blocks.update(self.scroll_vel)
        self.blocks.draw(self.display_surface)
        self.scroll_x()

        #for hero
        self.player.update()
        self.horizontal_collision_movement()
        self.vertical_collision_movement()
        self.player.draw(self.display_surface)

    


