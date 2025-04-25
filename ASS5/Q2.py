t = int(input())

for i in range(t):
        # k = map(int,input("").split())
        k = int(input())
        if k%2 == 0:
            j = k//2
            in_p = j*j
            print(f"{in_p}")
        else:
            in_p1 = k + 1
            in_p2 = in_p1 // 2 
            in_p3 = k - in_p2
            in_p4 = in_p3 * in_p2
            print(in_p4)



