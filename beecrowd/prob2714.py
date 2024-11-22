

def generate_password(ra):
    if (len(ra) == 20) and (ra[:2] == 'RA'):
        return str(int(ra[2:]))
    else:
        return 'INVALID DATA'


ra_count = int(input())
while ra_count > 0:
    ra_count -= 1

    ra = input().strip('\n')
    password = generate_password(ra)
    print(password)
