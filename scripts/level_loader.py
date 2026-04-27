# helper to load levels

from scripts import AABB
from pathlib import Path
from scripts import config
import json
import pygame
from scripts import textures

level = None

class Level:
    def __init__(self, data: dict):
        # not collection tyepes
        self.name = data.get("name")
        self.level_type = data.get("level_type")

        # collection types basic
        p1 = data.get("player_1")
        p2 = data.get("player_2")

        self.P1_pos = AABB.XYTtoBox(p1)

        self.P2_pos = AABB.XYTtoBox(p2)



        # collection types triple nested

        tile_data = data.get("tiles")
        for t in tile_data:
            self.tiles.append(AABB.XYTtoBox(t))
        pass

    surface: pygame.Surface

    name: str = "noname"
    level_type: int = 0

    P1_pos: AABB.Box
    P2_pos: AABB.Box

    # defined by func
    tiles: list[AABB.Box] = []


def GetAllLevelNames():
    return ["hii", "look"]

Base_path = Path(__file__).resolve().parent.parent

def LoadLevel(name: str):
    global level

    level_path = Base_path / config.LEVEL_FOLDER / (name + config.LVL_EXTENSION)

    # https://www.w3schools.com/python/python_json.asp How to read json file in python

    # json syntax: https://www.w3schools.com/whatis/whatis_json.asp

    # with is uesd in place of try catch, load a file and parse it to a dict

    with open(level_path, "r") as l:
        data = json.load(l)

    level = Level(data)

    print("JSON:" , data)
    print("Level loaded:" , level)

def CreateLevelSurface(level: Level, screen: pygame.Surface):
    surface = pygame.Surface((config.W,config.H))

    for t in level.tiles:
        texture = textures.GetTexture(t.textureIndex)
        pygame.Surface.blit(surface, texture, (t.pos[0]*config.TILE_SIZE,
                                                t.pos[1]*config.TILE_SIZE))
    
    level.surface = surface

    print("Created level surface!")

def RenderLevel(screen: pygame.Surface):
    screen.blit(screen, level.surface, (0,0))