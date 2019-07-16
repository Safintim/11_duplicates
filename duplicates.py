import argparse
import os


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    if not namespace.path:
        exit('Укажите правильный путь каталога')


def create_parser():
    parser = argparse.ArgumentParser(prefix_chars='-+/')
    parser.add_argument('path',
                        nargs='?',
                        default=False,
                        type=is_directory,
                        help='Path to directory')
    return parser


def is_directory(path):
    if os.path.isdir(path):
        return path


if __name__ == '__main__':
    main()
