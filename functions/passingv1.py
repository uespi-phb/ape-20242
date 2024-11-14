
import sys


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x // y


for line in sys.stdin:
    oper1, oper2, operator = line.split()

    oper1 = int(oper1)
    oper2 = int(oper2)

    if operator == '+':
        result = add(oper1, oper2)
    elif operator == '-':
        result = sub(oper1, oper2)
    elif operator == 'x':
        result = mul(oper1, oper2)
    else:
        result = div(oper1, oper2)

    print(f'{oper1} {operator} {oper2} = {result}')
