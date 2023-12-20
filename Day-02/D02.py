import re

def is_possible(count):
    if count['red'] > 12 or count['green'] > 13 or count['blue'] > 14:
        return False
    return True

def count_rgb(str):
    rgb = dict(red=0, green=0, blue=0)
    color_counts = re.sub(';', ',', str).split(', ') # Assume only one space character for each comma.
    for color_count in color_counts:
        (count, color) = color_count.split()
        if int(count) > rgb[color]:
            rgb[color] = int(count)
    return rgb

file = 'Day-02/input.txt'
# file = 'Day-02/example-1.txt'

rgb_counts = []
sum = 0
power_sum = 0
with open(file) as f:
    lines = [s.rstrip() for s in f.readlines()]
    for line in lines:
        rgb_str = re.sub(r'.*\d+: ' , '', line)
        rgb = count_rgb(rgb_str)

        rgb_counts.append(rgb)

for num, rgb_count in enumerate(rgb_counts, 1):
    if is_possible(rgb_count):
        sum += num
    power_sum += rgb_count['red'] * rgb_count['green'] * rgb_count['blue']

print(sum)
print(power_sum)
