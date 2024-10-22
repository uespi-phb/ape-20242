
import sys

for line in sys.stdin:
    size = int(line)

    for part in range(2):
        stars = 1
        shift = size // 2
        while shift >= 0:
            print(' '*shift, '*'*stars, sep='')
            stars += 2
            shift -= 1

            if part == 1 and stars > 3:
                break
    print()
