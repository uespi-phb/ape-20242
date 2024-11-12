
def read_input():
    rat1_num, _, rat1_den, operator, rat2_num, _, rat2_den = input().split()
    return {
        'rational1': (int(rat1_num), int(rat1_den)),
        'rational2': (int(rat2_num), int(rat2_den)),
        'operator': operator,
    }


def rational_operation(operation_data):
    num = 0
    den = 1

    rat1 = operation_data['rational1']
    rat2 = operation_data['rational2']
    operator = operation_data['operator']

    if operator == '+':
        rat_num = (rat1[num] * rat2[den] + rat2[num] * rat1[den])
        rat_den = rat1[den] * rat2[den]
    elif operator == '-':
        rat_num = (rat1[num] * rat2[den] - rat2[num] * rat1[den])
        rat_den = rat1[den] * rat2[den]
    elif operator == '*':
        rat_num = rat1[num] * rat2[num]
        rat_den = rat1[den] * rat2[den]
    elif operator == '/':
        rat_num = rat1[num] * rat2[den]
        rat_den = rat1[den] * rat2[num]

    return (rat_num, rat_den)


def rational_simplify(rational):
    rat_num = rational[0]
    rat_den = rational[1]

    div = 2
    div_max = min(abs(rat_num), abs(rat_den))
    while div <= div_max:
        if (rat_num % div == 0) and (rat_den % div == 0):
            rat_num = rat_num // div
            rat_den = rat_den // div
        else:
            div = div + 1

    return (rat_num, rat_den)


def print_result(rational_result, rational_simplified):
    num = 0
    den = 1

    print(rational_result[num], '/', rational_result[den],
          ' = ',
          rational_simplified[num], '/', rational_simplified[den],
          sep=''
          )


def beecrowd_1022():
    rational_expressions = int(input())

    while rational_expressions > 0:
        rational_expressions -= 1

        input_data = read_input()

        result_data = rational_operation(input_data)
        simplified_data = rational_simplify(result_data)

        print_result(result_data, simplified_data)


if __name__ == '__main__':
    beecrowd_1022()

'''
        rat1 = data['rational1']
        rat2 = data['rational2']
        operator = data['operator']

        if oper == '+':
            nr = (n1*d2 + n2*d1)
            dr = d1*d2
        elif oper == '-':
            nr = (n1*d2 - n2*d1)
            dr = d1*d2
        elif oper == '*':
            nr = n1*n2
            dr = d1*d2
        elif oper == '/':
            nr = n1*d2
            dr = d1*n2

        ns = nr
        ds = dr

        div = 2
        div_max = min(abs(nr), abs(dr))
        while div <= div_max:
            if (ns % div == 0) and (ds % div == 0):
                ns = ns // div
                ds = ds // div
            else:
                div = div + 1

        print(nr, '/', dr, ' = ', ns, '/', ds, sep='')

'''
