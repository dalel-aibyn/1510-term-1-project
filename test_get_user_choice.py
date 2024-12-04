from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice


class Test(TestCase):
    @patch('builtins.input', return_value='north')
    def test_get_user_choice_cardinal_direction_lowercase(self, mock_input):
        expected = 'north'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='SOUTH')
    def test_get_user_choice_cardinal_direction_uppercase(self, mock_input):
        expected = 'SOUTH'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='e')
    def test_get_user_choice_cardinal_direction_one_letter(self, mock_input):
        expected = 'e'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='right')
    def test_get_user_choice_direction(self, mock_input):
        expected = 'right'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='Hahaha!')
    def test_get_user_choice_irrelevant_input(self, mock_input):
        expected = 'Hahaha!'
        actual = get_user_choice()
        self.assertEqual(expected, actual)
