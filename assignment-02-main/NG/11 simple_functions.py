# 1
# 1 A function is_odd(n)) that returns True if the integer n is odd, otherwise False.
def is_odd(n):
    if n%2==0:
        return(False)
    else:
        return(True)
result = is_odd(5)
print(result)
# 2
def sum_range(m,n):
    n or m != 1
    sum=0
    for i in range (m,n+1):
        i+=1
        sum+=i
        return sum
result = sum_range(1,5)
print(result)
# 3
def contains(str):
    X=False
    Y=False
    for c in str:
        if c=="X":
            X=True
        if c == "Y":
            Y = True
    if X and Y==True:
       return X
    else:
        return False
print(contains("XYlofon"))  # True
print(contains("Xylofon"))  # False
# 4
def multi_print(s, n):
    return (s + " ") * n
print(multi_print("hello", 5))
