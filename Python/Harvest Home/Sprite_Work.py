import pygame
import Character
from Attributes import *
black = (255,255,255)
h =847
w=1440
pygame.init()
screen = pygame.display.set_mode((w,h))
playerSpriteSheet = pygame.image.load('Python/Harvest Home/Sprites/Player.png').convert_alpha()
cropsSpriteSheet = pygame.image.load('Python/Harvest Home/Sprites/Crops.png').convert_alpha()
iconsSpriteSheet = pygame.image.load('Python/Harvest Home/Sprites/Icons.png').convert_alpha()
treesSpriteSheet = pygame.image.load('Python/Harvest Home/Sprites/Trees.png').convert_alpha()
spriteSheetPlayer=Character.Sprite(playerSpriteSheet)
spriteSheetCrops=Character.Sprite(cropsSpriteSheet)
spriteSheetIcons=Character.Sprite(iconsSpriteSheet)
spriteSheetTrees=Character.Sprite(treesSpriteSheet)

#Player Movement Sprites
playerRightOne=spriteSheetPlayer.get_image(71, 344, 37, 79, black,0.5)
playerRightTwo=spriteSheetPlayer.get_image(160, 344, 42, 76, black,0.5)
playerRightThree=spriteSheetPlayer.get_image(654, 343, 40, 80, black,0.5)
playerRightFour=spriteSheetPlayer.get_image(744, 343, 43, 78, black,0.5)
playerLeftOne=spriteSheetPlayer.get_image(79, 118, 39, 80, black,0.5)
playerLeftTwo=spriteSheetPlayer.get_image(160, 120, 42, 77, black,0.5)
playerLeftThree=spriteSheetPlayer.get_image(663, 118, 38, 82, black,0.5)
playerLeftFour=spriteSheetPlayer.get_image(744, 119, 42, 78, black,0.5)
playerUpOne=spriteSheetPlayer.get_image(78, 233, 37, 81, black,0.5)
playerUpTwo=spriteSheetPlayer.get_image(164, 235, 34, 75, black,0.5)
playerUpThree=spriteSheetPlayer.get_image(662, 233, 37, 83, black,0.5)
playerUpFour=spriteSheetPlayer.get_image(748, 235, 36, 76, black,0.5)
playerDownOne=spriteSheetPlayer.get_image(79, 0, 40, 81, black,0.5)
playerDownTwo=spriteSheetPlayer.get_image(163, 0, 40, 78, black,0.5)
playerDownThree=spriteSheetPlayer.get_image(663, 0, 40, 81, black,0.5)
playerDownFour=spriteSheetPlayer.get_image(747, 0, 40, 78, black,0.5)

#Player Idle Sprites
playerRightIdle=spriteSheetPlayer.get_image(0, 343, 38, 84, black,0.5)
playerLeftIdle=spriteSheetPlayer.get_image(0, 117, 38, 84, black,0.5)
playerUpIdle=spriteSheetPlayer.get_image(0, 231, 41, 83, black,0.5)
playerDownIdle=spriteSheetPlayer.get_image(0, 0,41,83, black,0.5)

#Player Scythe Sprites
playerRightScytheOne=spriteSheetPlayer.get_image(506, 323, 77, 97, black,0.5)
playerRightScytheTwo=spriteSheetPlayer.get_image(1089, 334, 78, 85, black,0.5)
playerLeftScytheOne=spriteSheetPlayer.get_image(481, 104, 78, 97, black,0.5)
playerLeftScytheTwo=spriteSheetPlayer.get_image(1063, 115, 80, 86, black,0.5)
playerUpScytheOne=spriteSheetPlayer.get_image(496, 213, 61, 101, black,0.5)
playerUpScytheTwo=spriteSheetPlayer.get_image(1106, 219, 62, 95, black,0.5)
playerDownScytheOne=spriteSheetPlayer.get_image(505, 0, 79, 102, black,0.5)
playerDownScytheTwo=spriteSheetPlayer.get_image(1071, 0, 61, 92, black,0.5)

#Player Axe Sprites 
playerRightAxeTwo=spriteSheetPlayer.get_image(305, 337, 84, 81, black,0.5)
playerRightAxeOne=spriteSheetPlayer.get_image(890, 337, 73, 80, black,0.5)
playerLeftAxeTwo=spriteSheetPlayer.get_image(273, 117, 84, 81, black,0.5)
playerLeftAxeOne=spriteSheetPlayer.get_image(865, 117, 76, 81, black,0.5)
playerUpAxeTwo=spriteSheetPlayer.get_image(315, 232, 34, 77, black,0.5)
playerUpAxeOne=spriteSheetPlayer.get_image(899, 232, 34, 77, black,0.5)
playerDownAxeTwo=spriteSheetPlayer.get_image(312, 0, 40, 99, black,0.5)
playerDownAxeOne=spriteSheetPlayer.get_image(899, 0, 36, 84, black,0.5)


#Plant Seeds
taroRoot=spriteSheetIcons.get_image(15, 14, 21, 24, black,0.5)
coffeeBeanSeeds=spriteSheetIcons.get_image(54,3, 37, 43, black,0.5)
cranberrySeeds=spriteSheetIcons.get_image(438,0, 37, 48, black,0.5)
blueberrySeeds=spriteSheetIcons.get_image(630,3, 37, 42, black,0.5)
wheatSeeds=spriteSheetIcons.get_image(678,0, 37, 48, black,0.5)

#Plant Product
taro=spriteSheetIcons.get_image(387,0, 43, 48, black,0.5)
coffeeBean=spriteSheetIcons.get_image(483,3, 42, 42, black,0.5)
cranberry=spriteSheetIcons.get_image(825,9, 36, 36, black,0.5)
blueberry=spriteSheetIcons.get_image(777,12, 30, 31, black,0.5)
wheat=spriteSheetIcons.get_image(725,0, 36, 48, black,0.5)

#Tree Saplings
pomegranateSapling=spriteSheetIcons.get_image(192,0, 48, 48, black,0.5)
orangeSapling=spriteSheetIcons.get_image(240,0, 48, 48, black,0.5)
appleSapling=spriteSheetIcons.get_image(288,0, 48, 48, black,0.5)
cherrySapling=spriteSheetIcons.get_image(336,0, 48, 47, black,0.5)

#Tree Products
pomegranate=spriteSheetIcons.get_image(969,14, 30, 30, black,0.5)
orange=spriteSheetIcons.get_image(869,2, 39, 45, black,0.5)
apple=spriteSheetIcons.get_image(921,9, 33, 36, black,0.5)
cherry=spriteSheetIcons.get_image(1014,2, 36, 45, black,0.5)

#Artisan Products
honey=spriteSheetIcons.get_image(153,5, 30, 39, black,0.5)

#Tools
scythe=spriteSheetIcons.get_image(576,0, 48, 48, black,0.5)
axe=spriteSheetIcons.get_image(528,3, 48, 45, black,0.5)
wateringCan=spriteSheetIcons.get_image(96,12, 48, 33, black,0.5)

#Plant 
blueBerryOne=spriteSheetCrops.get_image(131, 149, 10, 7, black,1)
blueBerryTwo=spriteSheetCrops.get_image(179, 143, 10, 13, black,1)
blueBerryThree=spriteSheetCrops.get_image(209, 133, 10, 7, black,1)
blueBerryFour=spriteSheetCrops.get_image(225, 131, 14, 23, black,1)

#Trees
cherryOne=spriteSheetTrees.get_image(17, 60, 15, 17, black,0.5)
cherryTwo=spriteSheetTrees.get_image(108, 43, 21, 37, black,0.5)
cherryThree=spriteSheetTrees.get_image(146, 28, 42, 52, black,0.5)
cherryFour=spriteSheetTrees.get_image(432, 0, 97, 160, black,0.5)


