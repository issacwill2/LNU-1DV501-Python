# the users need to see a saving amount after 5 years by entering. 
# the intial amount and interest rate in percentage.

amount = int(input("Initial savings amount: "))
interst_rate = int(input("Interest rate %: "))
rate = interst_rate * 0.01
n = 1
nt = 5
result = round(amount*(1+rate/n)**nt)
print("The amount of savings after 5 years is:", result)
