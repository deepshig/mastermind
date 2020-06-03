import array as arr
import random as rand
import time


class CodeBreaker:

    def get_first_move(self):
        self.move = arr.array('i', [4, 6, 2, 1])
        return self.move

    def get_next_move(self, feedback):
        new_move = arr.array('i', [0, 0, 0, 0])
        old_move = self.move

        new_move = self.__handle_perfectly_correct_elements(new_move, feedback)

        new_move = self.__handle_correct_color_incorrect_position_elements(
            new_move, feedback)

        new_move = self.__handle_incorrect_elements(new_move, feedback)

        self.move = new_move
        return self.move

    def __handle_perfectly_correct_elements(self, new_move, feedback):
        for i in range(0, 4):
            if feedback[i] == 1:
                new_move[i] = self.move[i]

        return new_move

    def __handle_correct_color_incorrect_position_elements(self, new_move, feedback):
        empty_indices = arr.array('i')
        values_to_handle = arr.array('i')

        for i in range(0, 4):
            if feedback[i] == 0:
                values_to_handle.append(self.move[i])
            if new_move[i] == 0:
                empty_indices.append(i)

        if len(values_to_handle) != 0 and len(empty_indices) != 0:
            rand.seed(time.time_ns())

            for val in values_to_handle:
                random_index = rand.choice(empty_indices)
                new_move[random_index] = val

        for i in range(0, 4):
            if feedback[i] == 0:
                if self.move[i] == new_move[i]:
                    empty_indices.remove(i)
                    random_index = rand.choice(empty_indices)

                    new_move[i], new_move[random_index] = new_move[random_index], new_move[i]
                    break

        return new_move

    def __handle_incorrect_elements(self, new_move, feedback):
        values_to_substitute = arr.array('i')
        for i in range(0, 4):
            if feedback[i] == -1:
                values_to_substitute.append(self.move[i])

        new_move = substitute_values(new_move, values_to_substitute)
        return new_move


def substitute_values(move, values_to_substitute):
    for i in range(0, 4):
        if move[i] == 0:
            new_val = rand.randint(1, 6)

            while not can_substitute(move, values_to_substitute, new_val):
                new_val = rand.randint(1, 6)

            move[i] = new_val

    return move


def can_substitute(move, values_to_substitute, new_val):
    if move.count(new_val) == 0 and values_to_substitute.count(new_val) == 0:
        return True
    else:
        return False
