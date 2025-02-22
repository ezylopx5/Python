# 3. Utopian Tree
# The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the monsoon, when it doubles in height. The second growth cycle occurs during the summer, when its height increases by l meter.
# Now, a new Utopian tree sapling is planted at the onset of the monsoon. Its height is 1 meter. Can you find the height of the tree after N growth cycles?

tcases = int(input("Enter the number of test cases\n"))
total = 1
for i in range(tcases):
    n = int(input("Enter the number of the cycle:\n"))
    for num in range(1,n+1):
        if num%2 != 0:
            total *= 2

        else:
            total += 1 
    print(total)
    total = 1
