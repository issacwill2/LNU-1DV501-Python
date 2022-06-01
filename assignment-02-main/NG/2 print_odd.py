# print odd
k = int(input("enter a positive integer: "))
n = 1
while n <= k:
    print("odd numbers: ", n, end=(" "))
    n += 2
if n < 0:
    print("please enter positive number: ")
