import numpy as np
import matplotlib.pyplot as plt

# Task 4: Derivative Using Unequally Spaced Values

# Given data
x = np.array([1, 2, 4, 7])
y = np.array([3, 6, 12, 21])
x_target = 3  # Compute dy/dx at x=3

# Lagrange formula for derivatives
def lagrange_derivative(x, y, x_target):
    n = len(x)
    derivative = 0

    for i in range(n):
        term = 0
        for j in range(n):
            if i != j:
                prod = 1
                for k in range(n):
                    if k != i and k != j:
                        prod *= (x_target - x[k]) / (x[i] - x[k])
                term += prod / (x[i] - x[j])
        derivative += y[i] * term

    return derivative

# Compute first derivative
dy_dx = lagrange_derivative(x, y, x_target)

# Plot function and tangent
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x, y, label='Function y=f(x)')
plt.axline((x_target, np.interp(x_target, x, y)), slope=dy_dx, color='green', linestyle='dashed', label=f'Tangent at x={x_target}')

# Plot settings
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('First Derivative (Lagrange Formula)')
plt.grid()
plt.show()

# Output result
print(f"First derivative at x=3: {dy_dx}")
