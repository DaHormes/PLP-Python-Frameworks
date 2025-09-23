
# part1_exploration.py
import pandas as pd

# Load the dataset (use just metadata.csv from Kaggle)
df = pd.read_csv("metadata.csv")

# Preview first rows
print(df.head())

# Shape of dataset
print("Shape:", df.shape)

# Column info
print(df.info())

# Missing values
print(df.isnull().sum().head(20))  # only first 20 cols for readability

# Basic statistics
print(df.describe())
