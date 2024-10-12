import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load selected features and phenotype data
features = pd.read_csv("results/selected_features.txt")
phenotypes = pd.read_csv("data/phenotypes/your_phenotype_data.txt")

# Merge data
data = pd.merge(features, phenotypes, on='SNP')
X = data.drop('phenotype', axis=1)
y = data['phenotype']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model to file
with open("results/machine_learning_model.pkl", 'wb') as f:
    pickle.dump(model, f)

