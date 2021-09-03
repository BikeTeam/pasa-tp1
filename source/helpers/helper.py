import numpy as np
import scipy.signal as sps
import matplotlib.pyplot as plt

def frec_shifter(data,fshift=100,sample_rate=4096):
    """
    Frequency shift the signal by constant
    
    Parameters
    ----------
        'data':   array_like - The signal to work on. An array that contains the signal amplitude samples.
        'fshift':        float - the frecuency delta to implement
        'sample_rate':        float - value of sample rate fs in the signal

    Returns
    ----------
        'white_ht': array_like - Resulting shifted signal with the corresponding delta frecuency.
    """
    x = np.fft.rfft(data)
    T = len(data)/float(sample_rate)
    df = 1.0/T
    nbins = int(fshift/df)
    y = np.roll(x.real,nbins) + 1j*np.roll(x.imag,nbins)
    y[0:nbins]=0.
    z = np.fft.irfft(y)
    return z


def plot_spectrograms(strain_h1, strain_l1, fs, f0, f1, t0, t1):
    h1_f, h1_t, h1_sxx = sps.spectrogram(strain_h1, fs, window='blackman', nperseg=256, noverlap=240)
    l1_f, l1_t, l1_sxx = sps.spectrogram(strain_l1, fs, window='blackman', nperseg=256, noverlap=240)

    fig, axs = plt.subplots(1,2, figsize=(20,7))
    fig.suptitle('LIGO event spectrogram')

    # Plot H1 spectrogram
    axs[0].pcolormesh(h1_t, h1_f, h1_sxx, shading='gouraud')
    axs[0].set_ylabel('Frequency [Hz]')
    axs[0].set_label('Time [sec]')
    axs[0].set_ylim(f0, f1)
    axs[0].set_xlim(t0, t1)
    axs[0].set_title('H1')

    # Plot L1 spectrogram
    axs[1].pcolormesh(l1_t, l1_f, l1_sxx, shading='gouraud')
    axs[1].set_ylabel('Frequency [Hz]')
    axs[1].set_label('Time [sec]')
    axs[1].set_ylim(f0, f1)
    axs[1].set_xlim(t0, t1)
    axs[1].set_title('L1');
    
    fig.show()