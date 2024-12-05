from unittest import TestCase
from unittest.mock import patch
from game import handle_duel_result


class Test(TestCase):
    @patch('builtins.print')
    def test_handle_duel_result_critical(self, _):
        """Test handling critical failure."""
        character = {"mood": 20}
        opponent_stats = {"damage": 5}
        result = handle_duel_result(character, "critical", 7.0, 10, opponent_stats)
        self.assertFalse(result)
        self.assertEqual(10, character["mood"])

    @patch('builtins.print')
    def test_handle_duel_result_timeout(self, _):
        """Test handling timeout."""
        character = {"mood": 20}
        opponent_stats = {"damage": 5}
        result = handle_duel_result(character, None, 7.0, 10, opponent_stats)
        self.assertFalse(result)
        self.assertEqual(15, character["mood"])

    @patch('builtins.print')
    def test_handle_duel_result_calculator_correct(self, _):
        """Test handling correct calculator answer."""
        character = {"damage": 5}
        opponent_stats = {"mood": 20}
        result = handle_duel_result(character, {"answer": True}, 7.0, 10, opponent_stats)
        self.assertTrue(result)
        self.assertEqual(15, opponent_stats["mood"])

    @patch('builtins.print')
    def test_handle_duel_result_calculator_incorrect(self, _):
        """Test handling incorrect calculator answer."""
        character = {"mood": 20}
        opponent_stats = {"damage": 5}
        result = handle_duel_result(character, {"answer": False}, 7.0, 10, opponent_stats)
        self.assertFalse(result)
        self.assertEqual(15, character["mood"])

    @patch('builtins.print')
    def test_handle_duel_result_player_closer(self, _):
        """Test when player's answer is closer."""
        character = {"damage": 5}
        opponent_stats = {"mood": 20}
        result = handle_duel_result(character, 9.5, 7.0, 10, opponent_stats)
        self.assertTrue(result)
        self.assertEqual(15, opponent_stats["mood"])

    @patch('builtins.print')
    def test_handle_duel_result_opponent_closer(self, _):
        """Test when opponent's answer is closer."""
        character = {"mood": 20}
        opponent_stats = {"damage": 5}
        result = handle_duel_result(character, 7.0, 9.5, 10, opponent_stats)
        self.assertFalse(result)
        self.assertEqual(15, character["mood"])

    @patch('builtins.print')
    def test_handle_duel_result_unsolvable(self, _):
        """Test handling unsolvable problem."""
        character = {"damage": 5}
        opponent_stats = {"mood": 20}
        result = handle_duel_result(character, 7.0, 9.5, None, opponent_stats)
        self.assertTrue(result)
        self.assertEqual(15, opponent_stats["mood"])
