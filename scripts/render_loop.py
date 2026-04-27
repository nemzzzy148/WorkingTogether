import pygame
from scripts import background

def Loop(screen: pygame.Surface):
    # blit background onto screen

    # doc useful: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    
    background.RenderBackground(screen)

    
    pygame.display.flip()