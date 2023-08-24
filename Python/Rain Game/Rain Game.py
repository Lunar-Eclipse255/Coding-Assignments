#get libray for pygame
import pygame
import random
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Rain Game')

width = 800
height = 600
screen = pygame.display.set_mode((width,height))
screen.fill([0,0,0])
GREEN = (0,255,0)
x=500
y=500
score=0

backgroundImage=pygame.image.load("Python/Rain Game/Sprites/Background")
backgroundImage=pygame.transform.scale(backgroundImage, (800,600))
rainAmbience = pygame.mixer.Sound("Python/Rain Game/Sprites/Rain ambience") 
#Umbrella_2=pygame.image.load("Umbrella 2")
#Umbrella_2=pygame.transform.scale(Umbrella_2, (130,200))



class Rain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((45,50))
        self.image = pygame.image.load("Python/Rain Game/Sprites/Raindrop")
        self.image = pygame.transform.scale(self.image,(45,50))
        self.rect = self.image.get_rect()
        x = random.randint(0,800)
        y = random.randint(0,800)
        self.rect.topleft = (x,y)
    def update(self): 
        self.rect.y +=6
        if self.rect.y >=height:
            self.rect.y = 0

       


class Umbrella(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((130,200))
        self.image = pygame.image.load("Python/Rain Game/Sprites/Umbrella")
        self.image = pygame.transform.scale(self.image,(130,200))
        self.rect = self.image.get_rect()
        x=400
        y=400
        self.rect.topleft = (x,y) 
    def update(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rect.x+=2
        elif key[pygame.K_a]:
            self.rect.x+=-2
        if self.rect.x>=790:
            self.rect.x=790
            screen.blit(self.image, (self.rect.x,self.rect.y))
            pygame.display.flip()
        elif self.rect.x<=0:
            self.rect.x=5
            screen.blit(self.image, (self.rect.x,self.rect.y))
            pygame.display.flip()
            



            

raindrops = pygame.sprite.Group()

for i in range(100):
    newRain = Rain()
    raindrops.add(newRain)

#generate an umbrella
rains=Rain()
umbrellas=Umbrella()
pygame.display.flip()




#Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
   
    
    
   
    
    #add sprites to screen and update them
    
    screen.blit(backgroundImage,(0,0))
    
    
    largeFont = pygame.font.SysFont('comicsans', 60)
    text = largeFont.render('Your Score is: ' + str(score), 1, (255,255,255))

    #add sprites to screen and update them
    raindrops.update()
    umbrellas.update()
    screen.blit(umbrellas.image,umbrellas.rect.topleft)
    raindrops.draw(screen)
    umbrellas.update()
    screen.blit(text, (150,100))
    getHits = pygame.sprite.spritecollide(umbrellas,raindrops,True)

  
    for p in getHits: 
        newRain = Rain()
        raindrops.add(newRain)
        score+=1
    rainAmbience.play(-1) 
    pygame.display.flip()