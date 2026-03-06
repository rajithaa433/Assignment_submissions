import pandas as pd

# Load dataset and set order_id as index
# df = pd.read_csv("orders.csv", index_col="order_id")
df = pd.read_csv("Pandas/orders.csv", index_col="order_id")
# Display first 5 rows
df.head()

# Display last 5 rows
df.tail()

##Task 2 — Structural Inspection

df.info()
df.info()
df.shape
df.isnull().sum()

df['order_date'] = pd.to_datetime(df['order_date'])

# Task 3 — Statistical Summary

df.describe()
df['unit_price'].skew()
