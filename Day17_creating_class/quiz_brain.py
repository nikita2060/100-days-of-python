# TODO: 1 ASKING THE QUESTIONS
# TODO: 2 CHECKING IF THE ANSWER WAS CORRECT
# TODO: 3  CHECKING IF WE ARE IN THE END OF THE QUIZ


class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def next_question(self):
        self.question_number += 1

    def input(self):
        self.index = self.question_number
        self.question = self.question_bank[self.index]
        answer = input(f"Q.{self.question_number + 1}: {self.question.text}.(True/False)?:").lower()
        self.next_question()
        if answer == self.question.answer.lower():  # writing it inside input method because variables inside these method are
            # useful for checking answer
            self.score += 1
            print("You are right ")
        else:
            print("You are wrong ")
        print(f"The correct answer was: {self.question.answer}.\nYour current score is: {self.score} / {self.index + 1}")

    def still_has_questions(self):  # returns true or false
        self.length = len(self.question_bank)
        return self.question_number < self.length  # we can use !=length, but it will also run if qno is greater and we
        # don't want that
