import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_result


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if the generated operator is one of the expected operators
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, ['+', '-', '*'])

    def test_function_C(self):
        # Test the calculation for addition
        result = calculate_result(5, 2, '+')
        self.assertEqual(result, ("5 + 2", 7))

        # Test the calculation for subtraction
        result = calculate_result(8, 5, '-')
        self.assertEqual(result, ("8 - 5", 3))

        # Test the calculation for multiplication
        result = calculate_result(2, 6, '*')
        self.assertEqual(result, ("2 * 6", 12))

        # Add more test cases as needed
        # test_cases = [
        #     (num1, num2, operator, expected_problem, expected_answer),
        #     ...
        # ]
        # for num1, num2, operator, expected_problem, expected_answer in test_cases:
        #     result = calculate_result(num1, num2, operator)
        #     self.assertEqual(result, (expected_problem, expected_answer))


if __name__ == "__main__":
    unittest.main()
