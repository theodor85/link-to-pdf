from dataclasses import dataclass
from enum import Enum


class ItemType(Enum):
    TEXT = 1
    HEADER = 2
    PICTURE = 3
    VIDEO = 4


@dataclass
class Item:
    item_type: ItemType
    value: str
