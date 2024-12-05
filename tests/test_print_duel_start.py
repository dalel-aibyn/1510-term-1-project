from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):
    @patch('builtins.print')
    @patch('random.choice', return_value="\nA mathematical entity materializes before you...")
    def test_print_duel_start_message_1(self, _, mock_print):
        expected = [
            '\nA mathematical entity materializes before you...'
        ]

        game.print_duel_start()

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    @patch('random.choice', return_value="\nThe air crackles with mathematical energy as a challenger appears...")
    def test_print_duel_start_message_2(self, _, mock_print):
        expected = [
            '\nThe air crackles with mathematical energy as a challenger appears...'
        ]

        game.print_duel_start()

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    @patch('random.choice', return_value="\nNumbers swirl and coalesce into a challenging form...")
    def test_print_duel_start_message_3(self, _, mock_print):
        expected = [
            '\nNumbers swirl and coalesce into a challenging form...'
        ]

        game.print_duel_start()

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    @patch('random.choice', return_value="\nA guardian of mathematical truth blocks your path...")
    def test_print_duel_start_message_4(self, _, mock_print):
        expected = [
            '\nA guardian of mathematical truth blocks your path...'
        ]

        game.print_duel_start()

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    @patch('random.choice', return_value="\nThe mathematical realm itself challenges your knowledge...")
    def test_print_duel_start_message_5(self, _, mock_print):
        expected = [
            '\nThe mathematical realm itself challenges your knowledge...'
        ]

        game.print_duel_start()

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)
