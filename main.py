from app.args_parser import parse_args
from app.common.registry import registry
from app.common.validator import ValidationError
from app.common.http_client import http_client
from app.common.item import Item
from app.pikabu.parser import PikabuParser



def validate_url(url: str):
    try:
        validated_url = registry.get_validator().validate(url)
    except ValidationError as e:
        print(f'Ошибка валидации URL: {e}')
        quit()
    else:
        return validated_url


def parse_response(response: str, site_name: str) -> list[Item]:
    parser = registry.get_parser(site_name)
    return parser.parse(response)


def main():
    url, output_filename = parse_args()

    validated_url = validate_url(url)
    response = http_client.do_request(validated_url.url)

    # print(response)

    parsed_data = parse_response(response, validated_url.site_name)
    print(parsed_data[0].value)
    # pdf_file = create_pdf(parsed_data)
    # pdf_file.save(output_filename)


if __name__ == '__main__':
    main()
