#######################################################################
#Sammax - CurveCalculator.py
#Calculates curves
#Copyright Thomas Ring, Erik Trygg, Eddie Dunn 2012
#######################################################################

import math

class CurveCalculator():

    def calcCurve(start_pos, end_pos, speed, start_heading, turnrate)
        pos = start_pos
        heading = start_heading
        out_vector[]
        step = 0

        while step < 10:
            angleToGoal = math.degrees(math.atan2(end_pos[0] - pos[0], end_pos[1] - pos[1]))

            if angleToGoal < 0
                heading = heading - turnrate
            if angleToGoal > 0
                heading = heading + turnrate

            pos[0] = pos[0] + speed*cos(heading)
            pos[1] = pos[1] + speed*sin(heading)

            out_object = [pos[0], pos[1], heading]
            out_vector.append(out_object)

            step = step + 1
