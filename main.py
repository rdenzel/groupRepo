import pygame, sys, random
from pygame.locals import *
from soldiers import Soldier
from grid import Grid
from random import randint
from square import Square 

pygame.init()

clock = pygame.time.Clock()

height = 25
width = 25
square_size = 20


white = (255,255,255)
black = (0,0,0)


#------Actual Code------

grid = Grid(width,height,square_size)


player_size = square_size
soldier_size = square_size

player_pos= [2,2]
soldier1_pos = [0,0]

soldier1 = Soldier(soldier1_pos)
print soldier1.pos[0]
soldier1.move(soldier1_pos,"right")
print soldier1.pos[0]

soldier1_x = grid.getCoor(soldier1_pos)[0]
soldier1_y = grid.getCoor(soldier1_pos)[1]

player_x = grid.getCoor(player_pos)[0]
player_y = grid.getCoor(player_pos)[1]


the_square = Square([100,100],"regular",True,100)


def moveSoldier(direction):
	global soldier1_pos
	global soldier1_x
	global soldier1_y

	if direction==0:
		soldier1_pos = grid.up(soldier1_pos)
		soldier1_x = grid.getCoor(soldier1_pos)[0]
		soldier1_y = grid.getCoor(soldier1_pos)[1]
		print "moved 0"
	if direction==1:
		soldier1_pos = grid.right(soldier1_pos)
		soldier1_x = grid.getCoor(soldier1_pos)[0]
		soldier1_y = grid.getCoor(soldier1_pos)[1]
		print "moved 1"
	
	if direction==2:
		soldier1_pos = grid.down(soldier1_pos)
		soldier1_x = grid.getCoor(soldier1_pos)[0]
		soldier1_y = grid.getCoor(soldier1_pos)[1]

	if direction==3:	
		soldier1_pos = grid.left(soldier1_pos)
		soldier1_x = grid.getCoor(soldier1_pos)[0]
		soldier1_y = grid.getCoor(soldier1_pos)[1]




def movePlayer(position,move):
	
	global player_pos
	global player_x
	global player_y

	if move =="right":
		player_pos = (grid.right(position))
		player_x = grid.getCoor(player_pos)[0]
		player_y = grid.getCoor(player_pos)[1]
		

	elif move =="left":
		player_pos = (grid.left(position))
		player_x = grid.getCoor(player_pos)[0]
		player_y = grid.getCoor(player_pos)[1]

	elif move =="up":
		player_pos = (grid.up(position))
		player_x = grid.getCoor(player_pos)[0]
		player_y = grid.getCoor(player_pos)[1]

	elif move == "down":
		player_pos = (grid.down(position))
		player_x = grid.getCoor(player_pos)[0]
		player_y = grid.getCoor(player_pos)[1]

	#Pretty cool, huh?

print("code es bueno!")


#---------Running---------



#set up screen
screen = pygame.display.set_mode((500,500))

done = False

while(not done):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True

		elif event.type==MOUSEBUTTONDOWN:
			#print("Mouse click")
			#print grid.getSquare(pygame.mouse.get_pos())	
			
			grid.changeSquare(pygame.mouse.get_pos(),white)

		elif event.type ==KEYDOWN:
			if event.key == K_LEFT:
				movePlayer(player_pos,"left")
			if event.key ==(K_RIGHT):
				movePlayer(player_pos,"right")
			if event.key== (K_UP):
				movePlayer(player_pos,"up")
			if event.key ==(K_DOWN):
				movePlayer(player_pos,"down")





	x=randint(0,101)	
	
	if (x>95):
		y = x%4
		moveSoldier(y)	
	



#-----------Changes to Screen--------


	#screen color 
	screen.fill(black)
	grid.draw(screen)
	#print player_x



	#------draw the player
	pygame.draw.rect(screen,white,[player_x,player_y,player_size,player_size])

	#------draw the soldier
	pygame.draw.rect(screen,(255,0,0),[soldier1_x,soldier1_y,player_size,player_size])





	#update
	pygame.display.update()

	clock.tick(30)			
