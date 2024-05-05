import matplotlib.pyplot as plt
import pandas as pd

from data.data_manager import DataManager


class ChartBuilder:
    def __init__(self, csv_file_path):
        self.data_processor = DataManager(csv_file_path)
        self.data = self.data_processor.load_data()
        self.processed_data = self.data_processor.process_data(self.data)

    def build_scatter_plot(self):
        """
        Constrói um gráfico de dispersão relacionando child_IQ_score com mother_age.
        """
        child_iq_score = self.data['child_IQ_score']
        mother_age = self.data['mother_age']

        plt.figure(figsize=(8, 6))
        plt.scatter(mother_age, child_iq_score, color='blue', alpha=0.5)
        plt.title('Relação entre Child IQ Score e Idade da Mãe')
        plt.xlabel('Idade da Mãe')
        plt.ylabel('Child IQ Score')
        plt.grid(True)
        plt.show()

    def build_bar_chart(self):
        """
        Constrói um gráfico de barras.
        """
        plt.figure(figsize=(8, 6))
        plt.bar(self.data['mother_age'], self.data['child_IQ_score'])
        plt.title('Gráfico de Barras')
        plt.xlabel('Idade Mãe')
        plt.ylabel('Pontos de QI crianças')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def build_line_chart(self):
        """
        Constrói um gráfico de linhas.
        """
        sorted_data = self.data.groupby('mother_age')['child_IQ_score'].mean().reset_index().sort_values(by='mother_age')
        plt.figure(figsize=(8, 6))
        plt.plot(sorted_data['mother_age'], sorted_data['child_IQ_score'], color="red", marker="o")
        plt.title("QI criança x idade mãe", fontsize=14)
        plt.xlabel("Idade Mãe", fontsize=14)
        plt.ylabel("QI criança", fontsize=14)
        plt.grid(True)
        plt.show()

    def build_histogram(self):
        """
        Constrói um histograma.
        """
        plt.figure(figsize=(8, 6))
        plt.hist(self.processed_data['child_IQ_score'], bins=10, color='skyblue', edgecolor='black')
        plt.title('Histograma de Pontuação de QI')
        plt.xlabel('Pontuação de QI')
        plt.ylabel('Frequência')
        plt.grid(True)
        plt.show()
