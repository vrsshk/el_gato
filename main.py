import pygame, sys
import os
from level import Level
from overworld import Overworld
from ui import UI
from data import window_height, window_width, fps
pygame.init() 

class Game:
    def __init__(self):
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
        self.level = Level(current_level, window, self.create_overworld, self.change_coins, self.change_hb)
        self.status = 'level'

    def create_overworld(self):
        self.status = 'overworld'

    def change_hb(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.exit = True
            self.exit_time = pygame.time.get_ticks()


    def exit_timer(self):
        if self.exit == True:
            im = pygame.image.load(os.path.join("assets", "bg", "bg_defeat.png"))
            window.blit(im,[0,0])
            current_time = pygame.time.get_ticks()
            if current_time - self.exit_time >= self.exit_delay:
                self.create_overworld()
        
    def change_coins(self):
        self.coins += 1

    def run(self):
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