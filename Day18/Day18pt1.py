## Import Section ##

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

## Data Section ##

np.random.seed(42)
n = 500                             # randn(n) below follows normal distribution where the values cluster around central mean e.g zero.
noise = np.random.randn(n) * 20000  # Generates 500 random numbers around zero then '*' multiplies them by 20k to scale them upto dollar amounts.
df = pd.DataFrame({
    "size_sqft": np.random.randint(500, 3500, n),
})

df["price"] = (df["size_sqft"] * 200) + (df["size_sqft"] ** 2 * 0.05) + noise   # '** 2* 0.05' adds a slight curve to the data.
# the *200 is the price per sqft 200dollar per sq ft.
# ** 2 creates the curve in the data by squaring and it creates huge number and then by multiplying it with 0.05 scales it down for realistic values.


# Features & Targets

X = df[["size_sqft"]]  # Double brackets ALWAYS required for DataFrame. Single is for series.
y = df["price"]        # y is always one column aka series aka answer column. On the other hand X is double aka input table(can have multiple columns).

# Features & Targets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Model Section

model = LinearRegression()          # This one is training on Regular data
model.fit(X_train, y_train)

# Model Poly section - This is trained on transformed aka poly data

poly = PolynomialFeatures(degree=2)   # degree=2 will make it to the power of 2 aka squared featured.
X_train_poly = poly.fit_transform(X_train)  # poly mean it squares | .fit means it learns | _transform means it applies what it learnt.
X_test_poly = poly.transform(X_test)   # only transforms just like standardscaler no learning for test only apply what learnt from train.

poly_model = LinearRegression()       # regular linear regression model
poly_model.fit(X_train_poly, y_train)  # Train the model on the transformed data which is X_tain_poly

# Evaluate

linear_predictions = model.predict(X_test)
linear_train_predictions = model.predict(X_train)

poly_predictions = poly_model.predict(X_test_poly)
poly_train_predictions = poly_model.predict(X_train_poly)


# Print Section

print("Linear Regression")
print(f"   R2: {r2_score(y_test, linear_predictions):.2f}")
print(f"   MAE: {mean_absolute_error(y_test, linear_predictions):.2f}")


print("Polynomial Regression")
print(f"   R2:  {r2_score(y_test, poly_predictions):.2f}")
print(f"   MAE: {mean_absolute_error(y_test, poly_predictions):.2f}")

# Our graph

plt.figure(figsize=(10, 6))  # 10 inches wide and 6 inches tall

plt.scatter(X_test, y_test, color="gray", alpha=0.5, label="Actual Data")  # Alpha is the transparency of the dot which is 50 percent here.

# For Smooth Lines

sorted_idx = X_test["size_sqft"].argsort()  # argsort returns the indexes position from small to big. for e.g 5,10,15 - 5 is index 1, 10 is index 2 etc.
X_sorted = X_test.iloc[sorted_idx]  # does the actual reordering of X-test from smallest to biggest using the indexes given by argsort.
X_test_poly_sorted = poly.transform(X_sorted)  # transforms sorted x into polynomial features so poly_model can predict.

plt.plot(X_sorted, model.predict(X_sorted), color="red", label="Linear")  # draws the linear red line
plt.plot(X_sorted, poly_model.predict(X_test_poly_sorted), color="blue", label="Polynomial")  # draws a blue curved line

plt.xlabel("Size (sqft)")
plt.ylabel("Price ($)")
plt.title("Linear vs Polynomial Regression")
plt.legend()  # shows the color legend which line is which.
plt.show()  # Will display the plot


# iloc stands for index positions which does the actual sorting via argsort instructions.
# argsort stands for argument position which sorts from small to big using indexes
