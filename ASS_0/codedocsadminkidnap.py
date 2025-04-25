#Magician had N boxes and gold coin; He puts gold coin into the Xth box and performs 'S' swaps

#'t' is the test cases
t = int(input(" "))
#N is the Number boxes and S is the number of swaps and the X is

for j in range(t):
    #in each swap we have to take input from the user
    N,X,S = map(int,input("").split())

    for i in range(S):
        a,b = map(int,input("").split())
        
        if(a != X and b != X):
            print("Coin is not present in either 'a' or 'b'")

        if(a == X and b != X):
            
            X = b

        elif(a != X and b == X):
            
            X = a
    
print(X)


