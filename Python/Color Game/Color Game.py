#get library for pygame
import pygame
import random
pygame.init()
pygame.display.set_caption('Color Game')
#create a screen that is 800 x 800 that is black
screen = pygame.display.set_mode((800,800))
screen.fill([0,0,0])


#create 3 variables red, green and blue filled with random value from 0 to 255
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)
#create a variable called size with value 50
size=50
#create a circle of that color that is at center of screen with radius of size
pygame.draw.circle(screen, (red,green,blue), (400,400), size)
pygame.display.flip()

#Main Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    key = pygame.key.get_pressed()
    #if space key pressed it should change color
        #what do we want to change to get a new color circle?
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        red=random.randint(0,255)
        green=random.randint(0,255)
        blue=random.randint(0,255)
        pass
        
    pygame.display.flip()
    #if up or down arrow pressed size should change
    if key[pygame.K_w]:
        size=size+3
        
    elif key[pygame.K_s]:
        size=size-3
    
    elif key[pygame.K_ESCAPE]:
        screen.fill([0,0,0])
        pygame.display.flip()
    
    if size<=0:
        size=1
        

  #gets the mouse position  
    pos = pygame.mouse.get_pos()

    #use mouse position to move around circle
    x = pos[0]   
    y = pos[1] 
    pygame.draw.circle(screen, (red,green,blue), (x,y), size)
    
    pygame.display.flip()
