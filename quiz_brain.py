class QuizBrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def question_num(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.text} (True/False)?: ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current Score is: {self.score}/{self.question_no}")
        print("\n")
