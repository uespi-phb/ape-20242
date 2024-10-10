#
# Beecrowd - Problem 1153
#
n = int(input())

factorial = 1

# range produz uma seq de int de 1 a N
for term in range(1, n + 1):
    factorial *= term

print(factorial)
