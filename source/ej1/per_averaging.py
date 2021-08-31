import numpy as np
from scipy import signal as sig

def periodogram_averaging(data, K, L):
    if data is None or data is np.empty:
        raise ValueError("Data array doesn't exist.")
    #Check parameters
    data_array = np.array(data)
    N = len(data_array)

    if K<=0:
        raise ValueError("K must be positive.")

    if L<=0:
        raise ValueError("L must be positive.")

    if K>N:
        raise ValueError("Sample amount (N) must be greater or equal to segments amount (K)")

    if L>N:
        raise ValueError("Invalid. Data array's size must be greater or equal to segment's size (L).")

    #Create periodograms
    D = int(round(N/K))

    # Add zero padding due to overlap
    zeros_to_add = D*(K-1)+L - N

    if zeros_to_add<0:
        raise ValueError("Invalid segment amount or size.")

    zeros_beginning = int(zeros_to_add/2)
    data_array = np.pad(data_array, (zeros_beginning, zeros_to_add - zeros_beginning), 'edge')

    periodograms = []
    for i in range(K):
        data_i = data_array[D*i:D*i+L]
        f_i, p_i = sig.periodogram(data_i, window='hann')
        periodograms.append(np.array(p_i))
    
    #Average periodograms
    avg_periodogram = np.mean(np.array(periodograms), axis=0)

    return f_i, avg_periodogram

