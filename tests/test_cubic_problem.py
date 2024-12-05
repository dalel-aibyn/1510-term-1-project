from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):
    @patch('game.randint', side_effect=[1, 2, 3])
    @patch('game.random.randint', side_effect=[1, 2, 3])
    def test_cubic_problem_small_positive(self, _, __):
        expected_problem = "x³ - 6x² + 11x - 6 = 0"
        expected_answer = (1, 2, 3)

        actual_problem, actual_answer = game.cubic_problem()

        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[-1, -2, -3])
    @patch('game.random.randint', side_effect=[-1, -2, -3])
    def test_cubic_problem_small_negative(self, _, __):
        expected_problem = "x³ + 6x² + 11x + 6 = 0"
        expected_answer = (-1, -2, -3)

        actual_problem, actual_answer = game.cubic_problem()

        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[2, -1, 3])
    @patch('game.random.randint', side_effect=[2, -1, 3])
    def test_cubic_problem_mixed(self, _, __):
        expected_problem = "x³ - 4x² + 1x + 6 = 0"
        expected_answer = (2, -1, 3)

        actual_problem, actual_answer = game.cubic_problem()

        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)
