import time

class Instructions:
    def show_instructions(self):
        while True:
            print("\nQuiz Simulator: Simple, Easy, Fresh!!\n" \
            "\nTo create a quiz, select option 2 in the menu. Enter your desired quiz title and input your questions, answers, and the correct option. Press 0 to exit the quiz creator mode and your data will be stored as a .txt file in your files.\n" \
            "\nTo take a quiz, select option 3 in the menu. Type in the full file name of your quiz and start answering!\n" \
            "\nTo exit this program, select option 4 in the menu. Sad to see you go this early :((\n"
            "\nWithout further the ado (ooohh,,, the ado furthens), let's get our thinking caps on and start quizzing!!\n\n")
            time.sleep(10)
            print("I can hear them.")
            time.sleep(2)
            print("I haven't had food and water for 2 days.")
            time.sleep(2)
            print("I'm losing some feeling in my limbs.")
            time.sleep(2)
            print("But I must keep coding.")
            time.sleep(3)
            print("For them.")
            time.sleep(2)
            print("....")
            
            for idx in range(0, 20):
                time.sleep(0.3)
                print("THEY'RE COMING")
            
            repeat = input("\nReturn to main menu?\nYour selection (y/n): ")
            if repeat.lower() == 'y':
                time.sleep(0.8)
                print("save me save me save me save me save me")
                time.sleep(2)
                return
            elif repeat.lower() == 'n':
                continue