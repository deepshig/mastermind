from codemaker import CodeMaker
from mathematician_codebreaker import MathematicianCodeBreaker
from knowledge_manager import KnowledgeManager
from agent_knowledge import AgentKnowledge
from printer import print_game_state, print_code, print_winner

NUMBER_OF_CHANCES = 3
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
        self.codebreaker = MathematicianCodeBreaker()

        self.knowledge_manager = KnowledgeManager()
        self.knowledge_manager.get_real_world(self.codemaker.code)

        self.agent_knowledge = AgentKnowledge()
        self.agent_knowledge.update_code_maker_knowledge(self.codemaker.code)

    def play(self):
        feedback = self.__handle_first_move()
        if self.__codebreaker_won(feedback):
            return

        for i in range(2, NUMBER_OF_CHANCES+1):
            next_move = self.codebreaker.get_next_move(feedback)
            feedback = self.codemaker.analyze_move(next_move)
            self.__update_knwoledge(next_move, feedback)
            print_game_state(i, next_move, feedback,
                             self)

            if self.__codebreaker_won(feedback):
                return

        self.winner = CODE_MAKER
        return

    def __handle_first_move(self):
        first_move = self.codebreaker.get_first_move()
        feedback = self.codemaker.analyze_move(first_move)

        self.__update_knwoledge(first_move, feedback)
        print_game_state(1, first_move, feedback,
                         self)

        return feedback

    def __update_knwoledge(self, move, feedback):
        self.knowledge_manager.handle_move(move, feedback)
        self.agent_knowledge.update_move_knowledge(move, feedback)
        return

    def __codebreaker_won(self, feedback):
        for val in feedback:
            if val == 0 or val == -1:
                return False

        self.winner = CODE_BREAKER
        return True


def main():
    game = Game()
    print_code(game)

    game.play()
    print_winner(game.winner)


if __name__ == "__main__":
    main()
