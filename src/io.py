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