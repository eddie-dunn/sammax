
from dasboot import *
from boatsim import *
from boatgfx import *

def main():
	"Meckar upp ett fonster med lite skrap i"
	
	"""Spelar ett ljud jag hittade pa www.soundbible.com
	Bonuskommentar: om man skriver svenska vokaler i kommentarerna
	far man felmeddelanden nar man kor"""
			
	"Changed to list"
	boat = [DasBoot(20, 20, 100, 5, 5,), DasBoot(10, 20, 200, 25, 25)]
	
	"Skapar en sim och ett fonster"
	sim_obj = BoatSim(boat)
	sim_win = BoatGfx(boat)
	
	"Main thing, game runs until one or both ships are destroyed or all ammo is gone"
	print "boat1", "boat2", "turn"
	print boat[0].h, boat[1].h
	
	"Alltid true, kor sim och uppdatera fonster"
	while 1:
		"Ett steg i simulationen"
		sim_obj.run()
		"En uppdatering av fonstret"
		sim_win.run()


if __name__ == '__main__':
	main()
