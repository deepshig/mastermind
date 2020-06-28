import copy
from kripke_model import get_relations, generate_worlds, get_proposition
from codemaker import LENGTH_OF_CODE
from github_com.erohkohl.mlsolver.kripke import KripkeStructure


class KnowledgeManager:
    """
    Maintains the knowledge structure for the game.
    Initialises with a Kripke Model for the game.
    Keeps track of the real world, according to the secret code.
    Processes every move to update the knowledge structure accrodingly.
    """

    def __init__(self):
        worlds = generate_worlds()
        relations = get_relations(worlds)
        self.model = KripkeStructure(worlds, relations)

    def get_real_world(self, code):
        """
        Initialises the real world in the Kripke Model
        from the secret code generated for the game.
        """
        real_world_assignment = get_assignment(code)
        for world in self.model.worlds:
            if world.assignment == real_world_assignment:
                self.real_world = world
                return

    def handle_move(self, move, feedback):
        """
        Handles each move and its feedback as a public
        announcement, and restricts the available model
        accordingly.
        """
        for i in range(0, LENGTH_OF_CODE):
            if feedback[i] == 1:
                assignment = get_proposition(i+1, move[i])
                self.__handle_perfectly_correct_element(assignment)

            if feedback[i] == 0:
                assignment = get_proposition(i+1, move[i])
                self.__handle_wrongly_positioned_element(
                    assignment)

            if feedback[i] == -1:
                self.__handle_incorrect_element(move[i])
        return

    def __handle_perfectly_correct_element(self, assignment):
        """
        For correctly guessed color, remove the worlds
        which have some other color at this position
        and derive the reduced model.
        """
        worlds = copy.deepcopy(self.model.worlds)
        for w in worlds:
            if not (assignment in w.assignment):
                self.model.remove_node_by_name(w.name)
        return

    def __handle_wrongly_positioned_element(self, assignment):
        """
        For wrongly positioned color, remove the worlds
        which have this color at this position
        and derive the reduced model.
        """
        worlds = copy.deepcopy(self.model.worlds)
        for w in worlds:
            if assignment in w.assignment:
                self.model.remove_node_by_name(w.name)
        return

    def __handle_incorrect_element(self, color_number):
        """
        For incorrectly guessed color, remove the worlds
        which have this color at any position
        and derive the reduced model.
        """
        worlds = copy.deepcopy(self.model.worlds)
        for w in worlds:
            for i in range(1, LENGTH_OF_CODE+1):
                assignment = get_proposition(i, color_number)
                if assignment in w.assignment:
                    self.model.remove_node_by_name(w.name)
        return


def get_assignment(code):
    """
    Get world assignment from the code
    [1 2 3 4] -> {'1:yellow', '2:violet', '3:red', '4:green'}
    """
    assignment = {}

    for i in range(0, LENGTH_OF_CODE):
        proposition = get_proposition(i+1, code[i])
        assignment[proposition] = True

    return assignment
