import numpy as np
from scipy import signal as sig

def periodogram_averaging(data, K, L):
    if data is None or data is np.empty:
        raise ValueError("Data array doesn't exist.")
    #Check parameters
    data_array = np.array(data)
    N = len(data_array)

    if K>N:
        raise ValueError("Invalid. Less array divisions (K) than samples.")

    if L>N:
        raise ValueError("Invalid. Division size (L) is greater than data array size.")

    #Create periodograms
    D = int(N/K)

    if D*(K-1)+L > N:
        zeros_to_add = D*(K-1)+L - N
        zeros = np.zeros(zeros_to_add)
        data_array = np.append(data_array, zeros)

    periodograms = []
    for i in range(K):
        data_i = data_array[D*i:D*i+L]
        f_i, p_i = sig.periodogram(data_i, window='hann')
        periodograms.append(np.array(p_i))
    
    #Average periodograms
    averaged_periodogram = np.mean(np.array(periodograms), axis=0)

    return averaged_periodogram

