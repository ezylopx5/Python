#This prorgam is for maximizig XOR
L = int(input())
R = int(input())
#maximum of A XOR B given;                    L <= A <= B <= R

def max_xor(L, R):
    max_val = 0
    for A in range(L, R + 1):
        for B in range(A, R + 1):
            max_val = max(max_val, A ^ B)
    return max_val


print(max_xor(L, R))