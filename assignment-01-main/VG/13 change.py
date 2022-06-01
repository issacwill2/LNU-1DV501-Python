
price = float(input("price: "))
payment = int(input("payment: ")) 
change = int(payment - price)
round(change)
print("change: ", change, "kr")

kr1000 = change // 1000
print("1000kr bills: ",kr1000) 

kr500 = change % 1000 // 500
print("500kr bills: ",kr500)

kr200 = change % 1000 % 500 // 200
print("200kr bills: ",kr200)

kr100 = change % 1000 % 500 % 200 // 100
print("100kr bills: ",kr100)

kr50 = change % 1000 % 500 % 200 % 100 // 50
print("50kr bills: ",kr50)

kr20 = change % 1000 % 500 % 200 % 100 % 50 // 20
print("20kr bills: ",kr20)
kr10 = change % 1000 % 500 % 200 % 100 % 50 % 20 // 10
print("10kr coins: ",kr10)

kr5 = change % 1000 % 500 % 200 % 100 % 50 % 20 % 10 // 5
print("5kr coins: ",kr5)

kr2 = change % 1000 % 500 % 200 % 100 % 50 % 20 % 10 % 5 // 2
print("2kr coins: ",kr2)

kr1 = change % 1000 % 500 % 200 % 100 % 50 % 20 % 10 % 5 % 2 // 1
print("1kr coins: ",kr1) 
