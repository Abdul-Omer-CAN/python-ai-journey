## Machine Learning ##

# 3 types of Machine Leaning a) Supervised b)  Unsupervised(No labels find patterns yourself)
#  c)Reinforcement(trial,error,reward - like a trading bot learning to buy and sell, gets better or self driving car
# that gets better, gets penalised for crashes and eventually learns how to drive safely)

# We will five dive into Supervised -> has 2 types a) Classification which is basically Yes or No
# & Regression which predicts a number
# How does a machine learn it uses these 3 steps:
# Makes a prediction...Measures the Error...Adjusts...Then repeats it a thousand times to be better and accurate.
# ^ This is called the "training model"

# In ML we split data into 2 sets: 1set is called -> Training set(80%) second one is -> Test set(20%)
# The model never sees the test set during the training set. Its like a child practising & then final exam is differ.
# Every training model has a train & test split.
# In machine learning x is what you input in it or teach it and y is what it predicts aka output.

# Example ->  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Over here 'x train' is the feature model learns from & 'y train' is the answers during training.
# 'x test' is the features for testing and 'y test' is the real answers to check

#### In depth example ###
# Another way to look at it - model looks at one row of x_train and predicts the answer and checks it against
# 'y_train' it asks itself am i right or wrong and by how much and then it makes adjustments automatically.
# It then repeats it for e.g for all 800 rows over and over again reducing its wrongness each time.
# And then when testing it will only get 'x_test' no peaking at 'y_test' and then YOU compare the answers using
# a line of code in scikit-learn.


## Question ##

# If a model gets 95% accuracy on training data but only 60% on test data, what does that tell you?
# that tells us the ML is overfitting meaning the model memorized the training data instead of learning the patterns. e.g
# it got 95% because it memorized all 800 examples and got 60% on test data because it did not learn the pattern!
# The opposite is called underfitting where it performs poorly in both training and test data. like a student who did not study at all.
