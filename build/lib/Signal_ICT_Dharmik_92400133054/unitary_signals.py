#This is my 1st file created...

import numpy as np
import matplotlib.pyplot as plt

My_Name = "Dharmik Godalka"

def unit_step(n: np.ndarray):
    """unit step signal."""
    x = np.where(n >= 0, 1, 0)
    plt.stem(n, x)
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("u[n]")
    plt.grid(True)
    plt.show()
    return x

def unit_impulse(n: np.ndarray):
    """unit impulse signal."""
    x = np.where(n == 0, 1, 0)
    plt.stem(n, x)
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("δ[n]")
    plt.grid(True)
    plt.show()
    return x

def ramp_signal(n: np.ndarray):
    """a ramp signal."""
    x = np.where(n >= 0, n, 0)
    plt.stem(n, x)
    plt.title("Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("r[n]")
    plt.grid(True)
    plt.show()
    return x
