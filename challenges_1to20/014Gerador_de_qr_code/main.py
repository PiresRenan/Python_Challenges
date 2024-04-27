# Gerador de QR Code: Desenvolva um gerador de QR Code que transforme uma string em um código QR.
from qr_code_generator import QRCodeGenerator


def main():
    print("Bem-vindo ao Gerador de QR Code!")
    generator = QRCodeGenerator()
    data = input("Digite o texto para gerar o QR Code: ")
    file_name = input("Digite o nome do arquivo para salvar o QR Code (com extensão .png): ")

    # Gera o QR Code
    generator.generate_qr_code(data, file_name)
    print(f"O QR Code foi gerado com sucesso e salvo como '{file_name}'.")


if __name__ == "__main__":
    main()