from unittest import TestCase
from game import make_character


class Test(TestCase):
    def test_make_character(self):
        expected_character = {'x_position': 0, 'y_position': 0, 'Current HP': 5, 'inventory': []}
        actual_character = make_character()
        self.assertEqual(expected_character, actual_character)
