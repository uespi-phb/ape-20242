
def wrong_letters(guess_word, wright_word):
    count = 0
    for i in range(len(guess_word)):
        if guess_word[i] != wright_word[i]:
            count += 1
    return count


def guess_number(word):
    if len(word) == 3:
        if wrong_letters(word, 'one') <= 1:
            return 1
        else:
            return 2
    else:
        return 3


words = int(input())

while words > 0:
    words -= 1

    word = input().strip()
    number = guess_number(word)
    print(number)
