import argparse
import math
parser = argparse.ArgumentParser()
#parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="display a square of a given number", type=float)
args = parser.parse_args()
parser.print_help()
#print(args.echo)
print(pow(args.square, 2))
