import pandas as pd
import numpy as np
import src

def extract_pagerank_results(result_dict, perturbed_prots):
    perturbation_df = pd.DataFrame(columns=['Perturbation'] + perturbed_prots)

    perturbations = set(result_dict.keys())
    perturbations.remove('Base-PageRank')

    perturbation_df['Perturbation'] = list(result_dict.keys())

    for p in perturbed_prots:
        perturbation_df[p] = perturbation_df['Perturbation'].apply(
            lambda x: src.pagerank.div_pagerank(result_dict[x][p],
                                                result_dict['Base-PageRank'][p]
                                                ))

    perturbation_df.set_index('Perturbation', inplace=True)
    perturbation_df = perturbation_df.apply(np.log2)
    return perturbation_df