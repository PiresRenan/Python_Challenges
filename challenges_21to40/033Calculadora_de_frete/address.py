class Address:
    def __init__(self, zip, street, city, state):
        self.zip = zip
        self.street = street
        self.city = city
        self.state = state

    def validate_cep(self):
        # Implemente a validação do formato do CEP aqui
        pass

    def format_address(self):
        # Implemente a formatação do endereço aqui
        pass

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, CEP: {self.cep}"