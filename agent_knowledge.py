from kripke_model import get_proposition


class AgentKnowledge:
    def __init__(self):
        self.agent1 = []
        self.agent2 = []
        self.common_knowledge = []

    def update_code_maker_knowledge(self, code):
        self.__extract_direct_knowledge(code)
        self.__extract_indirect_knowledge(code)
        return

    def __extract_direct_knowledge(self, code):
        for i in range(0, len(code)):
            proposition = get_proposition(i+1, code[i])
            self.agent1.append(proposition)
        return

    def __extract_indirect_knowledge(self, code):
        all_available_colors = [1, 2, 3, 4, 5, 6]

        for i in range(0, len(code)):
            for c in all_available_colors:
                if c != code[i]:
                    proposition = get_proposition(i+1, c)
                    negative = generate_negative_proposition(proposition)
                    self.agent1.append(negative)

        return


def generate_negative_proposition(proposition):
    negative = "~(" + proposition + ")"
    return negative
