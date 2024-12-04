from unittest import TestCase
from game import check_if_goal_attained


class Test(TestCase):
    def test_check_if_goal_attained_true(self):
        character = {'x_position': 0, 'y_position': 0}
        goal_pos = (2, 2)
        expected = False
        actual = check_if_goal_attained(goal_pos, character)
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_False(self):
        character = {'x_position': 2, 'y_position': 2}
        goal_pos = (2, 2)
        expected = True
        actual = check_if_goal_attained(goal_pos, character)
        self.assertEqual(expected, actual)
