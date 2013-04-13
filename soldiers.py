import pygame, sys, random
from pygame.locals import *
from grid import Grid
pygame.init()



class Soldier():
	grid = Grid(5,5,100)
	level = 0
	hp = 10
	type=""
	pos=[0,0]
	hSpeed = 0
	vSpeed = 0

	def __init__(self,position):
		#self.type = theType
		self.level = 1
		self.hp = 10
		self.pos[0] = position[0]
		self.pos[1] = position[1]




	def move(self,position,direction):
		if direction=="right":
			self.pos = self.grid.right(position)

		if direction=="left":
			self.pos = self.grid.left(position)

		if direction=="up":
			self.pos = self.grid.up(position)
			
		if direction=="down":
			self.pos = self.grid.down(position)			


	def getHit(self,x):
		self.hp = self.hp-x


	def attack(self,enemy):
		enemy.getHit(1)








			
			

