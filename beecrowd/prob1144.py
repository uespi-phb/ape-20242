
n = int(input())

i = 0
while i < n:
    i += 1

    n1 = i**2   # i * i
    n2 = i**3   # i * i * i
    print(f'{i} {n1} {n2}')
    print(f'{i} {n1 + 1} {n2 + 1}')
