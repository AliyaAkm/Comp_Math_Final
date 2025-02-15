import numpy as np
import matplotlib.pyplot as plt

# Task 3: First Derivative Using Newton’s Backward Difference Formula.

# Given data
x = np.array([5, 6, 7, 8, 9])
y = np.array([10, 16, 26, 40, 58])

# Step size
h = x[1] - x[0]

# Backward difference table
n = len(y)
backward_diff = np.zeros((n, n))
backward_diff[:, 0] = y

for j in range(1, n):
    for i in range(n - j):
        backward_diff[i + 1, j] = backward_diff[i + 1, j - 1] - backward_diff[i, j - 1]

# First derivative using Newton's Backward Difference formula
dy_dx = backward_diff[-1, 1] / h

# Plot function and tangent
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x, y, label='Function y=f(x)')
plt.axline((x[-1], y[-1]), slope=dy_dx, color='green', linestyle='dashed', label='Tangent at x=9')

# Plot settings
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('First Derivative (Newton’s Backward Difference)')
plt.grid()
plt.show()

# Output result
print(f"First derivative at x=9: {dy_dx}")
