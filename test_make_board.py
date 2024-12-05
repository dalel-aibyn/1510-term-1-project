from unittest import TestCase
from game import make_board


class Test(TestCase):
    def test_make_board_correct_dimensions(self):
        """Test board dimensions are correct."""
        expected_x = 7
        expected_y = 7
        board = make_board()
        self.assertEqual(expected_x, board["max_x"])
        self.assertEqual(expected_y, board["max_y"])

    def test_make_board_entrance_position(self):
        """Test entrance position has correct properties."""
        board = make_board()
        expected_name = "Entrance"
        expected_color = "blue"
        
        actual_name = board[(0, 6)]["tier_name"]
        actual_color = board[(0, 6)]["tier_color"]
        
        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected_color, actual_color)

    def test_make_board_goal_position(self):
        """Test goal position has correct properties."""
        board = make_board()
        expected_name = "Goal"
        expected_color = "purple"
        
        actual_name = board[(6, 6)]["tier_name"]
        actual_color = board[(6, 6)]["tier_color"]
        
        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected_color, actual_color)

    def test_make_board_sample_positions(self):
        """Test various positions have correct tier properties."""
        board = make_board()
        test_positions = [
            ((3, 1), "Arithmetics", "green"),
            ((4, 2), "Algebra", "yellow"),
            ((4, 3), "Calculus", "orange"),
            ((5, 5), "Number Theory", "red")
        ]
        
        for pos, expected_name, expected_color in test_positions:
            actual_name = board[pos]["tier_name"]
            actual_color = board[pos]["tier_color"]
            self.assertEqual(expected_name, actual_name)
            self.assertEqual(expected_color, actual_color)

    def test_make_board_invalid_dimensions(self):
        """Test board creation with invalid dimensions raises ValueError."""
        with self.assertRaises(ValueError):
            make_board(6, 7)
            
        with self.assertRaises(ValueError):
            make_board(7, 6)
            
        with self.assertRaises(ValueError):
            make_board(8, 8)
