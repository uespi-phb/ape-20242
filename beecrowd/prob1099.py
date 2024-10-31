
def sum_odds(begin, end):
    sum = 0
    for number in range(min(begin, end) + 1, max(begin, end)):
        if number % 2 == 1:
            sum += number
    return sum


tests_count = int(input())
while tests_count > 0:
    tests_count -= 1

    x, y = input().split()

    odd_sum = sum_odds(int(x), int(y))

    print(odd_sum)
