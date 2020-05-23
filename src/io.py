import json
import pickle
import os

import ndex2
from src.network_manipulation import change_node_names, print_network_info


def load_cx_network(filename, mode='default', network_mode=None, dict_key='name', mapper=None, print_stats=False):
    net = ndex2.create_nice_cx_from_file(filename)
    G = net.to_networkx(mode=mode)
    if network_mode is not None:
        G = change_node_names(G, network_mode=network_mode, dict_key=dict_key, mapper=mapper)

    if print_stats:
        print_network_info(G)
    return G


def save_dict(d, filename):
    with open(filename, 'w') as outfile:
        json.dump(d, outfile)


def load_dict(filename):
    return json.load(filename)


def export_variable_with_pickle(variable, filename):
    '''
    Export a large size variable in a python readable way using pickle.
    '''

    max_bytes = 2 ** 31 - 1

    bytes_out = pickle.dumps(variable)
    with open(filename, 'wb') as f_out:
        for idx in range(0, len(bytes_out), max_bytes):
            f_out.write(bytes_out[idx:idx + max_bytes])
    print(filename, 'was correctly saved.')


def load_variable_with_pickle(filename):
    '''
    Import a large size variable in a python readable way using pickle.
    '''

    max_bytes = 2 ** 31 - 1
    bytes_in = bytearray(0)
    input_size = os.path.getsize(filename)
    with open(filename, 'rb') as f_in:
        for _ in range(0, input_size, max_bytes):
            bytes_in += f_in.read(max_bytes)
    variable = pickle.loads(bytes_in)
    return variable