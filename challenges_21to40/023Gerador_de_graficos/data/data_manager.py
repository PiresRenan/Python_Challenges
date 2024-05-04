class DataManager:
    def load_data(self, file_path):
        """
        Carrega os dados de um arquivo CSV.
        Args:
            file_path (str): O caminho para o arquivo CSV.
        Returns:
            list: Uma lista de tuplas representando os dados carregados.
        """
        data = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        data.append(tuple(line.split(',')))
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {file_path}")
        return data

    def process_data(self, raw_data):
        """
        Processa os dados brutos para formato adequado para geração de gráficos.
        Args:
            raw_data (list): Uma lista de tuplas representando os dados brutos.
        Returns:
            dict: Um dicionário contendo os dados processados.
        """
        labels = [item[0] for item in raw_data]
        values = [int(item[1]) for item in raw_data]
        return {'labels': labels, 'values': values}