from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass
class ValidatedUrl:
    url: str
    site_name: str


class ValidationError(BaseException):
    ''' Error while validate URL '''


class Validator:
    def __init__(self, site_names: list[str]) -> None:
        self.site_names = site_names

    def validate(self, url: str) -> ValidatedUrl:
        parsed_url = urlparse(url)

        if not (parsed_url.netloc and parsed_url.path):
            raise ValidationError('Wrong URL format!')
        elif not (parsed_url.netloc in self.site_names):
            raise ValidationError(f'I can parse only sites: {self.site_names}')

        return ValidatedUrl(url=url, site_name=parsed_url.netloc)
