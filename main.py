import random
from dasboot import *

def main():
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
