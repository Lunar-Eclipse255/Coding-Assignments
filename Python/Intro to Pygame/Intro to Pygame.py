#get library for pygame
import pygame
pygame.init()
pygame.display.set_caption('Intro to Pygame')
screen = pygame.display.set_mode((800,760))
screen.fill([0,0,0])
characterImage=pygame.image.load("Python/Intro to Pygame/character.png")
#characterImage=pygame.transform.scale(characterImage, (400,330))
X=200
Y=400
#screen.blit(characterImage, (X,Y))
x=0
y=600



pygame.display.flip()

#Main Loop
running = True
while running:
    if y<= 69:
        y=920
        screen.blit(characterImage, (x,y))
        pygame.display.flip()

    elif y>= 920:
        y=75
        screen.blit(characterImage, (x,y))
        pygame.display.flip()

    elif x<= -90:
        x=790
        screen.blit(characterImage, (x,y))
        pygame.display.flip()

    elif x>=800:
        x=-85
        screen.blit(characterImage, (x,y))
        pygame.display.flip()

    screen.fill([0,0,0])
    screen.blit(characterImage, (x,y))
    
    
    key = pygame.key.get_pressed()
    screen.blit(characterImage, (x,y))
    if key[pygame.K_s]:
        y=y+0.75
        pygame.display.flip()
        screen.blit(characterImage, (x,y))
    elif key[pygame.K_w]:
        y=y-0.75
        pygame.display.flip()
        screen.blit(characterImage, (x,y))
    elif key[pygame.K_d]:
        x=x+0.75
        pygame.display.flip()
        screen.blit(characterImage, (x,y))
    elif key[pygame.K_a]:
        x=x-0.75
        
        pygame.display.flip()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #pygame.draw.rect(screen,(120,123,10),(300,500,100,100))
            #pygame.draw.arc(screen,(100,50,150),(200,400,100,100), (0.436332), (0.99)) 
            #pygame.draw.circle(screen,(150,10,150),(100,500), 20) 
            
    
        

  
  
    pygame.display.flip()
