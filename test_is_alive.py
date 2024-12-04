from unittest import TestCase
from game import is_alive


class Test(TestCase):
    def test_is_alive_true(self):
        character = {'Current HP': 5}
        expected_result = True
        actual = is_alive(character)
        self.assertEqual(expected_result, actual)

    def test_is_alive_false(self):
        character = {'Current HP': 0}
        expected_result = False
        actual = is_alive(character)
        self.assertEqual(expected_result, actual)