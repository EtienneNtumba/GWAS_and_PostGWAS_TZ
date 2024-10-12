#!/usr/bin

# Create the Conda environments
conda env create -f envs/plink.yaml
conda env create -f envs/ml.yaml

# Activate environment and run the pipeline
snakemake --use-conda --cores 4

