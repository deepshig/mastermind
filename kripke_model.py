import github_com.erohkohl.mlsolver
from github_com.erohkohl.mlsolver.kripke import KripkeStructure, World
from permutations import generate_all_combinations, generate_all_permutations
from codemaker import LENGTH_OF_CODE


numbers_to_colors = {
    1: "yellow",
    2: "violet",
    3: "red",
    4: "green",
    5: "pink",
    6: "blue"
}


def get_relations(worlds):
    number_of_worlds = len(worlds)
    relations = {
        '1': {()},
        '2': {()},
    }

    for agent, agents_relations in relations.items():
        agents_relations.remove(())
        for i in range(0, number_of_worlds):
            for j in range(0, number_of_worlds):
                relation = (worlds[i].name, worlds[j].name)

                if agent == '1' and i == j:
                    agents_relations.add(relation)

                if agent == '2':
                    agents_relations.add(relation)

    return relations


def get_corresponding_world(order_of_colors, world_iterator):
    proposition_map = {}
    for i in range(0, LENGTH_OF_CODE):
        color = numbers_to_colors[order_of_colors[i]]
        key = str(i+1) + ":" + color
        proposition_map[key] = True

    world_name = "w" + str(world_iterator)
    world = World(world_name, proposition_map)

    return world


def generate_worlds():
    available_colors = [1, 2, 3, 4, 5, 6]
    all_possible_combinations = generate_all_combinations(
        available_colors, LENGTH_OF_CODE)

    world_iterator = 1
    worlds = []

    for combination in all_possible_combinations:
        all_possible_permutations = generate_all_permutations(
            list(combination))

        for permutation in all_possible_permutations:
            world = get_corresponding_world(list(permutation), world_iterator)
            worlds.append(world)
            world_iterator = world_iterator + 1

    return worlds
