from abc import ABC, abstractmethod


class ConverterStrategy(ABC):
    @abstractmethod
    def convert(self, value):
        pass
