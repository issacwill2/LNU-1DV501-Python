# Enter a positive integer like 25 and find the largest k such that 0+2.+k < 25

number = int(input('Enter a positive integer: '))
k = 0
sum = 0
if number < 1:
    print('please enter positive number')
else:
    for i in range(0, number, 2):
        sum += i
    if sum < number:
        k = i
    print(k, 'is the largest k such that 0+2+4+6+...+k < 25')

s=0
n=25
h=0
while k < n:
    h+=2
    k+=h
print(h)