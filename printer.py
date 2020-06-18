def print_code(code, knowledge):
    print("++++++++++++++++++++++++")
    print("CODE : ", *code, sep=" ")
    print_knowledge(knowledge)
    print("++++++++++++++++++++++++")


def print_game_state(i, move, feedback, knowledge):
    print("++++++++++++++++++++++++")
    print("Move :", i, ": ", *move, sep=" ")
    print("Feedback : ", *feedback, sep=" ")
    print_knowledge(knowledge)
    print("++++++++++++++++++++++++")


def print_winner(winner):
    print("++++++++++++++++++++++++")
    print("WINNER : ",  winner)
    print("++++++++++++++++++++++++")


def print_knowledge(knowledge):
    print("Total worlds : ", len(knowledge.model.worlds))
    print()

    for w in knowledge.model.worlds:
        print(w.name, w.assignment)

    print()
    print("Real World : ", knowledge.real_world)
    print("Number of Relations for Agent 1 : ",
          len(knowledge.model.relations['1']))
    print("Number of Relations for Agent 2 : ",
          len(knowledge.model.relations['2']))


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
