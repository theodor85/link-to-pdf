from typing import Any

import requests
from requests import RequestException


class HttpError(BaseException):
    pass


class HttpClient:
    def __init__(self, req: Any) -> None:
        self.req = req

    def do_request(self, url: str) -> str:
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/101.0.4951.54 '
                          'Safari/537.36',
        }

        try:
            response = self.req.get(url, headers=headers)
        except RequestException as e:
            raise HttpError(f'Ошибка при выполнении запроса: {e}')
        else:
            if not response.status_code == 200:
                raise HttpError(
                    f'Запрос завершился ошибкой со статусом '
                    f'{response.status_code}')
            return response.text


http_client = HttpClient(requests)
