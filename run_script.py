# -*- coding: utf-8 -*-

import argparse
from csv_parser import ParsersRunner

parser = argparse.ArgumentParser(description='CSV filter')
parser.add_argument('-p', '--path', type=str, metavar='', help='directory path')
parser.add_argument('-f', '--process', type=int, metavar='', help='numbers of process')
args = parser.parse_args()

if __name__ == '__main__':
    try:
        ParsersRunner(src=args.path, numbers_process=args.process).run()
    except FileNotFoundError as exc:
        print(f"Error: {exc} type {(type(exc))}")
