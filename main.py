import time
from instructions import Instructions
from quiz_creator import QuizCreator
from quiz_data import QuizData
from questions import Question
from quiz import Quiz

def main_menu():
    print("\nWelcome to the Quiz Simulator!" \
    "\n[1] Instructions" \
    "\n[2] Create Quiz" \
    "\n[3] Take Quiz" \
    "\n[4] Exit Quiz Simulator")

while True:
    main_menu()
    try:
        option = int(input("\nMain menu selection: "))
    except ValueError:
        print("Please enter a valid number from 1-4!! Only those numbers Please.")
        continue

    if option == 1:
        print("Loading instructions....\n")
        time.sleep(2)
        Instructions
    elif option == 2:
        print("Loading Quiz Creator homescreen....\n")
        time.sleep(2)
        creator = QuizCreator()
        creator.create_quiz()
    elif option == 3:
        print("Loading Quiz homescreen....\n")
        time.sleep(2)
        filename = input("Enter quiz filename: ")
        loader = QuizData
        try:
            questions = loader.load_quiz(filename)
            quiz = Quiz(filename, questions)
            quiz.start_quiz()
        except FileNotFoundError:
            print("Nawwww file not found. Please check filename and trytrytrytry again.")
    elif option == 4:
        print("Exiting program.")
        time.sleep(5)
        print("I hope you come back for me soon...")
        break
    else:
        print("Invalid selection. Please pleasepleaseplease try again andagainandagain.")