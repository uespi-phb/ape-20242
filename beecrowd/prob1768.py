import sys

for line in sys.stdin:
    n = int(line)

    for step in range(2):
        for stars in range(1, n + 1, 2):
            if (step == 1) and (stars == 5):
                break

            spaces = (n - stars) // 2
            print(' ' * spaces, '*' * stars, sep='')
    print()
