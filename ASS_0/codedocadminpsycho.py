#Taking number input from user;we gotta do is .-^
no_ofmem = int(input(""))
listnum = []

#Taking other numbers  [7,9,87,96,14]
for i in range(0,no_ofmem):
    membersnum = int(input(""))
    listnum.append(membersnum)

for ind,num in enumerate(listnum):
    print(ind,num)
    





