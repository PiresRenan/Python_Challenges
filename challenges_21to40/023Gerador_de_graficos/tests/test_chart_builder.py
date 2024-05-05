import unittest

from visualization import chart_builder
from visualization.chart_builder import ChartBuilder


class TestChartBuilder(unittest.TestCase):
    def setUp(self):
        file_path = '../data/kid_iq.csv'
        self.chart_builder = ChartBuilder(file_path)

    def test_build_scatter_plot(self):
        self.chart_builder.build_scatter_plot()

    def test_build_bar_chart(self):
        self.chart_builder.build_bar_chart()

    def test_build_line_chart(self):
        self.chart_builder.build_line_chart()


if __name__ == '__main__':
    unittest.main()
