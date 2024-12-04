from unittest import TestCase
from unittest.mock import patch
from game import item_decision


class Test(TestCase):
    @patch('builtins.input', side_effect=['y'])
    @patch('builtins.print')
    def test_item_decision_take_item(self, mock_print, mock_input):
        expected_board = {(1, 1): '--', 'max_x': 2, 'max_y': 2}
        expected_character = {'x_position': 1, 'y_position': 1, 'inventory': ['rock']}

        actual_board = {(1, 1): 'rock', 'max_x': 2, 'max_y': 2}
        actual_character = {'x_position': 1, 'y_position': 1, 'inventory': []}
        result = item_decision(actual_board, actual_character, 'rock')

        self.assertTrue(result)
        self.assertEqual(expected_board, actual_board)
        self.assertEqual(expected_character, actual_character)

        mock_print.assert_any_call('Would you like to take rock with you? (y/n):')
        mock_print.assert_any_call(f'You have acquired: rock.\n')

    @patch('builtins.input', side_effect=['n'])
    @patch('builtins.print')
    def test_item_decision_leave_item(self, mock_print, mock_input):
        expected_board = {(1, 1): 'paper', 'max_x': 3, 'max_y': 3}
        expected_character = {'x_position': 1, 'y_position': 1, 'inventory': []}

        actual_board = {(1, 1): 'paper', 'max_x': 3, 'max_y': 3}
        actual_character = {'x_position': 1, 'y_position': 1, 'inventory': []}
        result = item_decision(actual_board, actual_character, 'paper')

        self.assertTrue(result)
        self.assertEqual(expected_board, actual_board)
        self.assertEqual(expected_character, actual_character)

        mock_print.assert_any_call('Would you like to take paper with you? (y/n):')
        mock_print.assert_any_call(f'You decided to leave it behind.\n')

    @patch('builtins.input', side_effect=['invalid'])
    @patch('builtins.print')
    def test_item_decision_invalid(self, mock_print, mock_input):
        expected_board = {(1, 1): 'scissors', 'max_x': 4, 'max_y': 5}
        expected_character = {'x_position': 1, 'y_position': 1, 'inventory': []}

        actual_board = {(1, 1): 'scissors', 'max_x': 4, 'max_y': 5}
        actual_character = {'x_position': 1, 'y_position': 1, 'inventory': []}
        result = item_decision(actual_board, actual_character, 'scissors')

        self.assertFalse(result)
        self.assertEqual(expected_board, actual_board)
        self.assertEqual(expected_character, actual_character)
        mock_print.assert_any_call('Would you like to take scissors with you? (y/n):')
        mock_print.assert_any_call(f'Invalid input.\n')


