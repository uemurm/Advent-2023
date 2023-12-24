"""
Day 05: Transform seed numbers to their locations.
"""
import re
import argparse

FILE_NAME = 'Day-05/input.txt'
FILE_NAME = 'Day-05/input-0.txt'
# FILE_NAME = 'Day-05/example-1.txt'
# FILE_NAME = 'Day-05/example-0.txt'

class MyMap:
    """
    kk
    """
    def __init__(self, map_lines):
        self.map_lines = map_lines

    def get(self, key):
        """
        docstring
        """
        for map_line in self.map_lines:
            dst, src, size = map_line
            if src <= key <= src + size:
                return dst + (key - src)
        return key

class MapList(list):
    """
    A list of maps to map seed numbers to their locations.
    """

    def input(self, num):
        """
        Input a seed number to find out its location.
        """
        for a_map in self:
            num = a_map.get(num)   # Return the same value unless the key exists.
        return num

parser = argparse.ArgumentParser(description='Transform seed numbers to their locations')
parser.add_argument('input_file', help='input file name')
parser.add_argument('-d', '--debug', help='print debug info', action='store_true')
args = parser.parse_args()

maps = MapList()

with open(args.input_file, 'r', -1, 'UTF-8') as file:
    lines = file.read().splitlines()

IS_MAP = False
for row, line in enumerate(lines, 1):
    if re.match(r'^seeds: ', line):
        seeds = list(map(int, re.findall(r'\d+', line)))
    elif re.search(r'map:$', line):
        IS_MAP = True
        my_map = {}
        sub_maps = []
    elif IS_MAP and len(line) == 0: # Detect end of each map.
        IS_MAP = False
        my_map = MyMap(sub_maps)
        maps.append(my_map)
    elif IS_MAP:
        dst_st, src_st, length = map(int, re.findall(r'\d+', line))
        sub_maps.append((dst_st, src_st, length))

LOCATIONS = list(map(maps.input, seeds))
if args.debug:
    print(LOCATIONS)
print(min(LOCATIONS))
