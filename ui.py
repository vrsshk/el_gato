import pygame
from os.path import join
from images import sprite_separator

class UI:
    def __init__(self, surface):
        #
        self.display_surface = surface

        #helth
        self.health = pygame.image.load(join('assets', 'surrounding', 'health.png')).convert_alpha()
        self.hb = pygame.image.load(join('assets', 'surrounding', 'health_bar.png')).convert_alpha()

        self.hb_left = 29
        self.hb_down = 177
        self.hb_max_height = 90
        self.hb_width = 6

        #coins
        self.coin = pygame.image.load(join('assets', 'surrounding', 'money_1.png')).convert_alpha()
        self.font = pygame.font.Font(join('assets', 'surrounding', 'fibberish.ttf'), 30)

    def show_health(self, current_health, full_health):
        self.display_surface.blit(self.health, (15, 55))
        hb_rect = pygame.Rect((0, 0),(self.hb_width, current_health))
        self.display_surface.blit(self.hb, (self.hb_left, self.hb_down - current_health), hb_rect )

    
    def show_coins(self, amount):
        self.display_surface.blit(self.coin, (15, 15))
        coin_amount_surf = self.font.render(str(amount), False, '#382F35')
        coin_amount_rect = coin_amount_surf.get_rect(midleft = (50, 35))
        self.display_surface.blit(coin_amount_surf, coin_amount_rect)
        