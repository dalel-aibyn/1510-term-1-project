from unittest import TestCase
from game import has_adjacent_item


class Test(TestCase):
    def test_has_adjacent_item_no_items(self):
        """Test position with no adjacent items."""
        items = {(3, 3): "Textbook"}
        position = (0, 0)
        actual = has_adjacent_item(position, items)
        self.assertEqual(False, actual)

    def test_has_adjacent_item_north(self):
        """Test position with item to the north."""
        items = {(2, 1): "Calculator"}
        position = (2, 2)
        actual = has_adjacent_item(position, items)
        self.assertEqual(True, actual)

    def test_has_adjacent_item_east(self):
        """Test position with item to the east."""
        items = {(3, 2): "Manual"}
        position = (2, 2)
        actual = has_adjacent_item(position, items)
        self.assertEqual(True, actual)

    def test_has_adjacent_item_south(self):
        """Test position with item to the south."""
        items = {(2, 3): "Textbook"}
        position = (2, 2)
        actual = has_adjacent_item(position, items)
        self.assertEqual(True, actual)

    def test_has_adjacent_item_west(self):
        """Test position with item to the west."""
        items = {(1, 2): "Pen and paper"}
        position = (2, 2)
        actual = has_adjacent_item(position, items)
        self.assertEqual(True, actual)

    def test_has_adjacent_item_diagonal(self):
        """Test position with item only in diagonal position."""
        items = {(3, 3): "Calculator"}
        position = (2, 2)
        actual = has_adjacent_item(position, items)
        self.assertEqual(False, actual)

    def test_has_adjacent_item_multiple_items(self):
        """Test position with multiple items around."""
        items = {
            (2, 1): "Calculator",
            (3, 2): "Manual",
            (1, 2): "Textbook"
        }
        position = (2, 2)
        actual = has_adjacent_item(position, items)
        self.assertEqual(True, actual)
