print('INÍCIO DO PROGRAMA')

try:
    a = int(input('Informe o 1o valor: '))
    b = int(input('Informe o 2o valor: '))
    r = a / b
    print(f'{a} / {b} = {r}')
except ValueError:
    print('Os valores devem ser numéricos!')
except ZeroDivisionError:
    print('O 2o valor não pode ser 0!')
else:
    print('Código executado com sucesso!')
finally:
    print('Ocorreu algum error!')

print('FINAL DO PROGRAMA')


# Possible Errors
# ValueError
# ZeroDivisionError
