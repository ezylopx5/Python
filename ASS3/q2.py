# 2. Is Fibo
# You are given a integer, N. Write a program to determine if N is an element of the Fibonacci Sequence.
# The first few elements of Fibonacci sequence are 0,1,1,2,3,5,8, 13...... A Fibonacci sequence is one where every element is a sum of the previous two elements in the sequence. The first two elements are 0 and 1.
def fibo(num):
    if(num == 0):
        return 0
    
    if(num == 1):
        return 1
    return fibo(num-2)+fibo(num-1)


t_cases = int(input("Enter the number of test cases:\n"))

for i in range(t_cases):
    exp = int(input("Enter the number\n"))
    list_temp = []
    for j in range(exp+5):
        list_temp.append(fibo(j))
    if exp in list_temp:
        print('Is A FIBO')
    else:
        print('Is NOT FIBO')