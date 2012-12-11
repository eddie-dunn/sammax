import math
import random

class newBoat:

    def __init__(self, x=400, y=400, destination=(400,400), speed = 10, heading=0, max_turn=5, picpath="pil.png"):

        # Initialized variables
        self.location = (x, y)
        self.destination = destination
        self.speed = speed
        self.heading = heading
        self.max_turn = max_turn
        self._picpath = picpath

    @property
    def image_path(self):
        """Return filepath of boat's image sprite."""
        return self._picpath

    @property
    def location(self):
        """Return the location of the boat"""
        return self.location

    @property
    def heading(self):
        """Return the heading of the boat"""
        return self.heading


    def change_heading(self, change_degrees):
        self.heading = self.heading + change_degrees
        print self.heading

    def set_heading(self, new_heading):
        self.heading = new_heading

    def set_position(self, new_x, new_y):
        self.location[0] = new_x
        self.location[1] = new_y

    def set_destination(self, new_destination):
        self.destination = new_destination
        print self.destination

    def turn_towards_destination(self):

        self.angle_to_goal = math.degrees(math.atan2(self.destination[1] - self.location[1], self.destination[0] - self.location[0]))

        self.angle_to_goal = -1*self.angle_to_goal + 90

        #Remap angle_to_goal so that 0 degrees is "up"
        #~
        #~ if self.angle_to_goal == 0:
            #~ self.angle_to_goal = 90
        #~ elif self.angle_to_goal == -90:
            #~ self.angle_to_goal = 0
        #~ elif self.angle_to_goal == 90:
            #~ self.angle_to_goal = 180
        #~ elif self.angle_to_goal == -180:
            #~ self.angle_to_goal = 270
        #~ elif self.angle_to_goal == 180:
            #~ self.angle_to_goal = 270
#~
        #~ elif -90 < self.angle_to_goal < 0:
            #~ self.angle_to_goal = 90 + self.angle_to_goal
        #~ elif -180 < self.angle_to_goal < -90:
            #~ self.angle_to_goal = 270 + (180+self.angle_to_goal)
        #~ elif self.angle_to_goal > 0:
            #~ self.angle_to_goal = self.angle_to_goal + 90
#~
        #Determine which direction the boat should turn

        self.heading_difference = self.angle_to_goal - self.heading

        if self.heading_difference > 180 :
            self.heading_difference = self.heading_difference - 360
        elif self.heading_difference < -180 :
            self.heading_difference = self.heading_difference + 360

        if self.heading_difference > 0 :
            if self.heading_difference < self.max_turn:
                self.heading = self.angle_to_goal
            else:
                self.heading = self.heading + self.max_turn

        elif self.heading_difference < 0:
            if self.heading_difference > self.max_turn:
                self.heading = self.angle_to_goal
            else:
                self.heading = self.heading - self.max_turn

 #       elif 180 < self.heading_difference < 360:
 #           self.heading = self.heading + self.max_turn

            #print "angle > 0"
        if self.heading > 360:
            self.heading = self.heading - 360
        if self.heading < 0:
            self.heading = self.heading + 360

        print self.heading

    def move(self):

        self.dx = (math.cos(math.radians(self.heading-90))*self.speed)
        self.dy = -1*(math.sin(math.radians(self.heading-90))*self.speed)

        new_location = (self.location[0] + self.dx, self.location[1] + self.dy)

        self.location = new_location

        if abs(self.location[0] - self.destination[0]) < 5 and abs(self.location[1] - self.destination[1]) < 5:
            self.new_destination = (random.randint(0, 800), random.randint(0, 800))
            self.destination = self.new_destination

        print self.dx, self.dy
