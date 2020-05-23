import networkx as nx
import numpy as np

from joblib import delayed
from src.parallelization import ProgressParallel

def pagerank(G, algorithm='default', **kwargs):
    if algorithm == 'default':
        return nx.algorithms.link_analysis.pagerank(G, **kwargs)
    elif algorithm == 'numpy':
        return nx.algorithms.link_analysis.pagerank_numpy(G, **kwargs)
    elif algorithm == 'google_matrix':
        return nx.algorithms.link_analysis.google_matrix(G, **kwargs)
    elif algorithm == 'scipy':
        return nx.algorithms.link_analysis.pagerank_scipy(G, **kwargs)
    else:
        raise ValueError('Not a correct algorithm')


def compute_perturbed_pagerank(G, node, *args):
    H = G.copy()
    H.remove_node(node)
    return pagerank(H, *args)


def run_perturbed_pagerank(G, nodes=None, n_jobs=1, **kwargs):
    if nodes is None:
        nodes = list(set(G))
    else:
        nodes = list(set(nodes))

    result = ProgressParallel(n_jobs=n_jobs, total=len(nodes))(delayed(compute_perturbed_pagerank)(G, n, **kwargs) for n in nodes)
    perturbed_page_rank = dict(zip(nodes, result))
    return perturbed_page_rank


def div_pagerank(perturbed, normal):
    if normal == 0.:
        return np.nan
    else:
        return(perturbed/normal)


def calculate_alpha(network, m=-0.02935302, b=0.74842057):
    '''Taken from
    https://github.com/idekerlab/Network_Evaluation_Tools/blob/master/network_evaluation_tools/network_propagation.py'''
    log_edge_count = np.log10(len(network.edges()))
    alpha_val = round(m*log_edge_count+b,3)
    if alpha_val <=0:
        raise ValueError('Alpha <= 0 - Network Edge Count is too high')
        # There should never be a case where Alpha >= 1, as avg node degree will never be negative
    else:
        return alpha_val