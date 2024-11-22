
input()

numbers = map(int, input().split())

div2_count = 0
div3_count = 0
div4_count = 0
div5_count = 0

for number in numbers:
    if number % 2 == 0:
        div2_count += 1
    if number % 3 == 0:
        div3_count += 1
    if number % 4 == 0:
        div4_count += 1
    if number % 5 == 0:
        div5_count += 1

print(div2_count,'Multiplos(s) de 2')
print(div3_count,'Multiplos(s) de 3')
print(div4_count,'Multiplos(s) de 4')
print(div5_count,'Multiplos(s) de 5')
