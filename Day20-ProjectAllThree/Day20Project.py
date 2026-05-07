# Import Section

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# Data Section

np.random.seed(42)
n = 500
noise = np.random.randn(n) * 20000

df = pd.DataFrame({
    "size_sqft": np.random.randint(500, 3500, n),
    "bedrooms": np.random.randint(1, 6, n),
    "bathrooms": np.random.randint(1, 4, n),
    "location_score": np.random.uniform(1, 10, n),
    "age_years": np.random.randint(1, 50, n)
})

df["price"] = (df["size_sqft"] * 200) + (df["bedrooms"] * 15000) + (df["location_score"] * 30000) - (df["age_years"] * 8000) + noise

# Define X and y & our Train test Split

X = df[["size_sqft", "bedrooms", "bathrooms", "location_score", "age_years"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## OUR THREE MODELS ##

# Linear Model

model = LinearRegression()
model.fit(X_train, y_train)


# Polynomial Model

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

# RandomForest Model

rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)


## PREDICTIONS ##

# Linear:

linear_predictions = model.predict(X_test)
linear_train_predictions = model.predict(X_train)

# Polynomials:

poly_predictions = poly_model.predict(X_test_poly)
poly_train_predictions = poly_model.predict(X_train_poly)

# RandomForest:

rf_predictions = rf_model.predict(X_test)
rf_train_predictions = rf_model.predict(X_train)


## Print Section ##


print("Linear Regression")
print(f"    R2:{r2_score(y_test, linear_predictions):.2f}")
print(f"    MAE:{mean_absolute_error(y_test, linear_predictions):.2f}")

print("Polynomials Regression")
print(f"    R2:{r2_score(y_test, poly_predictions):.2f}")
print(f"    MAE:{mean_absolute_error(y_test, poly_predictions):.2f}")

print("RandomForest Regression")
print(f"    R2:{r2_score(y_test, rf_predictions):.2f}")
print(f"    MAE:{mean_absolute_error(y_test, rf_predictions):.2f}")
