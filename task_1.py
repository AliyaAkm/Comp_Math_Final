import numpy as np
import matplotlib.pyplot as plt

# Task 1: First Derivative Using Newton’s Forward Difference Formula

# Given data
x = np.array([0, 2, 4, 6, 8])
y = np.array([1, 4, 16, 36, 64])

# Step size
h = x[1] - x[0]

# Forward difference table
n = len(y)
forward_diff = np.zeros((n, n))
forward_diff[:, 0] = y

for j in range(1, n):
    for i in range(n - j):
        forward_diff[i, j] = forward_diff[i + 1, j - 1] - forward_diff[i, j - 1]

# First derivative using Newton's Forward Difference formula
dy_dx = forward_diff[0, 1] / h

# Plotting the function and tangent
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x, y, label='Function y=f(x)')
plt.axline((x[0], y[0]), slope=dy_dx, color='green', linestyle='dashed', label='Tangent at x=0')

# Plot settings
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('First Derivative (Newton’s Forward Difference)')
plt.grid()
plt.show()

# Output result
print(f"First derivative at x=0: {dy_dx}")
