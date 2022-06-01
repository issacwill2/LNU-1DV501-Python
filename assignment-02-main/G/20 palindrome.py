
def no_remove_all(strings):
    for i in range(20, 100):
        strings = strings.replace(chr(i), '')
    for i in range(140, 160):
        strings = strings.replace(chr(i), '')
    return strings

def palindrome(strings):
    strings = strings.lower()
    strings = no_remove_all(strings)
    length = len(strings)
    ends = length//2
    for i in range(ends):
        is_equal = strings[i] == strings[length-(i+1)]
        if is_equal:
            continue
        return False
    return True

palindromee = "Was it a rat I saw?"

if palindrome(palindromee):
    print(f'{palindromee} is a palindrome')
not_palindrome = '\nwe are students.'
if not palindrome(not_palindrome):
    print(f'{not_palindrome} is not a palindrome\n')

string_te = 'we study online, is not it good? ?=><<<\n'
print(string_te)
print(no_remove_all(string_te))

