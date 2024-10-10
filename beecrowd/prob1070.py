#
# Beecrowd - Problem 1070
#
n = int(input())

if n % 2 == 0:
    n += 1

count = 0
while count < 6:
    count += 1
    print(n)
    n += 2    # n = n + 2
