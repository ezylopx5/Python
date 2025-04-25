#Write a program that generates 100 random integers that are either 0 or 1. 
# Then find the longest run of zeros, the largest number of zeros in a row. For instance, 
# the longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

import random
num = random.randint(1, 10)

listofzero = [1,0,1,1,0,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0]
listcount = []
n = len(listofzero)
for i in range(0,n):

    if listofzero[i] == 0:
        listcount.append(i)

