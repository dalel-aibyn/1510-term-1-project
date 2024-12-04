from unittest import TestCase
from unittest.mock import patch
from game import action_with_item


class Test(TestCase):
    @patch('builtins.input', side_effect=['y'])
    @patch('builtins.print')
    def test_action_with_item_take(self, mock_print, mock_input):
        expected_board = {(1, 1): '--', 'max_x': 2, 'max_y': 2}
        expected_character = {'x_position': 1, 'y_position': 1, 'inventory': ['rock']}

        actual_board = {(1, 1): 'rock', 'max_x': 2, 'max_y': 2}
        actual_character = {'x_position': 1, 'y_position': 1, 'inventory': []}
        action_with_item(actual_board, actual_character)

        self.assertEqual(expected_board, actual_board)
        self.assertEqual(expected_character, actual_character)

        mock_print.assert_any_call('You have found: rock.')
        mock_print.assert_any_call('You have acquired: rock.\n')

    @patch('builtins.input', side_effect=['n'])
    @patch('builtins.print')
    def test_action_with_item_leave(self, mock_print, mock_input):
        expected_board = {(1, 1): 'paper', 'max_x': 3, 'max_y': 3}
        expected_character = {'x_position': 1, 'y_position': 1, 'inventory': []}

        actual_board = {(1, 1): 'paper', 'max_x': 3, 'max_y': 3}
        actual_character = {'x_position': 1, 'y_position': 1, 'inventory': []}
        action_with_item(actual_board, actual_character)

        self.assertEqual(expected_board, actual_board)
        self.assertEqual(expected_character, actual_character)

        mock_print.assert_any_call('You have found: paper.')
        mock_print.assert_any_call('You decided to leave it behind.\n')

    @patch('builtins.input', side_effect=['lol', 'n'])
    @patch('builtins.print')
    def test_action_with_item_invalid_then_leave(self, mock_print, mock_input):
        expected_board = {(1, 1): 'scissors', 'max_x': 4, 'max_y': 5}
        expected_character = {'x_position': 1, 'y_position': 1, 'inventory': []}

        actual_board = {(1, 1): 'scissors', 'max_x': 4, 'max_y': 5}
        actual_character = {'x_position': 1, 'y_position': 1, 'inventory': []}
        action_with_item(actual_board, actual_character)

        self.assertEqual(expected_board, actual_board)
        self.assertEqual(expected_character, actual_character)

        mock_print.assert_any_call('You have found: scissors.')
        mock_print.assert_any_call('Invalid input.\n')
        mock_print.assert_any_call('You decided to leave it behind.\n')