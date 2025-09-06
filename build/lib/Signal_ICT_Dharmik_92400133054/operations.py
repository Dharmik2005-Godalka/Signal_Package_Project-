#This is 3rd file created...

"""Signal operations:
- Time shifting
- Time scaling
- Signal addition
- Signal multiplication"""

import numpy as np
import matplotlib.pyplot as plt

def time_shift(x: np.ndarray, n: np.ndarray, k: int):
    """Shifts signal by k units."""
    shifted_n = n - k
    plt.stem(n, x, linefmt="b-", markerfmt="bo", basefmt=" ", label="Original")
    plt.stem(shifted_n, x, linefmt="r--", markerfmt="ro", basefmt=" ", label=f"Shifted by {k}")
    plt.legend()
    plt.title("Time Shift Operation")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.grid(True)
    plt.show()
    return shifted_n, x

def time_scale(x: np.ndarray, n: np.ndarray, a: int):
    """Scales time axis by factor a."""
    scaled_n = n * a
    plt.stem(n, x, linefmt="b-", markerfmt="bo", basefmt=" ", label="Original")
    plt.stem(scaled_n, x, linefmt="g--", markerfmt="go", basefmt=" ", label=f"Scaled by {a}")
    plt.legend()
    plt.title("Time Scale Operation")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.grid(True)
    plt.show()
    return scaled_n, x

def signal_addition(x1: np.ndarray, x2: np.ndarray, n: np.ndarray):
    """Adds two signals element-wise."""
    y = x1 + x2
    plt.stem(n, y)
    plt.title("Signal Addition")
    plt.xlabel("n")
    plt.ylabel("x1[n] + x2[n]")
    plt.grid(True)
    plt.show()
    return y

def signal_multiplication(x1: np.ndarray, x2: np.ndarray, t: np.ndarray):
    """Multiplies two signals element-wise."""
    y = x1 * x2
    plt.plot(t, y)
    plt.title("Signal Multiplication")
    plt.xlabel("t")
    plt.ylabel("x1(t) * x2(t)")
    plt.grid(True)
    plt.show()
    return y
