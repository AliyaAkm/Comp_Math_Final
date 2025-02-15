import numpy as np
import matplotlib.pyplot as plt

# Given data
x = np.array([2, 4, 6, 8, 10])
y = np.array([5, 7, 8, 6, 3])

# Finding the index of maximum and minimum values
max_index = np.argmax(y)  # Maximum
min_index = np.argmin(y)  # Minimum

max_x, max_y = x[max_index], y[max_index]
min_x, min_y = x[min_index], y[min_index]

# Plot function and extremum points
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x, y, label='Function y=f(x)')
plt.scatter(max_x, max_y, color='blue', label='Maximum', zorder=3)
plt.scatter(min_x, min_y, color='green', label='Minimum', zorder=3)

# Plot settings
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Maximum and Minimum of the Tabulated Function')
plt.grid()
plt.show()

# Output results
print(f"Function reaches a maximum at x={max_x}, y={max_y}")
print(f"Function reaches a minimum at x={min_x}, y={min_y}")
