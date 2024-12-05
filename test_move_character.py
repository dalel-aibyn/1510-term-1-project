from unittest import TestCase
from game import move_character


class Test(TestCase):
    def test_move_character_north(self):
        """Test moving character north."""
        character = {"row": 3, "column": 3, "steps_taken": 0}
        direction = (-1, 0)
        move_character(character, direction)
        self.assertEqual(2, character["row"])
        self.assertEqual(3, character["column"])
        self.assertEqual(1, character["steps_taken"])

    def test_move_character_south(self):
        """Test moving character south."""
        character = {"row": 3, "column": 3, "steps_taken": 0}
        direction = (1, 0)
        move_character(character, direction)
        self.assertEqual(4, character["row"])
        self.assertEqual(3, character["column"])
        self.assertEqual(1, character["steps_taken"])

    def test_move_character_east(self):
        """Test moving character east."""
        character = {"row": 3, "column": 3, "steps_taken": 0}
        direction = (0, 1)
        move_character(character, direction)
        self.assertEqual(3, character["row"])
        self.assertEqual(4, character["column"])
        self.assertEqual(1, character["steps_taken"])

    def test_move_character_west(self):
        """Test moving character west."""
        character = {"row": 3, "column": 3, "steps_taken": 0}
        direction = (0, -1)
        move_character(character, direction)
        self.assertEqual(3, character["row"])
        self.assertEqual(2, character["column"])
        self.assertEqual(1, character["steps_taken"])

    def test_move_character_multiple_moves(self):
        """Test multiple character movements."""
        character = {"row": 3, "column": 3, "steps_taken": 0}
        moves = [(0, 1), (1, 0), (-1, 0)]
        for direction in moves:
            move_character(character, direction)
        self.assertEqual(3, character["row"])
        self.assertEqual(4, character["column"])
        self.assertEqual(3, character["steps_taken"])
