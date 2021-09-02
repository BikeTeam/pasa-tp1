from scipy.fft import fft
import scipy.signal as sps
import numpy as np

def periodogram(signal_, window='boxcar', padding=False, use_autocorrelation=False):

    """
    The function estimates the power spectral density of the signal by using the Periodogram method.
    
    Parameters
    ----------
        'signal': The signal to work on. An array that contains the signal amplitude samples.
        'use_autocorrelation': Boolean indicating which method is going to be used to estimate psd.
        'window': String that indicates window form.
        'padding': Indicates whether to perform zero padding to have double precision on spectrum. Only works in 'periodogram by definition' mode.

    Returns
    ----------
        'freqs': An array that represents the normalized frequencies of the resulting periodogram's samples.
        'avg_periodogram': An array that represents the resulting periodogram. Each sample has units of V**2/Hz.
    """
    # Create signal copy
    signal = signal_.copy()
    # Get number of samples
    N = signal.shape[0]

    # Apply window if needed

    if use_autocorrelation == True:
        # Autocorrelation method
        ac = np.correlate(signal, signal, mode='full') / N
        per = np.absolute(fft(ac, norm='ortho'))
        # Now we have 2N-1 points instead of N. Then there is an improvement in frequency resolution.
        xf = np.arange(len(per)) / len(per)
    
    else:

        # Apply window if required
        if window == 'bartlett':
            signal *= sps.windows.bartlett(N)
        elif window == 'parzen':
            signal *= sps.windows.parzen(N)
        elif window == 'hann':
            signal *= sps.windows.hann(N)
        elif window == 'hamming':
            signal *= sps.windows.hamming(N)

        # By definition
        # First, compute the signal FFT
        # Adding zero-padding to enhance frequency resolution
        if padding==True:
            signal = np.pad(signal, (N//2,N//2))
            
        yf = fft(signal, norm='ortho')
        xf = np.arange(len(yf)) / len(yf)
        
        # Calculate periodogram by powering amplitude spectrum modulus by 2 and dividing by N
        per = (np.abs(yf)**2) / N
        
    # Returning positive freq spectrum only
    return xf[xf <= 0.5], per[xf <= 0.5]   