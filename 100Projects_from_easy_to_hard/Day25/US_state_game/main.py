from state import Stategoto
import turtle
import pandas
import time
screen = turtle.Screen()
screen.title("U.S. State Game")
screen.bgpic("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
x = 0
statenames, xcord, ycord = data.state.to_list(), data.x.to_list(), data.y.to_list()
y = len(statenames)
game_is_on = True
while game_is_on:
    state = screen.textinput(title=f"{x}/{y}State", prompt=("Enter a state name.")).title()
    if state in statenames:
        x +=1
        a = statenames.index(state)
        stategoto = Stategoto(xcord[a], ycord[a], state)
        statenames.pop(a)
        xcord.pop(a)
        ycord.pop(a)
        time.sleep(1)
        
    if statenames == []:
        stategoto = Stategoto(0, 0, "You Won the game.")
        game_is_on = False
    
    if state == "Exit":break
remaining = pandas.DataFrame({
    "state":statenames,
    "x":xcord,
    "y":ycord
})

remaining.to_csv("missing_states.csv")
print("States that You missed")
print(pandas.read_csv("missing_states.csv"))
screen.exitonclick()