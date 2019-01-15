# file to handle gamemap stuff


color_black = (0,0,0)
color_white = (255, 255, 255)
color_red = (220,20,60)
color_brown = (205,133,63)
color_green = (0,128,0)

    
class tile:
    def __init__(self,color,collision, tile_id):
        self.color = color
        self.collision = collision
        self.tile_id = tile_id

tile_grass = tile(color_green, True, 0)
tile_dirt = tile(color_brown, True, 1)
tile_lava= tile(color_red,False , 2)
list_tiles = []
list_tiles.append(tile_dirt)
list_tiles.append(tile_grass)
list_tiles.append(tile_lava)

def get_color(index):
    # get color from tiles or default if out of range
    if index < 0 or index > len(list_tiles):
        return color_black
    else:
        return list_tiles[index].color
