

def max_element(n):
    max_number = 0
    for index in range(1, n + 1):
        number = int(input())
        if number > max_number:
            max_number = number
            max_index = index
    return {
        'major_number': max_number,
        'major_index': max_index
    }


result = max_element(100)

print(result['major_number'])
print(result['major_index'])
