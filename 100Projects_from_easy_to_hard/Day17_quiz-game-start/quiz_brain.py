class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_list
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no +=1
        user_ans = input(f"Q.{self.question_no} : {current_question.text} (True/False) : ").title()
        self.check_answer(user_ans, current_question.answer)
        print("\n")
        
    def still_has_question(self):
        return len(self.question_list) > self.question_no
    
    def check_answer(self,user_ans, ans):
        if user_ans == ans:
            self.score+=1
            print(f"You got it right!\nThe correct answer was: {ans}.\nYour current score is: {self.score}/{self.question_no}")
        else : print(f"That's wrong.\nThe correct answer was: {ans}.\nYour current score is: {self.score}/{self.question_no}")