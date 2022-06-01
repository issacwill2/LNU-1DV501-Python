def concat(s, n):
    return s*n
def count(s, x):
    count_x = 0
    for character in s:
        if character == x:
            count_x += 1
    return count_x
def reverse(s):
    reverse = ' '
    for character in s:
        reverse = character + reverse
    return reverse
def first_last(s):
    first = s[0]
    last = s[len(s)-1]
    return first, last

def has_two(s, x):
    return count(s, x) == 2

def has_two_X(s):
    return has_two(s, 'X')

def has_duplicates(s):
    for character in s:
        if has_two(s, character):
            return True
    return False
