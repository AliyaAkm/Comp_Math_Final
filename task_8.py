import numpy as np
import tkinter as tk
from tkinter import messagebox

def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("n must be even for Simpson's Rule")

    h = (b - a) / n  # step size
    x = np.linspace(a, b, n+1)
    y = f(x)

    integral = (h / 3) * (y[0] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2]) + y[n])
    return integral

# def func f(x) = sin(x)
def f(x):
    return np.sin(x)

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get())

        if n % 2 == 1:
            messagebox.showerror("input error", "num of subintervals must be even")
            return

        I_approx = simpsons_rule(f, a, b, n)
        I_exact = 2  # we calculated this earlier
        error = abs(I_exact - I_approx)

        result_label.config(text=f"Simpson's Rule Approximation: {I_approx}\nExact Integral Value: {I_exact}\nAbsolute Error: {error}")
    except ValueError:
        messagebox.showerror("input error", "pls, enter correct num")

# creating interface by using tkinter
root = tk.Tk()
root.title("Simpson's Rule Calculator")

label_a = tk.Label(root, text="enter lower limit (a):")
label_a.grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=5)

label_b = tk.Label(root, text="enter upper limit (b):")
label_b.grid(row=1, column=0, padx=10, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=5)

label_n = tk.Label(root, text="enter num of subintervals (even n):")
label_n.grid(row=2, column=0, padx=10, pady=5)
entry_n = tk.Entry(root)
entry_n.grid(row=2, column=1, padx=10, pady=5)

compute_button = tk.Button(root, text="Compute Integral", command=calculate)
compute_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="result", justify=tk.LEFT)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
