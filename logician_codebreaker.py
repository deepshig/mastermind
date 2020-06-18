import random
import time

from kripke_model import get_index_and_color_number


class LogicianCodeBreaker:
    def __init__(self, knowledge_model):
        self.knowledge_model = knowledge_model

    def get_first_move(self):
        world = self.__generate_random_world()
        self.move = world_to_move(world)
        return self.move

    def get_next_move(self, feedback):
        world = self.__generate_random_world()
        self.move = world_to_move(world)
        return self.move

    def __generate_random_world(self):
        random.seed(time.time_ns())
        world = random.choice(self.knowledge_model.model.worlds)
        return world


def world_to_move(world):
    move = [0, 0, 0, 0]

    for key in world.assignment:
        index, color = get_index_and_color_number(key)
        move[index-1] = color

    return move
