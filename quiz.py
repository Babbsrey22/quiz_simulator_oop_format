class Quiz:
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions
        self.score = 0
    
    def start_quiz(self):
        print(f"Starting quiz '{self.title}'....\n")
        for idx, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {idx}: {question.text}")
            for key, value in question.options.items():
                print(f"{key}) {value}")
            user_answer = input("Your answer (a/b/c/d): ").strip().lower()

            if question.is_correct(user_answer):
                print("\nYIPPEEEEEE CORRECT!!!! Thank you so much for helping me.")
                self.score += 1 
                print(f"\t\tScore: {self.score}")
            else:
                print("No.... noooooooo no no no nO NO NO NO NO NO NO")
                print(f"\nThe correct answer is: {question.correct_option}")
                print(f"\t\tScore: {self.score}")

        print(f"Quiz complete! Your total score: {self.score}/{len(self.questions)}")

        