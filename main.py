import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# -------------------
# Map
# -------------------
def create_map():
    mapBG = pygame.sprite.Sprite()
    mapBG.y = 0
    mapBG.image = pygame.image.load("mapbg.png")
    mapBG.rect = mapBG.image.get_rect(topleft=(0, SCREEN_HEIGHT))

    full_image = pygame.image.load("mapkitchen.png")
    mapkitchen = pygame.sprite.Sprite()
    mapkitchen.image = full_image.subsurface(pygame.Rect(174, 72, 180, 125)).copy()
    mapkitchen.y = 72
    mapkitchen.rect = mapkitchen.image.get_rect(topleft=(174, SCREEN_HEIGHT + mapkitchen.y))

    mapcockpit = pygame.sprite.Sprite()
    full_image = pygame.image.load("mapcockpit.png")
    mapcockpit.y = 102
    mapcockpit.image = full_image.subsurface(pygame.Rect(33, 102, 160, 500)).copy()
    mapcockpit.rect = mapcockpit.image.get_rect(topleft=(33, SCREEN_HEIGHT + mapcockpit.y))

    mapcargo = pygame.sprite.Sprite()
    full_image = pygame.image.load("mapcargo.png").convert_alpha()
    mapcargo.y = 67
    mapcargo.image = full_image.subsurface(pygame.Rect(943, 67, 310, 575)).copy()
    mapcargo.rect = mapcargo.image.get_rect(topleft=(943, SCREEN_HEIGHT + mapcargo.y))

    mapbathroom = pygame.sprite.Sprite()
    full_image = pygame.image.load("mapbathroom.png").convert_alpha()
    mapbathroom.y = 467
    mapbathroom.image = full_image.subsurface(pygame.Rect(168, 467, 190, 180)).copy()
    mapbathroom.rect = mapbathroom.image.get_rect(topleft=(168, SCREEN_HEIGHT + mapbathroom.y))

    mapcabin = pygame.sprite.Sprite()
    full_image = pygame.image.load("mapcabin.png").convert_alpha()
    mapcabin.y = 70
    mapcabin.image = full_image.subsurface(pygame.Rect(353, 70, 655, 571)).copy()
    mapcabin.rect = mapcabin.image.get_rect(topleft=(353, SCREEN_HEIGHT + mapcabin.y))

    map = [mapBG, mapcockpit, mapkitchen, mapcargo, mapbathroom, mapcabin]
    return map


def map_update(mouse_pos, map):
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
    else:
        location = None
    return location


def animate_map(map_direction, map):
    done = True
    for sprite in map:
        sprite.rect.y += 20 * map_direction
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


# -------------------
# Objects
# -------------------
def cockpit_init():
    cockpit_objects = []

    # Headphones object
    image = pygame.image.load("headphones.png").convert_alpha()
    rect = image.get_rect(topleft=(160,600))
    obj = {
        "name": "headphones",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 12,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cockpit_objects.append(obj)

    # Coat object
    image = pygame.image.load("coat.png").convert_alpha()
    rect = image.get_rect(topleft=(1150, 300))
    obj = {
        "name": "coat",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 9,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cockpit_objects.append(obj)

    image = pygame.image.load("toolbox.png").convert_alpha()
    rect = image.get_rect(topleft=(900,500))
    obj = {
        "name": "toolbox",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 36,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cockpit_objects.append(obj)

    image = pygame.image.load("trash.png").convert_alpha()
    rect = image.get_rect(topleft=(450,585))
    obj = {
        "name": "trash",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 3,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cockpit_objects.append(obj)

    image = pygame.image.load("dumbbell.png").convert_alpha()
    rect = image.get_rect(topleft=(750,600))
    obj = {
        "name": "dumbbell",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 30,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cockpit_objects.append(obj)

    return cockpit_objects

def kitchen_init():
    kitchen_objects = []

    image = pygame.image.load("fridge.png").convert_alpha()
    rect = image.get_rect(topleft=(200,145))
    obj = {
        "name": "fridge",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 98,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    kitchen_objects.append(obj)

    image = pygame.image.load("cabinet.png").convert_alpha()
    rect = image.get_rect(topleft=(480, 365))
    obj = {
        "name": "cabinet",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 45,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    kitchen_objects.append(obj)

    image = pygame.image.load("HM.png").convert_alpha()
    rect = image.get_rect(topleft=(1120, 450))
    obj = {
        "name": "happy meal",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 4,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    kitchen_objects.append(obj)

    return kitchen_objects

def cabin_init():
    cabin_objects = []

    image = pygame.image.load("computer.png").convert_alpha()
    rect = image.get_rect(topleft=(1090,570))
    obj = {
        "name": "computer",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 23,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cabin_objects.append(obj)

    image = pygame.image.load("charger.png").convert_alpha()
    rect = image.get_rect(topleft=(520, 515))
    obj = {
        "name": "charger",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 5,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cabin_objects.append(obj)

    image = pygame.image.load("scarf.png").convert_alpha()
    rect = image.get_rect(topleft=(250, 510))
    obj = {
        "name": "scarf",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 4,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cabin_objects.append(obj)

    image = pygame.image.load("headband.png").convert_alpha()
    rect = image.get_rect(topleft=(690,600))
    obj = {
        "name": "headband",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 3,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cabin_objects.append(obj)

    image = pygame.image.load("blahaj.png").convert_alpha()
    rect = image.get_rect(topleft=(400,580))
    obj = {
        "name": "blahaj",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 14,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cabin_objects.append(obj)

    return cabin_objects

def cargo_init():
    cargo_objects = []

    image = pygame.image.load("suitcases.png").convert_alpha()
    rect = image.get_rect(topleft=(420, 267))
    obj = {
        "name": "suitcases",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 89,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cargo_objects.append(obj)

    image = pygame.image.load("luggage.png").convert_alpha()
    rect = image.get_rect(topleft=(80, 180))
    obj = {
        "name": "luggage",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 59,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cargo_objects.append(obj)

    image = pygame.image.load("boxes.png").convert_alpha()
    rect = image.get_rect(topleft=(680,385))
    obj = {
        "name": "boxes",
        "images": [image, pygame.Surface((rect.width, rect.height))],
        "rect": rect,
        "weight": 67,
        "clicked": False,
        "state": 1
    }
    obj["images"][1].fill((255, 0, 255))
    cargo_objects.append(obj)

    return cargo_objects

def draw_ui(obj, screen, font):
    # Draw blue box in center
    box_rect = pygame.Rect(0, 0, 300, 200)
    box_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.draw.rect(screen, (0, 0, 255), box_rect)

    # Draw weight
    text_surf = font.render(f"Object: {obj['name']}", True, (255, 255, 255))
    text_rect = text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
    screen.blit(text_surf, text_rect)

    text2_surf = font.render(f"Weight: {obj['weight']}", True, (255, 255, 255))
    text2_rect = text2_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 10))
    screen.blit(text2_surf, text2_rect)

    # Draw buttons
    eject_button = pygame.Rect(SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 40, 90, 40)
    keep_button = pygame.Rect(SCREEN_WIDTH // 2 + 30, SCREEN_HEIGHT // 2 + 40, 90, 40)

    pygame.draw.rect(screen, (200, 0, 0), eject_button)
    pygame.draw.rect(screen, (0, 200, 0), keep_button)

    screen.blit(font.render("Eject", True, (255, 255, 255)),
                font.render("Eject", True, (255, 255, 255)).get_rect(center=eject_button.center))
    screen.blit(font.render("Keep", True, (255, 255, 255)),
                font.render("Keep", True, (255, 255, 255)).get_rect(center=keep_button.center))

    return eject_button, keep_button


def handle_click(obj, mouse_pos):
    if obj["rect"].collidepoint(mouse_pos):
        obj["clicked"] = True
        return True
    return False


def cutscene(num):
    font = pygame.font.SysFont("Arial", 32)
    text_color = (255, 255, 255)

    cutText = [
        [
        "Hack Club's new plane, Daydream, is finally off the ground!",
        "Fitted with not-quite-state-of-the-art equipment, a hundred teenagers, and a whole lot of caffeine, this new plane is certain to be revolutionary.",
        "And yet, you, dearest hacker, have the worst luck known to mankind.",
        "Because not long after takeoff, the plane is running out of power!",
        "If you don't throw enough weight off, you're screwed to hell and back.",
        "Better start looking around! Tap on an object to see the weight, and press enter to activate the map."
        ],
        [
        "50 -- that's a lot of weight to throw out.",
        "But you made it! Amazing job, you. Finally, you can sit back and relax...",
        "Wait. Why did the alarms start again?",
        "...",
        "...",
        "...You cannot be serious. Another power line has crashed?!",
        "Good luck. You might need it."
        ],
        ["Cool, cool. There goes another set of precious items. The plane is gonna be bare at this rate.",
         "But hey, there we go! The plane's flying steadily again!",
         "You settle back into your seat, satisfied.",
         "And then, the plane dips again. Lights flicker overhead.",
         "Standing up, you despair at another announcement. The power has failed again?!",
         "This must be human intervention. Once, twice, okay, maybe the plane's just bad.",
         "But this many times? This was clearly planned -- and you're going to make them pay.",
         "...But before that, you need to stop the plane from crashing into Toronto."],
        ["Oh. My god.",
         "It says something that you're not even surprised this time when the alarms only pause for a short moment.",
         "There must be a saboteur on the plane.",
         "But who in the world would?",
         "Well, you gotta find out. But before you can...",
         "Time to toss out every remaining thing to buy time!",
         "Fight on, soldier.",
         "We definitely didn't bring popcorn."],
         ["There's just no way.",
          "You've thrown out everything. Every single removable item.",
          "It's still not enough. The plane is still falling.",
          "What else is there?",
          "...Or, maybe you're asking the wrong question.",
          "The objects weren't the only source of weight.",
          "The right question is... Who else is there?",
          "You know there is a saboteur. The sabotage must be in the electrical rooms.",
          "But the only ones with access are the co-pilot and pilot!",
          "Kashyap or Erin. It has to be one of them. Or both of them.",
          "Make your choice -- quickly!"]
    ]

    def render_wrapped_text(text, font, color, max_width):
        words = text.split(" ")
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        if current_line:
            lines.append(current_line.strip())

        rendered = []
        for line in lines:
            surf = font.render(line, True, color)
            rendered.append(surf.convert_alpha())  # allow alpha fading
        return rendered

    current_index = 0
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == K_RETURN:
                    if current_index < len(cutText[num]) - 1:
                        # fade out current text
                        for alpha in range(255, -1, -15):
                            screen.fill((0, 0, 0))
                            wrapped_lines = render_wrapped_text(
                                cutText[num][current_index], font, text_color, SCREEN_WIDTH - 100
                            )
                            y = SCREEN_HEIGHT // 2 - (len(wrapped_lines) * font.get_linesize()) // 2
                            for line_surface in wrapped_lines:
                                fade_surface = line_surface.copy()
                                fade_surface.set_alpha(alpha)
                                rect = fade_surface.get_rect(centerx=SCREEN_WIDTH // 2, y=y)
                                screen.blit(fade_surface, rect)
                                y += font.get_linesize() + 5
                            pygame.display.flip()
                            clock.tick(30)

                        current_index += 1
                    else:
                        # last line → exit cutscene
                        running = False

        # draw current text
        screen.fill((0, 0, 0))
        wrapped_lines = render_wrapped_text(cutText[num][current_index], font, text_color, SCREEN_WIDTH - 100)
        y = SCREEN_HEIGHT // 2 - (len(wrapped_lines) * font.get_linesize()) // 2
        for line_surface in wrapped_lines:
            rect = line_surface.get_rect(centerx=SCREEN_WIDTH // 2, y=y)
            screen.blit(line_surface, rect)
            y += font.get_linesize() + 5

        pygame.display.flip()
        clock.tick(60)


        # draw current text (normal)
        screen.fill((0, 0, 0))
        wrapped_lines = render_wrapped_text(cutText[num][current_index], font, text_color, SCREEN_WIDTH - 100)
        y = SCREEN_HEIGHT // 2 - (len(wrapped_lines) * font.get_linesize()) // 2
        for line_surface in wrapped_lines:
            rect = line_surface.get_rect(centerx=SCREEN_WIDTH // 2, y=y)
            screen.blit(line_surface, rect)
            y += font.get_linesize() + 5

        pygame.display.flip()
        clock.tick(60)

def finalChoice(screen, font):
    choosing = True
    ending_text = None

    # Define buttons
    button1 = pygame.Rect(SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT - 200, 150, 60)
    button2 = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT - 200, 150, 60)
    button3 = pygame.Rect(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT - 200, 150, 60)

    while choosing:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    cutscene(5)
                    choosing = False
                elif button2.collidepoint(event.pos):
                    cutscene(6)
                    choosing = False
                elif button3.collidepoint(event.pos):
                    cutscene(7)
                    choosing = False

        # Draw cockpit background
        bg = pygame.image.load("cockpit.png").convert()
        screen.blit(bg, (0, 0))

        # Draw buttons
        pygame.draw.rect(screen, (100, 100, 200), button1)
        pygame.draw.rect(screen, (100, 100, 200), button2)
        pygame.draw.rect(screen, (100, 100, 200), button3)

        screen.blit(font.render("Kashyap", True, (255, 255, 255)),
                    font.render("Kashyap", True, (255, 255, 255)).get_rect(center=button1.center))
        screen.blit(font.render("Both", True, (255, 255, 255)),
                    font.render("Both", True, (255, 255, 255)).get_rect(center=button2.center))
        screen.blit(font.render("Erin", True, (255, 255, 255)),
                    font.render("Erin", True, (255, 255, 255)).get_rect(center=button3.center))
        heading_surf = font.render("Who will you eject?", True, (255, 0, 0))
        heading_rect = heading_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 90))
        screen.blit(heading_surf, heading_rect)
        pygame.display.flip()

# -------------------
# Main loop
# -------------------
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Game Example")

font = pygame.font.SysFont("Arial", 32)
clock = pygame.time.Clock()
running = True

bg = pygame.image.load("bg.png").convert()
map = create_map()
all_sprites = pygame.sprite.Group(map)

map_animating = False
map_direction = 1
frame = 0
location = "cargo"

cockpit_objects = cockpit_init()
kitchen_objects = kitchen_init()
cabin_objects = cabin_init()
cargo_objects = cargo_init()
objects = {"cockpit": cockpit_objects, "cabin": cabin_objects, "bathroom": [], "cargo": cargo_objects, "kitchen": kitchen_objects}

active_object = None
object_thrown_this_level = False
weight = 500
weightLimit = 450
level = 0
cutscene(level)


while running:
    if level == 4:
        finalChoice(screen, font)
    frame += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RETURN and not map_animating:
                map_direction *= -1
                map_animating = True
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # --- Map is showing ---
            if map[0].rect.y < SCREEN_HEIGHT:  
                new_loc = map_update(mouse_pos, map)
                if new_loc:
                    location = new_loc
                    # auto close map
                    map_direction = 1
                    map_animating = True
            # --- Objects only clickable if map is hidden ---
            elif active_object is None:
                for obj in objects[location]:
                    if handle_click(obj, mouse_pos):
                        active_object = obj
                        break
            else:
                eject_button, keep_button = draw_ui(active_object, screen, font)
                if eject_button.collidepoint(mouse_pos):
                    active_object["state"] = 0
                    weight -= active_object["weight"]
                    active_object["clicked"] = False
                    objects[location].remove(active_object)
                    active_object = None
                    object_thrown_this_level = True
                elif keep_button.collidepoint(mouse_pos):
                    active_object["clicked"] = False
                    active_object = None

    if map_animating:
        if animate_map(map_direction, map):
            map_animating = False

    # --- draw --

    if location == "cockpit":
        bg = pygame.image.load("cockpit.png").convert()
    elif location == "kitchen":
        bg = pygame.image.load("kitchen.png").convert()
    elif location == "cabin":
        bg = pygame.image.load("cabin.png").convert()
    elif location == "cargo":
        bg = pygame.image.load("cargo.png").convert()
    
    screen.blit(bg, (0, 0))

    all_sprites.draw(screen)

    # Only draw objects if map is fully hidden
    if map[0].rect.y >= SCREEN_HEIGHT:
        for obj in objects[location]:
            if not obj["clicked"] and obj["state"] == 1:
                screen.blit(obj["images"][0], obj["rect"].topleft)

    if active_object and active_object["clicked"]:
        draw_ui(active_object, screen, font)

    if weight <= weightLimit and object_thrown_this_level:
        level += 1
        weightLimit -= 50
        cutscene(level)
        object_thrown_this_level = False


    text_surface = font.render("Weight: " + str(weight), True, (255, 0, 0))
    screen.blit(text_surface, (10, 0))
    text_surface = font.render("Current weight limit: " + str(weightLimit), True, (21, 200, 21))
    screen.blit(text_surface, (10, 40))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
