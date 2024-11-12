
purchases = {
    1: 0,
    2: 0,
    3: 0,
}

while True:
    fuel_type = int(input())
    if fuel_type == 4:
        break

    if (fuel_type >= 1) and (fuel_type <= 3):
        purchases[fuel_type] += 1


print('MUITO OBRIGADO')
print('Alcool:', purchases[1])
print('Gasolina:', purchases[2])
print('Diesel:', purchases[3])
