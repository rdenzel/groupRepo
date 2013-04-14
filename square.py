import pygame, sys, random
from pygame.locals import *


class Square():

	pos = [0,0]
	active = False
	name = ""
	color = (0,0,0)
	size = 0



	def __init__(self,position,theType,isActive,theSize):

		self.pos = position
		self.active = isActive
		self.name = theType
		self.size = theSize

		if self.name == "regular":
			self.color = (0,0,255)


	def draw(self,screen):
		#print self.pos
		pygame.draw.rect(screen,self.color,[self.pos[0],self.pos[1],self.pos[0]+self.size,self.pos[1]+self.size])



	def setActive(self):
		self.active = True


	def changeColor(self,theColor):
		self.color = theColor
		print "changed color!"





