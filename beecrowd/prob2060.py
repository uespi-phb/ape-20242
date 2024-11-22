
input()

numbers = map(int, input().split())

divs_count = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
}

for number in numbers:
    for div in divs_count.keys():
        if number % div == 0:
            divs_count[div] += 1

for div in divs_count.keys():
    print(divs_count[div], 'Multiplos(s) de', div)
