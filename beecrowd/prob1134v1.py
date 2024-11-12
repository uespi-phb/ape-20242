
gasoline = 0
alcohol = 0
diesel = 0

while True:
    fuel_type = int(input())
    if fuel_type == 4:
        break

    if fuel_type == 1:
        alcohol += 1
    elif fuel_type == 2:
        gasoline += 1
    elif fuel_type == 3:
        diesel += 1

print('MUITO OBRIGADO')
print('Alcool:', alcohol)
print('Gasolina:', gasoline)
print('Diesel:', diesel)
