# configurations file

W, H = 864,648

# aspect ratio = 4/3

TILE_SIZE: int = 18 * 3

# the amount of different tiles that can be spawned in the set layer y cord 26

BACKGROUND_LAYER_Y: int = (H // 2) // TILE_SIZE

BACKGROUND_LAYER_PART: int = 4

# 48 tiles x-axis, 36 tiles y-axis

TITLE = "WorkingTogether"

# tile config

IMAGE_FOLDER = "images/"

IMG_EXTENSION = ".png"

# level config

LEVEL_FOLDER = "levels"

LVL_EXTENSION = ".json"