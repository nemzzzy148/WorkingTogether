import pygame
from pathlib import Path
from scripts import config

# store texture name

textureDict = {1: "1_light_sky_1",
               2: "2_light_background_1",
               3: "3_light_background_2",
               4: "4_light_background_3",
               5: "5_light_background_4",
               6: "6_light_sky_2"}

# on runtime load

loadedTextures: dict[int, pygame.Surface] = {}

# base images folder path setup (for dumb people: gets absolute path of current file and then goes to base with parent x2)

Base_path = Path(__file__).resolve().parent.parent

Images_folder = Base_path / config.IMAGE_FOLDER

def GetTexture(index: int):
    if index in loadedTextures:
        return loadedTextures.get(index)
    
    texture = pygame.image.load(GetPathFromIndex(index))
    texture = pygame.transform.scale(texture, (config.TILE_SIZE, config.TILE_SIZE))
    loadedTextures[index] = texture
    return texture

def GetPathFromIndex(index: int):
    return Images_folder / (textureDict.get(index) + config.IMG_EXTENSION)