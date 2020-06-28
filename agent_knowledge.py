from kripke_model import get_proposition


class AgentKnowledge:
    """
    Monitors and maintains the agent knowledge for the game.
    Processes the secret code to update the agent1 knowledge.
    Processes every move to update the common knowledge
    and deduced knowledge for agent2 accrodingly.
    """

    def __init__(self):
        self.agent1 = []
        self.agent2 = []
        self.common_knowledge = []

    def update_code_maker_knowledge(self, code):
        """
        Extracts knowledge from the secret code and
        adds it to the individual knowledge of agent1.
        """
        self.__extract_direct_knowledge(code)
        self.__extract_indirect_knowledge(code)
        return

    def update_move_knowledge(self, move, feedback):
        """
        Extracts knowledge from the move and its feedback,
        and adds it to the common knowledge of the model
        and the individual knowledge of agent2, accordingly.
        """
        for i in range(0, len(move)):
            if feedback[i] == 1:
                self.__add_knowledge_for_perfectly_correct_element(
                    i+1, move[i])

            if feedback[i] == -1:
                self.__add_knowledge_for_incorrect_element(i+1, move[i])

            if feedback[i] == 0:
                self.__add_knowledge_for_wrongly_positioned_element(
                    i+1, move[i])
        return

    def __extract_direct_knowledge(self, code):
        """
        From the secret code, extracts direct knowledge about
        the colors being present at given positions,
        and adds it to agent1 individual knowledge.
        """
        for i in range(0, len(code)):
            proposition = get_proposition(i+1, code[i])
            self.agent1.append(proposition)
        return

    def __extract_indirect_knowledge(self, code):
        """
        From the secret code, extracts indirect knowledge about
        the other colors NOT being present at given positions,
        and adds it to agent1 individual knowledge.
        """
        all_available_colors = [1, 2, 3, 4, 5, 6]

        for i in range(0, len(code)):
            for c in all_available_colors:
                if c != code[i]:
                    proposition = get_proposition(i+1, c)
                    negative = generate_negative_proposition(proposition)
                    self.agent1.append(negative)
        return

    def __add_knowledge_for_perfectly_correct_element(self, index, color_number):
        """
        From the move and feedback, extracst knowledge about
        the colors which are perfectly positioned.
        Adds direct knowledge about those colors being present
        to the common knowledge.
        Invokes extraction of indirect knowledge
        """
        proposition = get_proposition(index, color_number)

        self.common_knowledge.append(proposition)
        self.__deduce_knowledge_for_correct_element(index, color_number)

        return

    def __deduce_knowledge_for_correct_element(self, index, color_number):
        """
        Extracts indirect knowledge about perfectly positioned colors,
        that is, other colors NOT being present at those positions,
        and adds it to individual knowledge of agent2.
        """
        all_available_colors = [1, 2, 3, 4, 5, 6]
        for c in all_available_colors:
            if c != color_number:
                proposition = get_proposition(index, c)
                negative = generate_negative_proposition(proposition)
                self.agent2.append(negative)
        return

    def __add_knowledge_for_incorrect_element(self, index, color_number):
        """
        From the move and feedback, extracts knowledge about
        the colors which are incorrectly guessed.
        Extracts direct knowledge about these colors NOT being
        present anywhere, and adds it to the common knowledge.
        Invokes extraction of indirect knowledge.
        """
        for i in range(1, 5):
            proposition = get_proposition(i, color_number)
            negative = generate_negative_proposition(proposition)
            self.common_knowledge.append(negative)

        self.__deduce_knowledge_for_incorrect_element(index, color_number)
        return

    def __deduce_knowledge_for_incorrect_element(self, index, color_number):
        """
        Extracts indirect knowledge about incorrectly guessed color,
        that is, MAY BE some other color is present at that position,
        and adds it to individual knowledge of agent2.
        """
        all_available_colors = [1, 2, 3, 4, 5, 6]
        for c in all_available_colors:
            if c != color_number:
                proposition = get_proposition(index, c)
                may_be = generate_may_be_proposition(proposition)
                self.agent2.append(may_be)
        return

    def __add_knowledge_for_wrongly_positioned_element(self, index, color_number):
        """
        From the move and feedback, extracts knowledge about
        the colors which are wrongly positioned.
        Extracts direct knowledge about these colors NOT being
        present at that position, and adds it to the common knowledge.
        Invokes extraction of indirect knowledge
        """
        proposition = get_proposition(index, color_number)
        negative = generate_negative_proposition(proposition)
        self.common_knowledge.append(negative)

        self.__deduce_knowledge_for_wrongly_positioned_element(
            index, color_number)
        return

    def __deduce_knowledge_for_wrongly_positioned_element(self, index, color_number):
        """
        Extracts indirect knowledge about wrongly positioned color,
        that is, this color is MAY BE present at some other position,
        and adds it to individual knowledge of agent2.
        """
        for i in range(1, 5):
            if i != index:
                proposition = get_proposition(i, color_number)
                may_be = generate_may_be_proposition(proposition)
                self.agent2.append(may_be)
        return


def generate_negative_proposition(proposition):
    """
    Get negative proposition:
    1:red -> ~(1:red)
    """
    negative = "~(" + proposition + ")"
    return negative


def generate_may_be_proposition(proposition):
    """
    Get may be proposition:
    1:red -> *(1:red)
    """
    may_be = "*(" + proposition + ")"
    return may_be
