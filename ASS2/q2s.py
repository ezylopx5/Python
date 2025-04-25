# Dictionary to store product names and prices
dict_1 = {}

# Taking product input from the user
print("Enter product names and prices. Type 'done' to stop.")

while True:
    in_key = input("Product Name: ").strip()
    if in_key.lower() == "done":
        break  # Stop input when the user types "done"
    
    try:
        in_val = float(input("Price: "))  # Allow decimal prices
        dict_1[in_key] = in_val  # Store in dictionary
    except ValueError:
        print("Invalid price. Please enter a numeric value.")

# Searching for product prices
while True:
    pro = input("\nEnter a product name to check price (or 'exit' to stop): ").strip()
    
    if pro.lower() == "exit":
        break  # Stop search when the user types "exit"

    # Check if the product exists in dictionary
    if pro in dict_1:
        print(f"Price of {pro}: ₹{dict_1[pro]}")
    else:
        print(f"{pro} not found in the product list.")