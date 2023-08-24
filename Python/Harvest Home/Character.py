import pygame
from Attributes import *

h =847
w=1440
class Sprite():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, startX, startY, width, height, color,scale):
        image=pygame.Surface((width,height)).convert_alpha()
        #image.fill('green')
        image.blit(self.sheet, (0,0),(startX,startY, width, height)) 
        image=pygame.transform.scale(image,(width*scale, height*scale))
        image.set_colorkey(color)
        
        return image    



