from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):
    @patch('builtins.print')
    def test_print_item_found_pen_and_paper(self, mock_print):
        expected = [
            '\nYou have found a trusty pen and paper! Now you\'ll have more time to solve problems.'
        ]

        game.print_item_found("Pen and paper")

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_print_item_found_textbook(self, mock_print):
        expected = [
            '\nAn ancient mathematical tome! Its pages contain helpful tips for solving problems.'
        ]

        game.print_item_found("Textbook")

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_print_item_found_manual(self, mock_print):
        expected = [
            '\nA manual of mathematical wisdom! It will show you the range where answers lie.'
        ]

        game.print_item_found("Manual")

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_print_item_found_calculator(self, mock_print):
        expected = [
            '\nA mystical Calculator! You can now type in the problems instead of solving them.'
        ]

        game.print_item_found("Calculator")

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_print_item_found_unknown_item(self, mock_print):
        expected = [
            '\nYou found a Unknown Item!'
        ]

        game.print_item_found("Unknown Item")

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)
