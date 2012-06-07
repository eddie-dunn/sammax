import random
from dasboot import *

def main():
	boat1 = DasBoot(10, 100, 5, 5,)
	boat2 = DasBoot(10, 200, 25, 25)
		
	print "boat1", "boat2"
	while boat1.h > 0 and boat2.h > 0:
		print boat1.h, boat2.h
		boat1.h = boat1.h-random.randint(0, boat2.d)
		boat2.h = boat2.h-random.randint(0, boat1.d)
	print boat1.h, boat2.h
		

if __name__ == '__main__':
	main()
