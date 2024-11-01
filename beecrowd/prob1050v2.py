# 1050

ddd_codes = [61, 71, 11, 21, 32, 19, 27, 31]
ddd_cities = ['Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro',
              'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte']
ddd_code = int(input())

index = 0
for ddd in ddd_codes:
    if ddd == ddd_code:
        print(ddd_cities[index])
        break
    else:
        index += 1

if index > len(ddd_codes):
    print('DDD nao cadastrado')
