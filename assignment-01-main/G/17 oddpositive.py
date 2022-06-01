# we have from -15 to 15 integers and we get numbers randomly with identifying them,
import random  

num = random.randint(-15,15)

if num < 0:
  if num % 2 == 0:
      print("The generated number is",num,"\n",num, "is even and negative")
  else:
      print("The generated number is",num,"\n",num, "is odd and negative")
elif num > 0:
  if num % 2 == 0:
      print("The generated number is",num,"\n",num, "is even and positive")
  else :
      print("The generated number is",num,"\n",num, "is odd and positive")
elif num == 0:
      print("The generated number is",num,"\n",num,"is even and neither positive nor negative")
