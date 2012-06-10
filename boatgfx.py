import os, sys, pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class BoatGfx():
	
	def __init__(self, boat):
		pygame.init()
		
		self.boat = boat
		self.boatpic = []
		
		sound = pygame.mixer.Sound("geese.mp3")
		sound.play()

		self.size = self.width, self.height = 600,400
		self.backg = 0,0,0
		
		self.screen = pygame.display.set_mode(self.size)
		
		for i in range(len(boat)):
			self.boatpic.append(pygame.image.load(self.boat[i].picpath))
		
		self.x. = 0
		self.y = 0
		self.x1 = 1
		self.y1 = 1
	
	def run(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		self.backg = self.x%255, self.y%255, ((self.x+self.y)%255)
		self.screen.fill(self.backg)
		self.screen.blit(self.boatpic[0],(self.x,self.y))
		pygame.display.flip()
		
		if self.x == self.width:
			self.x1 = -1
		elif self.x == 0:
			self.x1 = 1
		if self.y == self.height:
			self.y1 = -1
		elif self.y == 0:
			self.y1 = 1
	
		self.x = self.x+self.x1
		self.y = self.y+self.y1
