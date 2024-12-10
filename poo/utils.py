
def float_to_currency(value):
    man, dec = f'{value:0.2f}'.split('.')
    man = int(man)

    thousands = []
    while True:
        thousands.insert(0, str(man % 1000))
        man = man // 1000
        if man == 0:
            break

    man = '.'.join(thousands)
    return f'R${man},{dec}'
