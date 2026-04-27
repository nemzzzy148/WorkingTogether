import pygame
from scripts import config, render_loop, background, level_loader

# configurations


# pygame setup

pygame.init()

screen = pygame.display.set_mode((config.W, config.H))

pygame.display.set_caption(config.TITLE)

# runtime var

running = True

currentLevel = "level"

level_loader.LoadLevel(currentLevel)

background.CreateBackground(0)

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    # render everything
    render_loop.Loop(screen)




pygame.quit()