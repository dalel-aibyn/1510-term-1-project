from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):
    @patch('game.randint', side_effect=[5, 5, 2])
    @patch('game.random.randint', side_effect=[5, 5, 2])
    def test_hard_power_problem_small(self, _, __):
        expected_problem = "2 * 5^5 = ?"
        expected_answer = 6250
        
        actual_problem, actual_answer = game.hard_power_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[10, 6, 5])
    @patch('game.random.randint', side_effect=[10, 6, 5])
    def test_hard_power_problem_medium(self, _, __):
        expected_problem = "5 * 10^6 = ?"
        expected_answer = 5000000
        
        actual_problem, actual_answer = game.hard_power_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)

    @patch('game.randint', side_effect=[25, 10, 9])
    @patch('game.random.randint', side_effect=[25, 10, 9])
    def test_hard_power_problem_large(self, _, __):
        expected_problem = "9 * 25^10 = ?"
        expected_answer = 9 * (25 ** 10)
        
        actual_problem, actual_answer = game.hard_power_problem()
        
        self.assertEqual(expected_problem, actual_problem)
        self.assertEqual(expected_answer, actual_answer)
