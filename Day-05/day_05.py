"""
Day 05: Transform seed numbers to their locations.
"""
import re

FILE_NAME = 'Day-05/input.txt'
FILE_NAME = 'Day-05/example-1.txt'
FILE_NAME = 'Day-05/example-0.txt'

class MapList(list):
    """
    A list of maps to map seed numbers to their locations.
    """

    def __init__(self):
        print("init")

    def input(self, num):
        """
        Input a seed number to find out its location.
        """
        v = num
        for my_map in self:
            v = my_map.get(v, v)   # Return the same value unless the key exists.
        return v

ml = MapList()

f = open(FILE_NAME, 'r', -1, 'UTF-8')
lines = f.read().splitlines()

IS_MAP = False
m = {}
for line in lines:
    if IS_MAP and len(line) == 0:
        IS_MAP = False
        print('before:\n', ml)
        print('m:\n', m)
        ml.append(m)
        print('after:\n', ml)
        # print("\n")

    if IS_MAP:
        dst_st, src_st, length = map(int, re.findall(r'\d+', line))
        for i in range(length):
            m[src_st + i] = dst_st + i

    if re.search(r'map:$', line):
        IS_MAP = True
        m.clear()
# print(ml)
# print(ml.input(79))
