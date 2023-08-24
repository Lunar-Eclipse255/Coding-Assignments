#get library for pygame
import pygame
pygame.init()
pygame.display.set_caption('Pong')
screen = pygame.display.set_mode((800,800))
screen.fill([0,0,0])
heightBottom=680
heightTop=0
widthRight=680
widthLeft=0
paddleOneX=10
paddleOneY=375
paddleTwoX=770
paddleTwoY=375
ballX=340
ballY=340
White=(255,255,255)
Black=(0,0,0)
score1=0
score2=0

def Line():
    pygame.draw.line(screen, (255,255,255),(400,0),(400,800),width=10)

class Paddle(pygame.sprite.Sprite):
    def __init__(self,X, Y):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((10,50))
        self.image.fill(White) 
        self.rect = self.image.get_rect()
        self.rect.topleft=(X,Y)
        
        
    

    def update(self, Key):
        if pygame.K_w == Key:
            self.rect.y+=-5
        if pygame.K_s== Key:
            self.rect.y+=5
        if pygame.K_UP==Key:
            self.rect.y+=-5
        if pygame.K_DOWN==Key:
            self.rect.y+=5
        if self.rect.y >=heightBottom:
            self.rect.y = heightBottom
        elif self.rect.y <=heightTop:
            self.rect.y = heightTop

    
        






class Ball(pygame.sprite.Sprite):
    def __init__(self, ballX, ballY):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((25,25))
        self.image.fill(Black) 
        pygame.draw.circle(self.image,(White),(12,12),12)
        self.rect = self.image.get_rect()
        self.rect.topleft=(ballX,ballY)
        self.velocity = [2,3]
    
    
    def update(self, bounce):
        
        self.rect.x += self.velocity[0] 
        self.rect.y += self.velocity[1]
        if self.rect.y >=720:
            self.velocity[1] = -self.velocity[1]
        if self.rect.y <=0:
            self.velocity[1] = -self.velocity[1]
        if bounce==True:
            self.velocity[0]=-self.velocity[0] 
def endScreen1():
    screen.fill((0,0,0))
    largeFont = pygame.font.SysFont('comicsans', 60)
    Win1 = largeFont.render("Player 1 Won", 1, (255,255,255))
    screen.blit(Win1, (200,300))
    run = True
    pygame.display.flip()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
def endScreen2():
    screen.fill((0,0,0))
    largeFont = pygame.font.SysFont('comicsans', 60)
    Win1 = largeFont.render("Player 2 Won", 1, (255,255,255))
    screen.blit(Win1, (200,300))
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
    

 


        

paddleOne=Paddle(paddleOneX,paddleOneY)
paddleTwo=Paddle(paddleTwoX,paddleTwoY)
paddles = pygame.sprite.Group()
paddles.add(paddleOne,paddleTwo)

ball=Ball(ballX,ballY)

pygame.display.flip()
clockobject = pygame.time.Clock()
#Main Loop
running = True
while running:
    clockobject.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        

        
    
    screen.fill([0,0,0])
    Line()
    key=pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddleOne.update(pygame.K_w)
    if key[pygame.K_s]:
        paddleOne.update(pygame.K_s)
    if key[pygame.K_UP]:
        paddleTwo.update(pygame.K_UP)
    if key[pygame.K_DOWN]:
        paddleTwo.update(pygame.K_DOWN)
    if key[pygame.K_q]:
        endScreen1()
    if key[pygame.K_p]:
        endScreen2()
        
    getHits = pygame.sprite.spritecollide(ball, paddles, False) 
    for p in getHits: 
        ball.update(True)
    if ball.rect.x<=-5:
        score2+=1
        ball.rect.x=340
        ball.rect.y=340
    if ball.rect.x>=790:
        score1+=1
        ball.rect.x=340
        ball.rect.y=340

    if score1 >= 10:
        endScreen1()
    elif score2>=10:
        endScreen2()
    largeFont = pygame.font.SysFont('comicsans', 60)
    Score1 = largeFont.render(str(score1), 1, (255,255,255))
    Score2 = largeFont.render(str(score2), 1, (255,255,255))
        
    screen.blit(paddleOne.image, paddleOne.rect.topleft)
    screen.blit(paddleTwo.image,paddleTwo.rect.topleft)
    screen.blit(ball.image,ball.rect.topleft)
    screen.blit(Score1, (150,100))
    screen.blit(Score2, (700,100))
    ball.update(False)
    pygame.display.flip()