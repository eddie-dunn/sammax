import random
import math

class BoatSim():

    def __init__(self, boat):
        self.winner = 0
        self.draw = 0
        self.turn = 0
        self.boat = boat

    def run(self):
        boat = self.boat
        if self.winner == 0 and self.draw == 0:
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
                
    def run2(self):
        dt = .01
        boat = self.boat[0]
        acc_fact_max = 10.0
        ret_fact = 50.0
        turn_fact = 1.0
        turn_max = 15.0
        if boat.x != boat.targetheadingx or boat.y != boat.targetheadingy:
            #Adjust heading
            dist = math.sqrt((boat.targetheadingx - boat.x)*(boat.targetheadingx - boat.x) + (boat.targetheadingy - boat.y)*(boat.targetheadingy - boat.y))
            angleTarget =math.degrees(math.atan2(boat.targetheadingx - boat.x, boat.targetheadingy - boat.y))
            angleBow = math.degrees(math.atan2(boat.ix,boat.iy))
            
            diffA = angleTarget-angleBow
            if diffA > turn_max:
                diffA = turn_max
            if diffA < -turn_max:
                diffA = turn_max
            boat.ix = math.cos(math.radians(diffA*dt + angleBow))
            boat.iy = math.sin(math.radians(diffA*dt + angleBow))
            
            # Calc total acceleration
            if dist > acc_fact_max:
                dist = acc_fact_max
            accX = dist*math.cos(angleBow) - ret_fact*boat.dx*boat.dx
            accY = dist*math.sin(angleBow) - ret_fact*boat.dy*boat.dy
            
            # Update velocity
            boat.dx = boat.dx + accX*dt
            boat.dy = boat.dy + accY*dt
            
            # Update position   
            boat.x = boat.x + boat.dx
            boat.y = boat.y + boat.dy
                
            boat.drawx = math.floor(boat.x)
            boat.drawy = math.floor(boat.y)
                
                
                
                
                
                
                
                
                
                
