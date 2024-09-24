#
# Escreva um programa em Python que verifique se um
# dado inteiro é positivo, negativo ou zero.
#
print('Verifica o sinal de um número inteiro\n')

# Obter o número
number = int(input('Informe um número: '))

if number > 0:
    result = 'POSITIVO'
elif number < 0:
    result = 'NEGATIVO'
else:
    result = 'ZERO'

print(f'O número {number} é {result}.')
