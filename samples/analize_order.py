#
# Escreva um programa que analize a ordenação
# entre dois números inteiros
#

number1 = int(input('Informe o 1º número: '))
number2 = int(input('Informe o 2º número: '))

if number1 > number2:
    print(number1, 'é MAIOR que', number2)
elif number1 < number2:
    print(number1, 'é MENOR que', number2)
else:
    print(number1, 'é IGUAL a', number2)
