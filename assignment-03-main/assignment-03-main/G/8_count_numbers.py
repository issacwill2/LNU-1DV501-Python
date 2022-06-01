import os

file = os.getcwd()

file_path_a = os.getcwd()+'\\assign_03\\10000_integers\\\
file_10000integers_A.txt'
file_path_b = os.getcwd()+'\\assign_03\\10000_integers\\\
file_10000integers_B.txt'


def read_file_A(file_path):
    with open(file_path_a, 'r')as file:
        my_fil = file.read()
        a = my_fil.strip().replace('\n', ', ')
        lst = a.split(', ')
        return lst


def read_file_B(file_path):
    with open(file_path_b, 'r')as file:
        my_fil = file.read()
        a = my_fil.strip().replace(':', ', ')
        lst = a.split(', ')
        return lst


def count_different(lst):
    lst1 = set(lst)
    lst2 = len(lst1)
    return lst2


def count_occurrences(lst):
    dct = {}
    for digit in lst:
        if digit in dct:
            dct[digit] += 1
        else:
            dct[digit] = 1

    count_sort = sorted(dct.items(), key=lambda v: v[1], reverse=True)
    print('Numbers:\tOccurrences:')
    for i in range(5):
        print(f'{count_sort[i][0]}\t\t{count_sort[i][1]}')


def main():
    a = read_file_A(file_path_a)
    b = read_file_B(file_path_b)
    print('different A: ', count_different(a))
    print('Top 5 numbers that occurred in file A:')
    count_occurrences(a)

    print('\ndifferent B: ', count_different(b))
    print('Top 5 numbers that occurred in file B:')
    count_occurrences(b)


main()

# OUTPUT
'''different A:  424
Top 5 numbers that occurred in file A:
Numbers:        Occurrences:
238             76
260             72
240             71
217             70
252             69

different B:  584
Top 5 numbers that occurred in file B:
Numbers:        Occurrences:
22              62
35              53
37              51
-12             50
23              49'''
