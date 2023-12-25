"""
Solve
"""
import re
import argparse

# class MyClass(SuperClass):
#     """
#     Class docstring
#     """
#     def __init__(self, value):
#         self.value = value
#
#     def my_method(self, num):
#         """
#         Method docstring
#         """


parser = argparse.ArgumentParser(description='Solution to Day 6')
parser.add_argument('input_file', help='input file name')
parser.add_argument('-d', '--debug', help='print debug info', action='store_true')
args = parser.parse_args()

with open(args.input_file, 'r', -1, 'UTF-8') as file:
    lines = file.read().splitlines()

times = []
distances = []
for line in lines:
    if re.match(r'Time:', line):
        times = list(map(int, re.findall(r'\d+', line)))
    elif re.match(r'Distance:', line):
        distances = list(map(int, re.findall(r'\d+', line)))

races = []
for i, time in enumerate(times):
    races.append((time, distances[i]))

product = 1
for race in races:
    time, record_dist = race
    win_count = 0
    for hold_duration in range(1, time + 1):
        distance = hold_duration * (time - hold_duration)
        if distance > record_dist:
            win_count += 1
    product *= win_count

print(product)
