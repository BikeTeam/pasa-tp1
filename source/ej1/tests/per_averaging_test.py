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
f, Pxx = welch(data, nperseg = L, noverlap=L-D)
print('Test 1')
print(manual_averaging)
print(Pxx)

L2 = 70
K2 = 20
D2 = int(N/K2)
manual_averaging2 = periodogram_averaging(data,K2,L2)
f2, Pxx2 = welch(data, nperseg = L2, noverlap=L2-D2)
print('Test 2')
print(manual_averaging2)
print(Pxx2)
