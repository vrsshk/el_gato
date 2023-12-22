import pygame
from images import load_sprite_sheets

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, change_hb):
        super().__init__()
        
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

        self.fall_count = 0
        self.animation_count = 0
        self.jump_count = 0
    
    def get_status(self):
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
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.y_vel

    def get_damage(self, damage):
        if not self.invincible:
            self.change_hb(damage)
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()

    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks() 
            if current_time - self.hurt_time >= self.invincibility_delay:
                self.invincible = False

    def update(self):
        self.handle_move()
        self.get_status()
        self.animate()
        self.invincibility_timer()
