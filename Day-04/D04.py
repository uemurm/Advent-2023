import re

file = 'Day-04/input.txt'
# file = 'Day-04/example-1.txt'

f = open(file, "r")
lines = f.read().splitlines()

sum = 0
for line in lines:
    nums = re.sub(r'Card\s+\d+: ', '', line)
    win_nums = set(re.findall(r'\d+', re.sub(r' \|.*', '', nums)))
    my_nums  = set(re.findall(r'\d+', re.sub(r'.*\| ', '', nums)))
    win_count = len(win_nums & my_nums)
    sum += 0 if win_count == 0 else 2 ** (win_count - 1)
print(sum)