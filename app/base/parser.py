from abc import ABC, abstractmethod


class BaseParser(ABC):
    @abstractmethod
    def parse(self, row_data):
        pass
