from unittest import TestCase
from game import validate_move


class Test(TestCase):
    def test_validate_move_valid_north(self):
        """Test valid move north."""
        board = {"max_x": 7, "max_y": 7}
        character = {"row": 3, "column": 3}
        direction = (-1, 0)
        expected = (-1, 0)
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_valid_south(self):
        """Test valid move south."""
        board = {"max_x": 7, "max_y": 7}
        character = {"row": 3, "column": 3}
        direction = (1, 0)
        expected = (1, 0)
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_valid_east(self):
        """Test valid move east."""
        board = {"max_x": 7, "max_y": 7}
        character = {"row": 3, "column": 3}
        direction = (0, 1)
        expected = (0, 1)
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_valid_west(self):
        """Test valid move west."""
        board = {"max_x": 7, "max_y": 7}
        character = {"row": 3, "column": 3}
        direction = (0, -1)
        expected = (0, -1)
        actual = validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_invalid_north(self):
        """Test invalid move north off board."""
        board = {"max_x": 7, "max_y": 7}
        character = {"row": 0, "column": 3}
        direction = (-1, 0)
        actual = validate_move(board, character, direction)
        self.assertFalse(actual)

    def test_validate_move_invalid_south(self):
        """Test invalid move south off board."""
        board = {"max_x": 7, "max_y": 7}
        character = {"row": 6, "column": 3}
        direction = (1, 0)
        actual = validate_move(board, character, direction)
        self.assertFalse(actual)

    def test_validate_move_invalid_east(self):
        """Test invalid move east off board."""
        board = {"max_x": 7, "max_y": 7}
        character = {"row": 3, "column": 6}
        direction = (0, 1)
        actual = validate_move(board, character, direction)
        self.assertFalse(actual)

    def test_validate_move_invalid_west(self):
        """Test invalid move west off board."""
        board = {"max_x": 7, "max_y": 7}
        character = {"row": 3, "column": 0}
        direction = (0, -1)
        actual = validate_move(board, character, direction)
        self.assertFalse(actual)
