from app.args_parser import parse_args


def main():
    url, output_filename = parse_args()
    print(url)
    print(output_filename)


if __name__ == '__main__':
    main()
