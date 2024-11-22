
test_cases = int(input())
while test_cases > 0:
    test_cases -= 1

    a, b = input().split()

    if a.endswith(b):
        print('encaixa')
    else:
        print('nao encaixa')
