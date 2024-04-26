# Busca de CEP: Crie um programa que permita ao usuário buscar informações de um CEP específico.
from cep_search import CEPSearch


def main():
    cep_search = CEPSearch()

    print("Bem-vindo ao Buscador de CEP!")

    while True:
        cep = input("Digite o CEP que deseja buscar (ou 'sair' para encerrar): ")

        if cep.lower() == "sair":
            print("Obrigado por usar o Buscador de CEP!")
            break

        result = cep_search.search(cep)

        if result:
            print("Informações do CEP:")
            print(f"CEP: {result['cep']}")
            print(f"Logradouro: {result['logradouro']}")
            print(f"Complemento: {result['complemento']}")
            print(f"Bairro: {result['bairro']}")
            print(f"Cidade: {result['localidade']}")
            print(f"Estado: {result['uf']}")
        else:
            print("Nenhuma informação encontrada para este CEP.")


if __name__ == "__main__":
    main()
