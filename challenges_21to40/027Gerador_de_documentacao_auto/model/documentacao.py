class Documentacao:
    def __init__(self, dados_codigo_fonte: list) -> None:
        """
         Inicializa um objeto Documentacao com os dados do código-fonte.
        :param dados_codigo_fonte: Dados do código-fonte obtidos pela classe CodigoFonte.
        """
        self.dados_codigo_fonte = dados_codigo_fonte

    def gerar_documentacao(self) -> str:
        """
        Gera a documentação a partir dos dados do código-fonte.
        :return: A documentação gerada.
        """
        documentacao = ""
        for class_name, method_name in self.dados_codigo_fonte:
            documentacao += f"Classe: {class_name}\n"
            documentacao += f"Método: {method_name}\n\n"
        return documentacao
