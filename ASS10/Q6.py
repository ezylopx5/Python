import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 4*x - 9  # Example function

def bisection_method(a, b, tol=1e-5):
    """Find root using the bisection method."""
    iterations = []
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        iterations.append(c)
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, np.array(iterations)

# Initial Interval
root, updates = bisection_method(-5, 5)

# Plot the process
plt.plot(updates, f(updates), 'ro-', label="Bisection Steps")
plt.axhline(0, color='black', linestyle='--')
plt.xlabel("x-value")
plt.ylabel("f(x)")
plt.title("Bisection Method for Root Finding")
plt.legend()
plt.show()