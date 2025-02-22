import math
orilist = []
newlist = []
#For Input
for i in range(10):
    X,Y,Z = map(int,input("").split())
    orilist.append([X,Y,Z])

for (X,Y,Z) in orilist:
    dislist = []
    for (x,y,z) in orilist:
        dis = math.sqrt(pow(X-x,2)+pow(Y-y,2)+pow(Z-z,2))
        if dis != 0.0:
            dislist.append((dis,(x,y,z)))
    add = min(dislist)
    newlist.append(add)
    
print(newlist)
        
    
