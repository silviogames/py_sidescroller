# file to handle gamemap stuff
import pygame
import color
import utils
import entity    
from random import randint

class tile:
    def __init__(self,color,collision, tile_id):
        self.color = color
        self.collision = collision
        self.tile_id = tile_id

tile_air = tile(color.black, False, 0)
tile_grass = tile(color.green, True, 1)
tile_dirt = tile(color.brown, True, 2)
tile_lava= tile(color.red,False , 3)
list_tiles = []

list_tiles.append(tile_air)
list_tiles.append(tile_dirt)
list_tiles.append(tile_grass)
list_tiles.append(tile_lava)

#fast lookup table for collision
tile_collision = []
for tile in list_tiles:
    tile_collision.append(tile.collision)


def get_color(index):
    # get color from tiles or default if out of range
    if index < 0 or index > len(list_tiles):
        return color.black
    else:
        return list_tiles[index].color

class world:
    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.content = utils.create_array(width, height)
        self.entities = []

    def generate(self):
        #(re)generate content of this map
        for x in range(self.width):
            for y in range(self.height):
                self.content[x][y] = utils.random_range((0,15),(1,3),(2,1),(3,1)) 

    def add_entity(self, new_entity):
        if isinstance(new_entity, entity.entity):
            self.entities.append(new_entity)
        else:
            print('this is not an entity')
            print(type(entity))

    def render(self, surf):
        #TODO add offset later
        for x in range(len(self.content)):
             for y in range(len(self.content[0])):
                 pygame.draw.rect(surf, get_color(self.content[x][y]),(x * self.tile_size, y * self.tile_size,self.tile_size - 1 ,self.tile_size - 1))
        #render entities
        for e in self.entities:
            e.render(surf)

    def collision(self,x,y):
        #returns true if collision 
        tilex = int( x / self.tile_size)
        tiley =int( y / self.tile_size)
        if tilex < 0 or tilex >= self.width or tiley < 0 or tiley >= self.height:
            return False
        else:
            return tile_collision[self.content[tilex][tiley]]

    def get_tile(self,tilex,tiley):
        if tilex < 0 or tilex >= self.width or tiley < 0 or tiley >= self.height:
            return None
        else:
            return self.content[tilex][tiley]

    def update(self,dt):
         for e in self.entities:
             e.update(dt)
             
    # remove objects after all objects updated
         for e in self.entities:
             if e.dead == True:
                 self.entities.remove(e)
