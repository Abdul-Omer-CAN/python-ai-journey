# Too many features(e.g a 100) makes a model worse this is called curse of dimensionality. It will result in slower computing speed.
# We cant plot more than 2 or 3 features. Having a 100 features is just absurd & also too much noise. PCA Solves this by compressing
# it like a zip file and compresses the 100 features for e.g into 2-3 super features.


# We will Learn PCA aka Principal Component Analysis

# Import Section

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Data Section

np.random.seed(42)
n = 300

df = pd.DataFrame({
    "feature_1": np.random.randint(1, 50, n),
    "feature_2": np.random.randint(100, 500, n),
    "feature_3": np.random.randint(1000, 3000, n),
    "feature_4": np.random.randint(3500, 50000, n),
    "feature_5": np.random.randint(10, 1000, n),
    "feature_6": np.random.randint(100, 500, n),
    "feature_7": np.random.randint(10000, 500000, n),
    "feature_8": np.random.randint(100000, 50000000, n),
    "feature_9": np.random.randint(1, 2, n),
    "feature_10": np.random.randint(4, 8, n),
})

# Features & Target

X = df
scaler = StandardScaler()  # Creates the StandardScaler tool
X_scaled = scaler.fit_transform(X)  # '.fit' learns the mean and standard deviation. 'transform' scales all of our features on the same scale.
# PCA will treat all features equally because of our X_scaled arguments.

# PCA Code

pca = PCA(n_components=2)
x_pca = pca.fit_transform(X_scaled)  # '.fit' here learns which data in our set has the most variation. 'transform' then compresses our 10 features into
# 2 principal components.


# Plot

plt.scatter(x_pca[:, 0], x_pca[:, 1], alpha=0.5, color="blue")  # [:, 0] is our princip comp 1 at column 0 and [:, 1] is our princip comp 2 at column 1
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - 10 Features compressed to 2")
plt.show()


# Print OPTIONAL to show how much info each component captured.

print(f" Explained Variance: {pca.explained_variance_ratio_}")
