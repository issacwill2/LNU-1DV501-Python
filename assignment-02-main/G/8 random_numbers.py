# Enter number of integers to be generated: 10

# Generated values: 77 15 13 54 96 73 100 12 98 28
# Average, min, and max are 56.6, 12, and 100

from random import randint
number = None
while type(number) != int or number < 0:
    try:
        number = input("\nEnter number of integers to be generated: ")
        number = int(number)
        if number < 0:
            raise Exception
    except Exception:
        print("\nPlease enter Positive number.")
guessed = [randint(1, 100) for x in range(0, number)]
print(f"\nGenerated Values: {guessed}")
average = sum(guessed)/len(guessed)
maximum = max(guessed)
minimum = min(guessed)
print(f"\nAverage, Max and Min: {average}, {maximum}, {minimum} \n")
