import numpy as np
from scipy import signal as ss
from scipy.fft import fft

def periodogram_smothing(signal, L, window='bartlett', M=None):
    """
    La funcion periodogram_smothing estima la densidad espectral de potencia de la señal signal
    utilizando el metodo de Periodogram Smopthing
    
    Parametros
    ----------
        'signal': la señal con la cual se quiere trabajar
        'L': tamaño de la ventana de autocorrelación
        'M': parametro para el ancho del lobulo si se utiliza ventana bm_tukey
        'fs': frecuencia de muestreo de la señal
        'window': ventana que se desea utilizar para la autocorrelación
                    Solo soporta 'bartlett', 'parzen', 'bm_tukey'(sinc)
    """
    # Busco el largo de la señal
    N = len(signal)
    
    # Calculo la autocorrelación de la señal
    lags = np.arange(-(N-1), N)
    rxx = ss.correlate(signal, signal, method='direct') / N
    rxx = rxx[np.logical_and(lags > -L, lags < L)]
    lags = lags[np.logical_and(lags > -L, lags < L)]

    win = None
    
    # Armo la ventana seleccionada
    if window == 'bartlett':
        win = ss.windows.bartlett(2 * L - 1) 
    elif window == 'parzen':
        win = ss.windows.parzen(2 * L - 1)
    elif window == 'bm_tukey':
        dw, t = (2 * np.pi / N) * (2 * M + 1), np.arange(-L + 1, L)
        w = np.sinc(t * dw / (2 * np.pi)) * (dw / (2*np.pi))
        win = w / max(w) # Normalizo la ventana w(0) = 1
    
    if win is None:
        raise ValueError("Unknown window.")
    
    # Multiplico la
    windowed_rxx = rxx * win
    
    spectre = np.abs(fft(windowed_rxx, norm='forward')) 
    freq = np.arange(len(spectre)) / len(spectre)

    freq, spectre = freq[freq < 0.5], spectre[freq < 0.5]
    
    return freq, spectre