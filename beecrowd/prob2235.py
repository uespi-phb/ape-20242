
years = list(map(int, input().split()))
years.sort()

can_travel = False

if (years[0] == years[1]) or (years[1] == years[2]):
    can_travel = True
else:
    can_travel = (years[0] + years[1]) == years[2]

print('S' if can_travel else 'N')
