# Import Section

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt    # .pyplot is needed to pull functions like plt.plot() & plt.show()

# Data Section

np.random.seed(42)
n = 500
noise = np.random.randn(n) * 20000

df = pd.DataFrame({
    "size_sqft": np.random.randint(500, 3500, n)
})

df["price"] = (df["size_sqft"] * 200) + (df["size_sqft"] ** 2 * 0.05) + noise

# Define X and y and our 'train and test split'

X = df[["size_sqft"]]
y = df["price"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # random_state split will be consistent each time we run it.

# Model Section

model = LinearRegression()                # Our training on Regular Data
model.fit(X_train, y_train)

rf_model = RandomForestRegressor()       # Our training on Rf Data
rf_model.fit(X_train, y_train)

# Predictions Section

linear_predictions = model.predict(X_test)
linear_train_predictions = model.predict(X_train)

rf_predictions = rf_model.predict(X_test)
rf_train_predictions = rf_model.predict(X_train)

# Predictions

print("Linear Regression")
print(f"    R2:  {r2_score(y_test, linear_predictions):.2f}")
print(f"    MAE: {mean_absolute_error(y_test, linear_predictions):.2f}")

print("Random Forest Regressor")
print(f"    R2:  {r2_score(y_test, rf_predictions):.2f}")
print(f"    MAE: {mean_absolute_error(y_test, rf_predictions):.2f}")

# Graph generation

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color="gray", alpha=0.5, label="Actual Data")

sorted_idx = X_test["size_sqft"].argsort()
X_sorted = X_test.iloc[sorted_idx]

plt.plot(X_sorted, model.predict(X_sorted), color="red", label="Linear")
plt.plot(X_sorted, rf_model.predict(X_sorted), color="blue", label="Random Forest Regressor")

plt.xlabel("Size (sqft)")
plt.ylabel("Price ($)")
plt.title("Linear vs RandomForest Regressor")
plt.legend()
plt.show()
