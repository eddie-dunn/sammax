from newBoat import *
from boatgfx import *

def main():

    boat = newBoat()

    #~ Initilizing needed objects
    sim_gfx = BoatGfx(boat)

    #~ Main loop
    while 1:
        #~ Handle events
        sim_gfx.handleEvents()
        #~ Update boat
        boat.turn_towards_destination()
        boat.move()

        #~ Draw
        sim_gfx.drawToBuffer()
        sim_gfx.drawToScreen()

        pygame.time.wait(30)


if __name__ == '__main__':
    main()
