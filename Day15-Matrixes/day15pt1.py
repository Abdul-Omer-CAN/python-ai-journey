# Precision #

# When you say 'YES' how often are you right? | out of everyone the doctor said had cancer how many really did.
# When doctor says 'YES; you can trust him. ( This is high precision)
# Out of everyone the model flagged as for e.g 'default' how many actually defaulted. ak high precision model only says 'YES' when it is really sure.

# Recall #

# Out of all actual YES cases how many did we catch? | High recall means doctor caught all of the cases.
# Out of all people who defaulted - how many did the model catch? aka high recall model doesnt miss real cases

# Comparing the two #

# Precision is out of all the fish you caught how many were the right fish? AKA Quality
# Recall is out of all the right fish in the lake - how many did you catch? (Didnt miss any) AKA Quantity


## SUMMARIZE ##

# Accuracy is overall correctness
# Confusion matrix breaks down the 4 types of predictions [True +, False +, True -, False -]
# True + when model said yes client will default and client does.
# True - when model says no client will not default and client does not default.
# False +, when model said YES client will default but client doesnt.
# False - when model says no you wont default but client will.(most dangerous)


# Precision is Quality out of all the fish how many were right? checking quality
# Recall is Quantity out of all the right fish in the lake. How many did you catch? checking quantity of right
