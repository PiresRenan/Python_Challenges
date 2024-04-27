# Analisador de URLs: Construa um programa que analise uma URL e retorne suas diferentes partes (protocolo, domínio,
# caminho, etc.).
from url_analyzer import URLAnalyzer


def main():
    print("Bem-vindo ao Analisador de URLs!")
    analyzer = URLAnalyzer()

    # Solicita ao usuário a URL
    url = input("Digite a URL que deseja analisar: ")

    # Analisa a URL
    scheme, netloc, path, params, query, fragment = analyzer.analyze_url(url)

    # Exibe as partes da URL
    print(f"Protocolo (Scheme): {scheme}")
    print(f"Local da Rede (Netloc): {netloc}")
    print(f"Caminho (Path): {path}")
    print(f"Parâmetros (Params): {params}")
    print(f"Consulta (Query): {query}")
    print(f"Fragmento (Fragment): {fragment}")


if __name__ == "__main__":
    main()
