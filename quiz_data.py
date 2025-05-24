from questions import Question

class QuizData:
    def load_quiz(filename):
        questions = []
        with open(filename, 'r') as file:
            lines = file.readlines()

        current_question = None
        options = {}
        correct_option = None

        for line in lines:
            line = line.strip()
            if not line:
                continue
            elif line.startswith("Quiz name:"):
                continue
            elif line.startswith("Correct answer:"):
                correct_option = line.split(":")[1].strip()
                questions.append(Question(current_question, options, correct_option))
                current_question = None
                options = {}
            elif line[1:3] == ") ": 
                key = line[0]
                value = line[3:]
                options[key] = value
            else:
                current_question = line 

        return questions