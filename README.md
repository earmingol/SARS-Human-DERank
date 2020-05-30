# Finding important human genes for SARS-CoV-2 infection
## Project for the course *Networks Biology and Medicine* @ UC San Diego

Search of important genes for viral infection given a
[SARS-Cov-2 - Human protein interaction network](https://www.nature.com/articles/s41586-020-2286-9),
[Human interaction network](https://doi.org/10.1016/j.cell.2015.06.043),
[transcriptomics](https://doi.org/10.1101/2020.05.05.079194) and 
[proteomics data](https://www.nature.com/articles/s41586-020-2332-7).

This search is based on deleting each of the genes in the human interaction network and observing
the perturbation on the PageRank values for each of the viral proteins.

## Installation

First, clone/download this repo and go into its directory. Then:

* Generate a anaconda environment:

```
conda create -n pagerank -y python=3.7 jupyter
```

* Activate the environment:

```
conda activate pagerank
```

* Install dependencies:

```
pip install -r ./requirements.txt
```

## Running the analysis
### For running the analysis without omics data
 * For example, run the analysis using 8 cores:
```
python run_perturbed_pagerank.py -t 8 --output ./PPR-results.pkl --virus ./inputs/SARS-CoV-2-Host-Pathogen-Interaction.cx --human ./inputs/BioPlex2.0.cx
```
 
 ### For running the analysis with omics data
 * Integrating **transcriptomics data** (see how the file Transcriptomics-Personalization.pkl was generate
 in the jupyter notebook [Differential-Expression](./Differential-Expression.ipynb)) and using 8 cores
 
```
python run_perturbed_pagerank.py -t 8 --output ./PPR-Transcriptomics-results.pkl --virus ./inputs/SARS-CoV-2-Host-Pathogen-Interaction.cx --human ./inputs/BioPlex2.0.cx --de ./inputs/Transcriptomics-Personalization.pkl
```

 * Integrating **proteomics data** (see how the file Transcriptomics-Personalization.pkl was generate
 in the jupyter notebook [Differential-Expression](./Differential-Expression.ipynb)) and using 8 cores
 
```
python run_perturbed_pagerank.py -t 8 --output ./PPR-Proteomics-results.pkl --virus ./inputs/SARS-CoV-2-Host-Pathogen-Interaction.cx --human ./inputs/BioPlex2.0.cx --de ./inputs/Proteomics-Personalization.pkl
```

### For extracting Base-PageRank results (i.e. PageRank values for each node, without perturbing the network -*removing any node*-)
* Using any output from the previous analyses, run:

```
python extract_base_pagerank.py --result ./PPR-results.pkl
```

### For extracting Perturbed-PageRank results (i.e. fold changes for the base PageRank values of each viral protein after removing each of the other nodes in the network)
* Using any output from the previous analyses, run:

```
python pagerank_results_to_dataframe.py --result ./PPR-results.pkl
```