matriz_size = 12

operation = input()

ref_index = matriz_size // 2

sum = 0
count = 0
for i in range(matriz_size):
    for j in range(matriz_size):
        value = float(input())
        if (i > ref_index) and (j >= matriz_size - i) and (j <= i - 1):
            count += 1
            sum += value

if operation == 'M':
    result = sum / count
else:
    result = sum

print('%0.1f' % (result))
