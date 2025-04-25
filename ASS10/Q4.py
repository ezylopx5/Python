import numpy as np
import random
N = 10  # Generate at least 10 random points
cartesian_points = np.random.rand(N, 2) * 10  # Random points in range (0,10)

# Convert to polar coordinates
r = np.sqrt(cartesian_points[:, 0]**2 + cartesian_points[:, 1]**2)
theta = np.arctan2(cartesian_points[:, 1], cartesian_points[:, 0])

polar_coordinates = np.column_stack((r, theta))
print("Polar Coordinates:\n", polar_coordinates)