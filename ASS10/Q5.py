import numpy as np

array = np.array(["AI", "Machine Learning", "Deep Learning", "NIT", "SVNIT", "Python"])

# Center Justified
centered = np.char.center(array, 15, "_")

# Left Justified
left_justified = np.char.ljust(array, 15, "_")

# Right Justified
right_justified = np.char.rjust(array, 15, "_")

print("Centered:\n", centered)
print("Left Justified:\n", left_justified)
print("Right Justified:\n", right_justified)