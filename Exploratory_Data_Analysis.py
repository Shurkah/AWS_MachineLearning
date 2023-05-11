import numpy as np
import pandas as pd

dataset = [
    {"date": "2021-01-01", "ice_cream_type": 1, "topping": 1, "location": 1},
    {"date": "2021-01-01", "ice_cream_type": 2, "topping": 1, "location": 2},
    {"date": "2021-01-01", "ice_cream_type": 1, "topping": 2, "location": 2},
    {"date": "2021-01-01", "ice_cream_type": 3, "topping": 1, "location": 1},
    {"date": "2021-01-01", "ice_cream_type": 1, "topping": 2, "location": 2},
    {"date": "2021-01-01", "ice_cream_type": 1, "topping": 2, "location": 2},
    {"date": "2021-01-01", "ice_cream_type": 1, "topping": 1, "location": 1},
    {"date": "2021-01-02", "ice_cream_type": 1, "topping": 1, "location": 1},
    {"date": "2021-01-02", "ice_cream_type": 3, "topping": 3, "location": 1},
    {"date": "2021-01-02", "ice_cream_type": 3, "topping": 2, "location": 2},
    {"date": "2021-01-02", "ice_cream_type": 2, "topping": 3, "location": 2},
    {"date": "2021-01-02", "ice_cream_type": 2, "topping": 3, "location": 2},
    {"date": "2021-01-02", "ice_cream_type": 3, "topping": 1, "location": 1},
    {"date": "2021-01-02", "ice_cream_type": 1, "topping": 2, "location": 2},
]

# Given the dataset above, please create a pandas dataframe.
df = pd.dataset()

# Output the dataframe to a csv for backup.
df.to_csv()

# Always good to make sure your data look correct
df.head()

# Output basic statistical metrics (count, mean, std, min, max, and percentiles).
print(df.describe())

# Create the correlation matrix of the 4 features.
print(df.corr())

# Create a histogram plot using pandas or matplotlib.
df.hist()