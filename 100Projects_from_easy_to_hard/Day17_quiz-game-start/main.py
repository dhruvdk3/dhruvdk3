from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
Question_Bank = [Question(i["question"], i["correct_answer"]) for i in question_data]
quiz = QuizBrain(Question_Bank)
while quiz.still_has_question():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score was : {quiz.score}/{quiz.question_no}")