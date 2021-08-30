import numpy as np
from scipy.signal.spectral import welch
import sys
# Add the folder path to the sys.path list
sys.path.append('source/ej1/')
from per_averaging import periodogram_averaging

data = np.random.rand(500)
L = 10
N = len(data)
K = 40
D = int(N/K)

manual_averaging = periodogram_averaging(data,K,L)
print(manual_averaging)

f, Pxx = welch(data, nperseg = L, noverlap=L-D)
print(Pxx)
