import numpy as np
import matplotlib.pyplot as plt

# Given data (reused from Task 1)
x = np.array([0, 2, 4, 6, 8])
y = np.array([1, 4, 16, 36, 64])

# Step size
h = x[1] - x[0]

# Forward difference table (recreate it here)
n = len(y)
forward_diff = np.zeros((n, n))
forward_diff[:, 0] = y

for j in range(1, n):
    for i in range(n - j):
        forward_diff[i, j] = forward_diff[i + 1, j - 1] - forward_diff[i, j - 1]

# Second derivative using Newton's Forward Difference formula
d2y_dx2 = forward_diff[0, 2] / (h ** 2)

# Plotting second derivative values
plt.scatter(x[:-2], forward_diff[:-2, 2], color='blue', label="Second difference Δ²y")
plt.axhline(d2y_dx2, color='green', linestyle='dashed', label="d²y/dx² at x=0")

# Plot settings
plt.xlabel('x')
plt.ylabel('Δ²y')
plt.legend()
plt.title('Second Derivative (Newton’s Forward Difference)')
plt.grid()
plt.show()

# Output result
print(f"Second derivative at x=0: {d2y_dx2}")
