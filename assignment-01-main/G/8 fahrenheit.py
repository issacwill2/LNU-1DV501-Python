# The users will enter a degree fahrenheit and it will be converted,
#  and computed or printed to celsius.

fahrenheit = float(input("enter a temperature in Fahrenheit: "))
celsius = (fahrenheit-32)*5/9
result = (round(celsius, 2))

print("temperature in Celsius is:", result, "c")
