
while True:

    size = int(input())
    if size == 0:
        break

    for i in range(size):
        for j in range(size):
            e = abs(i - j) + 1
            if j > 0:
                print(f'{e:>4}', end='')
            else:
                print(f'{e:>3}', end='')
        print()
    print()
