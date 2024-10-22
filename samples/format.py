
fruits = ['Abacate', 'Limão', 'Manga', 'Melancia', 'Laranja']
prices = [7.13, 1.50, 14.95, 122.95, 9.00]

print('-' * 28)
print('|%-15s|%10s|' % ('Fruta', 'Preço'))
print('-' * 28)

for i in range(0, len(fruits)):
    print('|%-15s|%10.2f|' % (fruits[i], prices[i]))

print('-' * 28)
