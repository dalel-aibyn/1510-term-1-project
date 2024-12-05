from unittest import TestCase
from unittest.mock import patch
from game import make_character


class Test(TestCase):
    @patch('builtins.input', return_value="nybia")
    def test_make_character_name(self, _):
        """Test character name is set correctly."""
        character = make_character()
        expected = "nybia"
        self.assertEqual(expected, character["name"])

    @patch('builtins.input', return_value="nybia")
    def test_make_character_starting_position(self, _):
        """Test character starts at correct position."""
        character = make_character()
        self.assertEqual(0, character["column"])
        self.assertEqual(6, character["row"])

    @patch('builtins.input', return_value="nybia")
    def test_make_character_initial_stats(self, _):
        """Test character's initial stats are correct."""
        character = make_character()
        self.assertEqual(20, character["mood"])
        self.assertEqual(20, character["max_mood"])
        self.assertEqual(3, character["damage"])
        self.assertEqual(0, character["steps_taken"])
        self.assertEqual(0.0, character["level"])

    @patch('builtins.input', return_value="nybia")
    def test_make_character_initial_inventory(self, _):
        """Test character's initial inventory state."""
        character = make_character()
        expected_inventory = {
            "Pen and paper": False,
            "Textbook": False,
            "Manual": False,
            "Calculator": False
        }
        self.assertEqual(expected_inventory, character["inventory"])

    @patch('builtins.input', return_value="nybia")
    def test_make_character_areas_visited(self, _):
        """Test character's initial areas visited state."""
        character = make_character()
        self.assertTrue(character["areas_visited"]["Entrance"])
        self.assertFalse(character["areas_visited"]["Arithmetics"])
        self.assertFalse(character["areas_visited"]["Algebra"])
        self.assertFalse(character["areas_visited"]["Calculus"])
        self.assertFalse(character["areas_visited"]["Number Theory"])
        self.assertFalse(character["areas_visited"]["Goal"])

    @patch('builtins.input', return_value="nybia")
    def test_make_character_opponents_encountered(self, _):
        """Test character's initial opponents encountered state."""
        character = make_character()
        self.assertFalse(character["opponents_encountered"]["Entrance"])
        self.assertFalse(character["opponents_encountered"]["Arithmetics"])
        self.assertFalse(character["opponents_encountered"]["Algebra"])
        self.assertFalse(character["opponents_encountered"]["Calculus"])
        self.assertFalse(character["opponents_encountered"]["Number Theory"]) 