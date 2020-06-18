import random
import time

LENGTH_OF_CODE = 4


class CodeMaker:
    """
    CodeMaker generates the code for each game.
    There are no repetitions allowed in the code, and the move.
    It also gives a feedback on each move of the CodeBreaker, and maintains its own knowledge
    """

    def __init__(self):
        self.__generate_code()

    def __generate_code(self):
        self.code = []
        available_choices = [1, 2, 3, 4, 5, 6]

        random.seed(time.time_ns())
        for _ in range(0, LENGTH_OF_CODE):
            val = random.choice(available_choices)
            self.code.append(val)
            available_choices.remove(val)

    def analyze_move(self, move):
        """
        Analyse the code-breaker's move and generate feedback
        Feedback = 1, if element in the move matches the code at index i
        Feedback = 0, if element in the move occurs in the code, but not at index i
        Feedback = -1, if element in the move does not occur in the code at all
        """
        feedback = [-1, -1, -1, -1]

        for i in range(0, LENGTH_OF_CODE):
            if self.code[i] == move[i]:
                feedback[i] = 1
            elif self.code.count(move[i]) == 1:
                feedback[i] = 0
            else:
                feedback[i] = -1

        return feedback
