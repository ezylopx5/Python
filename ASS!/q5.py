
namelist = []
for i in range(10):
    name = str(input(f"Enter the name of the {i+1}'s Student name: "))
    if len(name) < 15:
        namelist.append(name)
    else :
        print('name is exceeding limit of 15 charecters')

print(namelist)
print("\n")
#Reverse the name 
revnamelist = []
for name in namelist:
    revname = name[::-1]
    revnamelist.append(revname)

print(revnamelist)


