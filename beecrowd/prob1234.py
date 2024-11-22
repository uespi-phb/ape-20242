
import sys

def to_dancing_text2(text):
    upper = True
    dancing_text = ''
    for char in text:
        if char == ' ':
            dancing_text += char
            continue
        # if upper:
        #     char = char.upper()
        # else:
        #     char = char.lower()
        dancing_text += char.upper() if upper else char.lower()
        upper = not upper
    return dancing_text


def to_dancing_text(text):
    upper = True
    dancing_text = ''
    for char in text:
        if not char.isspace():
            char = char.upper() if upper else char.lower()
            upper = not upper
        dancing_text += char

    return dancing_text


for text in sys.stdin:
    text = text.strip('\n')
    print(to_dancing_text(text))