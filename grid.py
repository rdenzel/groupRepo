import pygame, sys, random
from pygame.locals import *
from square import Square



#This is an edit but i am a man
class Grid():

	#apparently you need to declare these variables here
	width = 0
	height = 0
	square_size = 0
	color = (255,255,255)
	pos = []
	squares = []


	def __init__(self,the_height,the_width,ss):
		self.height = the_height
		self.width = the_width
		self.square_size = ss
		pos = []

		
		#I don't use this yet, but might come in handy later. lol not sure really
		for i in range(self.width):
			for j in range(self.height):
				self.squares.append(Square([(i*self.square_size),(j*self.square_size)],"regular",False,self.square_size))
				#print [i,j]
		
			


#-----------The instructions for moving left,right,up,down--------
	def right (self,position):

		if  position[0]+1>=self.width:
			return position

		return [position[0]+1,position[1]]	

	def left (self,position):
		if position[0]<1:
			return position
	

		return [position[0]-1,position[1]]	
		
	def up (self,position):	
		if position[1]<1:
			return position	

		return [position[0],position[1]-1]	
		
	def down (self,position):
		if  position[1]+1>=self.height:	
			return position	

		return [position[0],position[1]+1]		


#---------return the coordinates in regular x,y form from the screen----				

	def getCoor (self,position):
		return[(position[0]*self.square_size),(position[1]*self.square_size)]	


	def changeSquare(self,position,color):
		for i in range(self.width*self.height):
			if position[0]>self.squares[i].pos[0] and position[0]<self.squares[i].pos[0]+self.square_size:
				if position[1]>self.squares[i].pos[1] and position[1]<self.squares[i].pos[1]+self.square_size:
					self.squares[i].changeColor((0,0,0))
					i = 1000 




	def getSquare(self,position):
	
		for i in range(self.width):
			for j in range(self.height):
				if position[0]>i*self.square_size and position[0]<(i+1)*self.square_size:
					if position[1]>j*self.square_size and position[1]<(j+1)*self.square_size:
						return [i,j]


#--------draws the grid.  easier here since it takes up too much space in the main

	def draw (self,screen):
		
		for i in range (self.width*self.height):	
			self.squares[i].draw(screen)


		for i in range (self.width):
			pygame.draw.line(screen,self.color,[self.square_size*i,0],[self.square_size*i,self.square_size*self.height])
			#print i

		for j in range (self.height):
			pygame.draw.line(screen,self.color,[0,self.square_size*j],[self.square_size*self.width,self.square_size*j])	
			#print j	
				


'''

#-------These are tests that I used when constructing the grid-----
screen = pygame.display.set_mode((500,500))

grid = Grid(10,10,10)

position = [9,5]

print grid.right(position)


done = False

while(not done):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True

	screen.fill((0,0,0))
	pygame.draw.line(screen,(255,255,255),[0,0],[100,100])
	grid.draw(screen)		

	#update
	pygame.display.update()

	clock.tick(60)		

'''
