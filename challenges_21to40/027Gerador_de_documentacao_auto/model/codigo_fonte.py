class CodigoFonte:
    def __init__(self, diretorio:str) -> None:
        """
        Inicializa um objeto CodigoFonte com o diretorio do projeto.
        :param diretorio: O diretorio do projeto.
        """
        self.diretorio = diretorio

    def obter_classes_metodos(self) -> list:
        """
        Obtém as classes e métodos do código-fonte.
        :return: Um dicionário contendo as classes e métodos do código-fonte.
        """
        classes_metodos = []
        with open(self.diretorio, 'r') as file:
            lines = file.readlines()
            current_class = None
            for line in lines:
                if line.startswith('class'):
                    current_class = line.split(' ')[1].split(':')[0]
                elif line.startswith('    def'):
                    if current_class:
                        method_name = line.split(' ')[5].split('(')[0]
                        classes_metodos.append((current_class, method_name))
        return classes_metodos
