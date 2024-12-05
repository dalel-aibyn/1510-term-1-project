from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice


class Test(TestCase):
    @patch('builtins.input', return_value='n')
    def test_get_user_choice_north(self, _):
        """Test north direction input."""
        expected = (-1, 0)
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='s')
    def test_get_user_choice_south(self, _):
        """Test south direction input."""
        expected = (1, 0)
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='e')
    def test_get_user_choice_east(self, _):
        """Test east direction input."""
        expected = (0, 1)
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='w')
    def test_get_user_choice_west(self, _):
        """Test west direction input."""
        expected = (0, -1)
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['x', 'n'])
    @patch('builtins.print')
    def test_get_user_choice_invalid_then_valid(self, mock_print, _):
        """Test invalid input followed by valid input."""
        expected = (-1, 0)
        actual = get_user_choice()
        self.assertEqual(expected, actual)
        mock_print.assert_called_once()

    @patch('builtins.input', return_value='N')
    def test_get_user_choice_uppercase(self, _):
        """Test uppercase input is accepted."""
        expected = (-1, 0)
        actual = get_user_choice()
        self.assertEqual(expected, actual)
