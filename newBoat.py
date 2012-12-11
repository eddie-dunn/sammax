import math

class newBoat:

    def __init__(self, x=0, y=0, destination=(0,0), speed = 10, heading=0, max_turn=5, picpath="boat.jpg"):

        # Initialized variables
        self.x = x
        self.y = y
        self.destination = destination
        self.speed = speed
        self.heading = heading
        self.max_turn = max_turn
        self._picpath = picpath

    def do_step():
        self.turn_towards_destination()
        self.move()

    def change_heading(change_degrees):
        self.heading = self.heading + change_degrees

    def set_heading(new_heading):
        self.heading = new_heading

    def set_position(new_x, new_y):
        self.x = new_x
        self.y = new_y

    def set_destination(new_destination):
        self.destination = new_destination

    def turn_towards_destination():

        self.angle_to_goal = math.degrees(math.atan2(self.destination[0] - self.x, self.destination[1] - self.y))

        if self.angle_to_goal < 0
            if abs(self.angle_to_goal) < self.max_turn
                self.heading = self.heading - (abs(self.angle_to_goal - self.max_turn))
            else
                self.heading = self.heading - max_turn

        if self.angle_to_goal > 0
            if abs(self.angle_to_goal) < self.max_turn
                self.heading = self.heading + (abs(self.angle_to_goal - self.max_turn))
            else
                self.heading = self.heading + self.max_turn

    def move():

        self.dx = math.cos(self.heading)*self.speed
        self.dy = math.sin(self.heading)*self.speed

        self.x = self.x + self.dx
        self.y = self.y + self.dy
