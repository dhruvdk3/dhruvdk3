# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
i = 0
while(True):
    if right_is_clear():
        turn_right()
        move()
        i+=1
        if i ==3:
            if front_is_clear():
                move()
            else:
                turn_left()
    elif front_is_clear():
        move()
    else:
        turn_left()
    if i == 3: 
        i = 0
    if at_goal():
        break
    
