from math import sqrt, pi
from random import uniform
orign = [0, 0]
min_of_x, max_of_x = -1, 1
min_of_y, max_of_y = -1, 1
def point_rand():
    return [uniform(min_of_x, max_of_x), uniform(min_of_y, max_of_y)]
def dist(x, y):
    return sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
def the_circle(points_in_number):
    points_in = 0
    for i in range(points_in_number):
        if dist(point_rand(), orign) <= 1:
            points_in += 1
    return 4*points_in/points_in_number
approx_pi_100 = the_circle(100)
approx_pi_10000 = the_circle(10000)
approx_pi_1000000 = the_circle(1000000)
for_100_error = abs(approx_pi_100-pi)
for_10000_error = abs(approx_pi_10000-pi)
for_1000000_error = abs(approx_pi_1000000-pi)

print(f'Approximation of pi for 100:\
 {approx_pi_100} and the error is {for_100_error}.')
print(f'Approximation of pi for 10000:\
 {approx_pi_10000} and the error is {for_10000_error}.')
print(f'Pi approximation of pi for 1000000:\
 {approx_pi_1000000} and the error is {for_1000000_error}.')
