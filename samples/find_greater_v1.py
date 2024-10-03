# V1
# Escreva um programa que verifique qual o maior de
# dois números lidos pelo teclado
#

print('CALCULA QUAL O MAIOR DE DOIS NÚMEROS (V1)\n')
number1 = int(input('Digite o 1º número: '))
number2 = int(input('Digite o 2º número: '))

if number1 > number2:
    print(number1, 'é MAIOR que', number2)
else:
    if number2 > number1:
        print(number2, 'é MAIOR que', number1)
    else:
        print(number1, 'é IGUAL a', number2)
