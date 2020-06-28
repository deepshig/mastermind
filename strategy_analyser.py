from codemaker import CodeMaker
from mathematician_codebreaker import MathematicianCodeBreaker
from logician_codebreaker import LogicianCodeBreaker
from random_codebreaker import RandomCodeBreaker
from knowledge_manager import KnowledgeManager
from game import NUMBER_OF_CHANCES
from printer import print_simulation_results

NUMBER_OF_SIMULATIONS = 20


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

        self.mathematician_codebreaker_score = 0
        self.logician_codebreaker_score = 0
        self.random_codebreaker_score = 0

    def __play(self, codebreaker):
        """
        Provides interface to conduct the game.
        Provides opportunities to the code-breaker to
        make moves, passes them to code-maker, gets the feedback
        and passes it to the code-breaker, to get the next move.
        Also, keeps track of the winner for the game, and updates
        the scores accordingly.
        """
        feedback = self.__handle_first_move(codebreaker)

        if self.__codebreaker_won(feedback, codebreaker):
            return

        for i in range(2, NUMBER_OF_CHANCES+1):
            next_move = codebreaker.get_next_move(feedback)
            feedback = self.codemaker.analyze_move(next_move)

            self.__update_knowledge(next_move, feedback)

            if self.__codebreaker_won(feedback, codebreaker):
                return

        return

    def __handle_first_move(self, codebreaker):
        """
        Handles the first move for the game.
        Gets the move from code-breaker, passes it
        onto the code-maker, and gets feedback from it.
        """
        first_move = codebreaker.get_first_move()
        feedback = self.codemaker.analyze_move(first_move)

        self.__update_knowledge(first_move, feedback)
        return feedback

    def __update_knowledge(self, move, feedback):
        """
        Updates the knowledge model of the game, with
        the knowledge acquired from this move and its feedback.
        """
        self.knowledge_manager.handle_move(move, feedback)
        return

    def __codebreaker_won(self, feedback, codebreaker):
        """
        Checks if the codebreaker has correctly
        guessed the secret code, and won the game.
        If yes, updates the score accordingly.
        """
        for val in feedback:
            if val == 0 or val == -1:
                return False

        self.__update_score(codebreaker)
        return True

    def __update_score(self, codebreaker):
        """
        Checks the type of the code-breaker
        and updates the score by 1 accordingly.
        """
        if (isinstance(codebreaker, MathematicianCodeBreaker)):
            self.mathematician_codebreaker_score = self.mathematician_codebreaker_score + 1
            return

        if (isinstance(codebreaker, LogicianCodeBreaker)):
            self.logician_codebreaker_score = self.logician_codebreaker_score + 1
            return

        if (isinstance(codebreaker, RandomCodeBreaker)):
            self.random_codebreaker_score = self.random_codebreaker_score + 1

    def run_simulation(self):
        """
        Runs the strategy analyser simulation.
        Allows 'n' games to be played, with new instances
        of all the players and the knowledge model
        for each game.
        """
        for i in range(0, self.number_of_games):
            self.knowledge_manager = KnowledgeManager()
            self.codemaker = CodeMaker()

            print("Running Game : ", i+1, " : Code : ", self.codemaker.code)

            self.mathematician_codebreaker = MathematicianCodeBreaker()
            self.logician_codebreaker = LogicianCodeBreaker(
                self.knowledge_manager)
            self.random_codebreaker = RandomCodeBreaker()

            self.__play(self.mathematician_codebreaker)
            self.__play(self.logician_codebreaker)
            self.__play(self.random_codebreaker)
        return


def main():
    analyser = StrategyAnalyser(NUMBER_OF_SIMULATIONS)
    analyser.run_simulation()
    print_simulation_results(analyser)


if __name__ == "__main__":
    main()
