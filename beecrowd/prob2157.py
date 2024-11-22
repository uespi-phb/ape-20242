
def mirror_sequence(start, end):
    sequence = ''.join(map(str, range(start, end + 1)))
    return sequence + sequence[::-1]


mirror_count = int(input())
while mirror_count > 0:
    mirror_count -= 1

    start, end = map(int, input().split())
    print(mirror_sequence(start, end))
