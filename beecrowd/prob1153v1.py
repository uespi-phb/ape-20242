#
# Beecrowd - Problem 1153
#
n = int(input())

factorial = 1
term = 1
while term <= factorial:
    factorial *= term
    term += 1

print(factorial)
