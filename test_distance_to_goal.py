from unittest import TestCase
from game import distance_to_goal


class Test(TestCase):
    def test_distance_to_goal_small_board(self):
        character = {'x_position': 0, 'y_position': 0}
        goal_pos = (2, 2)
        expected = 4
        actual = distance_to_goal(goal_pos, character)
        self.assertEqual(expected, actual)

    def test_distance_to_goal_medium_board(self):
        character = {'x_position': 2, 'y_position': 1}
        goal_pos = (6, 7)
        expected = 10
        actual = distance_to_goal(goal_pos, character)
        self.assertEqual(expected, actual)

    def test_distance_to_goal_big_board(self):
        character = {'x_position': 10, 'y_position': 15}
        goal_pos = (30, 20)
        expected = 25
        actual = distance_to_goal(goal_pos, character)
        self.assertEqual(expected, actual)

    def test_distance_to_goal_on_goal(self):
        character = {'x_position': 5, 'y_position': 6}
        goal_pos = (5, 6)
        expected = 0
        actual = distance_to_goal(goal_pos, character)
        self.assertEqual(expected, actual)