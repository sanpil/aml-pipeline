import argparse
import os

print("In compare.py")
print("As a data scientist, this is where I use my compare code.")
parser = argparse.ArgumentParser("compare")
parser.add_argument("--compare_data1", type=str, help="compare_data1 data")
parser.add_argument("--compare_data2", type=str, help="compare_data2 data")
parser.add_argument("--output_compare", type=str, help="output_compare directory")

args = parser.parse_args()

print(f"Argument 1: {args.compare_data1}")
print(f"Argument 2: {args.compare_data2}")
print(f"Argument 3: {args.output_compare}")

if not (args.output_compare is None):
	os.makedirs(args.output_compare, exist_ok=True)
	print(f"{args.output_compare} created")
