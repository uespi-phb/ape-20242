
while True:
    start, end = map(int, input().split())
    if start == 0 and end == 0:
        break

    digits_count = [0] * 10
    for number in range(start, end + 1):
        while number > 0:
            digit = number % 10
            digits_count[digit] += 1
            number = number // 10
    
    # print(' '.join(map(str, digits_count)))
    for digit in range(len(digits_count)):
        print(digits_count[digit], end='')
        if digit < 9:
            print(' ', end='')
    print()
