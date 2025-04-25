# Take numbers from 1 to 10000. Create equivalence classes for modulo 5 on this set of
# numbers. Check the validity of your equivalence classes. 
#[Hint: the union of all equivalence classes should be the original set/list.]
list_ = []
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
#taking input in 1 to 1000 list
for i in range(1,1001):
    list_.append(i)

#now finding the the equivalence classes
for num in list_:
    if num%5 == 0:
        list_1.append(num)
    if num%5 == 1:
        list_2.append(num)
    if num%5 == 2:
        list_3.append(num)
    if num%5 == 3:
        list_4.append(num)
    if num%5 == 4:
        list_5.append(num)

result = sorted(list_1+list_2+list_3+list_4+list_5)
print(result)


#now comparing numbers in list of(1to1000) and all other list
if list_ == result:
    print("It works")