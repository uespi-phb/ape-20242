#
# Leia uma sequência de inteiros terminada por 0 (não faz parte da lista)
# e depois exiba esta mesma sequência na ordem inversa em que foram lidas
#
# Entrada:
#  10 5 -1 9 -6 22 -13 0
# Saída:
#  -13 22 -6 9 -1 5 10

numbers = []
while True:
    data = int(input())
    if data == 0:
        break
    numbers.append(data)

# print(numbers[::-1])

for elem in numbers[::-1]:
    print(elem, end=' ')
print()
