#
# Beecrowd - Problem 1144
#

n = int(input())

for k in range(1, n + 1):
    k2 = k * k
    k3 = k * k * k
    print(f'{k} {k2} {k3}')
    print(f'{k} {k2 + 1} {k3 + 1}')
