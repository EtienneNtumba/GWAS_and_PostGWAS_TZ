import pandas as pd
from sklearn.linear_model import LassoCV
from sklearn.ensemble import RandomForestRegressor

# Load association results
assoc_results = pd.read_csv("results/association_results.txt", delim_whitespace=True)

# Select SNPs with p-values below threshold
significant_snps = assoc_results[assoc_results['P'] < 1e-5]

# Save selected SNPs
significant_snps[['SNP']].to_csv("results/selected_features.txt", index=False)

