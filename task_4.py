import numpy as np
import tkinter as tk
from tkinter import messagebox


# func to do LU factorization
def lu_decomposition(A):
    n = A.shape[0]
    L = np.zeros_like(A)
    U = np.zeros_like(A)

    # here we use gauss method for LU factorization
    for i in range(n):
        # here we are filling U matrix
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])

        # here we are filling L matrix
        L[i, i] = 1  # L's main diagonal always equal to 1
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

    return L, U


# Func for input processing and do LU factorization
def calculate():
    try:
        # reading matrix A
        a11 = float(entry_a11.get())
        a12 = float(entry_a12.get())
        a13 = float(entry_a13.get())
        a21 = float(entry_a21.get())
        a22 = float(entry_a22.get())
        a23 = float(entry_a23.get())
        a31 = float(entry_a31.get())
        a32 = float(entry_a32.get())
        a33 = float(entry_a33.get())

        # creating matrix A
        A = np.array([[a11, a12, a13],
                      [a21, a22, a23],
                      [a31, a32, a33]])

        L, U = lu_decomposition(A)

        result_label.config(text=f"Matrix L:\n{L}\n\nMatrix U:\n{U}")

    except ValueError:
        messagebox.showerror("input error", "pls, input correct number.")


# creating interface with tkinter
root = tk.Tk()
root.title("LU-factorization")

# input interface
label_a11 = tk.Label(root, text="a11:")
label_a11.grid(row=0, column=0, padx=10, pady=5)
entry_a11 = tk.Entry(root)
entry_a11.grid(row=0, column=1, padx=10, pady=5)

label_a12 = tk.Label(root, text="a12:")
label_a12.grid(row=1, column=0, padx=10, pady=5)
entry_a12 = tk.Entry(root)
entry_a12.grid(row=1, column=1, padx=10, pady=5)

label_a13 = tk.Label(root, text="a13:")
label_a13.grid(row=2, column=0, padx=10, pady=5)
entry_a13 = tk.Entry(root)
entry_a13.grid(row=2, column=1, padx=10, pady=5)

label_a21 = tk.Label(root, text="a21:")
label_a21.grid(row=3, column=0, padx=10, pady=5)
entry_a21 = tk.Entry(root)
entry_a21.grid(row=3, column=1, padx=10, pady=5)

label_a22 = tk.Label(root, text="a22:")
label_a22.grid(row=4, column=0, padx=10, pady=5)
entry_a22 = tk.Entry(root)
entry_a22.grid(row=4, column=1, padx=10, pady=5)

label_a23 = tk.Label(root, text="a23:")
label_a23.grid(row=5, column=0, padx=10, pady=5)
entry_a23 = tk.Entry(root)
entry_a23.grid(row=5, column=1, padx=10, pady=5)

label_a31 = tk.Label(root, text="a31:")
label_a31.grid(row=6, column=0, padx=10, pady=5)
entry_a31 = tk.Entry(root)
entry_a31.grid(row=6, column=1, padx=10, pady=5)

label_a32 = tk.Label(root, text="a32:")
label_a32.grid(row=7, column=0, padx=10, pady=5)
entry_a32 = tk.Entry(root)
entry_a32.grid(row=7, column=1, padx=10, pady=5)

label_a33 = tk.Label(root, text="a33:")
label_a33.grid(row=8, column=0, padx=10, pady=5)
entry_a33 = tk.Entry(root)
entry_a33.grid(row=8, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text=" LU-factorization", command=calculate)
calculate_button.grid(row=9, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="result:\nmatrix L and U", justify=tk.LEFT)
result_label.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()
