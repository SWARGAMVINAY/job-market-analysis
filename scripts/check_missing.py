import pandas as pd

df = pd.read_csv("data/postings.csv")

missing = df.isnull().sum()

print(missing.sort_values(ascending=False))