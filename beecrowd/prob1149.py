
def calc_sum(a, n):
    sum = 0
    for i in range(n):
        sum += a + i
    return sum


data = input().split()

a = int(data[0])
for n in data[1:]:
    n = int(n)
    if n > 0:
        print(calc_sum(a, n))
        break
