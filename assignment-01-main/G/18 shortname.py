# 1st letter of the First and 4 letter of Last name will be printed as 
# short name.

first_name = input("First name: ")
last_name = input("Last name: ")

# print("Short name: ", first_name[0],". ", last_name[:4])

print(f'shortname: {first_name[0]}. {last_name[:4]}')
