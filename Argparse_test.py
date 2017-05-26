#!/usr/local/biotools/python/2.7.3/bin/python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('square',
                    help="display a square of a given number",
                    type=int)

parser.add_argument('-v', '--verbose',
                    help="increase output verbosity",
                    action="store_true")

parser.add_argument('-e', '--echo',
                    required=False,
                    help="echoes your message")

args = parser.parse_args()

print(args.square**2)
if args.echo:
    print(args.echo)

if args.verbose:
    print(str(args.square) + ' squared is ' + str((args.square**2)))
