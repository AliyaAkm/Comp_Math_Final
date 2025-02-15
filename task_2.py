import numpy as np
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


def f(x):
    return x ** 3 - x - 2


# bisection method
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    iterations = 0
    x_prev = a
    x_curr = b
    relative_errors = []

    while iterations < max_iter:
        x_mid = (a + b) / 2

        if x_mid != 0:
            relative_error = abs((x_mid - x_prev) / x_mid) if iterations > 0 else 0
            relative_errors.append(relative_error)

        if abs(f(x_mid)) < tol:
            break

        if f(a) * f(x_mid) < 0:
            b = x_mid
        else:
            a = x_mid

        x_prev = x_curr
        x_curr = x_mid
        iterations += 1

    return x_curr, iterations, relative_errors


# The Secant Method
def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    iterations = 0
    relative_errors = []

    while iterations < max_iter:

        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        relative_error = abs((x_new - x1) / x_new)
        relative_errors.append(relative_error)

        if abs(f(x_new)) < tol:
            break

        x0 = x1
        x1 = x_new
        iterations += 1

    return x1, iterations, relative_errors


# graphing function
def plot_graph(a, b):
    x_values = np.linspace(a, b, 400)
    y_values = f(x_values)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=r'$f(x) = x^3 - x - 2$', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.title("Graph of f(x) = x^3 - x - 2")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()


# func to calculate

def calculate():
    try:

        x_min = float(entry_xmin.get())
        x_max = float(entry_xmax.get())

        if x_min >= x_max:
            messagebox.showerror("Interval Error", "The minimum value must be less than the maximum value.")
            return

        root_bisection, iter_bisection, errors_bisection = bisection_method(f, x_min, x_max)

        root_secant, iter_secant, errors_secant = secant_method(f, x_min, x_max)

        result_label.config(text=f"Method: Bisection\nRoot: {root_bisection}\nIterations: {iter_bisection}")
        result_label2.config(text=f"Method: Secant\nRoot: {root_secant}\nIterations: {iter_secant}")

        plot_graph(x_min, x_max)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for the interval.")


# create interface
root = tk.Tk()
root.title("Root Finding Tool")

# interface for input info
label_xmin = tk.Label(root, text="Enter minimum x value:")
label_xmin.grid(row=0, column=0, padx=10, pady=5)
entry_xmin = tk.Entry(root)
entry_xmin.grid(row=0, column=1, padx=10, pady=5)

label_xmax = tk.Label(root, text="Enter maximum x value:")
label_xmax.grid(row=1, column=0, padx=10, pady=5)
entry_xmax = tk.Entry(root)
entry_xmax.grid(row=1, column=1, padx=10, pady=5)

# button for calculate
calculate_button = tk.Button(root, text="Calculate Root", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# result
result_label = tk.Label(root, text="Method: \nRoot: \nIterations: ", justify=tk.LEFT)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

result_label2 = tk.Label(root, text="Method: \nRoot: \nIterations: ", justify=tk.LEFT)
result_label2.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
