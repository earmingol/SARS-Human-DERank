# Finding important human genes for SARS-CoV-2 infection
## Project for the course *Networks Biology and Medicine* @ UC San Diego

Search of important genes for viral infection given a
[SARS-Cov-2 - Human protein interaction network](https://www.nature.com/articles/s41586-020-2286-9),
[Human interaction network](https://doi.org/10.1016/j.cell.2015.06.043),
[transcriptomics](https://doi.org/10.1101/2020.05.05.079194) and 
[proteomics data](https://www.nature.com/articles/s41586-020-2332-7).

This search is based on deleting each of the genes in the human interaction network and observing
the perturbation on the PageRank values for each of the viral proteins.