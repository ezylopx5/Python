
# For each test case, output a string lexicographically bigger than w in a separate line. In case of
# multiple possible answers print the lexicographically smallest one and if no answer exists, print
# no answer

t = int(input())
for i in range(t):
    st = str(input())
    ls1 = list(st)
    # ls2 = []
    # for w in ls1:
    #     ls2.append(ord(w))

    # # for i in ls2:
    # ls2  = ls2[::-1]
    # for i in range(len(ls2)-1):
    #     if ls2[i] > ls2[i+1]:
    #         # ls2[i],ls2[i+1] = ls2[i+1],ls2[i]
    #         break
    # ls2 = ls2[::-1]
    # ls3 = []
    # for w in ls2:
    #     ls3.append(chr(w))

    # print(''.join(ls3))
    n = len(ls1)
    i = n - 2
    while ls1[i] > ls1[i+1] and i>= 0:
        i -= 1
    if i == -1:
        print('there is no reverse')
    
    j = n - 1
    while ls1[j] <= ls1[i]:
        j -= 1

    ls1[i],ls1[j] = ls1[j],ls1[i]

    ls1 = ls1[:i+1] + ls1[i+1:][::-1]






