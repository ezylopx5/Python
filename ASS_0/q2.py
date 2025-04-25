#By making a function
def fact(num):
    if(num == 0):
        return 1
    a = fact(num-1)*num
    return a


#taking input from the user
num = int(input("Enter the number: "))

result = fact(num)
print(f"The factorial of number is : {result}")
