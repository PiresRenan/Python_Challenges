from unit_converters import (
    MetersToKilometersConverter, MetersToCentimetersConverter, MetersToMillimetersConverter,
    MetersToMilesConverter, MetersToYardsConverter, MetersToInchesConverter,
    GallonsToLitersConverter, KilosToGramsConverter, KilosToTonsConverter,
    LitersToGallonsConverter
)


class ConverterFactory:
    @staticmethod
    def create_converter(choice):
        if choice == "1":
            return MetersToKilometersConverter()
        elif choice == "2":
            return MetersToCentimetersConverter()
        elif choice == "3":
            return MetersToMillimetersConverter()
        elif choice == "4":
            return MetersToMilesConverter()
        elif choice == "5":
            return MetersToYardsConverter()
        elif choice == "6":
            return MetersToInchesConverter()
        elif choice == "7":
            return GallonsToLitersConverter()
        elif choice == "8":
            return KilosToGramsConverter()
        elif choice == "9":
            return KilosToTonsConverter()
        elif choice == "10":
            return LitersToGallonsConverter()
        else:
            return None
