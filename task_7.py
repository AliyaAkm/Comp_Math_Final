import numpy as np
import tkinter as tk
from tkinter import messagebox

# func to fit quadratic polynomial and compute second derivative
def estimate_second_derivative(x_points, y_points, x_to_estimate):
    # quadratic polynomial y = ax^2 + bx + c
    coefficients = np.polyfit(x_points, y_points, 2)

    second_derivative = 2 * coefficients[0]

    return second_derivative

# func to process input and calculate second derivative
def calculate_second_derivative():
    try:
        # reading input
        x_values = list(map(float, entry_x.get().split(',')))
        y_values = list(map(float, entry_y.get().split(',')))
        x_target = float(entry_x_target.get())

        if len(x_values) != len(y_values):
            messagebox.showerror("input error", "num of x and y values must be the same")
            return

        estimated_value = estimate_second_derivative(np.array(x_values), np.array(y_values), x_target)

        result_label.config(text=f"estimated d²y/dx² at x={x_target}: {estimated_value:.4f}")

    except ValueError:
        messagebox.showerror("input error", "pls, enter correct num")

# creating interface with tkinter
root = tk.Tk()
root.title("Second Derivative using Polynomial Fit")

# input x and y
tk.Label(root, text="Enter x (comma-separated):").grid(row=0, column=0, padx=10, pady=5)
entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1, padx=10, pady=5)
entry_x.insert(0, "5,6,7,8")

tk.Label(root, text="Enter y (comma-separated):").grid(row=1, column=0, padx=10, pady=5)
entry_y = tk.Entry(root)
entry_y.grid(row=1, column=1, padx=10, pady=5)
entry_y.insert(0, "25,36,49,64")

tk.Label(root, text="enter x to estimate:").grid(row=2, column=0, padx=10, pady=5)
entry_x_target = tk.Entry(root)
entry_x_target.grid(row=2, column=1, padx=10, pady=5)
entry_x_target.insert(0, "1")

compute_button = tk.Button(root, text="Compute Second Derivative", command=calculate_second_derivative)
compute_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="result", justify=tk.LEFT)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
