import unittest
from address import Address
from shipping import ShippingCalculator


class TestShippingCalculator(unittest.TestCase):
    def setUp(self):
        self.origin_address = Address("12345-678", "Rua A", "Cidade A", "Estado A")
        self.destination_address = Address("98765-432", "Rua B", "Cidade B", "Estado B")
        self.weight = 5
        self.shipping_type = "Standard"

    def test_shipping_calculator_initialization(self):
        shipping_calculator = ShippingCalculator(self.origin_address, self.destination_address, self.weight, self.shipping_type)
        self.assertEqual(shipping_calculator.origin_address, self.origin_address)
        self.assertEqual(shipping_calculator.destination_address, self.destination_address)
        self.assertEqual(shipping_calculator.weight, self.weight)
        self.assertEqual(shipping_calculator.shipping_type, self.shipping_type)

    # Aqui você pode adicionar mais testes para diferentes cenários de cálculo de frete

if __name__ == '__main__':
    unittest.main()