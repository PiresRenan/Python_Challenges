from converter_strategy import ConverterStrategy


class MetersToKilometersConverter(ConverterStrategy):
    def convert(self, meters):
        return meters / 1000


class MetersToCentimetersConverter(ConverterStrategy):
    def convert(self, meters):
        return meters * 100


class MetersToMillimetersConverter(ConverterStrategy):
    def convert(self, meters):
        return meters * 1000


class MetersToMilesConverter(ConverterStrategy):
    def convert(self, meters):
        return meters / 1609.34


class MetersToYardsConverter(ConverterStrategy):
    def convert(self, meters):
        return meters * 1.09361


class MetersToInchesConverter(ConverterStrategy):
    def convert(self, meters):
        return meters * 39.3701


class GallonsToLitersConverter(ConverterStrategy):
    def convert(self, gallons):
        return gallons * 3.78541


class KilosToGramsConverter(ConverterStrategy):
    def convert(self, kilos):
        return kilos * 1000


class KilosToTonsConverter(ConverterStrategy):
    def convert(self, kilos):
        return kilos / 1000


class LitersToGallonsConverter(ConverterStrategy):
    def convert(self, liters):
        return liters / 3.78541
