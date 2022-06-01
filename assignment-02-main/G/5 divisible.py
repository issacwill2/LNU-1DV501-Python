# 100 - 200
# Numbers dividable by 4 0r 5, but not both in range 100 to 200.

n = 0

def dividable(n, i):
    print(i, end=' ')
    n += 1
    if n % 10 == 0:
        print(' ')
    return n

for i in range(100, 201):
    if i % 4 == 0:
        if i % 5 != 0:
            n = dividable(n, i)
    elif i % 5 == 0:
        n = dividable(n, i)
