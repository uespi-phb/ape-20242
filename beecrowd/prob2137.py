#
# Beecrowd - Problem 2137
#
import sys

for line in sys.stdin:
    code_count = int(line)

    numbers = []
    while code_count > 0:
        line = sys.stdin.readline().strip()
        numbers.append(line)
        code_count -= 1

    numbers.sort()

    for number in numbers:
        print(number)
