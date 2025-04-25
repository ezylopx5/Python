a = ord('a')
z = ord('z')
list_alpha = []
for i in range(a,z+1):
    list_alpha.append(chr(i))

# A = ord('A')
# Z = ord('Z')
# for j in range(A,Z+1):
#     list_alpha.append(chr(j))

str_1 = str(input("Enter the sentence: ")).lower()
temp = set(str_1)
temp_1 = set(list_alpha)

if temp_1.issubset(temp) == True:

    print('pangram')
else:
    print('Not a pangram')
