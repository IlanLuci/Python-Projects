#General
DISPLAYSIZEX = 400
DISPLAYSIZEY = 500
MATRIXLENGTH = 4
MATRIXPADDINGX = 40
MATRIXPADDINGY = 140

#Colors
WHITE = (255, 255, 255)
GREEN = (50, 168, 82)
RED = (204, 59, 78)
BLUE = (76, 114, 173)
BLACK = (0, 0, 0)

COLORS = {0: BLACK, 2: GREEN, 4: RED, 8: BLUE, 16: BLUE, 32: BLUE, 64: BLUE, 128: BLUE, 256: BLUE, 512: BLUE, 1024: BLUE, 2048: BLUE}

def getcolor(blocknum):
    return COLORS[blocknum]
