# Generate the first numbers of Fibonacci Series
#
# Ex: 1 1 2 3 5 8 13 21 ...

n1 = 1
n2 = 0
while n2 < 20:
    print(n1 + n2)
    n1, n2 = n2, n1 + n2
