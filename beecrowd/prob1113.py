#
# Beecrowd - Problem 1113
#

while True:
    line = input()
    numbers = line.split(' ')

    x = int(numbers[0])
    y = int(numbers[1])

    if x < y:
        print('Crescente')
    elif x > y:
        print('Decrescente')
    else:
        break
