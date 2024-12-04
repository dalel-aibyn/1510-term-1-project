from unittest import TestCase
from unittest.mock import patch
from game import validate_move


class Test(TestCase):
    def test_validate_move_up_valid(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 1}
        expected = 'up'
        actual = validate_move(board, character, 'up')
        self.assertEqual(expected, actual)

    def test_validate_move_up_invalid(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 0}
        expected = False
        actual = validate_move(board, character, 'up')
        self.assertEqual(expected, actual)

    def test_validate_move_capital_down_valid(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 1}
        expected = 'down'
        actual = validate_move(board, character, 'DOWN')
        self.assertEqual(expected, actual)

    def test_validate_move_down_invalid(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 2}
        expected = False
        actual = validate_move(board, character, 'down')
        self.assertEqual(expected, actual)

    def test_validate_move_camel_left_valid(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 1}
        expected = 'left'
        actual = validate_move(board, character, 'LeFt')
        self.assertEqual(expected, actual)

    def test_validate_move_left_invalid(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 0, 'y_position': 1}
        expected = False
        actual = validate_move(board, character, 'left')
        self.assertEqual(expected, actual)

    def test_validate_move_padded_with_spaces_right_valid(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 1}
        expected = 'right'
        actual = validate_move(board, character, '    right  ')
        self.assertEqual(expected, actual)

    def test_validate_move_right_invalid(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 2, 'y_position': 1}
        expected = False
        actual = validate_move(board, character, 'right')
        self.assertEqual(expected, actual)

    def test_validate_move_compass_direction(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 1}
        expected = 'up'
        actual = validate_move(board, character, 'north')
        self.assertEqual(expected, actual)

        expected = 'right'
        actual = validate_move(board, character, 'east')
        self.assertEqual(expected, actual)

        expected = 'down'
        actual = validate_move(board, character, 'south')
        self.assertEqual(expected, actual)

        expected = 'left'
        actual = validate_move(board, character, 'west')
        self.assertEqual(expected, actual)

    def test_validate_move_compass_short_direction(self):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 1}
        expected = 'up'
        actual = validate_move(board, character, 'n')
        self.assertEqual(expected, actual)

        expected = 'right'
        actual = validate_move(board, character, 'e')
        self.assertEqual(expected, actual)

        expected = 'down'
        actual = validate_move(board, character, 's')
        self.assertEqual(expected, actual)

        expected = 'left'
        actual = validate_move(board, character, 'w')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_validate_move_invalid_direction(self, mock_print):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 1}
        expected = False
        actual = validate_move(board, character, 'over there')
        self.assertEqual(expected, actual)
        mock_print.assert_called_once_with('Invalid direction entered: over there')

    @patch('builtins.print')
    def test_validate_move_off_board(self, mock_print):
        board = {'max_x': 3, 'max_y': 3}
        character = {'x_position': 1, 'y_position': 0}
        expected = False
        actual = validate_move(board, character, 'up')
        self.assertEqual(expected, actual)
        mock_print.assert_called_once_with('Unable to move up, as it goes off the board.')