class TemperatureConverter:
    def __init__(self, temperature, scale):
        self.temperature = temperature
        self.scale = scale.lower()

    def to_celsius(self):
        if self.scale == 'c':
            return self.temperature
        elif self.scale == 'f':
            return (self.temperature - 32) * 5/9
        elif self.scale == 'k':
            return self.temperature - 273.15
        else:
            raise ValueError("Escala não suportada. Por favor, use 'C', 'F', ou 'K'.")

    def to_fahrenheit(self):
        if self.scale == 'c':
            return self.temperature * 9/5 + 32
        elif self.scale == 'f':
            return self.temperature
        elif self.scale == 'k':
            return (self.temperature - 273.15) * 9/5 + 32
        else:
            raise ValueError("Escala não suportada. Por favor, use 'C', 'F', ou 'K'.")

    def to_kelvin(self):
        if self.scale == 'c':
            return self.temperature + 273.15
        elif self.scale == 'f':
            return (self.temperature - 32) * 5/9 + 273.15
        elif self.scale == 'k':
            return self.temperature
        else:
            raise ValueError("Escala não suportada. Por favor, use 'C', 'F', ou 'K'.")
