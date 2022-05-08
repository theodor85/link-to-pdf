from app.args_parser import parse_args
from app.common.registry import registry
from app.common.validator import ValidationError


def validate_url(url: str):
    try:
        validated_url = registry.get_validator().validate(url)
    except ValidationError as e:
        print(f'Ошибка валидации URL: {e}')
    else:
        return validated_url


def main():
    url, output_filename = parse_args()

    validated_url = validate_url(url)

    print(validated_url)

    # response = do_request(validated_url)


    # parsed_data = parse_response(response)
    # pdf_file = create_pdf(parsed_data)
    # pdf_file.save(output_filename)
    # print(validated_url, output_filename)
    # print(url)
    # print(output_filename)


if __name__ == '__main__':
    main()
