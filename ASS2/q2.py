# Write a program that repeatedly asks the user to enter product names and prices. Store all of these in a dictionary whose keys are the product names and whose values are the 
# prices.
# When the user is done entering products and prices, allow them to rep
# eatedly enter a product name and print the corresponding price or a message if the product is not in the dictionary

#lets take a input from the user
dict_1 = {}
print("Enter the name of product and its price: ")
in_key = str(input(""))
in_val = int(input(""))

print("'If you want to continue then press 'y' and not then press 'n'" )
per1 = str(input(""))

while per1 == 'y':
    in_key = str(input(""))
    in_val = int(input(""))
    dict_1[in_key] = in_val #This is how you take input in dictonary
    per1 = chr(input("Want to continue? "))

pro = str(input("Enter the name of that product: "))

if pro in dict_1:
    print(dict_1.get("pro"))
print("Want to enter more name 'y' or 'n':")
per1 = str(input(""))
while per1 == 'y':
    pro = str(input("Enter the name of that product: "))
    if pro in dict_1:
        print(dict_1.get("pro"))
    print("Want to enter more name 'y' or 'n':")
    per1 = str(input(""))








    




