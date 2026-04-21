from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

df = pd.DataFrame({
    "salary": np.random.randint(30000, 120000, n),    # min value, max value, n is the amount of numbers to generate!
    "credit_score": np.random.randint(300, 850, n),
    "loan_amount": np.random.randint(5000, 50000, n),
    "loan_term": np.random.randint(12, 60, n),
    "debt_to_income": np.random.uniform(0.1, 0.9, n),
})


df["defaulted"] = ((df["credit_score"] < 550) | (df["debt_to_income"] > 0.7)).astype(int)

print(df.head())

X = df[["salary", "credit_score", "loan_amount", "loan_term", "debt_to_income"]]

y = df["defaulted"]

print(X.shape)

print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)

model = DecisionTreeClassifier(random_state=42, max_depth=3)  # Key note is that we are using DecisionTreeClassifier here not Regressor
model.fit(X_train, y_train)  # Learning Phase
# ^ THIS IS THE DIFFERENCE BETWEEN TRAIN AND TEST. With train it can go back and forth and train itself!

train_predictions = model.predict(X_train)   # makes predictions using the training set just to check how well it learnt
train_accuracy = accuracy_score(y_train, train_predictions)  # compares predictions against answers

predictions = model.predict(X_test)    # makes predictions with the actual test now!
accuracy = accuracy_score(y_test, predictions)  # compares prediction against answers

print(f"Training accuracy: {train_accuracy:.2f}")
print(f"Test accuracy: {accuracy:.2f}")

plt.figure(figsize=(10, 10))
plot_tree(model, max_depth=3, feature_names=["salary", "credit_score", "loan_amount", "loan_term", "debt_to_income"],
          class_names=["no default", "default"],
          filled=True, rounded=True)
plt.title("Loan Default Decision Tree")
plt.show()
