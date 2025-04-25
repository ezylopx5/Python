import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

# Convert to upper case
upper_case = s.str.upper()

# Convert to lower case
lower_case = s.str.lower()

# Find string lengths
lengths = s.str.len()

print("Upper Case:\n", upper_case)
print("Lower Case:\n", lower_case)
print("String Lengths:\n", lengths)