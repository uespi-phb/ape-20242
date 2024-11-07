
last_score = None
while True:
    score = float(input())
    if (score >= 0.0) and (score <= 10.0):
        if not (last_score is None):
            average = (last_score + score) / 2
            print(f'media = {average:0.2f}')
            break
        else:
            last_score = score
    else:
        last_score = None
        print('nota invalida')
