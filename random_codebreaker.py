import random as rand
import time
from codemaker import LENGTH_OF_CODE


class RandomCodeBreaker:
    def get_first_move(self):
        self.move = generate_random_move()
        return self.move

    def get_next_move(self, feedback):
        self.move = generate_random_move()
        return self.move


def generate_random_move():
    move = []
    available_choices = [1, 2, 3, 4, 5, 6]

    rand.seed(time.time_ns())
    for _ in range(0, LENGTH_OF_CODE):
        val = rand.choice(available_choices)
        move.append(val)
        available_choices.remove(val)

    return move
