from unittest import TestCase
from game import is_on_item_space


class Test(TestCase):
    def test_is_on_item_space_on_empty_space(self):
        character = {'x_position': 0, 'y_position': 0}
        board = {(0, 0): '--', (0, 1): '--', (1, 0): 'rock', (1, 1): 'GOAL'}
        expected = False
        actual = is_on_item_space(board, character)
        self.assertEqual(expected, actual)

    def test_is_on_item_space_on_goal(self):
        character = {'x_position': 1, 'y_position': 1}
        board = {(0, 0): '--', (0, 1): '--', (1, 0): 'rock', (1, 1): 'GOAL'}
        expected = False
        actual = is_on_item_space(board, character)
        self.assertEqual(expected, actual)

    def test_is_on_item_space_on_item(self):
        character = {'x_position': 1, 'y_position': 0}
        board = {(0, 0): '--', (0, 1): '--', (1, 0): 'rock', (1, 1): 'GOAL'}
        expected = True
        actual = is_on_item_space(board, character)
        self.assertEqual(expected, actual)

