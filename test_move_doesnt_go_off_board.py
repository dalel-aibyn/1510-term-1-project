from unittest import TestCase
from game import move_doesnt_go_off_board


class Test(TestCase):
    def test_move_doesnt_go_off_board_up_off_board(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 0}
        expected = False
        actual = move_doesnt_go_off_board(board, character, 'up')
        self.assertEqual(expected, actual)

    def test_move_doesnt_go_off_board_up_on_board(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 1}
        expected = True
        actual = move_doesnt_go_off_board(board, character, 'up')
        self.assertEqual(expected, actual)

    def test_move_doesnt_go_off_board_down_off_board(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 2}
        expected = False
        actual = move_doesnt_go_off_board(board, character, 'down')
        self.assertEqual(expected, actual)

    def test_move_doesnt_go_off_board_left_off_board(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 0, 'y_position': 1}
        expected = False
        actual = move_doesnt_go_off_board(board, character, 'left')
        self.assertEqual(expected, actual)

    def test_move_doesnt_go_off_board_right_off_board(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 2, 'y_position': 1}
        expected = False
        actual = move_doesnt_go_off_board(board, character, 'right')
        self.assertEqual(expected, actual)

    def test_move_doesnt_go_off_board_down_on_board(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 1}
        expected = True
        actual = move_doesnt_go_off_board(board, character, 'down')
        self.assertEqual(expected, actual)

    def test_move_doesnt_go_off_board_left_on_board(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 1}
        expected = True
        actual = move_doesnt_go_off_board(board, character, 'left')
        self.assertEqual(expected, actual)

    def test_move_doesnt_go_off_board_right_on_board(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 1}
        expected = True
        actual = move_doesnt_go_off_board(board, character, 'right')
        self.assertEqual(expected, actual)