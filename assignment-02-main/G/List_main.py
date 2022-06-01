import List_functions as lis_fun

random = lis_fun.random_list(10)
print(random)

avrg = lis_fun.average(random)
print(f'\nthe average of our list is: {avrg}')

odd_ball = lis_fun.only_odd(random)
print(f'\nhere are the odd elements in our list: {odd_ball}')

stringy_boi = lis_fun.to_string(odd_ball)
print(f'\ngere it is as a string: {stringy_boi}')

big_random = lis_fun.random_list(20)
has_1_then_2 = lis_fun.contains(big_random, 1, 2)
print(f'\nThe list: {big_random}')

if has_1_then_2:
    print('\nhas the numbers 1 and 2 in sequence')
else:
    print('\ndoes not have the numbers 1 and 2 in sequence')
definetly_has_1_and_2 = [1, 2]
has_1_then_2 = lis_fun.contains(definetly_has_1_and_2, 1, 2)
print(f'\nThe list: {definetly_has_1_and_2}')

if has_1_then_2:
    print('\nhas the numbers 1 and 2 in sequence')
else:
    print('\ndoes not have the numbers 1 and 2 in sequence')
duplicates = lis_fun.has_duplicates(big_random)
print(f'\nThe list: {big_random}')

if duplicates:
    print('\nHas duplicates')
else:
    print('\nDoes not have duplicates')
definetley_has_duplicates = [1, 1]
duplicates = lis_fun.has_duplicates(definetley_has_duplicates)

if duplicates:
    print(f'\nThe list {definetley_has_duplicates} has duplicates.')
else:
    print(f'\nThe list {definetley_has_duplicates} does not have duplicates.')
no_duplicates = [1, 2, 3, 4]
duplicates = lis_fun.has_duplicates(no_duplicates)

if duplicates:
    print(f'\nThe list {no_duplicates} has duplicates.')
else:
    print(f'\nThe list {no_duplicates} does not have duplicates.')
