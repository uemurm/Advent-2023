import re

file = 'Day-03/input.txt'
# file = 'Day-03/example-1.txt'

def is_part_ID(params):
    row, (begin, end) = params

    for symbol in symbols:
        if row == 0:
            print(begin, end, symbol)
        if row - 1 <= symbol[0] and symbol[0] <= row + 1:
            if begin - 1 <= symbol[1] and symbol[1] <= end + 1:
                return True
    return False

sum = 0
numbers = {}
symbols = []
with open(file) as f:
    lines = [s.rstrip() for s in f.readlines()]
    for row, line in enumerate(lines):
        nums = re.findall(r'\d+', line)
        for n in nums:
            column = re.search(n, line).span()
            numbers[n] = row, (column[0], column[1] - 1)
            # print(part_IDs[n])

        # syms = re.findall(r'[*#+$]', line)
        line = re.sub(r'\.', 'A', line)
        syms = re.findall(r'\W', line)
        # print(syms)
        for sym in syms:
            regex = '\\' + sym
            column = re.search(regex, line).span()[0]
            symbols.append((row, column))

for number in numbers:
    # print(number)
    if is_part_ID(numbers[number]):
        sum += int(number)
        # print(number)


print(sum)