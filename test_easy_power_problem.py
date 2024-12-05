from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):
    @patch('game.randint', side_effect=[2, 2])
    @patch('game.random.randint', side_effect=[2, 2])
    def test_easy_power_problem_small(self, _, __):
        expected_problem = "2^2 = ?"
        expected_answer = 4
        
        actual_problem, actual_answer = game.easy_power_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[5, 3])
    @patch('game.random.randint', side_effect=[5, 3])
    def test_easy_power_problem_medium(self, _, __):
        expected_problem = "5^3 = ?"
        expected_answer = 125
        
        actual_problem, actual_answer = game.easy_power_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[10, 5])
    @patch('game.random.randint', side_effect=[10, 5])
    def test_easy_power_problem_large(self, _, __):
        expected_problem = "10^5 = ?"
        expected_answer = 100000
        
        actual_problem, actual_answer = game.easy_power_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)
