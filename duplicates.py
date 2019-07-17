import os
import argparse
from itertools import groupby


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    if not namespace.path:
        exit('Укажите правильный путь каталога')

    print('\n'.join(get_duplicate_files(namespace.path)))


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                        nargs='?',
                        default=False,
                        type=is_directory,
                        help='Path to directory')
    return parser


def is_directory(path):
    if os.path.isdir(path):
        return path


def get_duplicate_files(path):
    duplicates = []
    for filename, filepaths in find_files_with_same_name(path).items():
        for paths in get_duplicate(filepaths):
            duplicates.append('\n')
            duplicates.extend(paths)
    return duplicates


def find_files_with_same_name(path):
    files = {}
    for current_dir, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(current_dir, filename)
            if files.get(filename):
                files[filename].append(filepath)
            else:
                files[filename] = [filepath]
    return files


def get_duplicate(filepaths):
    filepaths_sizes = [(path, os.path.getsize(path)) for path in filepaths]
    filepaths_sizes.sort(key=lambda path: path[1])
    for key, filepaths in groupby(filepaths_sizes, lambda path: path[1]):
        paths = list(filepath[0] for filepath in filepaths)
        if len(paths) > 1:
            yield paths


if __name__ == '__main__':
    main()
