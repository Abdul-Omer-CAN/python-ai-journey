# Import Section

import pandas as pd  # Needed for all
import numpy as np   # Needed for all
from sklearn.metrics import accuracy_score  # Needed for All
from sklearn.model_selection import train_test_split, cross_val_score  # Cross val splits the data into K folds and trains and test the model K times on splits.
from sklearn.tree import DecisionTreeClassifier  # For decisiontree
from sklearn.ensemble import RandomForestClassifier  # For randomforest
from sklearn.neighbors import KNeighborsClassifier  # for KNN
from sklearn.preprocessing import StandardScaler  # for KNN because it needs scaling and distance.


# Data Section

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])  # ".drop(columns=)" -> means drop the following columns.
df["Age"] = df["Age"].fillna(df["Age"].mean())  # .fillna goes through each row and where it says NaN it fills it with in our case mean.
df["Embarked"] = df["Embarked"].fillna("S")  # Same here 2 missing values aka NaN so fill with 'S' because its the most common port to board the titanic

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

# Features and target

X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y = df["Survived"]

# Train Test split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model & Fit section

model1 = DecisionTreeClassifier(random_state=42)
model2 = RandomForestClassifier(random_state=42)
model3 = KNeighborsClassifier(n_neighbors=10)

model1.fit(X_train, y_train)
model2.fit(X_train, y_train)
model3.fit(X_train, y_train)

# Evaluation Section

predictions_model1 = model1.predict(X_test)
train_predictions_model1 = model1.predict(X_train)
train_accuracy_model1 = accuracy_score(y_train, train_predictions_model1)
accuracy_model1 = accuracy_score(y_test, predictions_model1)

predictions_model2 = model2.predict(X_test)
train_predictions_model2 = model2.predict(X_train)
train_accuracy_model2 = accuracy_score(y_train, train_predictions_model2)
accuracy_model2 = accuracy_score(y_test, predictions_model2)

predictions_model3 = model3.predict(X_test)
train_predictions_model3 = model3.predict(X_train)
train_accuracy_model3 = accuracy_score(y_train, train_predictions_model3)
accuracy_model3 = accuracy_score(y_test, predictions_model3)

# Print Section

print("DecisionTree")
print(f" Test accuracy: {accuracy_model1:.2f}")
print(f" Train Accuracy: {train_accuracy_model1:.2f}")

print("RandomForest")
print(f" Test Accuracy: {accuracy_model2:.2f}")
print(f" Train Accuracy: {train_accuracy_model2:.2f}")

print("KNN")
print(f" Test Accuracy: {accuracy_model3:.2f}")
print(f" Train Accuracy: {train_accuracy_model3:.2f}")


# DecisionTree is overfitting badly.
# RandomForest Slightly overfitting. It does memorize data but also generalizes better.
# KNN Minimal Overfitting. Because it chooses the nearest K neighbors so result is more smoother. Its a simple look around me algorithm. Does not capture algo like RandomForest does.
