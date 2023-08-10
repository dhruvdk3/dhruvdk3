from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    title_lable.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global reps
    reps = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    
    if reps%2 == 0:
        if reps%8==0:
            cowndown(LONG_BREAK_MIN*60)
            title_lable.config(text="Break",font=(FONT_NAME, 48,"bold"), fg=RED, bg=YELLOW)
        else:
            cowndown(SHORT_BREAK_MIN*60)
            title_lable.config(text="Break",font=(FONT_NAME, 48,"bold"), fg=PINK, bg=YELLOW)
    else:
        cowndown(WORK_MIN*60)
        title_lable.config(text="Work",font=(FONT_NAME, 48,"bold"), fg=GREEN, bg=YELLOW)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def cowndown(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = "0" + str(count_min)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, cowndown, count-1)
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark +="✔"
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

checkmark = Label(text="", fg=GREEN, bg=YELLOW)
title_lable = Label(text="Timer",font=(FONT_NAME, 48,"bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(row=3,column=1)
title_lable.grid(row=0, column=1)

canvas = Canvas(height=223, width=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)


window.mainloop()