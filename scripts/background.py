import pygame
import sys
from scripts import textures
from scripts import config
from scripts.config import W,H

surface = None

types = [
    [config.BACKGROUND_LAYER_Y, 1,2,3,4,5,6]
]



# optimized -> render background once to surface and re-use

def CreateBackground(typeIndex:int):
    global surface

    surface = pygame.Surface((W,H))

    AmountTilesX: int = W // config.TILE_SIZE
    AmountTilesY: int = H // config.TILE_SIZE

    type = types[typeIndex]

    for y in range(AmountTilesY):
        if y < type[0]:
            for x in range(AmountTilesX):
                surface.blit(textures.GetTexture(type[1]),(x * config.TILE_SIZE,y * config.TILE_SIZE))
        
        elif y == type[0]:
            for x in range(AmountTilesX):
                surface.blit(textures.GetTexture( type[ 2+(x%config.BACKGROUND_LAYER_PART) ] ),(x * config.TILE_SIZE,y * config.TILE_SIZE))
        
        else:
            for x in range(AmountTilesX):
                surface.blit(textures.GetTexture(type[6]),(x * config.TILE_SIZE,y * config.TILE_SIZE))
    print("Background created")

def RenderBackground(screen: pygame.Surface):
    if surface == None:
        print("Error: no background surface created!", file=sys.stderr)
        return
    screen.blit(surface,(0,0))