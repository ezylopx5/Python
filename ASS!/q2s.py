import random

# Step 1: Generate 100 random integers (0 or 1)
random_numbers = [random.randint(0, 1) for _ in range(100)]

# Step 2: Find the longest run of zeros
longest_run = 0
current_run = 0

for num in random_numbers:
    if num == 0:
        current_run += 1
        longest_run = max(longest_run, current_run)
    else:
        current_run = 0  # Reset the count if 1 is encountered

# Print the results
print("Generated list:", random_numbers)
print("Longest run of zeros:", longest_run)