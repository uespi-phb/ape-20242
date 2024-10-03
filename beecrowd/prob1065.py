n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

even = 0
if n1 % 2 == 0:
    even += 1       # even = even + 1
if n2 % 2 == 0:
    even += 1
if n3 % 2 == 0:
    even += 1
if n4 % 2 == 0:
    even += 1
if n5 % 2 == 0:
    even += 1

print(f'{even} valores pares')
