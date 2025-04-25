# rindex (finds the last occurrence of a substring in a string).
# index (finds the first occurrence of a substring or an element in a sequence).

str_1 = input('Enter a sentence\n')
str_2 = input('Enter the occurring word you want to find\n')

if str_2 not in str_1:
    print("Error")
else:
    # Finding the last occurrence manually (rindex alternative)
    l_1 = len(str_1)
    l_2 = len(str_2)
    
    for i in range(l_1 - l_2, -1, -1):  # Iterate from the back
        if str_1[i:i + l_2] == str_2:
            print("Last occurrence found at index:", i)
            break  # Stop at the first (last-found) occurrence from the back