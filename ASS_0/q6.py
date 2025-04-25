#Defining the function for reverse

def reverse(num):
    revnum = 0
    while(num != 0):
        temp = num % 10
        revnum = revnum*10 + temp
        num = num//10
    print(f"The Reverse of the number:{revnum}")
        
#taking input from the user 
num = int(input("Enter the Number: "))
reverse(num)
