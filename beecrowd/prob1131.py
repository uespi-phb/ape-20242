
matches = 0
win_gremio = 0
win_inter = 0

while True:
    line = input()
    values = line.split(' ')

    goals_inter = int(values[0])
    goals_gremio = int(values[1])

    matches += 1

    if goals_gremio > goals_inter:
        win_gremio += 1
    elif goals_inter > goals_gremio:
        win_inter += 1

    print('Novo grenal (1-sim 2-nao)')
    stop = input()

    if stop == '2':
        break

print(f'{matches} grenais')
print(f'Inter:{win_inter}')
print(f'Gremio:{win_gremio}')
print(f'Empates:{matches - win_inter - win_gremio}')

if win_inter > win_gremio:
    print('Inter venceu mais')
elif win_gremio > win_inter:
    print('Gremio venceu mais')
