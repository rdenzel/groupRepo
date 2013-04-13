import pygame, sys, random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

height = 480
width = 640


white = (255,255,255)
black = (0,0,0)


#set up screen
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Picture Test')


#background image
background_image = pygame.image.load("koala.jpg").convert()
screen.blit(background_image,[0,0])

player_image = pygame.image.load("playerX.png").convert()
screen.blit(player_image,[100,100])
player_image.set_colorkey(white)

done = False

while(not done):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True



	#screen color 
	#screen.fill(black)


	#update
	pygame.display.update()

	clock.tick(60)			

