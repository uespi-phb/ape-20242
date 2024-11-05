
def greeting(name, greet='Oi', sufix='!'):
    return f'{greet}, {name}{sufix}'


def sum(*values):
    values_sum = 0
    for value in values:
        values_sum += value
    return values_sum


def print_sum(prompt, *numbers):
    print(prompt, sum(*numbers))


print_sum('soma:', 10, 20)
