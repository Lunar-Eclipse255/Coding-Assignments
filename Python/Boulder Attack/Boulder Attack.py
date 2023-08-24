#get library for pygame
import pygame
import random 
pygame.init()

screen = pygame.display.set_mode((800,760))
screen.fill([132,132,132])
pygame.display.set_caption('Boulder Attack')
characterImage=pygame.image.load("Python/Boulder Attack/Sprites/Character")
boulderImage=pygame.image.load("Python/Boulder Attack/Sprites/Boulder")
flagpoleImage=pygame.image.load("Python/Boulder Attack/Sprites/Flagpole")
flagpoleImage=pygame.transform.scale(flagpoleImage, (350,350))
boulderImage=pygame.transform.scale(boulderImage, (100,100))
characterImage=pygame.transform.scale(characterImage, (60,80))
boulderX=400
boulderY=-40
flagpoleX=500
flagpoleY=410
pygame.display.flip()
characterX=0
characterY=680
boulderCheck=0
pygame.display.flip()
score=0



pygame.display.flip()

#Main Loop
running = True
while running:
    
    #if characterY<= 69:
        #characterY=920
        #screen.blit(characterImage, (characterX,characterY))
        #pygame.display.flip()

    #elif characterY>= 920:
        #characterY=75
        #screen.blit(characterImage, (characterX,characterY))
        #pygame.display.flip()

    if characterX<= -90:
        characterX=0
        screen.blit(characterImage, (characterX,characterY))
        pygame.display.flip()

    #elif characterX>=800:
        #characterX=-85
        #screen.blit(characterImage, (characterX,characterY))
        #pygame.display.flip()

    screen.fill([132,132,132])

    randEvent=random.randint(0,999)
    if randEvent== 256:
        score=score+10000
        hText = largeFont.render("LOTTERY", 1, (255,255,255))
        screen.blit(hText, (300,100))
    
    if randEvent== 989:
        randEvent=random.randint(0,300)
        if randEvent==282:
            score=score+1000000000
            hText = largeFont.render("LOTTERY", 1, (255,255,255))
            screen.blit(hText, (300,100))

    screen.blit(characterImage, (characterX,characterY))
    screen.blit(flagpoleImage, (flagpoleX,flagpoleY))
    if boulderCheck<1:
            boulderX=random.randint(0,600) 
            screen.blit(boulderImage, (boulderX,boulderY))
            boulderCheck=boulderCheck+1

    if boulderCheck==1:
        boulderY=boulderY+3
        screen.blit(boulderImage, (boulderX,boulderY))

    
    if boulderY>920:
        boulderCheck=boulderCheck-1
        boulderY=400
        pygame.display.flip()
    if characterY-70<= boulderY <= characterY+70 :
       
        if characterX-60<= boulderX <= characterX+60:
            
            characterX=0
            characterY=821
            score=score-100000
            hText = largeFont.render("HOSPITAL BILLS", 1, (255,255,255))
            screen.blit(hText, (300,100))
    
    if characterX==flagpoleX+70:
            
            characterX=0
            characterY=821
            score=score+11
    largeFont = pygame.font.SysFont('comicsans', 30)
    text = largeFont.render('Money $: ' + str(score), 1, (255,255,255))
    screen.blit(text, (300,100))

    

    key = pygame.key.get_pressed()
    
    #if key[pygame.K_s]:
        #characterY=characterY+1
        #pygame.display.flip()
        #screen.blit(characterImage, (characterX,characterY))
    #elif key[pygame.K_w]:
        #characterY=characterY-1
        #pygame.display.flip()
        #screen.blit(characterImage, (characterX,characterY))
    if key[pygame.K_d]:
        characterX=characterX+1.5
        pygame.display.flip()
        screen.blit(characterImage, (characterX,characterY))
    elif key[pygame.K_a]:
        characterX=characterX-1.5
        
        pygame.display.flip()
        screen.blit(characterImage, (characterX,characterY))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #pygame.draw.rect(screen,(120,123,10),(300,500,100,100))
            #pygame.draw.arc(screen,(100,50,150),(200,400,100,100), (0.436332), (0.99)) 
            #pygame.draw.circle(screen,(150,10,150),(100,500), 20) 
            
    
        

  
  
    pygame.display.flip()