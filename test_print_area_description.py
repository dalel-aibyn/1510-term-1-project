from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):
    @patch('builtins.print')
    def test_print_area_description_entrance_first_visit(self, mock_print):
        expected = [
            '\nYou stand at the beginning of your mathematical journey.'
        ]

        game.print_area_description("Entrance", first_visit=True)

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_print_area_description_entrance_revisit(self, mock_print):
        expected = [
            '\nThe familiar territory of addition and subtraction surrounds you.'
        ]

        game.print_area_description("Entrance", first_visit=False)

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_print_area_description_arithmetics_first_visit(self, mock_print):
        expected = [
            '\nNumbers float in the air around you. The fundamental laws of mathematics are strong here.'
        ]

        game.print_area_description("Arithmetics", first_visit=True)

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_print_area_description_algebra_first_visit(self, mock_print):
        expected = [
            '\nLetters and numbers intertwine in the space around you.'
        ]

        game.print_area_description("Algebra", first_visit=True)

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_print_area_description_calculus_revisit(self, mock_print):
        expected = [
            '\nFunctions flow like rivers around you.'
        ]

        game.print_area_description("Calculus", first_visit=False)

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_print_area_description_number_theory_first_visit(self, mock_print):
        expected = [
            '\nThe deepest mysteries await.'
        ]

        game.print_area_description("Number Theory", first_visit=True)

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_print_area_description_number_theory_revisit(self, mock_print):
        expected = [
            '\nThe very foundations of numbers surround you.'
        ]

        game.print_area_description("Number Theory", first_visit=False)

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_print_area_description_invalid_area(self, mock_print):
        expected = []

        game.print_area_description("Invalid Area", first_visit=True)

        actual = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected, actual)
