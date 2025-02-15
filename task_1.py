import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect
import tkinter as tk
from tkinter import messagebox

# func to calculate the value
def f(x):
    return np.e - x - x**2

# func to show graph
def plot_function():
    try:
        # take info
        x_min = float(entry_xmin.get())
        x_max = float(entry_xmax.get())

        # build a graph
        x_values = np.linspace(x_min, x_max, 400)
        y_values = f(x_values)

        plt.figure(figsize=(8,6))
        plt.plot(x_values, y_values, label=r'$f(x) = e - x - x^2$', color='blue')
        plt.axhline(0, color='black',linewidth=1)
        plt.axvline(0, color='black',linewidth=1)
        plt.title("Graph of f(x) = e -x - x^2")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        plt.show()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for the interval.")


def find_root():
    try:
        # take the interval
        x_min = float(entry_xmin.get())
        x_max = float(entry_xmax.get())

        # check to the codderct info
        if x_min >= x_max:
            messagebox.showerror("Interval Error", "The minimum value must be less than the maximum value.")
            return


        root = bisect(f, x_min, x_max, xtol=1e-6)

        # Count the error
        true_root = 0.567143
        absolute_error = abs(root - true_root)

        # print the result
        result_label.config(text=f"Root: {root}\nAbsolute error: {absolute_error}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for the interval.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# create interface
root = tk.Tk()
root.title("Root Finding Tool")

# interface for input interval
label_xmin = tk.Label(root, text="Enter minimum x value:")
label_xmin.grid(row=0, column=0, padx=10, pady=5)
entry_xmin = tk.Entry(root)
entry_xmin.grid(row=0, column=1, padx=10, pady=5)

label_xmax = tk.Label(root, text="Enter maximum x value:")
label_xmax.grid(row=1, column=0, padx=10, pady=5)
entry_xmax = tk.Entry(root)
entry_xmax.grid(row=1, column=1, padx=10, pady=5)

# graph
plot_button = tk.Button(root, text="Plot Function", command=plot_function)
plot_button.grid(row=2, column=0, columnspan=2, pady=10)

# root
find_root_button = tk.Button(root, text="Find Root", command=find_root)
find_root_button.grid(row=3, column=0, columnspan=2, pady=10)

#print
result_label = tk.Label(root, text="Root: \nAbsolute error: ", justify=tk.LEFT)
result_label.grid(row=4, column=0, columnspan=2, pady=10)


root.mainloop()
