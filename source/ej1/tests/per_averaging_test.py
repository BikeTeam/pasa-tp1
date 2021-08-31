import numpy as np
from scipy.signal.spectral import welch
import matplotlib.pyplot as plt
import sys
# Add the folder path to the sys.path list
sys.path.append('source/ej1/')
from per_averaging import periodogram_averaging

# Test without overlap
data = np.random.rand(5000)
L = 100
N = len(data)
K = 50
D = int(round(N/K))

manual_averaging = periodogram_averaging(data,K,L)
f, Pxx = welch(data, nperseg = L, noverlap=L-D,)

plt.plot(f, manual_averaging, color = 'red', label = 'manual')
plt.plot(f, Pxx, color = 'green', label = 'scipy')
plt.legend()
plt.title('Comparison Test. Without Overlap')
plt.grid()
plt.show()

# Test with overlap
L2 = 70
K2 = 200
D2 = int(round(N/K2))

manual_averaging2 = periodogram_averaging(data,K2,L2)
f2, Pxx2 = welch(data, nperseg = L2, noverlap=L2-D2)

plt.plot(f2, manual_averaging2, color = 'red', label = 'manual')
plt.plot(f2, Pxx2, color = 'green', label = 'scipy')
plt.legend()
plt.title('Comparison Test. With Overlap')
plt.grid()
plt.show()