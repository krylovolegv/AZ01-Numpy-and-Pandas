import pandas as pd

df = pd.read_csv('Large language models (2024).csv', encoding='latin1')
print(df.describe())
print(df.info())
print(df.head())
print(df.tail())