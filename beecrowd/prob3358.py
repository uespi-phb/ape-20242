#
# Beecrowd - Problem 3358
#
import sys

vowels = 'aeiou'

for line in sys.stdin:
    words_count = int(line)

    for _ in range(words_count):
        word = sys.stdin.readline().strip()

        easy_word = True
        consonants = 0
        for char in word:
            if char.lower() in vowels:
                consonants = 0
            else:
                consonants += 1
                if consonants == 3:
                    easy_word = False
                    break

        if easy_word:
            print(word, 'eh facil')
        else:
            print(word, 'nao eh facil')
