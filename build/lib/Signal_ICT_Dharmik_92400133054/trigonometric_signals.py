#This is my 2nd file Created, with given instruction.

import numpy as np
import matplotlib.pyplot as plt

AUTHOR = "Dharmik Godalka"

def sine_wave(amplitude: float, frequency: float, t: np.ndarray):
    """Generates and plots a sine wave."""
    x = amplitude * np.sin(2 * np.pi * frequency * t)
    plt.plot(t, x)
    plt.title(f"Sine Wave (A={amplitude}, f={frequency} Hz)")
    plt.xlabel("t")
    plt.ylabel("sin(t)")
    plt.grid(True)
    plt.show()
    return x

def cosine_wave(amplitude: float, frequency: float, t: np.ndarray):
    """Generates and plots a cosine wave."""
    x = amplitude * np.cos(2 * np.pi * frequency * t)
    plt.plot(t, x)
    plt.title(f"Cosine Wave (A={amplitude}, f={frequency} Hz)")
    plt.xlabel("t")
    plt.ylabel("cos(t)")
    plt.grid(True)
    plt.show()
    return x

def exponential_signal(a: float, t: np.ndarray):
    """Generates and plots an exponential signal."""
    x = np.exp(a * t)
    plt.plot(t, x)
    plt.title(f"Exponential Signal (a={a})")
    plt.xlabel("t")
    plt.ylabel("e^(at)")
    plt.grid(True)
    plt.show()
    return x
