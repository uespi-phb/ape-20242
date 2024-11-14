
rank = int(input())

top_ranks = (1, 3, 5, 10, 25, 50, 100)

for top_rank in top_ranks:
    if rank <= top_rank:
        break

print('Top', top_rank)
