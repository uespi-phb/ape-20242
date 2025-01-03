
def convert_to_int(string):
    try:
        result = int(string)
    except ValueError:
        raise ValueError(f'Invalid numeric string: "{string}"')

    return result


def main():
    candidates = [
        '7934',
        '-9334',
        'x190',
        '10+39',
        '120KG',
        '12345'
    ]

    print('CONVERTING NUMERIC STRING TO INT:\n')

    for cand in candidates:
        try:
            result = convert_to_int(cand)
            print(f'Converting "{cand}" to int: {result}')
        except ValueError:
            print(f'Error converting string "{cand}" to integer.')

    print(f'\n{len(candidates)} CONVERTIONS COMPLETED')


if __name__ == '__main__':
    main()
