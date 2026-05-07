# Import Section

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Data Section & Define X

np.random.seed(42)
n = 300

df = pd.DataFrame({
    "age": np.random.randint(18, 60, n),
    "income": np.random.randint(35000, 150000, n),
    "spending_score": np.random. randint(1, 100, n)
})

X = df[["age", "income", "spending_score"]]

# Elbow Method to find optimal 'K'

inertias = []

for k in range(1, 11):     # Loops K from 1 to 10
    kmeans = KMeans(n_clusters=k, random_state=42)  # KMeans(n_clusters=k) this creates a model with K clusters. Loops from 1 to 10.
    kmeans.fit(X)  # Fits on our X
    inertias.append(kmeans.inertia_)  # Afer fitting the data will add kmeans to inertia and '_' is imp it indicates attributes learnt after .fit().

plt.plot(range(1, 11), inertias)
plt.xlabel("K")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()


# Final KMeans Model

kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)
df["cluster"] = kmeans.labels_  # .labels_ means we are assigning  a cluster label e.g 0,1,2,3 to each customer. e.g customer 1 -> cluster 0,
# customer 2 -> cluster 2, customer 3 -> cluster 0 again.
# To summarize we have 300 customers because n=300 and they are sorted into 4 groups which means K=4. imagine 4 tables and 300 customers. each customer
# assigned their own table.


# Plotting
plt.scatter(df["income"], df["spending_score"], c=df["cluster"], cmap="viridis")  # c=df will give each cluster a color & cmap is colormap Viridis a builtin color scheme.
plt.xlabel("Income ($)")  # c= tells matplotlib what to color by which is by 'cluster' and cmap tells it what color to use.
plt.ylabel("Spending Score")
plt.title("Income vs Spending Score")
plt.colorbar()
plt.show()
