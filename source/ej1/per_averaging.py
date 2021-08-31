import numpy as np
from scipy import signal as sig

def periodogram_averaging(signal, K, L):
    """
    The function estimates the power spectral density of the signal by using the Periodogram Averaging method.
    
    Parameters
    ----------
        'signal': The signal to work on. An array that contains the signal amplitude samples.
        'K': Number of segments to divide the signal array into.
        'L': Number of samples of each segment.

    Returns
    ----------
        'freqs': An array that represents the frequencies of the resulting periodogram's samples.
        'avg_periodogram': An array that represents the resulting periodogram. Each sample has units of V**2/Hz.
    """
    if signal is None or signal is np.empty:
        raise ValueError("Signal array doesn't exist.")
    #Check parameters
    data_array = np.array(signal)
    N = len(data_array)

    if K<=0:
        raise ValueError("K must be positive.")

    if L<=0:
        raise ValueError("L must be positive.")

    if K>N:
        raise ValueError("Sample amount (N) must be greater or equal to segments amount (K)")

    if L>N:
        raise ValueError("Invalid. Signal array's size must be greater or equal to segment's size (L).")

    #Create periodograms
    D = int(round(N/K))

    # Add padding due to overlap
    padding_to_add = D*(K-1)+L - N

    if padding_to_add<0:
        raise ValueError("Invalid segment amount or size.")

    padding_beginning = int(padding_to_add/2)
    data_array = np.pad(data_array, (padding_beginning, padding_to_add - padding_beginning), 'edge')

    periodograms = []
    for i in range(K):
        data_i = data_array[D*i:D*i+L]
        f_i, p_i = sig.periodogram(data_i, window='hann')
        periodograms.append(np.array(p_i))
    
    freqs = f_i
    #Average periodograms
    avg_periodogram = np.mean(np.array(periodograms), axis=0)

    return freqs, avg_periodogram

