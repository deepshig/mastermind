from codemaker import CodeMaker
from mathematician_codebreaker import MathematicianCodeBreaker
from logician_codebreaker import LogicianCodeBreaker
from random_codebreaker import RandomCodeBreaker
from knowledge_manager import KnowledgeManager
from game import NUMBER_OF_CHANCES
from printer import print_simulation_results


class StrategyAnalyser:
    """
    Provides an interface for the code-maker and multiple code-breakers
    to play the game. An instance each of mathematician code-breaker,
    logician code-breaker and random code-breaker is created. Each of
    them try to solve the same code genrated by the code-maker.
    Simulation is performed 'n' number of times, and the different
    strategies taken up by each code-breaker are monitored in terms of
    number of codes sucessfully guessed by each.
    Game rules are the same as those in the normal Game class.
    """

    def __init__(self, number_of_games):
        self.number_of_games = number_of_games
        self.knowledge_manager = KnowledgeManager()

        self.codemaker = CodeMaker()
        self.mathematician_codebreaker = MathematicianCodeBreaker()
        self.logician_codebreaker = LogicianCodeBreaker(self.knowledge_manager)
        self.random_codebreaker = RandomCodeBreaker()

        self.mathematician_codebreaker_score = 0
        self.logician_codebreaker_score = 0
        self.random_codebreaker_score = 0

    def __play(self, codebreaker):
        feedback = self.__handle_first_move(codebreaker)

        if codebreaker_won(feedback):
            self.__update_score(codebreaker)
            return

        for i in range(2, NUMBER_OF_CHANCES+1):
            next_move = codebreaker.get_next_move(feedback)
            feedback = self.codemaker.analyze_move(next_move)

            self.__update_knwoledge(next_move, feedback)

            if codebreaker_won(feedback):
                self.__update_score(codebreaker)
                return

        return

    def __handle_first_move(self, codebreaker):
        first_move = codebreaker.get_first_move()
        feedback = self.codemaker.analyze_move(first_move)

        self.__update_knwoledge(first_move, feedback)
        return feedback

    def __update_knwoledge(self, move, feedback):
        self.knowledge_manager.handle_move(move, feedback)
        return

    def __update_score(self, codebreaker):
        if (isinstance(codebreaker, MathematicianCodeBreaker)):
            self.mathematician_codebreaker_score = self.mathematician_codebreaker_score + 1
            return

        if (isinstance(codebreaker, LogicianCodeBreaker)):
            self.logician_codebreaker_score = self.logician_codebreaker_score + 1
            return

        if (isinstance(codebreaker, RandomCodeBreaker)):
            self.random_codebreaker_score = self.random_codebreaker_score + 1

    def run_simulation(self):
        for _ in range(0, self.number_of_games):
            self.__play(self.mathematician_codebreaker)
            self.__play(self.logician_codebreaker)
            self.__play(self.random_codebreaker)
        return


def codebreaker_won(feedback):
    for val in feedback:
        if val == 0 or val == -1:
            return False

    return True


def main():
    analyser = StrategyAnalyser(20)
    analyser.run_simulation()
    print_simulation_results(analyser)


if __name__ == "__main__":
    main()
