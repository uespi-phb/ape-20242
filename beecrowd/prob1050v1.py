# 1050 - Felipe Martins

ddd = [61, 71, 11, 21, 32, 19, 27, 31]
lista = ['Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro',
         'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte']
v = 0
y = int(input())

for x in ddd:
    if y == x:
        print(lista[v])
    else:
        v += 1
if v > 7:
    print('DDD nao cadastrado')
