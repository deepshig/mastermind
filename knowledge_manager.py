from kripke_model import get_relations, generate_worlds, numbers_to_colors
from codemaker import LENGTH_OF_CODE
from github_com.erohkohl.mlsolver.kripke import KripkeStructure


class KnowledgeManager:
    """
    Maintains the knowledge structure for the game.
    Initialises with a Kripke Model for the game.
    Keeps track of the real world, according to the secret code.
    Processes every move to update the knowledge structure accrodingly.
    Maintains the common knowledge, and knowledge per agent basis.
    """

    def __init__(self):
        self.worlds = generate_worlds()
        self.relations = get_relations(self.worlds)
        self.model = KripkeStructure(self.worlds, self.relations)

    def get_real_world(self, code):
        real_world_assignment = get_assignment(code)
        for world in self.worlds:
            if world.assignment == real_world_assignment:
                self.real_world = world
                return


def get_assignment(code):
    assignment = {}

    for i in range(0, LENGTH_OF_CODE):
        key = str(i+1) + ":" + numbers_to_colors[code[i]]
        assignment[key] = True

    return assignment
