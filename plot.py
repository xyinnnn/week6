import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

def F(t):
    return np.maximum(1 - np.abs(t), 0)

def G(t):
    return 4 * (np.heaviside(-t, 1) - np.heaviside(-t - 5, 1))


t = np.linspace(-10, 10, 1000)


F_t = F(t)
G_t = G(t)


plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.plot(t, F_t, label="F(t)")
plt.title("F(t)")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, G_t, label="G(t)")
plt.title("G(t)")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

convolution = convolve(F_t, G_t, mode='full') 
convolution = convolution / np.max(convolution)
t_conv = np.linspace(2 * t[0], 2 * t[-1], len(convolution))

plt.figure(figsize=(8, 5))
plt.plot(t_conv, convolution)
plt.title("Convolution of F and G")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

