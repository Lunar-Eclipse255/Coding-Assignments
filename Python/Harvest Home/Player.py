import pygame
from Attributes import *
from Sprite_Work import *
from Time import *
from Plants import Plant

h =643
w=648


class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)
		self.animation()
		self.status='down'
		
		#issues, up,
		self.frame_index=0
		self.display_surface = pygame.display.get_surface()
		self.image = self.animations[self.status][self.frame_index]
		# general setup
		#self.image = self.animation[self.status][self.frame_index]
		self.rect = self.image.get_rect(center = pos)
		# movement attributes
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(self.rect.center)
		self.speed = 200

		self.hitbox=self.rect.copy().inflate((0,0))

		self.timers={
			'toolUsed':time(350, self.toolUse),
			'plantUsed':time(350, self.plantUse),
			'treeUsed':time(350, self.treeUse),
			'plantSwitch':time(200),
			'treeSwitch':time(200)
		}
		
		self.plantSeeds=['taroRoot','coffeeBeanSeeds','cranberrySeeds','blueberrySeeds','wheatSeeds']
		self.treeSeeds=['cherrySapling','appleSapling','orangeSapling','pomegranateSapling']
		self.plantSeedIndex=0
		self.treeSeedIndex=0
		self.plantSeedSelected=self.plantSeeds[self.plantSeedIndex]
		self.treeSeedSelected=self.treeSeeds[self.treeSeedIndex]

	def toolUse(self):
		pass
	
	def plantUse(self):
		pass

	def treeUse(self):
		pass
		
	def animation(self):
		self.animations = {'right': [playerRightOne,playerRightTwo,playerRightThree,playerRightFour],'left': [playerLeftOne,playerLeftTwo,playerLeftThree,playerLeftFour],'up': [playerUpOne, playerUpTwo,playerUpThree,playerUpFour],'down': [playerDownOne, playerDownTwo,playerDownThree,playerDownFour],
		                   'right_Idle':[playerRightIdle],'left_Idle':[playerLeftIdle],'up_Idle':[playerUpIdle],'down_Idle':[playerDownIdle],
	                       'right_Scythe':[playerRightScytheOne,playerRightScytheTwo],'left_Scythe':[playerLeftScytheOne,playerLeftScytheTwo],'up_Scythe':[playerUpScytheOne,playerUpScytheTwo],'down_Scythe':[playerDownScytheOne,playerDownScytheTwo],
	                       'right_Axe':[playerRightAxeOne,playerRightAxeTwo],'left_Axe':[playerLeftAxeOne,playerLeftAxeTwo],'up_Axe':[playerUpAxeOne,playerUpAxeTwo],'down_Axe':[playerDownAxeOne, playerDownAxeTwo]}
		
	def animate(self,time):
		self.frame_index += 4 * time
		if self.frame_index >= len(self.animations[self.status]):
			self.frame_index = 0

		self.image = self.animations[self.status][int(self.frame_index)]

	def Make(self):
		newplant=Plant(self.rect.x,self.rect.y,plants)
		plants.add(newplant)
	def input(self):
		keys = pygame.key.get_pressed()
		if not self.timers['toolUsed'].init:
			if keys[pygame.K_w]:
				self.direction.y = -1
				self.status = 'up'
			elif keys[pygame.K_s]:
				self.direction.y = 1
				self.status = 'down'

			else:
				self.direction.y = 0
			
			if keys[pygame.K_d]:
				self.direction.x = 1
				self.status = 'right'
			elif keys[pygame.K_a]:
				self.direction.x = -1
				self.status = 'left'
			else:
				self.direction.x = 0
				
			
			if keys[pygame.K_k]:
				self.tool='Scythe'
				self.timers['toolUsed'].Initialize()
				self.direction = pygame.math.Vector2()
				self.frame_index=0

			elif keys[pygame.K_l]:
				self.tool='Axe'
				self.timers['toolUsed'].Initialize()
				self.direction = pygame.math.Vector2()
				self.frame_index=0

			if keys[pygame.K_j]:
				self.timers['plantUsed'].Initialize()
				self.direction = pygame.math.Vector2()
				self.frame_index=0
				
			
			if keys[pygame.K_COMMA]and not self.timers['plantSwitch'].init:
				self.timers['plantSwitch'].Initialize()
				self.plantSeedIndex +=1
				self.plantSeedIndex=self.plantSeedIndex if self.plantSeedIndex<len(self.plantSeeds) else 0
				self.plantSeedSelected = self.plantSeeds[self.plantSeedIndex]



			if keys[pygame.K_h]:
				self.timers['treeUsed'].Initialize()
				self.direction = pygame.math.Vector2()
				self.frame_index=0
				
			
			if keys[pygame.K_PERIOD] and not self.timers['treeSwitch'].init:
				self.timers['treeSwitch'].Initialize()
				self.treeSeedIndex +=1
				self.treeSeedIndex=self.treeSeedIndex if self.treeSeedIndex<len(self.treeSeeds) else 0
				self.treeSeedSelected = self.treeSeeds[self.treeSeedIndex]
			if keys[pygame.K_p]:
				newPlant=Plant(self.rect.x,self.rect.y)
				plants.add(newPlant)
				#screen.blit(blueBerryThree,(200,200))
				pygame.display.flip()

				
				
	def get_status(self):
		
		# idle
		if self.direction.magnitude() == 0:
			self.status = self.status.split('_')[0] + '_Idle'

		# tool use
		if self.timers['toolUsed'].init:
			self.status = self.status.split('_')[0] + '_' + self.tool

	def timer(self):
		for Time in self.timers.values():
			Time.check()



						

	def move(self,time):

		# normalizing a vector 
		# normalizing a vector 
		if self.direction.magnitude() > 0:
			self.direction = self.direction.normalize()

		# horizontal movement
		self.pos.x += self.direction.x * self.speed * time
		self.rect.centerx = self.pos.x

		# vertical movement
		self.pos.y += self.direction.y * self.speed * time
		self.rect.centery = self.pos.y

	def update(self, time):
		self.input()
		self.get_status()
		self.timer()
		self.move(time)
		self.animate(time)