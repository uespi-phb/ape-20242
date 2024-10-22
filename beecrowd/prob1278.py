#
# Beecrowd - Problem 1278
#
use_case = 0
while True:
    n = int(input())
    if n == 0:
        break

    use_case += 1

    max_len = 0
    lines = []
    while n > 0:
        n = n - 1
        words = input().split()
        line = ' '.join(words)
        lines.append(line)

        if len(line) > max_len:
            max_len = len(line)

    if use_case > 1:
        print()

    for line in lines:
        print(' '*(max_len - len(line)), line, sep='')
