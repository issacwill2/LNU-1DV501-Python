# enter a positive integer: 100
# 19 is the smallest k such 1+3+5+7+...+k >= 100

# Find smallest N such
# that 1+2+3+...+N > 100

s = 0  # sum
k = 1
j = int(input("enter a positive integer: "))
while s <= j:
    k += 2  # N = 1,2,3,4, ...
    s += k  # s = 1,3,6,10, ...
print("Smallest k is", k-2)
print(k-2,s)

