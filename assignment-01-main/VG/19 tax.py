
income = int(input("Please provide monthly income: ") )

if income < 38000:
 print("Corresponding income tax: ", int(income * 0.3) )
elif income > 38000 and income < 50000: 
 print ("Corresponding income tax: ",int(38000*0.3) + int((income-50000) * 0.35))
elif income > 50000:
 print ("Corresponding income tax: ",int(38000*0.3) + int((12000*0.35)) + int((income-50000) * 0.4))
    
   