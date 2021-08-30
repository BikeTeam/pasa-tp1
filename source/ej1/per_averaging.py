import numpy as np

def periodogram_averaging(data, K, L):
    #Check parameters
    data_array = np.array(data)
    N = len(data_array)

    #Create periodograms

    #Average periodograms