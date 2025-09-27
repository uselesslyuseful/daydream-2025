import pygame
from pygame.locals import *
import math

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def create_object(objectName):
    object = pygame.sprite.Sprite()
    object.name = objectName
    return object

def update_object(object):
    if object.image == object.image1:
        object.image = object.image0
        object.rect = object.image.get_rect(center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2))

def create_map():
    mapBG = pygame.sprite.Sprite()
    mapBG.y = 0
    mapBG.image = pygame.image.load("mapbg.png")
    mapBG.rect = mapBG.image.get_rect(topleft=(0,SCREEN_HEIGHT))

    full_image = pygame.image.load("mapkitchen.png")
    mapkitchen = pygame.sprite.Sprite()
    mapkitchen.image = full_image.subsurface(pygame.Rect(174, 72, 180, 125)).copy()
    mapkitchen.y = 72
    mapkitchen.rect = mapkitchen.image.get_rect(topleft=(174,SCREEN_HEIGHT + mapkitchen.y))

    mapcockpit = pygame.sprite.Sprite()
    full_image = pygame.image.load("mapcockpit.png")
    mapcockpit.y = 102
    mapcockpit.image = full_image.subsurface(pygame.Rect(33, 102, 160, 500)).copy()
    mapcockpit.rect = mapcockpit.image.get_rect(topleft=(33,SCREEN_HEIGHT + mapcockpit.y))

    mapcargo = pygame.sprite.Sprite()
    full_image = pygame.image.load("mapcargo.png").convert_alpha()
    mapcargo.y = 67
    mapcargo.image = full_image.subsurface(pygame.Rect(943, 67, 310, 575)).copy()
    mapcargo.rect = mapcargo.image.get_rect(topleft=(943,SCREEN_HEIGHT + mapcargo.y))

    mapbathroom = pygame.sprite.Sprite()
    full_image = pygame.image.load("mapbathroom.png").convert_alpha()
    mapbathroom.y = 467
    mapbathroom.image = full_image.subsurface(pygame.Rect(168, 467, 190, 180)).copy()
    mapbathroom.rect = mapbathroom.image.get_rect(topleft=(168,SCREEN_HEIGHT + mapbathroom.y))

    mapcabin = pygame.sprite.Sprite()
    full_image = pygame.image.load("mapcabin.png").convert_alpha()
    mapcabin.y = 70
    mapcabin.image = full_image.subsurface(pygame.Rect(353, 70, 655, 571)).copy()
    mapcabin.rect = mapcabin.image.get_rect(topleft=(353,SCREEN_HEIGHT + mapcabin.y))

    map = [mapBG, mapcockpit, mapkitchen, mapcargo, mapbathroom, mapcabin]
    return map

def map_update(mouse_pos):
    if map[1].rect.collidepoint(mouse_pos):
        location = "cockpit"
    elif map[2].rect.collidepoint(mouse_pos):
        location = "kitchen"
    elif map[3].rect.collidepoint(mouse_pos):
        location = "cargo"
    elif map[4].rect.collidepoint(mouse_pos):
        location = "bathroom"
    elif map[5].rect.collidepoint(mouse_pos):
        location = "cabin"
    return location

def animate_map(map_direction):
    done = True
    for sprite in map:
        sprite.rect.y += 20 * map_direction  # move up or down
        if map_direction == -1:  # going up
            if sprite.rect.y > sprite.y:
                done = False
            else:
                sprite.rect.y = sprite.y
        elif map_direction == 1:  # going down
                if sprite.rect.y < SCREEN_HEIGHT + sprite.y:
                    done = False
                else:
                    sprite.rect.y = SCREEN_HEIGHT + sprite.y
    return done

def cockpit_init():
    return

def cockpit(objects, found_objects):
    cockpit_objects = objects["cockpit"]
    found_cockpit_objects = found_objects["cockpit"]
    print("You're at cockpit")
    return

def bathroom():
    print("You're at bathroom")
    return

def kitchen():
    print("You're at kitchen")
    return

def cabin():
    return

def cargo():
    print("You're at cargo")
    return


map_animating = False
map_direction = -1
bg = pygame.image.load("bg.png")
running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
map = create_map()
all_sprites = pygame.sprite.Group()
for sprite in map:
    all_sprites.add(sprite)
frame = 0
location = "cabin"
cockpit_objects = cockpit_init()
objects = {"cockpit":[],"cabin":[],"bathroom":[],"cargo":[],"kitchen":[]}

while running:
    frame += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_RETURN:
                if not map_animating:
                    # toggle direction
                    map_direction *= -1
                    map_animating = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if map[0].rect.y == 0:
                location = map_update(mouse_pos)

    pressed_keys = pygame.key.get_pressed()
    if map_animating:
        done = animate_map(map_direction)
        if done:
            map_animating = False
    screen.blit(bg, (0, 0))
    if location == "cabin":
        location = cabin()
        all_sprites.draw(screen)
    elif location == "kitchen":
        location = kitchen()
        all_sprites.draw(screen)
    elif location == "bathroom":
        location = bathroom()
        all_sprites.draw(screen)
    elif location == "cockpit":
        location = cockpit({"cockpit":[]}, {"cockpit":[]})
        all_sprites.draw(screen)
    elif location == "cargo":
        location = cargo()
        all_sprites.draw(screen)
    else:
        all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)