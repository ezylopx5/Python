num = int(input("Put the value of the length in feet: "))
print('For conversion Press: Inches = 1 ; Yard = 2; Miles = 3; milimeters = 4 ; centimeter = 5; kilometers = 6')

list = [num*12 , num *0.333333 , num * 0.000189394,num * 304.8 ,num * 30.48 , num * 0.3048 ,num * 0.0003048]
#Changed number of indices




#Asking for input
conversion = int(input())
print(list[conversion])

