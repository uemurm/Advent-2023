"""
Module docstring
"""
import re
import argparse


# class MyClass(SuperClass):
#     """
#     Class docstring
#     """
#
#     def __init__(self, value):
#         self.value = value
#
#     def my_method(self, num):
#         """
#         Method docstring
#         """


parser = argparse.ArgumentParser(description='Calculate total winnings of poker hands')
parser.add_argument('input_file', help='input file name')
parser.add_argument('-d', '--debug', help='print debug info', action='store_true')
args = parser.parse_args()

with open(args.input_file, 'r', -1, 'UTF-8') as file:
    lines = file.read().splitlines()

for line in lines:
    hand, bid = re.match(r'(\w+) (\d+)', line)
    print(hand, int(bid))
