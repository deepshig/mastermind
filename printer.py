from termcolor import cprint


def print_code(game):
    print("++++++++++++++++++++++++")

    text = "CODE : " + str(game.codemaker.code)
    cprint(text, "green", attrs=['bold'])

    print_knowledge(game, False)
    print("++++++++++++++++++++++++")


def print_game_state(i, move, feedback, game):
    print("++++++++++++++++++++++++")

    text = "Move : " + str(i) + " : " + str(move)
    cprint(text, "green", attrs=['bold'])

    text = "Feedback : " + str(feedback)
    cprint(text, "green", attrs=['bold'])
    print_knowledge(game)
    print("++++++++++++++++++++++++")


def print_winner(winner):
    print("++++++++++++++++++++++++")

    text = "WINNER : " + winner
    cprint(text, "green", attrs=['bold'])

    print("++++++++++++++++++++++++")


def print_knowledge(game, print_worlds=True):
    print()

    text = "Total worlds possible after this move : " + \
        str(len(game.knowledge_manager.model.worlds))
    cprint(text, "yellow", attrs=['bold'])
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

    text = "Code Maker Knowledge : "
    cprint(text, "yellow", attrs=['bold'])
    print(game.agent_knowledge.agent1)
    print()

    text = "Code Breaker Knowledge : "
    cprint(text, "yellow", attrs=['bold'])
    print(game.agent_knowledge.agent2)
    print()

    text = "Common Knowledge : "
    cprint(text, "yellow", attrs=['bold'])
    print(game.agent_knowledge.common_knowledge)
    print()


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
