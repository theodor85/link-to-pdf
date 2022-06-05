from abc import ABC, abstractmethod
from app.common import item

from app.common.item import Item, ItemType


class BaseParser(ABC):

    def __init__(self, soup_class: any) -> None:
        self.soup_class = soup_class

    @abstractmethod
    def parse(self, row_data: str) -> list[Item]:
        pass
