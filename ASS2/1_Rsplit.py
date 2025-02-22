#using rsplit without its functon
str_1 = str(input('Enter a sentence\n'))
# str_2 = str(input('Enter a sentence\n'))
s = int(input('Enter the number for split\n'))

list_1 = list(str_1)
l = len(list_1)
b = l - s
list_2 = []

for i in range(l,b):#from reverse
    list_2.append(list_1[i])
    list_1.remove(list_1[i])

a ="".join(list_1)
list_3 = list(a)
print(list_3+list_1)
