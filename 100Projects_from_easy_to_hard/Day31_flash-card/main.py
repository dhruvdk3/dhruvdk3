from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#------------------------------- DATA --------------------------------#
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text = current_card["French"], fill="black")
    canvas.itemconfig(card_image, image = card_front_image)
    flip_timer = window.after(3000,flip_card)
    

#--------------------------- Flip Card -------------------------------#
def flip_card():
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(card_text, text = current_card["English"],fill = "white")
    canvas.itemconfig(card_image, image = flip_image)
    
#----------------------------------------------------------------------#

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()



#-------------------------------- UI ---------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(0,next_card)
#------------------------- Card Image Design --------------------------#

canvas = Canvas(height=526,width=800)
card_front_image = PhotoImage(file="images/card_front.png")
flip_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400,263,image = card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card_text = canvas.create_text(400, 260, text="Word", font=("Ariel", 60, "bold"), fill="black")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row = 0, columnspan=2)


# -------------------------- Button Design ---------------------------#
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)

right_button.grid(column=1, row=1)

window.mainloop()