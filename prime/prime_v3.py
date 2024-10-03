#
# Verificar se um inteiro qualquer "p" é primo
#
# Abordagem 3: Verificar se existe algum dividor de p
#              entre 2 e |p-1|. Se existir, p não é primo.
#
print('** VERIFICA SE UM INTEIRO POSITIVO É PRIMO **\n')

# Número a ser verificar
number = int(input('Informe um inteiro: '))
# Obtém valor absoluto de number
abs_number = abs(number)
# Indica se 'number' é primo. Inicialmente assume que sim.
prime = (abs_number != 0) and (abs_number != 1)
# prime = True if number != 1 else False

# Cada um dos candidatos a divisores de 'number' (2 até number-1)
d = 2
while d < abs_number:
    if abs_number % d == 0:
        prime = False
        break
    d = d + 1

if prime:
    print(number, 'É PRIMO')
else:
    print(number, 'NÃO É PRIMO')
