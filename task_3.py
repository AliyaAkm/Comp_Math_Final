import numpy as np
import tkinter as tk
from tkinter import messagebox


# func to gauss_seidel method
def gauss_seidel_iteration(x, y, z):
    # update
    x_new = 9 - y - z
    y_new = 7 - z
    z_new = 3 - x
    return x_new, y_new, z_new


def gauss_seidel(x0, y0, z0, tol=1e-6, max_iter=100):
    #  initial values for x, y, z
    x, y, z = x0, y0, z0
    iteration = 0
    while iteration < max_iter:

        x_old, y_old, z_old = x, y, z

        x, y, z = gauss_seidel_iteration(x, y, z)

        if (abs(x - x_old) < tol) and (abs(y - y_old) < tol) and (abs(z - z_old) < tol):
            break

        iteration += 1

    return x, y, z, iteration


# func to calculate

def calculate():
    try:

        tol = float(entry_tol.get())
        max_iter = int(entry_max_iter.get())

        #  x0, y0, z0
        x0 = float(entry_x.get())
        y0 = float(entry_y.get())
        z0 = float(entry_z.get())

        # run method gauss_seidel
        x, y, z, iterations = gauss_seidel(x0, y0, z0, tol, max_iter)

        # print results
        result_label.config(text=f"Solution:\n x = {x}\n y = {y}\n z = {z}\nNumber of iterations: {iterations}")

    except ValueError:
        messagebox.showerror("Input error", "Please enter the correct values.")


# create interface
root = tk.Tk()
root.title("Gauss-Seidel method")

# interface for input
label_x = tk.Label(root, text="Enter the initial value of x:")
label_x.grid(row=0, column=0, padx=10, pady=5)
entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1, padx=10, pady=5)

label_y = tk.Label(root, text="Enter the initial value of y:")
label_y.grid(row=1, column=0, padx=10, pady=5)
entry_y = tk.Entry(root)
entry_y.grid(row=1, column=1, padx=10, pady=5)

label_z = tk.Label(root, text="Enter the initial value of z:")
label_z.grid(row=2, column=0, padx=10, pady=5)
entry_z = tk.Entry(root)
entry_z.grid(row=2, column=1, padx=10, pady=5)

label_tol = tk.Label(root, text="Enter the precision:")
label_tol.grid(row=3, column=0, padx=10, pady=5)
entry_tol = tk.Entry(root)
entry_tol.grid(row=3, column=1, padx=10, pady=5)

label_max_iter = tk.Label(root, text="Enter the maximum number of iterations:")
label_max_iter.grid(row=4, column=0, padx=10, pady=5)
entry_max_iter = tk.Entry(root)
entry_max_iter.grid(row=4, column=1, padx=10, pady=5)

# button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Solution:\n x = \n y = \n z = \nNumber of iterations: ", justify=tk.LEFT)
result_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
