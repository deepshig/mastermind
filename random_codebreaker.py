import random as rand
import time
from codemaker import LENGTH_OF_CODE


class RandomCodeBreaker:
    def get_first_move(self):
        self.move = []
        available_choices = [1, 2, 3, 4, 5, 6]

        rand.seed(time.time_ns())
        for _ in range(0, LENGTH_OF_CODE):
            val = rand.choice(available_choices)
            self.move.append(val)
            available_choices.remove(val)

        return self.move

    def get_next_move(self, feedback):
        self.move = []
        available_choices = [1, 2, 3, 4, 5, 6]

        rand.seed(time.time_ns())
        for _ in range(0, LENGTH_OF_CODE):
            val = rand.choice(available_choices)
            self.move.append(val)
            available_choices.remove(val)

        return self.move


r = RandomCodeBreaker()
print(r.get_first_move())
