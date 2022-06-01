
from random import randint

def random_list(n):
    lst = []
    for _ in range(n):
        lst.append(randint(1, 100))
    return lst
random = random_list(10)
print(random)


def average(lst):
    sum_ = 0
    for n in lst:
        sum_ += n
    return round(sum_/len(lst))
avrg = average(random)
print(f'\nthe average of our list is: {avrg}')


def only_odd(lst):
    odd_list = []
    for n in lst:
        if n % 2 == 1:
            odd_list.append(n)
    return odd_list
odd_ball = only_odd(random)
print(f'\nhere are the odd elements in our list: {odd_ball}')


def to_string(lst):
    str_ = ''
    for n in lst:
        str_ += f'{str(n)}, '
    return str_
stringy_boi = to_string(odd_ball)
print(f'\ngere it is as a string: {stringy_boi}')


def contains(lst, a, b):
    stop = len(lst)-1
    for i in range(stop):
        if lst[i] == a:
            if lst[i+1] == b:
                return True
    return False

def has_duplicates(lst):
    match_count = 0
    for i in lst:
        for j in lst:
            if i == j:
                match_count += 1
            if match_count > 1:
                return True
        match_count = 0
    return False

import List_functions as lis_fun









big_random = random_list(20)
has_1_then_2 = contains(big_random, 1, 2)
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
