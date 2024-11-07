
import sys

def is_valid_score(score):
    return (score >= 0) and (score <= 10)

valid_scores = []
for data in sys.stdin:
    data = float(data)
    if is_valid_score(data):
        valid_scores.append(data)
        if len(valid_scores) == 2:
            average = (valid_scores[0] + valid_scores[1]) / 2
            print(f'media = {average:0.2f}')
            break
    else:
        print('nota invalida')  
