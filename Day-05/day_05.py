"""
Day 05: Transform seed numbers to their locations.
"""
import re
import argparse

FILE_NAME = 'Day-05/input.txt'
# FILE_NAME = 'Day-05/example-1.txt'
# FILE_NAME = 'Day-05/example-0.txt'

class MapList(list):
    """
    A list of maps to map seed numbers to their locations.
    """

    def input(self, num):
        """
        Input a seed number to find out its location.
        """
        v = num
        for my_map in self:
            v = my_map.get(v, v)   # Return the same value unless the key exists.
        return v

parser = argparse.ArgumentParser(description='Transform seed numbers to their locations.')
parser.add_argument('-d', '--debug', help='Print debug info.', action='store_true')
args = parser.parse_args()

maps = MapList()

f = open(FILE_NAME, 'r', -1, 'UTF-8')
lines = f.read().splitlines()

IS_MAP = False
for row, line in enumerate(lines, 1):
    if re.match(r'^seeds: ', line):
        seeds = list(map(int, re.findall(r'\d+', line)))
    elif IS_MAP and len(line) == 0:
        IS_MAP = False
        if args.debug:
            print('m:\n', m)
        maps.append(m)

    elif IS_MAP:
        dst_st, src_st, length = map(int, re.findall(r'\d+', line))
        for i in range(length):
            m[src_st + i] = dst_st + i

    elif re.search(r'map:$', line):
        IS_MAP = True
        m = {}

    if args.debug:
        print(row, 'maps:\n', maps)

LOCATIONS = list(map(maps.input, seeds))
print(min(LOCATIONS))
