D = int(input("enter three digits: "))
res = 0
added = D

while D > 0:
    remainder = D % 10
    res = res + remainder
    D = int(D/10)

print("Sum of digits: ", added, ": ", res)

D = (input("enter three digits: "))

one = int(D[0])
two = int(D[1])
three = int(D[2])

sum = one + two + three
print("Sum of digits: ", sum)

