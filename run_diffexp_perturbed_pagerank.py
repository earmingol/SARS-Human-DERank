import argparse
import src

import networkx as nx
import numpy as np

parser = argparse.ArgumentParser(description='Compute perturbed pagerank for virus-human PPI networks.')
parser.add_argument('-t', dest="threads", default=1, type=int, help='Number of threads. By default, it uses 1.')
parser.add_argument('--output', dest='output', type=str, help='Complete path for output file')
parser.add_argument('--virus', dest='virus', type=str, help='Complete path for CX file containing virus-human PPI network')
parser.add_argument('--human', dest='human', type=str, help='Complete path for CX file containing human PPI network')
parser.add_argument('--de', dest='diffexp', type=str, help='Complete path for pickle file containing dict with fold changes for differentially expressed genes/prots')
args = parser.parse_args()

# Setup
threads = args.threads
output = args.output
virus = args.virus
human = args.human
diffexp = args.diffexp

if __name__ == "__main__":
    # Load files
    humannet = src.io.load_cx_network(human,
                                      network_mode='undirected',
                                      print_stats=True)

    virusnet = src.io.load_cx_network(virus,
                                      network_mode='undirected',
                                      print_stats=True)

    # Merge networks
    virus_human = nx.compose(humannet, virusnet)

    # Personalization
    perso = src.io.load_variable_with_pickle(diffexp)
    vals = [v for v in perso.values()]
    median = np.nanmedian(vals)

    node_perso = dict()
    for n in virus_human.nodes:
        if n in perso.keys():
            node_perso[n] = perso[n]
        else:
            node_perso[n] = median

    # Run Perturbed PageRank
    sars_prots = src.SARS_PROTS

    print('Running Basal PageRank (without perturbation)')
    base_pagerank= nx.algorithms.link_analysis.pagerank(virus_human,
                                                        nstart=node_perso,
                                                        personalization=node_perso)

    print('Running Perturbed PageRank')
    perturbed_pagerank = src.pagerank.run_perturbed_pagerank(G=virus_human,
                                                             nodes=set(virus_human.nodes) - set(sars_prots),
                                                             n_jobs=threads,
                                                             nstart=node_perso,
                                                             personalization=node_perso
                                                             )

    perturbed_pagerank['Base-PageRank'] = base_pagerank

    src.io.export_variable_with_pickle(perturbed_pagerank, output)