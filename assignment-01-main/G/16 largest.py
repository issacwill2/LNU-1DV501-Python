# we will find out the largest number.

print("enter three integers below")
A = int(input("enter A: "))
B = int(input("enter B: "))
C = int(input("enter C: "))

if C < B < A:
    print("The largest number is: ", A)
elif B < C < A:
    print("The largest number is: ", A)
elif C < A < B:
    print("The largest number is: ", B)
elif B < A < C:
    print("The largest number is: ", C)
elif A < C < B:
    print("The largest number is: ", B)
elif A < B < C:
    print("The largest number is: ", C)
