
price_table = (
    4.00,
    4.50,
    5.00,
    2.00,
    1.50,
)

item_id, item_quantity = map(int, input().split())

bill_total = item_quantity * price_table[item_id - 1]

print('Total: R$ %0.2f' % (bill_total))
