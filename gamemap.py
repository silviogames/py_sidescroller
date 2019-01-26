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

tile_grass = tile(color.green, True, 0)
tile_dirt = tile(color.brown, True, 1)
tile_lava= tile(color.red,False , 2)
list_tiles = []
list_tiles.append(tile_dirt)
list_tiles.append(tile_grass)
list_tiles.append(tile_lava)

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
                self.content[x][y] = randint(0,2)

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
    
    def update(self,dt):
         for e in self.entities:
             e.update(dt)
             
    # remove objects after all objects updated
         for e in self.entities:
             if e.dead == True:
                 self.entites.remove(e)
