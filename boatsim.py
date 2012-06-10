import random

class BoatSim():

    def __init__(self, boat):
        self.winner = 0
        self.draw = 0
        self.turn = 0
        self.boat = boat

    def run(self):
        boat = self.boat
        if not self.winner and not self.draw:
            self.turn = self.turn+1
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
            print boat[0].h, boat[1].h, self.turn
            if boat[0].h <= 0 and boat[1].h > 0:
                self.winner = 2
                print "Boat 2 wins!"
            if boat[1].h <= 0 and boat[0].h > 0:
                self.winner = 1
                print "Boat 1 wins!"
            if self.winner == 0 and boat[0].ammostash == 0 and boat[1].ammostash == 0:
                self.draw = 1
                print "Draw!"
