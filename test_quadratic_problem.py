from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):
    @patch('game.randint', side_effect=[1, 2])
    @patch('game.random.randint', side_effect=[1, 2])
    def test_quadratic_problem_small_positive(self, _, __):
        expected_problem = "x² - 3x + 2 = 0"
        expected_answer = (1, 2)
        
        actual_problem, actual_answer = game.quadratic_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[-2, -3])
    @patch('game.random.randint', side_effect=[-2, -3])
    def test_quadratic_problem_small_negative(self, _, __):
        expected_problem = "x² + 5x + 6 = 0"
        expected_answer = (-2, -3)
        
        actual_problem, actual_answer = game.quadratic_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[5, -4])
    @patch('game.random.randint', side_effect=[5, -4])
    def test_quadratic_problem_mixed(self, _, __):
        expected_problem = "x² - 1x - 20 = 0"
        expected_answer = (5, -4)
        
        actual_problem, actual_answer = game.quadratic_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)