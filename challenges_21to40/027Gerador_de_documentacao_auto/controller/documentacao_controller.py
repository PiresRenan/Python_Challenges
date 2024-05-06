from model.codigo_fonte import CodigoFonte
from model.documentacao import Documentacao


class DocumentacaoController:
    def __init__(self, file_path: str) -> None:
        self.codigo_fonte = CodigoFonte(file_path)

    def gerar_documentacao(self) -> str:
        """
        Método para gerar a documentação a partir de um código-fonte Python.
        :param diretorio: O diretorio do projeto a ser documentado.
        :return: str: A documentação gerada.
        """
        classes_metodos = self.codigo_fonte.obter_classes_metodos()
        documentacao = Documentacao(classes_metodos)
        return documentacao.gerar_documentacao()
