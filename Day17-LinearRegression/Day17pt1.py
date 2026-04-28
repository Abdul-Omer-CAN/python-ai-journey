# Import Section

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


# Data section

np.random.seed(42)
n = 500

df = pd.DataFrame({
    "size_sqft": np.random.randint(500, 3500, n),
    "bedrooms": np.random.randint(1, 6, n),
    "location_score": np.random.uniform(1, 10, n),        # Gives us floats
    "age_years": np.random.randint(1, 50, n),
})

noise = np.random.randn(n) * 100000

df["price"] = (df["size_sqft"] * 200) + (df["bedrooms"] * 15000) + (df["location_score"] * 30000) - (df["age_years"] * 8000) + noise

# Features and Target

X = df[["size_sqft", "bedrooms", "location_score", "age_years"]]
y = df["price"]

# Our train test split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Model

model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate

predictions = model.predict(X_test)
train_predictions = model.predict(X_train)


# Print

print(f"R2 Score : {r2_score(y_test, predictions):.2f}")
print(f"Mean absolute: {mean_absolute_error(y_test, predictions):.2f}")
print(f"Mean Squared:  {mean_squared_error(y_test, predictions):.2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, predictions)):.2f}")  # np means from the numpy tools

for feature, coef in zip(model.feature_names_in_, model.coef_):   # model.feature_name_in learns the column names because of model.fit()
    print(f"[{feature}: {coef:.2f}]")                             # the numbers the model learnt 200,15000,30000,-8000
# print feature and coef to 2 decimal place.
# feature is assigned to model.feature_names_in and coef is assigned to model.coef_. it loops so feature first loop might be  "size_sqft" second
# might be coef = 200. feature second loop might be bedrooms with coef  15000 etc..

# Definitions

# R2 is the variation in price higher is perfect upto a max value of 1. Lower is terrible upto a lowest value of 0.
# MAE(Mean Absolute Error) on average how many dollars off is each prediction.
# MSE(Mean squared Error) Like MAE but squares the errors punishing the big mistakes.
# RMSE(Root mean squared Error) square root of MSE, brings it back to dollar terms by squaring it so that its readable.
# Gradient descent - model makes a random guess for each multiplier - checks how wrong it was and rinse and repeat adjusts accordingly in the
# right direction repeats thousands times until error is fully minimized. like a rolling ball rolling down a hill until it reaches the lowest point
# where it has the lowest error.
