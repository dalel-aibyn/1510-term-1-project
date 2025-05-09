from unittest import TestCase
from game import generate_term3


class Test(TestCase):
    def test_generate_term3_solvable_negative(self):
        """Test generating negative third term for solvable problem."""
        term1_value = 5.0
        term2_value = 10.0
        expected_value = -15.0
        expected_string = "- 15.0"
        
        actual_value, actual_string = generate_term3(term1_value, term2_value)
        
        self.assertEqual(expected_value, actual_value)
        self.assertEqual(expected_string, actual_string)

    def test_generate_term3_solvable_positive(self):
        """Test generating positive third term for solvable problem."""
        term1_value = -5.0
        term2_value = -10.0
        expected_value = 15.0
        expected_string = "+ 15.0"

        actual_value, actual_string = generate_term3(term1_value, term2_value)

        self.assertEqual(expected_value, actual_value)
        self.assertEqual(expected_string, actual_string)

    def test_generate_term3_zero_sum(self):
        """Test generating third term that results in zero-sum."""
        term1_value = 5.0
        term2_value = -5.0
        expected_value = 0.0
        expected_string = "+ 0.0"
        
        actual_value, actual_string = generate_term3(term1_value, term2_value)
        
        self.assertEqual(expected_value, actual_value)
        self.assertEqual(expected_string, actual_string)
