from unittest import TestCase
from game import determine_tier


class Test(TestCase):
    def test_determine_tier_entrance_area(self):
        """Test entrance area positions."""
        expected = 0
        actual = determine_tier(0, 5)
        self.assertEqual(expected, actual, "Main entrance position")
        
        expected = 0
        actual = determine_tier(1, 6)
        self.assertEqual(expected, actual, "Secondary entrance position")
        
    def test_determine_tier_goal_area(self):
        """Test goal position."""
        expected = 5
        actual = determine_tier(6, 6)
        self.assertEqual(expected, actual, "Goal position at bottom right")
        
    def test_determine_tier_arithmetics(self):
        """Test arithmetics area positions."""
        expected = 1
        actual = determine_tier(0, 0)
        self.assertEqual(expected, actual, "Top left corner of arithmetics")
        
        expected = 1
        actual = determine_tier(3, 1)
        self.assertEqual(expected, actual, "Upper area of arithmetics")
        
        expected = 1
        actual = determine_tier(1, 2)
        self.assertEqual(expected, actual, "Left side of arithmetics")
        
        expected = 1
        actual = determine_tier(0, 4)
        self.assertEqual(expected, actual, "Left column of arithmetics")
        
    def test_determine_tier_algebra(self):
        """Test algebra area positions."""
        expected = 2
        actual = determine_tier(4, 1)
        self.assertEqual(expected, actual, "Upper right of algebra")
        
        expected = 2
        actual = determine_tier(2, 2)
        self.assertEqual(expected, actual, "Middle right of algebra")
        
        expected = 2
        actual = determine_tier(3, 3)
        self.assertEqual(expected, actual, "Center of algebra")
        
        expected = 2
        actual = determine_tier(2, 4)
        self.assertEqual(expected, actual, "Lower middle of algebra")
        
    def test_determine_tier_calculus(self):
        """Test calculus area positions."""
        expected = 3
        actual = determine_tier(4, 3)
        self.assertEqual(expected, actual, "Upper right of calculus")
        
        expected = 3
        actual = determine_tier(5, 4)
        self.assertEqual(expected, actual, "Middle right of calculus")
        
        expected = 3
        actual = determine_tier(3, 5)
        self.assertEqual(expected, actual, "Lower middle of calculus")
        
    def test_determine_tier_number_theory(self):
        """Test number theory area positions."""
        expected = 4
        actual = determine_tier(5, 5)
        self.assertEqual(expected, actual, "Upper right corner of number theory")
        
        expected = 4
        actual = determine_tier(4, 6)
        self.assertEqual(expected, actual, "Lower right of number theory")
        
        expected = 4
        actual = determine_tier(5, 6)
        self.assertEqual(expected, actual, "Bottom right of number theory")
        
    def test_determine_tier_invalid_position(self):
        """Test invalid board positions."""
        with self.assertRaises(ValueError):
            determine_tier(-1, 0)
            
        with self.assertRaises(ValueError):
            determine_tier(0, -1)
            
        with self.assertRaises(ValueError):
            determine_tier(7, 0)
            
        with self.assertRaises(ValueError):
            determine_tier(0, 7) 