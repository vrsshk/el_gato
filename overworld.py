from typing import Any
import pygame
from data import levels, icon_picture
from level import Level

class Node(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((222, 124))

        self.rect = self.image.get_rect(center = pos)

class Icon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((222, 124))
        self.image = icon_picture
        self.rect = self.image.get_rect(center = pos)
    

class Overworld:
    def __init__(self, start_level, max_level, surface, create_level):

        #setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level
        self.create_level = create_level

        #
        self.press_index = 0
        self.press_speed = 0.13

        #sprites
        self.setup_nodes()
        self.setup_icon()

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()
        for data in levels.values():
            node_sprite = Node(data['node_pos'])
            node_sprite.image = data['node_picture']
            self.nodes.add(node_sprite)

    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center) 
        self.icon.add(icon_sprite)

    def handle_input(self):
        self.press_index += self.press_speed
        if self.press_index > 1:
            self.press_index = 0

        keys = pygame.key.get_pressed()
        if self.press_index == 0:
            if keys[pygame.K_RIGHT] and self.current_level < 2:
                self.current_level += 1
            elif keys[pygame.K_LEFT] and self.current_level > 0:
                self.current_level -= 1
            elif keys[pygame.K_SPACE] or keys[pygame.K_KP_ENTER]:
                self.create_level(self.current_level)

    def update_icon_position(self):
        self.icon.sprite.rect.center = self.nodes.sprites()[self.current_level].rect.center

    def run(self):
        self.handle_input()

        self.update_icon_position()
        
        self.icon.draw(self.display_surface)
        self.nodes.draw(self.display_surface)



'''

    def get_move_vector(self, d):
        start = pygame.math.Vector2(self.nodes.sprites()[self.current_level].rect.center)
        end = pygame.math.Vector2(self.nodes.sprites()[self.current_level + d].rect.center)

        return (end - start).normalize()
    
    def update_icon_position(self):
        if self.moving and self.moving_vector:

            self.icon.sprite.pos += self.moving_vector * 5
            target_node = self.nodes.sprites()[self.current_level]'''