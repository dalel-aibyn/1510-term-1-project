from unittest import TestCase
from unittest.mock import patch
from game import place_tier_items


def alternating_values():
    """Generator that alternates valid values."""
    valid_positions = [(1, 1), (1, 2)]
    for _ in range(70):
        for pos in valid_positions:
            yield pos


class Test(TestCase):
    @patch('random.choice', side_effect=[(1, 1), (3, 3)])
    def test_place_tier_items_two_items(self, _):
        """Test placing two items in non-adjacent positions."""
        tier_positions = [(1, 1), (2, 2), (3, 3), (4, 4)]
        items_locations = {}
        
        place_tier_items(tier_positions, "Textbook", 2, items_locations)
        
        expected_locations = {(1, 1): "Textbook", (3, 3): "Textbook"}
        self.assertEqual(expected_locations, items_locations)

    @patch('random.choice', side_effect=alternating_values())
    def test_place_tier_items_adjacent_positions(self, _):
        """Test attempting to place items in adjacent positions."""
        tier_positions = [(1, 1), (1, 2)]
        items_locations = {}
        
        place_tier_items(tier_positions, "Manual", 2, items_locations)
        
        expected_locations = {(1, 1): "Manual"}
        self.assertEqual(expected_locations, items_locations)

    @patch('random.choice', return_value=(1, 1))
    def test_place_tier_items_single_item(self, _):
        """Test placing a single item."""
        tier_positions = [(1, 1), (2, 2), (3, 3)]
        items_locations = {}
        
        place_tier_items(tier_positions, "Calculator", 1, items_locations)
        
        expected_locations = {(1, 1): "Calculator"}
        self.assertEqual(expected_locations, items_locations)

    @patch('random.choice', side_effect=[(1, 1)])
    def test_place_tier_items_empty_positions(self, _):
        """Test placing items with empty tier positions."""
        tier_positions = []
        items_locations = {}
        
        place_tier_items(tier_positions, "Textbook", 2, items_locations)
        
        expected_locations = {}
        self.assertEqual(expected_locations, items_locations)

    @patch('random.choice', side_effect=[(1, 1)])
    def test_place_tier_items_zero_quantity(self, _):
        """Test placing zero items."""
        tier_positions = [(1, 1), (2, 2)]
        items_locations = {}
        
        place_tier_items(tier_positions, "Manual", 0, items_locations)
        
        expected_locations = {}
        self.assertEqual(expected_locations, items_locations)

    @patch('random.choice', side_effect=[(1, 1)])
    def test_place_tier_items_existing_items(self, _):
        """Test placing items with existing items on board."""
        tier_positions = [(1, 1), (2, 2), (3, 3)]
        items_locations = {(4, 4): "Calculator"}
        
        place_tier_items(tier_positions, "Textbook", 1, items_locations)
        
        expected_locations = {(4, 4): "Calculator", (1, 1): "Textbook"}
        self.assertEqual(expected_locations, items_locations)
