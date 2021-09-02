def check_unit_root_test(p_value, threshold = 0.05):
    print(f'p-value: {p_value:.2f}')
    print(f'p-threshold: {threshold}')
    if p_value > threshold:
        print('=> Serie Estacionaria')
    else:
        print('=> Serie No Estacionaria')