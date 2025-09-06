#This is my 5th File...

import numpy as np
from Signal_ICT_Dharmik_92400133054.unitary_signals import unit_step, unit_impulse, ramp_signal
from Signal_ICT_Dharmik_92400133054.trigonometric_signals import sine_wave, cosine_wave
from Signal_ICT_Dharmik_92400133054.operations import time_shift, signal_addition, signal_multiplication

if __name__ == "__main__":
    # Discrete signals
    vijay = np.arange(-10, 11)

    # Continuous signals
    t = np.linspace(0, 1, 500)

    # Author variable
    ram = unit_step(vijay)
    jay = unit_impulse(vijay)
    amit = ramp_signal(vijay)

    # 2) Trigonometric signals
    sine = sine_wave(2, 5, t)
    cos = cosine_wave(2, 5, t)

    # 3) Time shift
    time_shift(sine, np.arange(len(sine)), 5)

    # 4) Signal addition (unit step + ramp)
    signal_addition(ram, amit, vijay)

    # 5) Signal multiplication (sine * cosine)
    signal_multiplication(sine, cos, t)
