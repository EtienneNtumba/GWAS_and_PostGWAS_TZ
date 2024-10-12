import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Conv1D, Flatten
from sklearn.model_selection import train_test_split
import pickle

# Load selected features and phenotype data
features = pd.read_csv("results/selected_features.txt")
phenotypes = pd.read_csv("data/phenotypes/your_phenotype_data.txt")

# Merge data
data = pd.merge(features, phenotypes, on='SNP')
X = data.drop('phenotype', axis=1)
y = data['phenotype']

# Reshape data for CNN
X = X.values.reshape(X.shape[0], X.shape[1], 1)

# Build CNN model
model = Sequential()
model.add(Conv1D(64, 2, activation='relu', input_shape=(X.shape[1], 1)))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile and train model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10, batch_size=32)

# Save model to file
model.save("results/deep_learning_model.h5")

