import pygame
from Attributes import *
from Sprite_Work import *
class Plant (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self) 
        self.display_surface=pygame.display.get_surface()
        self.image = blueBerryOne
        self.rect=blueBerryOne.get_rect(midbottom=(x,y))
        self.display_surface.blit(self.image,self.rect)
        pygame.display.flip()
        