# Crie uma função chamada divide que receba dois números como parâmetros. Caso o divisor
# seja igual a zero, lance uma exceção ZeroDivisionError com uma mensagem personalizada.
# Implemente também o tratamento da exceção e exiba a mensagem ao usuário.

def divide(dividend, divisor):
    return dividend / divisor


def main():
    print('CÁLCULO DA DIVISÃO:\n')

    try:
        a = int(input('Dividendo: '))
        b = int(input('Divisor  : '))

        r = divide(a, b)

        print(f'{a} : {b} = {r}')
    except ValueError:
        print('Os valores do dividendo e divisor devem ser numéricos.')
    except ZeroDivisionError:
        print('O dividendo não pode ser zero.')


if __name__ == '__main__':
    main()

# UnboundLocalError
# NameError
# ZeroDivisionError
