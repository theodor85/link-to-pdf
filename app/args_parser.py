import argparse


def parse_args():
    arg_parser = argparse.ArgumentParser(
        description='Convert data from url to pdf-file.')
    arg_parser.add_argument('-u', '--url', nargs=1, required=True)
    arg_parser.add_argument(
        '-o', '--output', nargs=1, required=False, default='output.pdf')

    args = arg_parser.parse_args()
    return args.url[0], args.output[0] if isinstance(args.output, list) else args.output
