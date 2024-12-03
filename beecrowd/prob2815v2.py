
text = input()
text_words = text.split()

for index, word in enumerate(text_words):
    if word[0:2] == word[2:4]:
        text_words[index] = word[2:]

correct_text = ' '.join(text_words)
print(correct_text)
