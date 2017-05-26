#!/usr/local/biotools/python/2.7.3/bin/python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('square',
                    help="display a square of a given number",
                    type=int)

parser.add_argument('--verbose',
                    help="increase output verbosity",
                    action="store_true")

args = parser.parse_args()

print(args.square**2)

if args.verbose:
    print("verbosity turned on")