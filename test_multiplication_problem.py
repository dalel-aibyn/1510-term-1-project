from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):
    @patch('game.randint', side_effect=[1, 1, 1])
    @patch('game.random.randint', side_effect=[1, 1, 1])
    def test_multiplication_problem_ones(self, _, __):
        expected_problem = "1 * 1 * 1 = ?"
        expected_answer = 1
        
        actual_problem, actual_answer = game.multiplication_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[2, 3, 4])
    @patch('game.random.randint', side_effect=[2, 3, 4])
    def test_multiplication_problem_small(self, _, __):
        expected_problem = "2 * 3 * 4 = ?"
        expected_answer = 24
        
        actual_problem, actual_answer = game.multiplication_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[10, 20, 30])
    @patch('game.random.randint', side_effect=[10, 20, 30])
    def test_multiplication_problem_medium(self, _, __):
        expected_problem = "10 * 20 * 30 = ?"
        expected_answer = 6000
        
        actual_problem, actual_answer = game.multiplication_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[100, 90, 80])
    @patch('game.random.randint', side_effect=[100, 90, 80])
    def test_multiplication_problem_large(self, _, __):
        expected_problem = "100 * 90 * 80 = ?"
        expected_answer = 720000
        
        actual_problem, actual_answer = game.multiplication_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)
