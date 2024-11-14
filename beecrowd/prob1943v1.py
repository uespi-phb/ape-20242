
rank = int(input())

if rank <= 1:
    top_rank = 1
elif rank <= 3:
    top_rank = 3
elif rank <= 5:
    top_rank = 5
elif rank <= 10:
    top_rank = 10
elif rank <= 25:
    top_rank = 25
elif rank <= 50:
    top_rank = 50
else:
    top_rank = 100

print('Top', top_rank)
