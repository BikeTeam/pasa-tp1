def check_stationarity(p_value, threshold = 0.05, type='unit'):
    """
    The function compares the p_value obtained by a stationarity or unit root test with a threshold to determine wether a signal is stationary or not.
    
    Parameters
    ----------
        'p_value':      float - The p-value of the test. 
        'threshold':    float - The limit of the p-value below which the null hypothesis of the test is rejected.
        'type':         string - 'unit' (default): The test corresponds to a unit root test. 'kpss': The test corresponds to a Kwiatkowski-Phillips-Schmidt-Shin test.
    """
    print(f'p-value: {p_value:.2f}')
    print(f'p-threshold: {threshold}')
    if p_value > threshold:
        if type == 'unit':
            print('=> Serie No Estacionaria')
        elif type == 'kpss':
            print('=> Serie Estacionaria')
    else:
        if type == 'unit':
            print('=> Serie Estacionaria')
        elif type == 'kpss':
            print('=> Serie No Estacionaria')