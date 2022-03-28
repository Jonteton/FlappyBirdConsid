import pygame
import random
from bird import Bird
from pillar import Pillar

pygame.init()

BIRD_IMG = "./assets/frame-11.png"
BACKGROUND_IMG = "./assets/background.png"

running = True


def main():

    bird_start_x = 200
    bird_start_y = 450

    floor_y = 595
    pillar_start_x = bird_start_x + 250
    pillar_start_y = 0
    pillar_width = 50
    pillar_height = 75
    pillar_velocity_x = 0.4

    pillar_gap_x = 250
    pillar_gap_y = 100

    bird_img_loaded, background_img_loaded = load_resources()
    screen_width = background_img_loaded.get_width() * 2

    bg_flipped = pygame.transform.flip(
        background_img_loaded, True, False)
    screen = pygame.display.set_mode(
        [screen_width, background_img_loaded.get_height()])

    bird = Bird(bird_start_x, bird_start_y, bird_img_loaded)

    pillar = Pillar(pillar_start_x, pillar_start_y,
                    pillar_width, pillar_height, pillar_velocity_x)

    all_pillars = [pillar]

    while running:
        if bird.y <= floor_y:
            for event in pygame.event.get():
                event_handler(event, bird)

            last_pillar = all_pillars[-1]

            if last_pillar.x < screen_width:
                pillar_height = random.randint(100, 500)
                new_pillar = Pillar(last_pillar.x + pillar_gap_x, pillar_start_y,
                                    pillar_width, pillar_height, pillar_velocity_x)

                all_pillars.append(new_pillar)

            bird.falling()
            for pillar in all_pillars:
                pillar.update_position()

        render(screen, background_img_loaded, bg_flipped,
               all_pillars, bird, pillar_gap_y, floor_y)

        pygame.display.update()


def load_resources():
    bird_img_loaded = pygame.image.load(BIRD_IMG)
    background_img_loaded = pygame.image.load(BACKGROUND_IMG)

    return bird_img_loaded, background_img_loaded


def event_handler(event, bird):
    global running
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            bird.up()


def render(screen, background_img_loaded, bg_flipped, all_pillars, bird, pillar_gap_y, floor_y):

    screen.blit(background_img_loaded, (0, 0))
    screen.blit(bg_flipped,
                (background_img_loaded.get_width(), 0))

    for pillar in all_pillars:
        pillar.render(screen, pillar_gap_y, floor_y)

    bird.render(screen)


if __name__ == "__main__":
    main()
