# lets take input from the user

tcase = int(input("Enter the number of testcases: "))
count = 0
for i in range(1,tcase+1):
    count = 0
    exp = int(input("Enter the number: "))
    digits = [int(digit) for digit in str(exp)]
    l = len(digits)
    for num in digits:
        if exp%num == 0:
            count += 1
    print(count)
            
