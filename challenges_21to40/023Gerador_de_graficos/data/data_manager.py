import pandas as pd


class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """
        Carrega os dados de um arquivo CSV utilizando o pandas.
        Args:
            file_path (str): O caminho para o arquivo CSV.
        Returns:
            pandas.DataFrame: Um DataFrame contendo os dados carregados.
        """
        try:
            df = pd.read_csv(self.file_path, usecols=lambda column: 'Unnamed' not in column)
            return df
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {self.file_path}")
            return None

    def process_data(self, raw_data):
        """
        Processa os dados brutos para o formato adequado para geração de gráficos.
        Args:
            raw_data (pandas.DataFrame): Um DataFrame contendo os dados brutos.
        Returns:
            dict: Um dicionário contendo os dados processados.
        """
        processed_data = {'child_IQ_score': raw_data['child_IQ_score'].tolist(),
                          'mother_education': raw_data['mother_education'].tolist(),
                          'mother_iq': raw_data['mother_iq'].tolist(), 'mother_job': raw_data['mother_job'].tolist(),
                          'mother_age': raw_data['mother_age'].tolist()}
        return processed_data
