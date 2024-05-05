import unittest

from calculator.compound_interest_calculator import CompoundInterestCalculator


class TestCompoundInterestCalculator(unittest.TestCase):
    def test_calculate_final_amount(self):
        principal = 1000
        interest_rate = 0.05
        time = 5
        expected_final_amount = 1000 * (1 + 0.05) ** 5
        calculator = CompoundInterestCalculator(principal, interest_rate, time)
        final_amount = calculator.calculate_final_amount()
        self.assertAlmostEqual(final_amount, expected_final_amount, delta=0.01)

    def test_principal_zero(self):
        principal = 0
        interest_rate = 0.05
        time = 10
        calculator = CompoundInterestCalculator(principal, interest_rate, time)
        result = calculator.calculate_final_amount()
        self.assertEqual(result, 0)

    def test_rate_zero(self):
        principal = 1000
        interest_rate = 0
        time = 10
        calculator = CompoundInterestCalculator(principal, interest_rate, time)
        result = calculator.calculate_final_amount()
        self.assertEqual(result, principal)

    def test_time_zero(self):
        principal = 1000
        interest_rate = 0.05
        time = 0
        calculator = CompoundInterestCalculator(principal, interest_rate, time)
        result = calculator.calculate_final_amount()
        self.assertEqual(result, principal)


if __name__ == '__main__':
    unittest.main()
