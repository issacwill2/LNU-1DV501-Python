
ld = "b5"
letter = "abcdefgh"


letter.index(ld[0])
hor = int(letter.index(ld[0]) )+1
ver = int(ld[-1])

(hor + ver) % 2 

letter = "abcdefgh"
color_number = (input("Enter a chess square identifier (e.g. e5): "))
ver = int(letter.index(color_number[0]) )+1
hor = int(ld[-1])
result = hor + ver

if result % 2 == 1:
  print(color_number, "is black")
else: 
  print(color_number, "is white")
