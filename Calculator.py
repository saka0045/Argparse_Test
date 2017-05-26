#!/usr/local/biotools/python/2.7.3/bin/python

import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('firstint',
                    type=int,
                    help="The first integer")

parser.add_argument('secondint',
                    type=int,
                    help="The second integer")

parser.add_argument('--add',
                    required=False,
                    action='store_true',
                    help="Adds the first and second integer")

parser.add_argument('--subtract',
                    required=False,
                    action='store_true',
                    help="Subtracts the second integer from the first integer")

args = parser.parse_args()

if args.add:
    addint = args.firstint + args.secondint
    print(addint)
    sys.exit(1)

if args.subtract:
    subtractint = args.firstint - args.secondint
    print(subtractint)
    sys.exit(1)

print('What do you want to do with these numbers??')
