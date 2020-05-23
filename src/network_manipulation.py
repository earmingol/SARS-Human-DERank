import networkx as nx


def print_network_info(G, label=''):
    if len(label) == 0:
        print('Network contains {} nodes and {} edges'.format(len(G.nodes),
                                                              len(G.edges)
                                                              ))
    else:
        print('Network {} contains {} nodes and {} edges'.format(label,
                                                                 len(G.nodes),
                                                                 len(G.edges)
                                                                 ))


def change_node_names(G, network_mode='undirected', dict_key='name', mapper=None):
    if network_mode == 'undirected':
        H = nx.Graph()
    elif network_mode == 'directed':
        H = nx.DiGraph()
    elif network_mode == 'multi-undirected':
        H = nx.MultiGraph()
    elif network_mode == 'multi-directed':
        H = nx.MultiDiGraph()
    else:
        raise ValueError('Not a valid network_mode')

    if mapper is None:
        nodes = [G.nodes[n][dict_key] for n in G.nodes]
        edges = [(G.nodes[e[0]][dict_key], G.nodes[e[1]][dict_key]) for e in G.edges]
    else:
        nodes = [mapper[n] for n in G.nodes]
        edges = [(mapper[e[0]], mapper[e[1]]) for e in G.edges]

    H.add_nodes_from(nodes)
    H.add_edges_from(edges)
    return H