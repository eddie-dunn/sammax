import os, sys, pygame
from pygame.locals import *
import random
from dasboot import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
	"Meckar upp ett fonster med lite skrap i"
	
	pygame.init()
	
	size = width, height = 800,800
	backg = 0,0,0
	
	screen = pygame.display.set_mode(size)
	
	boatpic = pygame.image.load("boat.jpg")
	
	x = 0
	y = 0
	x1 = 1
	y1 = 1
	
	"""Spelar ett ljud jag hittade pa www.soundbible.com
	Bonuskommentar: om man skriver svenska vokaler i kommentarerna
	far man felmeddelanden nar man kor"""
	
	sound = pygame.mixer.Sound("geese.mp3")
	
	sound.play()
	
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		backg = x%255, y%255, ((x+y)%255)
		screen.fill(backg)
		screen.blit(boatpic,(x,y))
		pygame.display.flip()
		
		if x == width:
			x1 = -1
		elif x == 0:
			x1 = 1
		if y == height:
			y1 = -1
		elif y == 0:
			y1 = 1
	
		x = x+x1
		y = y+y1
	"Changed to list"
	boat = [DasBoot(20, 20, 100, 5, 5,), DasBoot(10, 20, 200, 25, 25)]
	
	"Tracking variables"
	turn = 0
	winner = 0
	draw = 0
	
	"Main thing, game runs until one or both ships are destroyed or all ammo is gone"
	print "boat1", "boat2", "turn"
	print boat[0].h, boat[1].h
	while winner == 0 and draw == 0:
		turn = turn+1
		if boat[1].ammostash > 0:
			boat[0].h = boat[0].h-random.randint(0, boat[1].d)
			boat[1].ammostash = boat[1].ammostash-1
		else:
			print "Boat 2 No ammo!"
		if boat[0].ammostash > 0:
			boat[1].h = boat[1].h-random.randint(0, boat[0].d)
			boat[0].ammostash = boat[0].ammostash-1
		else:
			print "Boat 1 No ammo!"
		print boat[0].h, boat[1].h, turn
		if boat[0].h <= 0 and boat[1].h > 0:
			winner = 2
			print "Boat 2 wins!"
		if boat[1].h <= 0 and boat[0].h > 0:
			winner = 1
			print "Boat 1 wins!"
		if winner == 0 and boat[0].ammostash == 0 and boat[1].ammostash == 0:
			draw = 1
			print "Draw!"
		

if __name__ == '__main__':
	main()
