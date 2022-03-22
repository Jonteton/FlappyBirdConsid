import pygame
from bird import Bird

pygame.init()

BIRD_IMG = "./assets/frame-11.png"
BACKGROUND_IMG = "./assets/background.png"

running = True


def main():

    bird_start_x = 200
    bird_start_y = 450

    death_y = 595

    bird_img_loaded, background_img_loaded = load_resources()
    bg_flipped = pygame.transform.flip(
        background_img_loaded, True, False)

    screen = pygame.display.set_mode(
        [background_img_loaded.get_width() * 2, background_img_loaded.get_height()])

    bird = Bird(bird_start_x, bird_start_y, bird_img_loaded)

    while running:
        if bird.y <= death_y:
            for event in pygame.event.get():
                event_handler(event, bird)

            bird.falling()

        render(screen, background_img_loaded, bg_flipped)
        bird.render(screen)
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


def render(screen, background_img_loaded, bg_flipped):
    screen.blit(background_img_loaded, (0, 0))
    screen.blit(bg_flipped,
                (background_img_loaded.get_width(), 0))


if __name__ == "__main__":
    main()
