
import math

class ChangeHeading (start_pos, target_pos, current_heading, max_turn)

    new_heading = 0

    angle_to_goal = math.degrees(math.atan2(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))

    if angle_to_goal < 0
        if abs(angle_to_goal) < max_turn
            new_heading = current_heading - (abs(angle_to_goal - max_turn))
        else
            new_heading = current_heading - max_turn
    if angle_to_goal > 0
        if abs(angle_to_goal) < max_turn
            new_heading = current_heading + (abs(angle_to_goal - max_turn))
        else
            new_heading = current_heading + max_turn
