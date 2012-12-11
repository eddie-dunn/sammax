import math

def moveBoats(self.dest_x, self.dest_y, self.boat_cnt=0):

    while self.steps_taken < self.boat[self.boat_cnt].spd:

        #~ Calculate the distance and angle from the boat's current position to its destination
        dist_x = self.boat[self.boat_cnt].drawx - self.dest_x
        dist_y = self.boat[self.boat_cnt].drawy - self.dest_y
        self.boat[self.boat_cnt].angle_to_dest = math.degrees(math.atan2(dist_x, dist_y))

        #~ If the boat is not pointing in the right direction, turn MANEUVER degrees towards destination.
        #~ If MANEUVER is greater than difference of actual heading and desired heading, set heading to
        #~ desired heading
        if self.boat[self.boat_cnt].heading != self.boat[self.boat_cnt].angle_to_dest:
            if abs(self.boat[self.boat_cnt].angle_to_dest-self-boat[self.boat_cnt].heading) < self.boat[self.boat_cnt].maneuver
                self.boat[boat_cnt].heading = self.boat[boat_cnt].angle_to_dest
            else:
                if self.boat[self.boat_cnt].heading < self.boat[self.boat_cnt].angle_to_dest:
                    self.boat[self.boat_cnt].heading += self.boat[self.boat_cnt].maneuver
                else:
                    self.boat[self.boat_cnt].heading -= self.boat[self.boat_cnt].maneuver

        #~ Calculate how much of the boat's speed will be in x and y, based on its new heading
        self.x_comp = sin(self.boat[self.boat_cnt].heading)*self.boat[self.boat_cnt].spd
        self.y_comp = cos(self.boat[self.boat_cnt].heading)*self.boat[self.boat_cnt].spd

        #~ Check if the boat is closer to its destination than x_comp and y_comp and update its position
        #~ accordingly
        if abs(self.dest_x-self.boat[self.boat_cnt].drawx) <= self.x_comp and abs(self.dest_y-self.boat[self.boat_cnt].drawy) <= self.y_comp:
            self.boat[self.boat_cnt].drawx = self.dest_x
            self.boat[self.boat_cnt].drawy = self.dest_y
            self.steps_taken = self.boat[self.boat_cnt].spd
        else:
            self.boat[self.boat_cnt].drawx -= self.x_comp
            self.boat[self.boat_cnt].drawy -= self.y_comp

        self.steps_taken += 1
        self.run()
        pygame.time.wait(40)
