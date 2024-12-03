
text = input()
text_words = text.split()

for i in range(len(text_words)):
    word = text_words[i]
    if (len(word) >= 4) and (word[0] == word[2]) and (word[1] == word[3]):
        text_words[i] = word[2:]

correct_text = ''
for word in text_words:
    correct_text = correct_text + ' ' + word

print(correct_text.strip())
