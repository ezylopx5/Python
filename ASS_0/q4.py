#taking the input from the user
x = int(input("Enter the number for 'X' : "))
y = int(input("Enter the number for 'Y' : "))

#Swaping the variable
x = x + y
y = x - y
x = x - y

#Printing the output
print(f"Now 'X' is {x} and 'Y' is {y}")
