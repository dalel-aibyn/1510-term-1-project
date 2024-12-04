from unittest import TestCase
from unittest.mock import patch
from game import print_info_row


class Test(TestCase):
    @patch('builtins.print')
    def test_print_info_row_with_player(self, mock_print):
        board = {
            'max_x': 3, 'max_y': 4,
            (0, 0): '--', (1, 0): 'rock', (2, 0): '--',
            (0, 1): '--', (1, 1): 'paper', (2, 1): '--',
            (0, 2): '--', (1, 2): '--', (2, 2): '--',
            (0, 3): '--', (1, 3): '--', (2, 3): 'GOAL'
        }
        player_pos = (0, 0)
        slot_wideness = 12
        row = 0
        cyan = "\033[36m"
        yellow = "\033[33m"
        reset = "\033[0m"
        print_info_row(board, player_pos, slot_wideness, row)
        mock_print.assert_called_once_with(f'{cyan}||{reset}    YOU     {yellow}#{reset}    rock    {cyan}|{reset}     --     {cyan}||')

    @patch('builtins.print')
    def test_print_info_row_with_player_on_item(self, mock_print):
        board = {
            'max_x': 3, 'max_y': 4,
            (0, 0): '--', (1, 0): 'rock', (2, 0): '--',
            (0, 1): '--', (1, 1): 'paper', (2, 1): '--',
            (0, 2): '--', (1, 2): '--', (2, 2): '--',
            (0, 3): '--', (1, 3): '--', (2, 3): 'GOAL'
        }
        player_pos = (1, 1)
        slot_wideness = 12
        row = 1
        cyan = "\033[36m"
        yellow = "\033[33m"
        reset = "\033[0m"
        print_info_row(board, player_pos, slot_wideness, row)
        mock_print.assert_called_once_with(f'{cyan}||{reset}     --     {yellow}#{reset} YOU + pape {yellow}#{reset}     --     {cyan}||')

    @patch('builtins.print')
    def test_print_info_row_empty_row(self, mock_print):
        board = {
            'max_x': 3, 'max_y': 4,
            (0, 0): '--', (1, 0): 'rock', (2, 0): '--',
            (0, 1): '--', (1, 1): 'paper', (2, 1): '--',
            (0, 2): '--', (1, 2): '--', (2, 2): '--',
            (0, 3): '--', (1, 3): '--', (2, 3): 'GOAL'
        }
        player_pos = (0, 3)
        slot_wideness = 12
        row = 2
        cyan = "\033[36m"
        reset = "\033[0m"
        print_info_row(board, player_pos, slot_wideness, row)
        mock_print.assert_called_once_with(f'{cyan}||{reset}     --     {cyan}|{reset}     --     {cyan}|{reset}     --     {cyan}||')

    @patch('builtins.print')
    def test_print_info_row_player_and_goal(self, mock_print):
        board = {
            'max_x': 3, 'max_y': 4,
            (0, 0): '--', (1, 0): 'rock', (2, 0): '--',
            (0, 1): '--', (1, 1): 'paper', (2, 1): '--',
            (0, 2): '--', (1, 2): '--', (2, 2): '--',
            (0, 3): '--', (1, 3): '--', (2, 3): 'GOAL'
        }
        player_pos = (0, 3)
        slot_wideness = 12
        row = 3
        cyan = "\033[36m"
        yellow = "\033[33m"
        reset = "\033[0m"
        print_info_row(board, player_pos, slot_wideness, row)
        mock_print.assert_called_once_with(f'{cyan}||{reset}    YOU     {yellow}#{reset}     --     {cyan}|{reset}    GOAL    {cyan}||')