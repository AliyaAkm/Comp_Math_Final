import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

# formula of lagrange interpolation
def lagrange_interpolation(x_points, y_points, x_to_estimate):
    result = 0
    n = len(x_points)
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if j != i:
                term *= (x_to_estimate - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# func to show graph and result
def plot_interpolation():
    try:
        # reading x and y points
        x_points = np.array([
            float(entry_x0.get()), float(entry_x1.get()),
            float(entry_x2.get()), float(entry_x3.get())
        ])
        y_points = np.array([
            float(entry_y0.get()), float(entry_y1.get()),
            float(entry_y2.get()), float(entry_y3.get())
        ])

        # estimating the value at x = 5.5
        x_to_estimate = 5.5
        estimated_value = lagrange_interpolation(x_points, y_points, x_to_estimate)

        result_label.config(text=f"Estimated f(5.5) = {estimated_value:.4f}")

        # plot points
        x_curve = np.linspace(min(x_points) - 1, max(x_points) + 1, 100)
        y_curve = np.array([lagrange_interpolation(x_points, y_points, x) for x in x_curve])

        plt.plot(x_points, y_points, 'ro', label='Data points')
        plt.plot(x_curve, y_curve, label='Lagrange Interpolation', color='blue')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Lagrange Interpolation')
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("input error", "pls, enter correct points.")

# creating interface with tkinter
root = Tk()
root.title("Lagrange Interpolation")

# input interface
label_x0 = Label(root, text="x0:")
label_x0.grid(row=0, column=0, padx=10, pady=5)
entry_x0 = Entry(root)
entry_x0.insert(0, "5")
entry_x0.grid(row=0, column=1, padx=10, pady=5)

label_y0 = Label(root, text="y0:")
label_y0.grid(row=1, column=0, padx=10, pady=5)
entry_y0 = Entry(root)
entry_y0.insert(0, "25")
entry_y0.grid(row=1, column=1, padx=10, pady=5)

label_x1 = Label(root, text="x1:")
label_x1.grid(row=2, column=0, padx=10, pady=5)
entry_x1 = Entry(root)
entry_x1.insert(0, "6")
entry_x1.grid(row=2, column=1, padx=10, pady=5)

label_y1 = Label(root, text="y1:")
label_y1.grid(row=3, column=0, padx=10, pady=5)
entry_y1 = Entry(root)
entry_y1.insert(0, "36")
entry_y1.grid(row=3, column=1, padx=10, pady=5)

label_x2 = Label(root, text="x2:")
label_x2.grid(row=4, column=0, padx=10, pady=5)
entry_x2 = Entry(root)
entry_x2.insert(0, "7")
entry_x2.grid(row=4, column=1, padx=10, pady=5)

label_y2 = Label(root, text="y2:")
label_y2.grid(row=5, column=0, padx=10, pady=5)
entry_y2 = Entry(root)
entry_y2.insert(0, "49")
entry_y2.grid(row=5, column=1, padx=10, pady=5)

label_x3 = Label(root, text="x3:")
label_x3.grid(row=6, column=0, padx=10, pady=5)
entry_x3 = Entry(root)
entry_x3.insert(0, "8")
entry_x3.grid(row=6, column=1, padx=10, pady=5)

label_y3 = Label(root, text="y3:")
label_y3.grid(row=7, column=0, padx=10, pady=5)
entry_y3 = Entry(root)
entry_y3.insert(0, "64")
entry_y3.grid(row=7, column=1, padx=10, pady=5)

calculate_button = Button(root, text="Estimate f(5.5) and Plot", command=plot_interpolation)
calculate_button.grid(row=8, column=0, columnspan=2, pady=10)

result_label = Label(root, text="Estimated f(5.5) will appear here.", justify=LEFT)
result_label.grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()
