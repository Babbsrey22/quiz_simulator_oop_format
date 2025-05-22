from questions import Question

class QuizData:
    def load_quiz(self, filename):
        with open(filename, 'r') as file:
            content = file.read()

        blocks = content.strip().split("\n\n")[1:]
        questions = []

        for block in blocks:
            lines = block.strip().split("\n")
            if len(lines) < 6:
                print(block)
                continue

            quiz_data = {}

            quiz_data['question'] = lines[0]
            quiz_data['a'] = lines[1][3:].strip()
            quiz_data['b'] = lines[2][3:].strip()
            quiz_data['c'] = lines[3][3:].strip()
            quiz_data['d'] = lines[4][3:].strip()

            try:
                quiz_data['answer'] = lines[5].split(": ")[1].strip()
            except IndexError:
                print("Malformed answer line! They're not gonna like this..." \
                "\nOhhh... they're not gonna like this AT ALL.")
                print(block)
                continue

            questions.append(quiz_data)

        return questions

