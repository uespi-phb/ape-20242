
def factorial(n):
    f = 1
    for t in range(1, n + 1):
        f = f * t
    return f


def max_factorial(fat_limit):
    term = 0
    fat_term = 1
    while True:
        term += 1
        fat_last = fat_term
        fat_term = factorial(term)
        if fat_term >= fat_limit:
            if fat_term == fat_limit:
                return fat_term
            else:
                return fat_last
    return 1


number = int(input())

sum_terms = 0
qty_terms = 0

fat_term = number
while True:
    fat_max = max_factorial(fat_term)

    sum_terms += fat_max
    qty_terms += 1

    if sum_terms < number:
        fat_term = number - sum_terms
    else:
        break

print(qty_terms)
