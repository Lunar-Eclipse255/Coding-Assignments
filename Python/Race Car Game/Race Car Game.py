import pygame
import random
pygame.init()
pygame.mixer.init()
width = 700
height = 800
global white
white= (255,255,255)
pygame.display.set_caption('Race Car Game')
screen = pygame.display.set_mode((width,height))


#Create Background Class
class Road(pygame.sprite.Sprite):
    def __init__(self,X,Y):
        global boostRate
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((700,800))
        self.image = pygame.image.load("Python/Race Car Game/Sprites/Highway")
        self.image = pygame.transform.scale(self.image,(700,800))
        self.rect = self.image.get_rect()
        x=00
        y=00
        self.rect.topleft=(X,Y)
    def update(self): 
        self.rect.y +=2
        pygame.display.flip()
        if self.rect.y==800:
            self.rect.y=-800

class Trigger(pygame.sprite.Sprite):
    def __init__(self):
        global check
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((700,1))
        self.rect = self.image.get_rect()
        x= 0
        y=800
        self.rect.topleft=(x,y)
    def update(self): 
        self.rect.y +=2

          

class Car(pygame.sprite.Sprite):
    def __init__(self):
        global white
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((50,90))
        self.image= pygame.image.load("Python/Race Car Game/Sprites/Car")
        self.image = pygame.transform.scale(self.image,(50,100))
        self.rect = self.image.get_rect()
        x=350
        y=400
        self.rect.topleft = (x,y) 
    def update(self):
        global boostRate
        key=pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rect.x+=boostRate
        elif key[pygame.K_a]:
            self.rect.x+=-boostRate
        elif key[pygame.K_w]:
            self.rect.y+=-boostRate
        elif key[pygame.K_s]:
            self.rect.y+=boostRate
        if self.rect.y<=7:
            self.rect.y=8
        if self.rect.y>=622:
            self.rect.y=621
        elif self.rect.x<=113:
            self.rect.x=114
        elif self.rect.x>=542:
            self.rect.x=541
        
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((100,100))
        self.image = pygame.image.load("Python/Race Car Game/Sprites/Enemy")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        x= random.randint(113,542)
        y= random.randint(0,1)
        self.rect.topleft=(x,y)
    def draw(self):       
        self.rect.y+=2
        screen.blit(self.image,self.rect.topleft)
        """
        if self.rect.y >=height:
            x= random.randint(113,542)
            y= random.randint(20, 400)
        
            self.rect.y = y
            self.rect.x=x
            """


class Boost(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((50,50))
        self.image = pygame.image.load("Python/Race Car Game/Sprites/Engine")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        x= random.randint(113,542)
        y= random.randint(0,1)
        self.rect.topleft=(x,y)
    def draw(self):       
        self.rect.y+=2
        screen.blit(self.image,self.rect.topleft)
        if self.rect.y >=height:
            x= random.randint(113,542)
            y= random.randint(20, 400)
            self.rect.y = y
            self.rect.x=x
            
def endScreen1():
    image = pygame.image.load("Python/Race Car Game/Sprites/Slime")
    image = pygame.transform.scale(image,(700,800))
    screen.blit(image, (0,0))
    largeFont = pygame.font.SysFont('Pokemon GB.ttf', 60)
    Lose1 = largeFont.render("You died from slime acid", 1, (255,255,255))
    screen.blit(Lose1, (100,300))
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


def Main():
    run = True
    width = 700
    height = 800
    boostNum=1
    global boostRate
    global white
    boostRate=5
    check=0
    score=0
    boosts = []
    enemies=[]
    triggers=[]
    road1=Road(0,0)
    road2=Road(0,-800)
    car=Car()
    boost=Boost()
    trigger=Trigger()
    pygame.time.set_timer(pygame.USEREVENT+1, random.randrange(2000, 3500))
    pygame.time.set_timer(pygame.USEREVENT+2, random.randrange(2500, 2600))
    pygame.time.set_timer(pygame.USEREVENT+3, random.randrange(1, 2))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.USEREVENT+1:
                boosts.append(Boost())
            if event.type == pygame.USEREVENT+2:
                enemies.append(Enemy())
            if event.type == pygame.USEREVENT+3:
                score+=1
            
        largeFont2 = pygame.font.SysFont('comicsans', 40)       
        roadScore = largeFont2.render("Score:"+str(score), 1, (255,255,255))       




        screen.blit(screen,(0,0))
        if road1.rect.y==800:
            road1.rect.y=-800
        elif road2.rect.y==800:
            road2.rect.y=-800

            
    

        #display background object
        screen.blit(road1.image,road1.rect.topleft)
        screen.blit(road2.image,road2.rect.topleft)
        screen.blit(roadScore, (10,20))
        screen.blit(car.image,car.rect.topleft)
        screen.blit(car.image,car.rect.topleft)
        


        
        for x in boosts:
            x.draw()

            

        for y in enemies:
            y.draw()


        for z in boosts:
            gets_hit = pygame.sprite.collide_rect(z, car)
            if gets_hit:
                boosts.remove(z)
                boostRate=boostRate+boostNum
                boostNum=boostNum/1.1
               
        
        
                
    
        for b in enemies:
            gets_hit = pygame.sprite.collide_rect(b, car)
            if gets_hit:
                enemies.remove(b)
                endScreen1()

                
        for c in enemies:
            gets_hit = pygame.sprite.collide_rect(c, trigger)
            if gets_hit:
                enemies.remove(c)
                print("killed")

        for d in boosts:
            gets_hit = pygame.sprite.collide_rect(d, trigger)
            if gets_hit:
                boosts.remove(d)
                print("death")
                
                

        

        

    
        
        
        #update background object   
        road1.update()
        road2.update()      
        car.update()
   
    
        pygame.display.flip()
Main()