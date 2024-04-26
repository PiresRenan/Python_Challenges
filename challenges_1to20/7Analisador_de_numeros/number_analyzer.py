import statistics


class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_mean(self):
        return sum(self.numbers) / len(self.numbers)

    def calculate_median(self):
        return statistics.median(self.numbers)

    def calculate_standard_deviation(self):
        return statistics.stdev(self.numbers)
