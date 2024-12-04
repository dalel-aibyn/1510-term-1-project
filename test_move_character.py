from unittest import TestCase
from game import move_character


class Test(TestCase):
    def test_move_character_up(self):
        expected = {'x_position': 1, 'y_position': 0}
        actual = {'x_position': 1, 'y_position': 1}
        move_character(actual, 'up')
        self.assertEqual(expected, actual)

    def test_move_character_down(self):
        expected = {'x_position': 1, 'y_position': 2}
        actual = {'x_position': 1, 'y_position': 1}
        move_character(actual, 'down')
        self.assertEqual(expected, actual)

    def test_move_character_left(self):
        expected = {'x_position': 0, 'y_position': 1}
        actual = {'x_position': 1, 'y_position': 1}
        move_character(actual, 'left')
        self.assertEqual(expected, actual)

    def test_move_character_right(self):
        expected = {'x_position': 2, 'y_position': 1}
        actual = {'x_position': 1, 'y_position': 1}
        move_character(actual, 'right')
        self.assertEqual(expected, actual)
