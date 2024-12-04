from unittest import TestCase
from game import make_board


class Test(TestCase):
    def test_make_board_small(self):
        columns = 2
        rows = 2
        goal_pos = (1, 1)
        expected_board = {'goal_pos': goal_pos, 'max_x': 2, 'max_y': 2, goal_pos: "GOAL"}
        actual_board = make_board(columns, rows)
        self.assertEqual(expected_board['goal_pos'], actual_board['goal_pos'])
        self.assertEqual(expected_board['max_x'], actual_board['max_x'])
        self.assertEqual(expected_board['max_y'], actual_board['max_y'])
        self.assertEqual(expected_board[goal_pos], actual_board[goal_pos])

    def test_make_board_medium(self):
        columns = 5
        rows = 7
        goal_pos = (4, 6)
        expected_board = {'goal_pos': goal_pos, 'max_x': 5, 'max_y': 7, goal_pos: "GOAL"}
        actual_board = make_board(columns, rows)
        self.assertEqual(expected_board['goal_pos'], actual_board['goal_pos'])
        self.assertEqual(expected_board['max_x'], actual_board['max_x'])
        self.assertEqual(expected_board['max_y'], actual_board['max_y'])
        self.assertEqual(expected_board[goal_pos], actual_board[goal_pos])

    def test_make_board_big(self):
        columns = 15
        rows = 12
        goal_pos = (14, 11)
        expected_board = {'goal_pos': goal_pos, 'max_x': 15, 'max_y': 12, goal_pos: "GOAL"}
        actual_board = make_board(columns, rows)
        self.assertEqual(expected_board['goal_pos'], actual_board['goal_pos'])
        self.assertEqual(expected_board['max_x'], actual_board['max_x'])
        self.assertEqual(expected_board['max_y'], actual_board['max_y'])
        self.assertEqual(expected_board[goal_pos], actual_board[goal_pos])

    def test_make_board_huge(self):
        columns = 69
        rows = 42
        goal_pos = (68, 41)
        expected_board = {'goal_pos': goal_pos, 'max_x': 69, 'max_y': 42, goal_pos: "GOAL"}
        actual_board = make_board(columns, rows)
        self.assertEqual(expected_board['goal_pos'], actual_board['goal_pos'])
        self.assertEqual(expected_board['max_x'], actual_board['max_x'])
        self.assertEqual(expected_board['max_y'], actual_board['max_y'])
        self.assertEqual(expected_board[goal_pos], actual_board[goal_pos])