# Import section

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Data section

np.random.seed(42)
n = 500

df = pd.DataFrame({
    "salary": np.random.randint(30000, 120000, n),
    "credit_score": np.random.randint(300, 850, n),
    "loan_amount": np.random.randint(5000, 50000, n),
    "loan_term": np.random.randint(12, 60, n),
    "debt_to_income": np.random.uniform(0.1, 0.9, n),
})

df["defaulted"] = ((df["credit_score"] < 550) | (df["debt_to_income"] > 0.7)).astype(int)


# Features and target

X = df[["salary", "credit_score", "loan_amount", "loan_term", "debt_to_income"]]
y = df["defaulted"]


# Our train test split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # .fit_transform learns the new scaling because it is a X_train
X_test = scaler.transform(X_test)  # .transform implements what it learnt from .fit_transform to the test

# Model

model = KNeighborsClassifier(n_neighbors=10)
model.fit(X_train, y_train)

# Evaluate

predictions = model.predict(X_test)
train_predictions = model.predict(X_train)

accuracy = accuracy_score(y_test, predictions)
train_accuracy = accuracy_score(y_train, train_predictions)


# PRINT

print(f"Training accuracy: {train_accuracy:.2f}")
print(f"Test accuracy: {accuracy:.2f}")
