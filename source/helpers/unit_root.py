def check_stationarity(p_value, threshold = 0.05, type='unit'):
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