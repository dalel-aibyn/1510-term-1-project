from unittest import TestCase
from unittest.mock import patch
from game import handle_duel_result


class Test(TestCase):
    @patch('builtins.print')
    def test_handle_duel_result_player_closer(self, mock_print):
        character = {"damage": 10}
        opponent_stats = {"mood": 20}
        expected_result = True
        expected_opponent_mood = 10
        expected_output = [
            '\nOpponent guessed: 5.00',
            'You were closer! Opponent takes damage! (-10 mood)'
        ]

        actual_result = handle_duel_result(character, 3.0, 5.0, 2.0, opponent_stats)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_opponent_mood, opponent_stats["mood"])
        actual_calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected_output, actual_calls)

    @patch('builtins.print')
    def test_handle_duel_result_opponent_closer(self, mock_print):
        character = {"damage": 5, "mood": 20}
        opponent_stats = {"damage": 6}
        expected_result = False
        expected_character_mood = 14
        expected_output = [
            '\nOpponent guessed: 2.10',
            'Opponent was closer! You take damage! (-6 mood)'
        ]

        actual_result = handle_duel_result(character, 5.0, 2.1, 2.0, opponent_stats)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_character_mood, character["mood"])
        actual_calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected_output, actual_calls)

    @patch('builtins.print')
    def test_handle_duel_result_critical_fail(self, mock_print):
        character = {"mood": 20}
        opponent_stats = {"damage": 6}
        expected_result = False
        expected_character_mood = 8
        expected_output = [
            'Invalid input! Opponent deals CRITICAL damage! (-12 mood)'
        ]

        actual_result = handle_duel_result(character, "critical", 5.0, 2.0, opponent_stats)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_character_mood, character["mood"])
        actual_calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected_output, actual_calls)

    @patch('builtins.print')
    def test_handle_duel_result_calculator_correct(self, mock_print):
        character = {"damage": 11}
        opponent_stats = {"mood": 20}
        player_answer = {"answer": True}
        expected_result = True
        expected_opponent_mood = 9
        expected_output = [
            'You typed the problem correctly! Opponent takes damage! (-11 mood)'
        ]

        actual_result = handle_duel_result(character, player_answer, 5.0, 2.0, opponent_stats)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_opponent_mood, opponent_stats["mood"])
        actual_calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected_output, actual_calls)

    @patch('builtins.print')
    def test_handle_duel_result_calculator_incorrect(self, mock_print):
        character = {"mood": 26}
        opponent_stats = {"damage": 4}
        player_answer = {"answer": False}
        expected_result = False
        expected_character_mood = 22
        expected_output = [
            'You typed the problem incorrectly! You take damage! (-4 mood)'
        ]

        actual_result = handle_duel_result(character, player_answer, 5.0, 2.0, opponent_stats)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_character_mood, character["mood"])
        actual_calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected_output, actual_calls)
