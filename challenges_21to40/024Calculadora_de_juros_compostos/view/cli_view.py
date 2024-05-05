from calculator.compound_interest_calculator import CompoundInterestCalculator


class CommandLineView:

    def run(self):
        print("Bem-vindo à Calculadora de Juros Compostos!")
        while True:
            principal = input("Digite o valor principal (ou 'sair' para encerrar): ")
            if principal.lower() == 'sair':
                print("Encerrando a aplicação...")
                break

            try:
                principal = float(principal)
                rate = float(input("Digite a taxa de juros (em decimal): "))
                time = int(input("Digite o tempo (em períodos): "))

                calculator = CompoundInterestCalculator(principal, rate, time)
                result = calculator.calculate_final_amount()
                print(f"O montante final é: {result}")
            except ValueError:
                print("Por favor, insira um valor numérico válido para o principal.")
