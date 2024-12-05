from unittest import TestCase
import game


class Test(TestCase):
    def test_is_goal_at_goal_position(self):
        character = {"row": 6, "column": 6}
        expected = True

        actual = game.is_goal(character)

        self.assertEqual(expected, actual)

    def test_is_goal_wrong_row(self):
        character = {"row": 5, "column": 6}
        expected = False

        actual = game.is_goal(character)

        self.assertEqual(expected, actual)

    def test_is_goal_wrong_column(self):
        character = {"row": 6, "column": 5}
        expected = False

        actual = game.is_goal(character)

        self.assertEqual(expected, actual)

    def test_is_goal_wrong_both(self):
        character = {"row": 0, "column": 0}
        expected = False

        actual = game.is_goal(character)

        self.assertEqual(expected, actual)