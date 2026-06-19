import random
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#TODO question_bank = [Question(**question) for question in question_data] - code from AI intellisense. Gotta ask how operator ** works.
question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
   quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")