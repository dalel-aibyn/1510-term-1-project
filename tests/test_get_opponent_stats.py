from unittest import TestCase
from game import get_opponent_stats


class Test(TestCase):
    def test_get_opponent_stats_entrance(self):
        """Test entrance area opponent stats."""
        expected = {"mood": 6, "damage": 2, "experience": 0.3}
        actual = get_opponent_stats("Entrance")
        self.assertEqual(expected, actual)

    def test_get_opponent_stats_arithmetics(self):
        """Test arithmetics area opponent stats."""
        expected = {"mood": 9, "damage": 3, "experience": 0.5}
        actual = get_opponent_stats("Arithmetics")
        self.assertEqual(expected, actual)

    def test_get_opponent_stats_algebra(self):
        """Test algebra area opponent stats."""
        expected = {"mood": 12, "damage": 5, "experience": 0.8}
        actual = get_opponent_stats("Algebra")
        self.assertEqual(expected, actual)

    def test_get_opponent_stats_calculus(self):
        """Test calculus area opponent stats."""
        expected = {"mood": 15, "damage": 7, "experience": 1.4}
        actual = get_opponent_stats("Calculus")
        self.assertEqual(expected, actual)

    def test_get_opponent_stats_number_theory(self):
        """Test number theory area opponent stats."""
        expected = {"mood": 20, "damage": 11, "experience": 2}
        actual = get_opponent_stats("Number Theory")
        self.assertEqual(expected, actual)

    def test_get_opponent_stats_invalid_area(self):
        """Test invalid area raises KeyError."""
        with self.assertRaises(KeyError):
            get_opponent_stats("Invalid Area")
