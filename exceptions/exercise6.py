
def process_data(data):
    if isinstance(data, int):
        result = data // 2
    elif isinstance(data, float):
        result = data / 2
    elif isinstance(data, str):
        result = data.upper()
    elif isinstance(data, (list, tuple)):
        result = len(data)
    else:
        raise Exception('Invalid data type')

    return result


def main():
    data = (
        100,
        1.53,
        -210,
        -3.14,
        'Uespi Parnaiba',
        [1, 2, 3, 4],
        ('a', 'e', 'i', 'o', 'u'),
        {'name': 'Fulano', 'age': 22}
    )

    print('PROCESSING DATA:\n')

    for info in data:
        try:
            result = process_data(info)
            print(f'process_data({info}) -> {result}')
        except Exception as error:
            print(f'Unexpected error: {error} ({info}).')

    print(f'\n{len(data)} DATA PROCESSED')


if __name__ == '__main__':
    main()
