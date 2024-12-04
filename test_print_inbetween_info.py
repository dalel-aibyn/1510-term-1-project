from unittest import TestCase
from unittest.mock import patch
from game import print_inbetween_info


class Test(TestCase):
    @patch('builtins.print')
    def test_print_inbetween_info_with_player(self, mock_print):
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
        player_line = f'{yellow}#{yellow}#{yellow}#{yellow}#{yellow}#{yellow}#{yellow}#{yellow}#{yellow}#{yellow}#{yellow}#{yellow}#'
        slot_line = f'{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-'
        print_inbetween_info(board, player_pos, slot_wideness, row)
        mock_print.assert_called_once_with(f'{cyan}||{player_line}{yellow}#{slot_line}{cyan}+{slot_line}{cyan}{cyan}||')

    @patch('builtins.print')
    def test_print_inbetween_info_without_player(self, mock_print):
        board = {
            'max_x': 3, 'max_y': 4,
            (0, 0): '--', (1, 0): 'rock', (2, 0): '--',
            (0, 1): '--', (1, 1): 'paper', (2, 1): '--',
            (0, 2): '--', (1, 2): '--', (2, 2): '--',
            (0, 3): '--', (1, 3): '--', (2, 3): 'GOAL'
        }
        player_pos = (0, 0)
        slot_wideness = 12
        row = 1
        cyan = "\033[36m"
        slot_line = f'{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-{cyan}-'
        print_inbetween_info(board, player_pos, slot_wideness, row)
        mock_print.assert_called_once_with(f'{cyan}||{slot_line}{cyan}+{slot_line}{cyan}+{slot_line}{cyan}{cyan}||')