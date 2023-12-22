import re

file = 'Day-05/input.txt'
file = 'Day-05/example-1.txt'
file = 'Day-05/example-0.txt'

class MapList(list):
    def __init__(self):
        print("init")

    def input(self, n0):
        v = n0
        # print(v)
        for map in self:
            v = map.get(v, v)   # Return the same value unless the key exists.
            # print(v)
        return v

ml = MapList()

f = open(file, "r")
lines = f.read().splitlines()

is_map = False
m = {}
for line in lines:
    if is_map and len(line) == 0:
        is_map = False
        print('before:\n', ml)
        print('m:\n', m)
        ml.append(m)
        print('after:\n', ml)
        # print("\n")

    if is_map:
        dst_st, src_st, length = map(int, re.findall(r'\d+', line))
        for i in range(length):
            m[src_st + i] = dst_st + i

    if re.search(r'map:$', line):
        is_map = True
        m.clear()
# print(ml)
# print(ml.input(79))