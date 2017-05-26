#!/usr/local/biotools/python/2.7.3/bin/python
#!//anaconda/bin/python

import argparse
import sys

parser = argparse.ArgumentParser(description='Basic calculator function. Requires two integers')

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

parser.add_argument('--multiply',
                    required=False,
                    action='store_true',
                    help="Multiply the first and second integers")

parser.add_argument('--divide',
                    required=False,
                    action='store_true',
                    help="Divide the first integer by the second integer")

parser.add_argument('-v', '--verbose',
                    required=False,
                    default=False,
                    action="store_true",
                    help="Displays function and result")

args = parser.parse_args()

if args.add:
    addint = args.firstint + args.secondint
    print(addint)
    if args.verbose:
        print(str(args.firstint) + ' + ' + str(args.secondint) + ' = ' + str(addint))

if args.subtract:
    subtractint = args.firstint - args.secondint
    print(subtractint)
    if args.verbose:
        print(str(args.firstint) + ' - ' + str(args.secondint) + ' = ' + str(subtractint))

if args.multiply:
    multiplyint = args.firstint * args.secondint
    print(multiplyint)
    if args.verbose:
        print(str(args.firstint) + ' x ' + str(args.secondint) + ' = ' + str(multiplyint))

if args.divide:
    divideint = float(args.firstint) / float(args.secondint)
    print(divideint)
    if args.verbose:
        print(str(args.firstint) + ' / ' + str(args.secondint) + ' = ' + str(divideint))
