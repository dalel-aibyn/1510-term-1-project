from unittest import TestCase
from game import get_tier_positions


class Test(TestCase):
    def test_get_tier_positions_entrance(self):
        """Test entrance tier positions."""
        expected = [(0, 5), (1, 6)]
        actual = get_tier_positions(0)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_get_tier_positions_goal(self):
        """Test goal tier position."""
        expected = [(6, 6)]
        actual = get_tier_positions(5)
        self.assertEqual(expected, actual)

    def test_get_tier_positions_arithmetics(self):
        """Test arithmetics tier positions."""
        actual = get_tier_positions(1)
        
        self.assertIn((0, 0), actual)
        self.assertIn((3, 1), actual)
        self.assertIn((1, 2), actual)
        
        expected_count = 15
        self.assertEqual(expected_count, len(actual))

    def test_get_tier_positions_algebra(self):
        """Test algebra tier positions."""
        actual = get_tier_positions(2)
        
        self.assertIn((4, 1), actual)
        self.assertIn((2, 2), actual)
        self.assertIn((3, 3), actual)
        
        expected_count = 13
        self.assertEqual(expected_count, len(actual))

    def test_get_tier_positions_calculus(self):
        """Test calculus tier positions."""
        actual = get_tier_positions(3)
        
        self.assertIn((4, 3), actual)
        self.assertIn((5, 4), actual)
        self.assertIn((3, 5), actual)
        
        expected_count = 9
        self.assertEqual(expected_count, len(actual))

    def test_get_tier_positions_number_theory(self):
        """Test number theory tier positions."""
        actual = get_tier_positions(4)
        expected = [(2, 6), (3, 6), (4, 5), (4, 6), (5, 5), (5, 6), (6, 4), (6, 5)]
        
        self.assertEqual(sorted(expected), sorted(actual))
