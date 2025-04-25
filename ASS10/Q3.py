import numpy as np

def generate_magic_square(n):
    """Generate an N×N magic square."""
    if n % 2 == 1:
        magic_square = np.zeros((n, n), dtype=int)
        i, j = 0, n // 2
        for num in range(1, n * n + 1):
            magic_square[i, j] = num
            i -= 1
            j += 1
            if num % n == 0:
                i += 2
                j -= 1
            elif i < 0:
                i = n - 1
            elif j == n:
                j = 0
        return magic_square
    else:
        return f"Magic square generation for even n is more complex."

for size in [4, 5, 6, 7, 8]:
    print(f"\nMagic Square for N={size}:")
    print(generate_magic_square(size))