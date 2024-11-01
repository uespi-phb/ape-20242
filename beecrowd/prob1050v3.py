# 1050

ddd_codes = [61, 71, 11, 21, 32, 19, 27, 31]
ddd_cities = ['Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro',
              'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte']
ddd_code = int(input())

ddd_index = None
for index in range(len(ddd_codes)):
    if ddd_codes[index] == ddd_code:
        ddd_index = index
        break

if not (ddd_index is None):
    print(ddd_cities[ddd_index])
else:
    print('DDD nao cadastrado')
