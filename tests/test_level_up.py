from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):
    @patch('builtins.print')
    def test_level_up_single_level(self, mock_print):
        character = {
            "level": 2.5,
            "max_mood": 20,
            "damage": 5
        }
        experience = 0.8
        expected_character = {
            "level": 3.3,
            "max_mood": 23,
            "damage": 6
        }
        expected = [
            '\nLevel Up! You are now level 3!',
            'Max mood increased to 23!',
            'Damage increased to 6!'
        ]

        game.level_up(character, experience)

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)
        self.assertEqual(expected_character, character)

    @patch('builtins.print')
    def test_level_up_multiple_levels(self, mock_print):
        character = {
            "level": 2.8,
            "max_mood": 20,
            "damage": 5
        }
        experience = 2.5
        expected_character = {
            "level": 5.3,
            "max_mood": 29,
            "damage": 8
        }
        expected = [
            '\nLevel Up! You are now level 5!',
            'Max mood increased to 29!',
            'Damage increased to 8!'
        ]

        game.level_up(character, experience)

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)
        self.assertEqual(expected_character, character)

    @patch('builtins.print')
    def test_level_up_no_level_gained(self, mock_print):
        character = {
            "level": 2.2,
            "max_mood": 20,
            "damage": 5
        }
        experience = 0.3
        expected_character = {
            "level": 2.5,
            "max_mood": 20,
            "damage": 5
        }
        expected = []  # No output when no level is gained

        game.level_up(character, experience)

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)
        self.assertEqual(expected_character, character)

    @patch('builtins.print')
    def test_level_up_exact_level(self, mock_print):
        character = {
            "level": 2.0,
            "max_mood": 20,
            "damage": 5
        }
        experience = 1.0
        expected_character = {
            "level": 3.0,
            "max_mood": 23,
            "damage": 6
        }
        expected = [
            '\nLevel Up! You are now level 3!',
            'Max mood increased to 23!',
            'Damage increased to 6!'
        ]

        game.level_up(character, experience)

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)
        self.assertEqual(expected_character, character)
