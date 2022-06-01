from random import randint


def integer_pos(will_be_given):
    while True:
        pos_integer = int(input(will_be_given))
        return pos_integer

the_point_angle = [0, 0]


size = integer_pos('Enter the size: ')
steps = integer_pos('Enter the number of steps: ')
sailors = integer_pos('Enter the number of sailors: ')

position = 0
digits = 0

for i in range(sailors):
    for _ in range(steps):
        position = randint(0, 1)
        the_point_angle[position] += (-1)**randint(1, 2)
        if -size <= the_point_angle[position] <= size:
            continue
        digits += 1
        break
    the_point_angle = [0, 0]

print(f'Out of {sailors} sailors {digits}\
    ({round(100*digits/sailors,2)}%) fell in the water.')
