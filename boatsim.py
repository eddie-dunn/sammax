import random
import math
from eventstruct import *

class BoatSim():

    def __init__(self, event_stack, boat):
        self.winner = 0
        self.draw = 0
        self.turn = 0
        self.boat = boat
        self.event_stack = event_stack

        #~ print "boat1", "boat2", "turn"
        #~ print boat[0].h, boat[1].h

    def run(self):
		#~ "Check if there are any new events in stack"
		for i in range(len(self.event_stack)):
			E = self.event_stack.popleft()
			if E.getTarget() in self.boat:
				i = self.boat.index(E.getTarget())
				self.boat[i].order.append(E)

		
		
		#~ Update everything based on object.order
		#~ Boats:
		for i in range(len(self.boat)):
			action_boat(self.boat[i])
					

        #~ boat = self.boat
        #~ if self.winner == 0 and self.draw == 0:
            #~ self.turn = self.turn+1
            #~ if boat[1].ammostash > 0:
                #~ boat[0].h = boat[0].h-random.randint(0, boat[1].d)
                #~ boat[1].ammostash = boat[1].ammostash-1
            #~ else:
                #~ print "Boat 2 No ammo!"
            #~ if boat[0].ammostash > 0:
                #~ boat[1].h = boat[1].h-random.randint(0, boat[0].d)
                #~ boat[0].ammostash = boat[0].ammostash-1
            #~ else:
                #~ print "Boat 1 No ammo!"
            #~ print boat[0].h, boat[1].h, self.turn
            #~ if boat[0].h <= 0 and boat[1].h > 0:
                #~ self.winner = 2
                #~ print "Boat 2 wins!"
            #~ if boat[1].h <= 0 and boat[0].h > 0:
                #~ self.winner = 1
                #~ print "Boat 1 wins!"
            #~ if self.winner == 0 and boat[0].ammostash == 0 and boat[1].ammostash == 0:
                #~ self.draw = 1
                #~ print "Draw!"

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

def action_boat(boat):
	#~  Clean up used events & Remove doubles.
	clean_event_array(boat.order)
	
	#~ Static function
	for i in range(len(boat.order)):
		E = boat.order[i]
		
		#~ ############################
		#~ Movement
		#~ ############################
		if(E.getKey() == "_move_here_"):
			coord = E.getValues()
			if(E.isActive() == 0):
				#~ Calculate direction to go in
				dif_x = coord[0] -boat.x
				dif_y = coord[1] - boat.y
				angle = math.atan2(dif_x, dif_y)
				boat.dx = math.sin(angle)
				boat.dy = math.cos(angle)
				boat.ix = boat.dx
				boat.iy = boat.dy
				E.setActive(1)
				steps_needed = round((math.sqrt(dif_x*dif_x + dif_y*dif_y)), 0)
				#~ print steps_needed
				#~ print math.degrees(angle)
			
			#~  Move one step
			boat.x += boat.dx*boat.spd
			boat.y += boat.dy*boat.spd
			boat.drawx = boat.x
			boat.drawy = boat.y
			
			#~ Stop boat
			if boat.dx > 0.0 and boat.x - coord[0] > 0 or boat.dy > 0.0 and boat.y - coord[1] > 0:
				boat.dx = 0
				boat.dy = 0
				E.setActive(-1)
			elif boat.dx < 0.0 and boat.x - coord[0] < 0 or boat.dy < 0.0 and boat.y - coord[1] < 0:
				boat.dx = 0
				boat.dy = 0
				E.setActive(-1)
				
		#~ ############################
		#~ Fire
		#~ ############################
		elif E.getKey() == "_fire_weapon_":
			#~ print "FIRE"
			if boat.FIRE_ACTIVE == 0:
				boat.FIRE_ACTIVE += 1
			E.setActive(-1)
			#~ if(boat.FIRE_ACTIVE > 10):
				#~ boat.FIRE_ACTIVE = 0
				#~ E.setActive(-1)
	
	
	
	
	#~  Turn of fire after 10 frames
	if(boat.FIRE_ACTIVE > 0):
		boat.FIRE_ACTIVE += 1
	if(boat.FIRE_ACTIVE > 10):
		boat.FIRE_ACTIVE = 0

