import argparse
import src

parser = argparse.ArgumentParser(description='Compute perturbed pagerank for virus-human PPI networks.')
parser.add_argument('--result', dest="result", type=str, help='Complete path to result generated from perturbed pagerank.')
args = parser.parse_args()

filename = args.result
raw = src.io.load_variable_with_pickle(filename)

sars_prots = src.SARS_PROTS
base_df = src.result_processing.extract_pagerank_results(raw, sars_prots)

base_df.to_csv(filename.replace('.pkl', '.csv'))


