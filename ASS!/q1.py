
#(A)
lista = []
for i in range(50):
    lista.append(i)

print(lista)

#(B)
listb = []
for j in range(1,51):
    listb.append(i*i)

print(listb)

#(C) The list ['a','bb','ccc, dddd',..] that ends with 26 copies of the letter z.

listc = []
for k in range(1,27):
    char = chr(96+k)
    listc.append(char*k)
   

print(listc)
