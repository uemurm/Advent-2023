import re

# "eightwo" の様にふたつの数が繋がっている場合は、左を優先的にアラビア数字に変換する必要がある。
#
# one eight
# two one
# three eight
# five eight
# seven nine
# eight two
# nine eight

def replace_with_digits(str):
    # Python ではハッシュは辞書オブジェクトと呼ぶらしい。
    digits = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for key in digits:
        str = re.sub(key, digits[key], str)
    return str

file = 'input.txt'
file = 'example-2.txt'
replace_numbers = True
sum = 0
with open(file) as f:
    lines = [s.rstrip() for s in f.readlines()]
    for line in lines:
        if replace_numbers:
            line = replace_with_digits(line)

        print(line)
        first = re.search(r'\d', line).group()
        last_plus = re.search(r'(\d)\D*$', line).group()
        last = re.match(r'\d', last_plus).group()
        num = int(first + last)
        sum += num
print(sum)
