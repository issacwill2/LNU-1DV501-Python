''''Enter a large positive integer: 6789500'''

number = input("Enter a large positive integer: ")
zero, odd, even = 0, 0, 0


for digit in number:
    if digit == '0':
        zero += 1

    elif digit == '1':
        odd += 1
    elif digit == '3':
        odd += 1
    elif digit == '5':
        odd += 1
    elif digit == '7':
        odd += 1
    elif digit == '9':

        odd += 1
    elif digit == '2':
        even += 1
    elif digit == '4':
        even += 1
    elif digit == '6':
        even += 1
    elif digit == '8':
        even += 1

print("\nzero: ", zero)
print("odd: ", odd)
print("even: ", even)
