import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Define the functions F(t) and G(t)
def F(t):
    # Triangle function, defined between -1 and 1
    return np.maximum(1 - np.abs(t), 0)

def G(t):
    # Step function, 4 between t = -5 and t = 0
    return 4 * (np.heaviside(-t, 1) - np.heaviside(-t - 5, 1))

# Create an array of t values
t = np.linspace(-10, 10, 1000)

# Evaluate functions
F_t = F(t)
G_t = G(t)

# Plot F and G
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

# Compute the convolution
convolution = convolve(F_t, G_t, mode='full')  # 'full' for complete convolution
# Normalize the convolution to account for the discretization effect
convolution = convolution / np.max(convolution)
# Adjust time axis for convolution (the time axis will be twice as long minus one sample due to 'full' mode)
t_conv = np.linspace(2 * t[0], 2 * t[-1], len(convolution))

# Plot the convolution
plt.figure(figsize=(8, 5))
plt.plot(t_conv, convolution)
plt.title("Convolution of F and G")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

