# Import section

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline       # combines scaling and the model so cross validation scales properly

# Data section

np.random.seed(42)
n = 500

df = pd.DataFrame({
    "salary": np.random.randint(30000, 120000, n),
    "credit_score": np.random.randint(300, 800, n),
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
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model

model = KNeighborsClassifier(n_neighbors=10)
model.fit(X_train, y_train)

# Evaluate

predictions = model.predict(X_test)     # It does the predicting
train_predictions = model.predict(X_train)


accuracy = accuracy_score(y_test, predictions)               # Does the accuracy testing comparing it to the y answer sheet for each
train_accuracy = accuracy_score(y_train, train_predictions)

# PRINT

print(f" Training accuracy: {train_accuracy:.2f}")
print(f" Testing accuracy: {accuracy:.2f}")


# Cross Validation


pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=10))
])

scores = cross_val_score(pipeline, X, y, cv=5)  # We pass X,y not x_train or y_train because cross validation does its own  splitting
print(f"CV Average accuracy: {scores.mean():.2f}")
print(f"CV Standard deviation: {scores.std():.2f}")

# Again Cross Validation does not need us to pre split data,it takes the full dataset and does the splitting itself. hence why we use X, y.
# cv is the number of times it runs the data and it takes different chunks of it each time it runs.


# To summarize Cross validation is better than single test split because it takes different chunks and tests vs single test split where for example your
# test size is 0.2 and that 0.2 could all be a concept you understand not evenly spread resulting in a big fat 'F'. You might get lucky with easy or
# unlucky with hard questions.
