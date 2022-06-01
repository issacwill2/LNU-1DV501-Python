from random import randint

def dice_side():
    return randint(1, 6)
print('Frequency table (sum,count) for rolling two dices 10000 times')
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10000):
    sum_of_dice = dice_side()+dice_side()
    result[sum_of_dice-2] += 1
exist = 2
for i in result:
    print(f'{exist}: {i}')
    exist += 1
