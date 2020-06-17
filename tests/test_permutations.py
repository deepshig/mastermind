import pytest
import sys
sys.path.append('../')

from permutations import generate_all_combinations, generate_all_permutations  # NOQA


def test_generate_all_combinations():
    """ when we have a list of 1 element """
    input = [1]
    expected_combinations = [(1,)]

    combinations = generate_all_combinations(input, 1)
    assert len(combinations) == 1
    assert combinations == expected_combinations

    """ when length of subset is same as length of list """
    input = [1, 2, 3]
    expected_combinations = [(1, 2, 3)]

    combinations = generate_all_combinations(input, 3)
    assert len(combinations) == 1
    assert combinations == expected_combinations

    """ when length of subset is less than length of list """
    input = [1, 2, 3]
    expected_combinations = [(1, 2), (1, 3), (2, 3)]

    combinations = generate_all_combinations(input, 2)
    assert combinations == expected_combinations

    """ when length of subset is greater than length of list """
    input = [1, 2, 3]

    combinations = generate_all_combinations(input, 4)
    assert len(combinations) == 0


def test_generate_all_permutations():
    """ when length of input array is 1 """
    input = [1]
    expected_permutations = [[1]]

    permutations = generate_all_permutations(input)
    assert len(permutations) == 1
    assert permutations == expected_permutations

    """ when length of input array is more than 1 """
    input = [1, 2, 3]
    expected_permutations = [[1, 2, 3], [2, 1, 3],
                             [3, 1, 2], [1, 3, 2],
                             [2, 3, 1], [3, 2, 1]]

    permutations = generate_all_permutations(input)
    assert permutations == expected_permutations
