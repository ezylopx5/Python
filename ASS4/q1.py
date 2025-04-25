t_case = int(input('The number of test cases: '))

for _ in range(t_case):
    tot_1 = 0
    str_o = input('Write a string: ')  # Example: 'adflp'
    l = len(str_o)

    if l % 2 == 0:  # Even-length string case
        
        m = l // 2
        m -= 1
        str_1 = list(str_o[:m+1])
        str_2 = list(str_o[m+1:])
        str_3 = str_2[::-1]

        if str_1 == str_3:
            print('it is already palindrome')
        else:
            for n in range(len(str_1)):
                while str_1[n] != str_3[n]:
                    if str_1[n] > str_3[n]:
                        str_1[n] = chr(ord(str_1[n])-1)
                    else:
                        str_3[n] = chr(ord(str_3[n])-1)
                    tot_1 += 1
        print(''.join(str_1)+''.join(str_3[::-1]))
        print(tot_1)

        
    else:  # Odd-length string case
        i = l // 2
        str_1 = list(str_o[:i])  # First half as a list
        str_2 = list(str_o[i+1:])  # Second half as a list
        str_3 = str_2[::-1]  # Reverse of second half

        if str_1 == str_3:
            print('It is already a palindrome\n0')
        else:
            # # Convert first half to 'a'
            # for j in range(len(str_1)):
            #     while str_1[j] != 'a':
            #         str_1[j] = chr(ord(str_1[j]) - 1)
            #         tot_1 += 1

            # # Convert reversed second half to 'a'
            # for k in range(len(str_3)):
            #     while str_3[k] != 'a':
            #         str_3[k] = chr(ord(str_3[k]) - 1)
            #         tot_1 += 1
            for v in range(len(str_1)):
                while str_1[v] != str_3[v]:
                    
                    if str_1[v] > str_3[v]:
                        str_1[v] = chr(ord(str_1[v]-1))
                    else:
                        str_3[v] = chr(ord(str_3[v])-1)
                    tot_1 += 1

            print('It is now a palindrome:')
            print(''.join(str_1) + str_o[i] + ''.join(str_3[::-1]))  # Forming the palindrome
            print('Total operations needed:', tot_1)