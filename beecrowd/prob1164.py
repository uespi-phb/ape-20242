
def is_perfect(n):
    sum_divs = 0
    for div in range(1, (n // 2) + 1):
        if n % div == 0:
            sum_divs += div
    return sum_divs == n


numbers_count = int(input())
while numbers_count > 0:
    numbers_count -= 1

    number = int(input())
    if is_perfect(number):
        print(number,'eh perfeito')
    else:
        print(number,'nao eh perfeito')
