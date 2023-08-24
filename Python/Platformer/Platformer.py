import pygame
import Spritesheet

pygame.init()
tileSize=30
map = [
'                                                2     ',
'                                                2     ',
'                                                2     ',
' 00    000            00                        2     ',
' 00                                  00         2     ',
' 0000             00       00     0             2     ',
' 00000                           00             2     ',
' 00          00   00  00       0                2     ',
'    1       00    00  000    000                2     ',
'    0000  000000  00  0000000000     00         2     ',
'00000000  000000  00  0000000000    00     0   0222222']
w = 500
h = len(map)*tileSize
clock = pygame.time.Clock()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Spritesheets')



sprite_sheet_image = pygame.image.load('Python/Platformer/Sprites/DinoSprites - tard.png').convert_alpha()
sprite_sheet = Spritesheet.Spritesheet(sprite_sheet_image)
BG=pygame.image.load('Python/Platformer/Sprites/6N9Jnv.png')
BG=pygame.transform.scale(BG,(1440,760))
backgroundColor = (50, 50, 50)
black = (0, 0, 0)
screen.blit(BG,(0,0))


frame_0 = sprite_sheet.get_image(4,4,15,17,black, 3)
frame_1 = sprite_sheet.get_image(28,4, 15,17, black, 3)
frame_2 = sprite_sheet.get_image(72,4, 15,17, black, 3)
frame_3 = sprite_sheet.get_image(100,4, 15,17, black, 3)
frame_4 = sprite_sheet.get_image(124,4, 15,17, black, 3)
frame_5 = sprite_sheet.get_image(148,4, 15,17, black, 3)
frame_6 = sprite_sheet.get_image(172,4,15,17, black, 3)
frame_7 = sprite_sheet.get_image(196,4, 15,17, black, 3)
frame_8 = sprite_sheet.get_image(220,4, 15,17, black, 3)
frame_9 = sprite_sheet.get_image(244,4, 15,17, black, 3)
frame_10 = sprite_sheet.get_image(268,4, 15,17, black, 3)
frame_11 = sprite_sheet.get_image(292,4,15,17, black, 3)
frame_12 = sprite_sheet.get_image(316,4, 15,17, black, 3)
frame_13 = sprite_sheet.get_image(340,4,15,17, black, 3)

class Tile(pygame.sprite.Sprite):
    def __init__(self,position,size):
        super().__init__()
        self.image=pygame.Surface((size,size))
        self.image=pygame.image.load('Python/Platformer/Sprites/tileset_lava.png')
        self.rect=self.image.get_rect(topleft=position)
    def update(self,shift):
        self.rect.x-=shift
	
class Blank(pygame.sprite.Sprite):
    def __init__(self,position,size):
        super().__init__()
        self.image=pygame.Surface((size,size))
        self.image=pygame.image.load('Python/Platformer/Sprites/png.png')
        self.rect=self.image.get_rect(topleft=position)
    def update(self,shift):
        self.rect.x-=shift
	
class Player(pygame.sprite.Sprite):
	def __init__(self,pos,surface):
		super().__init__()
		
		self.animated()
		self.frameCount = 0
		self.animation_speed = 0.15
		self.image = self.animations['idle'][self.frameCount]
		self.rect = self.image.get_rect(topleft = pos)
		self.display_surface = surface


		# player movement
		self.direction = pygame.math.Vector2(0,0)
		self.speed = 4
		self.gravity = 0.8
		self.jump_speed = -13.5

		# player status
		self.status = 'idle'
		self.facing_right = True
		self.on_ground = False
		self.on_left = False
		self.on_right = False


	def animated(self):
		self.animations={'idle':[frame_0,frame_1],'run':[frame_2,frame_3,frame_4,frame_5,frame_6,frame_7,frame_8,frame_9,frame_10,frame_11,frame_12],'jump':[frame_0],'fall':[frame_13]}
#Learned how to animate from youtube
	def animate(self):
		
		animation = self.animations[self.status]

		# loop over frame index 
		self.frameCount += self.animation_speed
		if self.frameCount >= len(animation):
			self.frameCount = 0

		image = animation[int(self.frameCount)]
		if self.facing_right:
			self.image = image
		else:
			flipped_image = pygame.transform.flip(image,True,False)
			self.image = flipped_image

		# set the rect
		if self.on_ground and self.on_right:
			self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
		elif self.on_ground and self.on_left:
			self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
		elif self.on_ground:
			self.rect = self.image.get_rect(midbottom = self.rect.midbottom)


	
	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_d]:
			self.direction.x = 1
			self.facing_right = True
		elif keys[pygame.K_a]:
			self.direction.x = -1
			self.facing_left = True
		else:
			self.direction.x = 0

		if keys[pygame.K_SPACE] and self.on_ground:
			self.direction.y = self.jump_speed

	def status2(self):
		if self.direction.y < 0:
			self.status = 'jump'
		elif self.direction.y > 1:
			self.status = 'fall'
		else:
			if self.direction.x != 0:
				self.status = 'run'
			else:
				self.status = 'idle'

	def gravity2(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y


		

	def update(self):
		self.input()
		self.status2()
		self.animate()
		if self.rect.y>h+100:
			endScreen()

def endScreen():
    image = BG
    image = pygame.transform.scale(image,(w,h))
    screen.blit(image, (0,0))
    largeFont = pygame.font.SysFont('Pokemon GB.ttf', 60)
    Lose1 = largeFont.render('You died', 1, (255,255,255))
    Lose2 = largeFont.render('Respawn with Space', 1, (255,255,255))
    screen.blit(Lose1, (165,(h/2)-20))
    screen.blit(Lose2, (50,(h/2)+50))
    run = True
    pygame.display.flip()
    while run:
        key=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if key[pygame.K_SPACE]:
                run=False
                Main()
def winScreen():
    image = BG
    image = pygame.transform.scale(image,(w,h))
    screen.blit(image, (0,0))
    largeFont = pygame.font.SysFont('Pokemon GB.ttf', 60)
    Lose1 = largeFont.render('You Won!', 1, (255,255,255))
    Lose2 = largeFont.render('Respawn with Space', 1, (255,255,255))
    screen.blit(Lose1, (165,(h/2)-20))
    screen.blit(Lose2, (50,(h/2)+50))
    run = True
    pygame.display.flip()
    while run:
        key=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if key[pygame.K_SPACE]:
                run=False
                Main()
class Level:
	def __init__(self,level_data,surface):
		
		# level setup
		self.display_surface = surface 
		self.setup(level_data)
		self.shift = 0
		self.currentX = 0

		# dust 
		self.player_on_ground = False

	

	def get_player_on_ground(self):
		if self.player.sprite.on_ground:
			self.player_on_ground = True
		else:
			self.player_on_ground = False
			


	def setup(self,layout):
		self.tiles = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		self.finishes = pygame.sprite.Group()
        
		for row_index,row in enumerate(layout):
			for col_index,cell in enumerate(row):
				x = col_index * tileSize
				y = row_index * tileSize
				
				if cell == '0':
					tile = Tile((x-10,y-10),tileSize)
					self.tiles.add(tile)
				if cell == '1':
					player_sprite = Player((x,y),self.display_surface)
					self.player.add(player_sprite)
				if cell =='2':
					finish = Blank((x-10,y-10),tileSize)
					self.finishes.add(finish)

	def shifted(self):
		player = self.player.sprite
		player0 = player.rect.centerx
		direction0 = player.direction.x

		if player0 < 125 and direction0 < 0:
			self.shift = -8
			player.speed = 0
		elif player0 > 375 and direction0 > 0:
			self.shift = 8
			player.speed=0
			    
		else:
			self.shift = 0
			player.speed = 8

	def horizontal_movement_collision(self):
		player = self.player.sprite
		player.rect.x += player.direction.x * player.speed

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.x < 0: 
					player.rect.left = sprite.rect.right
					player.on_left = True
					self.currentX = player.rect.left
				elif player.direction.x > 0:
					player.rect.right = sprite.rect.left
					player.on_right = True
					self.currentX = player.rect.right

		if player.on_left and (player.rect.left < self.currentX or player.direction.x >= 0):
			player.on_left = False
		if player.on_right and (player.rect.right > self.currentX or player.direction.x <= 0):
			player.on_right = False

	def vertical_movement_collision(self):
		player = self.player.sprite
		player.gravity2()

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.y > 0: 
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.on_ground = True
				elif player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_ceiling = True

		if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
			player.on_ground = False
			
	def winCheck(self):
		player = self.player.sprite
		player.gravity2()
		for sprite in self.finishes.sprites():
			if sprite.rect.colliderect(player.rect):
				winScreen()
	def run(self):

		# level tiles
		self.tiles.update(self.shift)
		self.tiles.draw(self.display_surface)
		self.shifted()
		self.finishes.update(self.shift)
		self.finishes.draw(self.display_surface)
		# player
		self.player.update()
		self.horizontal_movement_collision()
		self.get_player_on_ground()
		self.vertical_movement_collision()
		self.winCheck()
		self.player.draw(self.display_surface)


tiles=pygame.sprite.Group()

def Main():
    run=True
    level=Level(map,screen)
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        screen.blit(BG,(0,0))
        level.run()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
Main()