
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

    if operator == '+':
        operation = add
    elif operator == '-':
        operation = sub
    elif operator == 'x':
        operation = mul
    else:
        operation = div

    result = operation(int(oper1), int(oper2))

    print(f'{oper1} {operator} {oper2} = {result}')
