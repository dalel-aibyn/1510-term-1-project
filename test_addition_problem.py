from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):

    @patch('game.randint', side_effect=[0, 0, 0])
    @patch('game.random.randint', side_effect=[0, 0, 0])
    def test_addition_problem_all_zeros(self, _, __):
        expected_problem = "0 + 0 + 0 = ?"
        expected_answer = 0
        
        actual_problem, actual_answer = game.addition_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[5, 3, 2])
    @patch('game.random.randint', side_effect=[5, 3, 2])
    def test_addition_problem_small_positive(self, _, __):
        expected_problem = "5 + 3 + 2 = ?"
        expected_answer = 10
        
        actual_problem, actual_answer = game.addition_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[100, 200, 300])
    @patch('game.random.randint', side_effect=[100, 200, 300])
    def test_addition_problem_medium_positive(self, _, __):
        expected_problem = "100 + 200 + 300 = ?"
        expected_answer = 600
        
        actual_problem, actual_answer = game.addition_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[-5, -3, -2])
    @patch('game.random.randint', side_effect=[-5, -3, -2])
    def test_addition_problem_small_negative(self, _, __):
        expected_problem = "-5 - 3 - 2 = ?"
        expected_answer = -10
        
        actual_problem, actual_answer = game.addition_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[5, -3, 2])
    @patch('game.random.randint', side_effect=[5, -3, 2])
    def test_addition_problem_mixed(self, _, __):
        expected_problem = "5 - 3 + 2 = ?"
        expected_answer = 4
        
        actual_problem, actual_answer = game.addition_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)
