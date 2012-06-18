from dasboot import *
from boatsim import *
from boatgfx import *

def main():

    boat = [DasBoot(20, 20, 100, 200, 200), DasBoot(10, 20, 200, 0, 200)]


    #~ "Skapar en sim och ett fonster"
    sim_obj = BoatSim(boat)
    sim_win = BoatGfx(boat)

    #~ "Alltid true, kor sim och uppdatera fonster"
    while 1:
        #~ # Handle events
        sim_win.handleEvents()
        #~ "Ett steg i simulationen"
        #~ sim_obj.run()
        #~ #En uppdatering av fonstret
        #~ sim_win.run()


if __name__ == '__main__':
    main()
