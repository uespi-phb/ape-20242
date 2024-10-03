#
# Verificar se um inteiro positivo "p" é primo
#
# Abordagem 1: Contar quantos divisores p possui.
#              Se tiver 2 dividores (1 e p), então p é primo.
#
print('** VERIFICA SE UM INTEIRO POSITIVO É PRIMO **\n')

# Número a ser verificar
number = int(input('Informe um inteiro positivo: '))
# Contador de divisores de 'number'
divs = 0

# Cada um dos candidatos a divisores de 'number' (1 até number)
d = 1
while d <= number:
    if number % d == 0:
        divs = divs + 1
    d = d + 1

if divs == 2:
    print(number, 'É PRIMO')
else:
    print(number, 'NÃO É PRIMO')
