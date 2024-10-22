#
# Escreva um programa que gere e imprima na tela
# uma matriz identidade de ordem N, onde N é
# fornecido pelo teclado.
#
n = int(input('Informe a ordem da matriz: '))

m = []
for i in range(n):
    m.append([0] * n)
    m[i][i] = 1

# m = [[1,0,0],[0,1,0],[0,0,1]]
#
# 1 0 0
# 0 1 0
# 0 0 1

for row in m:
    for elem in row:
        print(elem, end=' ')
    print()
