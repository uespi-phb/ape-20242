#
# Verificar se um inteiro positivo "p" é primo
#
# Abordagem 2: Verificar se existe algum dividor de p
#              entre 2 e p-1. Se existir, p não é primo.
#
print('** VERIFICA SE UM INTEIRO POSITIVO É PRIMO **\n')

# Número a ser verificar
number = int(input('Informe um inteiro positivo: '))
# Indica se 'number' é primo. Inicialmente assume que sim.
prime = number != 1
# prime = True if number != 1 else False

# Cada um dos candidatos a divisores de 'number' (2 até number-1)
d = 2
while d < number:
    if number % d == 0:
        prime = False
        break
    d = d + 1

if prime:
    print(number, 'É PRIMO')
else:
    print(number, 'NÃO É PRIMO')
