import github_com.erohkohl.mlsolver
from github_com.erohkohl.mlsolver.kripke import World
import pytest
import sys
sys.path.append('../')

from kripke_model import get_corresponding_world, generate_worlds  # NOQA


def test_get_corresponding_world():
    input_order_of_colors = [1, 2, 5, 6]
    input_world_iterator = 78

    expected_world = World(
        'w78', {'1:yellow': True, '2:violet': True, '3:pink': True, '4:blue': True})
    actual_world = get_corresponding_world(
        input_order_of_colors, input_world_iterator)

    assert actual_world.name == expected_world.name
    assert actual_world.assignment == expected_world.assignment
