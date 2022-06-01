import os
from math import sqrt


file_path = os.getcwd()
print(file_path)  # C:\Users\issac\Documents\1dv501.03

file_path_a = os.getcwd()+'\\assign_03\\10000_integers\\\
file_10000integers_A.txt'
file_path_b = os.getcwd()+'\\assign_03\\10000_integers\\\
file_10000integers_B.txt'
print(file_path_a)


def mean(lst):
    total = 0
    for i in lst:
        total += i
    return total/len(lst)


def standard_deviation(list):
    value_of_mean = mean(list)
    total = 0
    for i in list:
        total += (i-value_of_mean)**2
    return sqrt(total/len(list))


def int_file(path, seplt):
    lst_int = []
    try:
        with open(path, 'r') as files:
            for line in files:
                for i in line.split(seplt):
                    lst_int.append(int(i))
        return lst_int
    except FileNotFoundError:
        print(f'Path is Not founded : {path} shows not to file.')
        exit(0)
    except ValueError:
        print('ValueError')
        exit(0)


lst_a = int_file(file_path_a, ',')
lst_b = int_file(file_path_b, ':')
print('10000integers_A: ')
print('Mean', mean(lst_a))
print('Std', standard_deviation(lst_a))

print('\n10000integers_B: ')
print('Mean', mean(lst_b))
print('std', standard_deviation(lst_b))

# OUTPUT
'''
10000integers_A:
Mean 250.139
Std 69.4854609180943

10000integers_B:
Mean 11.0053
std 100.73912979527891
'''
