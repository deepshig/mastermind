import array as arr


class CodeMaker:
    """
    CodeMaker generates the code for each game.
    There are no repetitions allowed in the code, and the move.
    It also gives a feedback on each move of the CodeBreaker, and maintains its own knowledge
    """

    def __init__(self):
        self.__generate_code()

    def __generate_code(self):
        self.code = arr.array('i', [1, 2, 3, 4])

    def analyze_move(self, move):
        feedback = arr.array('i', [-1, -1, -1, -1])

        for i in range(0, 4):
            if self.code[i] == move[i]:
                feedback[i] = 1
            elif self.code.count(move[i]) == 1:
                feedback[i] = 0
            else:
                feedback[i] = -1

        return feedback
