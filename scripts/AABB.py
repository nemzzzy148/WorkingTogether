class Box:
    def __init__(self, pos, textureIndex: int):
        self.pos = pos
        self.textureIndex = textureIndex

    textureIndex: int = 0
    pos = (0,0)

def AABB(object: Box, rest: Box):
    return "okay"

def XYTtoBox(data: dict[str, int]):
    return Box((data.get("x"), data.get("y")), data.get("t"))