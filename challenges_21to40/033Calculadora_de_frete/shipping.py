class ShippingCalculator:
    def __init__(self, origin_address, destination_address, weight, shipping_type):
        self.origin_address = origin_address
        self.destination_address = destination_address
        self.weight = weight
        self.shipping_type = shipping_type

    def calculate_shipping_cost(self):
        # Implemente o cálculo do custo de frete aqui
        pass

    def __str__(self):
        return f"Shipping from {self.origin_address} to {self.destination_address}, Weight: {self.weight} kg, Type: {self.shipping_type}"