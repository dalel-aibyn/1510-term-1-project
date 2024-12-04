from unittest import TestCase
from game import add_items_to_board


class Test(TestCase):
    def test_add_items_to_board_2_by_2(self):
        expected_number_of_items = 3  # Including the GOAL
        columns = 2
        rows = 2
        items = ['rock', 'paper', 'scissors']
        goal_pos = (1, 1)
        actual_result = add_items_to_board(rows, columns, items, goal_pos)
        self.assertEqual(len(actual_result), expected_number_of_items)
        self.assertEqual(actual_result[goal_pos], 'GOAL')

    def test_add_items_to_board_3_by_5(self):
        expected_number_of_items = 5  # Including the GOAL
        columns = 3
        rows = 5
        items = ['rock', 'paper', 'scissors']
        goal_pos = (2, 4)
        actual_result = add_items_to_board(rows, columns, items, goal_pos)
        self.assertEqual(len(actual_result), expected_number_of_items)
        self.assertEqual(actual_result[goal_pos], 'GOAL')

    def test_add_items_to_board_15_by_10(self):
        expected_number_of_items = 13  # Including the GOAL
        columns = 15
        rows = 10
        items = ['rock', 'paper', 'scissors']
        goal_pos = (14, 9)
        actual_result = add_items_to_board(rows, columns, items, goal_pos)
        self.assertEqual(len(actual_result), expected_number_of_items)
        self.assertEqual(actual_result[goal_pos], 'GOAL')

    def test_add_items_to_board_60_by_30(self):
        expected_number_of_items = 43 # Including the GOAL
        columns = 60
        rows = 30
        items = ['rock', 'paper', 'scissors']
        goal_pos = (59, 29)
        actual_result = add_items_to_board(rows, columns, items, goal_pos)
        self.assertEqual(len(actual_result), expected_number_of_items)
        self.assertEqual(actual_result[goal_pos], 'GOAL')
