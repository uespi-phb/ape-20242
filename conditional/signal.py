#
# Escreva um programa em Python que verifique se um
# dado inteiro é positivo, negativo ou zero.
#
print('Verifica o sinal de um número inteiro\n')

# Obter o número
number = int(input('Informe um número:\n'))

if number > 0:
    print(f'O número {number} é POSITIVO.')
elif number < 0:
    print(f'O número {number} é NEGATIVO')
else:
    print(f'O número {number} é ZERO')
