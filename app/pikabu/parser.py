from app.base.parser import BaseParser
from app.common.item import Item, ItemType


class PikabuParser(BaseParser):
    def parse(self, row_data: str) -> list[Item]:
        soup = self.soup_class(row_data, 'html.parser')
        text = soup.find('span', class_="story__title-link").get_text()
        return [Item(item_type=ItemType.HEADER, value=text)]
