from dasboot import *
from boatsim import *
from boatgfx import *
from eventstruct import *

def main():

    boat = [DasBoot(20, 20, 100, 200, 200), DasBoot(10, 20, 200, 0, 200)]
    from collections import deque
    event_stack = deque([])


    #~ Initilizing needed objects
    sim_obj = BoatSim(event_stack, boat)
    sim_gfx = BoatGfx(event_stack, boat)

    #~ Main loop
    while 1:
        #~ Handle events
        sim_gfx.handleEvents()
        #~ "Ett steg i simulationen"
        sim_obj.run()
        #~ Draw
        sim_gfx.drawToBuffer()
        sim_gfx.drawToScreen()
        
        pygame.time.wait(20)


if __name__ == '__main__':
    main()
