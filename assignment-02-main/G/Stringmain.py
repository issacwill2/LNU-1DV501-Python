import Stringfunctions as str_fun

s = 'William '

print(str_fun.concat(s, 4))
print(str_fun.count(s, 'l'))
print(str_fun.reverse(s))
print(f'The first and last letter in {s} is: {str_fun.first_last(s)}')

if str_fun.has_two_X(s):
    print(f'{s} has two X')

exist_2X = 'XXyy'
more_2X = 'XXXyyy'

if str_fun.has_two_X(exist_2X):
    print(f'{exist_2X} has two X')

if str_fun.has_two_X(more_2X):
    print(f'{more_2X} has two X')

if str_fun.has_duplicates(s):
    print(f'{s} has duplicates')
