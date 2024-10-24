
fruits = [
    {'name': 'Abacate',  'price':   7.13},
    {'name': 'Limão',    'price':   1.50},
    {'name': 'Manga',    'price':  14.95},
    {'name': 'Melancia', 'price': 122.95},
    {'name': 'Laranja',  'price':   9.00},
]

print('-' * 28)
print('|%-15s|%10s|' % ('Fruta', 'Preço'))
print('-' * 28)

for fruit in fruits:
    print('|%(name)-15s|%(price)10.2f|' % fruit)

print('-' * 28)
