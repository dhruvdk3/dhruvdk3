from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_lable = Label(text=f"Score : 0", bg=THEME_COLOR, fg="white")
        self.score_lable.grid(row=0, column=1, padx=20, pady=20)
        
        self.canvas = Canvas(height=250, width=300, bg="white",highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,width=280, text="hello", font=("Arial", 20, "italic"), fill="black")
        self.canvas.grid(row=1,column=0, columnspan=2, padx=20, pady=20)
        
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true = Button(image=true_image, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.check_ans_true)
        self.true.grid(row=2, column=0, padx=20, pady=20)
        self.false = Button(image=false_image, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.check_ans_false)
        self.false.grid(row = 2, column=1, padx=20, pady=20)
        self.get_next_question()
        
        
        self.window.mainloop()

    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You have reached the end of the quiz.")
            self.false.config(state="disabled")
            self.true.config(state="disabled")

    
    def check_ans_true(self):
        self.feedback(self.quiz.check_answer("True"))
        self.score_lable.config(text=f"Score : {self.quiz.score}")
        
    def check_ans_false(self):
        self.feedback(self.quiz.check_answer("False"))
        self.score_lable.config(text=f"Score : {self.quiz.score}")
    
    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else : 
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)