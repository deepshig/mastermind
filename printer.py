def print_code(game):
    print("++++++++++++++++++++++++")
    print("CODE : ", *game.codemaker.code, sep=" ")
    print_knowledge(game, False)
    print("++++++++++++++++++++++++")


def print_game_state(i, move, feedback, game):
    print("++++++++++++++++++++++++")
    print("Move :", i, ": ", *move, sep=" ")
    print("Feedback : ", *feedback, sep=" ")
    print_knowledge(game)
    print("++++++++++++++++++++++++")


def print_winner(winner):
    print("++++++++++++++++++++++++")
    print("WINNER : ",  winner)
    print("++++++++++++++++++++++++")


def print_knowledge(game, print_worlds=True):
    print("Total worlds possible after this move : ",
          len(game.knowledge_manager.model.worlds))
    print()

    if print_worlds:
        for w in game.knowledge_manager.model.worlds:
            print(w.name, w.assignment)

    print()
    print("Real World : ", game.knowledge_manager.real_world)
    print("Number of Relations for Agent 1 : ",
          len(game.knowledge_manager.model.relations['1']))
    print("Number of Relations for Agent 2 : ",
          len(game.knowledge_manager.model.relations['2']))
    print()

    print("Code Maker Knowledge : ", game.agent_knowledge.agent1)
    print("Code Breaker Knowledge : ", game.agent_knowledge.agent2)
    print("Common Knowledge : ", game.agent_knowledge.common_knowledge)


def print_simulation_results(strategy_analyser):
    print("++++++++++++++++++++++++")
    print("Total games run for each strategy : ",
          strategy_analyser.number_of_games)
    print()

    print("Games won by Mathematician Code Breaker : ",
          strategy_analyser.mathematician_codebreaker_score)
    print("Games won by Logician Code Breaker : ",
          strategy_analyser.logician_codebreaker_score)
    print("Games won by Random Code Breaker : ",
          strategy_analyser.random_codebreaker_score)
    print("++++++++++++++++++++++++")
