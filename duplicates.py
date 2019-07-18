import os
import argparse
from collections import defaultdict


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    duplicates = get_duplicate_files(namespace.path)
    print_duplicates(duplicates)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',
                        type=is_directory,
                        help='Path to directory')
    return parser


def is_directory(path):
    if os.path.isdir(path):
        return path
    raise argparse.ArgumentTypeError('directory not found')


def get_duplicate_files(path):
    duplicates = []
    for filename, filepaths in find_files_with_same_name(path).items():
        if len(filepaths) > 1:
            duplicates.append(filepaths)
    return duplicates


def find_files_with_same_name(path):
    files = defaultdict(list)
    for current_dir, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(current_dir, filename)
            filename_filesize = (filename, os.path.getsize(filepath))
            files[filename_filesize].append(filepath)
    return files


def print_duplicates(duplicates):
    for filepaths in duplicates:
        print('\n')
        print('\n'.join(filepath for filepath in filepaths))


if __name__ == '__main__':
    main()
