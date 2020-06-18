from random_codebreaker import generate_random_move


class LogicianCodeBreaker:
    def __init__(self, knowledge_model):
        self.knowledge_model = knowledge_model

    def get_first_move(self):
        self.move = generate_random_move()
        return self.move
