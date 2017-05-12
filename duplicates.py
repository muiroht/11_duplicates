
import os
import sys
import argparse
from collections import defaultdict


def get_files_dict(root_dir):
    result_dict = defaultdict(list)
    for root, dirs, files in os.walk(root_dir):
        for file_name in files:
            full_file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(full_file_path)
            result_dict[(file_name, file_size)].append(full_file_path)
    return result_dict


def get_duplicated_files_dict(files_dict):
    return {key: value for key, value in files_dict.items() if len(value) > 1}


def show_duplicated_files(path_to_checking_dir):
    files_dict = get_files_dict(path_to_checking_dir)
    duplicated_files_dict = get_duplicated_files_dict(files_dict)
    for _, list_duplicated_files in duplicated_files_dict.items():
        print('{stars}Same files groups{stars}'.format(stars='*'*50))
        print('\n'.join(list_duplicated_files))


def get_args():
    parser = argparse.ArgumentParser(description='Find and remove duplicates in asked directory.')
    parser.add_argument('path', type=str, help='path where to find duplicates for removing')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    path_to_checking_dir = args.path
    if not os.path.exists(path_to_checking_dir):
        print('Path: {}\ndoes not exists'.format(path_to_checking_dir))
        sys.exit(1)
show_duplicated_files(path_to_checking_dir)
