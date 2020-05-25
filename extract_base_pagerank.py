import argparse
import src

parser = argparse.ArgumentParser(description='Compute perturbed pagerank for virus-human PPI networks.')
parser.add_argument('--result', dest="result", type=str, help='Complete path to result generated from perturbed pagerank.')
args = parser.parse_args()

filename = args.result
raw = src.io.load_variable_with_pickle(filename)

base = raw['Base-PageRank']

src.io.export_variable_with_pickle(base, filename.replace('.pkl', '_Base_PageRank.pkl'))


