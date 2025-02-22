
str_1 = input('Enter a sentence\n')
str_2 = input('Enter the occurring word you want to find\n')

if str_2 not in str_1:
    print("-1")
else:
    l_1 = len(str_1)
    l_2 = len(str_2)
    ret = -1  # Default value if not found
    
    # Searching from the end manually
    for i in range(l_1 - l_2, -1, -1):  # Iterate from back to front
        if str_1[i:i + l_2] == str_2:
            ret = i
            break  # Stop at the first (last-found) occurrence from the back
    
    print(ret)  # Last occurrence index