import time

class QuizCreator:
    def create_quiz(self):
        print("Loading QUiz Creator....\n")

        quiz_name = input("Enter the name of this quiz: ")
        quiz_filename = f"{quiz_name}.txt"

        quiz_questions = []

        while True:
            question = input(f"\nPress 0 to exit\nEnter question: ")
            if question == "0":
                print("Stopping Quiz Creator....")
                break

            choice_a = input("Option a: ")
            choice_b = input("Option b: ")
            choice_c = input("Option c: ")
            choice_d = input("Option d: ")

            while True:
                    correct_answer = input("Enter the correct option (a/b/c/d): ")
                    if correct_answer in ["a", "b", "c", "d"]:
                        break
                    else:
                        print("Please... enter a valid option. Please.")
            
            quiz_content = (
                f"{question}\n"
                f"a) {choice_a}\n"
                f"b) {choice_b}\n"
                f"c) {choice_c}\n"
                f"d) {choice_d}\n"
                f"Correct answer: {correct_answer}\n\n"
            )
            quiz_questions.append(quiz_content)

            with open(quiz_filename, "w") as file:
                file.write(f"Quiz name: {quiz_name}\n\n")
                for items in quiz_questions:
                    file.write(items)
                    file.write("\n\n")
            
            time.sleep(1)
            print("Quiz saved successfully!!!!")