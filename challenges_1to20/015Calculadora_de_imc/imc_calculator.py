class IMCCalculator:
    def calculate_imc(self, weight, height):
        # Calcula o IMC
        imc = weight / (height ** 2)
        return imc
