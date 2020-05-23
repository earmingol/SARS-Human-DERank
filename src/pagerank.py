import networkx as nx
import numpy as np

from joblib import delayed
from src.parallelization import ProgressParallel

def pagerank(G, algorithm='default', *args):
    if algorithm == 'default':
        return nx.algorithms.link_analysis.pagerank(G, *args)
    elif algorithm == 'numpy':
        return nx.algorithms.link_analysis.pagerank_numpy(G, *args)
    elif algorithm == 'google_matrix':
        return nx.algorithms.link_analysis.google_matrix(G, *args)
    elif algorithm == 'scipy':
        return nx.algorithms.link_analysis.pagerank_scipy(G, *args)
    else:
        raise ValueError('Not a correct algorithm')


def compute_perturbed_pagerank(G, node, *args):
    H = G.copy()
    H.remove_node(node)
    return pagerank(H, *args)


def run_perturbed_pagerank(G, nodes=None, n_jobs=1, *args):
    if nodes is None:
        nodes = list(set(G))
    else:
        nodes = list(set(nodes))

    result = ProgressParallel(n_jobs=n_jobs, total=len(nodes))(delayed(compute_perturbed_pagerank)(G, n, *args) for n in nodes)
    perturbed_page_rank = dict(zip(nodes, result))
    return perturbed_page_rank


def div_pagerank(perturbed, normal):
    if normal == 0.:
        return np.nan
    else:
        return(perturbed/normal)