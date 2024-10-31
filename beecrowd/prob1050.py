
ddd_table = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte',
}

ddd = int(input())
print(ddd_table.get(ddd, 'DDD nao cadastrado'))

# if ddd in ddd_table:
#     print(ddd_table[ddd])
# else:
#     print('DDD nao cadastrado')
