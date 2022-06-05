from bs4 import BeautifulSoup

from app.common.validator import Validator
from app.base.parser import BaseParser
from app.pikabu.parser import PikabuParser


class Registry:
    _REGISTRY: dict = {}

    def register(self, site_name: str, parser_class: object) -> None:
        self._REGISTRY[site_name] = {'parser_class': parser_class}

    def get_validator(self) -> Validator:
        return Validator(list(self._REGISTRY.keys()))

    def get_parser(self, site_name: str) -> BaseParser:
        return self._REGISTRY[site_name]['parser_class'](BeautifulSoup)


registry = Registry()
registry.register('pikabu.ru', PikabuParser)
