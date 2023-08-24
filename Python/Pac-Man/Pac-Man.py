import pygame
import pygame_menu
import random
pygame.init()
pygame.display.set_caption('Pac-Man')
screen = pygame.display.set_mode((1120,560))
screen.fill([0,0,0])
white=(0,2,237)
black=(0,0,0)
White=(255,255,255)
pacOneX=560
pacOneY=500
pacTwoX=540
pacTwoY=500
a=0
width=1120
height=540


maze =[
    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
    1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,
    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
    1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,
    1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,2,2,2,2,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,
    2,2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,2,2,2,2,
    1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,
    2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,
    2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,
    1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,
    2,2,2,2,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,2,2,2,2,
    1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,
    1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,
    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
    1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,
    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
]


class gridSquare(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,20))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.topleft=(x,y)

class Pellet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,20))
        self.image.fill(black) 
        pygame.draw.circle(self.image,(White),(10,10),5)
        self.rect = self.image.get_rect()
        self.rect.topleft=(x,y)
class Ghost(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,20))
        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.topleft=(x,y)
        self.direction=pygame.math.Vector2()
        self.pos=pygame.math.Vector2(self.rect.center)
        self.direction.y=-80
        self.pos+=self.direction
        self.rect.center=self.pos
    def update(self):
        
        self.direction=pygame.math.Vector2()
        self.pos=pygame.math.Vector2(self.rect.center)
        
        rand = random.randint(1, 4)
        if rand==1:
            self.direction.y=-10
            hi = tuple(map(lambda i, j: i - j, self.rect.midtop, (0,10)))
            check_ahead = hi
            if tuple(screen.get_at(check_ahead)) == (0,2,237,255):
                self.direction.y=0
        elif rand==2:
            self.direction.y=10
            check_ahead = self.rect.midbottom
            if tuple(screen.get_at(check_ahead)) == (0,2,237,255):
                self.direction.y=0
        elif rand==3:
            self.direction.x=-10
            bye = tuple(map(lambda i, j: i - j, self.rect.midleft, (10,0)))
            check_ahead = bye
            if tuple(screen.get_at(check_ahead)) == (0,2,237,255):
                self.direction.y=0
        elif rand==4:
            self.direction.x=10
            check_ahead = self.rect.midright
            if tuple(screen.get_at(check_ahead)) == (0,2,237,255):
                self.direction.y=0
        self.pos+=self.direction
        self.rect.center=self.pos
        print(rand)
        pygame.display.flip()
            

        


class PacMan(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,20))
        self.image = pygame.image.load("Python/Pac-Man/Sprites/PacMan Up.png")
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.topleft=(x,y)    

        print(screen.get_at(self.rect.topleft) )

    def update(self):
        self.direction=pygame.math.Vector2()
        self.pos=pygame.math.Vector2(self.rect.center)
        if self.rect.y >=height:
            self.rect.topleft=(560,280)
        key=pygame.key.get_pressed()
        check_ahead = self.rect.midtop
        x = random.randint(1, 100)

        if key[pygame.K_w]:
            self.image = pygame.image.load("Python/Pac-Man/Sprites/PacMan Up.png")
            self.image = pygame.transform.scale(self.image,(20,20))
            #self.rect.x += self.velocity[0] 
            self.direction.y=-10
            # Subtracting Tuples https://www.geeksforgeeks.org/python-how-to-get-subtraction-of-tuples/# 
            hi = tuple(map(lambda i, j: i - j, self.rect.midtop, (0,10)))
            check_ahead = hi
            print(self.rect.midtop)
            if tuple(screen.get_at(check_ahead)) == (0,2,237,255):
                self.direction.y=0

            

        elif key[pygame.K_s]:
            self.image = pygame.image.load("Python/Pac-Man/Sprites/PacMan Down.png")
            self.image = pygame.transform.scale(self.image,(20,20))
            self.direction.y=10
            #self.rect.x += self.velocity[0] 
            check_ahead = self.rect.midbottom
            print(screen.get_at(check_ahead))
            if tuple(screen.get_at(check_ahead)) == (0,2,237,255):
               self.direction.y=0
            
                
        elif key[pygame.K_a]:
            self.image = pygame.image.load("Python/Pac-Man/Sprites/PacMan Left.png")
            self.image = pygame.transform.scale(self.image,(20,20))
            self.direction.x=-10
            bye = tuple(map(lambda i, j: i - j, self.rect.midleft, (10,0)))
            check_ahead = bye
            if tuple(screen.get_at(check_ahead)) == (0,2,237,255):
                self.direction.x=0

        elif key[pygame.K_d]:
            self.image = pygame.image.load("Python/Pac-Man/Sprites/PacMan Right.png")
            self.image = pygame.transform.scale(self.image,(20,20))
            self.direction.x=10
            check_ahead = self.rect.midright
            if tuple(screen.get_at(check_ahead)) == (0,2,237,255):
                self.direction.x=0
        else:
            self.direction.x=0
            self.direction.y=0

        self.pos+=self.direction
        self.rect.center=self.pos

        pygame.display.flip()
        
g=0
h=0
q=1
gridSquares = pygame.sprite.Group()
pellets = pygame.sprite.Group()
for z in maze:
    if z==1:
        newGridSquare = gridSquare(g,h)
        gridSquares.add(newGridSquare)
        g+=20
    elif z==0:
        newPellet = Pellet(g,h)
        pellets.add(newPellet)
        g+=20
    elif z==2:
        g+=20
    if g==1120:
        g=0
        h+=20
    


pygame.display.flip()



def endScreen():
    screen.fill("black")
    largeFont = pygame.font.SysFont('Pokemon GB.ttf', 60)
    Lose1 = largeFont.render("You died", 1, (255,255,255))
    Lose2= largeFont.render("Click Space to Restart", 1, (255,255,255))
    screen.blit(Lose1, (560,280))
    screen.blit(Lose2, (560,380))
    running = True
    pygame.display.flip()
    while running:
        key=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if key[pygame.K_SPACE]:
                running=False
                Main()
def winScreen():
    screen.fill("black")
    largeFont = pygame.font.SysFont('Pokemon GB.ttf', 60)
    Lose1 = largeFont.render("You Won", 1, (255,255,255))
    Lose2= largeFont.render("Click Space to Restart", 1, (255,255,255))
    screen.blit(Lose1, (560,280))
    screen.blit(Lose2, (560,380))
    running = True
    pygame.display.flip()
    while running:
        key=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if key[pygame.K_SPACE]:
                running=False
                Main()

def Main():
   
    lives=3
    pacmen = pygame.sprite.Group()  
    ghosts=pygame.sprite.Group()
    ghostRan = random.randint(1, 4)
    if ghostRan==1:
        img="Python/Pac-Man/Sprites/Ghost 1.png"
    elif ghostRan==2:
        img="Python/Pac-Man/Sprites/Ghost 2.png"
    if ghostRan==3:
        img="Python/Pac-Man/Sprites/Ghost 3.png"
    if ghostRan==4:
        img="Python/Pac-Man/Sprites/Ghost 4.png"
    ghostOne=Ghost(570,245,img)
    ghosts.add(ghostOne)
    pacmanOne=PacMan(pacOneX, pacOneY)
    pacmanTwo=PacMan(pacOneX, pacOneY)
    pacmanThree=PacMan(pacOneX, pacOneY)
    pacmen=[]
    pacmen.append(pacmanOne)
    pacmen.append(pacmanTwo)
    pacmen.append(pacmanThree)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for b in pellets:
            gets_hit = pygame.sprite.collide_rect(b, pacmanOne)
            if gets_hit:
                pellets.remove(b)
        for s in ghosts:
            gets_hit = pygame.sprite.collide_rect(s, pacmanOne)
            if gets_hit:
                #for z in pacmen():
                #pacmen.remove(z)
                print('killed')
                lives=lives-1
                pacmanOne=PacMan(pacOneX, pacOneY)

                
        if lives==0:
            endScreen()
        if len(pellets) == 0: 
            winScreen()

        screen.fill([0,0,0])
        gridSquares.update
        gridSquares.draw(screen)
        pellets.update
        pellets.draw(screen)
        screen.blit(ghostOne.image, ghostOne.rect.topleft)
        screen.blit(pacmanOne.image, pacmanOne.rect.topleft)
        ghostOne.update()
        pacmanOne.update()
        pygame.display.flip()

Main()

