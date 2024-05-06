import unittest
from model.models import CreditCard, Validator


class TestCreditCard(unittest.TestCase):
    def test_credit_card_creation(self):
        card_number = "1234567890123456"
        card = CreditCard(card_number)
        self.assertEqual(card.number, card_number)


class TestValidator(unittest.TestCase):
    def test_validate_credit_card_valid(self):
        card_number = "5330517927376254"
        card = CreditCard(card_number)
        self.assertTrue(Validator.validate_credit_card(card))

    def test_validate_credit_card_invalid(self):
        card_number = "4025007142319317"
        card = CreditCard(card_number)
        self.assertFalse(Validator.validate_credit_card(card))

    def test_validate_credit_card_non_numeric(self):
        card_number = "1234-5678-9012-3456"
        card = CreditCard(card_number)
        self.assertFalse(Validator.validate_credit_card(card))

    def test_validate_credit_card_invalid_length(self):
        card_number = "123456789012345"
        card = CreditCard(card_number)
        self.assertFalse(Validator.validate_credit_card(card))


if __name__ == "__main__":
    unittest.main()
