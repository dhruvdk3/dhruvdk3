# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while(True):
    if front_is_clear():
        if wall_on_right():
            move()
        elif right_is_clear():
            turn_right()
            move()
    elif wall_on_right():
        turn_left()
    elif wall_in_front():
        if right_is_clear():
            turn_right()
            move()
        elif wall_on_right():
            turn_left()
    if at_goal():
        break
    
