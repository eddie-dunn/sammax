from dasboot import *
from boatsim import *
from boatgfx import *

def main():

    boat = [DasBoot(20, 20, 100, 0, 0,), DasBoot(10, 20, 200, 0, 200)]

    #~ "Skapar en sim och ett fonster"
    sim_obj = BoatSim(boat)
    sim_win = BoatGfx(boat)

    #~ "Main thing, game runs until one or both ships are destroyed or all ammo is gone"
    print "boat1", "boat2", "turn"
    print boat[0].h, boat[1].h

    #~ "Alltid true, kor sim och uppdatera fonster"
    while 1:
        #~ "Ett steg i simulationen"
        sim_obj.run()
        #En uppdatering av fonstret
        sim_win.run()


if __name__ == '__main__':
    main()
