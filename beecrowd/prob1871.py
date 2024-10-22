#
# Beecrowd - Problem 1871
#
while True:
    numbers = input().split()
    n1 = int(numbers[0])
    n2 = int(numbers[1])

    if (n1 == 0) and (n2 == 0):
        break

    sum = str(n1 + n2).replace('0', '')
    print(sum)
