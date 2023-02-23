from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []  # we need a list to store question objects
for question in question_data:  # creating question objects and adding them in list
    question_text = question["question"]  # dict["key"] gives value and question data is list of dictionary called
    # question so use question to find value for given key
    question_answer = question["correct_answer"]

    new_question = Question(question_text, question_answer)  # creating object using class Question
    question_bank.append(new_question)  # adding new questions in the list

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.input()

print(f"\nYour final score for quizbrain game  is {quiz_brain.score}/{quiz_brain.length}")