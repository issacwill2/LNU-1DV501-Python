
# print("Right Angled Triangle") print("Isosceles Triangle")

n = int(input("enter odd positive number: "))

if n % 2 == 0 or n < 0:
    print("please enter odd positive number")

# Right Angled Triangle
else:
    for i in range(n):
        for x in range(n - i):
            print("*", end="")
        print()

# Isosceles Triangle
    for i in range(n):
        print(" "*(n - i)+"* "*i)

