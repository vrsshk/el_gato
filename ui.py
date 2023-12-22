import pygame
from os.path import join
from images import sprite_separator

class UI:
    def __init__(self, surface):
        #
        self.display_surface = surface

        #helth
        self.health_bar = pygame.image.load(join('assets', 'surrounding', 'health.png')).convert_alpha()
        #coins
        self.coin = pygame.image.load(join('assets', 'surrounding', 'money.png')).convert_alpha()
        self.font = pygame.font.Font('../assets/surrounding/fibberish.ttf', 30)

    def show_health(self, current_healf, full_health):
        self.display_surface.blit(self.health_bar, (15, 55))
    
    def show_coins(self, amount):
        self.display_surface.blit(self.coin, (15, 15))
        