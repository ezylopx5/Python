#lets take a input from the user for A and B
t_cases = int(input('Enter the number of test cases:\n'))
for j in range(t_cases):

    a = int(input('\n'))
    b = int(input('\n'))
    list_sq = []
    for i in range(a,b+1):
        numsq = i ** 0.5
        if numsq == int(numsq):
            list_sq.append(numsq)
    print(len(list_sq))
    




