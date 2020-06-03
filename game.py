from codemaker import CodeMaker
from codebreaker import CodeBreaker
from printer import print_game_state, print_code, print_winner

NUMBER_OF_CHANCES = 5
CODE_MAKER = "Code Maker"
CODE_BREAKER = "Code breaker"


class Game:
    """
    Provides an interface for the code-maker and the code-breaker
    to play the game.
    Passes on the code and feedback from code-maker to the code breaker.
    Passes on the moves from the code-breaker to the code-maker.
    Keeps track of the common knowledge in the game.
    Keeps track of the state of the game and decides the winner.
    """

    def __init__(self):
        self.codemaker = CodeMaker()
        self.codebreaker = CodeBreaker()

    def play(self):
        feedback = self.__handle_first_move()
        if codebreaker_won(feedback):
            self.winner = CODE_BREAKER
            return

        for i in range(2, NUMBER_OF_CHANCES+1):
            next_move = self.codebreaker.get_next_move(feedback)
            feedback = self.codemaker.analyze_move(next_move)
            print_game_state(i, next_move, feedback)

            if codebreaker_won(feedback):
                self.winner = CODE_BREAKER
                return

        self.winner = CODE_MAKER
        return

    def __handle_first_move(self):
        first_move = self.codebreaker.get_first_move()
        feedback = self.codemaker.analyze_move(first_move)
        print_game_state(1, first_move, feedback)
        return feedback


def codebreaker_won(feedback):
    for val in feedback:
        if val == 0 or val == -1:
            return False

    return True


game = Game()
print_code(game.codemaker.code)

game.play()
print_winner(game.winner)
