class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Question number: {self.question_number}")
        try:
            choice = input(f"{current_question.text} (True/False) :  ")
        except EOFError:
            quit()
        self.check_answer(choice, current_question.answer)

    def still_has_question(self, quiz):
        if self.question_number < len(quiz.question_list):
            return True
        else:
            return False

    def check_answer(self, choice, correct_answer):
        if choice == correct_answer:
            self.score += 1
            print(f"Correct Answer: {correct_answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
            return True
        else:
            print(f"Incorrect Answer: {correct_answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
            return False
