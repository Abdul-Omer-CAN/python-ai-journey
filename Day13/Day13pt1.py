# imports
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Data
np.random.seed(42)
n = 500

df = pd.DataFrame({
    "salary": np.random.randint(30000, 120000, n),
    "credit_score": np.random.randint(300, 850, n),
    "loan_amount": np.random.randint(5000, 50000, n),
    "loan_term": np.random.randint(12, 60, n),
    "debt_to_income": np.random.uniform(0.1, 0.9, n),      # .uniform because of decimals $ .randint is whole numbers only
})

df["defaulted"] = ((df["credit_score"] < 550) | (df["debt_to_income"] > 0.7)).astype(int)

# Features and target

X = df[["salary", "credit_score", "loan_amount", "loan_term", "debt_to_income"]]
y = df["defaulted"]

# train test split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model

model = RandomForestClassifier(n_estimators=500, random_state=42)
model.fit(X_train, y_train)    # This is waht compares the training answers with the answer sheet and learns

# Evaluate X_test and X_train

predictions = model.predict(X_test)
train_predictions = model.predict(X_train)

accuracy = accuracy_score(y_test, predictions)
train_accuracy = accuracy_score(y_train, train_predictions)

# Print

print(f"Training accuracy: {train_accuracy:.2f}")
print(f"Test accuracy: {accuracy:.2f}")

# Check features OPTIONAL

print(model.feature_importances_)
print(model.max_features)     # sqrt means square root fo the amount of features sqrt of 5 is 2.

## Key Changes being made this week is the middle import ##

# sklearn.linear_model   -> Logistic Regression
# sklearn.tree           -> Decision Tree
# sklearn.ensemble       -> Random Forest
# sklearn.neighbors      -> KNN
# sklearn.svm            -> SVM


# in line 33 adding more trees by n_estimators at one points is useless because it costs more computation time and gives you the
# same result.
