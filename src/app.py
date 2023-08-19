import json

def read_input():
    """Get user input from command line

    Returns
    -------
    dictionary
        user input
    """
    valid_probe_types = [
        '6_15',
        '4_20',
    ]
    valid_probe_types_print_form = ', '.join(valid_probe_types)
    while True:
        print("Probe count:", end=' ')
        probe_count = input()

        if not probe_count.isdigit():
            print(f'Probe count must be integer. Your value is {probe_count}')
            continue

        print("Probe Type:", end=' ')
        probe_type = input()

        if not probe_type in valid_probe_types:
            probe_count_error = f'Probe type not valid. Your value is: {probe_type}'
            probe_type_error = f'Valid options must be one of: {valid_probe_types_print_form}'
            print(f'{probe_count_error}. {probe_type_error}')
            continue

        probe_count = int(probe_count)
        print(f'Probe count: {probe_count}')
        print(f'Probe type: {probe_type}')
        break

    return {
        'probe_count': probe_count,
        'probe_type': probe_type,
    }

def get_trodes_conf(size):
    """Get trodes configuration
    Parameters
    ----------
    size : str
        size of the configuration

    Returns
    -------
    dict
        dictionary of configuration
    """
    trodes_conf_file = ''
    trodes_configuration = {}
    match size:
        case '4_20':
            trodes_conf_file = 'src/base_conf_4_20.json'
        case '6_15':
            trodes_conf_file = 'src/base_conf_6_15.json'
        case _:
            raise ValueError(f'{size} is not supported')
    with open(trodes_conf_file, encoding='utf-8') as json_file:
        trodes_configuration = json.load(json_file)
    return trodes_configuration

if __name__ == '__main__':
    user_input = read_input()
    trodes_conf = get_trodes_conf(user_input['probe_type'])
