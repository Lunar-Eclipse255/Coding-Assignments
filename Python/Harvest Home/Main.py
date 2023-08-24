import pygame
from Attributes import *
from Player import *
from Sprite_Work import *
from pytmx.util_pygame import load_pygame
from Plants import *
value=16
h =643
w=648

pygame.init()
screen = pygame.display.set_mode((w,h))
BG=pygame.image.load("Python/Harvest Home/Sprites/Map.png")
screen.fill([50,50,50])
pygame.display.set_caption('Harvest Home')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player((20,20),all_sprites)	
def Main():
	display_surface = pygame.display.get_surface()
	check=False
	plants=pygame.sprite.Group()
	run=True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
		time = clock.tick() / 1000
		#screen.blit(BG,(0,0))

		all_sprites.draw(display_surface)
		all_sprites.update(time)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_p]:
			check=True
		if check:
			plants.draw(display_surface)
		pygame.display.flip()
		
Main()