
import sys


for line in sys.stdin:
    oper1, oper2, operator = line.split()

    if operator == '+':
        operation = lambda x,y: x + y 
    elif operator == '-':
        operation = lambda x,y: x - y
    elif operator == 'x':
        operation = lambda x,y: x * y
    else:
        operation = lambda x,y: x // y

    result = operation(int(oper1), int(oper2))

    print(f'{oper1} {operator} {oper2} = {result}')
