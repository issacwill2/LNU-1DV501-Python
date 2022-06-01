from random import randint

def lotto(list, value):
    for digit in list:
        if digit == value:
            return True
    return False
begin = 1
ended = 35
numbers_of_lotto = [randint(begin, ended)]
available = 0

for i in range(6):
    available = randint(begin, ended)
    while lotto(numbers_of_lotto, available):
        available = randint(begin, ended)
    numbers_of_lotto.append(available)
print(numbers_of_lotto)
