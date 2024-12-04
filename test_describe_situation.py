from unittest import TestCase
from unittest.mock import patch
from game import describe_situation


class Test(TestCase):
    @patch('builtins.print')
    def test_describe_situation_default_character(self, mock_print):
        character = {'x_position': 0, 'y_position': 0, 'Current HP': 5, 'inventory': []}
        expected = f'You are 4 steps away from the goal.\nYou have 5 health.\nYou have no items.\n'
        describe_situation((2, 2), character)
        mock_print.assert_called_once_with(expected)

    @patch('builtins.print')
    def test_describe_situation_moved(self, mock_print):
        character = {'x_position': 3, 'y_position': 1, 'Current HP': 5, 'inventory': []}
        expected = f'You are 6 steps away from the goal.\nYou have 5 health.\nYou have no items.\n'
        describe_situation((5, 5), character)
        mock_print.assert_called_once_with(expected)

    @patch('builtins.print')
    def test_describe_situation_injured(self, mock_print):
        character = {'x_position': 1, 'y_position': 2, 'Current HP': 3, 'inventory': []}
        expected = f'You are 3 steps away from the goal.\nYou have 3 health.\nYou have no items.\n'
        describe_situation((3, 3), character)
        mock_print.assert_called_once_with(expected)

    @patch('builtins.print')
    def test_describe_situation_some_items(self, mock_print):
        character = {'x_position': 5, 'y_position': 3, 'Current HP': 2, 'inventory': ['rock', 'paper', 'scissors']}
        expected = f'You are 8 steps away from the goal.\nYou have 2 health.\nYou have: rock, paper, scissors.\n'
        describe_situation((7, 9), character)
        mock_print.assert_called_once_with(expected)
