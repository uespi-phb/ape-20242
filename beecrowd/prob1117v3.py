
sum_valid_scores = 0
count_valid_scores = 0

while True:
    score = float(input())

    if (score >= 0.0) and (score <= 10.0):
        count_valid_scores += 1
        sum_valid_scores += score       

        if count_valid_scores == 2:
            average_scores = sum_valid_scores / count_valid_scores
            print(f'media = {average_scores:0.2f}')
            break
    else:
        print('nota invalida')