import random

class DasBoot:
	def __init__(self, spd, dmg, hp, xcoord, ycoord):
		self.s = spd
		self.d = dmg
		self.h = hp
		self.x = xcoord
		self.y = ycoord

def main():
	boat1 = DasBoot(10, 30, 100, 5, 5,)
	boat2 = DasBoot(10, 15, 200, 25, 25)
		
	print "boat1", "boat2"
	while boat1.h and boat2.h > 0:
		print boat1.h, boat2.h
		boat1.h = boat1.h-random.randint(0, boat2.d)
		boat2.h = boat2.h-random.randint(0, boat1.d)

if __name__ == '__main__':
	main()
