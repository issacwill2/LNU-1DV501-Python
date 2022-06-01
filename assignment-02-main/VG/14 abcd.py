def get_number(a, b, c, d):
    return 1000 * a + 100 * b + 10 * c + d


a, b, c, d = 0, 0, 0, 0
for one in range(1, 10):
    if a != 0:
        break
    for two in range(0, 10):
        if a != 0:
            break
        for three in range(0, 10):
            if a != 0:
                break
            for four in range(1, 10):
                if get_number(one, two, three, four)*4 == get_number(four, three, two, one):
                    a, b, c, d = one, two, three, four
                    break

print(f'a = {a}\tb = {b}\tc = {c}\td = {d}')
print(f'ABCD*4 = DCBA: {get_number(a, b, c, d)}*4 = {get_number(a, b, c, d)*4}')
