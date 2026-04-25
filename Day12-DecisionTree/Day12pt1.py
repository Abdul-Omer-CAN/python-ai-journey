from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

np.random.seed(42)   # generates random numbers but w/ seed(42) it keeps them the same each run

n = 500

df = pd.DataFrame({
    "salary": np.random.randint(30000, 120000, n),
    "credit_score": np.random.randint(300, 850, n),
    "loan_amount": np.random.randint(5000, 50000, n),  # np.random.randint() generates random whole numbers
    "loan_term": np.random.randint(12, 60, n),
    "debt_to_income": np.random.uniform(0.1, 0.9, n),  # np.random.uniform generates random decimal numbers
})

df["defaulted"] = ((df["credit_score"] < 550) | (df["debt_to_income"] > 0.7)).astype(int)  # '|' means OR.
# In eng for ^ person defaulted i credit score less than 550 and debt to income greater than 0.7
# astype(int) converts true/false to 0/1 because ML models needs numbers not booleans.

print(df.head())  # Returns a dataframe object requires print() in =-Jupyter notebooks print() is not required for the last line of fxn.

X = df[["salary", "credit_score", "loan_amount", "loan_term", "debt_to_income"]]  # 5 questions that the model can ask are the variables!
y = df["defaulted"]

print(X.shape)  # Gives us the features of X - which is 500 rows of people and 5 columns
print(y.shape)  # this wont print 1 becuase it is a series aka only a single column


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


print(X_train.shape)
print(X_test.shape)


model = LogisticRegression(max_iter=1000)  # If () left empty it defaults to 100 iterations
model.fit(X_train, y_train)  # model.fit() is where the learning happens! makes a prediction against x_train and compares w/ y_train.
# & repeats multiple times to get better! This line is ^ is super imp! it is were all the learning happens.


predictions = model.predict(X_test)  # With this line of code it will make prediction using model.predict()
accuracy = accuracy_score(y_test, predictions)  # Compares prediction against against real answers
print(f"Model accuracy: {accuracy:.2f}")  # Gives us a 2 decimal output


# Summarize today: We loaded data -> defined X and y -> Train/test split -> Train model -> Predict then Accuracy.
