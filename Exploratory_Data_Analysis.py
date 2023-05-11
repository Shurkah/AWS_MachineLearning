import pandas as pd
import matplotlib.pyplot as plt

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
df = pd.DataFrame(data=dataset)


# Output the dataframe to a csv for backup.
df.to_csv()


# Always good to make sure your data look correct
print(df.head())


# Output basic statistical metrics (count, mean, std, min, max, and percentiles).
print(df.describe())


# Create the correlation matrix of the 4 features.

# df.corr() in Jupyter Notebooks is enough
df['date'] = df['date'].apply(lambda x: float(x.split()[0].replace('2021-01-', '')))
corr = df.corr()
print(corr)


# Create a histogram plot using pandas or matplotlib.
hst = df.hist()
plt.show()