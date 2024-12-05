from unittest import TestCase
from unittest.mock import patch
from game import handle_item_pickup


class Test(TestCase):
    def test_handle_item_pickup_no_item(self):
        """Test when no item at position."""
        character = {"inventory": {"Textbook": False}}
        items = {(1, 1): "Textbook"}
        position = (0, 0)
        actual = handle_item_pickup(character, items, position)
        self.assertFalse(actual)

    @patch('builtins.print')
    def test_handle_item_pickup_new_item(self, mock_print):
        """Test picking up a new item."""
        character = {"inventory": {"Textbook": False}}
        items = {(1, 1): "Textbook"}
        position = (1, 1)
        
        actual = handle_item_pickup(character, items, position)
        
        self.assertTrue(actual)
        self.assertTrue(character["inventory"]["Textbook"])
        self.assertNotIn(position, items)

    @patch('builtins.print')
    def test_handle_item_pickup_duplicate_item(self, mock_print):
        """Test attempting to pick up already owned item."""
        character = {"inventory": {"Textbook": True}}
        items = {(1, 1): "Textbook"}
        position = (1, 1)
        
        actual = handle_item_pickup(character, items, position)
        
        self.assertTrue(actual)
        self.assertIn(position, items)

    @patch('builtins.print')
    def test_handle_item_pickup_all_items(self, mock_print):
        """Test picking up each type of item."""
        character = {
            "inventory": {
                "Pen and paper": False,
                "Textbook": False,
                "Manual": False,
                "Calculator": False
            }
        }
        items = {
            (0, 0): "Pen and paper",
            (1, 1): "Textbook",
            (2, 2): "Manual",
            (3, 3): "Calculator"
        }
        
        for pos, item in items.copy().items():
            actual = handle_item_pickup(character, items, pos)
            self.assertTrue(actual)
            self.assertTrue(character["inventory"][item])
            self.assertNotIn(pos, items)
