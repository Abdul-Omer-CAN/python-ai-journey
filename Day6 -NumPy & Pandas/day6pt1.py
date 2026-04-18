# Today we learn a NumPy and Pandas

# NumPy -> fast mathematical operations on array of numbers
# Pandas -> Working with tables of data (like excel but in python)

# import numpy as np
# import pandas as pd

# print("NumPy version:", np.__version__)
# print("Pandas version:", pd.__version__)


# New exercise
# Think of python as basic tools like (print, input, len etc.)
import numpy as np  # Think of numpy as specialized math tools (meax, max, array etc)
# Think of pandas as specialized data tools (Dataframes, CSV reading etc)
prices = np.array([182.50, 141.20, 245.80, 378.90, 156.30])

print(prices)
print("Mean price:", np.mean(prices))
print("Max price:", np.max(prices))
print("Min price", np.min(prices))
print("Total:", np.sum(prices))


quantities = np.array([10, 5, 8, 3, 7])          # Multiplies each number by 10
values = prices * quantities
print(values)

yesterday_prices = np.array([180.00, 139.50, 250.00, 375.00, 152.00])
pct_change = ((prices - yesterday_prices) / yesterday_prices) * 100
print(pct_change.round(2))  # .round() means round to () decimal place in our case 2

# NEW NumPy fxns learnt TODAY:
# import numpy as _____
# np.array([...])
# np.mean(array)
# np.max(array)
# np.min(array)
# np.sum(array)
# array.round(2)
# array * array
# array - array
