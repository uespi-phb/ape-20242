# 1050

ddd_data = [
    (61, 'Brasilia'),
    (71, 'Salvador'),
    (11, 'Sao Paulo'),
    (21, 'Rio de Janeiro'),
    (32, 'Juiz de Fora'),
    (19, 'Campinas'),
    (27, 'Vitoria'),
    (31, 'Belo Horizonte'),
]

ddd_code = int(input())

ddd_city = None
for ddd in ddd_data:
    if ddd[0] == ddd_code:
        ddd_city = ddd[1]
        break

if ddd_city:
    print(ddd_city)
else:
    print('DDD nao cadastrado')
