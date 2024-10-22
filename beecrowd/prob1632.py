#
# Beecrowd - Problem 1632
#
n = int(input())
while n > 0:
    n -= 1

    password = input()

    combs = 1
    for char in password:
        if char in 'aAeEiIoOsS':
            f = 3
        else:
            f = 2
        combs = combs * f

    print(combs)
