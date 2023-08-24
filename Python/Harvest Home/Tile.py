import pygame
from Attributes import *
from Game import*
def new(self):
    for tile_object in self.map.tmxdata.objects:

        tile_object.x *= int(value / self.map.tilesize)
        tile_object.y *= int(value / self.map.tilesize)

        obj_center = (tile_object.x + tile_object.width / 2,
                         tile_object.y + tile_object.height / 2)

    
        tile_object.width *= int(value / self.map.tilesize)
        tile_object.height *= int(value / self.map.tilesize)

        # if tile_object.name == 'zombie':
        #     Mob(self, tile_object.x, tile_object.y)



    self.camera = Camera(self.map.width, self.map.height)
    self.paused = False
    self.draw_debug = False
