import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox


# func to perform polynomial fitting
def fit_polynomial(x_data, y_data):
    # solving linear system for coeff a, b, c
    A = np.vstack([x_data**2, x_data, np.ones(len(x_data))]).T
    coefficients = np.linalg.lstsq(A, y_data, rcond=None)[0]
    return coefficients


# func show graph and results
def plot_curve():
    try:
        # reading points
        x_points = np.array([float(entry_x0.get()), float(entry_x1.get()), float(entry_x2.get()), float(entry_x3.get()), float(entry_x4.get())])
        y_points = np.array([float(entry_y0.get()), float(entry_y1.get()), float(entry_y2.get()), float(entry_y3.get()), float(entry_y4.get())])

        coefficients = fit_polynomial(x_points, y_points)

        # generate curve x and y based on coeff
        x_curve = np.linspace(min(x_points), max(x_points), 100)
        y_curve = coefficients[0]*x_curve**2 + coefficients[1]*x_curve + coefficients[2]

        # plot graph
        plt.plot(x_points, y_points, 'ro', label='Data points')
        plt.plot(x_curve, y_curve, label='Fitted quadratic curve', color='blue')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Polynomial Curve Fitting')
        plt.legend()
        plt.grid(True)
        plt.show()

        result_label.config(text=f"Coefficients: a = {coefficients[0]:.4f}, b = {coefficients[1]:.4f}, c = {coefficients[2]:.4f}")

    except ValueError:
        messagebox.showerror("input error", "pls, enter correct number")

# creating interface with tkinter
root = Tk()
root.title("Polynomial Curve Fitting")

# input interface
label_x0 = Label(root, text="x0:")
label_x0.grid(row=0, column=0, padx=10, pady=5)
entry_x0 = Entry(root)
entry_x0.grid(row=0, column=1, padx=10, pady=5)

label_y0 = Label(root, text="y0:")
label_y0.grid(row=1, column=0, padx=10, pady=5)
entry_y0 = Entry(root)
entry_y0.grid(row=1, column=1, padx=10, pady=5)

label_x1 = Label(root, text="x1:")
label_x1.grid(row=2, column=0, padx=10, pady=5)
entry_x1 = Entry(root)
entry_x1.grid(row=2, column=1, padx=10, pady=5)

label_y1 = Label(root, text="y1:")
label_y1.grid(row=3, column=0, padx=10, pady=5)
entry_y1 = Entry(root)
entry_y1.grid(row=3, column=1, padx=10, pady=5)

label_x2 = Label(root, text="x2:")
label_x2.grid(row=4, column=0, padx=10, pady=5)
entry_x2 = Entry(root)
entry_x2.grid(row=4, column=1, padx=10, pady=5)

label_y2 = Label(root, text="y2:")
label_y2.grid(row=5, column=0, padx=10, pady=5)
entry_y2 = Entry(root)
entry_y2.grid(row=5, column=1, padx=10, pady=5)

label_x3 = Label(root, text="x3:")
label_x3.grid(row=6, column=0, padx=10, pady=5)
entry_x3 = Entry(root)
entry_x3.grid(row=6, column=1, padx=10, pady=5)

label_y3 = Label(root, text="y3:")
label_y3.grid(row=7, column=0, padx=10, pady=5)
entry_y3 = Entry(root)
entry_y3.grid(row=7, column=1, padx=10, pady=5)

label_x4 = Label(root, text="x4:")
label_x4.grid(row=8, column=0, padx=10, pady=5)
entry_x4 = Entry(root)
entry_x4.grid(row=8, column=1, padx=10, pady=5)

label_y4 = Label(root, text="y4:")
label_y4.grid(row=9, column=0, padx=10, pady=5)
entry_y4 = Entry(root)
entry_y4.grid(row=9, column=1, padx=10, pady=5)

calculate_button = Button(root, text="Fit Polynomial Curve", command=plot_curve)
calculate_button.grid(row=10, column=0, columnspan=2, pady=10)

result_label = Label(root, text="Coeff will be displayed here.", justify=LEFT)
result_label.grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()
