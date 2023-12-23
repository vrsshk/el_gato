from images import load_sprite_sheets, sprite_separator
from settings import surrounding
import pygame
import os

#load_sprite_sheets
def test_sprites1():
    assert len(load_sprite_sheets("hero", 39, 48, True)["fall_right"]) == 6 

def test_sprites2():
    assert len(load_sprite_sheets("hero", 39, 48, True)["idle_right"]) == 6 

def test_sprites3():
    assert len(load_sprite_sheets("hero", 39, 48, True)["jump_right"]) == 6 

def test_sprites4():
    assert len(load_sprite_sheets("hero", 39, 48, True)["run_right"]) ==  8

def test_sprites5():
    assert len(load_sprite_sheets("hero", 39, 48, True)["fall_left"]) == 6 

def test_sprites6():
    assert len(load_sprite_sheets("hero", 39, 48, True)["idle_left"]) == 6 

def test_sprites7():
    assert len(load_sprite_sheets("hero", 39, 48, True)["jump_left"]) == 6 

def test_sprites8():
    assert len(load_sprite_sheets("hero", 39, 48, True)["run_left"]) ==  8

def test_sprites9():
    assert type(load_sprite_sheets("hero", 39, 48, True)["fall_right"][0]) == pygame.surface.Surface

def test_sprites10():
    assert type(load_sprite_sheets("hero", 39, 48, True)["fall_right"]) == list

def test_sprites10():
    assert len(load_sprite_sheets("hero", 39, 48, True)) == 10


#sprite_separator
def test_sprites11():
    image = pygame.image.load(os.path.join("assets", "hero", "damage.png"))
    sprites = sprite_separator(image, 39, 48)
    assert len(sprites) == 3 

def test_sprites12():
    image = pygame.image.load(os.path.join("assets", "hero", "fall.png"))
    sprites = sprite_separator(image, 39, 48)
    assert len(sprites) == 6

def test_sprites13():
    image = pygame.image.load(os.path.join("assets", "hero", "jump.png"))
    sprites = sprite_separator(image, 39, 48)
    assert len(sprites) == 6

def test_sprites14():
    image = pygame.image.load(os.path.join("assets", "hero", "idle.png"))
    sprites = sprite_separator(image, 39, 48)
    assert len(sprites) == 6

def test_sprites15():
    image = pygame.image.load(os.path.join("assets", "hero", "run.png"))
    sprites = sprite_separator(image, 39, 48)
    assert len(sprites) == 8

def test_sprites16():
    image = pygame.image.load(os.path.join("assets", "bat", "angry.png"))
    sprites = sprite_separator(image, 48, 48)
    assert len(sprites) == 5

def test_sprites17():
    image = pygame.image.load(os.path.join("assets", "bat", "idle.png"))
    sprites = sprite_separator(image, 48, 48)
    assert len(sprites) == 5

def test_sprites18():
    image = pygame.image.load(os.path.join("assets", "bat", "dead.png"))
    sprites = sprite_separator(image, 48, 48)
    assert len(sprites) == 5

def test_sprites19():
    image = pygame.image.load(os.path.join("assets", "bat", "angry.png"))
    sprites = sprite_separator(image, 48, 48)
    assert type(sprites[0]) == pygame.surface.Surface

#surrounding
def test_sprites20():
    assert type(surrounding(0)) == dict

def test_sprites21():
    assert type(surrounding(0)['barrier']) == list

def test_sprites22():
    assert type(surrounding(0)['bats']) == list

def test_sprites23():
    assert type(surrounding(0)['blocks']) == list

def test_sprites24():
    assert type(surrounding(0)['coins']) == list

def test_sprites25():
    assert type(surrounding(0)['grass']) == list

def test_sprites26():
    assert type(surrounding(0)['barrier'][0]) == list

def test_sprites27():
    assert type(surrounding(0)['barrier'][1]) == list

def test_sprites28():
    assert type(surrounding(0)['bats'][3]) == list

def test_sprites29():
    assert type(surrounding(0)['blocks'][4]) == list

def test_sprites30():
    assert type(surrounding(0)['coins'][7]) == list

def test_sprites31():
    assert type(surrounding(0)['grass'][0]) == list

def test_sprites32():
    names = ['barrier', 'grass', 'blocks', 'coins', 'bats']
    k = 0
    for name in names:
        map = surrounding(0)[name]
        k += len(map)
    assert k == 110

def test_sprites33():
    names = ['barrier', 'grass', 'blocks', 'coins', 'bats']
    k = 0
    for name in names:
        map = surrounding(1)[name]
        k += len(map)
    assert k == 110

def test_sprites34():
    names = ['barrier', 'grass', 'blocks', 'coins', 'bats']
    k = 0
    for name in names:
        map = surrounding(2)[name]
        k += len(map)
    assert k == 110
